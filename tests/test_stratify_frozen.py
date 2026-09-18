"""T03: a frozen recomputation must refuse a changed input.

`scripts/stratify.py` rebuilds the published diagnostics from the local
predictions; `scripts/export.py` republishes them. Both must bind a run to the
digest the snapshot records for it, so a prediction that was edited - even
when every normalized metric stays the same - stops the run instead of
producing new numbers under old provenance.
"""
import csv
import hashlib
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import export
import stratify

TEXT = 'Contact Sample Person today.'
START = TEXT.index('Sample')
END = START + len('Sample Person')
GOLD = 'Sample Person'
# Two masks with identical normalized outcome: each touches one word of the
# gold span, so missed, hidden and the character counts cannot tell them apart.
MASK_SAMPLE = [{'start': START, 'end': START + 1, 'label': 'person', 'score': 1.0}]
MASK_PERSON = [{'start': END - 1, 'end': END, 'label': 'person', 'score': 1.0}]


def write_prediction(path, spans, digest_source):
    meta = {'name': 'demo', 'bench': 'example', 'protocol': 1, 'rows': 1, 'chars': len(TEXT),
            'bench_sha256': digest_source}
    path.write_text(json.dumps({'meta': meta}) + '\n'
                    + json.dumps({'id': 'one', 'spans': spans, 'err': None}) + '\n')


with tempfile.TemporaryDirectory() as d:
    base = Path(d)
    (base / 'benchmark').symlink_to(ROOT / 'benchmark')
    bench = base / 'BENCH' / 'example'
    result = base / 'RESULTS' / 'example'
    (base / 'results').mkdir()
    result.mkdir(parents=True)
    (base / 'BENCH').mkdir(exist_ok=True)
    bench.mkdir()
    with (bench / 'bench.csv').open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['id', 'domain', 'text', 'entities'])
        writer.writerow(['one', 'demo', TEXT, json.dumps([{'start': START, 'end': END, 'type': 'PERSON'}])])
    (bench / 'meta.json').write_text(json.dumps({
        'lang': 'en', 'kind': 'pii', 'source': 'local synthetic example',
        'groups': {'PERSON': 'PERSON'}}))
    corpus_sha = hashlib.sha256((bench / 'bench.csv').read_bytes()).hexdigest()

    prediction = result / 'pred.demo.jsonl'
    write_prediction(prediction, MASK_SAMPLE, corpus_sha)
    digest = hashlib.sha256(prediction.read_bytes()).hexdigest()
    snapshot = {
        'threshold': 0.5,
        'datasets': [{'id': 'example', 'bench_sha256': corpus_sha,
                      'original_annotations': 1, 'gold_spans': 1}],
        'measurements': [{'dataset': 'example', 'model': 'demo', 'train': False, 'missed': 0,
                          'gold_spans': 1, 'hidden_pct_reported': 0.0,
                          'char_precision_reported': 1.0,
                          'char_recall_reported': len(GOLD) and 6 / 13,
                          'char_f1_reported': 2 * (6 / 13) / (1 + 6 / 13)}],
        'ensembles': [], 'composition_counts': [],
        'sources': {'RESULTS/example/pred.demo.jsonl': digest},
    }

    # Positive control: with the recorded digest the recomputation runs and
    # produces the published numbers.
    def shape(result):
        row = result['results'][0]
        return (row['char_tp'], row['char_fp'], row['char_fn'],
                [(t['label'], t['hit'], t['hidden'], t['raw_hidden']) for t in row['types']])

    built = stratify.build(base, snapshot)
    assert shape(built) == (6, 0, 7, [('PERSON', 1, 0, 0)]), shape(built)

    # The changed prediction: same normalized metrics by construction, other
    # bytes, so only the digest can notice.
    write_prediction(prediction, MASK_PERSON, corpus_sha)
    changed = snapshot | {'sources': {'RESULTS/example/pred.demo.jsonl':
                                      hashlib.sha256(prediction.read_bytes()).hexdigest()}}
    rebuilt = stratify.build(base, changed)
    assert shape(rebuilt) == shape(built), (shape(rebuilt), shape(built))
    try:
        stratify.build(base, snapshot)
    except ValueError as error:
        assert 'Frozen prediction changed' in str(error), error
    else:
        raise AssertionError('A prediction that no longer matches its digest was accepted')

    # The documented entry point refuses before writing anything: the published
    # snapshot stays byte-identical.
    (base / 'results/snapshot.json').write_text(json.dumps(snapshot))
    before = (base / 'results/snapshot.json').read_bytes()
    real_root, real_argv = stratify.ROOT, sys.argv
    stratify.ROOT, sys.argv = base, ['stratify.py', '--data', str(base)]
    try:
        try:
            stratify.main()
        except ValueError as error:
            assert 'Frozen prediction changed' in str(error), error
        else:
            raise AssertionError('stratify.py republished a changed input')
    finally:
        stratify.ROOT, sys.argv = real_root, real_argv
    assert (base / 'results/snapshot.json').read_bytes() == before, 'artifact changed on a refused run'
    assert not list((base / 'results').glob('*.tmp')), 'a temporary file was left behind'

# The export entry point enforces the same contract on every field a published
# number was computed from, including the source digests.
previous = {'threshold': 0.5, 'datasets': [], 'measurements': [], 'ensembles': [],
            'composition_counts': [], 'sources': {'RESULTS/example/pred.demo.jsonl': digest}}
export.check_reuse(previous, dict(previous))
for key in export.REUSE_KEYS:
    staged = dict(previous) | {key: 'changed'}
    try:
        export.check_reuse(previous, staged)
    except ValueError as error:
        assert '--recompute-compositions' in str(error), error
    else:
        raise AssertionError(f'Reuse export accepted a changed {key}')

print('stratify and export frozen-input checks passed')
