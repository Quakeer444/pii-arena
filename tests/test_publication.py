"""The frozen-report parser rejects missing tables and broken rows."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'scripts'))
from export import table, number

assert table('| a | b |\n|---|---|\n| m | **42** |\n\nAfter', '| a |') == [{'a':'m','b':'42'}]
assert number('-') is None and number('1.5%')==1.5
try:
    table('| a | b |\n|---|---|\n| m | 42 | extra |','| a |')
except ValueError:pass
else:raise AssertionError('Malformed row accepted')
try:
    table('No table present','| a |')
except StopIteration:pass
else:raise AssertionError('Missing table accepted')

# F06: the secret-scan allowlist binds exceptions to reviewed content, not bare
# positions: digest sets for exact lines, a strict line-shape validator for the
# provenance manifest digest entries.
import hashlib, json, re
scan = Path(__file__).resolve().parent.parent/'scripts/scan_secrets.py'
source = scan.read_text()
assert 'content digests verified' in source and 're-review' in source
assert 'manifest-digest-line' in source
digests = re.findall(r"'([0-9a-f]{64})'", source.split('ALLOWED = {')[1].split('def main')[0])
assert digests, 'no digest-bound allowlist entries found'
lines = (scan.parent.parent/'benchmark/rules_ru.py').read_text().splitlines()

# R05: the manifest-digest exception is structural - only real
# public_module_sha256 entries with a matching module hash are allowed; a
# stray api_key field with a valid SHA-256 shape is rejected.
import scan_secrets
def _tree_bytes(name):
    p = scan_secrets.ROOT / 'benchmark' / name
    return p.read_bytes() if p.is_file() else None
_hex64 = hashlib.sha256(b'anything').hexdigest()
assert not scan_secrets.manifest_line_ok(f'  "api_key": "{_hex64}",', _tree_bytes)
assert not scan_secrets.manifest_line_ok(f'  "ghost.py": "{_hex64}",', _tree_bytes)
_prov = json.loads((scan_secrets.ROOT / 'benchmark/PROVENANCE.json').read_text())
_real = next(iter(_prov['public_module_sha256'].items()))
assert scan_secrets.manifest_line_ok(f'    "{_real[0]}": "{_real[1]}",', _tree_bytes)

# F14: GitHub slug rules used by the anchor checker.
import verify
assert verify.github_slug('Quick start') == 'quick-start'
assert verify.github_slug('What does the benchmark contain?') == 'what-does-the-benchmark-contain'
anchors = verify.heading_anchors('# One\n## Two\n# One\n### A & B!')
assert anchors == {'one', 'one-1', 'two', 'a--b'}, anchors
print('publication parser checks passed')
