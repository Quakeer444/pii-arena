"""T02: absence of evidence must not pass as evidence of a clean tree.

The release gate runs the pinned binary and reads its report. These checks
drive the gate's own contract with a substituted process: a valid empty report
passes, a missing or malformed report stops the gate, the command line closes
Gitleaks' own skip channels, both entry points check the binary version, and a
snapshot exception has to name a reviewed artifact of the run layout.
"""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import scan_secrets as G

HEX = hashlib.sha256(b'reviewed').hexdigest()
CALLS = []


class FakeRun:
    """Replacement for subprocess.run that writes a chosen report and records
    the command line the gate used."""

    def __init__(self, report, stdout=''):
        self.report, self.stdout = report, stdout

    def __call__(self, cmd, **kw):
        CALLS.append((list(cmd), dict(kw.get('env') or {})))
        if self.report is not None and cmd[0] == 'gitleaks' and '--report-path' in cmd:
            Path(cmd[cmd.index('--report-path') + 1]).write_text(self.report)
        return subprocess.CompletedProcess(cmd, 0, stdout=self.stdout, stderr='')


def run_gate(report, scope='dir', history=False):
    with tempfile.TemporaryDirectory() as d:
        real, G.subprocess.run = G.subprocess.run, FakeRun(report)
        try:
            return G.run_scan(scope, d, Path(d) / 'report.json', history=history)
        finally:
            G.subprocess.run = real


# A report the gate could not read is a failed scan, not a clean tree: the
# process may exit 0 without producing anything.
for absent in (None, '', 'not json at all', '{"findings": []}', '[{"File": 1}]',
               '[{"File": "a", "RuleID": "r"}]', '[{"File": "a", "RuleID": "r", "StartLine": 0}]'):
    try:
        run_gate(absent)
    except SystemExit as error:
        assert 'absence of a report' in str(error) or 'report' in str(error), error
    else:
        raise AssertionError(f'Unreadable report accepted: {absent!r}')

# A correctly shaped empty report is a legitimate result: nothing found.
assert run_gate('[]') == []
assert run_gate('[{"File": "a.py", "RuleID": "generic-api-key", "StartLine": 3}]')[0]['RuleID'] == 'generic-api-key'
# History findings must identify the commit they came from; a report without
# it cannot be validated against the scanned revision.
assert run_gate('[{"File": "a.py", "RuleID": "r", "StartLine": 1, "Commit": "%s"}]' % ('0' * 40), 'git', history=True)
try:
    run_gate('[{"File": "a.py", "RuleID": "r", "StartLine": 1}]', 'git', history=True)
except SystemExit as error:
    assert 'Commit' in str(error), error
else:
    raise AssertionError('History report without a commit identity accepted')

# Gitleaks' own skip channels stay closed: an inline allow-comment must not be
# able to hide a finding from the reviewer, and no caller configuration may
# replace the rule set.
cmd, env = CALLS[0]
assert '--ignore-gitleaks-allow' in cmd, cmd
assert '--gitleaks-ignore-path' in cmd, cmd
assert not set(G.ENV_CONFIG) & set(env), env
assert cmd[cmd.index('--report-format') + 1] == 'json'


def fake_version(output='8.30.1'):
    def run(cmd, **kw):
        CALLS.append((list(cmd), {}))
        return subprocess.CompletedProcess(cmd, 0, stdout=output + '\n', stderr='')
    return run


# A wrong or unavailable binary fails the gate before it reads anything.
for absent_binary in (fake_version('8.29.0'),):
    real, G.subprocess.run = G.subprocess.run, absent_binary
    try:
        try:
            G.gitleaks_version()
        except SystemExit as error:
            assert 'required' in str(error), error
        else:
            raise AssertionError('Wrong Gitleaks version accepted')
    finally:
        G.subprocess.run = real

# Both entry points check the version: the projection scan and the documented
# history command must not report a version they never verified.
reached = []


def sentinel():
    reached.append(True)
    raise SystemExit('version checked')


for entry in (lambda: G.projection_scan(), lambda: G.history_scan('.')):
    real, G.gitleaks_version = G.gitleaks_version, sentinel
    try:
        try:
            entry()
        except SystemExit as error:
            assert 'version checked' in str(error), error
        else:
            raise AssertionError('Entry point did not check the binary version')
    finally:
        G.gitleaks_version = real
assert len(reached) == 2, reached

# The snapshot exception binds a finding line to the publication's own
# catalog and inventory, not to the file's own contents or a hex shape.
snapshot = json.dumps({'sources': {'RESULTS/alexen2/REPORT.md': HEX,
                                  'RESULTS/alexen2/pred.demo.jsonl': HEX,
                                  'RESULTS/unknown/pred.demo.jsonl': HEX}})
catalog = json.dumps([{'id': 'alexen2'}])
inventory = json.dumps([{'dataset': 'alexen2', 'file': 'pred.demo.jsonl', 'pred_sha256': HEX}])
context = G.reviewed_context(snapshot, catalog, inventory)
assert G.source_line_ok(f'    "RESULTS/alexen2/pred.demo.jsonl": "{HEX}",', context)
assert G.source_line_ok(f'    "RESULTS/alexen2/REPORT.md": "{HEX}",', context)
assert G.source_line_ok(f'    "RESULTS/REPORT.md": "{HEX}",', context)
assert not G.source_line_ok(f'    "RESULTS/unknown/pred.demo.jsonl": "{HEX}",', context)
assert not G.source_line_ok(f'    "RESULTS/ghost/pred.demo.jsonl": "{HEX}",', context)
assert not G.source_line_ok(f'    "RESULTS/alexen2/pred.demo.jsonl": "{hashlib.sha256(b"other").hexdigest()}",', context)
assert not G.source_line_ok(f'    "RESULTS/alexen2/pred.demo.jsonl": "{HEX}"', {'datasets': set(), 'runs': {}, 'sources': {}}) is True
assert not G.source_line_ok(f'    "RESULTS/alexen2/SECRET.md": "{HEX}",', context)
assert not G.source_line_ok(f'    "api_key": "{HEX}",', context)
# Unreadable evidence fails closed instead of allowing the line.
empty = G.reviewed_context('not json', 'not json', 'not json')
assert G.source_line_ok(f'    "RESULTS/alexen2/REPORT.md": "{HEX}",', empty) is False

print('secret-scan gate checks passed')

# The policy above is only as good as the binary's behaviour: run the pinned
# scanner on a synthetic finding that carries Gitleaks' own inline allow
# comment. With the reviewed flags the finding must still reach the gate; the
# same file scanned without them is a control that the comment does hide it.
try:
    G.gitleaks_version()
except SystemExit:
    print('pinned gitleaks not available: inline allow-comment check skipped')
else:
    line = 'api_key = "9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c"  # gitleaks:allow\n'
    with tempfile.TemporaryDirectory() as d:
        Path(d, 'secret.txt').write_text(line)
        findings = G.run_scan('dir', d, Path(d) / 'report.json')
        control = subprocess.run(['gitleaks', 'dir', d, '-f', 'json', '--no-banner',
                                  '--exit-code', '0', '-r', str(Path(d) / 'control.json')],
                                 capture_output=True, text=True)
        assert control.returncode == 0, control.stderr
        hidden = json.loads((Path(d) / 'control.json').read_text() or '[]')
    assert [f['RuleID'] for f in findings], 'an inline allow-comment hid the finding from the gate'
    assert hidden == [], 'control is inconclusive: the binary did not honour its own allow-comment'
    print('inline allow-comment control passed')
