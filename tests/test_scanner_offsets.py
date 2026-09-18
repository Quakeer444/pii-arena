"""T01: the scanner adapter must not present a guessed position as resolved.

Fixtures replay the report shape of the pinned Gitleaks 8.30.1 (1-based
line numbers, UTF-8 byte columns counted from the preceding newline, Match vs
capture-group Secret, decoded findings whose columns describe the encoded
segment) against `gitleaks_item` and `spans_of`. A mapping the report cannot
prove has to come out `unresolved`, never as a confident position.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'benchmark'))
import run_leaks as R


def columns(text, offset):
    """Gitleaks 8.30.1 byte column for one character offset: 1-based, counted
    from the preceding newline character, so line 1 is exact and later lines
    are one column high."""
    line = text.count('\n', 0, offset) + 1
    line_start = text.rfind('\n', 0, offset) + 1
    if line == 1:
        return line, len(text[:offset].encode()) + 1
    return line, len(text[line_start:offset].encode()) + 2


def finding(text, start, end, secret, match, tags=()):
    sl, sc = columns(text, start)
    el, ec = columns(text, end)
    return {'RuleID': 'generic-api-key', 'StartLine': sl, 'StartColumn': sc,
            'EndLine': el, 'EndColumn': ec, 'Match': match, 'Secret': secret,
            'Tags': list(tags)}


def mapped(text, report):
    return R.spans_of(text, [R.gitleaks_item(text.encode(), report)])[0]


def occurrence(text, value, nth=0):
    start = -1
    for _ in range(nth + 1):
        start = text.index(value, start + 1)
    return start, start + len(value)


# 1. UTF-8 controls (the first-pass counter-examples): byte columns must be
# converted to character offsets, and a repeated value must stay on the
# occurrence the scanner reported, whichever one it is.
utf8 = 'Имя: Иванов, ключ "SAMEVALUE" и снова "SAMEVALUE".'
secret = 'SAMEVALUE'
first, second = occurrence(utf8, secret), occurrence(utf8, secret, 1)
for index, (a, b) in enumerate((first, second)):
    span = mapped(utf8, finding(utf8, a, b, secret, secret))
    assert (span['start'], span['end']) == (a, b), (index, span)
    assert 'unresolved' not in span, span

# 2. The Secret repeats inside its own Match: the capture it came from is not
# recoverable, so the reported Match range is kept and marked unresolved
# instead of silently landing on the identifier on the left.
collision = 'token_A1b2C3d4 = "token_A1b2C3d4"'
value = 'token_A1b2C3d4'
span = mapped(collision, finding(collision, 0, len(collision), value, collision))
assert span['unresolved'] is True and span['unresolved_reason'] == 'capture-collision', span
assert (span['start'], span['end']) != (0, len(value)), 'capture resolved by first substring hit'
assert span['start'] == 0, span

# 3. A capture that occurs once inside the Match is the capture: that one is
# provable, so the finding resolves onto the value and not the whole Match.
unique = 'aws_key: SECRET-9Q7Z'
mark = unique.index('SECRET-9Q7Z')
span = mapped(unique, finding(unique, 0, len(unique), 'SECRET-9Q7Z', unique))
assert (span['start'], span['end']) == (mark, mark + len('SECRET-9Q7Z')), span
assert 'unresolved' not in span, span

# 4. Decoded finding with an unrelated copy of the same value in open text:
# the reported range describes the encoded segment, so the open copy is not
# evidence of where the scanner found it.
blob = 'QUJDREVGR0g9U0VDUkVULVZBTEVF'
lines = ['The same value SECRET-VALUE appears here in the open.', 'payload=' + blob]
decoded_text = '\n'.join(lines)
open_copy = occurrence(decoded_text, 'SECRET-VALUE')
coded_at = decoded_text.index(blob)
report = finding(decoded_text, coded_at, coded_at + len(blob), 'SECRET-VALUE',
                 'key=SECRET-VALUE', tags=('decoded:base64', 'decode-depth:1'))
span = mapped(decoded_text, report)
assert span['unresolved'] is True and span['unresolved_reason'] == 'decoded', span
assert (span['start'], span['end']) == (coded_at, coded_at + len(blob)), span
assert span['start'] != open_copy[0], 'decoded finding moved onto an unrelated copy'

# 5. The same decoded finding without the copy keeps the reported range too:
# the defect was not the absence of a copy but the guessing itself.
only_blob = 'payload=' + blob
coded_at = only_blob.index(blob)
span = mapped(only_blob, finding(only_blob, coded_at, coded_at + len(blob), 'SECRET-VALUE',
                                 'key=SECRET-VALUE', tags=('decoded:base64',)))
assert span['unresolved'] is True and span['unresolved_reason'] == 'decoded', span
assert (span['start'], span['end']) == (coded_at, coded_at + len(blob)), span

# 6. A report without usable columns keeps the reported range as unresolved
# instead of resolving the value against the whole document.
nocol = 'inline SECRET-VALUE and later SECRET-VALUE'
report = {'RuleID': 'generic-api-key', 'Match': 'SECRET-VALUE', 'Secret': 'SECRET-VALUE'}
item = R.gitleaks_item(nocol.encode(), report)
assert len(item) == 6 and item[5] == R.NATIVE, item
span = R.spans_of(nocol, [item])[0]
assert span['unresolved'] is True and span['unresolved_reason'] == R.NATIVE, span

print('scanner offset mapping checks passed')
