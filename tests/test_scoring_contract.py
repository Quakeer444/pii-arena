"""T06: an unusable external annotation is refused, not silently dropped.

`norm` discards a span it cannot place in the text, so a mistyped annotation
used to leave the denominator without a word: the row simply scored easier.
The gold loader now names the offending row, and this pins that contract for
an external CSV that was not built by `benchlib.build`.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'benchmark'))
import score

CSV = Path('BENCH/example/bench.csv')
TEXT = 'Contact Sample Person today.'


def refuses(raw, needle):
    try:
        score.check_gold(CSV, 'one', TEXT, raw)
    except SystemExit as error:
        assert needle in str(error), error
    else:
        raise AssertionError(f'Unusable annotation accepted: {raw}')


def annotation(**fields):
    return json.dumps([{'start': 8, 'end': 21, 'type': 'PERSON'} | fields])


# `norm` would drop every one of these silently.
assert score.norm(TEXT, [{'start': 0, 'end': 50, 'type': 'PERSON'}], 'type') == []
assert score.norm(TEXT, [{'start': 8, 'end': 8, 'type': 'PERSON'}], 'type') == []

refuses(annotation(end=50), 'outside')
refuses(annotation(start=-1, end=4), 'outside')
refuses(annotation(start=21, end=21), 'empty')
refuses(annotation(start=True, end=4), 'integers')
refuses(annotation(end=4.5), 'integers')
refuses(annotation(type=''), 'type')
refuses(annotation(type=7), 'type')
refuses('not json', 'JSON')
refuses(json.dumps({'start': 8, 'end': 21, 'type': 'PERSON'}), 'list')

# A usable annotation passes, and a label the dataset groups do not name is
# not an error: it is scored and reported, not deleted.
entities = score.check_gold(CSV, 'one', TEXT, annotation())
assert entities == [{'start': 8, 'end': 21, 'type': 'PERSON'}], entities
assert score.check_gold(CSV, 'one', TEXT, annotation(type='UNLISTED_LABEL'))[0]['type'] == 'UNLISTED_LABEL'
print('scoring-contract checks passed')
