import collections, json, os, subprocess, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault('DEVICE', 'cpu')
import corrupt
import ens
import run
import run_leaks
import score as S
import secrets_recall as SR
GROUPS = {'A': 'PERSON', 'B': 'ID', 'SECRET': 'SECRET'}

def make(d, rows, spans_by_id, meta_extra=None):
    bench, res = (Path(d) / 'BENCH' / 't', Path(d) / 'RESULTS' / 't')
    bench.mkdir(parents=True)
    res.mkdir(parents=True)
    with (bench / 'bench.csv').open('w', newline='') as fh:
        fh.write('id,domain,text,entities\n')
        for rid, text, ents in rows:
            fh.write(f'{rid},,"{text}","{json.dumps(ents).replace(chr(34), chr(34) * 2)}"\n')
    (bench / 'meta.json').write_text(json.dumps({'lang': 'ru', 'kind': 'pii', 'source': 'selftest', 'license': '-', 'mode': 'link', 'domain': '-', 'labels': {'en': [], 'ru': []}, 'groups': GROUPS}))
    meta = {'name': 'm', 'bench': 't', 'rows': len(rows), 'chars': sum((len(t) for _, t, _ in rows)), 'protocol': S.PROTOCOL}
    meta.update(meta_extra or {})
    f = res / 'pred.m.jsonl'
    with f.open('w') as fh:
        fh.write(json.dumps({'meta': meta}) + '\n')
        for rid, _, _ in rows:
            fh.write(json.dumps({'id': rid, 'spans': spans_by_id.get(rid, []), 'err': None}) + '\n')
    S.BENCH, S.RESULTS = (Path(d) / 'BENCH', Path(d) / 'RESULTS')
    for fn in (S.gold, S.gold_norm, S.chars_of, S.meta_of, S.dirty, S._canon):
        fn.cache_clear()
    return f

def load(d, rows, spans_by_id, meta_extra=None):
    f = make(d, rows, spans_by_id, meta_extra)
    g, gg = (S.gold('t')[0], S.meta_of('t')['groups'])
    return S.load_model(f, g, gg)[1]

def coincident():
    ents = [{'start': 0, 'end': 4, 'type': 'A'}, {'start': 0, 'end': 4, 'type': 'B'}]
    with tempfile.TemporaryDirectory() as d:
        st = load(d, [('1', 'Иван идёт', ents)], {})
        nspans = sum((len(v) for v in S.gold_norm('t').values()))
        by_group = sum((v[1] for v in st['miss_g'].values()))
        missed = sum(st['ofn'])
        assert nspans == 2, nspans
        assert missed == 2, missed
        assert by_group == nspans == missed, (by_group, nspans, missed)
        assert sum((v[0] for v in st['miss_g'].values())) == missed

def hit_is_a_hit():
    ents = [{'start': 0, 'end': 4, 'type': 'A'}, {'start': 0, 'end': 4, 'type': 'B'}]
    with tempfile.TemporaryDirectory() as d:
        st = load(d, [('1', 'Иван идёт', ents)], {'1': [{'start': 1, 'end': 2, 'label': 'person'}]})
        assert sum(st['ofn']) == 0, st['ofn']
        assert sum((v[0] for v in st['miss_g'].values())) == 0

def hidden():
    ents = [{'start': 0, 'end': 11, 'type': 'A'}]
    with tempfile.TemporaryDirectory() as d:
        st = load(d, [('1', 'Иван Петров идёт', ents)], {'1': [{'start': 0, 'end': 4, 'label': 'person'}]})
        assert sum(st['ofn']) == 0 and sum(st['hid']) == 0, (st['ofn'], st['hid'])
    with tempfile.TemporaryDirectory() as d:
        st = load(d, [('1', 'Иван Петров идёт', ents)], {'1': [{'start': 0, 'end': 11, 'label': 'person'}]})
        assert sum(st['hid']) == 1 and sum(st['ng']) == 1, (st['hid'], st['ng'])

def folds():
    with tempfile.TemporaryDirectory() as d:
        rows = [(str(i), f'Sample {i}', []) for i in range(40)] + [('duplicate', 'Sample 0', [])]
        make(d, rows, {})
        copy = S.BENCH / 'corrupt-t'
        copy.mkdir()
        meta = S.meta_of('t') | {'base': 't'}
        (copy / 'meta.json').write_text(json.dumps(meta))
        assert {S.fold('t', r) for r, _, _ in rows} == {'dev', 'test'}
        assert all(S.fold('corrupt-t', r) == S.fold('t', r) for r, _, _ in rows)
        assert S.fold('t', '0') == S.fold('t', 'duplicate')

def out_of_text():
    ents = [{'start': 0, 'end': 4, 'type': 'A'}]
    with tempfile.TemporaryDirectory() as d:
        st = load(d, [('1', 'Иван идёт', ents)], {'1': [{'start': 40, 'end': 99, 'label': 'person'}]})
        assert st['bad'] == 1, st['bad']
        assert sum(st['ofn']) == 1, st['ofn']

def stale_and_dupes():
    ents = [{'start': 0, 'end': 4, 'type': 'A'}]
    with tempfile.TemporaryDirectory() as d:
        f = make(d, [('1', 'Иван идёт', ents)], {})
        meta = S.read_pred(f)[0]
        assert not S.check_data(f, meta), S.check_data(f, meta)
        assert S.check_data(f, meta | {'chars': meta['chars'] + 1})
        assert S.check_data(f, meta | {'protocol': S.PROTOCOL + 1})
        assert S.check_data(f, meta | {'bench_sha256': '0' * 64})
        with f.open('a') as fh:
            fh.write(json.dumps({'id': '1', 'spans': [], 'err': None}) + '\n')
        try:
            S.read_pred(f)
        except SystemExit as e:
            assert 'written twice' in str(e), e
        else:
            raise AssertionError('Duplicate row accepted')

def scanner_crash():
    dead = subprocess.CompletedProcess([], 2, stdout='', stderr='panic: boom')
    ok = subprocess.CompletedProcess([], 0, stdout='', stderr='')
    found = subprocess.CompletedProcess([], 200, stdout='', stderr='')
    for ps, by in (([dead], {}), ([dead], {0: [1]}), ([found], {0: [1]})):
        try:
            run_leaks.need('trufflehog', ps, by)
        except SystemExit as e:
            assert 'run failed' in str(e), e
        else:
            raise AssertionError('Scanner failure accepted as a result')
    assert run_leaks.need('trufflehog', [ok], {}) == {}
    assert run_leaks.need('kingfisher', [found], {0: [1]})
    try:
        run_leaks.need('kingfisher', [dead], {0: [1]})
    except SystemExit:
        pass
    else:
        raise AssertionError('Invalid Kingfisher exit code accepted with partial findings')
    with tempfile.TemporaryDirectory() as d:
        try:
            run_leaks.report_of('credsweeper', Path(d) / 'no.json', dead)
        except SystemExit as e:
            assert 'not created' in str(e), e
        else:
            raise AssertionError('Missing report accepted as empty output')

def quant():
    assert {S.quant_of({'quant': q}) for q in (None, '', 'none', 'n/a', '-')} == {S.NO_QUANT}
    assert S.quant_of({'quant': 'int8'}) == 'int8'

def pairs_not_chains():
    bm = {m: [0.1] * S.B for m in 'abc'}
    assert S.ties(list('abc'), bm) == ['a ≈ b', 'b ≈ c']
    bm['c'] = [0.9] * S.B
    assert S.ties(list('abc'), bm) == ['a ≈ b']

def clipped_spans():
    assert run.clip({'start': 0, 'end': 10}, 9) == (0, 9)
    assert run.clip({'start': 3, 'end': 7}, 9) == (3, 7)
    assert run.clip({'start': 9, 'end': 10}, 9) is None
    assert run.clip({'start': -2, 'end': 4}, 9) == (0, 4)

def incomplete_results():
    ents = [{'start': 0, 'end': 6, 'type': 'SECRET'}]
    with tempfile.TemporaryDirectory() as d:
        f = make(d, [('1', 'Secret', ents)], {'1': []})
        meta = S.read_pred(f)[0]
        cases = [[], [{'id': '1', 'spans': [{'start': 0, 'end': 6, 'label': 'secret'}], 'err': 'controlled failure'}]]
        for rows in cases:
            f.write_text('\n'.join(json.dumps(r) for r in [{'meta': meta}, *rows]) + '\n')
            for load in (lambda: ens.preds('t', 'm'), lambda: SR.load('t', ['m'])):
                try:
                    load()
                except SystemExit:
                    pass
                else:
                    raise AssertionError('Incomplete quality result accepted')
    with tempfile.TemporaryDirectory() as d:
        make(d, [('1', 'Secret', ents)], {'1': []})
        old = (run.BENCH, run.RESULTS, run.CFG.get('audit'), run.LOADERS['natasha'], run.revision, run.versions)
        run.BENCH, run.RESULTS = (Path(d) / 'BENCH', Path(d) / 'RESULTS')
        run.CFG['audit'] = {'family': 'natasha', 'repo': 'audit-local'}
        run.LOADERS['natasha'] = lambda *args, **kwargs: (lambda texts: [], None)
        run.revision = lambda cfg: 'audit-local'
        run.versions = lambda: {}
        try:
            run.main('audit', 't', '16')
            meta, pred = S.read_pred(run.RESULTS / 't' / 'pred.audit.jsonl')
            assert meta['errors'] == 1 and pred['1']['err'] and not pred['1']['spans']
        finally:
            run.BENCH, run.RESULTS, prior, run.LOADERS['natasha'], run.revision, run.versions = old
            if prior is None:
                run.CFG.pop('audit', None)
            else:
                run.CFG['audit'] = prior

def partial_composition():
    four = ['a', 'b', 'c', 'd']
    assert not SR.usable(four, ['a', 'b', 'c'], 2)
    assert SR.usable(four, four, 2)
    assert SR.usable(four, ['a'], 1) and (not SR.usable(four, [], 1))
    assert SR.mark({'have': 3, 'of': 4}) == ' [3/4]' and SR.mark({'have': 4, 'of': 4}) == ''

def corruption():
    groups = {'PERSON': 'PERSON', 'TOKEN': 'SECRET'}
    rows = [('Иванов Иван, ivan@corp.ru', [{'start': 0, 'end': 11, 'type': 'PERSON'}]), ('ключ AKIA1234567890ABCDEF', [{'start': 5, 'end': 25, 'type': 'TOKEN'}]), ('12345678901234567890', []), ('nothing to hide here', [])]
    for i in range(len(rows) * corrupt.VARIANTS):
        text, ents = rows[i % len(rows)]
        out, new = corrupt.corrupt(text, ents, i, groups)
        assert out != text, (i, text)
        assert len(new) == len(ents), (i, new)
        for a, b in zip(ents, new):
            assert 0 <= b['start'] < b['end'] <= len(out), (i, b)
            assert out[b['start']:b['end']].strip() and b['type'] == a['type'], (i, b)


def dataset_binding():
    """F01/F03: a valid prediction of dataset A must not pass for dataset B,
    even with identical row IDs and a correct hash of A; and a correct hash
    must not excuse wrong rows/chars metadata."""
    ents = [{'start': 0, 'end': 4, 'type': 'A'}]
    with tempfile.TemporaryDirectory() as d:
        f = make(d, [('1', 'Иван идёт', ents)], {'1': []}, {'name': 'm'})
        meta = S.read_pred(f)[0] | {'bench_sha256': bench_sha_of('t')}
        f.write_text('\n'.join(json.dumps(r) for r in [{'meta': meta}, {'id': '1', 'spans': [], 'err': None}]) + '\n')
        b2 = S.BENCH / 'u'
        b2.mkdir()
        (b2 / 'meta.json').write_text(json.dumps({'lang': 'ru', 'kind': 'pii', 'source': 'selftest', 'license': '-', 'mode': 'link', 'domain': '-', 'labels': {'en': [], 'ru': []}, 'groups': GROUPS}))
        with (b2 / 'bench.csv').open('w', newline='') as fh:
            fh.write('id,domain,text,entities\n')
            fh.write('1,,"Другой текст","[]"\n')
        try:
            bad = S.check_predictions(f, meta, S.read_pred(f)[1], complete=True, expected='u')
            assert bad and 'expected' in bad, bad
            bad = S.check_data(f, meta | {'rows': 99, 'chars': 999})
            assert bad and 'rows in run' in bad, bad
            bad = S.check_predictions(f, meta | {'name': 'other'}, S.read_pred(f)[1], complete=True, expected='t', expected_model='m')
            assert bad and 'expected' in bad, bad
            bad = S.check_data(f, meta | {'bench': '../t'})
            assert bad, bad
            # A limit larger than the dataset describes the whole slice.
            bad = S.check_data(f, meta | {'limit': 5, 'rows': 99})
            assert bad and 'rows in run' in bad, bad
            ok = S.check_data(f, meta | {'limit': 5})
            assert ok == '', ok
        finally:
            S.BENCH, S.RESULTS = real_paths
            for fn in (S.gold, S.gold_norm, S.chars_of, S.meta_of, S.dirty, S._canon):
                fn.cache_clear()


def bench_sha_of(bench):
    from benchlib import bench_sha256
    return bench_sha256(S.BENCH / bench / 'bench.csv')


real_paths = (S.BENCH, S.RESULTS)


def strict_meta_and_gold():
    """F04: exactly one leading meta record; duplicate gold IDs rejected."""
    ents = [{'start': 0, 'end': 4, 'type': 'A'}]
    with tempfile.TemporaryDirectory() as d:
        f = make(d, [('1', 'Иван идёт', ents)], {'1': []})
        meta = S.read_pred(f)[0]
        body = {'id': '1', 'spans': [], 'err': None}
        for lines, needle in (
                ([{'meta': meta}, body, {'meta': meta | {'rows': 5}}], 'only one'),
                ([body, {'meta': meta}], 'come first'),
                ([{'meta': {}}, {'meta': meta}], 'non-empty object'),
                ([{'meta': [1, 2]}, body], 'non-empty object')):
            f.write_text('\n'.join(json.dumps(r) for r in lines) + '\n')
            try:
                S.read_pred(f)
            except SystemExit as e:
                assert needle in str(e), e
            else:
                raise AssertionError('Malformed meta layout accepted')
        with (S.BENCH / 't' / 'bench.csv').open('w', newline='') as fh:
            fh.write('id,domain,text,entities\n')
            fh.write('1,,"Иван идёт","[]"\n')
            fh.write('1,,"Повтор","[]"\n')
        for fn in (S.gold, S.gold_norm, S.chars_of, S._canon):
            fn.cache_clear()
        try:
            S.gold('t')
        except SystemExit as e:
            assert 'duplicate row id' in str(e), e
        else:
            raise AssertionError('Duplicate gold id accepted')


def scanner_offsets():
    """F02/R01: a repeated secret stays on the occurrence the scanner reported."""
    text = 'example: SAMEVALUE\npassword: SAMEVALUE'
    span = run_leaks.spans_of(text, [('SAMEVALUE', 2, 11, 2, 19)])[0]
    assert (span['start'], span['end']) == (29, 38), span
    span = run_leaks.spans_of(text, [('SAMEVALUE', 1, 11, 1, 19)])[0]
    assert (span['start'], span['end']) == (9, 18), span
    t2 = 'SECRET and SECRET'
    assert run_leaks.spans_of(t2, [('SECRET', 1, 99, 1, 104)])[0].get('unresolved') is True
    t3 = 'line with stuff\nanother SECRET line'
    span = run_leaks.spans_of(t3, [('NOTPRESENT', 2, 9, 2, 18)])[0]
    assert span.get('unresolved') is True and span['start'] == 24, span
    assert run_leaks.spans_of('abc\n def ghi', [(None, 2, None, 2, None)])[0]['end'] == 12
    t4 = 'a: PW\r\nb: PW2'
    assert run_leaks.spans_of(t4, [('PW2', 2, 4, 2, 6)])[0] == {'start': 10, 'end': 13, 'label': 'secret'}


def gitleaks_byte_columns():
    """R01: Gitleaks reports byte columns for the whole Match; the adapter
    converts them to character columns and locates the Secret inside the
    confirmed Match, so a repeated value after multi-byte text keeps the
    occurrence the scanner reported."""
    t = 'яяяяяяяяяя SAMEVALUE SAMEVALUE'
    # Byte columns as Gitleaks 8.30.1 reports them for the first occurrence.
    assert run_leaks.gitleaks_item(t.encode(), {'Secret': 'SAMEVALUE', 'StartLine': 1, 'StartColumn': 22, 'EndLine': 1, 'EndColumn': 30}) == ('SAMEVALUE', 1, 12, 1, 20)
    span = run_leaks.spans_of(t, [run_leaks.gitleaks_item(t.encode(), {'Secret': 'SAMEVALUE', 'StartLine': 1, 'StartColumn': 22, 'EndLine': 1, 'EndColumn': 30})])[0]
    assert (span['start'], span['end']) == (11, 20) and 'unresolved' not in span, span
    # The second occurrence, on the columns the scanner reported for it.
    span = run_leaks.spans_of(t, [run_leaks.gitleaks_item(t.encode(), {'Secret': 'SAMEVALUE', 'StartLine': 1, 'StartColumn': 32, 'EndLine': 1, 'EndColumn': 40})])[0]
    assert (span['start'], span['end']) == (21, 30) and 'unresolved' not in span, span
    # Match with a prefix before the Secret (secretGroup): Secret wins inside the Match.
    t2 = 'key=SECRETVAL tail'
    span = run_leaks.spans_of(t2, [run_leaks.gitleaks_item(t2.encode(), {'Secret': 'SECRETVAL', 'StartLine': 1, 'StartColumn': 1, 'EndLine': 1, 'EndColumn': 15})])[0]
    assert (span['start'], span['end']) == (4, 13), span
    # Multi-line finding: line and column convert to the right character span.
    t3 = 'строка один\nAAA value AAA\nхвост'
    span = run_leaks.spans_of(t3, [run_leaks.gitleaks_item(t3.encode(), {'Secret': 'value', 'StartLine': 2, 'StartColumn': 5, 'EndLine': 2, 'EndColumn': 10})])[0]
    assert t3[span['start']:span['end']] == 'value' and 'unresolved' not in span, span
    # Missing or non-integer columns degrade to a line-only finding, never to a guess:
    # the reported range is kept and the reason is recorded for the consumer.
    assert run_leaks.gitleaks_item(b'x', {'Secret': 'x', 'StartLine': 1}) == ('x', 1, None, None, None, run_leaks.NATIVE)
    # A Secret repeated inside its Match has no recoverable capture: the match
    # range is kept and the reason says why (T01).
    t4 = 'tok_A1b2C3d4 = "tok_A1b2C3d4"'
    item = run_leaks.gitleaks_item(t4.encode(), {'Secret': 'tok_A1b2C3d4', 'Match': t4,
                                                 'StartLine': 1, 'StartColumn': 1,
                                                 'EndLine': 1, 'EndColumn': len(t4) + 1})
    span = run_leaks.spans_of(t4, [item])[0]
    assert span['unresolved_reason'] == 'capture-collision', span
    assert (span['start'], span['end']) != (0, len('tok_A1b2C3d4')), span
    # A finding whose values only exist in decoded content keeps the encoded
    # range, whatever plaintext copy exists elsewhere in the text (T01).
    coded = 'seen: PLAINTEXT\npayload=QUJD'
    item = run_leaks.gitleaks_item(coded.encode(), {'Secret': 'PLAINTEXT', 'Match': 'key=PLAINTEXT',
                                                    'StartLine': 2, 'StartColumn': 10,
                                                    'EndLine': 2, 'EndColumn': 14,
                                                    'Tags': ['decoded:base64', 'decode-depth:1']})
    span = run_leaks.spans_of(coded, [item])[0]
    assert span['unresolved_reason'] == 'decoded' and (span['start'], span['end']) == (24, 28), span


if __name__ == '__main__':
    real = (S.BENCH, S.RESULTS)
    for fn in (coincident, hit_is_a_hit, hidden, out_of_text, stale_and_dupes, scanner_crash, quant, corruption, folds, pairs_not_chains, clipped_spans, incomplete_results, partial_composition, dataset_binding, strict_meta_and_gold, scanner_offsets, gitleaks_byte_columns):
        fn()
        S.BENCH, S.RESULTS = real
    print('selftest ok')
