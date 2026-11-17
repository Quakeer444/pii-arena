"""Offline regression for the PIIX adapter and its Arena result identities."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PiixTest(unittest.TestCase):
    def test_settings_use_pinned_helpers_and_pass_strict_scoring(self):
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            dataset = work / "BENCH" / "example"
            dataset.mkdir(parents=True)
            (dataset / "meta.json").write_text(json.dumps({
                "lang": "en", "kind": "pii", "source": "synthetic", "groups": {"person": "PERSON"},
                "labels": {"en": ["person"]},
            }))
            (dataset / "bench.csv").write_text('id,domain,text,entities\n1,demo,ABC XYZ,[]\n')
            # Local stand-ins exercise the runner without downloading model weights.
            (work / "torch.py").write_text("def set_num_threads(threads): pass\n")
            (work / "huggingface_hub.py").write_text(
                "from pathlib import Path\n"
                "def snapshot_download(repo, *, revision, allow_patterns):\n"
                "    assert repo == 'Tracer-ML/PIIX-560m'\n"
                "    assert revision == '26d15846b62cb2bd1822871946c884f73879ca47'\n"
                "    assert 'rules.py' in allow_patterns and 'type_filter.py' in allow_patterns\n"
                "    return Path(__file__).parent / 'snapshot'\n"
            )
            snapshot = work / "snapshot"
            snapshot.mkdir()
            (snapshot / "rules.py").write_text("START = 0\n")
            (snapshot / "type_filter.py").write_text("END = 3\n")
            (snapshot / "piix.py").write_text(
                "import rules, type_filter\n"
                "class Redactor:\n"
                "    model = None\n"
                "    def __init__(self, snapshot, *, device, batch):\n"
                "        assert device == 'cpu' and batch == 2\n"
                "    def find(self, texts, *, types, recall):\n"
                "        assert types == ['person'] and texts == ['ABC XYZ']\n"
                "        return [{'mask': [(rules.START, type_filter.END + (4 if recall == 8 else 0))]}]\n"
            )
            env = dict(os.environ, BENCHMARK_DATA=directory, OUT=str(work/"RESULTS"),
                       PYTHONPATH=directory, DEVICE="cpu", THREADS="1", THRESH="0.1",
                       LIMIT="0", NORMALIZE="none", W="1")
            for recall, model, end in ((0, "piix-560m", 3), (8, "piix-560m+r8", 7)):
                subprocess.run([sys.executable, str(ROOT/"benchmark/run_piix.py"), "example",
                                "--recall", str(recall), "--batch", "2"], env=env, check=True)
                path = work / "RESULTS" / "example" / f"pred.{model}.jsonl"
                header, row = map(json.loads, path.read_text().splitlines())
                self.assertEqual(header["meta"]["chunk"], 0)
                self.assertEqual(header["meta"]["errors"], 0)
                self.assertEqual(row["spans"], [{"start": 0, "end": end, "label": "pii"}])
                score = subprocess.check_output([sys.executable, str(ROOT/"scripts/evaluate.py"),
                                                "--data", directory, "--dataset", "example",
                                                "--model", model], env=dict(env, THRESH="0.5"))
                self.assertFalse(json.loads(score)["legacy"])


if __name__ == "__main__":
    unittest.main()
