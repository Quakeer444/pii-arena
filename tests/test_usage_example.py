"""R02: the documented usage example must run exactly as published.

The shell block and its expected output are extracted from `docs/usage.md`
itself - not restated here - copied into a temporary workspace and executed.
A prose block that drifted from the code it documents then fails the build
instead of surviving as an untested claim.
"""
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUARD = 'scripts/evaluate.py --data .local/usage-example --dataset example --model demo'
WORKSPACE = '.local/usage-example'


def fenced(text):
    """(language, body) of every fenced block, in order, skipping inner fences."""
    out, language, body = [], None, None
    for line in text.splitlines():
        if body is None and line.startswith('```'):
            language, body = line[3:].strip(), []
        elif body is not None and line.startswith('```'):
            out.append((language, '\n'.join(body)))
            language, body = None, None
        elif body is not None:
            body.append(line)
    return out


doc = (ROOT / 'docs/usage.md').read_text()
example = next((body for lang, body in fenced(doc) if lang == 'sh' and GUARD in body), None)
assert example, 'docs/usage.md no longer publishes a runnable example for the evaluator'
expected = re.search(r'```json\n(.*?)\n```', doc[doc.index(GUARD):], re.S)
assert expected, 'the example has no published expected output'

with tempfile.TemporaryDirectory() as d:
    # The documented command writes into a workspace; point it at a scratch
    # directory so the check cannot touch the preserved local archive.
    script = example.replace(WORKSPACE, d)
    assert WORKSPACE not in script, script
    run = subprocess.run(['bash', '-c', script], cwd=ROOT, capture_output=True, text=True)
    assert run.returncode == 0, run.stdout + run.stderr
    observed = json.loads(run.stdout)
assert observed == json.loads(expected.group(1)), (observed, expected.group(1))
print('usage example checks passed')
