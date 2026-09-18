"""Scan the public projection with reviewed Gitleaks exceptions.

Each exception is bound to reviewed content instead of a bare position: the
rule plus the SHA-256 of every line that produces the finding. If the file's
content changes - even to another value the same rule fires on - the digest no
longer matches and the scan fails. Adding or relaxing an exception requires
editing this table and re-reviewing the new digest set.

The scan counts as evidence only when Gitleaks actually produced a well-formed
report: a missing or malformed report stops the gate instead of passing as a
clean result. Gitleaks' own skip channels are closed as well - an inline
`gitleaks:allow` comment cannot hide a finding (`--ignore-gitleaks-allow`), no
`.gitleaksignore` from the caller's directory applies (empty
`--gitleaks-ignore-path`), `GITLEAKS_CONFIG`/`GITLEAKS_CONFIG_TOML` are removed
from the environment, and a `.gitleaks.toml` inside the scanned tree is
refused - so the reviewed rule set cannot be replaced silently.

With --history <repo>, the same exception policy is applied to every finding
in the full Git history of the repository (R04): `gitleaks git` scans all
commits (--log-opts="--all"), and each finding is validated against the
content of the blob in the commit that produced it, not against the working
tree, so a reviewed test value that only exists in old commits is still
recognised and any new value fails the gate.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITLEAKS_VERSION = '8.30.1'
# Configuration channels that could replace the scanned rule set, in the
# precedence order of the pinned binary (v8.30.1 cmd/root.go: --config,
# GITLEAKS_CONFIG, GITLEAKS_CONFIG_TOML, a .gitleaks.toml inside the scanned
# path, then the built-in default).
ENV_CONFIG = ('GITLEAKS_CONFIG', 'GITLEAKS_CONFIG_TOML')
# file, rule -> (line digests for every allowed finding line, what the findings are)
ALLOWED = {
    # Two deterministic self-test fixtures for the Russian token rules: a
    # documented GitLab PAT example and the scanner's synthetic glpat value.
    ('benchmark/rules_ru.py', 'gitlab-pat'): (
     {'c910b0e1a4c48582c4c81a1853c529e6fe6a230c6b57c88dbefc5999120dba4c'},
     'rule self-test tokens in rules_ru.py'),
    # Generic-api-key firing on 64-hex SHA-256 digests inside the provenance
    # manifest (hashes of public modules, not credentials). Line numbers move
    # whenever the manifest is edited, so each finding line is validated
    # against the exact reviewed form `"module.py": "<64 hex>",` instead of a
    # fixed position; any other content still fails the scan. The key must be
    # an actual module of this repository whose recorded hash matches the
    # module's bytes (R05).
    ('benchmark/PROVENANCE.json', 'generic-api-key'): ('manifest-digest-line',
     'module sha256 digest lines in PROVENANCE.json'),
    # Same rule firing on source-hash entries inside the snapshot `sources`
    # map (R05, T02): a firing line must name a reviewed artifact of the run
    # layout - a report or prediction of a dataset in the published catalog,
    # carrying the digest of that run in the run inventory, or one of the
    # reviewed aggregate reports. A digest line for a path outside that
    # layout - `RESULTS/unknown/pred.demo.jsonl` - is not an exception,
    # whatever its shape, and the exception never rests on the scanned file's
    # own contents.
    ('results/snapshot.json', 'generic-api-key'): ('snapshot-sources-line',
     'source file sha256 entries in snapshot.json sources'),
    # The capture-collision self-test fixture (T01): a Secret value repeated
    # inside its Match, written as an explicit token in the self-test.
    ('benchmark/selftest.py', 'generic-api-key'): (
     {'9805a262022994c4171cd868d0d808ff0ee493705e0ce73e23e141481794d22f'},
     'capture-collision fixture token in selftest.py'),
    # The inline allow-comment gate test (T02): a synthetic hex api key that
    # the release gate must still report despite its own gitleaks:allow
    # comment. Synthetic fixture value, not a credential.
    ('tests/test_scan_gate.py', 'generic-api-key'): (
     {'8d58bd91007eca7c97d8956bca72c5f64e3cf7934668215d5bdd9bca7b2fca13'},
     'inline allow-comment gate fixture in test_scan_gate.py'),
}
# R05: the manifest exception only covers `public_module_sha256` entries, and
# only for real modules; any other key - a stray api_key field with a valid
# SHA-256 shape - is rejected by the validator below.
_MANIFEST_LINE = re.compile(r'\s*"public_module_sha256": \{\s*')
_MODULE_LINE = re.compile(r'\s*"([A-Za-z0-9_.-]+)": "([0-9a-f]{64})",?\s*')
_SOURCES_LINE = re.compile(r'\s*"RESULTS/([A-Za-z0-9_.-]+)/(pred\.[A-Za-z0-9_.+-]+\.jsonl|REPORT\.md)": "([0-9a-f]{64})",?\s*')
_AGGREGATE_LINE = re.compile(r'\s*"RESULTS/([A-Z]+\.md)": "([0-9a-f]{64})",?\s*')
# Aggregate report files of the run layout: the only non-dataset source keys.
AGGREGATE_REPORTS = ('REPORT.md', 'ENSEMBLE.md', 'SPEED.md', 'SECRETS.md', 'VERDICT.md')
# A finding without these fields cannot be reviewed at all, so the gate would
# be passing an entry it never saw.
FINDING_FIELDS = (('File', str), ('RuleID', str), ('StartLine', int))


def line_digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def manifest_line_ok(text, module_bytes):
    """A PROVENANCE.json finding line is allowed only when it is a
    public_module_sha256 entry for a real module whose recorded hash matches
    that module's bytes (R05). `module_bytes(name)` resolves the module in
    the content source being validated: the working tree for the projection
    scan, the scanned commit for the history scan."""
    if _MANIFEST_LINE.fullmatch(text):
        return True
    m = _MODULE_LINE.fullmatch(text)
    if not m:
        return False
    data = module_bytes(m.group(1))
    return data is not None and hashlib.sha256(data).hexdigest() == m.group(2)


def source_line_ok(text, context):
    """A snapshot `sources` finding line is allowed only when it names a
    reviewed artifact of the run layout (T02): a report or prediction of a
    published dataset, bound to the digest the run inventory records for that
    run, or one of the reviewed aggregate reports. A well-formed digest line
    for any other path - `RESULTS/unknown/pred.demo.jsonl` - stays a finding,
    whatever its shape, so the exception rests on the publication's own
    catalog and inventory instead of on a 64-hex pattern."""
    m = _SOURCES_LINE.fullmatch(text)
    if m:
        dataset, name, digest = (m.group(1), m.group(2), m.group(3))
        if dataset not in context['datasets']:
            return False
        # A prediction digest must be the one the run inventory records for
        # that run; a dataset report has no run record and is bound to the
        # published catalog only.
        return True if name == 'REPORT.md' else context['runs'].get((dataset, name)) == digest
    m = _AGGREGATE_LINE.fullmatch(text)
    return bool(m) and m.group(1) in AGGREGATE_REPORTS


def validate(key, text, module_bytes, context):
    digests, _ = ALLOWED.get(key, (set(), 'not reviewed'))
    if digests == 'manifest-digest-line':
        return manifest_line_ok(text, module_bytes)
    if digests == 'snapshot-sources-line':
        return source_line_ok(text, context)
    return line_digest(text) in digests


def reviewed_context(snapshot_text, catalog_text, inventory_text):
    """The reviewed context of a snapshot exception (T02): the published
    datasets, the runs the inventory records with their digests, and the
    aggregate reports. Missing or unreadable evidence leaves the exception
    nothing to bind to, so every line fails closed."""
    try:
        snapshot = json.loads(snapshot_text or '')
    except ValueError:
        snapshot = {}
    sources = snapshot.get('sources') if isinstance(snapshot, dict) else None
    sources = sources if isinstance(sources, dict) else {}

    def records(text):
        try:
            data = json.loads(text or '')
        except ValueError:
            return []
        return data if isinstance(data, list) else []

    datasets = {str(r['id']) for r in records(catalog_text) if isinstance(r, dict) and 'id' in r}
    runs = {(r['dataset'], r['file']): r.get('pred_sha256') for r in records(inventory_text)
            if isinstance(r, dict) and isinstance(r.get('dataset'), str) and isinstance(r.get('file'), str)}
    return {'datasets': datasets, 'runs': runs,
            'sources': {str(k)[len('RESULTS/'):]: v for k, v in sources.items() if str(k).startswith('RESULTS/')}}


def gitleaks_env():
    return {name: value for name, value in os.environ.items() if name not in ENV_CONFIG}


def gitleaks_version():
    """The pinned binary is part of the evidence: both entry points check it."""
    try:
        version = subprocess.run(['gitleaks', 'version'], check=True, text=True,
                                 capture_output=True, env=gitleaks_env()).stdout.strip()
    except (OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(f'Gitleaks {GITLEAKS_VERSION} required on PATH: {error}')
    if version != GITLEAKS_VERSION:
        raise SystemExit(f'Gitleaks {GITLEAKS_VERSION} required, found {version!r}')
    return version


def run_scan(scope, source, report, history=False):
    """Run the pinned binary with every caller-controlled skip channel closed,
    then read its report. An absent or malformed report is a failed scan, not
    a clean tree (T02)."""
    with tempfile.TemporaryDirectory() as ignore_dir:
        subprocess.run([
            'gitleaks', scope, str(source), '--no-banner', '--redact',
            '--report-format', 'json', '--report-path', str(report), '--exit-code', '0',
            '--ignore-gitleaks-allow', '--gitleaks-ignore-path', ignore_dir
        ] + (['--log-opts=--all'] if history else []),
            check=True, env=gitleaks_env())
    if not report.exists():
        raise SystemExit(f'Gitleaks wrote no report at {report}: absence of a report is not '
                         f'evidence of a clean tree.')
    try:
        findings = json.loads(report.read_text() or 'null')
    except ValueError as error:
        raise SystemExit(f'The Gitleaks report at {report} is not valid JSON: {error}')
    if not isinstance(findings, list):
        raise SystemExit(f'The Gitleaks report at {report} is not a list of findings')
    fields = FINDING_FIELDS + ((('Commit', str),) if history else ())
    for row in findings:
        for name, kind in fields:
            value = row.get(name) if isinstance(row, dict) else None
            if isinstance(value, bool) or not isinstance(value, kind) or (kind is int and value < 1):
                raise SystemExit(f'The Gitleaks report at {report} has a finding without a usable '
                                 f'{name}: {row!r:.200}')
    return findings


def projection_scan():
    gitleaks_version()
    names = subprocess.check_output(
        ['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
        cwd=ROOT).decode().split('\0')
    names = [n for n in names if n]
    with tempfile.TemporaryDirectory() as directory:
        public = Path(directory) / 'public'
        public.mkdir()
        for name in names:
            # A .gitleaks.toml inside the scanned path becomes the rule set
            # (v8.30.1 cmd/root.go); the reviewed public tree must not carry one.
            assert not Path(name).name.startswith('.gitleaks'), f'Scanned tree carries {name}'
            source = ROOT / name
            if source.is_file():
                target = public / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        findings = run_scan('dir', public, Path(directory) / 'gitleaks.json')
        observed = defaultdict(list)
        for row in findings:
            key = (str(Path(row['File']).relative_to(public)), row['RuleID'])
            observed[key].append(row['StartLine'])

    def module_bytes(name):
        p = ROOT / 'benchmark' / name
        return p.read_bytes() if p.is_file() else None

    context = reviewed_context((ROOT / 'results/snapshot.json').read_text(),
                               (ROOT / 'datasets/catalog.json').read_text(),
                               (ROOT / 'results/run-inventory.json').read_text())
    errors = []
    for key in sorted(set(observed) | set(ALLOWED)):
        lines = sorted(set(observed.get(key, [])))
        if key not in ALLOWED:
            errors.append(f'unexpected findings: {key} at lines {lines}')
            continue
        for line in lines:
            if line is None:
                continue
            content = (ROOT / key[0]).read_text().splitlines()
            text = content[line - 1] if 0 < line <= len(content) else ''
            if not validate(key, text, module_bytes, context):
                errors.append(f'finding on unreviewed content: {key[0]}:{line} ({ALLOWED[key][1]}); re-review before allowlisting')
    return findings, errors


def history_scan(repo):
    """Apply the same exception policy to the full Git history (R04).

    Each history finding is checked against the content of its file at the
    commit gitleaks attributes it to. The current working tree is never used
    as evidence for a history finding.
    """
    gitleaks_version()
    if subprocess.run(['git', 'rev-parse', '--is-shallow-repository'],
                      cwd=repo, check=True, text=True,
                      capture_output=True).stdout.strip() == 'true':
        raise SystemExit('History scan requires the full history; the repository is shallow.')
    with tempfile.TemporaryDirectory() as directory:
        findings = run_scan('git', repo, Path(directory) / 'history.json', history=True)

    def blob(commit, path):
        content = subprocess.run(['git', 'show', f'{commit}:{path}'], cwd=repo,
                                 text=True, capture_output=True)
        return content.stdout.splitlines() if content.returncode == 0 else []

    def raw(commit, path):
        content = subprocess.run(['git', 'show', f'{commit}:{path}'], cwd=repo,
                                 capture_output=True)
        return content.stdout if content.returncode == 0 else None

    caches = {}

    def cached(store, commit, path, load):
        return store.setdefault((commit, path), load())

    errors = []
    for row in findings:
        key = (row['File'], row['RuleID'])
        if key not in ALLOWED:
            errors.append(f"unexpected history findings: {key[0]}:{row['RuleID']} at {row['Commit'][:12]}:{row['StartLine']}")
            continue
        lines = cached(caches.setdefault('blob', {}), row['Commit'], row['File'], lambda: blob(row['Commit'], row['File']))
        line = row['StartLine']
        text = lines[line - 1] if 0 < line <= len(lines) else ''
        module_bytes = lambda name, commit=row['Commit']: cached(  # noqa: E731
            caches.setdefault('module', {}), commit, name, lambda: raw(commit, f'benchmark/{name}'))

        def committed(path, commit=row['Commit']):
            return cached(caches.setdefault('file', {}), commit, path,
                          lambda: (raw(commit, path) or b'').decode('utf-8', 'replace'))

        context = cached(caches.setdefault('context', {}), row['Commit'], 'reviewed',
                         lambda: reviewed_context(committed('results/snapshot.json'),
                                                  committed('datasets/catalog.json'),
                                                  committed('results/run-inventory.json')))
        if not validate(key, text, module_bytes, context):
            errors.append(f'history finding on unreviewed content: {row["File"]}:{line} at {row["Commit"][:12]} ({ALLOWED[key][1]}); re-review before allowlisting')
    return findings, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--history', type=Path, metavar='REPO',
                        help='scan the full Git history of REPO with the same exception policy')
    args = parser.parse_args()
    findings, errors = history_scan(args.history) if args.history else projection_scan()
    if errors:
        raise SystemExit('Gitleaks exceptions changed:\n  ' + '\n  '.join(errors))
    scope = 'candidate history' if args.history else 'public projection'
    print(f'Gitleaks {GITLEAKS_VERSION} ({scope}): {len(findings)} reviewed findings, content digests verified, no unexpected findings.')


if __name__ == '__main__':
    main()
