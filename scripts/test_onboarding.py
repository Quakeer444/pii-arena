"""Offline contract tests for the public onboarding layer; no model downloads."""
from __future__ import annotations

import argparse
import contextlib
import csv
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import onboarding as O


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.root_patch = patch.object(O, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        (self.root / "datasets").mkdir()
        (self.root / "datasets/samples.json").write_text('{"demo": ["a"]}\n')
        self.work = self.root / ".local/test"
        self.source = self.root / "provided"
        folder = self.source / "BENCH/demo"
        folder.mkdir(parents=True)
        with (folder / "bench.csv").open("w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            writer.writerow(["id", "domain", "text", "entities"])
            writer.writerow(["a", "test", "Alpha item", json.dumps([{"start": 0, "end": 5, "type": "NAME"}])])
        self.meta = {"lang": "en", "kind": "pii", "groups": {"NAME": "PERSON"}, "labels": {"en": ["person"]}}
        (folder / "meta.json").write_text(json.dumps(self.meta))
        self.item = {"id": "demo", "lang": "en", "kind": "pii", "groups": ["PERSON"], "source": "local test fixture",
                     "license": "test", "rows": 1, "characters": 10, "original_annotations": 1,
                     "bench_sha256": O.digest(folder / "bench.csv")}
        self.model = {"family": "hf", "repo": "example/model", "revision": "a" * 40, "contaminated": []}
        (self.root / "datasets/catalog.json").write_text(json.dumps([self.item]))
        (self.root / "benchmark").mkdir()
        (self.root / "benchmark/models.toml").write_text('[models.demo]\nfamily="hf"\nrepo="example/model"\nrevision="' + 'a' * 40 + '"\n')

    def import_data(self):
        return O.prepare(self.work, [self.item], self.source)

    def update_csv(self, text, entities, second=False):
        path = self.source / "BENCH/demo/bench.csv"
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            writer.writerow(["id", "domain", "text", "entities"])
            row = ["a", "test", text, json.dumps(entities)]
            writer.writerow(row)
            if second:
                writer.writerow(row)
        self.item["bench_sha256"] = O.digest(path)

    def test_missing_is_not_ready(self):
        self.assertEqual(O.check_dataset(self.work, self.item)["status"], "missing")

    def test_valid_input(self):
        self.assertEqual(O.check_dataset(self.source, self.item)["status"], "ready")

    def test_import_is_idempotent(self):
        self.assertEqual(self.import_data(), self.import_data())
        self.assertEqual(O.digest(self.work / "BENCH/samples.json"), O.digest(self.root / "datasets/samples.json"))

    def test_import_does_not_touch_source(self):
        before = O.digest(self.source / "BENCH/demo/bench.csv")
        self.import_data()
        self.assertEqual(before, O.digest(self.source / "BENCH/demo/bench.csv"))

    def test_hash_mismatch_blocks_import(self):
        self.item["bench_sha256"] = "f" * 64
        self.assertEqual(self.import_data()[0]["status"], "invalid")
        self.assertFalse((self.work / "BENCH/demo").exists())

    def test_selection_validated_before_any_promotion(self):
        bad = dict(self.item, id="missing")
        states = O.prepare(self.work, [self.item, bad], self.source)
        self.assertEqual([x["status"] for x in states], ["ready", "missing"])
        self.assertFalse((self.work / "BENCH/demo").exists())

    def test_existing_bad_data_is_not_overwritten(self):
        self.import_data()
        target = self.work / "BENCH/demo/bench.csv"
        target.write_text("changed")
        with self.assertRaises(ValueError):
            self.import_data()
        self.assertEqual(target.read_text(), "changed")

    def test_existing_different_metadata_is_not_overwritten(self):
        self.import_data()
        target = self.work / "BENCH/demo/meta.json"
        target.write_text(json.dumps(self.meta | {"labels": {"en": ["different"]}}))
        with self.assertRaises(ValueError):
            self.import_data()

    def test_frozen_samples_are_not_replaced(self):
        O.initialize(self.work)
        target = self.work / "BENCH/samples.json"
        target.write_text("{}")
        with self.assertRaises(ValueError):
            O.initialize(self.work)
        self.assertEqual(target.read_text(), "{}")

    def test_preserved_workspace_rejected(self):
        for name in ("research", "research/child"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                O.workspace(self.root / ".local" / name)

    def test_external_workspace_rejected(self):
        with self.assertRaises(ValueError):
            O.workspace(self.root / "public")

    def test_local_root_rejected(self):
        with self.assertRaises(ValueError):
            O.workspace(self.root / ".local")

    def test_symlink_escape_rejected(self):
        self.work.mkdir(parents=True)
        (self.work / "BENCH").symlink_to(self.source)
        with self.assertRaises(ValueError):
            O.workspace(self.work)

    def test_imported_file_symlink_escape_rejected(self):
        self.import_data()
        target = self.work / "BENCH/demo/bench.csv"
        target.unlink()
        target.symlink_to(self.source / "BENCH/demo/bench.csv")
        self.assertEqual(O.check_dataset(self.work, self.item)["status"], "invalid")

    def test_invalid_offsets(self):
        for start, end in ((-1, 5), (5, 5), (0, 99), (True, 5), (0.5, 5)):
            with self.subTest(start=start, end=end):
                self.update_csv("Alpha item", [{"start": start, "end": end, "type": "NAME"}])
                self.assertEqual(O.check_dataset(self.source, self.item)["status"], "invalid")

    def test_duplicate_ids(self):
        self.update_csv("Alpha item", [], second=True)
        self.assertEqual(O.check_dataset(self.source, self.item)["status"], "invalid")

    def test_missing_type_mapping(self):
        self.update_csv("Alpha item", [{"start": 0, "end": 5, "type": "MISSING"}])
        self.assertEqual(O.check_dataset(self.source, self.item)["status"], "invalid")

    def test_count_mismatch(self):
        for key in ("rows", "characters", "original_annotations"):
            with self.subTest(key=key):
                self.assertEqual(O.check_dataset(self.source, self.item | {key: 999})["status"], "invalid")

    def test_metadata_mismatch(self):
        (self.source / "BENCH/demo/meta.json").write_text(json.dumps(self.meta | {"lang": "ru"}))
        self.assertEqual(O.check_dataset(self.source, self.item)["status"], "invalid")

    def test_invalid_metadata_does_not_echo_text(self):
        (self.source / "BENCH/demo/meta.json").write_text('{"private": "example content"')
        self.assertNotIn("example content", str(O.check_dataset(self.source, self.item)))

    def test_selection_validation(self):
        self.assertEqual(O.select("demo,demo", {"demo": 1}), ["demo"])
        self.assertEqual(O.select("all", {"b": 1, "a": 1}), ["a", "b"])
        for value in ("", "../demo", "demo,", "unknown", "demo demo"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                O.select(value, {"demo": 1})

    def test_cpu_flag_is_not_capability(self):
        self.assertEqual(O.route(self.model | {"cpu": False}, "cpu", False), ("benchmark/run.py", None))

    def test_cpu_only_cuda_is_blocked(self):
        for family in ("onnx", "spacy"):
            with self.subTest(family=family):
                self.assertIsNone(O.route(self.model | {"family": family}, "cuda", False)[0])

    def test_unpinned_is_blocked(self):
        for revision in ("main", "z" * 40, ""):
            self.assertIsNone(O.route(self.model | {"revision": revision}, "cpu", False)[0])

    def test_historical_loader_is_not_claimed_reproducible(self):
        for family in ("natasha", "stanza", "rupii", "leaks", "rules", "presidio"):
            self.assertIsNone(O.route(self.model | {"family": family}, "cpu", False)[0])

    def test_remote_code_requires_opt_in(self):
        for cfg in (self.model | {"family": "pplx"}, self.model | {"trust_remote_code": True}):
            self.assertIsNone(O.route(cfg, "cpu", False)[0])
            self.assertIsNotNone(O.route(cfg, "cpu", True)[0])

    def test_zero_shot_labels_required(self):
        self.import_data()
        path = self.work / "BENCH/demo/meta.json"
        path.write_text(json.dumps({k: v for k, v in self.meta.items() if k != "labels"}))
        plan = O.make_plan(self.work, [self.item], {"demo": self.model | {"family": "gliner"}}, "cpu", False)
        self.assertEqual(plan["counts"], {"blocked": 1})

    def test_all_cells_are_accounted_for(self):
        plan = O.make_plan(self.work, [self.item], {"a": self.model, "b": self.model}, "cpu", False)
        self.assertEqual(len(plan["jobs"]), 2)
        self.assertEqual(plan["counts"], {"blocked": 2})

    def test_contamination_inherited_by_corruption(self):
        item = self.item | {"id": "corrupt-demo"}
        plan = O.make_plan(self.work, [item], {"demo": self.model | {"contaminated": ["demo"]}}, "cpu", False)
        self.assertTrue(plan["jobs"][0]["training_overlap"])

    def test_environment_drops_stale_settings_but_preserves_auth(self):
        with patch.dict(os.environ, {"OUT": "old", "LIMIT": "1", "ALLOW_ERR": "1", "HF_TOKEN": "test-only"}):
            env = O.environment(self.work)
        for name in ("OUT", "LIMIT", "ALLOW_ERR"):
            self.assertNotIn(name, env)
        self.assertEqual(env["HF_TOKEN"], "test-only")
        self.assertTrue(env["HF_HOME"].startswith(str(self.work)))

    def test_unknown_public_download_is_refused_before_network(self):
        with patch.object(O.subprocess, "run") as call, self.assertRaises(ValueError):
            O.download_public(self.work, [self.item])
        call.assert_not_called()

    def test_ready_public_data_reused_without_network(self):
        self.import_data()
        (self.work / "BENCH/demo").rename(self.work / "BENCH/leak-museum")
        with patch.object(O.subprocess, "run") as call:
            state = O.download_public(self.work, [self.item | {"id": "leak-museum"}])
        call.assert_not_called()
        self.assertEqual(state[0]["status"], "ready")

    def test_inventory_is_read_only_and_machine_readable(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = O.main(["inventory", "--workspace", str(self.work), "--json"])
        self.assertEqual(status, 0)
        self.assertEqual(json.loads(output.getvalue())[0]["status"], "missing")
        self.assertFalse(self.work.exists())

    def test_verify_missing_returns_nonzero(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(O.main(["verify", "--workspace", str(self.work)]), 2)

    def test_blocked_run_never_starts_a_process(self):
        args = argparse.Namespace()
        plan = {"counts": {"blocked": 1}}
        with patch.object(O.subprocess, "run") as call, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(O.run_matrix(args, self.work, plan, {}), 2)
        call.assert_not_called()

    def test_fingerprint_is_order_independent_and_changes_with_inputs(self):
        self.assertEqual(O.fingerprint({"a": 1, "b": 2}), O.fingerprint({"b": 2, "a": 1}))
        self.assertNotEqual(O.fingerprint({"a": 1}), O.fingerprint({"a": 2}))

    def test_atomic_json(self):
        path = self.work / "state.json"
        O.write_json(path, {"ok": True})
        self.assertEqual(json.loads(path.read_text()), {"ok": True})
        self.assertEqual([p.name for p in self.work.iterdir()], ["state.json"])


    def matrix_fixture(self):
        self.import_data()
        scripts = self.root / "scripts"
        scripts.mkdir(exist_ok=True)
        (scripts / "evaluate.py").write_text("# scorer contract fixture\n")
        (scripts / "onboarding.py").write_text("# onboarding identity fixture\n")
        (self.root / "benchmark/run.py").write_text("# inference contract fixture\n")
        file_patch = patch.object(O, "__file__", str(scripts / "onboarding.py"))
        file_patch.start()
        self.addCleanup(file_patch.stop)
        self.calls = []
        self.fail_score = False
        args = argparse.Namespace(environments=None, python="inference-python", device="cpu", batch=4,
                                  threads=2, score_threshold=0.5, resume=False)
        plan = O.make_plan(self.work, [self.item], {"demo": self.model}, "cpu", False)
        probe_patch = patch.object(O, "probe", return_value={"python": "3.12.11", "cpu": "test CPU", "packages": []})
        probe_patch.start()
        self.addCleanup(probe_patch.stop)
        return args, plan

    def fake_process(self, command, **kwargs):
        self.calls.append((command, kwargs))
        env = kwargs["env"]
        run = Path(env["BENCHMARK_DATA"])
        if command[1].endswith("benchmark/run.py"):
            prediction = run / "RESULTS" / command[3] / f"pred.{command[2]}.jsonl"
            prediction.parent.mkdir(parents=True, exist_ok=True)
            prediction.write_text('{"fixture": true}\n')
            return subprocess.CompletedProcess(command, 0)
        if self.fail_score:
            raise subprocess.CalledProcessError(1, command, stderr="fixture scoring failed")
        model = command[command.index("--model") + 1]
        dataset = command[command.index("--dataset") + 1]
        assert command[command.index("--data") + 1] == str(run)
        assert (run / "BENCH" / dataset / "bench.csv").is_file()
        assert (run / "RESULTS" / dataset / f"pred.{model}.jsonl").is_file()
        return subprocess.CompletedProcess(command, 0, stdout=json.dumps({"dataset": dataset, "model": model,
            "fully_hidden": 0, "missed": 1, "gold_spans": 1, "train": False}))

    def execute_matrix(self, args, plan):
        with patch.object(O.subprocess, "run", side_effect=self.fake_process), contextlib.redirect_stdout(io.StringIO()):
            return O.run_matrix(args, self.work, plan, {"demo": self.model})

    def test_run_and_score_use_same_isolated_workspace(self):
        args, plan = self.matrix_fixture()
        with patch.dict(os.environ, {"OUT": "/old/results", "LIMIT": "2", "THRESH": "0.9", "ALLOW_STALE": "1"}):
            self.assertEqual(self.execute_matrix(args, plan), 0)
        self.assertEqual(len(self.calls), 2)
        first, second = self.calls
        self.assertEqual(first[1]["env"]["BENCHMARK_DATA"], second[1]["env"]["BENCHMARK_DATA"])
        self.assertEqual(first[1]["env"]["THRESH"], "0.1")
        self.assertEqual(second[1]["env"]["THRESH"], "0.5")
        self.assertNotIn("OUT", first[1]["env"])
        self.assertNotIn("ALLOW_STALE", second[1]["env"])
        self.assertEqual(first[1]["env"]["LIMIT"], "0")
        self.assertFalse((self.work / "RESULTS").exists())
        self.assertFalse(list((self.work / "runs").glob("*/.running")))
        summary = json.loads(next((self.work / "runs").glob("*/summary.json")).read_text())
        self.assertEqual(summary["requested_cells"], summary["finished_cells"])
        self.assertEqual(summary["counts"], {"completed": 1})

    def test_resume_revalidates_score_without_repeating_inference(self):
        args, plan = self.matrix_fixture()
        self.execute_matrix(args, plan)
        self.calls.clear()
        args.resume = True
        self.assertEqual(self.execute_matrix(args, plan), 0)
        self.assertEqual(len(self.calls), 1)
        self.assertTrue(self.calls[0][0][1].endswith("evaluate.py"))
        summary = json.loads(next((self.work / "runs").glob("*/summary.json")).read_text())
        self.assertEqual(summary["counts"], {"reused": 1})

    def test_existing_run_requires_explicit_resume(self):
        args, plan = self.matrix_fixture()
        self.execute_matrix(args, plan)
        self.calls.clear()
        with self.assertRaises(ValueError):
            self.execute_matrix(args, plan)
        self.assertEqual(self.calls, [])

    def test_changed_prediction_is_not_reused(self):
        args, plan = self.matrix_fixture()
        self.execute_matrix(args, plan)
        next((self.work / "runs").glob("*/RESULTS/demo/pred.demo.jsonl")).write_text("changed")
        self.calls.clear()
        args.resume = True
        self.execute_matrix(args, plan)
        self.assertEqual(len(self.calls), 2)

    def test_corrupt_completion_marker_is_not_reused(self):
        args, plan = self.matrix_fixture()
        self.execute_matrix(args, plan)
        next((self.work / "runs").glob("*/completed/*.json")).write_text("broken json")
        self.calls.clear()
        args.resume = True
        self.execute_matrix(args, plan)
        self.assertEqual(len(self.calls), 2)

    def test_changed_parameters_create_new_run_identity(self):
        args, plan = self.matrix_fixture()
        self.execute_matrix(args, plan)
        args.batch = 8
        self.execute_matrix(args, plan)
        self.assertEqual(len(list((self.work / "runs").glob("*/identity.json"))), 2)

    def test_scoring_failure_is_not_marked_complete(self):
        args, plan = self.matrix_fixture()
        self.fail_score = True
        self.assertEqual(self.execute_matrix(args, plan), 3)
        self.assertFalse(list((self.work / "runs").glob("*/completed/*.json")))
        self.assertFalse(list((self.work / "runs").glob("*/.running")))
        summary = json.loads(next((self.work / "runs").glob("*/summary.json")).read_text())
        self.assertEqual(summary["counts"], {"failed": 1})

    def test_changed_data_after_planning_stops_inference(self):
        args, plan = self.matrix_fixture()
        (self.work / "BENCH/demo/bench.csv").write_text("changed")
        self.assertEqual(self.execute_matrix(args, plan), 3)
        self.assertEqual(self.calls, [])

    def test_active_run_lock_prevents_another_writer(self):
        args, plan = self.matrix_fixture()
        self.execute_matrix(args, plan)
        run = next((self.work / "runs").iterdir())
        (run / ".running").write_text("active")
        self.calls.clear()
        args.resume = True
        with self.assertRaises(ValueError):
            self.execute_matrix(args, plan)
        self.assertEqual(self.calls, [])
        self.assertTrue((run / ".running").exists())

    def test_probe_requires_python_312(self):
        result = subprocess.CompletedProcess([], 0, stdout='{"python":"3.13.1"}')
        with patch.object(O.subprocess, "run", return_value=result), self.assertRaises(ValueError):
            O.probe("python", "hf", "cpu", {})

    def test_probe_import_or_cuda_failure_is_fatal(self):
        with patch.object(O.subprocess, "run", side_effect=subprocess.CalledProcessError(1, [])):
            with self.assertRaises(subprocess.CalledProcessError):
                O.probe("python", "hf", "cuda", {})

    def test_invalid_metadata_shape_is_reported(self):
        (self.source / "BENCH/demo/meta.json").write_text("[]")
        self.assertEqual(O.check_dataset(self.source, self.item)["status"], "invalid")

    def test_escaping_result_directory_is_refused_on_resume(self):
        args, plan = self.matrix_fixture()
        self.execute_matrix(args, plan)
        run = next((self.work / "runs").iterdir())
        (run / "RESULTS").rename(run / "old-results")
        (run / "RESULTS").symlink_to(self.source)
        self.calls.clear()
        args.resume = True
        with self.assertRaises(ValueError):
            self.execute_matrix(args, plan)
        self.assertEqual(self.calls, [])
        self.assertFalse((run / ".running").exists())

    def test_non_object_receipt_is_not_reused(self):
        args, plan = self.matrix_fixture()
        self.execute_matrix(args, plan)
        next((self.work / "runs").glob("*/completed/*.json")).write_text("[]")
        self.calls.clear()
        args.resume = True
        self.execute_matrix(args, plan)
        self.assertEqual(len(self.calls), 2)

    def test_preflight_failure_reports_family_and_local_log(self):
        args, plan = self.matrix_fixture()
        with patch.object(O, "probe", side_effect=subprocess.CalledProcessError(1, [], stderr="fixture import failure")):
            with self.assertRaisesRegex(ValueError, "hf: cpu environment not ready"):
                self.execute_matrix(args, plan)
        self.assertIn("fixture import failure", (self.work / "preflight-hf.log").read_text())
        self.assertEqual(self.calls, [])


if __name__ == "__main__":
    unittest.main()
