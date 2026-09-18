import collections, multiprocessing, os, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import score as S
COMBOS = [('gitleaks', ['gitleaks'], 1), ('pplx', ['pplx'], 1), ('gitleaks+pplx', ['gitleaks', 'pplx'], 1), ('gitleaks+pplx+nvidia', ['gitleaks', 'pplx', 'gliner-nvidia'], 1), ('gitleaks+pplx+nvidia+legal', ['gitleaks', 'pplx', 'gliner-nvidia', 'ru-legal-ner'], 1), ('gitleaks+pplx+opf2+nvidia', ['gitleaks', 'pplx', 'opf-ru-v2', 'gliner-nvidia'], 1), ('gitleaks+pplx+opf2+nvidia+legal', ['gitleaks', 'pplx', 'opf-ru-v2', 'gliner-nvidia', 'ru-legal-ner'], 1), ('gitleaks+pplx+legal+vladlinv', ['gitleaks', 'pplx', 'ru-legal-ner', 'gliner2-vladlinv'], 1), ('fastino', ['gliner2-fastino'], 1), ('pplx+fastino', ['pplx', 'gliner2-fastino'], 1), ('pplx+fastino+mmbert', ['pplx', 'gliner2-fastino', 'mmbert32k'], 1), ('pplx+fastino+bardsai', ['pplx', 'gliner2-fastino', 'bardsai-eu'], 1), ('pplx+fastino+bardsai+mmbert', ['pplx', 'gliner2-fastino', 'bardsai-eu', 'mmbert32k'], 1), ('vote2(pplx,opf2,nvidia)', ['pplx', 'opf-ru-v2', 'gliner-nvidia'], 2), ('vote2(gitleaks,pplx,opf2,nvidia)', ['gitleaks', 'pplx', 'opf-ru-v2', 'gliner-nvidia'], 2)]
PAIRS = [('gitleaks+pplx+nvidia+legal', 'pplx'), ('gitleaks+pplx+nvidia+legal', 'gitleaks+pplx+opf2+nvidia'), ('vote2(pplx,opf2,nvidia)', 'pplx'), ('pplx+fastino', 'pplx'), ('pplx+fastino', 'fastino'), ('pplx+fastino+bardsai', 'pplx+fastino'), ('pplx+fastino+bardsai+mmbert', 'pplx+fastino+bardsai')]

def benches():
    return [d.name for d in (sorted(S.BENCH.iterdir()) if S.BENCH.exists() else []) if S.BENCH.exists() if d.is_dir() and (S.RESULTS / d.name).exists()]

def preds(bench, model):
    f = S.RESULTS / bench / f'pred.{model}.jsonl'
    if not f.exists():
        return None
    meta, pred = S.read_pred(f)
    if bad := S.check_predictions(f, meta, pred, complete=True, expected=bench, expected_model=model):
        sys.exit(bad)
    g = S.gold(bench)[0]
    return {rid: S.norm(g[rid][0], S.keep(pred[rid]['spans']), 'label') for rid in g}

def union(cs, ms, rid, k):
    if k == 1:
        return set().union(*(S.chars(cs[m][rid]) for m in ms))
    cnt = collections.Counter()
    for m in ms:
        cnt.update(S.chars(cs[m][rid]))
    return {p for p, c in cnt.items() if c >= k}

def _combos_set(b):
    g = S.gold(b)[0]
    need = sorted({m for _, ms, _ in COMBOS for m in ms})
    cs = {m: preds(b, m) for m in need}
    ge = S.gold_norm(b)
    gc = {rid: S.chars(ge[rid]) for rid in g}
    nspan = sum((len(v) for v in ge.values()))
    nneg = sum((1 for rid in g if not g[rid][1]))
    rows, train, per = ({}, set(), {})
    for name, ms, k in COMBOS:
        if any((b in S.dirty(m) for m in ms)):
            train.add(name)
            continue
        if any((cs[m] is None for m in ms)):
            continue
        miss = tp = fp = fn = fire = 0
        rtp, rfp, rfn = ([], [], [])
        for rid in g:
            pc = union(cs, ms, rid, k)
            for x, y, _ in ge[rid]:
                miss += not any((p in pc for p in range(x, y)))
            a, c, d = (len(gc[rid] & pc), len(pc - gc[rid]), len(gc[rid] - pc))
            tp += a
            fp += c
            fn += d
            rtp.append(a)
            rfp.append(c)
            rfn.append(d)
            if not g[rid][1] and pc:
                fire += 1
        P, R, F = S.prf(tp, fp, fn)
        rows[name] = (P, R, F, fire, nneg, miss, nspan)
        per[name] = (rtp, rfp, rfn)
    rng = random.Random(0)
    n = len(g)
    idxs = [rng.choices(range(n), k=n) for _ in range(500)]

    def f1(name, idx):
        t, f, m = per[name]
        return S.prf(sum(map(t.__getitem__, idx)), sum(map(f.__getitem__, idx)), sum(map(m.__getitem__, idx)))[2]
    pairs = {}
    for a, c in PAIRS:
        if a in per and c in per:
            d = sorted((f1(a, i) - f1(c, i) for i in idxs))
            pairs[f'{a} - {c}'] = (d[12], d[487])
    return (b, rows, train, pairs)

def jobs_of(n):
    j = int(os.environ.get('JOBS') or min(os.cpu_count() or 1, 8))
    return max(1, min(j, n))

def combos_report():
    bs = benches()
    rows = {name: {} for name, _, _ in COMBOS}
    train = {name: set() for name, _, _ in COMBOS}
    pairs = {}
    if jobs_of(len(bs)) > 1:
        with multiprocessing.Pool(jobs_of(len(bs))) as pool:
            done = pool.imap_unordered(_combos_set, bs)
            got = [(b, r, tr, pr) for b, r, tr, pr in done]
    else:
        got = [_combos_set(b) for b in bs]
    for b, r, tr, pr in got:
        for name, v in r.items():
            rows[name][b] = v
        for name in tr:
            train[name].add(b)
        pairs[b] = pr

    def cell(name, b, txt):
        return 'train' if b in train[name] else '-' if b not in rows[name] else txt()
    out = ['# Ensembles', '', 'Computed over the saved predictions: union of characters, or a k-of-N vote. Main metric - missed spans, a gold span no character of the composition touched. The unit of counting is the gold span of `score.py`, so the numbers match the per-set reports. `-` means one of the members has no run on that set; `train` means one of them was trained on the source of the set (its slices and corrupted copies count), so the composition is not scored there.', '', '## Missed spans, % of the gold spans of the set', '', '| composition | ' + ' | '.join(bs) + ' |', '|---|' + '---|' * len(bs)]
    for name, _, _ in COMBOS:
        out.append(f'| {name} | ' + ' | '.join((cell(name, b, lambda b=b, name=name: f'{S.pct(rows[name][b][5], rows[name][b][6])} ({rows[name][b][5]})') for b in bs)) + ' |')
    out += ['', '## char F1, reference', '', '| composition | ' + ' | '.join(bs) + ' |', '|---|' + '---|' * len(bs)]
    for name, _, _ in COMBOS:
        out.append(f'| {name} | ' + ' | '.join((cell(name, b, lambda b=b, name=name: f'{rows[name][b][2]:.3f}') for b in bs)) + ' |')
    out += ['', '## Precision / recall / rows without annotations', '',
            '`Rows touched` counts rows the source left without annotations where a composition masked something. It is not a false-alarm rate: the absence of annotations is not evidence that these rows hold nothing sensitive. The exact CSV keeps the technical column name `fp_rows` for the same count.', '']
    for b in bs:
        out += [f'### {b}', '', '| composition | missed | P | R | F1 | rows touched |', '|---|---|---|---|---|---|']
        for name, _, _ in COMBOS:
            if b not in rows[name]:
                mark = 'train' if b in train[name] else '-'
                out.append(f'| {name} | {mark} | {mark} | {mark} | {mark} | {mark} |')
                continue
            P, R, F, fire, nneg, miss, nspan = rows[name][b]
            out.append(f'| {name} | {miss} ({S.pct(miss, nspan)}) | {P:.3f} | {R:.3f} | {F:.3f} | ' + (f'{fire}/{nneg} |' if nneg else 'no negatives |'))
        out.append('')
    keys = sorted({k for v in pairs.values() for k in v})
    if keys:
        out += ['## Paired bootstrap, 95% (char F1 difference, 500 resamples)', '', '| set | ' + ' | '.join(keys) + ' |', '|---|' + '---|' * len(keys)]
        for b in bs:
            out.append(f'| {b} | ' + ' | '.join((f'[{pairs[b][k][0]:+.3f}, {pairs[b][k][1]:+.3f}]' if k in pairs[b] else '-' for k in keys)) + ' |')
        out.append('')
    return out

def _cover_set(args):
    b, models = args
    ge = S.gold_norm(b)
    items = {(b, rid, i) for rid, sp in ge.items() for i in range(len(sp))}
    has, cover = (set(), {})
    for m in models:
        ps = preds(b, m)
        if ps is None:
            continue
        has.add(m)
        cover[m] = {(b, rid, i) for rid, sp in ge.items() for i, (a, c, _) in enumerate(sp) if any((x < c and y > a for x, y, _ in ps[rid]))}
    return (b, items, has, cover)

def greedy_report(device):
    bs = benches()
    alt = 'cpu' if device == 'cuda' else 'cuda'
    per = S.speed_of(device, bs) | S.speed_of(alt, bs)
    if not per:
        return []
    ref = max(per, key=lambda m: (m[0] == device, len(per[m])))
    fast, borrowed = (dict(per[ref]), {})
    for mach, sp in per.items():
        for n, v in sp.items():
            if mach != ref and n not in fast:
                fast[n] = v
                borrowed[n] = mach
    note = f" Speed of {', '.join(sorted(borrowed))} is measured on another machine ({'; '.join(sorted({str(m) for m in borrowed.values()}))}), not on {ref}, so the cost of a composition with them is only an estimate." if borrowed else ''
    cands = {}
    for b in bs:
        for f in (S.RESULTS / b).glob('pred.*.jsonl'):
            n = f.stem[5:]
            base = S.base_of(n)
            if S.CFG.get(base, {}).get('mirror'):
                continue
            if n in fast and len(n) < len(cands.get(base, n + 'x')):
                cands[base] = n
    models = sorted(cands.values())
    lang = {b: S.meta_of(b)['lang'] for b in bs}
    kind = {b: S.meta_of(b)['kind'] for b in bs}
    items, cover, has = ({}, {m: set() for m in models}, {m: set() for m in models})
    if jobs_of(len(bs)) > 1:
        with multiprocessing.Pool(jobs_of(len(bs))) as pool:
            got = list(pool.imap_unordered(_cover_set, [(b, models) for b in bs]))
    else:
        got = [_cover_set((b, models)) for b in bs]
    for b, it, hs, cv in got:
        items[b] = it
        for m in hs:
            has[m].add(b)
        for m, s in cv.items():
            cover[m] |= s

    def applies(m, b):
        return not (S.CFG.get(S.base_of(m), {}).get('labels') == 'ru' and lang[b] != 'ru')
    why = {}
    for b in bs:
        train = [m for m in models if b in S.dirty(m)]
        absent = [m for m in models if applies(m, b) and b not in has[m]]
        if train:
            why[b] = 'train: ' + ', '.join(train)
        elif absent:
            why[b] = 'no run: ' + ', '.join(absent[:3]) + ('...' if len(absent) > 3 else '')
    pool = [b for b in bs if b not in why]
    left = '; '.join((f'{b} ({w})' for b, w in why.items())) or 'none'
    if not pool:
        return ['## Greedy cover', '', f'No common tasks: every set has a contaminated candidate or a missing run. Left out: {left}.', '']
    dev = {x for b in pool for x in items[b] if S.fold(b, x[1]) == 'dev'}
    test = {x for b in pool for x in items[b] if S.fold(b, x[1]) == 'test'}

    def pooled(ms, keep_b):
        use = {x for b in keep_b if b in pool for x in items[b]} & test
        got = set().union(*(cover[m] for m in ms))
        return (len(use - got) / len(use) if use else None, sum((1 for b in keep_b if b in pool)))
    start = min(models, key=lambda m: len(dev - cover[m]))
    chosen, rows = ([start], [])
    covered = set(cover[start])
    while True:
        cur = list(chosen)
        cells = []
        for keep_b in ([b for b in bs if lang[b] == 'ru'], [b for b in bs if lang[b] == 'en'], [b for b in bs if lang[b] == 'multi'], [b for b in bs if kind[b] == 'secrets']):
            p, k = pooled(cur, keep_b)
            cells.append(f'{p:.1%} ({k})' if p is not None else '-')
        cps = 1 / sum((1 / fast[m] for m in cur))
        rows.append((cur[-1], cells, cps))
        best, gain = (None, 0)
        for m in models:
            if m in chosen:
                continue
            g = len(cover[m] - covered & dev) * fast[m]
            if g > gain:
                best, gain = (m, g)
        if best is None:
            break
        chosen.append(best)
        covered |= cover[best]
    out = ['## Greedy cover', '', f'Start: the single detector with the fewest missed spans on the dev half. Each step adds the detector that removes the most remaining dev misses per second of cost, cost = 1 / chars-per-second from the {device} runs on {ref}.{note} Detectors run one after another, so the speed of a composition is 1 / sum(1 / speed). Every row is the composition of all the rows above it plus the one it adds.', '', f"Common tasks: {len(pool)} sets where no candidate was trained on the source and every candidate has a run ({', '.join(pool)}). Left out: {left}. Rows are split in half by crc32 of (base set, row id), so a corrupted copy lands in the same half as its original and so does an exact duplicate of a text inside one set; the composition is chosen on the dev half ({len(dev)} spans) and every number below is the test half ({len(test)} spans). Missed % per cut is over the pool sets of that cut, their count in brackets.", '', '| step | added | ru | en | multi | secrets | chars/s |', '|---|---|---|---|---|---|---|']
    for i, (name, cells, cps) in enumerate(rows, 1):
        out.append(f'| {i} | {name} | ' + ' | '.join(cells) + f' | {cps:.0f} |')
    return out + ['']

def main():
    device = 'cuda'
    if '--device' in sys.argv:
        device = sys.argv[sys.argv.index('--device') + 1]
    out = combos_report()
    if '--greedy' in sys.argv:
        out += greedy_report(device)
    (S.RESULTS / 'ENSEMBLE.md').write_text('\n'.join(out) + '\n')
    print('\n'.join(out))
if __name__ == '__main__':
    main()
