"""Validate the public snapshot without private data or inference dependencies."""
import csv
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tomllib
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
IGNORED = {'.local', '.venv', '.git', '.cache', '__pycache__'}
PUBLIC_DIRS = {'assets', 'benchmark', 'datasets', 'docs', 'results', 'scripts', 'tests', 'LICENSES', '.github'}
PUBLIC_FILES = {'README.md', 'LICENSE', 'NOTICE', 'AGENTS.md', 'CONTRIBUTING.md', 'CITATION.cff',
                'CHANGELOG.md', 'SECURITY.md', '.gitignore', '.gitattributes', '.python-version',
                'pyproject.toml', 'uv.lock'}


def files():
    result = []
    for directory, dirs, names in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORED]
        for name in dirs + names:
            p = Path(directory) / name
            rel = p.relative_to(ROOT)
            if p.is_symlink():
                raise AssertionError(f'Public symlink: {rel}')
            if len(rel.parts) == 1 and name not in IGNORED | PUBLIC_DIRS | PUBLIC_FILES:
                raise AssertionError(f'Unexpected publication entry: {rel}')
        result.extend(Path(directory) / n for n in names if not n.endswith(('.pyc', '.pyo')))
    return result


def load(name):
    return json.loads((ROOT / name).read_text())


def check_provenance(snapshot, inventory):
    """T03/T05: the published run inventory, the reviewed source digests and
    the per-scanner release status must describe the same runs.

    The snapshot `sources` map is the published digest manifest: every run in
    the inventory appears there with the same digest and every recorded
    prediction source has an inventory record, so a run cannot be re-exported
    under an old digest or silently dropped from the inventory. Scanner runs
    carry the reviewed adapter status here, which is what a machine-readable
    consumer reads instead of Markdown labels."""
    sys.path.insert(0, str(ROOT / 'benchmark'))
    from run_leaks import ADAPTER_STATUS, STATUS_VALUES, adapter_policy, adapter_status
    sources = snapshot['sources']
    recorded = {str(k): v for k, v in sources.items()}
    seen = set()
    tools = set()
    for r in inventory:
        assert re.fullmatch(r'[0-9a-f]{64}', r['pred_sha256'] or ''), r['file']
        assert r['file'].startswith('pred.') and r['file'].endswith('.jsonl'), r['file']
        key = f"RESULTS/{r['dataset']}/{r['file']}"
        assert recorded.get(key) == r['pred_sha256'], f'Inventory and sources disagree: {key}'
        seen.add(key)
        tool = r['file'][len('pred.'):-len('.jsonl')]
        assert (r['dataset'], tool) not in tools, f'Duplicate run record: {r["dataset"]}/{tool}'
        tools.add((r['dataset'], tool))
        if tool in ADAPTER_STATUS:
            assert r.get('adapter_status') in STATUS_VALUES, f'Unknown run status: {key}'
            assert r['adapter_status'] == adapter_status(tool), f'Status contradicts the reviewed table: {key}'
            # T05: the status has to come from the run, not from the table.
            # A run produced by the corrected mapping must say so itself.
            if r['adapter_status'] == 'corrected-rerun':
                assert r.get('adapter_policy'), f'Corrected rerun without its recorded mapping policy: {key}'
            if r.get('adapter_policy'):
                assert r['adapter_policy'] == adapter_policy(tool), f'Mapping policy contradicts the reviewed table: {key}'
                assert r['adapter_status'] != 'historical-pre-fix', f'Recorded policy cannot be pre-fix: {key}'
        if 'unresolved_spans' in r:
            assert isinstance(r['unresolved_spans'], int) and 0 < r['unresolved_spans'] <= r['rows'], key
            reasons = r.get('unresolved_reasons')
            assert isinstance(reasons, dict) and reasons, f'Unresolved findings without a reason: {key}'
            assert all(k in ('decoded', 'capture-collision', 'native') and isinstance(v, int) and v > 0
                       for k, v in reasons.items()), f'Unknown unresolved reason: {key}'
            assert sum(reasons.values()) == r['unresolved_spans'], f'Unresolved reasons do not add up: {key}'
    preds = {k for k in recorded if re.fullmatch(r'RESULTS/[^/]+/pred\..+\.jsonl', k)}
    assert preds == seen, f'Prediction sources without an inventory record: {sorted(preds - seen)[:3]}'
    print(f"Provenance: {len(inventory):,} runs bound to reviewed digests and release statuses.")


def check_snapshot():
    s = load('results/snapshot.json')
    assert s['schema_version'] == 3 and s['threshold'] == .5
    # T08: the frozen experiment, the code that packaged it and the released
    # result bundle are three separate identities, checked against their
    # single declared sources instead of one ambiguous date.
    sys.path.insert(0, str(ROOT / 'scripts'))
    import export
    assert s['experiment_date'] == export.EXPERIMENT_DATE == '2026-09-09'
    assert s['result_revision'] == export.RESULT_REVISION
    assert s['code_version'] == export.code_version() == tomllib.loads(
        (ROOT / 'pyproject.toml').read_text())['project']['version']
    ds = {d['id']: d for d in s['datasets']}
    assert len(ds) == len(s['datasets']) == 41
    assert sum(d['rows'] for d in ds.values()) == 41643
    assert sum(d['gold_spans'] for d in ds.values()) == 227466
    assert sum(d['original_annotations'] for d in ds.values()) == 230446
    assert Counter((d['lang'], d['kind']) for d in ds.values()) == {('ru','pii'):18,('ru','secrets'):1,('en','pii'):8,('en','secrets'):9,('multi','pii'):5}
    assert s['datasets'] == load('datasets/catalog.json')
    cfg = tomllib.loads((ROOT / 'benchmark/models.toml').read_text())['models']
    assert len(cfg) == 62 and all(c.get('revision') for c in cfg.values())
    measurements = s['measurements']
    assert len(measurements) == 2137
    assert len({(r['dataset'], r['model']) for r in measurements}) == len(measurements)
    for r in measurements:
        assert r['dataset'] in ds and r['model'].split('+')[0] in cfg
        assert 0 <= r['missed'] <= r['gold_spans'] == ds[r['dataset']]['gold_spans']
        assert math.isclose(r['missed_pct'], 100*r['missed']/r['gold_spans'])
        assert 0 <= r['missed_ci_low_reported'] <= r['missed_ci_high_reported'] <= 100
        assert 0 <= r['hidden_pct_reported'] <= 100 and isinstance(r['train'],bool)
        assert (r['lang'],r['kind']) == (ds[r['dataset']]['lang'],ds[r['dataset']]['kind'])
    ensemble = {(r['composition'],r['dataset']):r for r in s['ensembles']}
    assert len(ensemble) == len(s['ensembles']) == 615
    for r in ensemble.values():
        assert r['status'] in ('ok','train','missing')
        assert r['gold_spans'] == ds[r['dataset']]['gold_spans']
        assert len(set(r['members'])) == len(r['members']) and 1 <= r['votes'] <= len(r['members'])
        if r['status'] == 'ok':assert 0 <= r['missed'] <= r['gold_spans']
        else:assert r['missed'] is None
    counts = s['composition_counts']
    assert counts == load('results/composition-counts.json')
    assert len(counts) == len({(r['composition'],r['dataset']) for r in counts}) == 286
    for r in counts:
        e = ensemble[(r['composition'],r['dataset'])]
        assert e['status'] == 'ok' and r['miss'] == e['missed'] and r['nspan'] == e['gold_spans']
        assert r['hit'] + r['miss'] == r['nspan'] and 0 <= r['hid'] <= r['hit']
        assert 0 <= r['fire'] <= r['nneg'] and 0 <= r['extra'] <= r['negchars']
        assert sum(g[1] for g in r['grp'].values()) == r['nspan']
    reference = {'pplx':47647, 'fastino':30011, 'pplx+fastino':7872, 'pplx+fastino+mmbert':4746,
                 'pplx+fastino+bardsai':4258, 'pplx+fastino+bardsai+mmbert':3254}
    with (ROOT/'results/summary.csv').open() as f:summary=list(csv.DictReader(f))
    assert {r['composition'] for r in summary} == set(reference)
    for name, miss in reference.items():
        rs = [r for r in counts if r['composition']==name]
        assert len(rs)==41 and sum(r['miss'] for r in rs)==miss
        row=next(r for r in summary if r['composition']==name)
        for field in ('miss','nspan','hid','tp','fp','fn','fire','nneg','extra','negchars'):
            assert int(row[field]) == sum(r[field] for r in rs)
        assert int(row['residual']) == int(row['nspan']) - int(row['hid'])
        assert math.isclose(float(row['residual_pct']), 100*int(row['residual'])/int(row['nspan']))
    for dataset in ds:
        assert ensemble[('pplx+fastino+bardsai+mmbert',dataset)]['missed'] <= ensemble[('pplx+fastino+mmbert',dataset)]['missed'] <= ensemble[('pplx+fastino',dataset)]['missed'] <= ensemble[('pplx',dataset)]['missed']
    masking = s['masking_diagnostics']
    assert masking == {
        'composition': 'pplx+fastino+bardsai+mmbert',
        'members': ['pplx', 'gliner2-fastino', 'mmbert32k', 'bardsai-eu'],
        'gold_original': 230446, 'gold_normalized': 227466,
        'original_fully_hidden_raw': 216780,
        'normalized_fully_hidden_raw': 212658,
        'normalized_fully_hidden_normalized': 214738,
        'positive_rows': 34077, 'positive_rows_residual_raw': 7063,
        'positive_rows_residual_normalized': 6749,
        'clean_rows': 7566, 'clean_rows_touched': 5899,
        'clean_characters': 2895905, 'clean_characters_masked': 574028,
    }
    sensitivity = s['sensitivity']
    excluded = {d['id'] for d in ds.values() if d['synthetic'] or d['corrupted']}
    included = set(sensitivity['included_dataset_ids'])
    assert set(sensitivity['excluded_dataset_ids']) == excluded
    assert len(excluded) == 9 and len(included) == 32 and not excluded & included
    assert excluded | included == set(ds)
    inventory = load('results/run-inventory.json')
    assert len(inventory)==len({(r['dataset'],r['file']) for r in inventory})==2500
    assert all(r['dataset'] in ds and not {'host','hostname','text','spans','token','api_key'} & r.keys() for r in inventory)
    check_provenance(s, inventory)
    assert len(s['costs'])==5 and sum(r['mixed_device_estimate'] for r in s['costs'])==1
    for filename,key in [('measurements.csv','measurements'),('ensembles.csv','ensembles'),('speed.csv','speed')]:
        with (ROOT/'results'/filename).open() as f:rows=list(csv.DictReader(f))
        assert len(rows)==len(s[key])
        for row,record in zip(rows,s[key]):
            for k,v in record.items():
                expected=' + '.join(v) if k=='members' else '' if v is None else str(v)
                assert row[k]==expected, (filename,k)
    print('Snapshot: exact totals, 2,137 quality rows, 286 recomputed composition rows, 2,500 run records.')
    check_breakdowns(s, ds)


def check_breakdowns(snapshot, datasets):
    sys.path.insert(0, str(ROOT / 'scripts'))
    from stratify import category
    b = snapshot['breakdowns']
    assert b['taxonomy_version'] == 1
    categories = {r['id'] for r in b['categories']}
    assert len(categories) == len(b['categories']) == 12
    taxonomy = {(r['dataset'], r['label']): r for r in b['taxonomy']}
    assert len(taxonomy) == len(b['taxonomy'])
    for r in taxonomy.values():
        assert r['category'] in categories and r['category'] == category(r['label'], r['group'])
        assert 0 <= r['gold'] <= r['original_gold'] and r['characters'] >= r['gold']
    for dataset, d in datasets.items():
        rows = [r for r in taxonomy.values() if r['dataset'] == dataset]
        assert sum(r['gold'] for r in rows) == d['gold_spans']
        assert sum(r['original_gold'] for r in rows) == d['original_annotations']
    systems = {r['id']: r for r in b['systems']}
    assert len(systems) == len(b['systems'])
    expected = {(f"model:{r['model']}", r['dataset']): r for r in snapshot['measurements']}
    expected.update({(f"composition:{r['composition']}", r['dataset']): r for r in snapshot['composition_counts']})
    rows = {(r['system'], r['dataset']): r for r in b['results']}
    assert len(rows) == len(b['results']) == 2423 and rows.keys() == expected.keys()
    csv_labels, csv_categories, csv_datasets = {}, {}, {}
    for key, r in rows.items():
        assert r['system'] in systems
        ds = r['dataset']
        source = expected[key]
        assert r['train'] == source.get('train', False)
        assert {x['label'] for x in r['types']} == {t for dataset, t in taxonomy if dataset == ds}
        assert len(r['types']) == len({x['label'] for x in r['types']})
        grouped = {}
        for t in r['types']:
            definition = taxonomy[(ds, t['label'])]
            assert 0 <= t['hidden'] <= t['hit'] <= definition['gold']
            assert 0 <= t['raw_hidden'] <= definition['gold']
            assert 0 <= t['original_hidden'] <= definition['original_gold']
            assert 0 <= t['covered_characters'] <= definition['characters']
            values = {k: definition[k] for k in ('gold','original_gold','characters')}
            values.update({k: t[k] for k in ('hit','hidden','raw_hidden','original_hidden','covered_characters')})
            csv_labels[(*key, t['label'])] = values | {'category': definition['category'], 'group': definition['group'], 'train': r['train']}
            acc = grouped.setdefault(definition['category'], Counter())
            acc.update(values)
        for cat, acc in grouped.items():csv_categories[(*key,cat)] = dict(acc) | {'train':r['train']}
        gold = sum(g['gold'] for g in grouped.values())
        hit = sum(t['hit'] for t in r['types'])
        hidden = sum(t['hidden'] for t in r['types'])
        assert gold - hit == source.get('missed', source.get('miss'))
        if key[0].startswith('composition:'):
            assert hidden == source['hid']
            for field, old in (('char_tp','tp'),('char_fp','fp'),('char_fn','fn'),('negative_rows','nneg'),('negative_rows_touched','fire'),('negative_characters','negchars'),('negative_characters_masked','extra')):
                assert r[field] == source[old]
        else:
            assert abs(100*hidden/gold - source['hidden_pct_reported']) <= .051
        assert r['positive_rows'] + r['negative_rows'] == datasets[ds]['rows']
        for field in ('residual_rows','raw_residual_rows','raw_original_residual_rows'):
            assert 0 <= r[field] <= r['positive_rows']
        assert 0 <= r['negative_rows_touched'] <= r['negative_rows']
        assert 0 <= r['negative_characters_masked'] <= r['negative_characters']
        csv_datasets[key] = {k:v for k,v in r.items() if k!='types'}
        csv_datasets[key].update({k:sum(g[k] for g in grouped.values()) for k in ('gold','original_gold','hit','hidden','raw_hidden','original_hidden')})
        p = r['char_tp']/(r['char_tp']+r['char_fp']) if r['char_tp']+r['char_fp'] else 0
        recall = r['char_tp']/(r['char_tp']+r['char_fn']) if r['char_tp']+r['char_fn'] else 0
        csv_datasets[key].update(char_precision=p,char_recall=recall,char_f1=2*p*recall/(p+recall) if p+recall else 0)
    for filename, lookup, fields in (
        ('entity-metrics.csv',csv_labels,('system','dataset','label')),
        ('category-metrics.csv',csv_categories,('system','dataset','category')),
        ('dataset-metrics.csv',csv_datasets,('system','dataset'))):
        with (ROOT/'results'/filename).open() as f: records=list(csv.DictReader(f))
        assert len(records)==len(lookup)
        assert {tuple(r[k] for k in fields) for r in records}==lookup.keys()
        for record in records:
            for field,value in lookup[tuple(record[k] for k in fields)].items():
                assert record[field]==str(value), (filename,field)
    for d in datasets:assert (ROOT/f'results/types/{d}.md').exists()
    reference = [r for r in b['results'] if r['system']=='composition:pplx+fastino+bardsai+mmbert']
    mask = snapshot['masking_diagnostics']
    for field, old in (('hidden','normalized_fully_hidden_normalized'),('raw_hidden','normalized_fully_hidden_raw'),('original_hidden','original_fully_hidden_raw')):
        assert sum(t[field] for r in reference for t in r['types'])==mask[old]
    for field, old in (('residual_rows','positive_rows_residual_normalized'),('raw_original_residual_rows','positive_rows_residual_raw')):
        assert sum(r[field] for r in reference)==mask[old]
    print(f"Breakdowns: {len(rows):,} exact results; {len(csv_labels):,} original-label rows; category and dataset CSVs matched.")


def github_slug(text):
    """GitHub heading anchor: lowercase, strip punctuation, spaces to hyphens, deduplicate."""
    slug = re.sub(r'[^\w\- ]', '', text.lower()).strip().replace(' ', '-')
    return slug


def heading_anchors(text):
    """Anchors of every heading in a Markdown document, following GitHub dedup rules."""
    anchors, seen = [], {}
    in_code = False
    for line in text.splitlines():
        if line.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r'#{1,6}\s+(.*)', line)
        if not m:
            continue
        slug = github_slug(m.group(1).strip())
        if not slug:
            continue
        seen[slug] = seen.get(slug, 0) + 1
        anchors.append(slug if seen[slug] == 1 else f'{slug}-{seen[slug] - 1}')
    return set(anchors)


def check_anchors(paths):
    """Local Markdown links with #fragments must name an existing heading (F14)."""
    cache = {}
    for p in paths:
        if p.suffix != '.md':
            continue
        rel = p.relative_to(ROOT)
        prose = re.sub(r'```.*?```', '', p.read_text(), flags=re.S)
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', prose):
            url = urlsplit(link)
            if url.scheme or not url.fragment or re.search(r'^[A-Za-z]:', url.path):
                continue
            if not url.path:
                assert url.fragment in heading_anchors(prose), f'Broken self anchor: {rel} -> {link}'
                continue
            target = (p.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(ROOT):
                continue
            key = str(target)
            if key not in cache:
                assert target.exists(), f'Broken local link: {rel} -> {link}'
                cache[key] = heading_anchors(target.read_text())
            assert url.fragment in cache[key], f'Broken anchor: {rel} -> {link}'
    print(f'Anchors: local #fragments checked against GitHub heading slugs.')


def check_public(paths):
    assert '/.local/' in (ROOT/'.gitignore').read_text().splitlines()
    if (ROOT/'.git').exists():
        tracked=subprocess.check_output(['git','ls-files','-z','--cached','--others','--exclude-standard'],cwd=ROOT).decode().split('\0')
        for name in filter(None,tracked):
            p=Path(name)
            assert p.parts[0] in PUBLIC_DIRS or name in PUBLIC_FILES, f'Private or unexpected Git entry: {name}'
        expected={str(p.relative_to(ROOT)) for p in paths}
        assert expected == set(filter(None,tracked)), f'Public files hidden by Git rules: {sorted(expected - set(tracked))}'
        probes=['.local/research/RESULTS/pred.test.jsonl','.local/archive-manifest.json','.env','benchmark/synth_extra.toml']
        for p in probes:
            assert subprocess.run(['git','check-ignore','--no-index','-q',p],cwd=ROOT).returncode==0,p
    for p in paths:
        rel=p.relative_to(ROOT)
        assert p.stat().st_size < 25_000_000, f'Unexpected large public file: {rel}'
        if p.suffix in ('.md','.py','.toml','.json','.csv','.yml','.cff','.txt','.svg') or p.name in ('LICENSE','NOTICE','uv.lock'):
            text=p.read_text()
            assert not re.search(r'/Users/[A-Za-z0-9._-]{2,}/|/home/[A-Za-z0-9._-]{2,}/|[A-Z]:\\Users\\',text), f'Personal path: {rel}'
            assert not re.search(r'(?m)^-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----$',text), f'Private key block: {rel}'
        if p.suffix=='.md':
            assert '\u2014' not in text, f'Long dash: {rel}'
            assert not re.search(r'^\s*>',text,re.M), f'Blockquote: {rel}'
            prose=re.sub(r'```.*?```','',text,flags=re.S)
            for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',prose):
                url=urlsplit(link)
                if url.scheme:continue
                if url.fragment and not url.path:
                    assert url.fragment in heading_anchors(prose), f'Broken self anchor: {rel} -> {link}'
                if not url.path:continue
                target=(p.parent/unquote(url.path)).resolve()
                assert target.is_relative_to(ROOT) and target.exists(), f'Broken local link: {rel} -> {link}'
            if rel.parts[0]!='results':
                assert not re.search('[\u0400-\u04ff]',prose), f'Non-English prose: {rel}'
    for p in (ROOT/'assets').glob('*.svg'):
        node=ET.parse(p).getroot()
        assert node.find('{http://www.w3.org/2000/svg}title') is not None, p.name
        assert 'http://purl.org/dc/elements/1.1/' in p.read_text(),p.name
    assert len(list((ROOT/'assets').glob('*.svg')))==11
    offsets = load('benchmark/corpus_offsets.json')
    assert set(offsets) == {'leak-museum', 'leaky-repo'}
    totals = {}
    for name, dataset in offsets.items():
        assert set(dataset) == {'bench_sha256', 'files', 'revision'}
        assert re.fullmatch(r'[0-9a-f]{64}', dataset['bench_sha256'])
        assert re.fullmatch(r'[0-9a-f]{40}', dataset['revision'])
        total = 0
        for filename, entry in dataset['files'].items():
            assert filename and not Path(filename).is_absolute() and '..' not in Path(filename).parts
            assert set(entry) == {'sha256', 'spans'} and re.fullmatch(r'[0-9a-f]{64}', entry['sha256'])
            assert all(isinstance(a, int) and isinstance(b, int) and 0 <= a < b
                       for a, b in entry['spans'])
            total += len(entry['spans'])
        totals[name] = total
    assert totals == {'leak-museum': 101, 'leaky-repo': 95}
    source = (ROOT/'benchmark/sets_code.py').read_text()
    assert 'LM_VALUES' not in source and 'LR_VALUES' not in source
    manifest=load('benchmark/PROVENANCE.json')['public_module_sha256']
    for name,value in manifest.items():assert hashlib.sha256((ROOT/'benchmark'/name).read_bytes()).hexdigest()==value,name
    print(f'Publication: {len(paths)} files; English prose, local links, SVG metadata and private-directory rules checked.')


def check_readme_blocks():
    """The four README generated blocks must exist and match the snapshot (audit E/7.5)."""
    s = load('results/snapshot.json')
    counts = s['composition_counts']
    names = ('pplx', 'fastino', 'pplx+fastino', 'pplx+fastino+mmbert',
             'pplx+fastino+bardsai', 'pplx+fastino+bardsai+mmbert')
    text = (ROOT / 'README.md').read_text()
    for name in ('SNAPSHOT', 'HEADLINE OUTCOMES', 'COMPOSITION COMPARISON', 'DATASET EXAMPLES'):
        assert len(re.findall(f'<!-- (BEGIN|END) {name} -->', text)) == 2, f'Missing README block: {name}'
    mask = s['masking_diagnostics']
    head = mask['composition']
    summary = {r['composition']: r for r in csv.DictReader((ROOT / 'results/summary.csv').open())}
    total_miss = int(summary[head]['miss'])
    for label, part, whole in (
            ('Normalized annotations untouched', total_miss, mask['gold_normalized']),
            ('Normalized annotations not fully hidden', mask['gold_normalized'] - mask['normalized_fully_hidden_normalized'], mask['gold_normalized']),
            ('Annotated rows with residual gold characters', mask['positive_rows_residual_normalized'], mask['positive_rows']),
            ('Unannotated rows touched by a mask', mask['clean_rows_touched'], mask['clean_rows']),
            ('Characters masked in unannotated rows', mask['clean_characters_masked'], mask['clean_characters'])):
        assert f'| {label} | {part:,} / {whole:,} |' in text, f'README headline row missing or stale: {label}'
    summary = {r['composition']: r for r in csv.DictReader((ROOT / 'results/summary.csv').open())}
    for name in names:
        r = summary[name]
        untouched = f"{100 * int(r['miss']) / int(r['nspan']):.2f}%"
        residual = f"{float(r['residual_pct']):.2f}%"
        clean = f"{100 * int(r['extra']) / int(r['negchars']):.2f}%"
        assert f'| {untouched} | {residual} | {clean} |' in text, f'README comparison row missing or stale: {name}'
    print('README: four generated blocks present and matched to the snapshot.')


def check_reports():
    """T07: no published report presents a missing annotation as safe content.

    The exact CSVs keep their technical column names; the generated Markdown
    must not reintroduce the older wording that read an absent annotation as
    proof that a row had nothing to hide.
    """
    banned = ('nothing to hide', 'FP rows', 'FP chars')
    paths = [ROOT / 'README.md'] + sorted((ROOT / 'results').rglob('*.md')) + sorted((ROOT / 'docs').glob('*.md'))
    for p in paths:
        text = p.read_text()
        for phrase in banned:
            assert phrase not in text, f'Misleading presentation label in {p.relative_to(ROOT)}: {phrase!r}'
    print(f'Reports: {len(paths)} published Markdown files free of the retired wordings.')


def main():
    if not __debug__:raise SystemExit('Run verification without Python optimization')
    check_snapshot()
    check_public(files())
    check_anchors(files())
    check_readme_blocks()
    check_reports()
    for command in ([sys.executable,'benchmark/selftest.py'],[sys.executable,'benchmark/rules_ru.py','--selftest'],[sys.executable,'tests/test_publication.py'],[sys.executable,'tests/test_stratify.py'],[sys.executable,'tests/test_usage_example.py'],[sys.executable,'tests/test_export_swap.py'],[sys.executable,'tests/test_scanner_offsets.py'],[sys.executable,'tests/test_scan_gate.py'],[sys.executable,'tests/test_scoring_contract.py']):
        subprocess.run(command,cwd=ROOT,check=True)
    print('Publication verification passed.')


if __name__=='__main__':main()
