"""Build English views from the frozen numeric snapshot."""
import csv
import json
import math
import os
import sys
import tomllib
import re
from collections import defaultdict
from pathlib import Path

os.environ.setdefault('MPLCONFIGDIR', str(Path(__file__).resolve().parent.parent / '.local/matplotlib'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

ROOT = Path(__file__).resolve().parent.parent
S = json.loads((ROOT / 'results/snapshot.json').read_text())
COUNTS = S['composition_counts']
CAT = {d['id']: d for d in S['datasets']}
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
COLORS = ['#8ea2b8', '#4b6c93', '#268baf', '#087e8b', '#7863a9', '#ba6a38']
INK, MUTED = '#152b43', '#50647a'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'text.color': INK,
    'axes.labelcolor': MUTED, 'xtick.color': MUTED, 'ytick.color': INK,
    'axes.edgecolor': '#dce4ed', 'axes.spines.top': False, 'axes.spines.right': False,
    'axes.spines.left': False, 'svg.fonttype': 'none', 'svg.hashsalt': 'pii-secrets-benchmark-v1',
    'savefig.facecolor': 'white'})


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


def canvas(title, subtitle, height=6.2):
    fig, ax = plt.subplots(figsize=(13.2, height))
    fig.text(.035, .96, title, fontsize=22, fontweight='bold', va='top')
    fig.text(.035, .895, subtitle, fontsize=11, color=MUTED, va='top')
    return fig, ax


def heat(ax, matrix, cmap, vmin, vmax):
    # Vector cells: imshow embeds a resampled PNG whose bytes differ per platform.
    rows, cols = len(matrix), len(matrix[0])
    ax.pcolormesh([c - .5 for c in range(cols + 1)], [r - .5 for r in range(rows + 1)],
                  matrix, cmap=cmap, vmin=vmin, vmax=vmax)
    ax.set_xlim(-.5, cols - .5)
    ax.set_ylim(rows - .5, -.5)


def save(fig, slug, title, description, footer):
    fig.text(.035, .055, footer, color=MUTED, fontsize=9, va='bottom')
    fig.text(.965, .02, 'PII & Secrets Benchmark | snapshot 2026-09-09', color=MUTED,
             fontsize=8, ha='right')
    (ROOT / 'assets').mkdir(exist_ok=True)
    previews = ROOT / '.local/previews'
    previews.mkdir(parents=True, exist_ok=True)
    fig.savefig(ROOT / f'assets/{slug}.svg', metadata={'Date': None, 'Title': title, 'Description': description})
    fig.savefig(previews / f'{slug}.png', dpi=135)
    plt.close(fig)


def figures():
    names = list(NAMES)
    totals = [aggregate(n) for n in names]
    residual = [pct(r['nspan'] - r['hid'], r['nspan']) for r in totals]
    overmask = [pct(r['extra'], r['negchars']) for r in totals]
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 6.5), sharey=True)
    fig.text(.035, .96, 'Masking leaves residuals and masks unannotated text', fontsize=22, fontweight='bold', va='top')
    fig.text(.035, .89, 'All 41 datasets | normalized word-boundary masks | lower is better', color=MUTED)
    for ax, values, title in zip(axes, (residual, overmask),
                                 ('Gold spans not fully hidden', 'Characters masked in unannotated rows')):
        ax.barh(range(6), values, color=COLORS, height=.6)
        ax.set_title(title, loc='left', fontsize=12, pad=15, fontweight='bold')
        ax.set_yticks(range(6), NAMES.values())
        ax.set_xlim(0, max(values) * 1.28)
        ax.set_xlabel('Percent')
        ax.xaxis.grid(True, color='#e9eef4'); ax.set_axisbelow(True)
        ax.tick_params(axis='y', length=0, pad=10)
        for i, (value, row) in enumerate(zip(values, totals)):
            count = row['nspan'] - row['hid'] if ax is axes[0] else row['extra']
            ax.text(value + max(values) * .025, i, f'{value:.1f}%  ({count:,})', va='center', fontsize=9.5)
    axes[0].invert_yaxis()
    fig.subplots_adjust(left=.31, right=.97, top=.77, bottom=.22, wspace=.18)
    save(fig, 'overview', 'Residual exposure and masking outside annotations',
         'Residual normalized gold spans and characters masked in unannotated rows for six complete compositions on all 41 datasets.',
         '227,466 normalized gold spans; 2,895,905 characters in 7,566 rows without annotations.\nAnnotation-based descriptive counts. Unannotated text is not guaranteed to contain no sensitive content.')

    matrix = [[pct(aggregate(n, c)['miss'], aggregate(n, c)['nspan']) for c in CUTS] for n in names]
    fig, ax = canvas('Language and task change the answer', 'Untouched spans (%) | lower is better | each column uses the same datasets for every row', 6.8)
    cmap = LinearSegmentedColormap.from_list('missed', ['#eef7f6', '#58a7b1', '#1c3f64'])
    heat(ax, matrix, cmap, 0, 36)
    ax.set_yticks(range(6), NAMES.values())
    cuts = [f"{a.upper()} / {b.upper()}\n{sum((d['lang'], d['kind']) == (a,b) for d in CAT.values())} {'dataset' if (a,b)==('ru','secrets') else 'datasets'}" for a,b in CUTS]
    ax.set_xticks(range(5), cuts); ax.xaxis.tick_top()
    ax.tick_params(length=0, pad=9)
    for i, name in enumerate(names):
        for j, cut in enumerate(CUTS):
            r = aggregate(name, cut)
            ax.text(j, i, format_pct(r['miss'], r['nspan']), ha='center', va='center',
                    color='white' if matrix[i][j] > 17 else INK, fontsize=13, fontweight='bold')
    fig.subplots_adjust(left=.31, right=.97, top=.74, bottom=.18)
    save(fig, 'language-cuts', 'Missed spans by language and task',
         'Russian PII, synthetic Russian secrets, English PII, English secrets, and multilingual PII. No multilingual-secrets cut exists.',
         'RU / secrets is one synthetic dataset. MULTI pools languages and may include English; it is not a per-language guarantee.\nZero observed misses is not a guarantee. There is no MULTI / secrets dataset in this snapshot.')

    costs = S['costs']
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 6.4), sharey=True)
    fig.text(.035, .96, 'More detection has a compute cost', fontsize=22, fontweight='bold', va='top')
    fig.text(.035, .89, 'Seconds per 10,000 characters from throughput | lower is better | not single-request latency', color=MUTED)
    for ax, key, title in zip(axes, ('cpu_seconds_10k', 'gpu_seconds_10k'), ('CPU reference, calibrated', 'RTX 5090 reference')):
        vals = [r[key] for r in costs]
        bars = ax.barh(range(len(costs)), vals, color=[COLORS[names.index(r['composition'])] for r in costs], height=.57)
        bars[-1].set_hatch('//')
        ax.set_title(title, loc='left', fontsize=12, pad=15, fontweight='bold')
        ax.set_yticks(range(len(costs)), [NAMES[r['composition']] for r in costs])
        ax.set_xlim(0, max(vals) * 1.25); ax.set_xlabel('Seconds / 10,000 characters')
        ax.tick_params(axis='y', length=0, pad=10)
        ax.xaxis.grid(True, color='#e9eef4'); ax.set_axisbelow(True)
        for i,v in enumerate(vals): ax.text(v+max(vals)*.025, i, f'{v:.1f}' + (' *' if i == 4 else ''), va='center')
    axes[0].invert_yaxis()
    fig.subplots_adjust(left=.31, right=.97, top=.76, bottom=.23, wspace=.15)
    save(fig, 'compute-cost', 'Reference throughput cost',
         'Sequential composition cost from the frozen verdict. CPU W24 with 16 threads per worker; GPU W2. BardsAI uses a CPU-only ONNX graph.',
         'CPU: AMD EPYC 9K84, W=24, 16 threads per process; calibrated to PPLX at 1,100 chars/s. GPU: W=2.\n* Hatched bars include BardsAI at 8 CPU threads: a different-condition estimate; the right bar mixes GPU and CPU.\nAll composition costs are derived from member throughput; they are not measured end-to-end request times.')

    detected = [100-pct(r['miss'], r['nspan']) for r in totals]
    hidden = [pct(r['hid'], r['nspan']) for r in totals]
    fig, ax = canvas('Detected does not mean fully hidden', 'Gold spans (%) | higher is better | both metrics use the same normalized span boundaries', 6.5)
    y = list(range(6))
    ax.barh([v-.17 for v in y], detected, .3, color='#96c8cd', label='Touched by at least one predicted character')
    ax.barh([v+.17 for v in y], hidden, .3, color='#087e8b', label='All normalized gold characters hidden')
    ax.set_yticks(y, NAMES.values()); ax.invert_yaxis(); ax.set_xlim(0, 112)
    ax.set_xticks([0,25,50,75,100]); ax.set_xlabel('Share of normalized gold spans (%)')
    ax.tick_params(axis='y', length=0, pad=10)
    for i,(a,b) in enumerate(zip(detected,hidden)):
        ax.text(a+.8, i-.17, f'{a:.1f}%', va='center', fontsize=10)
        ax.text(b+.8, i+.17, f'{b:.1f}%', va='center', fontsize=10)
    ax.legend(loc='upper left', bbox_to_anchor=(-.40, -.19), frameon=False, ncols=1, fontsize=10)
    fig.subplots_adjust(left=.31, right=.97, top=.81, bottom=.28)
    save(fig, 'full-hiding', 'Touched versus fully hidden spans',
         'Detection recall and full hiding are computed independently from saved predictions on all 41 datasets.',
         '227,466 normalized spans. Word-boundary normalization can expand masks; neither percentage proves that original secrets are unusable.')

    selected = ['pplx','gliner2-fastino','mmbert32k','bardsai-eu','rules-ru','presidio-ru'] + [n for n,v in MODELS.items() if v['family'] == 'leaks']
    coverage = []
    for name in selected:
        row = []
        for a,b in CUTS:
            eligible = {r['dataset'] for r in S['measurements'] if r['model'] == name and not r['train'] and (r['lang'],r['kind']) == (a,b)}
            denom = sum((d['lang'],d['kind']) == (a,b) for d in CAT.values())
            row.append((len(eligible),denom))
        coverage.append(row)
    fig, ax = canvas('Coverage is part of the result', 'Eligible base-configuration datasets / available datasets | training-source overlaps excluded', 8.8)
    heat(ax, [[a/b for a,b in row] for row in coverage], LinearSegmentedColormap.from_list('coverage',['#f0f3f7','#087e8b']), 0, 1)
    ax.set_yticks(range(len(selected)),selected); ax.set_xticks(range(5),[f'{a.upper()} / {b.upper()}' for a,b in CUTS]); ax.xaxis.tick_top();ax.tick_params(length=0,pad=8)
    for i,row in enumerate(coverage):
        for j,(a,b) in enumerate(row):ax.text(j,i,f'{a}/{b}',ha='center',va='center',color='white' if a/b>.6 else INK,fontsize=10)
    fig.subplots_adjust(left=.20,right=.97,top=.81,bottom=.13)
    save(fig, 'coverage', 'Eligible dataset coverage',
         'Selected full-coverage models, Russian rules, Presidio, and all ten scanner configurations. A missing measurement is not a zero-miss result.',
         'This is measurement coverage, not detection quality. A zero can mean missing runs or excluded source overlap.\nScanners have a narrower intended scope. See the full per-dataset reports before comparing unequal subsets.')


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
        src=d['source']; link=f"[{d['id']}]({src})" if src.startswith('https://') else d['id']
        datasets.append(f"| {link} | {d['lang']} | {d['kind']} | {d['rows']:,} | {d['gold_spans']:,} | {d['license']} | [Results](../results/datasets/{d['id']}.md) |")
    missing_revision = [d['id'] for d in CAT.values() if not d.get('raw') or d['raw'].get('revision') in (None, '-')]
    datasets += ['', '## Reconstruction status', '', 'The public Leak Museum route is tested from source download through CPU inference and scoring. The following 22 historical cuts have no retained raw-source revision and cannot be reconstructed exactly from an upstream revision alone:', '', ', '.join(f'`{name}`' for name in missing_revision) + '.', '', 'A retained aggregate raw hash identifies the archived bytes where available but does not make a newer upstream download equivalent. Other dependency and acquisition gaps are documented in [source acquisition](sources.md).', '', 'See [source acquisition and conversion caveats](sources.md), [license notices](../LICENSES/README.md), [catalog.json](../datasets/catalog.json) and [samples.json](../datasets/samples.json). A source publication mode of `files` in archived metadata describes the original experiment; this repository distributes no corpus text.','']
    (ROOT/'docs/datasets.md').write_text('\n'.join(datasets))
    models=['# Detector catalog','','62 execution records: 50 model configurations (40 distinct weights, eight Russian-label variants, two mirrors), ten secret-scanner configurations, one rules layer and Presidio. A catalog entry does not imply a completed run. The `cpu` catalog flag controls the planned CPU sweep, not a universal capability claim.','','| Record | Family | Upstream | Pinned revision/version | Flags |','|---|---|---|---|---|']
    for n,c in MODELS.items():
        repo=c['repo'];url=('https://'+repo if repo.startswith('github.com/') else 'https://huggingface.co/'+repo)
        upstream=f'[{repo}]({url})' if ('/' in repo and ' + ' not in repo and not repo.startswith(('SCRIPTS/','benchmark/'))) else repo.replace('SCRIPTS/','benchmark/')
        flags=[]
        if c.get('mirror'):flags.append('mirror of '+c['mirror'])
        if c.get('labels')=='ru':flags.append('Russian labels')
        if c.get('disputed'):flags.append('disputed scope')
        if c.get('contaminated'):flags.append('source overlap: '+', '.join(c['contaminated']))
        models.append(f"| {n} | {c['family']} | {upstream} | `{c['revision']}` | {'; '.join(flags) or '-'} |")
    models += ['','## Training-source evidence','','`train` is a conservative source-overlap exclusion, not proof of memorization. An empty list is absence of known evidence, not proof of independence. Exclusions extend to other cuts and corrupted copies of the same source and to identical-weight records.','']
    for n,c in MODELS.items():models.append(f"- **{n}:** {c.get('train','Not disclosed.')}")
    models += ['','Exact execution settings are in [models.toml](../benchmark/models.toml), observed runtimes in [run-inventory.json](../results/run-inventory.json), and measured coverage in [by-language.md](../results/by-language.md). Model and scanner software licenses are controlled by their upstream projects; this project\'s MIT license does not relicense their weights.','']
    (ROOT/'docs/models.md').write_text('\n'.join(models))


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


def detail_views():
    labels, categories, datasets = detail_rows()
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
    subtitle = 'PPLX + Fastino + mmBERT + BardsAI | fixed composition | all retained datasets'
    fig, ax = canvas('Full hiding by sensitive-data type', subtitle, 10.1)
    ax.set_position([.035, .14, .93, .67]); ax.set_xlim(0, 1); ax.set_ylim(-.7, len(defs)-.1); ax.invert_yaxis(); ax.axis('off')
    for x, title, align in ((0, 'DATA TYPE', 'left'), (.72, 'FULLY HIDDEN', 'right'), (.86, 'DETECTED', 'right'), (1, 'GOLD SPANS', 'right')):
        ax.text(x, -.48, title, fontsize=9, color=MUTED, ha=align)
    for i, d in enumerate(defs):
        r = pooled[d['id']]
        ax.axhline(i+.68, color='#e4eaf0', lw=.8)
        ax.text(0, i+.12, d['title'], fontsize=13, fontweight='bold')
        ax.text(0, i+.43, d['family'], fontsize=9, color=MUTED)
        ax.barh(i+.2, .19, left=.42, height=.16, color='#e9eef4')
        ax.barh(i+.2, .19*r['hidden']/r['gold'], left=.42, height=.16, color='#087e8b')
        for x, value, color in ((.72, format_pct(r['hidden'], r['gold']), INK),
                                (.86, format_pct(r['hit'], r['gold']), MUTED), (1, f"{r['gold']:,}", MUTED)):
            ax.text(x, i+.2, value, ha='right', va='center', fontsize=12, color=color)
    save(fig, 'entity-types', 'Fully hidden and detected spans by data type',
         'Exact normalized annotation counts for one fixed four-member composition, with source labels mapped to twelve presentation categories.',
         'Full hiding uses normalized word-boundary masks. Detected means at least one character touched.\nUsernames are not necessarily secret; organizations and locations depend on context. All original labels remain in the CSV.')

    ids = sorted(CAT, key=lambda b: (('ru', 'en', 'multi').index(CAT[b]['lang']), CAT[b]['kind'], b))
    names = list(NAMES)
    short = ['PPLX', 'Fastino', 'P + F', 'P + F + M', 'P + F + B', 'P + F + M + B']
    lookup = {(r['composition'], r['dataset']): r for r in COUNTS}
    matrix = [[pct(lookup[(n, b)]['hid'], lookup[(n, b)]['nspan']) for n in names] for b in ids]
    fig, ax = plt.subplots(figsize=(13.2, 16.8))
    fig.text(.035, .974, 'Every dataset stays visible', fontsize=22, fontweight='bold')
    fig.text(.035, .948, 'Fully hidden normalized spans (%) | higher is better | same dataset in every column', color=MUTED)
    heat(ax, matrix, LinearSegmentedColormap.from_list('hidden', ['#f5e9e2', '#dddfe9', '#8bc2c5', '#087e8b']), 0, 100)
    ax.set_yticks(range(len(ids)), [f"{b}   ({CAT[b]['lang'].upper()}, n={CAT[b]['gold_spans']:,})" for b in ids], fontsize=9)
    ax.set_xticks(range(len(names)), short); ax.xaxis.tick_top(); ax.tick_params(length=0, pad=9)
    for i, b in enumerate(ids):
        for j, n in enumerate(names):
            r = lookup[(n, b)]
            ax.text(j, i, format_pct(r['hid'], r['nspan']), ha='center', va='center', fontsize=9,
                    color='white' if matrix[i][j] >= 88 else INK)
    fig.subplots_adjust(left=.39, right=.97, top=.913, bottom=.10)
    save(fig, 'dataset-heatmap', 'Full hiding across every frozen dataset',
         'All forty-one dataset cuts and all six complete compositions; rows are ordered by language, task, and dataset identifier, never removed for low scores.',
         'P = PPLX, F = Fastino, M = mmBERT, B = BardsAI. n = normalized gold spans.\nDifferent datasets have different annotations and difficulty; 100% means zero observed residuals on that sample.\nSee results/by-dataset.md for provenance, original-offset coverage, precision, recall and negative-row masking.')

    head = [r for r in COUNTS if r['composition'] == reference.removeprefix('composition:')]
    influential = sorted(head, key=lambda r: (-(r['nspan'] - r['hid']), r['dataset']))[:10]
    fig, ax = canvas('Where residual exposure comes from', 'Same four-member composition | ten largest contributions | all other datasets remain in the total', 7.4)
    values = [r['nspan']-r['hid'] for r in influential]
    ax.barh(range(len(values)), values, color='#b96e48', height=.65)
    ax.set_yticks(range(len(values)), [r['dataset'] for r in influential]); ax.invert_yaxis()
    ax.set_xlim(0, max(values)*1.55); ax.set_xlabel('Normalized spans not fully hidden')
    ax.xaxis.grid(True, color='#e9eef4'); ax.set_axisbelow(True); ax.tick_params(axis='y', length=0)
    for i, r in enumerate(influential):
        ax.text(values[i]+max(values)*.025, i, f"{values[i]:,} / {r['nspan']:,}  |  {format_pct(r['hid'],r['nspan'])} hidden", va='center', fontsize=10)
    total = sum(r['nspan']-r['hid'] for r in head)
    fig.subplots_adjust(left=.22, right=.97, top=.80, bottom=.19)
    save(fig, 'dataset-influence', 'Dataset contributions to residual spans',
         'Absolute residual counts for the ten largest contributors, with their denominators and full-hiding rates; no dataset is excluded.',
         f"These ten contribute {sum(values):,} of {total:,} residual spans; the other datasets contribute {total-sum(values):,}.\nA large contribution can reflect dataset size, annotation policy or difficulty. It is not proof of defective data.")

    fig, ax = canvas('The dataset mix changes the percentage', 'Fully hidden normalized spans (%) | same compositions in every cut', 7.1)
    series = [('All 41, span-weighted', None, False), ('All 41, equal dataset weight', None, True),
              ('Remaining 32, span-weighted', set(S['sensitivity']['included_dataset_ids']), False)]
    for j, (label, include, macro) in enumerate(series):
        values = []
        for n in names:
            rows = [r for r in COUNTS if r['composition']==n and (include is None or r['dataset'] in include)]
            values.append(100*sum(r['hid']/r['nspan'] for r in rows)/len(rows) if macro else pct(sum(r['hid'] for r in rows),sum(r['nspan'] for r in rows)))
        ax.barh([i+(j-1)*.24 for i in range(6)], values, height=.22, color=['#087e8b','#98c3c8','#8b7eae'][j], label=label)
        for i, v in enumerate(values): ax.text(v+.7, i+(j-1)*.24, f'{v:.2f}%', va='center', fontsize=9)
    ax.set_yticks(range(6),NAMES.values());ax.invert_yaxis();ax.set_xlim(0,110);ax.set_xticks([0,25,50,75,100])
    ax.legend(loc='lower left',bbox_to_anchor=(-.39,-.30),frameon=False,fontsize=10)
    ax.set_xlabel('Share fully hidden (%)');ax.tick_params(axis='y',length=0)
    fig.subplots_adjust(left=.31,right=.97,top=.79,bottom=.29)
    save(fig, 'dataset-mix', 'Full-hiding sensitivity to dataset weighting',
         'Span-weighted and dataset-macro full hiding on all forty-one cuts and span-weighted full hiding on the predeclared thirty-two-cut sensitivity subset.',
         'Remaining 32 excludes six project-generated synthetic sets and three corrupted copies; upstream synthetic data remains.\nThis is a descriptive sensitivity analysis, not a new selection or test split.')

    fig, ax = canvas('What the benchmark contains', 'Normalized gold spans by presentation category | larger categories have more weight in pooled scores', 8)
    ax.barh(range(len(defs)), [pooled[d['id']]['gold'] for d in defs], color=['#8b7eae' if d['family']=='Credentials' else '#087e8b' for d in defs],height=.65)
    ax.set_yticks(range(len(defs)),[d['title'] for d in defs]);ax.invert_yaxis();ax.set_xlabel('Normalized gold spans')
    largest=max(r['gold'] for r in pooled.values());ax.set_xlim(0,largest*1.45);ax.tick_params(axis='y',length=0)
    for i,d in enumerate(defs):
        r=pooled[d['id']]; nsets=sum(x['category']==d['id'] for x in selected)
        ax.text(r['gold']+largest*.025,i,f"{r['gold']:,}  |  {nsets} datasets",va='center',fontsize=10)
    fig.subplots_adjust(left=.28,right=.97,top=.81,bottom=.16)
    save(fig, 'category-distribution', 'Benchmark category support',
         'Gold-span counts and contributing dataset counts for twelve presentation categories. Each normalized annotation has exactly one category.',
         'These are annotation units, not distinct people or unique credentials. Nested and differently labeled annotations remain separate.\nCategory families are an explanatory grouping, not a legal determination that every occurrence is personal data.')

    fig,ax=canvas('Raw offsets and expanded masks differ', 'Same normalized gold spans | four-member composition | higher is better',8.1)
    for j,(key,label,color) in enumerate((('raw_hidden','Raw detector offsets','#98c3c8'),('hidden','Word-boundary masks','#087e8b'))):
        vals=[pct(pooled[d['id']][key],pooled[d['id']]['gold']) for d in defs]
        ax.barh([i+(j-.5)*.33 for i in range(len(defs))],vals,height=.30,color=color,label=label)
        for i,d in enumerate(defs):ax.text(vals[i]+.7,i+(j-.5)*.33,format_pct(pooled[d['id']][key],pooled[d['id']]['gold']),va='center',fontsize=9)
    ax.set_yticks(range(len(defs)),[d['title'] for d in defs]);ax.invert_yaxis();ax.set_xlim(0,113);ax.set_xticks([0,25,50,75,100]);ax.tick_params(axis='y',length=0)
    ax.legend(loc='lower left',bbox_to_anchor=(-.35,-.18),frameon=False,ncols=2,fontsize=10)
    fig.subplots_adjust(left=.28,right=.97,top=.81,bottom=.22)
    save(fig,'raw-offsets','Raw and normalized mask full hiding by type',
         'Both series use normalized gold spans; only the predicted mask changes. Original-annotation raw coverage is available separately in the CSV.',
         'Do not use expanded-mask percentages for an application that applies raw offsets.\nThese categories do not measure entity-type correctness or whether a partially hidden credential remains usable.')

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


def readme_blocks(selected):
    path=ROOT/'README.md'
    text=path.read_text()
    stats=f"The frozen experiment contains **{len(CAT)} datasets**, **{sum(d['rows'] for d in CAT.values()):,} rows**, **{sum(d['gold_spans'] for d in CAT.values()):,} normalized gold spans** and **{len(json.loads((ROOT/'results/run-inventory.json').read_text())):,} saved prediction runs**. The catalog has {len(MODELS)} execution records, including label variants, mirrors, scanners and rules."
    mask=S['masking_diagnostics']
    headline=['| Outcome | Exact count | Rate |','|---|---:|---:|',
              f"| Normalized annotations untouched | {aggregate(mask['composition'])['miss']:,} / {mask['gold_normalized']:,} | {format_pct(aggregate(mask['composition'])['miss'], mask['gold_normalized'])} |",
              f"| Normalized annotations not fully hidden | {mask['gold_normalized'] - mask['normalized_fully_hidden_normalized']:,} / {mask['gold_normalized']:,} | {format_pct(mask['gold_normalized'] - mask['normalized_fully_hidden_normalized'], mask['gold_normalized'])} |",
              f"| Annotated rows with residual gold characters | {mask['positive_rows_residual_normalized']:,} / {mask['positive_rows']:,} | {format_pct(mask['positive_rows_residual_normalized'], mask['positive_rows'])} |",
              f"| Unannotated rows touched by a mask | {mask['clean_rows_touched']:,} / {mask['clean_rows']:,} | {format_pct(mask['clean_rows_touched'], mask['clean_rows'])} |",
              f"| Characters masked in unannotated rows | {mask['clean_characters_masked']:,} / {mask['clean_characters']:,} | {format_pct(mask['clean_characters_masked'], mask['clean_characters'])} |"]
    comparison=['| Fixed configuration | Untouched annotations | Not fully hidden | Unannotated characters masked |','|---|---:|---:|---:|']
    for n,label in NAMES.items():
        r=aggregate(n)
        comparison.append(f"| {label} | {format_pct(r['miss'],r['nspan'])} | {format_pct(r['nspan']-r['hid'],r['nspan'])} | {format_pct(r['extra'],r['negchars'])} |")
    qualifying=[r for r in selected if r['gold']>=100]
    ordered=sorted(qualifying,key=lambda r:(-r['hidden']/r['gold'],-r['gold'],r['dataset'],r['category']))
    samples=[('High observed coverage',r) for r in ordered[:3]]+ [('Low observed coverage',r) for r in sorted(qualifying,key=lambda r:(r['hidden']/r['gold'],-r['gold'],r['dataset'],r['category']))[:3]]
    titles={d['id']:d['title'] for d in S['breakdowns']['categories']}
    examples=['| Diagnostic example | Dataset | Data type | Fully hidden / gold | Fully hidden |','|---|---|---|---:|---:|']
    for label,r in samples:
        examples.append(f"| {label} | [{r['dataset']}](results/types/{r['dataset']}.md) | {titles[r['category']]} | {r['hidden']:,} / {r['gold']:,} | {format_pct(r['hidden'],r['gold'])} |")
    for name,body in (('SNAPSHOT',stats),('HEADLINE OUTCOMES','\n'.join(headline)),('COMPOSITION COMPARISON','\n'.join(comparison)),('DATASET EXAMPLES','\n'.join(examples))):
        pattern=f'<!-- BEGIN {name} -->.*?<!-- END {name} -->'
        text,n=re.subn(pattern,lambda _:f'<!-- BEGIN {name} -->\n{body}\n<!-- END {name} -->',text,flags=re.S)
        if n!=1:raise ValueError(f'Missing README generated block: {name}')
    path.write_text(text)


if __name__ == '__main__':
    markdown()
    figures()
    readme_blocks(detail_views())
    print('Rendered 11 SVG figures, PNG previews, exact CSVs, category pages, README blocks and catalogs.')
