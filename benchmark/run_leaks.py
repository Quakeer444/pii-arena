import bisect, csv, json, os, re, shlex, shutil, subprocess, sys, tempfile, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from benchlib import PROTOCOL, bench_sha256, machine
ROOT = Path(os.environ.get('BENCHMARK_DATA', str(Path(__file__).resolve().parent.parent / '.local' / 'research'))).resolve()
RESULTS = Path(os.environ.get('OUT') or ROOT / 'RESULTS')
csv.field_size_limit(10 ** 7)
REPO = {'gitleaks': 'github.com/gitleaks/gitleaks', 'betterleaks': 'github.com/betterleaks/betterleaks', 'trufflehog': 'github.com/trufflesecurity/trufflehog', 'detect-secrets': 'github.com/Yelp/detect-secrets', 'noseyparker': 'github.com/praetorian-inc/noseyparker', 'kingfisher': 'github.com/mongodb/kingfisher', 'credsweeper': 'github.com/Samsung/CredSweeper', 'deepsecrets': 'github.com/ntoskernel/deepsecrets', 'credsweeper-noml': 'github.com/Samsung/CredSweeper', 'titus': 'github.com/praetorian-inc/titus'}
LINE_ONLY = ('trufflehog', 'detect-secrets')
OK_CODES = {'kingfisher': {0, 200, 205}}
# Sixth element of a finding tuple: the reason the scanner range is the only
# evidence for this finding and the exact secret range inside it is unknown
# (T01). spans_of keeps the reported range and marks the span resolved=False
# with that reason instead of searching the text for a copy of the secret.
#   'decoded'           - Match/Secret live in decoded content, the columns
#                         describe the encoded segment of the source file.
#   'capture-collision' - the Secret occurs zero or several times inside the
#                         reported Match, so the capture it came from is not
#                         recoverable from the report.
#   'native'            - the report carries no usable columns at all.
NATIVE = 'native'
UNRESOLVED = ('decoded', 'capture-collision', NATIVE)
# Span-mapping policy of this adapter. Every run made from here records it as
# `adapter_policy` in the prediction metadata, so a machine-readable consumer
# can tell which mapping produced a given run (T05) instead of reading it out
# of Markdown prose. Bump it when the mapping changes: 'capture-v1' resolved a
# capture-group Secret by first substring hit inside the Match,
# 'capture-v2' (2026-09-18) locates it only when the Match holds exactly one
# copy, keeps the reported range and marks it unresolved otherwise, treats
# decoded findings as encoded-segment ranges, and inverts the newline-relative
# column convention of the pinned binary.
ADAPTER_POLICY = 'capture-v2'
# Release status of the stored scanner predictions, per scanner: the policy
# recorded in the stored runs ('' when the runs predate policy recording) and
# the reviewed status. 'corrected-rerun': re-run at the recorded version with
# the fixed adapter, stored predictions replaced. 'verified-unchanged': re-run
# at the recorded version matched the stored predictions exactly.
# 'historical-pre-fix': stored predictions predate the fix and no re-run at
# the recorded revision is available (missing binary, or the unpinned fallback
# resolves to a newer version that differs).
ADAPTER_STATUS = {
    'gitleaks': (ADAPTER_POLICY, 'corrected-rerun'),
    'detect-secrets': ('', 'verified-unchanged'),
    'betterleaks': ('', 'historical-pre-fix'),
    'trufflehog': ('', 'historical-pre-fix'),
    'noseyparker': ('', 'historical-pre-fix'),
    'titus': ('', 'historical-pre-fix'),
    'kingfisher': ('', 'historical-pre-fix'),
    'credsweeper': ('', 'historical-pre-fix'),
    'credsweeper-noml': ('', 'historical-pre-fix'),
    'deepsecrets': ('', 'historical-pre-fix'),
}
STATUS_VALUES = ('corrected-rerun', 'verified-unchanged', 'historical-pre-fix')

def adapter_status(tool):
    return ADAPTER_STATUS.get(tool, ('', 'not-reviewed'))[1]

def adapter_policy(tool):
    return ADAPTER_STATUS.get(tool, ('', 'not-reviewed'))[0]

def bin_of(tool, default=None):
    v = os.environ.get(tool.upper().replace('-', '_') + '_BIN')
    return shlex.split(v) if v else list(default) if default else [tool]

def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

def need(tool, ps, by):
    ok = OK_CODES.get(tool, {0})
    bad = [p for p in ps if p.returncode not in ok]
    if bad:
        out = ((bad[0].stderr or '') + (bad[0].stdout or ''))[-2000:]
        sys.exit(f'{tool}: exit code {bad[0].returncode} (allowed {sorted(ok)}), parsed findings {sum((len(v) for v in by.values()))} - run failed\n{out}')
    return by

def report_of(tool, path, p):
    if not Path(path).exists():
        out = ((p.stderr or '') + (p.stdout or ''))[-2000:]
        sys.exit(f'{tool}: report {path} not created (exit code {p.returncode})\n{out}')
    return json.loads(Path(path).read_text() or 'null')

def ver_of(cmd):
    p = sh(cmd)
    return ((p.stdout or '') + (p.stderr or '')).strip().splitlines()[0] if p.stdout or p.stderr else '?'

def gitleaks_item(data, f):
    """Normalize one Gitleaks finding to the character-column protocol of
    spans_of (R01, T01).

    Gitleaks 8.30.1 reports 1-based line numbers and byte columns for the full
    regex Match (v8.30.1 detect/location.go), while `Secret` is the capture
    group when the rule sets `secretGroup` (v8.30.1 detect/detect.go:525).
    Three properties of that report are handled here, all measured against the
    pinned binary:

    * Columns are counted from the preceding newline character, not from the
      line start, so line 1 is exact and every later line is one column high.
      The byte offset is therefore rebuilt as `newline byte + column`, which
      reproduces the Match position for both cases.
    * Columns are UTF-8 bytes, so they are converted to character offsets; a
      byte column used as a character index selects a wrong duplicate after
      any multi-byte text.
    * The columns describe the Match, not the capture-group Secret.

    A finding whose `Tags` name a decoding pass (`decoded:base64`,
    `decode-depth:N`) has Match/Secret in decoded text while the columns
    describe the encoded segment in the source file: the encoded range is then
    the only evidence and the plaintext position is unknown, so the reported
    range is kept and marked NATIVE. Otherwise the Match range is rebuilt and
    checked against the reported Match text; when the reported range does not
    contain the Match (a match running to the end of the fragment gets no end
    column, and a multi-line match reports its end relative to its last line),
    the extent is taken from the Match text itself. Secret is accepted as the
    capture only when exactly one copy lies inside that range: with two or more
    copies, or none, the capture position is not recoverable from the report,
    so the Match range is kept and marked NATIVE instead of picking the first
    or last hit.
    """
    data = bytes(data)
    text = data.decode('utf-8')
    sl, sc, el, ec = (f.get('StartLine'), f.get('StartColumn'), f.get('EndLine'), f.get('EndColumn'))
    match = f.get('Match') or ''
    sec = f.get('Secret') or match or None
    if not all(isinstance(v, int) and not isinstance(v, bool) for v in (sl, sc, el, ec)):
        return (sec, sl, None, el, None, NATIVE)
    bstarts = [0] + [m.end() for m in re.finditer(b'\n', data)]

    def offset(line, col):
        line = min(max(line, 1), len(bstarts))
        base = bstarts[line - 1] - (1 if line > 1 else 0)
        return len(data[:min(max(base, 0) + max(col, 0), len(data))].decode('utf-8'))

    a, b = (offset(sl, sc - 1), offset(el, ec))
    starts = [0] + [m.end() for m in re.finditer('\n', text)]
    sli = min(bisect.bisect_right(starts, a), len(starts))
    eli = min(max(bisect.bisect_right(starts, max(b - 1, a)), sli), len(starts))
    decoded = any(str(t).startswith('decoded') for t in f.get('Tags') or ())
    if decoded:
        # The columns describe the encoded segment of the source file, not the
        # plaintext position: that range is the whole evidence, with or
        # without a recoverable Secret.
        return (sec, sli, a - starts[sli - 1] + 1, eli, b - starts[eli - 1], 'decoded')
    if text[a:b] != match and match and text[a:a + len(match)] == match:
        b = a + len(match)
    ambiguous = bool(sec) and sec != text[a:b]
    reason = NATIVE
    if ambiguous:
        hits, i = ([], text.find(sec, a, b))
        while i >= 0 and len(hits) < 2:
            hits.append(i)
            i = text.find(sec, i + 1, b)
        if len(hits) == 1:
            a, b, ambiguous = (hits[0], hits[0] + len(sec), False)
        else:
            reason = 'capture-collision'
    if not sec:
        ambiguous = False
    sli = min(bisect.bisect_right(starts, a), len(starts))
    eli = min(max(bisect.bisect_right(starts, max(b - 1, a)), sli), len(starts))
    item = (sec, sli, a - starts[sli - 1] + 1, eli, b - starts[eli - 1])
    return item + (reason,) if ambiguous else item

def scan_gitleaks(d, tool='gitleaks'):
    rep = Path(d).parent / f'{tool}.json'
    cmd = bin_of(tool) + ['dir', str(d), '-f', 'json', '-r', str(rep), '--no-banner', '--exit-code', '0']
    depth = os.environ.get('GITLEAKS_DECODE')
    if depth:
        cmd += ['--max-decode-depth', depth]
    p = sh(cmd)
    by, raw = ({}, {})
    for f in report_of(tool, rep, p) or []:
        path = Path(f['File'])
        if path not in raw:
            resolved = path if path.is_absolute() else Path(d) / path
            raw[path] = resolved.read_bytes()
        by.setdefault(int(path.stem), []).append(gitleaks_item(raw[path], f))
    return (need(tool, [p], by), ver_of(bin_of(tool) + ['version']))

def scan_betterleaks(d):
    return scan_gitleaks(d, 'betterleaks')

def scan_trufflehog(d):
    p = sh(bin_of('trufflehog') + ['filesystem', str(d), '--no-verification', '--json'])
    by = {}
    for line in p.stdout.splitlines():
        if not line.startswith('{'):
            continue
        fs = (json.loads(line).get('SourceMetadata') or {}).get('Data', {}).get('Filesystem') or {}
        if 'file' not in fs:
            continue
        ln = int(fs.get('line', 1))
        by.setdefault(int(Path(fs['file']).stem), []).append((json.loads(line).get('Raw') or None, ln, None, ln, None))
    return (need('trufflehog', [p], by), ver_of(bin_of('trufflehog') + ['--version']))

def scan_detect_secrets(d):
    p = sh(bin_of('detect-secrets') + ['scan', '.', '--all-files'], cwd=str(d))
    by = {}
    for path, items in (json.loads(p.stdout or '{}').get('results') or {}).items():
        for it in items:
            ln = int(it['line_number'])
            by.setdefault(int(Path(path).stem), []).append((None, ln, None, ln, None))
    return (need('detect-secrets', [p], by), ver_of(bin_of('detect-secrets') + ['--version']))

def scan_noseyparker(d):
    ds = Path(d).parent / 'np.datastore'
    shutil.rmtree(ds, ignore_errors=True)
    ps = sh(bin_of('noseyparker') + ['scan', '--datastore', str(ds), str(d)])
    p = sh(bin_of('noseyparker') + ['report', '--datastore', str(ds), '--format', 'json'])
    by = {}
    for fnd in json.loads(p.stdout or '[]') or []:
        for m in fnd.get('matches', []):
            path = (m.get('provenance') or [{}])[0].get('path')
            ss = m['location']['source_span']
            by.setdefault(int(Path(path).stem), []).append(((m.get('snippet') or {}).get('matching') or None, ss['start']['line'], ss['start']['column'], ss['end']['line'], ss['end']['column'] + 1))
    return (need('noseyparker', [ps, p], by), ver_of(bin_of('noseyparker') + ['--version']))

def scan_titus(d):
    ds = Path(d).parent / 'titus.ds'
    shutil.rmtree(ds, ignore_errors=True)
    ps = sh(bin_of('titus') + ['scan', str(d), '--output', str(ds), '--ruleset', 'all', '--format', 'human'])
    p = sh(bin_of('titus') + ['report', '--datastore', str(ds), '--format', 'json'])
    by = {}
    for fnd in json.loads(p.stdout or '[]') or []:
        for m in fnd.get('Matches', []):
            path = Path(m['file_path'])
            o, src = (m['Location']['Offset'], m['Location']['Source'])
            sec = path.read_bytes()[o['Start']:o['End']].decode('utf-8', 'replace')
            by.setdefault(int(path.stem), []).append((sec or None, src['Start']['Line'], src['Start']['Column'], src['End']['Line'], src['End']['Column'] + 1))
    return (need('titus', [ps, p], by), ver_of(bin_of('titus') + ['version']).strip() or '?')

def scan_kingfisher(d):
    conf = os.environ.get('KINGFISHER_CONFIDENCE', 'low')
    p = sh(bin_of('kingfisher') + ['scan', str(d), '--format', 'json', '--no-validate', '--confidence', conf])
    by = {}
    for line in p.stdout.splitlines():
        if not line.startswith('{'):
            continue
        o = json.loads(line)
        for f in o.get('findings') if isinstance(o.get('findings'), list) else []:
            fi = f['finding']
            ln = int(fi.get('line', 1))
            by.setdefault(int(Path(fi['path']).stem), []).append((fi.get('snippet') or None, ln, int(fi.get('column_start', 0)) + 1, ln, int(fi.get('column_end', 0)) + 1))
    return (need('kingfisher', [p], by), ver_of(bin_of('kingfisher') + ['--version']))

def scan_credsweeper(d, ml=True):
    base = bin_of('credsweeper', ['uv', 'run', '--quiet', '--with', 'credsweeper', 'python', '-m', 'credsweeper'])
    out = Path(d).parent / 'credsweeper.json'
    p = sh(base + ['--path', str(d), '--save-json', str(out)] + ([] if ml else ['--ml_threshold', '0']))
    by = {}
    for cred in report_of('credsweeper', out, p) or []:
        for ld in cred.get('line_data_list', []):
            ln, a, b = (int(ld['line_num']), ld.get('value_start'), ld.get('value_end'))
            by.setdefault(int(Path(ld['path']).stem), []).append((ld.get('value') or None, ln, a + 1 if isinstance(a, int) and a >= 0 else None, ln, b if isinstance(b, int) and b >= 0 else None))
    return (need('credsweeper', [p], by), ver_of(base + ['--version']))

def scan_credsweeper_noml(d):
    return scan_credsweeper(d, ml=False)

def scan_deepsecrets(d):
    base = bin_of('deepsecrets', ['uv', 'run', '--quiet', '--with', 'deepsecrets', 'deepsecrets'])
    out = Path(d).parent / 'deepsecrets.json'
    p = sh(base + ['--target-dir', str(d), '--outfile', str(out)])
    run = ((report_of('deepsecrets', out, p) or {}).get('runs') or [{}])[0]
    by = {}
    for r in run.get('results', []):
        for loc in r.get('locations', []):
            pl = loc['physicalLocation']
            reg = pl['region']
            by.setdefault(int(Path(pl['artifactLocation']['uri']).stem), []).append((None, reg.get('startLine'), reg.get('startColumn'), reg.get('endLine'), reg.get('endColumn')))
    return (need('deepsecrets', [p], by), run.get('tool', {}).get('driver', {}).get('semanticVersion', '?'))
TOOLS = {'gitleaks': scan_gitleaks, 'betterleaks': scan_betterleaks, 'trufflehog': scan_trufflehog, 'detect-secrets': scan_detect_secrets, 'noseyparker': scan_noseyparker, 'titus': scan_titus, 'kingfisher': scan_kingfisher, 'credsweeper': scan_credsweeper, 'credsweeper-noml': scan_credsweeper_noml, 'deepsecrets': scan_deepsecrets}

def scan(tool, texts):
    with tempfile.TemporaryDirectory() as d:
        din = Path(d) / 'in'
        din.mkdir()
        for i, t in enumerate(texts):
            (din / f'{i}.txt').write_text(t)
        t0 = time.perf_counter()
        started_utc = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        by, ver = TOOLS[tool](str(din))
        el = time.perf_counter() - t0
        return (by, ver, el, started_utc)

def spans_of(text, findings):
    """Map scanner findings to Python character offsets in the source text.

    A finding is `(secret, start line, start column, end line, end column)`
    with an optional sixth element from `UNRESOLVED`, meaning the adapter could
    not locate the secret inside the scanner range and that range is the only
    evidence. Such a finding keeps the reported range and is stored as
    `unresolved: true` with that reason (`unresolved_reason`): a copy of the
    secret somewhere else in the document is not evidence of where the scanner
    found it.

    Otherwise the scanner's native line/column position is the primary
    evidence: a repeated secret value must stay on the occurrence the scanner
    reported, not on the first `text.find` hit. Columns are already normalized
    per scanner by the adapters above; they may still be byte-based, so a
    native position is only trusted after the text at that position matches
    the reported secret. When it does not, the secret is searched inside the
    reported line range, then globally only if it occurs exactly once.
    Otherwise the finding is kept at its native position and marked
    `unresolved` instead of guessing.
    """
    lines, starts, off = (text.split('\n'), [], 0)
    for ln in lines:
        starts.append(off)
        off += len(ln) + 1
    out = []
    for finding in sorted(findings, key=lambda f: (f[1] or 0, f[2] or 0)):
        sec, sl, sc, el, ec = finding[:5]
        marker = finding[5] if len(finding) > 5 and finding[5] in UNRESOLVED else None
        a = b = -1
        reason = marker
        sli = min(max(sl or 1, 1), len(starts))
        eli = min(max(el or sl or 1, 1), len(starts))
        if marker:
            a = starts[sli - 1] + max((sc or 1) - 1, 0)
            b = starts[eli - 1] + (ec if ec else len(lines[eli - 1]))
        elif sec:
            na = starts[sli - 1] + max((sc or 1) - 1, 0)
            if 0 <= na and text[na:na + len(sec)] == sec:
                a, b = (na, na + len(sec))
            else:
                lo, hi = (starts[sli - 1], starts[eli - 1] + len(lines[eli - 1]))
                i = text.find(sec, lo, hi)
                if i >= 0 and text.find(sec, i + 1, hi) < 0:
                    a, b = (i, i + len(sec))
                elif text.count(sec) == 1:
                    a, b = (text.find(sec), text.find(sec) + len(sec))
                else:
                    a, b = (na, starts[eli - 1] + (ec if ec else len(lines[eli - 1])))
                    reason = reason or NATIVE
        else:
            a = starts[sli - 1] + max((sc or 1) - 1, 0)
            b = starts[eli - 1] + (ec if ec else len(lines[eli - 1]))
        span = {'start': max(a, 0), 'end': min(max(b, a + 1), len(text)), 'label': 'secret'}
        if reason:
            span['unresolved'] = True
            span['unresolved_reason'] = reason
        out.append(span)
    # Canonical order: the adapter's internal decisions (narrowing a capture,
    # keeping a reported range) must not reorder the stored spans.
    out.sort(key=lambda s: (s['start'], s['end']))
    return out

def main(tool, *benches):
    if tool not in TOOLS:
        sys.exit(f"unknown scanner {tool}; available: {', '.join(TOOLS)}")
    for bench in benches or sorted((d.name for d in (ROOT / 'BENCH').iterdir() if (d / 'bench.csv').exists())):
        rows = list(csv.DictReader((ROOT / 'BENCH' / bench / 'bench.csv').open(newline='')))
        if not rows:
            print(f'{tool}/{bench}: empty bench.csv; skipped')
            continue
        by, ver, el, started_utc = scan(tool, [r['text'] for r in rows])
        ms = round(el / max(len(rows), 1) * 1000, 2)
        out = RESULTS / bench / f'pred.{tool}.jsonl'
        out.parent.mkdir(parents=True, exist_ok=True)
        sha = bench_sha256(ROOT / 'BENCH' / bench / 'bench.csv')
        meta = {'name': tool, 'repo': REPO.get(tool, tool), 'revision': ver, 'family': 'leaks', 'protocol': PROTOCOL, 'bench': bench, 'bench_sha256': sha, 'device': 'cpu', **machine(), 'rows': len(rows), 'chars': sum((len(r['text']) for r in rows)), 'elapsed_s': round(el, 1), 'rows_per_s': round(len(rows) / el, 1), 'errors': 0, 'granularity': 'line' if tool in LINE_ONLY else 'span', 'started_utc': started_utc, 'finished_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'adapter_policy': ADAPTER_POLICY}
        if tool in ('gitleaks', 'betterleaks'):
            # Gitleaks 8.30.1 decodes recursively up to depth 5 by default;
            # record the effective depth, not the absence of an override.
            meta['decode_depth'] = int(os.environ.get('GITLEAKS_DECODE', 5))
        if tool == 'kingfisher':
            meta['confidence'] = os.environ.get('KINGFISHER_CONFIDENCE', 'low')
        if tool.startswith('credsweeper'):
            meta['ml'] = tool == 'credsweeper'
        spans_by_row = {i: spans_of(r['text'], by.get(i, [])) for i, r in enumerate(rows)}
        unresolved = [s for v in spans_by_row.values() for s in v if s.get('unresolved')]
        if unresolved:
            meta['unresolved_spans'] = len(unresolved)
            # T05: the reason is part of the public picture, not only the
            # count - a decoded finding and an unplaceable capture need
            # different reading, and neither is a proven false positive.
            reasons = {}
            for span in unresolved:
                key = span.get('unresolved_reason', NATIVE)
                reasons[key] = reasons.get(key, 0) + 1
            meta['unresolved_reasons'] = dict(sorted(reasons.items()))
        with out.open('w') as fh:
            fh.write(json.dumps({'meta': meta}, ensure_ascii=False) + '\n')
            for i, r in enumerate(rows):
                fh.write(json.dumps({'id': r['id'], 'spans': spans_by_row[i], 'ms': ms, 'err': None}, ensure_ascii=False) + '\n')
        print(f'{tool} {ver}/{bench}: {len(rows)} rows, findings {sum((len(v) for v in by.values()))}, {el:.1f}s -> {out}')
if __name__ == '__main__':
    main(*sys.argv[1:])
