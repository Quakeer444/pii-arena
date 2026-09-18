"""Rebuild one public CPU subset and reproduce its Gitleaks result."""
import argparse
import hashlib
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = 'https://github.com/printemps-tokyo/leak-museum'
REVISION = '6b1483a00cfa7bb47551b7304c1e2d4bc9a3a919'
BENCH_SHA256 = '8938b8d88dd5d9c71eba942a997a301ce7ce4f63c50530d46be3c87e597618cd'
EXPECTED = {'missed': 86, 'gold_spans': 101, 'fully_hidden': 15,
            'char_tp': 876, 'char_fp': 0, 'char_fn': 2418,
            'dropped_spans': 0, 'train': False}


def run(command, env=None, capture=False):
    return subprocess.run(command, cwd=ROOT, env=env, check=True, text=True,
                          capture_output=capture)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work-dir', type=Path,
                        default=ROOT / '.local/reproduction/leak-museum-gitleaks')
    args = parser.parse_args()
    work = args.work_dir.resolve()
    if not work.is_relative_to((ROOT / '.local').resolve()):
        parser.error('The reproduction workspace must stay under .local/')
    source = work / 'BENCH/raw/leak-museum'
    if not source.exists():
        source.parent.mkdir(parents=True, exist_ok=True)
        run(['git', 'clone', '--no-checkout', SOURCE, str(source)])
        run(['git', '-C', str(source), 'checkout', '--detach', REVISION])
    actual = run(['git', '-C', str(source), 'rev-parse', 'HEAD'], capture=True).stdout.strip()
    if actual != REVISION:
        raise SystemExit(f'Wrong Leak Museum revision: {actual}')
    env = os.environ | {'BENCHMARK_DATA': str(work)}
    run([sys.executable, 'benchmark/sets_code.py', 'leak-museum'], env)
    bench = work / 'BENCH/leak-museum/bench.csv'
    bench_sha256 = hashlib.sha256(bench.read_bytes()).hexdigest()
    if bench_sha256 != BENCH_SHA256:
        raise SystemExit(f'Corpus hash mismatch: expected {BENCH_SHA256}, observed {bench_sha256}')
    version_cmd = shlex.split(env.get('GITLEAKS_BIN', 'gitleaks')) + ['version']
    version = run(version_cmd, capture=True).stdout.strip()
    if version != '8.30.1':
        raise SystemExit(f'Gitleaks 8.30.1 required, found {version!r}')
    run([sys.executable, 'benchmark/run_leaks.py', 'gitleaks', 'leak-museum'], env)
    result = json.loads(run([sys.executable, 'scripts/evaluate.py', '--data', str(work),
                             '--dataset', 'leak-museum', '--model', 'gitleaks'],
                            capture=True).stdout)
    observed = {key: result[key] for key in EXPECTED}
    if observed != EXPECTED:
        raise SystemExit(f'Quality mismatch: expected {EXPECTED}, observed {observed}')
    print(json.dumps({'bench_sha256': bench_sha256, **observed}, indent=2))


if __name__ == '__main__':
    main()
