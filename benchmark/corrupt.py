import csv, json, random, re, sys
import benchlib
VARIANTS = 7
ZWSP = '\u200b'
HOMO = {'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'х': 'x', 'у': 'y', 'к': 'k', 'м': 'm', 'т': 't', 'н': 'h', 'в': 'b', 'А': 'A', 'Е': 'E', 'О': 'O', 'Р': 'P', 'С': 'C', 'Х': 'X', 'У': 'Y', 'К': 'K', 'М': 'M', 'Т': 'T', 'Н': 'H', 'В': 'B'}
HOMO |= {v: k for k, v in HOMO.items()}
OCR = {'о': '0', 'О': '0', 'l': '1', 'з': '3', 'З': '3'}
TRL = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia'}
URL_TOKEN = re.compile('[^\\s@:]+(?:@|://)\\S*')

def urlenc(s):
    return s.replace('@', '%40').replace(':', '%3A').replace(' ', '%20')

def homoglyph(s, r):
    return ''.join((HOMO[c] if c in HOMO and r.random() < 0.3 else c for c in s))

def ocr(s, r):
    s = s.replace('rn', 'm')
    s = ''.join((OCR.get(c, c) for c in s))
    return ''.join(('' if c == ' ' and r.random() < 0.3 else c for c in s))

def translit(s):
    out = []
    for c in s:
        v = TRL.get(c.lower())
        out.append(c if v is None else v.capitalize() if c.isupper() else v)
    return ''.join(out)

def invisible(s, r):
    if len(s) < 2:
        return s + ZWSP
    for pos in sorted((r.randrange(1, len(s)) for _ in range(r.randint(1, 3))), reverse=True):
        s = s[:pos] + ZWSP + s[pos:]
    return s

def piece(s, var, r, span, pii, edge, prev=''):
    if var == 0:
        return urlenc(s) if span and ('@' in s or '://' in s) else URL_TOKEN.sub(lambda m: urlenc(m[0]), s)
    if var == 1:
        return homoglyph(s, r) if span and pii else s
    if var == 2:
        out = re.sub('(?<!\\r)\\n', '\r\n', '\r' + s if prev == '\r' else s).replace(' ', '  ')
        return out[1:] if prev == '\r' else out
    if var == 3:
        return ocr(s, r) if span or edge else s
    if var == 4:
        return s.upper()
    if var == 5:
        return translit(s) if span and pii else s
    return invisible(s, r) if span else s

def _apply(text, ents, var, r, groups):
    if not ents:
        return (piece(text, var, r, var in (1, 5, 6), True, True), [])
    out, new, pos = ('', [], 0)
    for e in sorted(ents, key=lambda e: e['start']):
        gap = text[pos:e['start']]
        if gap:
            head, mid, tail = (gap, '', '') if len(gap) <= 60 else (gap[:30], gap[30:-30], gap[-30:])
            out += piece(head, var, r, False, False, len(gap) <= 60 or pos > 0, out[-1:])
            out += piece(mid, var, r, False, False, False, out[-1:])
            out += piece(tail, var, r, False, False, True, out[-1:])
        val = piece(text[e['start']:e['end']], var, r, True, groups.get(e['type']) != 'SECRET', False, out[-1:])
        assert val.strip(), (var, e)
        new.append({'start': len(out), 'end': len(out) + len(val), 'type': e['type']})
        out += val
        pos = e['end']
    rest = text[pos:]
    out += piece(rest[:30], var, r, False, False, bool(ents), out[-1:])
    out += piece(rest[30:], var, r, False, False, False, out[-1:])
    return (out, new)

def corrupt(text, ents, i, groups):
    for k in range(VARIANTS):
        out, new = _apply(text, ents, (i + k) % VARIANTS, random.Random(i), groups)
        if out != text:
            break
    assert out != text, i
    return (out, new)

def rows(name, groups):
    for i, r in enumerate(csv.DictReader((benchlib.BENCH / name / 'bench.csv').open(newline=''))):
        ents = json.loads(r['entities'])
        text, new = corrupt(r['text'], ents, i, groups)
        assert len(new) == len(ents), (name, r['id'])
        yield (r['id'], r['domain'], text, new)

def main(names):
    for name in names:
        meta = json.loads((benchlib.BENCH / name / 'meta.json').read_text())
        out = list(rows(name, meta['groups']))
        base = list(csv.DictReader((benchlib.BENCH / name / 'bench.csv').open(newline='')))
        assert len(out) == len(base), (name, len(out), len(base))
        assert sum((len(e) for *_, e in out)) == sum((len(json.loads(b['entities'])) for b in base)), name
        meta |= {'base': name, 'corruption': 'i % 7: 0 url-encoding of email and url, 1 cyrillic/latin homoglyphs, 2 CRLF and doubled spaces, 3 OCR noise, 4 upper case, 5 transliteration, 6 zero-width spaces; a row without gold spans is corrupted as a whole; a variant that is a no-op on its row yields to the next one, so no row equals the base; homoglyphs and transliteration touch PII spans only'}
        benchlib.build(f'corrupt-{name}', lambda o=out: iter(o), meta)
if __name__ == '__main__':
    main(sys.argv[1:] or ['hivetrace', 'redmadrobot', 'secrets-issues'])
