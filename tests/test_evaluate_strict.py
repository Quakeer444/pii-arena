"""Strict rescoring refuses a prediction that omits protocol or fingerprint.

Same-length text edits must not produce an unmarked success. `--legacy` may
score a file that never recorded those fields, and it has to say so.
"""
import csv
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def write_run(directory, text, meta):
    bench = directory / 'BENCH' / 'tiny'
    result = directory / 'RESULTS' / 'tiny'
    bench.mkdir(parents=True, exist_ok=True)
    result.mkdir(parents=True, exist_ok=True)
    with (bench / 'bench.csv').open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['id', 'domain', 'text', 'entities'])
        writer.writerow(['one', 'demo', text, '[]'])
    (bench / 'meta.json').write_text(json.dumps({
        'lang': 'en', 'kind': 'pii', 'source': 'synthetic strict-input check',
        'groups': {'PERSON': 'PERSON'},
    }))
    digest = hashlib.sha256((bench / 'bench.csv').read_bytes()).hexdigest()
    record = {'name': 'demo', 'bench': 'tiny', 'rows': 1, 'chars': len(text), **meta}
    (result / 'pred.demo.jsonl').write_text(
        json.dumps({'meta': record}) + '\n' + json.dumps({'id': 'one', 'spans': []}) + '\n')
    return digest


def evaluate(directory, *extra):
    return subprocess.run(
        [sys.executable, 'scripts/evaluate.py', '--data', str(directory),
         '--dataset', 'tiny', '--model', 'demo', *extra],
        cwd=ROOT, capture_output=True, text=True)


def test_missing_identity():
    with tempfile.TemporaryDirectory() as raw:
        directory = Path(raw)
        write_run(directory, 'ABC', {})
        strict = evaluate(directory)
        assert strict.returncode != 0, strict.stdout
        assert 'bench_sha256' in strict.stderr and 'protocol' in strict.stderr
        legacy = evaluate(directory, '--legacy')
        assert legacy.returncode == 0, legacy.stderr
        body = json.loads(legacy.stdout)
        assert body['legacy'] is True
        assert body['protocol'] is None
        assert body['bench_sha256'] is None
        assert 'frozen corpus text' in body['limitations']


def test_same_length_edit_without_hash():
    with tempfile.TemporaryDirectory() as raw:
        directory = Path(raw)
        write_run(directory, 'XYZ', {})
        strict = evaluate(directory)
        assert strict.returncode != 0, strict.stdout
        assert 'bench_sha256' in strict.stderr


def test_same_length_edit_with_original_hash():
    with tempfile.TemporaryDirectory() as raw:
        directory = Path(raw)
        original = write_run(directory, 'ABC', {})
        write_run(directory, 'XYZ', {'protocol': 1, 'bench_sha256': original})
        mismatch = evaluate(directory, '--legacy')
        assert mismatch.returncode != 0, mismatch.stdout
        assert 'fingerprint mismatch' in mismatch.stderr


def test_strict_success_records_identity():
    with tempfile.TemporaryDirectory() as raw:
        directory = Path(raw)
        digest = write_run(directory, 'ABC', {})
        write_run(directory, 'ABC', {'protocol': 1, 'bench_sha256': digest})
        strict = evaluate(directory)
        assert strict.returncode == 0, strict.stderr
        body = json.loads(strict.stdout)
        assert body['legacy'] is False
        assert body['protocol'] == 1
        assert body['threshold'] == 0.5
        assert body['bench_sha256'] == digest
        assert body['dataset_sha256'] == digest
        assert 'limitations' not in body


test_missing_identity()
test_same_length_edit_without_hash()
test_same_length_edit_with_original_hash()
test_strict_success_records_identity()
print('strict evaluate checks passed')
