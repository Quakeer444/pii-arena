import sys
import os
import types
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
from stratify import category, tally_row

gold = [(0, 3, 'PERSON'), (0, 3, 'USERNAME'), (4, 7, 'PASSWORD')]
original = [{'start': a, 'end': b, 'type': label} for a, b, label in gold]
counts = tally_row(gold, original, {0, 1, 2, 4}, {0, 4})
assert counts['PERSON'] == dict(hit=1, hidden=1, raw_hidden=0, covered_characters=3, original_hidden=0)
assert counts['USERNAME'] == counts['PERSON']
assert counts['PASSWORD'] == dict(hit=1, hidden=0, raw_hidden=0, covered_characters=1, original_hidden=0)
assert category('ACCOUNT_NUMBER', 'ID') == 'financial'
assert category('USERNAME', 'ACCOUNT') == 'logins'
assert category('Employee_ID_Number', 'ACCOUNT') == 'accounts'
assert category('PASSPORT', 'ID') == 'identity'
assert category('DATE', 'OTHER') == 'dates'
assert category('UUID', 'SECRET') == 'secrets'
os.environ['DEVICE'] = 'cpu'
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'benchmark'))
import run

class ShortTagger:
    def __init__(self, embedding):
        pass

    def map(self, texts):
        return iter([types.SimpleNamespace(spans=[])])

prior = sys.modules.get('natasha')
sys.modules['natasha'] = types.SimpleNamespace(NewsEmbedding=lambda: None, NewsNERTagger=ShortTagger)
try:
    predict, _ = run._natasha(None, None)
    assert predict(['one', '  ']) == [[], []]
    try:
        predict(['one', 'two'])
    except ValueError:
        pass
    else:
        raise AssertionError('Missing tagger response became an empty successful prediction')
finally:
    if prior is None:
        del sys.modules['natasha']
    else:
        sys.modules['natasha'] = prior
print('Category mapping and raw/normalized full-hiding checks passed.')
