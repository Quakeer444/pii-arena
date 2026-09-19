"""Export the frozen run without rerunning any detector."""
import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# The frozen experiment, the code that packages it and the released result
# bundle are separate identities (T08): the experiment date is never rewritten
# by a later fix, and `code_version` is read from the single declared source.
EXPERIMENT_DATE = '2026-09-09'
RESULT_REVISION = '2026-09-19'
# Fields a reuse-only export must find unchanged: they are what the published
# numbers were computed from. `sources` holds the SHA-256 of every prediction
# and report file, so a changed input cannot pass as a republish (T03).
REUSE_KEYS = ('threshold', 'datasets', 'measurements', 'ensembles', 'composition_counts', 'sources')


def digest_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def code_version():
    return tomllib.loads((ROOT / 'pyproject.toml').read_text())['project']['version']


def check_reuse(previous, staged):
    """T03: a reuse export may only republish the inputs it was built from.

    Anything that decides a published number - the frozen corpora, the
    measurements, the ensembles, the recomputed compositions and the digests
    of every source file - must be identical to the released snapshot.
    A deliberate rebuild is `--recompute-compositions`, which rewrites those
    fields together with a new result revision."""
    for key in REUSE_KEYS:
        if previous.get(key) != staged.get(key):
            raise ValueError(f'Inputs changed: {key}; use --recompute-compositions for a new result revision')


def _swap(staging, destination, keep_backup=False, preserve=()):
    """Move one staged tree into place, restoring the previous copy on error.

    Files listed in `preserve` exist only in the previous destination (they
    are produced by render.py, not by export) and are copied into staging
    before anything is renamed, so the live tree is never the new export
    without them (T04); the only step left after the rename is removing the
    backup. Crash-atomicity against SIGKILL or a failing disk is not claimed:
    ordinary exceptions are handled.
    """
    backup = destination.with_name(destination.name + '.previous')
    shutil.rmtree(backup, ignore_errors=True)
    had_previous = destination.exists()
    if had_previous:
        for name in preserve:
            source, target = (destination / name, staging / name)
            if source.exists() and not target.exists():
                if source.is_dir():
                    shutil.copytree(source, target)
                else:
                    shutil.copy2(source, target)
        destination.rename(backup)
    try:
        staging.rename(destination)
    except BaseException:
        if had_previous:
            backup.rename(destination)
        raise
    if not keep_backup:
        shutil.rmtree(backup, ignore_errors=True)


RENDER_OUTPUT = ('overview.md', 'by-language.md', 'by-entity.md', 'by-dataset.md',
                 'summary.csv', 'entity-metrics.csv', 'category-metrics.csv',
                 'dataset-metrics.csv', 'types')


def replace_projection(staging_results, staging_catalog, root):
    """Swap both public directories as one consistent operation (F12/R03).

    A failure while switching the second directory must not leave the
    publication with a new snapshot and no datasets catalog. The results
    backup is kept until the catalog swap succeeds; if the catalog swap
    fails, the results swap is rolled back, so the publication is either
    entirely the previous export or entirely the new one. Files produced only
    by render.py are carried over from the previous results tree.
    """
    _swap(staging_results, root / 'results', keep_backup=True, preserve=RENDER_OUTPUT)
    try:
        _swap(staging_catalog, root / 'datasets')
    except BaseException:
        shutil.rmtree(root / 'results', ignore_errors=True)
        (root / 'results').with_name('results.previous').rename(root / 'results')
        raise
    shutil.rmtree((root / 'results').with_name('results.previous'), ignore_errors=True)


def table(text, header):
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith(header))
    columns = [s.strip() for s in lines[start].strip('|').split('|')]
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith('|'):
            break
        cells = [s.strip().replace('**', '') for s in line.strip('|').split('|')]
        if len(cells) != len(columns):
            raise ValueError(f'Table width mismatch: {cells[0]}')
        rows.append(dict(zip(columns, cells)))
    return rows


def number(value):
    return None if value in ('-', '', 'train') else float(re.search(r'-?\d+(?:\.\d+)?', value)[0])


def write_csv(path, rows):
    if not rows:
        raise ValueError(f'No rows for {path}')
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def masking_diagnostics(data, catalog, S, SR):
    members = ['pplx', 'gliner2-fastino', 'mmbert32k', 'bardsai-eu']
    keys = ('gold_original', 'gold_normalized', 'original_fully_hidden_raw',
            'normalized_fully_hidden_raw', 'normalized_fully_hidden_normalized',
            'positive_rows', 'positive_rows_residual_raw',
            'positive_rows_residual_normalized')
    totals = {key: 0 for key in keys}
    for item in catalog:
        bench = item['id']
        gold, normalized = (S.gold(bench)[0], S.gold_norm(bench))
        cooked = SR.load(bench, members)
        raw = {}
        for model in members:
            path = data / 'RESULTS' / bench / f'pred.{model}.jsonl'
            meta, pred = S.read_pred(path)
            if bad := S.check_predictions(path, meta, pred, complete=True, expected=bench, expected_model=model):
                raise ValueError(bad)
            raw[model] = pred
        for rid, (text, entities) in gold.items():
            raw_chars, normalized_chars = (set(), set())
            for model in members:
                raw_chars.update(p for e in S.keep(raw[model][rid]['spans'])
                                 if 0 <= e['start'] < e['end'] <= len(text)
                                 for p in range(e['start'], e['end']))
                normalized_chars.update(S.chars(cooked[model][rid]))
            totals['gold_original'] += len(entities)
            totals['gold_normalized'] += len(normalized[rid])
            totals['original_fully_hidden_raw'] += sum(
                all(p in raw_chars for p in range(e['start'], e['end'])) for e in entities)
            totals['normalized_fully_hidden_raw'] += sum(
                all(p in raw_chars for p in range(a, b)) for a, b, _ in normalized[rid])
            totals['normalized_fully_hidden_normalized'] += sum(
                all(p in normalized_chars for p in range(a, b)) for a, b, _ in normalized[rid])
            totals['positive_rows'] += bool(entities)
            totals['positive_rows_residual_raw'] += bool(entities) and any(
                any(p not in raw_chars for p in range(e['start'], e['end'])) for e in entities)
            totals['positive_rows_residual_normalized'] += bool(normalized[rid]) and any(
                any(p not in normalized_chars for p in range(a, b)) for a, b, _ in normalized[rid])
        for fn in (S.gold, S.gold_norm, S.chars_of, S._canon, S.meta_of):
            fn.cache_clear()
    return {'composition': 'pplx+fastino+bardsai+mmbert', 'members': members, **totals}


REQUIRED_ARTIFACTS = ('snapshot.json', 'composition-counts.json', 'run-inventory.json',
                      'measurements.csv', 'ensembles.csv', 'speed.csv',
                      'report.md', 'ensemble.md', 'secrets.md', 'speed.md')


def export(data, recompute):
    """Stage the whole public projection and swap it in only on success (F12)."""
    os.environ['BENCHMARK_DATA'] = str(data)
    real_results = ROOT / 'results'
    real_results.mkdir(exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='export-staging-', dir=str(real_results.parent)))
    try:
        staging_catalog = staging / 'datasets'
        staging_catalog.mkdir()
        _export(data, recompute, staging / 'results', staging_catalog)
        # R03: a reuse-only export must still produce the complete projection;
        # refuse to switch directories if any companion file is missing.
        missing = [name for name in REQUIRED_ARTIFACTS if not (staging / 'results' / name).exists()]
        missing += [name for name in ('catalog.json', 'samples.json') if not (staging_catalog / name).exists()]
        if missing:
            raise ValueError(f'Staged export is incomplete: missing {missing}')
    except BaseException:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    replace_projection(staging / 'results', staging_catalog, ROOT)
    shutil.rmtree(staging, ignore_errors=True)


def _export(data, recompute, output, datasets_dir):
    sys.path.insert(0, str(ROOT / 'benchmark'))
    import score as S
    import secrets_recall as SR
    import ens as E
    from run_leaks import ADAPTER_STATUS, adapter_status
    output.mkdir(exist_ok=True)
    (output / 'datasets').mkdir(exist_ok=True)
    catalog, measurements, inventory, sources = [], [], [], {}
    for directory in sorted((data / 'BENCH').iterdir()):
        if not (directory / 'meta.json').exists():
            continue
        name = directory.name
        meta = json.loads((directory / 'meta.json').read_text())
        report = (data / 'RESULTS' / name / 'REPORT.md').read_text()
        match = re.search(r'\((\d+) rows, (\d+) spans, (\d+) negatives\)', report)
        if not match:
            raise ValueError(f'Cannot parse dataset totals: {name}')
        rows, gold, negatives = map(int, match.groups())
        with (directory / 'bench.csv').open() as stream:
            original = list(csv.DictReader(stream))
        if rows != len(original):
            raise ValueError(f'Wrong row count: {name}')
        item = {'id': name, 'lang': meta['lang'], 'kind': meta['kind'], 'rows': rows,
                'gold_spans': gold, 'original_annotations': sum(len(json.loads(r['entities'])) for r in original),
                'characters': sum(len(r['text']) for r in original), 'negative_rows': negatives,
                'source': meta['source'], 'license': meta['license'], 'source_mode': meta['mode'],
                'synthetic': name.startswith('synth-'), 'corrupted': name.startswith('corrupt-'),
                'bench_sha256': S.bench_sha256(directory / 'bench.csv'), 'raw': meta.get('raw'),
                'languages': meta.get('langs', {}), 'groups': sorted(set(meta['groups'].values()))}
        catalog.append(item)
        text = report.replace(f'# BENCH/{name}', f'# {name}')
        text = text.replace('`SCRIPTS/', '`benchmark/').replace('`models.toml`', '`benchmark/models.toml`')
        (output / 'datasets' / f'{name}.md').write_text(text)
        sources[f'RESULTS/{name}/REPORT.md'] = hashlib.sha256(report.encode()).hexdigest()
        for row in table(report, '| model | missed |'):
            ci = [float(n) for n in re.findall(r'\d+(?:\.\d+)?', row['missed % [95% CI]'])]
            m = row['model']
            cfg = S.CFG.get(S.base_of(m), {})
            measurements.append({'dataset': name, 'lang': meta['lang'], 'kind': meta['kind'],
                                 'model': m, 'family': cfg.get('family', 'unknown'),
                                 'variant': m.split('+', 1)[1] if '+' in m else 'base',
                                 'missed': int(row['missed']), 'gold_spans': gold,
                                 'missed_pct': 100 * int(row['missed']) / gold if gold else None,
                                 'missed_ci_low_reported': ci[1], 'missed_ci_high_reported': ci[2],
                                 'hidden_pct_reported': number(row['hidden']),
                                 'char_f1_reported': number(row['char F1 [95% CI]']),
                                 'char_precision_reported': number(row['P']),
                                 'char_recall_reported': number(row['R']), 'train': row['train'] == 'train',
                                 'dropped_spans': int(row['dropped spans']),
                                 'fp_rows': row['rows touched'], 'fp_chars': int(row['chars masked'])})
        for prediction in sorted((data / 'RESULTS' / name).glob('pred.*.jsonl')):
            m, pred = S.read_pred(prediction)
            if bad := S.check_predictions(prediction, m, pred, complete=not m.get('limit'), expected=name, expected_model=prediction.stem[5:]):
                raise ValueError(bad)
            allowed = ('name', 'repo', 'revision', 'family', 'protocol', 'bench_sha256', 'variant',
                       'device', 'gpu', 'cpu', 'workers', 'threads', 'quant', 'batch', 'chunk',
                       'chunk_mode', 'overlap', 'normalize', 'threshold', 'labels_lang', 'labels',
                       'limit', 'versions', 'rows', 'pieces', 'chars', 'elapsed_s', 'errors',
                       'started_utc', 'finished_utc', 'rss_mb', 'clipped', 'dropped', 'granularity',
                       'decode_depth', 'confidence', 'ml', 'unresolved_spans', 'unresolved_reasons',
                       'adapter_policy')
            tool = prediction.stem[5:]
            record = {'dataset': name, 'file': prediction.name,
                      **{k: m[k] for k in allowed if k in m},
                      'pred_sha256': digest_file(prediction)}
            # T05: scanner runs carry their release status in the public
            # machine-readable inventory, not only in table labels: the
            # reviewed status of the tool and the mapping policy its metadata
            # records (absent for runs that predate policy recording).
            if tool in ADAPTER_STATUS:
                record['adapter_status'] = m.get('adapter_status') or adapter_status(tool)
            inventory.append(record)
            sources[f'RESULTS/{name}/{prediction.name}'] = digest_file(prediction)
        print(f'Exported reports: {name}', flush=True)
    lookup = {d['id']: d for d in catalog}
    combinations = {name: (members, k) for name, members, k in E.COMBOS}
    ensemble_text = (data / 'RESULTS/ENSEMBLE.md').read_text()
    ensemble = []
    for row in table(ensemble_text, '| composition | alexen2 |'):
        name = row['composition']
        members, k = combinations[name]
        for dataset, value in row.items():
            if dataset == 'composition':
                continue
            missed = int(re.search(r'\((\d+)\)', value)[1]) if value not in ('-', 'train') else None
            ensemble.append({'composition': name, 'members': members, 'votes': k, 'dataset': dataset,
                             'lang': lookup[dataset]['lang'], 'kind': lookup[dataset]['kind'],
                             'status': 'missing' if value == '-' else 'train' if value == 'train' else 'ok',
                             'missed': missed, 'gold_spans': lookup[dataset]['gold_spans']})
    speed = []
    for device in ('cpu', 'cuda'):
        section = (data / 'RESULTS/SPEED.md').read_text().split(f'## {device}\n')[1]
        for row in table(section, '| model | chars/s |'):
            speed.append({'device': device, 'model': row['model'], 'chars_per_second': number(row['chars/s']),
                          'rows_per_second': number(row['rows/s']), 'relative_pplx': number(row['x pplx']),
                          'p50_ms_reported': number(row['amortized ms/row p50']), 'p95_ms_reported': number(row['p95']),
                          'hardware': row['gpu / cpu'], 'threads': row['threads'], 'workers': row['W'],
                          'quant': row['quant'], 'variant': row['variant'], 'rss_mb': number(row['rss MB']),
                          'datasets': int(row['sets'])})
    for filename in ('REPORT.md', 'ENSEMBLE.md', 'SPEED.md', 'SECRETS.md', 'VERDICT.md'):
        original = (data / 'RESULTS' / filename).read_text()
        sources[f'RESULTS/{filename}'] = hashlib.sha256(original.encode()).hexdigest()
        if filename != 'VERDICT.md':
            (output / filename.lower()).write_text(original.replace('SCRIPTS/', 'benchmark/'))
    verdict = (data / 'RESULTS/VERDICT.md').read_text()
    cost_lines = verdict.split('| composition | missed, all 41 |', 1)[1].splitlines()[2:]
    names = ['pplx', 'fastino', 'pplx+fastino', 'pplx+fastino+mmbert', 'pplx+fastino+bardsai+mmbert']
    costs = []
    for name, line in zip(names, cost_lines):
        cells = [c.strip().replace(' ', '') for c in line.strip('|').split('|')]
        if len(cells) != 6:
            raise ValueError('Invalid frozen cost table')
        costs.append({'composition': name, 'cpu_chars_s': int(cells[2]), 'cpu_seconds_10k': float(cells[3]),
                      'gpu_chars_s': int(cells[4]), 'gpu_seconds_10k': float(cells[5]),
                      'mixed_device_estimate': 'bardsai' in name})
    if len(costs) != len(names):
        raise ValueError('Incomplete frozen cost table')
    if recompute:
        selected = {n: combinations[n] for n in ('pplx', 'fastino', 'pplx+fastino', 'pplx+fastino+mmbert',
                    'pplx+fastino+bardsai', 'pplx+fastino+bardsai+mmbert', 'vote2(pplx,opf2,nvidia)')}
        members = sorted({m for ms, _ in selected.values() for m in ms})
        exact = []
        expected = {(x['composition'], x['dataset']): x for x in ensemble}
        for d in catalog:
            name = d['id']
            g = S.gold(name)[0]
            for m in members:
                f = data / 'RESULTS' / name / f'pred.{m}.jsonl'
                if not f.exists():
                    continue
                meta, predictions = S.read_pred(f)
                if bad := S.check_predictions(f, meta, predictions, complete=True, expected=name, expected_model=m):
                    raise ValueError(bad)
            cs = SR.load(name, members)
            for n, (ms, k) in selected.items():
                e = expected[(n, name)]
                if e['status'] != 'ok':
                    continue
                if any(m not in cs for m in ms):
                    raise ValueError(f'Missing selected member: {n}/{name}')
                counts = SR.tally(name, cs, ms, k)
                if (counts['miss'], counts['nspan']) != (e['missed'], e['gold_spans']):
                    raise ValueError(f'Frozen report mismatch: {n}/{name}')
                exact.append({'composition': n, 'dataset': name, **counts})
            print(f'Recomputed and matched compositions: {name}', flush=True)
            for fn in (S.gold, S.gold_norm, S.chars_of, S._canon):
                fn.cache_clear()
        (output / 'composition-counts.json').write_text(json.dumps(exact, indent=2) + '\n')
    else:
        exact = json.loads((ROOT / 'results/composition-counts.json').read_text())
        # R03: a reuse-only export writes the companion file into staging too;
        # previously it was read from the old results and then lost in the swap.
        (output / 'composition-counts.json').write_text(json.dumps(exact, indent=2) + '\n')
    masking = masking_diagnostics(data, catalog, S, SR)
    headline = [r for r in exact if r['composition'] == masking['composition']]
    masking |= {'clean_rows': sum(r['nneg'] for r in headline),
                'clean_rows_touched': sum(r['fire'] for r in headline),
                'clean_characters': sum(r['negchars'] for r in headline),
                'clean_characters_masked': sum(r['extra'] for r in headline)}
    excluded = [d['id'] for d in catalog if d['synthetic'] or d['corrupted']]
    # T08: the frozen experiment, the code that packaged it and the result
    # bundle are three different identities and are named separately here.
    payload = {'schema_version': 3, 'experiment_date': EXPERIMENT_DATE,
               'code_version': code_version(), 'result_revision': RESULT_REVISION,
               'threshold': 0.5,
               'datasets': catalog, 'measurements': measurements, 'ensembles': ensemble,
               'composition_counts': exact, 'masking_diagnostics': masking,
               'sensitivity': {'excluded_dataset_ids': excluded,
                               'included_dataset_ids': [d['id'] for d in catalog if d['id'] not in excluded]},
               'speed': speed, 'costs': costs, 'sources': sources}
    if recompute:
        from stratify import build
        payload['breakdowns'] = build(data, payload)
    else:
        previous = json.loads((ROOT / 'results/snapshot.json').read_text())
        # F11/T03: `sources` carries the SHA-256 of every prediction file, so an
        # edited prediction no longer passes the reuse contract even when its
        # reports are unchanged.
        check_reuse(previous, payload)
        payload['breakdowns'] = previous['breakdowns']
    (output / 'snapshot.json').write_text(json.dumps(payload, ensure_ascii=True, indent=2) + '\n')
    write_csv(output / 'measurements.csv', measurements)
    write_csv(output / 'ensembles.csv', [{**r, 'members': ' + '.join(r['members'])} for r in ensemble])
    write_csv(output / 'speed.csv', speed)
    (output / 'run-inventory.json').write_text(json.dumps(inventory, ensure_ascii=True, indent=2) + '\n')
    (datasets_dir / 'catalog.json').write_text(json.dumps(catalog, ensure_ascii=True, indent=2) + '\n')
    (datasets_dir / 'samples.json').write_bytes((data / 'BENCH/samples.json').read_bytes())
    print(f'Export complete: {len(catalog)} datasets, {len(measurements)} quality rows, {len(inventory)} runs', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=ROOT / '.local/research')
    parser.add_argument('--recompute-compositions', action='store_true')
    args = parser.parse_args()
    export(args.data.resolve(), args.recompute_compositions)
