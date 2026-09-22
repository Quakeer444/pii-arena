"""Inspect, prepare and run local benchmark workspaces without changing the release."""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PINNED = {"opf", "hf", "pplx", "gliner", "gliner2", "onnx", "spacy"}
CUDA = {"opf", "hf", "pplx", "gliner", "gliner2"}
GROUPS = {"PERSON", "ADDRESS", "CONTACT", "ID", "NET", "ACCOUNT", "SECRET", "ORG", "DATE", "OTHER"}
IMPORTS = {
    "opf": ["torch", "transformers", "safetensors", "huggingface_hub"],
    "hf": ["torch", "transformers"], "pplx": ["torch", "transformers"],
    "gliner": ["torch", "gliner"], "gliner2": ["torch", "gliner2"],
    "onnx": ["torch", "transformers", "optimum.onnxruntime"],
    "spacy": ["spacy", "huggingface_hub"],
}
CONTROLLED = {
    "BENCHMARK_DATA", "OUT", "DEVICE", "THREADS", "W", "LIMIT", "THRESH",
    "CHUNK", "CHUNK_MODE", "OVERLAP", "VARIANT", "NORMALIZE", "QUANT",
    "ALLOW_ERR", "ALLOW_STALE", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
    "OPENBLAS_NUM_THREADS", "HF_HOME", "HF_HUB_CACHE", "HF_DATASETS_CACHE",
    "TRANSFORMERS_CACHE", "TORCH_HOME", "XDG_CACHE_HOME", "HF_MODULES_CACHE",
}


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def fingerprint(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=True).encode()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", dir=path.parent, encoding="utf-8", delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(value, stream, indent=2, ensure_ascii=True)
        stream.write("\n")
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def workspace(path: Path) -> Path:
    resolved = path.resolve()
    local = ROOT / ".local"
    preserved = local / "research"
    if not resolved.is_relative_to(local) or resolved == local:
        raise ValueError("Use a workspace strictly inside this repository's .local/ directory")
    if resolved == preserved or resolved.is_relative_to(preserved):
        raise ValueError("The preserved .local/research archive is read-only; choose another workspace")
    # Existing nested links must not redirect writes outside the workspace.
    for name in ("BENCH", "MODELS", "runs", "cache", "staging"):
        if not (resolved / name).resolve().is_relative_to(resolved):
            raise ValueError(f"Workspace {name} points outside the workspace")
    return resolved


def catalog() -> tuple[dict, dict]:
    datasets = json.loads((ROOT / "datasets/catalog.json").read_text(encoding="utf-8"))
    models = tomllib.loads((ROOT / "benchmark/models.toml").read_text(encoding="utf-8"))["models"]
    return {item["id"]: item for item in datasets}, models


def select(expression: str, items: dict) -> list[str]:
    names = sorted(items) if expression == "all" else list(dict.fromkeys(expression.split(",")))
    if not names or any(not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.+-]*", name) for name in names):
        raise ValueError("Use 'all' or comma-separated catalog IDs, without spaces or paths")
    unknown = set(names) - items.keys()
    if unknown:
        raise ValueError("Unknown IDs: " + ", ".join(sorted(unknown)))
    return names


def initialize(work: Path) -> None:
    for name in ("BENCH/raw", "MODELS", "runs", "cache", "staging"):
        path = work / name
        if not path.resolve().is_relative_to(work):
            raise ValueError("Workspace contains an escaping symlink")
        path.mkdir(parents=True, exist_ok=True)
    source, target = ROOT / "datasets/samples.json", work / "BENCH/samples.json"
    if target.exists() and digest(source) != digest(target):
        raise ValueError("samples.json differs from the release; use a new workspace")
    if not target.exists():
        shutil.copyfile(source, target)


def check_dataset(work: Path, item: dict) -> dict:
    name = item["id"]
    result = {"dataset": name, "status": "missing", "reason": "prepare or import bench.csv and meta.json"}
    folder = work / "BENCH" / name
    paths = [folder / "bench.csv", folder / "meta.json"]
    if not all(path.is_file() for path in paths):
        return result
    try:
        if any(not path.resolve().is_relative_to(work.resolve()) for path in paths):
            raise ValueError("dataset files point outside the selected workspace")
        if digest(paths[0]) != item["bench_sha256"]:
            raise ValueError("corpus SHA-256 differs from the frozen catalog")
        meta = json.loads(paths[1].read_text(encoding="utf-8"))
        if any(meta.get(key) != item[key] for key in ("lang", "kind")):
            raise ValueError("metadata language/task differs from the catalog")
        groups = meta.get("groups")
        if not isinstance(groups, dict) or not groups or not all(
            isinstance(k, str) and k and isinstance(v, str) and v in GROUPS for k, v in groups.items()
        ):
            raise ValueError("metadata needs a valid label-to-group map")
        if "groups" in item and not set(item["groups"]).issubset(set(groups.values())):
            raise ValueError("metadata groups differ from the catalog")
        counts = {"rows": 0, "characters": 0, "original_annotations": 0}
        ids = set()
        csv.field_size_limit(10 ** 7)
        with paths[0].open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != ["id", "domain", "text", "entities"]:
                raise ValueError("unexpected corpus columns")
            for row in reader:
                if not row["id"] or row["id"] in ids:
                    raise ValueError("empty or duplicate row ID")
                ids.add(row["id"])
                entities = json.loads(row["entities"])
                if not isinstance(entities, list):
                    raise ValueError("entities must be a list")
                for entity in entities:
                    a, b = entity["start"], entity["end"]
                    if type(a) is not int or type(b) is not int or not 0 <= a < b <= len(row["text"]):
                        raise ValueError("invalid annotation offsets")
                    if entity["type"] not in groups:
                        raise ValueError("annotation type is absent from metadata")
                text = row["text"]
                counts["rows"] += 1
                # Catalog totals follow open(), which folds each CRLF to one character.
                counts["characters"] += len(text) - text.count("\r\n")
                counts["original_annotations"] += len(entities)
        if any(counts[k] != item[k] for k in counts if k in item):
            raise ValueError("corpus counts differ from the catalog")
        return {"dataset": name, "status": "ready", "bench_sha256": item["bench_sha256"],
                "meta_sha256": digest(paths[1]), **counts}
    except (ValueError, OSError, KeyError, TypeError, AttributeError, csv.Error) as error:
        # Never include corpus text or exception details that may contain a row.
        message = str(error) if type(error) is ValueError else type(error).__name__
        return {"dataset": name, "status": "invalid", "reason": message}


def prepare(work: Path, items: list[dict], source: Path | None) -> list[dict]:
    initialize(work)
    if source is None:
        return [check_dataset(work, item) for item in items]
    source = source.resolve()
    if source == work:
        raise ValueError("Import source and destination must be different workspaces")
    checks = [check_dataset(source, item) for item in items]
    if any(row["status"] != "ready" for row in checks):
        return checks  # Validate the complete selection before copying anything.
    for item in items:
        target = work / "BENCH" / item["id"]
        if target.exists():
            state = check_dataset(work, item)
            if state["status"] != "ready" or state["meta_sha256"] != digest(source / "BENCH" / item["id"] / "meta.json"):
                raise ValueError(f"{item['id']}: refusing to overwrite existing data or different metadata")
    for item in items:
        target = work / "BENCH" / item["id"]
        if target.exists():
            continue
        with tempfile.TemporaryDirectory(dir=work / "staging") as name:
            stage = Path(name)
            staged = stage / "BENCH" / item["id"]
            staged.mkdir(parents=True)
            for filename in ("bench.csv", "meta.json"):
                shutil.copyfile(source / "BENCH" / item["id"] / filename, staged / filename)
            if check_dataset(stage, item)["status"] != "ready":
                raise ValueError("Source changed during import; no unverified dataset was promoted")
            staged.rename(target)
    return [check_dataset(work, item) for item in items]


def environment(work: Path) -> dict:
    env = {k: v for k, v in os.environ.items() if k not in CONTROLLED}
    cache = work / "cache"
    env.update({"HF_HOME": str(cache / "huggingface"), "HF_HUB_CACHE": str(cache / "huggingface/hub"),
                "HF_DATASETS_CACHE": str(cache / "huggingface/datasets"),
                "HF_MODULES_CACHE": str(cache / "huggingface/modules"),
                "TORCH_HOME": str(cache / "torch"), "XDG_CACHE_HOME": str(cache)})
    return env


def download_public(work: Path, items: list[dict]) -> list[dict]:
    if [item["id"] for item in items] != ["leak-museum"]:
        raise ValueError("Only leak-museum has an audited automatic download recipe. See docs/run-benchmarks.md")
    initialize(work)
    existing = [check_dataset(work, item) for item in items]
    if all(row["status"] == "ready" for row in existing):
        return existing
    spec = importlib.util.spec_from_file_location("public_cpu_recipe", ROOT / "scripts/reproduce_cpu.py")
    recipe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(recipe)
    with tempfile.TemporaryDirectory(dir=work / "staging") as name:
        stage = Path(name)
        raw = stage / "BENCH/raw/leak-museum"
        raw.parent.mkdir(parents=True)
        log = work / "prepare.log"
        env = environment(work) | {"BENCHMARK_DATA": str(stage)}
        commands = [["git", "clone", "--no-checkout", recipe.SOURCE, str(raw)],
                    ["git", "-C", str(raw), "checkout", "--detach", recipe.REVISION],
                    [sys.executable, str(ROOT / "benchmark/sets_code.py"), "leak-museum"]]
        with log.open("w", encoding="utf-8") as stream:
            for command in commands:
                subprocess.run(command, cwd=ROOT, env=env, check=True, stdout=stream, stderr=stream)
        return prepare(work, items, stage)


def route(model: dict, device: str, trust_remote: bool) -> tuple[str | None, str | None]:
    family = model["family"]
    if family not in PINNED:
        return None, "historical/package/scanner route needs its own validated environment; see docs/reproduce.md"
    if not re.fullmatch(r"[a-fA-F0-9]{40}", model.get("revision", "")):
        return None, "missing immutable model revision"
    if device == "cuda" and family not in CUDA:
        return None, "current adapter is CPU-only; use a separate CPU campaign"
    if (family == "pplx" or model.get("trust_remote_code")) and not trust_remote:
        return None, "remote model code requires --trust-remote-code"
    return "benchmark/run.py", None


def make_plan(work: Path, datasets: list[dict], models: dict, device: str, trust_remote: bool) -> dict:
    checks = {item["id"]: check_dataset(work, item) for item in datasets}
    jobs = []
    for name, model in models.items():
        adapter, reason = route(model, device, trust_remote)
        for item in datasets:
            dataset = item["id"]
            problems = [reason] if reason else []
            if checks[dataset]["status"] != "ready":
                problems.append(checks[dataset]["reason"])
            elif model["family"] in {"gliner", "gliner2"}:
                meta = json.loads((work / "BENCH" / dataset / "meta.json").read_text(encoding="utf-8"))
                labels = meta.get("labels", {}).get(model.get("labels", "en"))
                if not isinstance(labels, list) or not labels or not all(isinstance(x, str) and x for x in labels):
                    problems.append("metadata lacks the model's zero-shot labels")
            contaminated = model.get("contaminated", [])
            overlap = dataset in contaminated or dataset.removeprefix("corrupt-") in contaminated
            jobs.append({"model": name, "dataset": dataset, "family": model["family"],
                         "device": device, "adapter": adapter, "training_overlap": overlap,
                         "status": "blocked" if problems else "planned", "reasons": problems})
    return {"datasets": list(checks.values()), "jobs": jobs,
            "counts": dict(Counter(job["status"] for job in jobs)),
            "note": "Planned is not environment-verified. Historical result variants are not new model definitions."}


def probe(python: str, family: str, device: str, env: dict) -> dict:
    code = """import importlib, importlib.metadata as md, json, platform, subprocess, sys
from pathlib import Path
for name in json.loads(sys.argv[1]):
    importlib.import_module(name)
if sys.argv[2] == 'cuda':
    import torch
    if not torch.cuda.is_available():
        raise SystemExit('CUDA was requested but is unavailable; no CPU fallback')
cpu = platform.processor()
try:
    if sys.platform == 'darwin':
        cpu = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string'], text=True).strip()
    elif Path('/proc/cpuinfo').exists():
        cpu = next(line.split(':', 1)[1].strip() for line in Path('/proc/cpuinfo').read_text().splitlines() if line.startswith('model name'))
except (OSError, StopIteration, subprocess.SubprocessError):
    pass
print(json.dumps({'python': platform.python_version(), 'platform': platform.platform(), 'cpu': cpu,
 'cuda_runtime': torch.version.cuda if sys.argv[2] == 'cuda' else None,
 'packages': sorted((d.metadata.get('Name', ''), d.version) for d in md.distributions()),
 'gpu': torch.cuda.get_device_name(0) if sys.argv[2] == 'cuda' else None}))
"""
    result = subprocess.run([python, "-c", code, json.dumps(IMPORTS[family]), device], env=env,
                            capture_output=True, text=True, check=True, timeout=120)
    data = json.loads(result.stdout.strip().splitlines()[-1])
    if not data["python"].startswith("3.12."):
        raise ValueError("Inference environments must use Python 3.12")
    return data


def run_matrix(args: argparse.Namespace, work: Path, plan: dict, models: dict) -> int:
    if plan["counts"].get("blocked"):
        print("Blocked cells remain. Prepare data or explicitly select supported model/dataset IDs; nothing was run.")
        return 2
    initialize(work)
    python_map = {}
    if args.environments:
        python_map = tomllib.loads(args.environments.read_text(encoding="utf-8")).get("python", {})
    probes, interpreters = {}, {}
    env = environment(work)
    for family in sorted({job["family"] for job in plan["jobs"]}):
        interpreter = python_map.get(family, args.python or sys.executable)
        interpreters[family] = interpreter
        try:
            probes[family] = probe(interpreter, family, args.device, env)
        except (ValueError, OSError, subprocess.SubprocessError) as error:
            log = work / f"preflight-{family}.log"
            if not log.resolve().is_relative_to(work):
                raise ValueError("Preflight log points outside the workspace") from None
            log.write_text(f"{type(error).__name__}\n{getattr(error, 'stdout', '') or ''}\n"
                           f"{getattr(error, 'stderr', '') or ''}", encoding="utf-8")
            raise ValueError(f"{family}: {args.device} environment not ready ({interpreter}); see {log}") from None
    files = sorted((ROOT / "benchmark").glob("*.py")) + [ROOT / "scripts/evaluate.py", Path(__file__)]
    identity = {"schema": 1, "models": models, "data": plan["datasets"], "device": args.device,
                "batch": args.batch, "threads": args.threads, "inference_threshold": 0.1,
                "score_threshold": args.score_threshold, "chunk": 600, "chunk_mode": "char",
                "normalize": "none", "quant": "none", "runtime": probes,
                "code": {str(path.relative_to(ROOT)): digest(path) for path in files}}
    expected_data = {row["dataset"]: row for row in plan["datasets"]}

    def unchanged(dataset: str) -> None:
        for name, key in (("bench.csv", "bench_sha256"), ("meta.json", "meta_sha256")):
            path = work / "BENCH" / dataset / name
            if not path.resolve().is_relative_to(work) or digest(path) != expected_data[dataset][key]:
                raise ValueError("Dataset changed after planning; use unchanged verified inputs")

    run_id = fingerprint(identity)[:24]
    run = work / "runs" / run_id
    if run.exists() and not args.resume:
        raise ValueError("This run already exists; use --resume or a new workspace")
    if not run.resolve().is_relative_to(work):
        raise ValueError("Run directory points outside the workspace")
    run.mkdir(parents=True, exist_ok=True)
    lock = run / ".running"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise ValueError(f"Run is locked: {lock}. Check for an active process before removing a stale lock.") from None
    os.close(fd)
    try:
        for name in ("RESULTS", "completed", "identity.json", "plan.json", "summary.json"):
            if not (run / name).resolve().is_relative_to(run):
                raise ValueError("Run output points outside the run directory")
        for name in ("BENCH", "MODELS"):
            link = run / name
            if not link.exists():
                link.symlink_to(work / name, target_is_directory=True)
            elif link.resolve() != (work / name).resolve():
                raise ValueError("Run contains an unexpected workspace link")
        write_json(run / "identity.json", identity)
        write_json(run / "plan.json", plan)
        outcomes = []
        for index, job in enumerate(plan["jobs"], 1):
            model, dataset, family = job["model"], job["dataset"], job["family"]
            key = f"{dataset}--{model}"
            prediction = run / "RESULTS" / dataset / f"pred.{model}.jsonl"
            marker = run / "completed" / f"{key}.json"
            log = run / f"{key}.log"
            print(f"[{index}/{len(plan['jobs'])}] {model} / {dataset} ({args.device})", flush=True)
            child_env = env | {"BENCHMARK_DATA": str(run), "DEVICE": args.device,
                               "THREADS": str(args.threads), "W": "1", "LIMIT": "0", "THRESH": "0.1",
                               "CHUNK": "600", "CHUNK_MODE": "char", "OVERLAP": "100", "VARIANT": "",
                               "NORMALIZE": "none", "QUANT": "none", "OMP_NUM_THREADS": str(args.threads),
                               "MKL_NUM_THREADS": str(args.threads), "OPENBLAS_NUM_THREADS": str(args.threads)}
            try:
                if any(not path.resolve().is_relative_to(run) for path in (prediction, marker, log)):
                    raise ValueError("Cell output points outside the run directory")
                unchanged(dataset)
                reuse = False
                if args.resume and marker.is_file() and prediction.is_file():
                    try:
                        saved = json.loads(marker.read_text(encoding="utf-8"))
                    except ValueError:
                        saved = {}
                    reuse = isinstance(saved, dict) and saved.get("identity") == fingerprint(identity) and saved.get("prediction_sha256") == digest(prediction)
                if not reuse:
                    marker.unlink(missing_ok=True)
                    with log.open("w", encoding="utf-8") as stream:
                        subprocess.run([interpreters[family], str(ROOT / job["adapter"]), model, dataset, str(args.batch)],
                                       cwd=ROOT, env=child_env, stdout=stream, stderr=stream, check=True)
                unchanged(dataset)
                result = subprocess.run([sys.executable, str(ROOT / "scripts/evaluate.py"), "--data", str(run),
                                         "--dataset", dataset, "--model", model], cwd=ROOT,
                                        env=child_env | {"THRESH": str(args.score_threshold)},
                                        capture_output=True, text=True, check=True)
                metrics = json.loads(result.stdout)
                write_json(marker, {"identity": fingerprint(identity), "prediction_sha256": digest(prediction), "metrics": metrics})
                outcomes.append({**job, "status": "reused" if reuse else "completed", "metrics": metrics})
            except (subprocess.CalledProcessError, ValueError, OSError) as error:
                if any(not path.resolve().is_relative_to(run) for path in (prediction, marker, log)):
                    raise ValueError("Cell output points outside the run directory") from None
                marker.unlink(missing_ok=True)
                # Raw process output stays local; do not echo corpus-bearing errors.
                with log.open("a", encoding="utf-8") as stream:
                    stream.write(f"\n{type(error).__name__}\n")
                    if isinstance(error, subprocess.CalledProcessError):
                        stream.write(error.stderr or "")
                outcomes.append({**job, "status": "failed", "log": log.name})
            write_json(run / "summary.json", {"run_id": run_id, "jobs": outcomes,
                        "requested_cells": len(plan["jobs"]), "finished_cells": len(outcomes),
                        "counts": dict(Counter(x["status"] for x in outcomes)),
                        "note": "New measurements, not an exact rerun of all historical profiles. Do not pool training-overlap cells."})
        print(f"Results: {run / 'summary.json'}")
        return 3 if any(job["status"] == "failed" for job in outcomes) else 0
    finally:
        lock.unlink(missing_ok=True)


def positive(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be positive")
    return number


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["inventory", "prepare", "verify", "plan", "run"])
    parser.add_argument("--workspace", type=Path, default=ROOT / ".local/benchmark")
    parser.add_argument("--datasets", default="all", help="all or comma-separated catalog IDs")
    parser.add_argument("--models", default="all", help="all or comma-separated model IDs")
    parser.add_argument("--device", choices=["cpu", "cuda"], default="cpu")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--from-workspace", type=Path)
    source.add_argument("--download", action="store_true", help="explicitly download the audited Leak Museum recipe")
    parser.add_argument("--python", help="Python 3.12 executable in an inference environment")
    parser.add_argument("--environments", type=Path, help="TOML [python] mapping from family to executable")
    parser.add_argument("--trust-remote-code", action="store_true")
    parser.add_argument("--batch", type=positive, default=4)
    parser.add_argument("--threads", type=positive, default=4)
    parser.add_argument("--score-threshold", type=float, default=0.5)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        if not 0.1 <= args.score_threshold <= 1:
            raise ValueError("score threshold must be between the inference floor 0.1 and 1")
        work = workspace(args.workspace)
        data, all_models = catalog()
        items = [data[name] for name in select(args.datasets, data)]
        models = {name: all_models[name] for name in select(args.models, all_models)}
        if args.command == "inventory":
            rows = [{"dataset": item["id"], "source": item["source"], "license": item["license"],
                     "source_revision": (item.get("raw") or {}).get("revision", "-"),
                     "raw_paths": (item.get("raw") or {}).get("paths", []),
                     "automatic_download": item["id"] == "leak-museum", **check_dataset(work, item)} for item in items]
        elif args.command == "prepare":
            rows = download_public(work, items) if args.download else prepare(work, items, args.from_workspace)
        elif args.command == "verify":
            rows = [check_dataset(work, item) for item in items]
        else:
            plan = make_plan(work, items, models, args.device, args.trust_remote_code)
            if args.command == "run":
                return run_matrix(args, work, plan, models)
            if args.json:
                print(json.dumps(plan, indent=2))
            else:
                print(json.dumps(plan["counts"], sort_keys=True))
                for name in models:
                    jobs = [job for job in plan["jobs"] if job["model"] == name]
                    reasons = sorted({reason for job in jobs for reason in job["reasons"]})
                    print(f"{name}: {sum(job['status'] == 'planned' for job in jobs)}/{len(jobs)} planned" +
                          ("; " + "; ".join(reasons) if reasons else ""))
                print(plan["note"])
            return 2 if plan["counts"].get("blocked") else 0
        if args.json:
            print(json.dumps(rows, indent=2))
        else:
            for row in rows:
                print(f"{row['dataset']:<28} {row['status']:<8} {row.get('reason', '')}")
            print(json.dumps(dict(Counter(row["status"] for row in rows)), sort_keys=True))
        return 0 if args.command == "inventory" or all(row["status"] == "ready" for row in rows) else 2
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        print(f"Not ready: {error if isinstance(error, ValueError) else type(error).__name__}. See docs/run-benchmarks.md", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
