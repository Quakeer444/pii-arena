import csv, fcntl, hashlib, json, os, platform, random, re, socket, subprocess, sys
from pathlib import Path
ROOT = Path(os.environ.get('BENCHMARK_DATA', str(Path(__file__).resolve().parent.parent / '.local' / 'research'))).resolve()
BENCH, RAW = (ROOT / 'BENCH', ROOT / 'BENCH' / 'raw')
SAMPLES_F = BENCH / 'samples.json'
GROUPS = ('PERSON', 'ADDRESS', 'CONTACT', 'ID', 'NET', 'ACCOUNT', 'SECRET', 'ORG', 'DATE', 'OTHER')
DEDUPE = ('alexen2', 'ameau01', 'arthur-passwords', 'creddata', 'nym-en')
csv.field_size_limit(10 ** 7)
PROTOCOL = 1

def bench_sha256(csv_path):
    return hashlib.sha256(Path(csv_path).read_bytes()).hexdigest()

def machine():
    cpu = ''
    try:
        if sys.platform == 'darwin':
            cpu = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string'], text=True).strip()
        else:
            with open('/proc/cpuinfo') as fh:
                cpu = next((ln.split(':', 1)[1].strip() for ln in fh if ln.startswith('model name')), '')
    except Exception:
        pass
    return {'cpu': cpu or platform.processor() or '?', 'host': hashlib.sha256(socket.gethostname().encode()).hexdigest()[:12], 'workers': int(os.environ.get('W') or 1)}
_CYR, _LAT, _UKR = (re.compile('[а-яА-ЯёЁ]'), re.compile('[a-zA-Z]'), re.compile('[іїєґІЇЄҐ]'))

def ru(text):
    c = len(_CYR.findall(text))
    return c > 5 and c > len(_LAT.findall(text)) and (not _UKR.search(text))

def pick(name, ids, k):
    with SAMPLES_F.open('r+') as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        samples = json.load(fh)
        if name not in samples:
            samples[name] = sorted(random.Random(0).sample(sorted(ids), k)) if len(ids) > k else sorted(ids)
            fh.seek(0)
            fh.truncate()
            fh.write(json.dumps(samples, ensure_ascii=False, indent=1))
        return samples[name]

def find_all(text, needle, seen):
    out, pos = ([], 0)
    while (i := text.find(needle, pos)) >= 0:
        if not any((a < i + len(needle) and b > i for a, b in seen)):
            out.append((i, i + len(needle)))
            seen.append((i, i + len(needle)))
        pos = i + 1
    return out

def build(name, builder, meta):
    assert meta['lang'] in ('ru', 'en', 'multi') and meta['kind'] in ('pii', 'secrets'), name
    assert set(meta['groups'].values()) <= set(GROUPS), (name, set(meta['groups'].values()) - set(GROUPS))
    out = BENCH / name / 'bench.csv'
    out.parent.mkdir(exist_ok=True)
    n = spans = neg = cr = dup = 0
    ids, types, seen = (set(), set(), set())
    with out.open('w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['id', 'domain', 'text', 'entities'])
        for rid, dom, text, ents in builder():
            if name in DEDUPE:
                key = (text, json.dumps(ents, ensure_ascii=False, sort_keys=True))
                if key in seen:
                    dup += 1
                    continue
                seen.add(key)
            assert rid not in ids, rid
            ids.add(rid)
            cr += '\r' in text
            for e in ents:
                assert 0 <= e['start'] < e['end'] <= len(text), (name, rid, e)
                assert text[e['start']:e['end']].strip(), (name, rid, e)
                types.add(e['type'])
            w.writerow([rid, dom, text, json.dumps(ents, ensure_ascii=False)])
            n += 1
            spans += len(ents)
            neg += not ents
    missing = types - set(meta['groups'])
    assert not missing, (name, 'types missing from meta.groups', sorted(missing))
    prev = BENCH / name / 'meta.json'
    if 'raw' not in meta and prev.exists() and ('raw' in (old := json.loads(prev.read_text()))):
        meta = meta | {'raw': old['raw']}
    prev.write_text(json.dumps(meta, ensure_ascii=False, indent=1) + '\n')
    print(f"{name}: {n} rows, {spans} spans, {neg} negatives, {cr} rows with \\r{(f', duplicates removed {dup}' if dup else '')} -> {out}")

def table():
    rows = []
    for d in sorted(BENCH.iterdir()):
        if not (d / 'meta.json').exists() or not (d / 'bench.csv').exists():
            continue
        m = json.loads((d / 'meta.json').read_text())
        n = spans = neg = chars = 0
        for r in csv.DictReader((d / 'bench.csv').open(newline='')):
            ents = json.loads(r['entities'])
            n += 1
            spans += len(ents)
            neg += not ents
            chars += len(r['text'])
        rows.append((m['lang'], m['kind'], d.name, n, spans, neg, chars, m['license'], m['mode'], m['source']))
    order = {'ru': 0, 'en': 1, 'multi': 2}
    out = ['| dataset | language | kind | rows | spans | negatives | characters | license | mode | source |', '|---|---|---|---:|---:|---:|---:|---|---|---|']
    for lang, kind, name, n, spans, neg, chars, lic, mode, src in sorted(rows, key=lambda r: (order[r[0]], r[1], r[2])):
        out.append(f'| {name} | {lang} | {kind} | {n} | {spans} | {neg} | {chars / 1000000.0:.2f}M | {lic} | {mode} | {src} |')
    out.append(f'\nTotal: {len(rows)} datasets, {sum((r[3] for r in rows))} rows, {sum((r[4] for r in rows))} spans, {sum((r[6] for r in rows)) / 1000000.0:.1f} million characters.')
    return '\n'.join(out)

def main(builders, meta):
    if sys.argv[1:] == ['--table']:
        print(table())
        return
    for name in sys.argv[1:] or builders:
        build(name, builders[name], meta[name])
