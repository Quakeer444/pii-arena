"""Build English views from the frozen numeric snapshot."""
import csv
import json
import math
import sys
import tomllib
import re
from collections import defaultdict
from functools import cache
from pathlib import Path

import figures as fx

ROOT = Path(__file__).resolve().parent.parent
S = json.loads((ROOT / 'results/snapshot.json').read_text())
COUNTS = S['composition_counts']
CAT = {d['id']: d for d in S['datasets']}
IDS = sorted(CAT, key=lambda b: (('ru', 'en', 'multi').index(CAT[b]['lang']), CAT[b]['kind'], b))
sys.path.insert(0, str(ROOT / 'benchmark'))
from run_leaks import STATUS_VALUES, adapter_status
# T05: the release status of a scanner row is shown next to the number and is
# also machine-readable in results/run-inventory.json (`adapter_status`).
ADAPTER_TAG = {'historical-pre-fix': 'historical pre-fix', 'corrected-rerun': 'corrected rerun',
               'verified-unchanged': 'verified unchanged'}
assert set(ADAPTER_TAG) == set(STATUS_VALUES)
MODELS = tomllib.loads((ROOT / 'benchmark/models.toml').read_text())['models']
CUTS = [('ru', 'pii'), ('ru', 'secrets'), ('en', 'pii'), ('en', 'secrets'), ('multi', 'pii')]
NAMES = {
    'pplx': 'PPLX', 'fastino': 'Fastino GLiNER2', 'pplx+fastino': 'PPLX + Fastino',
    'pplx+fastino+mmbert': 'PPLX + Fastino + mmBERT',
    'pplx+fastino+bardsai': 'PPLX + Fastino + BardsAI',
    'pplx+fastino+bardsai+mmbert': 'PPLX + Fastino + mmBERT + BardsAI',
}
REFERENCE = 'composition:pplx+fastino+bardsai+mmbert'
MEMBERS = {'pplx', 'gliner2-fastino', 'mmbert32k', 'bardsai-eu'}
# One machine group per device: same processor, workers, threads and variant.
# Dataset counts still differ, so the group is not a same-input speed test.
CPU_GROUP = (('device', 'cpu'), ('hardware', 'AMD EPYC 9K84 96-Core Processor'),
             ('threads', '16'), ('workers', '24'), ('quant', '-'), ('variant', 'cpu-speed'))
GPU_GROUP = (('device', 'cuda'), ('hardware', 'NVIDIA GeForce RTX 5090'), ('workers', '2'),
             ('quant', '-'), ('variant', '-'))
CPU_LABEL = 'AMD EPYC 9K84, 16 threads per process, 24 concurrent workers'
GPU_LABEL = 'NVIDIA GeForce RTX 5090, 2 concurrent workers'


def aggregate(name, cut=None, datasets=None):
    rows = [r for r in COUNTS if r['composition'] == name and
            (cut is None or (CAT[r['dataset']]['lang'], CAT[r['dataset']]['kind']) == cut) and
            (datasets is None or r['dataset'] in datasets)]
    if not rows:
        raise ValueError(f'Missing composition cut: {name}/{cut}')
    return {k: sum(r[k] for r in rows) for k in ('miss', 'nspan', 'hid', 'tp', 'fp', 'fn', 'fire', 'nneg', 'extra', 'negchars')}


def pct(n, d):
    return 100 * n / d if d else math.nan


def format_pct(n, d):
    if not d:
        return 'n/a'
    value = pct(n, d)
    if n < d and round(value, 2) == 100:
        return '>99.99%'
    return '<0.01%' if n and value < 0.01 else f'{value:.2f}%'


def bucket(value, edges):
    """Index of the first edge the value falls under, for the five-step heat scale."""
    return sum(value >= edge for edge in edges)


@cache
def model_totals():
    """Pooled counts per detector configuration over its eligible runs.

    Training-source runs are excluded here exactly as they are in the language
    tables, so a configuration's dataset count is part of its result.
    """
    taxonomy = {(r['dataset'], r['label']): r for r in S['breakdowns']['taxonomy']}
    totals = {}
    for r in S['breakdowns']['results']:
        if not r['system'].startswith('model:') or r['train']:
            continue
        acc = totals.setdefault(r['system'].removeprefix('model:'), defaultdict(int))
        acc['sets'] += 1
        for t in r['types']:
            definition = taxonomy[(r['dataset'], t['label'])]
            acc['gold'] += definition['gold']
            acc['hit'] += t['hit']
            acc['hidden'] += t['hidden']
        for key in ('char_tp', 'char_fp', 'char_fn', 'negative_rows', 'negative_rows_touched',
                    'negative_characters', 'negative_characters_masked'):
            acc[key] += r[key]
    rows = []
    for name, a in totals.items():
        precision = a['char_tp'] / (a['char_tp'] + a['char_fp']) if a['char_tp'] + a['char_fp'] else 0
        recall = a['char_tp'] / (a['char_tp'] + a['char_fn']) if a['char_tp'] + a['char_fn'] else 0
        rows.append({
            'model': name, 'base': name.split('+')[0],
            'family': MODELS.get(name.split('+')[0], {}).get('family', '-'),
            'sets': a['sets'], 'gold': a['gold'], 'missed': a['gold'] - a['hit'], 'hidden': a['hidden'],
            'missed_pct': pct(a['gold'] - a['hit'], a['gold']),
            'hidden_pct': pct(a['hidden'], a['gold']),
            'extra_pct': pct(a['negative_characters_masked'], a['negative_characters']),
            'char_f1': 2 * precision * recall / (precision + recall) if precision + recall else 0,
        })
    return tuple(sorted(rows, key=lambda r: (-r['sets'], r['missed_pct'], r['model'])))


@cache
def speed_group(group):
    """Speed rows of one machine group, fastest first, with derived seconds per 10k characters."""
    rows = []
    for r in S['speed']:
        if any(r[key] != value for key, value in group):
            continue
        rows.append(r | {'model': r['model'].split('+cpu-')[0],
                         'seconds_10k': 10000 / r['chars_per_second']})
    return tuple(sorted(rows, key=lambda r: -r['chars_per_second']))


def category_pools(categories):
    defs = S['breakdowns']['categories']
    selected = [r for r in categories if r['system'] == REFERENCE and not r['train']]
    keys = ('gold', 'original_gold', 'hit', 'hidden', 'raw_hidden', 'original_hidden',
            'characters', 'covered_characters')
    pooled = {}
    for definition in defs:
        rows = [r for r in selected if r['category'] == definition['id']]
        pooled[definition['id']] = {key: sum(r[key] for r in rows) for key in keys}
        pooled[definition['id']]['datasets'] = len(rows)
    return defs, selected, pooled


def figures(categories):
    defs, selected, pooled = category_pools(categories)
    names = list(NAMES)
    totals = {n: aggregate(n) for n in names}
    quality = model_totals()
    complete = [r for r in quality if r['sets'] == len(CAT) and '+' not in r['model']]
    cpu, gpu = speed_group(CPU_GROUP), speed_group(GPU_GROUP)

    fig = fx.Figure('Masking leaves residuals and masks unannotated text',
                    'Six complete configurations on all 41 datasets and 227,466 normalized gold spans',
                    'masking outcome')
    rows = [{'label': NAMES[n], 'focal': n == 'pplx+fastino+bardsai+mmbert',
             'untouched': pct(totals[n]['miss'], totals[n]['nspan']),
             'untouched_text': f"{format_pct(totals[n]['miss'], totals[n]['nspan'])}  ({totals[n]['miss']:,})",
             'residual': pct(totals[n]['nspan'] - totals[n]['hid'], totals[n]['nspan']),
             'residual_text': f"{format_pct(totals[n]['nspan'] - totals[n]['hid'], totals[n]['nspan'])}"
                              f"  ({totals[n]['nspan'] - totals[n]['hid']:,})",
             'extra': pct(totals[n]['extra'], totals[n]['negchars']),
             'extra_text': f"{format_pct(totals[n]['extra'], totals[n]['negchars'])}  ({totals[n]['extra']:,})"}
            for n in names]
    fx.bartable(fig, rows, [
        ('Annotations untouched', 'untouched', 'lower is better  |  scale 0-30%', 30, lambda v: f'{v:.2f}%'),
        ('Not fully hidden', 'residual', 'lower is better  |  scale 0-30%', 30, lambda v: f'{v:.2f}%'),
        ('Characters masked outside annotations', 'extra', 'lower is better  |  scale 0-30%', 30, lambda v: f'{v:.2f}%')],
        label_width=252, value_width=126, pitch=26)
    fig.save(ROOT, 'overview', 'Residual exposure and masking outside annotations',
             ['227,466 normalized gold spans; 2,895,905 characters in 7,566 rows without annotations.',
              'Annotation-based descriptive counts. Unannotated text is not guaranteed to be free of sensitive content.'])

    fig = fx.Figure('Language and task change the answer',
                    'Untouched normalized gold spans; lower is better; every column uses the same datasets in every row',
                    'language cuts')
    rows = []
    for n in names:
        cells = []
        for cut in CUTS:
            r = aggregate(n, cut)
            cells.append((bucket(pct(r['miss'], r['nspan']), (2, 8, 18, 30)), format_pct(r['miss'], r['nspan'])))
        rows.append((NAMES[n], None, cells))
    headers = [(f'{a.upper()} / {b.upper()}',
                f"{sum((d['lang'], d['kind']) == (a, b) for d in CAT.values())} "
                f"{'dataset' if (a, b) == ('ru', 'secrets') else 'datasets'}") for a, b in CUTS]
    fx.heatmap(fig, rows, headers, label_width=252, header_lines=2)
    fig.save(ROOT, 'language-cuts', 'Missed spans by language and task',
             ['Darker cells hold a larger share of untouched annotations. RU / secrets is one synthetic dataset.',
              'MULTI pools source languages and may include English; it is not a per-language guarantee.',
              'Zero observed misses is not a guarantee, and there is no MULTI / secrets dataset in this snapshot.'])

    fig = fx.Figure('Every detector measured on the complete matrix',
                    f'{len(complete)} configurations with all {len(CAT)} datasets and '
                    f"{complete[0]['gold']:,} normalized gold spans; ranked by untouched annotations",
                    'detectors')
    fx.bartable(fig, [{'label': r['model'], 'sub': r['family'], 'focal': r['model'] in MEMBERS,
                       'missed_pct': r['missed_pct'], 'hidden_pct': r['hidden_pct'],
                       'extra_pct': r['extra_pct'], 'char_f1': r['char_f1']} for r in complete], [
        ('Annotations untouched', 'missed_pct', 'lower is better  |  scale 0-100%', 100, lambda v: f'{v:.1f}%'),
        ('Fully hidden', 'hidden_pct', 'higher is better  |  scale 0-100%', 100, lambda v: f'{v:.1f}%'),
        ('Masked outside gold', 'extra_pct', 'lower is better  |  scale 0-40%', 40, lambda v: f'{v:.1f}%'),
        ('Character F1', 'char_f1', 'higher is better  |  scale 0-1', 1, lambda v: f'{v:.3f}')])
    fig.save(ROOT, 'detectors', 'Pooled outcomes for every complete-coverage detector',
             ['Untouched means no predicted character reaches the normalized annotation; fully hidden means every one of its characters is masked.',
              'Configurations with partial coverage are excluded from this chart and listed with their dataset counts in results/detectors.md.',
              'Highlighted rows are the four members of the reference composition. This is a descriptive comparison, not a selected winner.'])

    fig = fx.Figure('CPU cost of one detector pass',
                    f'{CPU_LABEL}; batch throughput under load, not the latency of a single request',
                    'cpu speed')
    fx.lollipop(fig, [{'label': r['model'], 'value': r['seconds_10k'], 'text': fx.short(r['seconds_10k']),
                       'focal': r['model'] in MEMBERS,
                       'right': f"{r['chars_per_second']:,.0f} ch/s   {r['datasets']} sets"} for r in cpu],
                'seconds per 10,000 characters', 'throughput / datasets')
    fig.save(ROOT, 'cpu-speed', 'Measured CPU throughput per detector',
             ['Seconds per 10,000 characters = 10,000 / chars per second, on a log axis.',
              'Saved throughput on one machine group. Dataset counts differ, so this is not a same-input comparison. Other CPU machines are in results/speed.md.',
              'BardsAI, the scanners and the ONNX runs were measured on other machines and are absent here.'])

    fig = fx.Figure('GPU cost of one detector pass',
                    f'{GPU_LABEL}; batch throughput pooled over the datasets of each run',
                    'gpu speed')
    fx.lollipop(fig, [{'label': r['model'], 'value': r['seconds_10k'], 'text': fx.short(r['seconds_10k']),
                       'focal': r['model'] in MEMBERS,
                       'right': f"{r['chars_per_second']:,.0f} ch/s   {r['datasets']} sets"} for r in gpu],
                'seconds per 10,000 characters', 'throughput / datasets')
    fig.save(ROOT, 'gpu-speed', 'Measured GPU throughput per detector',
             ['Seconds per 10,000 characters = 10,000 / chars per second, on a log axis.',
              'BardsAI has no row here: its ONNX graph runs on CPU only, which is why composition GPU cost is a mixed-device estimate.',
              'Rows pool different numbers of datasets; a row measured on few datasets carries less evidence.'])

    fig = fx.Figure('What a detector costs for what it finds',
                    'Untouched annotations against measured cost; both axes are lower is better',
                    'cost and quality')
    lookup = {r['model']: r for r in quality if '+' not in r['model']}
    for rows, label, device in ((cpu, CPU_LABEL, 'CPU'), (gpu, GPU_LABEL, 'GPU')):
        points = [{'x': r['seconds_10k'], 'y': lookup[r['model']]['missed_pct'], 'label': r['model'],
                   'focal': r['model'] in MEMBERS} for r in rows if r['model'] in lookup]
        fx.scatter(fig, points, f'{device} seconds per 10,000 characters, log scale',
                   'Annotations untouched, %', 100, height=380, label_min=30,
                   corner='cheaper and more thorough is down and left', title=f'{device}: {label}')
    fig.save(ROOT, 'speed-quality', 'Detector quality against measured cost',
             ['Quality pools every eligible dataset of a configuration; speed comes from one machine group, so the two axes are different runs.',
              'Configurations without a run in the machine group are absent; dataset coverage differs between points.',
              'No position here is a production safety claim.'])

    costs = S['costs']
    fig = fx.Figure('More detection has a compute cost',
                    'Seconds per 10,000 characters derived from member throughput; lower is better',
                    'composition cost')
    fx.bartable(fig, [{'label': NAMES[r['composition']], 'focal': r['mixed_device_estimate'],
                       'cpu': r['cpu_seconds_10k'], 'gpu': r['gpu_seconds_10k'],
                       'cpu_text': f"{r['cpu_seconds_10k']:.1f} s",
                       'gpu_text': f"{r['gpu_seconds_10k']:.1f} s" + (' mixed device' if r['mixed_device_estimate'] else '')}
                      for r in costs], [
        ('CPU reference, calibrated', 'cpu', 'lower is better  |  scale 0-35 s', 35, lambda v: f'{v:.1f}'),
        ('RTX 5090 reference', 'gpu', 'lower is better  |  scale 0-12 s', 12, lambda v: f'{v:.1f}')],
        label_width=276, value_width=134, pitch=28)
    fig.save(ROOT, 'compute-cost', 'Reference throughput cost',
             ['CPU: AMD EPYC 9K84, W=24, 16 threads per process, calibrated to PPLX at 1,100 chars/s. GPU: RTX 5090, W=2.',
              'The highlighted row includes BardsAI at 8 CPU threads: a different-condition estimate whose GPU column mixes devices.',
              'All composition costs are derived from member throughput; they are not measured end-to-end request times.'])

    fig = fx.Figure('Detected does not mean fully hidden',
                    'Share of normalized gold spans; higher is better; both metrics use the same span boundaries',
                    'detection and hiding')
    fx.bartable(fig, [{'label': NAMES[n], 'focal': n == 'pplx+fastino+bardsai+mmbert',
                       'detected': 100 - pct(totals[n]['miss'], totals[n]['nspan']),
                       'hidden': pct(totals[n]['hid'], totals[n]['nspan'])} for n in names], [
        ('Touched by a prediction', 'detected', 'higher is better  |  scale 0-100%', 100, lambda v: f'{v:.1f}%'),
        ('All characters hidden', 'hidden', 'higher is better  |  scale 0-100%', 100, lambda v: f'{v:.1f}%')],
        label_width=272, value_width=96, pitch=28)
    fig.save(ROOT, 'full-hiding', 'Touched versus fully hidden spans',
             ['227,466 normalized spans. Word-boundary normalization can expand masks.',
              'Neither percentage proves that an original secret is unusable after masking.'])

    chosen = ['pplx', 'gliner2-fastino', 'mmbert32k', 'bardsai-eu', 'rules-ru', 'presidio-ru']
    chosen += [n for n, v in MODELS.items() if v['family'] == 'leaks']
    fig = fx.Figure('Coverage is part of the result',
                    'Eligible base-configuration datasets out of the datasets available in each cut',
                    'coverage')
    rows = []
    for name in chosen:
        cells = []
        for a, b in CUTS:
            eligible = {r['dataset'] for r in S['measurements']
                        if r['model'] == name and not r['train'] and (r['lang'], r['kind']) == (a, b)}
            denominator = sum((d['lang'], d['kind']) == (a, b) for d in CAT.values())
            cells.append((bucket(len(eligible) / denominator, (.01, .34, .67, .99)),
                          f'{len(eligible)}/{denominator}'))
        rows.append((name, None, cells))
    fx.heatmap(fig, rows, [(f'{a.upper()} / {b.upper()}',) for a, b in CUTS], label_width=252)
    fig.save(ROOT, 'coverage', 'Eligible dataset coverage',
             ['This is measurement coverage, not detection quality. A zero can mean a missing run or an excluded source overlap.',
              'Training-source overlaps are excluded. A missing measurement is never counted as a zero-miss result.',
              'Scanners have a narrower intended scope; compare them on their own datasets, not across unequal subsets.'])

    fig = fx.Figure('Full hiding by sensitive-data type',
                    'PPLX + Fastino + mmBERT + BardsAI; one fixed composition on every retained dataset',
                    'data types')
    fx.bartable(fig, [{'label': d['title'], 'sub': d['family'].split(' &')[0].lower(),
                       'hidden': pct(pooled[d['id']]['hidden'], pooled[d['id']]['gold']),
                       'detected': pct(pooled[d['id']]['hit'], pooled[d['id']]['gold']),
                       'gold': pooled[d['id']]['gold'],
                       'gold_text': f"{pooled[d['id']]['gold']:,}  |  {pooled[d['id']]['datasets']} sets"}
                      for d in defs], [
        ('Fully hidden', 'hidden', 'higher is better  |  scale 0-100%', 100, lambda v: f'{v:.1f}%'),
        ('Touched by a prediction', 'detected', 'higher is better  |  scale 0-100%', 100, lambda v: f'{v:.1f}%'),
        ('Normalized gold spans', 'gold', 'category weight in pooled scores', max(p['gold'] for p in pooled.values()), lambda v: f'{v:,}')],
        label_width=252, value_width=118, pitch=26)
    fig.save(ROOT, 'entity-types', 'Fully hidden and detected spans by data type',
             ['Full hiding uses normalized word-boundary masks; detected means at least one character was touched.',
              'Usernames are not necessarily secret, and organizations and locations depend on context.',
              'All original source labels are preserved in results/entity-metrics.csv.'])

    fig = fx.Figure('Raw offsets and expanded masks differ',
                    'Same normalized gold spans, four-member composition; only the applied mask changes',
                    'mask boundaries')
    fx.bartable(fig, [{'label': d['title'], 'sub': d['family'].split(' &')[0].lower(),
                       'raw': pct(pooled[d['id']]['raw_hidden'], pooled[d['id']]['gold']),
                       'expanded': pct(pooled[d['id']]['hidden'], pooled[d['id']]['gold'])} for d in defs], [
        ('Raw detector offsets', 'raw', 'higher is better  |  scale 0-100%', 100, lambda v: f'{v:.1f}%'),
        ('Word-boundary masks', 'expanded', 'higher is better  |  scale 0-100%', 100, lambda v: f'{v:.1f}%')],
        label_width=252, value_width=96, pitch=26)
    fig.save(ROOT, 'raw-offsets', 'Raw and normalized mask full hiding by type',
             ['Do not use expanded-mask percentages for an application that applies raw detector offsets.',
              'These categories do not measure label correctness or whether a partially hidden credential stays usable.'])

    fig = fx.Figure('What the benchmark contains',
                    'Normalized gold spans per presentation category; larger categories carry more weight in pooled scores',
                    'composition of the corpus')
    fx.bartable(fig, [{'label': d['title'], 'sub': d['family'].split(' &')[0].lower(),
                       'gold': pooled[d['id']]['gold'],
                       'gold_text': f"{pooled[d['id']]['gold']:,}  |  {pooled[d['id']]['datasets']} datasets"}
                      for d in defs], [
        ('Normalized gold spans', 'gold', 'annotation units, not distinct people',
         max(p['gold'] for p in pooled.values()), lambda v: f'{v:,}')],
        label_width=252, value_width=180, pitch=26)
    fig.save(ROOT, 'category-distribution', 'Benchmark category support',
             ['These are annotation units, not distinct people or unique credentials.',
              'Nested and differently labeled annotations remain separate rows in the source data.',
              'Category families are an explanatory grouping, not a legal determination.'])

    head = [r for r in COUNTS if r['composition'] == REFERENCE.removeprefix('composition:')]
    influential = sorted(head, key=lambda r: (-(r['nspan'] - r['hid']), r['dataset']))[:10]
    total = sum(r['nspan'] - r['hid'] for r in head)
    shown = sum(r['nspan'] - r['hid'] for r in influential)
    fig = fx.Figure('Where residual exposure comes from',
                    'Ten largest contributions for the same four-member composition; every other dataset stays in the total',
                    'dataset influence')
    fx.bartable(fig, [{'label': r['dataset'], 'sub': f"{format_pct(r['hid'], r['nspan'])} hidden",
                       'residual': r['nspan'] - r['hid'],
                       'residual_text': f"{r['nspan'] - r['hid']:,} / {r['nspan']:,}"} for r in influential], [
        ('Normalized spans not fully hidden', 'residual', 'absolute count, not a rate',
         max(r['nspan'] - r['hid'] for r in influential), lambda v: f'{v:,}')],
        label_width=252, value_width=190, pitch=26)
    fig.save(ROOT, 'dataset-influence', 'Dataset contributions to residual spans',
             [f'These ten contribute {shown:,} of {total:,} residual spans; the other datasets contribute {total - shown:,}.',
              'A large contribution can reflect dataset size, annotation policy or difficulty. It is not proof of defective data.'])

    fig = fx.Figure('The dataset mix changes the percentage',
                    'Fully hidden normalized spans under three weightings of the same predictions',
                    'weighting sensitivity')
    remaining = set(S['sensitivity']['included_dataset_ids'])
    rows = []
    for n in names:
        every = [r for r in COUNTS if r['composition'] == n]
        subset = [r for r in every if r['dataset'] in remaining]
        rows.append({'label': NAMES[n], 'focal': n == 'pplx+fastino+bardsai+mmbert',
                     'pooled': pct(sum(r['hid'] for r in every), sum(r['nspan'] for r in every)),
                     'macro': 100 * sum(r['hid'] / r['nspan'] for r in every) / len(every),
                     'subset': pct(sum(r['hid'] for r in subset), sum(r['nspan'] for r in subset))})
    fx.bartable(fig, rows, [
        ('All 41, span-weighted', 'pooled', 'higher is better  |  scale 0-100%', 100, lambda v: f'{v:.2f}%'),
        ('All 41, equal dataset weight', 'macro', 'higher is better  |  scale 0-100%', 100, lambda v: f'{v:.2f}%'),
        ('Remaining 32, span-weighted', 'subset', 'higher is better  |  scale 0-100%', 100, lambda v: f'{v:.2f}%')],
        label_width=252, value_width=100, pitch=28)
    fig.save(ROOT, 'dataset-mix', 'Full-hiding sensitivity to dataset weighting',
             ['Remaining 32 excludes six project-generated synthetic sets and three corrupted copies; upstream synthetic data remains.',
              'This is a descriptive sensitivity analysis, not a new selection or a held-out test split.'])

    fig = fx.Figure('Every dataset stays visible',
                    'Fully hidden normalized spans; higher is better; the same dataset appears in every column',
                    'all datasets')
    lookup = {(r['composition'], r['dataset']): r for r in COUNTS}
    rows = []
    for dataset in IDS:
        cells = []
        for n in names:
            r = lookup[(n, dataset)]
            cells.append((bucket(pct(r['hid'], r['nspan']), (25, 55, 80, 95)),
                          format_pct(r['hid'], r['nspan'])))
        rows.append((f"{dataset}   n={CAT[dataset]['gold_spans']:,}",
                     f"{CAT[dataset]['lang'].upper()} / {CAT[dataset]['kind']}", cells))
    fx.heatmap(fig, rows, [('PPLX',), ('Fastino',), ('P + F',), ('P + F + M',), ('P + F + B',), ('P + F + M + B',)],
               label_width=290, cell_height=22)
    fig.save(ROOT, 'dataset-heatmap', 'Full hiding across every frozen dataset',
             ['P = PPLX, F = Fastino, M = mmBERT, B = BardsAI. n = normalized gold spans in that dataset.',
              'Rows are ordered by language, task and identifier, and are never removed for a low score.',
              '100% means zero observed residuals on that sample, not zero population risk.'])
    return len(list((ROOT / 'assets').glob('*.svg')))


def markdown():
    rows = []
    out = ['# Results at a glance', '', 'Frozen predictions: **2026-09-09**. The rows below cover the same **41 datasets and 227,466 normalized gold spans**. All are fixed unions, except the single-model rows. No disclosed training-source overlap was identified for these members; undisclosed overlap remains possible.', '',
           'Model names: **PPLX** = `pplx`; **Fastino** = `gliner2-fastino`; **mmBERT** = `mmbert32k`; **BardsAI** = `bardsai-eu`. Exact repositories and revisions are in the [model catalog](../docs/models.md).', '']
    mask = S['masking_diagnostics']
    out += ['## Headline masking outcome', '',
            'For **PPLX + Fastino + mmBERT + BardsAI**, detection and masking answer different questions:', '',
            '| Diagnostic | Exact count | Rate |', '|---|---:|---:|',
            f"| Normalized entities untouched | {aggregate(mask['composition'])['miss']:,} / {mask['gold_normalized']:,} | {format_pct(aggregate(mask['composition'])['miss'], mask['gold_normalized'])} |",
            f"| Normalized entities not fully hidden after boundary expansion | {mask['gold_normalized'] - mask['normalized_fully_hidden_normalized']:,} / {mask['gold_normalized']:,} | {format_pct(mask['gold_normalized'] - mask['normalized_fully_hidden_normalized'], mask['gold_normalized'])} |",
            f"| Normalized entities not fully hidden using raw offsets | {mask['gold_normalized'] - mask['normalized_fully_hidden_raw']:,} / {mask['gold_normalized']:,} | {format_pct(mask['gold_normalized'] - mask['normalized_fully_hidden_raw'], mask['gold_normalized'])} |",
            f"| Rows with annotations retaining exposed characters after expansion | {mask['positive_rows_residual_normalized']:,} / {mask['positive_rows']:,} | {format_pct(mask['positive_rows_residual_normalized'], mask['positive_rows'])} |",
            f"| Rows without annotations touched by a mask | {mask['clean_rows_touched']:,} / {mask['clean_rows']:,} | {format_pct(mask['clean_rows_touched'], mask['clean_rows'])} |",
            f"| Characters masked in rows without annotations | {mask['clean_characters_masked']:,} / {mask['clean_characters']:,} | {format_pct(mask['clean_characters_masked'], mask['clean_characters'])} |", '',
            f"Raw detector offsets fully cover {mask['original_fully_hidden_raw']:,} of {mask['gold_original']:,} original annotations. This uses a different denominator from normalized masking. These are annotation-based measurements, not a production leak probability; rows without annotations are not guaranteed to be free of sensitive content.", '',
            '## Complete-composition comparison', '',
            '| Composition | Missed spans | Missed % | Residual after masking | Residual % | Macro missed % | Unannotated rows touched % | Unannotated characters masked % |',
            '|---|---:|---:|---:|---:|---:|---:|---:|']
    for n,label in NAMES.items():
        r=aggregate(n); per=[x['miss']/x['nspan'] for x in COUNTS if x['composition']==n]; macro=100*sum(per)/len(per)
        row={'composition':n,**r,'missed_pct':pct(r['miss'],r['nspan']),'residual':r['nspan']-r['hid'],'residual_pct':pct(r['nspan']-r['hid'],r['nspan']),'macro_missed_pct':macro};rows.append(row)
        out.append(f"| {label} | {r['miss']:,} / {r['nspan']:,} | {format_pct(r['miss'],r['nspan'])} | {r['nspan']-r['hid']:,} / {r['nspan']:,} | {format_pct(r['nspan']-r['hid'],r['nspan'])} | {macro:.2f}% | {format_pct(r['fire'],r['nneg'])} | {format_pct(r['extra'],r['negchars'])} |")
    out += ['', '`Missed` means no predicted character touches the normalized gold span. `Residual` means at least one normalized gold character remains visible after word-boundary expansion. Macro gives each dataset equal weight. The unannotated columns use only rows with no gold spans; rows without annotations are not guaranteed to be free of sensitive content. Exact numerators are in [summary.csv](summary.csv).', '',
            '## By language and task', '', '| Composition | RU / PII | RU / secrets | EN / PII | EN / secrets | MULTI / PII |', '|---|---:|---:|---:|---:|---:|']
    for n,label in NAMES.items():
        out.append('| '+label+' | '+' | '.join(format_pct(aggregate(n,c)['miss'],aggregate(n,c)['nspan']) for c in CUTS)+' |')
    out += ['', '**RU / secrets is one synthetic dataset.** There is no MULTI / secrets cut. MULTI is an aggregate of multilingual corpora, including some English; it does not certify every language. Counts and sources are in the [dataset catalog](../docs/datasets.md).', '',
            '## Weighting sensitivity', '',
            'The fixed compositions below are rescored without this project\'s six synthetic datasets and three corrupted copies. The remaining 32 datasets still include upstream synthetic material. No composition was re-selected for this cut.', '',
            '| Composition | All 41 pooled | All 41 macro | Project synthetic | Corrupted copies | Remaining 32 pooled |',
            '|---|---:|---:|---:|---:|---:|']
    synthetic = {d['id'] for d in S['datasets'] if d['synthetic']}
    corrupted = {d['id'] for d in S['datasets'] if d['corrupted']}
    remaining = set(S['sensitivity']['included_dataset_ids'])
    for n in ('pplx+fastino', 'pplx+fastino+mmbert', 'pplx+fastino+bardsai+mmbert'):
        all_rows = [x for x in COUNTS if x['composition'] == n]
        vals = [aggregate(n), aggregate(n, datasets=synthetic), aggregate(n, datasets=corrupted), aggregate(n, datasets=remaining)]
        cell = lambda r: f"{r['miss']:,}/{r['nspan']:,} ({format_pct(r['miss'], r['nspan'])})"
        macro = 100 * sum(x['miss'] / x['nspan'] for x in all_rows) / len(all_rows)
        out.append(f"| {NAMES[n]} | {cell(vals[0])} | {macro:.2f}% | {cell(vals[1])} | {cell(vals[2])} | {cell(vals[3])} |")
    out += ['', 'The dev/test assignment remains frozen by source lineage and row identity. This sensitivity view changes only the reporting denominator; it does not create an independently held-out deployment result.', '',
            '## Reference compute cost', '', '| Composition | CPU seconds / 10k chars | GPU seconds / 10k chars | Qualification |', '|---|---:|---:|---|']
    for r in S['costs']:
        out.append(f"| {NAMES[r['composition']]} | {r['cpu_seconds_10k']:.1f} | {r['gpu_seconds_10k']:.1f} | {'Different CPU conditions; GPU column includes CPU-only BardsAI' if r['mixed_device_estimate'] else 'Derived from member throughput'} |")
    out += ['', 'CPU: AMD EPYC 9K84, W=24 processes, 16 threads each; calibrated through a same-condition PPLX reference at 1,100 chars/s. GPU: RTX 5090, W=2. BardsAI was measured with 8 CPU threads. Sequential composition cost is derived by summing inverse member throughput. These are throughput costs under load, **not isolated 16-thread service latency** or direct end-to-end composition measurements.', '',
            '## Choosing a starting point', '', 'PPLX + Fastino is the smallest complete union highlighted here. Adding mmBERT lowers the observed missed count from 7,872 to 4,746 and supports CPU and GPU execution. Adding BardsAI as a fourth member leaves 3,254 untouched spans, with more masking and a CPU-only step. Choose against your own content and latency requirement; these are fixed candidates, not an optimized or independently held-out winner.', '',
            'The tested two-of-three vote uses different members and has 40 eligible datasets, so it is excluded from these same-coverage charts. Its 59,252 misses out of 218,075 gold spans are available in the [ensemble report](ensemble.md). This does not establish that every voting scheme is inferior.', '',
            'The pooled figures are descriptive. Use the per-dataset confidence intervals and paired comparisons before calling a difference reliable. Comparisons from reports do not supply a new pooled confidence interval.', '',
            '## Explore the evidence', '', '- [Every base model by language and task](by-language.md)', '- [Full quality report, variants and quantization](report.md)', '- [All fixed ensembles and paired comparisons](ensemble.md)', '- [Secrets and masking tradeoffs](secrets.md)', '- [Measured speed and hardware groups](speed.md)', '- [Run metadata inventory](run-inventory.json)', '- [Methods](../docs/methodology.md) and [limitations](../docs/limitations.md)', '']
    (ROOT/'results/overview.md').write_text('\n'.join(out))
    with (ROOT/'results/summary.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,rows[0]);w.writeheader();w.writerows(rows)
    language=['# Base models by language and task','','Coverage-first listing, then observed missed percentage within equal coverage counts. Equal counts do not imply equal dataset subsets: this is **not a leaderboard across unequal subsets**. Missing and training-source runs are excluded, never counted as perfect detections. Inspect the linked per-dataset reports.','','A `-ru` suffix changes zero-shot labels to Russian using the same weights. Such runs apply only to Russian cuts. Chunking variants are in the [full quality report](report.md).','','**Scanner rows use mixed adapter status (2026-09-18 capture and decoded-content correction).** `gitleaks` rows use corrected positions from a rerun whose mapping policy is recorded in the run inventory; `detect-secrets` was re-run and matched its stored predictions; every other scanner row (`betterleaks`, `trufflehog`, `noseyparker`, `titus`, `kingfisher`, `credsweeper`, `credsweeper-noml`, `deepsecrets`) is a historical result produced before the correction and is marked historical. Scanner coverage is partial; see the [scanner status table](../docs/reproduce.md#scanner-adapter-status).','']
    for a,b in CUTS:
        sets=[d for d in CAT.values() if (d['lang'],d['kind'])==(a,b)]
        language += [f'## {a.upper()} / {b.upper()}', '',f"{len(sets)} datasets, {sum(d['gold_spans'] for d in sets):,} normalized gold spans. " + ('Synthetic-only secrets evaluation.' if (a,b)==('ru','secrets') else ''),'', '| Model | Eligible sets | Missed / eligible gold | Missed % |', '|---|---:|---:|---:|']
        pooled=[]
        for name in MODELS:
            records=[r for r in S['measurements'] if r['model']==name and not r['train'] and (r['lang'],r['kind'])==(a,b)]
            if records:
                miss=sum(r['missed'] for r in records);gold=sum(r['gold_spans'] for r in records)
                pooled.append((name,len(records),miss,gold))
        for name,count,miss,gold in sorted(pooled,key=lambda r:(-r[1],r[2]/r[3],r[0])):
            status = adapter_status(name)
            tag = f' *({ADAPTER_TAG[status]})*' if status in ADAPTER_TAG else ''
            language.append(f'| {name}{tag} | {count}/{len(sets)} | {miss:,} / {gold:,} | {format_pct(miss,gold)} |')
        language += ['', '`Missed` means no predicted character touches the normalized annotation; it says nothing about full hiding. A detector that touches nearly every annotation can still leave characters exposed, and one that hides well can mask text without annotations. Full-hiding and extra-masking outcomes for the fixed reference composition are in the [overview](overview.md#headline-masking-outcome).', '', 'Datasets: '+', '.join(f"[{d['id']}](datasets/{d['id']}.md)" for d in sets)+'.', '']
    (ROOT/'results/by-language.md').write_text('\n'.join(language))
    datasets=['# Dataset catalog','','41 datasets, 41,643 rows, 230,446 original annotations; scoring normalization leaves 227,466 gold spans. Raw texts and annotations are stored only in the ignored local workspace. Public metadata, source links, row-selection IDs, checksums and aggregate results remain available.','','The `synthetic` flag in the machine-readable catalog identifies only this project\'s six `synth-*` datasets; other sources also contain synthetic material. Corrupted copies inherit their source and training-overlap exclusions. License labels describe the archived 2026-09-05 source audit, not a fresh legal review.','','| Dataset | Language | Task | Rows | Normalized spans | Source license | Report |','|---|---|---|---:|---:|---|---|']
    for d in CAT.values():
        sources = re.findall(r'https://[^\s)]+', d['source'])
        if len(sources) == 1:
            link = f"[{d['id']}]({sources[0]})"
        elif sources:
            refs = ' + '.join(f"[{url.rstrip('/').rsplit('/', 1)[-1]}]({url})" for url in sources)
            link = f"{d['id']} ({refs}; rule test cases)"
        else:
            link = d['id']
        datasets.append(f"| {link} | {d['lang']} | {d['kind']} | {d['rows']:,} | {d['gold_spans']:,} | {d['license']} | [Results](../results/datasets/{d['id']}.md) |")
    missing_revision = [d['id'] for d in CAT.values() if not d.get('raw') or d['raw'].get('revision') in (None, '-')]
    datasets += ['', '## Reconstruction status', '', 'The public Leak Museum route is tested from source download through CPU inference and scoring. The following 22 historical cuts have no retained raw-source revision and cannot be reconstructed exactly from an upstream revision alone:', '', ', '.join(f'`{name}`' for name in missing_revision) + '.', '', 'A retained aggregate raw hash identifies the archived bytes where available but does not make a newer upstream download equivalent. Other dependency and acquisition gaps are documented in [source acquisition](sources.md).', '', 'See [source acquisition and conversion caveats](sources.md), [license notices](../LICENSES/README.md), [catalog.json](../datasets/catalog.json) and [samples.json](../datasets/samples.json). A source publication mode of `files` in archived metadata describes the original experiment; this repository distributes no corpus text.','']
    (ROOT/'docs/datasets.md').write_text('\n'.join(datasets))
    models=['# Detector catalog','','62 execution records: 50 model configurations (40 distinct weights, eight Russian-label variants, two mirrors), ten secret-scanner configurations, one rules layer and Presidio. A catalog entry does not imply a completed run. The `cpu` catalog flag controls the planned CPU sweep, not a universal capability claim.','','| Record | Family | Upstream | Pinned revision/version | Flags |','|---|---|---|---|---|']
    model_catalog=[]
    for n,c in MODELS.items():
        repo=c['repo'];url=('https://'+repo if repo.startswith('github.com/') else 'https://huggingface.co/'+repo)
        upstream=f'[{repo}]({url})' if ('/' in repo and ' + ' not in repo and not repo.startswith(('SCRIPTS/','benchmark/'))) else repo.replace('SCRIPTS/','benchmark/')
        flags=[]
        if c.get('mirror'):flags.append('mirror of '+c['mirror'])
        if c.get('labels')=='ru':flags.append('Russian labels')
        if c.get('disputed'):flags.append('disputed scope')
        if c.get('contaminated'):flags.append('source overlap: '+', '.join(c['contaminated']))
        models.append(f"| {n} | {c['family']} | {upstream} | `{c['revision']}` | {'; '.join(flags) or '-'} |")
        model_catalog.append({'id':n,'family':c['family'],'upstream':url if '/' in repo and ' + ' not in repo and not repo.startswith(('SCRIPTS/','benchmark/')) else None,'revision':c['revision'],'flags':'; '.join(flags) or '-'})
    models += ['','## Training-source evidence','','`train` is a conservative source-overlap exclusion, not proof of memorization. An empty list is absence of known evidence, not proof of independence. Exclusions extend to other cuts and corrupted copies of the same source and to identical-weight records.','']
    for n,c in MODELS.items():models.append(f"- **{n}:** {c.get('train','Not disclosed.')}")
    models += ['','Exact execution settings are in [models.toml](../benchmark/models.toml), observed runtimes in [run-inventory.json](../results/run-inventory.json), and measured coverage in [by-language.md](../results/by-language.md). Model and scanner software licenses are controlled by their upstream projects; this project\'s MIT license does not relicense their weights.','']
    (ROOT/'docs/models.md').write_text('\n'.join(models))
    (ROOT/'results/model-catalog.json').write_text(json.dumps(model_catalog,indent=2)+'\n')


def csv_file(name, rows):
    with (ROOT / 'results' / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def detail_rows():
    b = S['breakdowns']
    taxonomy = {(r['dataset'], r['label']): r for r in b['taxonomy']}
    labels, categories, datasets = [], [], []
    for r in b['results']:
        grouped = defaultdict(lambda: defaultdict(int))
        for t in r['types']:
            definition = taxonomy[(r['dataset'], t['label'])]
            values = {key: definition[key] for key in ('gold', 'original_gold', 'characters')}
            values.update({key: t.get(key, 0) for key in ('hit', 'hidden', 'raw_hidden', 'original_hidden', 'covered_characters')})
            common = {key: r[key] for key in ('system', 'dataset', 'train')}
            labels.append(common | {'label': t['label'], 'group': definition['group'], 'category': definition['category']} | values)
            for key, value in values.items():
                grouped[definition['category']][key] += value
        categories += [common | {'category': key} | dict(values) for key, values in grouped.items()]
        row = {key: value for key, value in r.items() if key != 'types'}
        row.update({key: sum(g[key] for g in grouped.values()) for key in ('gold', 'original_gold', 'hit', 'hidden', 'raw_hidden', 'original_hidden')})
        p, recall = (row['char_tp'] / (row['char_tp'] + row['char_fp']) if row['char_tp'] + row['char_fp'] else 0,
                     row['char_tp'] / (row['char_tp'] + row['char_fn']) if row['char_tp'] + row['char_fn'] else 0)
        row.update(char_precision=p, char_recall=recall, char_f1=2*p*recall/(p+recall) if p+recall else 0)
        datasets.append(row)
    return labels, categories, datasets


def detail_views(labels, categories, datasets):
    csv_file('entity-metrics.csv', labels)
    csv_file('category-metrics.csv', categories)
    csv_file('dataset-metrics.csv', datasets)
    defs = S['breakdowns']['categories']
    titles = {d['id']: d['title'] for d in defs}
    reference = 'composition:pplx+fastino+bardsai+mmbert'
    selected = [r for r in categories if r['system'] == reference and not r['train']]
    pooled = {}
    for definition in defs:
        rows = [r for r in selected if r['category'] == definition['id']]
        pooled[definition['id']] = {key: sum(r[key] for r in rows) for key in
            ('gold', 'original_gold', 'hit', 'hidden', 'raw_hidden', 'original_hidden', 'characters', 'covered_characters')}
    ids = IDS
    head = [r for r in COUNTS if r['composition'] == reference.removeprefix('composition:')]
    out=['# Results by sensitive-data type','','All figures and tables on this page use **PPLX + Fastino + mmBERT + BardsAI**, threshold 0.5. The same fixed composition is used in every cell. It is an illustration of category behavior, not an independently selected winner.','','![Full hiding by data type](../assets/entity-types.svg)','','## Pooled category results','','| Category | Fully hidden / normalized gold | Hidden % | Detected % | Raw mask / same normalized gold | Raw mask / original annotations | Datasets |','|---|---:|---:|---:|---:|---:|---:|']
    for d in defs:
        r=pooled[d['id']]
        out.append(f"| {d['title']} | {r['hidden']:,} / {r['gold']:,} | {format_pct(r['hidden'],r['gold'])} | {format_pct(r['hit'],r['gold'])} | {format_pct(r['raw_hidden'],r['gold'])} | {r['original_hidden']:,}/{r['original_gold']:,} ({format_pct(r['original_hidden'],r['original_gold'])}) | {sum(x['category']==d['id'] for x in selected)} |")
    out += ['', 'The last two percentage columns have explicitly different gold boundaries. A source label remains a separate annotation unit after normalization even if another label has the same boundaries. The presentation mapping does not change scoring protocol 1. No per-category precision is invented from label-blind masks: false-positive characters cannot be uniquely assigned to a gold category.', '',
            'Credentials groups include passwords, keys, tokens and explicitly labeled usernames/logins. Customer IDs, employee references, badge numbers and ambiguous social identifiers have their own row. Some upstream SECRET labels describe salts, UUIDs or resource identifiers; this chart preserves their source annotation policy and does not assert that every value is a usable secret. Dates include only the date/time labels actually retained in the frozen inputs.', '',
            '## Every category on every contributing dataset', '',
            'Dataset order is stable. Absent categories are not measured and do not become 100%. Counts below 100 spans are marked small; the cutoff is a display convention, not a confidence bound. All entries remain in the CSV.', '']
    for d in defs:
        out += [f"### {d['title']}",'','| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |','|---|---:|---:|---:|---:|---|']
        for r in sorted((x for x in selected if x['category']==d['id']),key=lambda r:ids.index(r['dataset'])):
            out.append(f"| [{r['dataset']}](types/{r['dataset']}.md) | {r['gold']:,} | {r['hidden']:,} ({format_pct(r['hidden'],r['gold'])}) | {format_pct(r['hit'],r['gold'])} | {format_pct(r['raw_hidden'],r['gold'])} | {'small' if r['gold']<100 else '-'} |")
        out.append('')
    out += ['## All detectors, configurations and original labels','','[category-metrics.csv](category-metrics.csv) contains exact category counts for every measured configuration and the seven recomputed compositions. [entity-metrics.csv](entity-metrics.csv) retains the original source labels. [dataset-metrics.csv](dataset-metrics.csv) adds exact character precision/recall/F1 and document residuals. Training-source rows are marked and excluded from pooled results. Missing runs have no fabricated rows.','','[Metric and taxonomy contract](../docs/metrics.md) · [Dataset effects](by-dataset.md) · [Methods compared with other projects](../docs/comparison.md)','']
    (ROOT/'results/by-entity.md').write_text('\n'.join(out))

    out=['# Dataset effects','','Every frozen dataset remains in the headline. A low result can reflect content, annotation policy, conversion, or detector errors; aggregate scores alone do not identify which.','','![Every dataset and complete composition](../assets/dataset-heatmap.svg)','','## Four-member composition on every dataset','','| Dataset | Language/task | Gold | Fully hidden | Raw original hiding | Character P / R / F1 | Rows retaining residuals | Unannotated rows touched |','|---|---|---:|---:|---:|---|---:|---:|']
    for b in ids:
        r=next(r for r in datasets if r['system']==reference and r['dataset']==b)
        out.append(f"| [{b}](types/{b}.md) | {CAT[b]['lang']} / {CAT[b]['kind']} | {r['gold']:,} | {r['hidden']:,} ({format_pct(r['hidden'],r['gold'])}) | {r['original_hidden']:,}/{r['original_gold']:,} ({format_pct(r['original_hidden'],r['original_gold'])}) | {r['char_precision']:.3f} / {r['char_recall']:.3f} / {r['char_f1']:.3f} | {r['residual_rows']:,}/{r['positive_rows']:,} | {r['negative_rows_touched']:,}/{r['negative_rows']:,} |")
    out += ['', 'A zero denominator means that outcome cannot be measured on this dataset. Character P/R/F1 use the normalized mask over all rows. Unannotated rows are not guaranteed to be free of sensitive data.', '', '## Influence of each dataset', '',
            'This counterfactual removes one dataset at a time from the same fixed composition. A positive change means the remaining average would increase. No dataset is actually removed from the headline, and the change is not an estimate of data quality.', '',
            '| Dataset | Gold weight | Residual spans | Share of residuals | Hidden % without this dataset | Change, percentage points |', '|---|---:|---:|---:|---:|---:|']
    total_gold=sum(r['nspan'] for r in head);total_hidden=sum(r['hid'] for r in head)
    for r in sorted(head,key=lambda r:(-(r['nspan']-r['hid']),r['dataset'])):
        without=pct(total_hidden-r['hid'],total_gold-r['nspan'])
        out.append(f"| {r['dataset']} | {format_pct(r['nspan'],total_gold)} | {r['nspan']-r['hid']:,} | {format_pct(r['nspan']-r['hid'],total_gold-total_hidden)} | {without:.2f}% | {without-pct(total_hidden,total_gold):+.2f} |")
    out += ['', '![Dataset contributions](../assets/dataset-influence.svg)', '', '![Mix sensitivity](../assets/dataset-mix.svg)', '',
            'The [overview](overview.md) includes the predeclared sensitivity subset and missed-span counts. The remaining 32 cuts still contain upstream synthetic material. [Source conversion notes](../docs/sources.md) explain dropped labels, reconstructed text, language heuristics, nested annotations and incomplete labeling.', '',
            '## Exact results for every configuration','','Per-dataset category pages below contain all measured model configurations and recomputed compositions, with training-source overlaps marked. Original-label counts are in [entity-metrics.csv](entity-metrics.csv). Dataset totals and masking tradeoffs are in [dataset-metrics.csv](dataset-metrics.csv).','']
    out += [f"- [{b}](types/{b}.md): [historical report and bootstrap intervals](datasets/{b}.md)." for b in ids]
    (ROOT/'results/by-dataset.md').write_text('\n'.join(out)+'\n')
    (ROOT/'results/types').mkdir(exist_ok=True)
    for b in ids:
        out=[f'# {b}: category results','','Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.','','[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/'+b+'.md) · [Metric contract](../../docs/metrics.md)','','| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |','|---|---|---|---:|---:|---:|---:|']
        for r in sorted((r for r in categories if r['dataset']==b),key=lambda r:(r['system'],list(titles).index(r['category']))):
            out.append(f"| {r['system']} | {'train' if r['train'] else 'eligible'} | {titles[r['category']]} | {r['hidden']}/{r['gold']} | {format_pct(r['hidden'],r['gold'])} | {format_pct(r['hit'],r['gold'])} | {format_pct(r['raw_hidden'],r['gold'])} |")
        (ROOT/f'results/types/{b}.md').write_text('\n'.join(out)+'\n')
    return selected


def costs_by_model():
    return ({r['model']: r['seconds_10k'] for r in speed_group(CPU_GROUP)},
            {r['model']: r['seconds_10k'] for r in speed_group(GPU_GROUP)})


def speed_table(group):
    out = ['| Detector | Seconds / 10k chars | Chars / s | Rows / s | Amortized ms/row p50 | p95 | Peak RSS MB | Datasets |',
           '|---|---:|---:|---:|---:|---:|---:|---:|']
    quantile = lambda value: '-' if value is None else f'{value:,.0f}'
    for r in speed_group(group):
        rss = f"{r['rss_mb']:,.0f}" if r['rss_mb'] else '-'
        out.append(f"| {r['model']} | {r['seconds_10k']:.2f} | {r['chars_per_second']:,.0f} | "
                   f"{r['rows_per_second']:,.2f} | {quantile(r['p50_ms_reported'])} | "
                   f"{quantile(r['p95_ms_reported'])} | {rss} | {r['datasets']} |")
    return out


def detector_table(rows):
    cpu, gpu = costs_by_model()
    out = ['| Detector | Family | Eligible sets | Untouched / gold | Untouched | Fully hidden | Masked outside annotations | Char F1 | CPU s/10k | GPU s/10k |',
           '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in rows:
        cost = lambda value: f'{value:.2f}' if value else '-'
        out.append(f"| {r['model']} | {r['family']} | {r['sets']}/{len(CAT)} | {r['missed']:,} / {r['gold']:,} | "
                   f"{format_pct(r['missed'], r['gold'])} | {r['hidden_pct']:.2f}% | {r['extra_pct']:.2f}% | "
                   f"{r['char_f1']:.3f} | {cost(cpu.get(r['model']))} | {cost(gpu.get(r['model']))} |")
    return out


def detectors_page():
    """One page with every measured configuration, its coverage and its measured cost."""
    quality = model_totals()
    complete = [r for r in quality if r['sets'] == len(CAT) and '+' not in r['model']]
    partial = [r for r in quality if r not in complete]
    out = ['# Every detector configuration', '',
           f'Pooled outcomes for {len(quality)} measured configurations at threshold 0.5. Every number below comes from the '
           'saved predictions of the frozen experiment. Runs on a known training source are excluded from these pools, '
           'so the eligible dataset count is part of the result and configurations with different counts are not directly comparable.', '',
           '`Untouched` means no predicted character reaches the normalized annotation. `Fully hidden` means every character of '
           'the annotation is masked after word-boundary expansion. `Masked outside annotations` is the share of characters masked '
           'in rows that carry no annotation; those rows are not verified clean content. Speed columns come from the two reference '
           'machine groups below and are blank when a configuration was never run there.', '',
           f'![Pooled outcomes for every complete-coverage detector](../assets/detectors.svg)', '',
           f'## Complete coverage: all {len(CAT)} datasets', '']
    out += detector_table(complete)
    out += ['', '## Partial coverage, label variants, chunking and quantization', '',
            'A `-ru` suffix switches zero-shot labels to Russian with the same weights, so those runs apply only to Russian cuts. '
            '`+sent300`, `+ov100` and `+nochunk` are cutting variants, `+cpu-int8` and `+cpu-speed` are CPU execution variants. '
            'A smaller dataset count is a missing measurement, never a zero-miss result.', '']
    out += detector_table(partial)
    out += ['', '## Measured CPU speed', '',
            f'{CPU_LABEL}. Saved batch throughput, not request latency. Dataset counts differ, '
            'so these rows are not a controlled same-input comparison. '
            'Amortized ms/row quantiles are the per-row share of measured compute, not individually timed requests.', '',
            '![Measured CPU throughput per detector](../assets/cpu-speed.svg)', '']
    out += speed_table(CPU_GROUP)
    out += ['', '## Measured GPU speed', '',
            f'{GPU_LABEL}. BardsAI has no row: its ONNX graph runs on CPU only.', '',
            '![Measured GPU throughput per detector](../assets/gpu-speed.svg)', '']
    out += speed_table(GPU_GROUP)
    out += ['', '## Cost against quality', '',
            '![Detector quality against measured cost](../assets/speed-quality.svg)', '',
            'Other machines, quantized runs, scanners and every historical measurement condition are in [speed.md](speed.md). '
            'Per-language results are in [by-language.md](by-language.md), exact per-dataset counts in '
            '[dataset-metrics.csv](dataset-metrics.csv), and execution metadata in [run-inventory.json](run-inventory.json).', '']
    (ROOT / 'results/detectors.md').write_text('\n'.join(out))


def readme_blocks(selected):
    path=ROOT/'README.md'
    text=path.read_text()
    stats=f"The frozen experiment contains **{len(CAT)} datasets**, **{sum(d['rows'] for d in CAT.values()):,} rows**, **{sum(d['gold_spans'] for d in CAT.values()):,} normalized gold spans** and **{len(json.loads((ROOT/'results/run-inventory.json').read_text())):,} saved prediction runs**. The catalog has {len(MODELS)} execution records, including label variants, mirrors, scanners and rules."
    mask=S['masking_diagnostics']
    headline=['| Outcome | Exact count | Rate |','|---|---:|---:|',
              f"| Normalized annotations fully hidden | {mask['normalized_fully_hidden_normalized']:,} / {mask['gold_normalized']:,} | {format_pct(mask['normalized_fully_hidden_normalized'], mask['gold_normalized'])} |",
              f"| Normalized annotations detected / overlapped | {mask['gold_normalized'] - aggregate(mask['composition'])['miss']:,} / {mask['gold_normalized']:,} | {format_pct(mask['gold_normalized'] - aggregate(mask['composition'])['miss'], mask['gold_normalized'])} |",
              f"| Characters masked in unannotated rows | {mask['clean_characters_masked']:,} / {mask['clean_characters']:,} | {format_pct(mask['clean_characters_masked'], mask['clean_characters'])} |",
              f"| Annotated rows with residual gold characters | {mask['positive_rows_residual_normalized']:,} / {mask['positive_rows']:,} | {format_pct(mask['positive_rows_residual_normalized'], mask['positive_rows'])} |",
              f"| Unannotated rows touched by a mask | {mask['clean_rows_touched']:,} / {mask['clean_rows']:,} | {format_pct(mask['clean_rows_touched'], mask['clean_rows'])} |"]
    comparison=['| Fixed configuration | Fully hidden ↑ | Detected / overlapped ↑ | Extra masking ↓ |','|---|---:|---:|---:|']
    for n,label in NAMES.items():
        r=aggregate(n)
        comparison.append(f"| {label} | {format_pct(r['hid'],r['nspan'])} | {format_pct(r['nspan']-r['miss'],r['nspan'])} | {format_pct(r['extra'],r['negchars'])} |")
    qualifying=[r for r in selected if r['gold']>=100]
    ordered=sorted(qualifying,key=lambda r:(-r['hidden']/r['gold'],-r['gold'],r['dataset'],r['category']))
    samples=[('High observed coverage',r) for r in ordered[:3]]+ [('Low observed coverage',r) for r in sorted(qualifying,key=lambda r:(r['hidden']/r['gold'],-r['gold'],r['dataset'],r['category']))[:3]]
    titles={d['id']:d['title'] for d in S['breakdowns']['categories']}
    examples=['| Diagnostic example | Dataset | Data type | Fully hidden / gold | Fully hidden |','|---|---|---|---:|---:|']
    for label,r in samples:
        examples.append(f"| {label} | [{r['dataset']}](results/types/{r['dataset']}.md) | {titles[r['category']]} | {r['hidden']:,} / {r['gold']:,} | {format_pct(r['hidden'],r['gold'])} |")
    complete=[r for r in model_totals() if r['sets']==len(CAT) and '+' not in r['model']]
    detectors=detector_table(complete)
    for name,body in (('SNAPSHOT',stats),('HEADLINE OUTCOMES','\n'.join(headline)),
                      ('COMPOSITION COMPARISON','\n'.join(comparison)),('DATASET EXAMPLES','\n'.join(examples)),
                      ('DETECTOR TABLE','\n'.join(detectors)),('CPU SPEED','\n'.join(speed_table(CPU_GROUP))),
                      ('GPU SPEED','\n'.join(speed_table(GPU_GROUP)))):
        pattern=f'<!-- BEGIN {name} -->.*?<!-- END {name} -->'
        text,n=re.subn(pattern,lambda _:f'<!-- BEGIN {name} -->\n{body}\n<!-- END {name} -->',text,flags=re.S)
        if n!=1:raise ValueError(f'Missing README generated block: {name}')
    path.write_text(text)


if __name__ == '__main__':
    detail = detail_rows()
    markdown()
    selected = detail_views(*detail)
    count = figures(detail[1])
    detectors_page()
    readme_blocks(selected)
    print(f'Rendered {count} SVG figures, exact CSVs, category pages, README blocks and catalogs.')
