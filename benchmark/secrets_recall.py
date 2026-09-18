import collections, json, multiprocessing, os, statistics, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import score as S

def benches():
    return [d.name for d in (sorted(S.BENCH.iterdir()) if S.BENCH.exists() else []) if S.BENCH.exists() if d.is_dir() and (S.RESULTS / d.name).exists()]
ALLSETS = benches()
SETS = [b for b in ALLSETS if S.meta_of(b)['kind'] == 'secrets']
PII = [b for b in ALLSETS if S.meta_of(b)['kind'] == 'pii']
ALL = sorted((m for m, c in S.CFG.items() if c['family'] != 'leaks'))
OPTS = [('gitleaks', ['gitleaks'], 1), ('betterleaks', ['betterleaks'], 1), ('gitleaks + betterleaks', ['gitleaks', 'betterleaks'], 1), ('pplx', ['pplx'], 1), ('gitleaks + pplx', ['gitleaks', 'pplx'], 1), ('gitleaks + pplx + gliner-nvidia', ['gitleaks', 'pplx', 'gliner-nvidia'], 1), ('gitleaks + pplx + gliner-nvidia + ru-legal-ner', ['gitleaks', 'pplx', 'gliner-nvidia', 'ru-legal-ner'], 1), ('gitleaks + pplx + opf-ru-v2 + gliner-nvidia', ['gitleaks', 'pplx', 'opf-ru-v2', 'gliner-nvidia'], 1), ('gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner', ['gitleaks', 'pplx', 'opf-ru-v2', 'gliner-nvidia', 'ru-legal-ner'], 1), ('gitleaks + pplx + ru-legal-ner + gliner2-vladlinv', ['gitleaks', 'pplx', 'ru-legal-ner', 'gliner2-vladlinv'], 1), ('pplx + gliner2-fastino', ['pplx', 'gliner2-fastino'], 1), ('pplx + gliner2-fastino + mmbert32k', ['pplx', 'gliner2-fastino', 'mmbert32k'], 1), ('pplx + gliner2-fastino + bardsai-eu + mmbert32k', ['pplx', 'gliner2-fastino', 'bardsai-eu', 'mmbert32k'], 1), ('vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia)', ['pplx', 'opf-ru-v2', 'gliner-nvidia'], 2), (f'gitleaks + all {len(ALL)} models', ['gitleaks'] + ALL, 1)]
PICK = 'pplx + gliner2-fastino + mmbert32k'

def load(b, models):
    out = {}
    for m in models:
        f = S.RESULTS / b / f'pred.{m}.jsonl'
        if not f.exists():
            continue
        meta, pred = S.read_pred(f)
        if bad := S.check_predictions(f, meta, pred, complete=True, expected=b, expected_model=m):
            sys.exit(bad)
        g = S.gold(b)[0]
        out[m] = {rid: S.norm(g[rid][0], S.keep(pred[rid]['spans']), 'label') for rid in g}
    return out

def covered(cs, ms, rid, k):
    if k == 1:
        return set().union(*(S.chars(cs[m][rid]) for m in ms))
    cnt = {}
    for m in ms:
        for p in S.chars(cs[m][rid]):
            cnt[p] = cnt.get(p, 0) + 1
    return {p for p, c in cnt.items() if c >= k}

def tally(b, cs, ms, k):
    g = S.gold(b)[0]
    ge = S.gold_norm(b)
    gg = S.meta_of(b)['groups']
    hit = miss = hid = tp = fp = fn = fire = extra = negchars = nneg = 0
    grp = collections.defaultdict(lambda: [0, 0])
    for rid in g:
        pc = covered(cs, ms, rid, k)
        for a, c, t in ge[rid]:
            got = any((p in pc for p in range(a, c)))
            hit += got
            miss += not got
            hid += all((p in pc for p in range(a, c)))
            q = grp[gg.get(t, 'OTHER')]
            q[0] += not got
            q[1] += 1
        gc = S.chars(ge[rid])
        tp += len(gc & pc)
        fp += len(pc - gc)
        fn += len(gc - pc)
        if not g[rid][1]:
            nneg += 1
            negchars += len(g[rid][0])
            fire += bool(pc)
            extra += len(pc)
    return {'hit': hit, 'miss': miss, 'hid': hid, 'nspan': sum((len(v) for v in ge.values())), 'f1': S.prf(tp, fp, fn)[2], 'p': S.prf(tp, fp, fn)[0], 'r': S.prf(tp, fp, fn)[1], 'tp': tp, 'fp': fp, 'fn': fn, 'fire': fire, 'nneg': nneg, 'extra': extra, 'negchars': negchars, 'grp': dict(grp)}

def mark(a):
    return '' if a['have'] == a['of'] else f" [{a['have']}/{a['of']}]"


def composition_status(name, have=None):
    """R06/T05: rows built from stored pre-correction scanner predictions are
    labeled next to the number, not only in the changelog. `have` names the
    members that actually produced the row, so a composition whose declared
    scanner has no run on this set is not labeled after a scanner that did not
    take part."""
    try:
        from run_leaks import adapter_status
    except ImportError:
        return ''
    members = next((ms for n, ms, _ in OPTS if n == name), [])
    if any(adapter_status(m) == 'historical-pre-fix' for m in (members if have is None else have)):
        return ' `historical pre-fix`'
    return ''

def usable(ms, have, k):
    return len(have) >= (len(ms) if k > 1 else 1)

def rate(ms):
    tot = 0.0
    for m in ms:
        rows = secs = 0.0
        for b in ALLSETS:
            f = S.RESULTS / b / f'pred.{m}.jsonl'
            if not f.exists():
                continue
            meta = S.read_pred(f)[0]
            rows += meta.get('rows') or 0
            secs += meta.get('elapsed_s') or 0
        if rows and secs:
            tot += secs / rows
    return 1 / tot if tot else None
CSS = ':root{color-scheme:light dark;--bg:#fff;--fg:#1a1a1a;--dim:#6b7280;--line:#e5e7eb;--pick:#f0fdf4;--pickb:#16a34a}\n@media(prefers-color-scheme:dark){:root{--bg:#0f1115;--fg:#e5e7eb;--dim:#9ca3af;--line:#242832;--pick:#0f2417;--pickb:#22c55e}}\n*{box-sizing:border-box}body{margin:0;padding:28px 20px;background:var(--bg);color:var(--fg);\nfont:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif}\nmain{max-width:1100px;margin:0 auto}h1{font-size:17px;font-weight:600;margin:0 0 4px}\np{color:var(--dim);font-size:12.5px;margin:0 0 18px}.wrap{overflow-x:auto;border:1px solid var(--line);border-radius:8px}\ntable{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}\nth,td{padding:6px 10px;text-align:right;white-space:nowrap;border-bottom:1px solid var(--line)}\nthead th{position:sticky;top:0;background:var(--bg);font-weight:600;font-size:11.5px;color:var(--dim);\ntext-transform:uppercase;letter-spacing:.03em}\nthead tr:first-child th{border-bottom:0;padding-bottom:1px}\nth.sub{text-transform:none;letter-spacing:0;font-weight:400;font-size:10.5px;padding-top:0;opacity:.75}th:first-child,td:first-child{text-align:left;position:sticky;left:0;background:var(--bg)}\ntbody tr:last-child td{border-bottom:0}tr.pick td{background:var(--pick);font-weight:600}\ntr.pick td:first-child{background:var(--pick);box-shadow:inset 3px 0 var(--pickb)}\nul{color:var(--dim);font-size:12.5px;padding-left:18px;margin:14px 0 0}'

def html(cols, rows, nrows):
    head = '<thead><tr><th rowspan=2>composition</th>' + ''.join((f'<th title="{t}">{h}</th>' for _, h, _, t in cols)) + '</tr><tr>' + ''.join((f'<th class=sub>{s}</th>' for _, _, s, _ in cols)) + '</tr></thead>'
    body = []
    for name, cells in rows:
        cls = ' class="pick"' if name == PICK else ''
        body.append(f'<tr{cls}><td>{name}</td>' + ''.join((f'<td>{cells[i]}</td>' for i, *_ in cols)) + '</tr>')
    doc = f"<!doctype html><html lang=en><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>Masking: every option</title><style>{CSS}</style><main><h1>What each composition hides and what it lets through</h1><p>{len(ALLSETS)} sets, {nrows} rows. Green is the reference composition; read its own numbers in the row, they are not zero. Every cell is the measurement, not a claim.</p><div class=wrap><table>{head}<tbody>{''.join(body)}</tbody></table></div><ul><li><b>Untouched</b> - the annotation was not touched by a single character and goes to the model as it is; partially hidden annotations are not counted here and remain partly exposed. Lower is better.</li><li><b>Over-masked</b> and <b>unannotated rows touched</b> are the price of playing safe: the first counts characters, the second counts rows.</li><li>The rule test cases of <code>gitleaks</code> and <code>betterleaks</code> are their own: there they grade themselves by their own table of rules.</li><li><b>[k/N]</b> - only k of the N members of the composition have a run on that set, so the cell is that partial composition, not the one the name lists.</li><li>Full numbers per set are in <code>RESULTS/SECRETS.md</code> and <code>RESULTS/REPORT.md</code>.</li></ul></main>"
    (S.RESULTS / 'SUMMARY.html').write_text(doc)

def per_set(b):
    cs = load(b, {x for _, ms, _ in OPTS for x in ms})
    agg, train = ({}, {})
    for name, ms, k in OPTS:
        have = [m for m in ms if m in cs]
        train[name] = dirty = any((b in S.dirty(m) for m in ms))
        agg[name] = None if dirty or not usable(ms, have, k) else tally(b, cs, have, k) | {'have': len(have), 'of': len(ms), 'members': have}
    return (b, agg, train)

def scanner_table():
    """T05: the run-level facts a machine-readable consumer needs - which
    datasets each scanner has runs on, how many spans its adapter could not
    place confidently, the mapping policy its metadata records and the
    reviewed release status - in the public report instead of only in prose."""
    try:
        from run_leaks import ADAPTER_STATUS, STATUS_VALUES
    except ImportError:
        return []
    rows = []
    for tool, (policy, status) in ADAPTER_STATUS.items():
        sets, runs, unresolved, recorded = ([], 0, 0, set())
        for b in ALLSETS:
            f = S.RESULTS / b / f'pred.{tool}.jsonl'
            if not f.exists():
                continue
            meta = S.read_pred(f)[0]
            sets.append(b)
            runs += 1
            unresolved += meta.get('unresolved_spans') or 0
            recorded.add(meta.get('adapter_policy') or 'not recorded')
        assert status in STATUS_VALUES, status
        rows.append((tool, status, runs, len(sets), unresolved, ' + '.join(sorted(recorded)) or '-'))
    return ['## Scanner runs: status and unresolved findings', '',
            '`Unresolved` counts findings whose exact secret range the adapter could not place: the span keeps the range the scanner reported (for a decoded finding, the encoded segment) and is scored there, so it can mask more text than the credential occupies. Such a run stays comparable, but the count is part of reading it; per-run counts are in the [run inventory](../results/run-inventory.json) as `unresolved_spans` and `adapter_status`. `Mapping` is the adapter policy recorded in the run metadata; a run without one predates policy recording.', '',
            '| scanner | release status | runs | datasets | unresolved findings | mapping |', '|---|---|---:|---:|---:|---|'] + \
           [f'| `{tool}` | {status} | {runs} | {sets} | {unresolved} | {policy} |' for tool, status, runs, sets, unresolved, policy in rows] + ['']


def run_unresolved(tool):
    """Findings the adapter stored without a located secret, over every set
    the scanner ran on (T05): the count is read from run metadata, so the
    published report states the number the artifacts carry."""
    total = 0
    for b in ALLSETS:
        f = S.RESULTS / b / f'pred.{tool}.jsonl'
        if f.exists():
            total += json.loads(f.open().readline())['meta'].get('unresolved_spans') or 0
    return total


def partial_table(agg):
    """T05: which members actually produced a partial row, so `[k/N]` is not
    the only evidence in the table."""
    rows = []
    for b in ALLSETS:
        for name, ms, _ in OPTS:
            a = agg[b].get(name)
            if a and a['have'] < a['of']:
                rows.append((b, name, a['have'], a['of'], ' + '.join(a['members'])))
    if not rows:
        return []
    return ['## Partial compositions: the members that actually ran', '',
            'A row marked `[k/N]` is not the composition its name lists: only these members have a run on that dataset.', '',
            '| dataset | composition | k/N | members used |', '|---|---|---:|---|'] + \
           [f'| {b} | {name} | {k}/{n} | {" + ".join(f"`{m}`" for m in ms.split(" + "))} |' for b, name, k, n, ms in rows] + ['']


def main():
    lines = ['# Secrets: a miss costs more than playing safe', '',
             'Span recall - the share of annotated spans a detector touched with at least one character. **Missed** - annotated spans not touched at all. **Untouched annotations** are the same missed count stated plainly: it does not mean partially hidden spans are safe. **Unannotated rows touched** - rows without annotations where the detector found something; the volume of that extra masking in characters is next to it. Rows without annotations are not guaranteed to be free of sensitive content.',
             f'Score threshold {S.THRESH:g}; spans without a score always count.', '',
             '## Scanner-coordinate status (2026-09-18 capture and decoded-content correction)', '',
             'Gitleaks rows were produced by a re-run whose adapter locates the capture-group Secret inside the reported Match range only when the Match contains exactly one copy; with two or more copies, or for a finding that only exists in decoded content, the span keeps the reported range and is counted as unresolved instead of being moved to a copy of the value elsewhere in the document. ' + (f'{run_unresolved("gitleaks")} findings are stored as unresolved and are scored at that reported range, neither dropped nor treated as a false positive; the per-run counts and reasons are in the run inventory.' if run_unresolved('gitleaks') else '') + ' `detect-secrets` was re-run earlier and matched its stored predictions exactly. The other scanners keep stored predictions made before the correction; the rows that use them are marked `historical pre-fix` and can mix with corrected members in the same composition. See the [changelog](../CHANGELOG.md) and [reproduction](../docs/reproduce.md#scanner-adapter-status).', '']
    agg, train = ({}, {})
    jobs = int(os.environ.get('JOBS') or min(os.cpu_count() or 1, 8))
    if jobs > 1 and len(ALLSETS) > 1:
        with multiprocessing.Pool(min(jobs, len(ALLSETS))) as pool:
            for b, a, tr in pool.imap_unordered(per_set, ALLSETS):
                agg[b], train[b] = (a, tr)
    else:
        for b in ALLSETS:
            _, agg[b], train[b] = per_set(b)
    lines += scanner_table()
    lines += partial_table(agg)
    hot = [b for b in SETS if any(agg[b].values())]
    pii_hot = [b for b in PII if any(agg[b].values())]
    for b in hot:
        g = S.gold(b)[0]
        nspan = sum((len(v) for v in S.gold_norm(b).values()))
        nneg = sum((1 for rid in g if not g[rid][1]))
        lines += [f'## {b} ({len(g)} rows, {nspan} annotated spans, {nneg} rows without annotations)', '', '| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |', '|---|---|---|---|---|---|---|---|']
        for name, _, _ in OPTS:
            a = agg[b][name]
            status = composition_status(name, a['members'] if a else [])
            if not a:
                dash = 'train' if train[b][name] else '-'
                lines.append(f'| {name}{status} | ' + ' | '.join([dash] * 7) + ' |')
                continue
            over = S.pct(a['extra'], a['negchars'])
            lines.append(f"| {name}{mark(a)}{status} | {a['hit'] / a['nspan']:.3f} | **{a['miss']}** | {a['p']:.3f} | {a['r']:.3f} | {a['f1']:.3f} | {a['fire']}/{a['nneg']} | {a['extra']} ({over} of the text) |")
        lines += ['', '`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.', '']
    lines += ['## Every set: annotated spans nobody noticed at all', '', 'The number is spans not touched by a single character, the share of all spans of the set in brackets. `[k/N]` - only k of the N members of the composition have a run on that set: the cell is that partial composition. `-` - a vote with an incomplete composition, or nobody ran. `historical pre-fix` - the named composition includes a scanner with stored pre-correction predictions; the per-set tables above name the members that actually ran.', '', '| composition | ' + ' | '.join(ALLSETS) + ' |', '|---|' + '---|' * len(ALLSETS)]
    for name, _, _ in OPTS:
        status = composition_status(name)
        lines.append(f'| {name}{status} | ' + ' | '.join((('train' if train[b][name] else '-') if not agg[b][name] else f"{agg[b][name]['miss']} ({S.pct(agg[b][name]['miss'], agg[b][name]['nspan'])}){mark(agg[b][name])}" for b in ALLSETS)) + ' |')
    lines += ['', '## Every option in percent', '', 'One table per composition. **Untouched annotations** - entities not touched by a single character, as a share of all entities of the set; partially hidden entities are not counted as untouched and remain partly exposed. **Over-masked** and **unannotated rows touched** are pooled over every set that has rows without annotations. F1 is the char-level detection without type, median over the pii sets. Rows/s is over every set: detectors run one after another, so their times add up. `[k/N]` marks a set where only k of the N members have a run; the pooled columns to the right mix such sets in, so they describe the actually available members, not the full composition. `historical pre-fix` - the named composition includes a scanner with stored pre-correction predictions; the per-set tables above name the members that actually ran.', '', '| composition | ' + ' | '.join((f'untouched, {b}' for b in hot)) + ' | pii untouched, worst set | pii untouched, median | over-masked | unannotated rows touched | pii F1, median | rows/s |', '|---|' + '---|' * (len(hot) + 6)]
    rows = []
    for name, ms, k in OPTS:
        a = {b: agg[b][name] for b in ALLSETS}
        pii = [a[b]['miss'] / a[b]['nspan'] for b in PII if a[b]]
        extra = sum((a[b]['extra'] for b in ALLSETS if a[b]))
        negch = sum((a[b]['negchars'] for b in ALLSETS if a[b]))
        fire = sum((a[b]['fire'] for b in ALLSETS if a[b]))
        nneg = sum((a[b]['nneg'] for b in ALLSETS if a[b]))
        r = rate([m for m in ms if any(((S.RESULTS / b / f'pred.{m}.jsonl').exists() for b in ALLSETS))])
        cells = [S.pct(a[b]['miss'], a[b]['nspan']) + mark(a[b]) if a[b] else 'train' if train[b][name] else '-' for b in hot]
        cells += [f'{max(pii):.1%}' if pii else '-', f'{statistics.median(pii):.1%}' if pii else '-', S.pct(extra, negch), S.pct(fire, nneg), f"{statistics.median((a[b]['f1'] for b in PII if a[b])):.3f}" if pii else '-', f'{r:.1f}' if r else '-']
        rows.append((f'{name}{composition_status(name)}', cells))
    for name, cells in rows:
        lines.append(f'| {name} | ' + ' | '.join(cells) + ' |')
    lines.append('')
    (S.RESULTS / 'SECRETS.md').write_text('\n'.join(lines) + '\n')
    cols = [(i, 'secrets untouched', f'{b}, {sum((len(v) for v in S.gold_norm(b).values()))}', 'the annotation was not touched by a single character; partially hidden ones are not counted here and remain partly exposed') for i, b in enumerate(hot)]
    cols += [(len(hot), 'pii untouched', f'worst of {len(pii_hot)} sets', 'name, address, phone, id not touched by a single character'), (len(hot) + 2, 'over-masked', 'characters in unannotated rows', 'hidden where the source had no annotation: the model will not see this'), (len(hot) + 3, 'unannotated rows touched', 'rows without annotations', 'share of rows without entities where something was masked anyway'), (len(hot) + 5, 'speed', 'rows/s', 'the whole composition, one pass')]
    html(cols, rows, sum((len(S.gold(b)[0]) for b in ALLSETS)))
    print('\n'.join(lines))
if __name__ == '__main__':
    main()
