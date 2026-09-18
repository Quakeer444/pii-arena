import functools
import json
import re
from collections import Counter
import pyarrow.parquet as pq
from benchlib import RAW, pick, ru
import benchlib

def _spans(tokens, tags, keep):
    text, ents, prev = ('', [], 'O')
    for tok, tag in zip(tokens, tags):
        if text:
            text += ' '
        a, b = (len(text), len(text) + len(tok))
        text += tok
        t = tag[2:] if tag != 'O' else 'O'
        if tag.startswith('I-') and ents and (prev == t):
            ents[-1]['end'] = b
        elif tag != 'O':
            ents.append({'start': a, 'end': b, 'type': t})
        prev = t
    return (text, [e for e in ents if e['type'] in keep])

def alexen2():
    for i, r in enumerate(pq.read_table(RAW / 'alexen2-pii-ner-ru-benchmark-test.parquet').to_pylist()):
        text, ents = _spans(r['tokens'], r['ner_tags'], {'PER', 'PHONE', 'EMAIL'})
        yield (f'alx-{i}', '', text, ents)
NEREL_KEEP = {'PERSON', 'ORGANIZATION', 'CITY', 'COUNTRY', 'DISTRICT', 'STATE_OR_PROVINCE', 'LOCATION', 'FACILITY'}

def _nerel(f):
    for line in (RAW / 'nerel' / f).open(encoding='utf-8'):
        o = json.loads(line)
        ents = []
        for e in o['entities']:
            _, head, val = e.split('\t', 2)
            typ, *pos = head.split()
            if typ not in NEREL_KEEP or len(pos) != 2:
                continue
            a, b = (int(pos[0]), int(pos[1]))
            assert o['text'][a:b] == val, (f, o['id'], e)
            ents.append({'start': a, 'end': b, 'type': typ})
        ents.sort(key=lambda e: (e['start'], e['end']))
        yield (f"nerel-{f[:2]}{o['id']}", f.partition('.')[0], o['text'], ents)

def nerel():
    rows = list(_nerel('test.jsonl')) + list(_nerel('dev.jsonl'))
    train = list(_nerel('train.jsonl'))
    keep = set(pick('nerel', [r[0] for r in train], 1500 - len(rows)))
    yield from rows
    yield from (r for r in train if r[0] in keep)
FRE_KEEP = {'name', 'surname', 'patronymic', 'nickname', 'org_name', 'loc_name'}

def factrueval():
    for coll in ('devset', 'testset'):
        for p in sorted((RAW / 'factrueval-2016' / coll).glob('book_*.txt')):
            text = p.open(encoding='utf-8', newline='').read()
            starts = {}
            for f in (ln.split() for ln in p.with_suffix('.tokens').open(encoding='utf-8')):
                if f:
                    starts[f[0]] = int(f[1])
                    assert text[int(f[1]):int(f[1]) + int(f[2])] == f[3], (p.name, f[0])
            ents = set()
            for line in p.with_suffix('.spans').open(encoding='utf-8'):
                f = line.partition('#')[0].split()
                if f[1] in FRE_KEEP:
                    assert starts[f[4]] == int(f[2]), (p.name, f[0])
                    ents.add((int(f[2]), int(f[2]) + int(f[3]), f[1]))
            yield (f'fre-{coll[0]}{p.stem[5:]}', coll, text, [{'start': a, 'end': b, 'type': t} for a, b, t in sorted(ents)])
RUB_KEEP = {'NAME', 'PHONE', 'ADDRESS', 'DOCUMENT_ID', 'CARD_NUMBER'}

def rubai_ru():
    rows = []
    for line in (RAW / 'rubai' / 'data.jsonl').open(encoding='utf-8'):
        o = json.loads(line)
        if ru(o['original']) and len(o['original'].split()) == len(o['types']):
            rows.append(o)
    keep = set(pick('rubai-ru', [f"rub-{o['id']}" for o in rows], 1500))
    for o in rows:
        rid = f"rub-{o['id']}"
        if rid not in keep:
            continue
        ents, prev = ([], -2)
        for i, (m, t) in enumerate(zip(re.finditer('\\S+', o['original']), o['types'])):
            if t not in RUB_KEEP:
                continue
            if prev == i - 1 and ents[-1]['type'] == t:
                ents[-1]['end'] = m.end()
            else:
                ents.append({'start': m.start(), 'end': m.end(), 'type': t})
            prev = i
        yield (rid, o['domain'], o['original'], ents)

def _conll(path):
    rid = dom = None
    toks, tags = ([], [])
    for line in path.open(encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('# id '):
            rid, dom = line[5:].split(None, 1)
            dom = dom.partition('=')[2]
        elif not line.strip():
            if toks:
                yield (rid, dom, toks, tags)
                toks, tags = ([], [])
        else:
            tok, tag = line.split(' _ _ ')
            toks.append(tok)
            tags.append(tag)
    if toks:
        yield (rid, dom, toks, tags)

def multiconer_ru():
    f = RAW / 'multiconer-v1' / 'RU-Russian' / 'ru_test.conll'
    keep = set(pick('multiconer-ru', [f'mcn-{rid}' for rid, *_ in _conll(f)], 1500))
    for rid, dom, toks, tags in _conll(f):
        if f'mcn-{rid}' in keep:
            text, ents = _spans(toks, tags, {'PER', 'CORP', 'GRP', 'LOC'})
            yield (f'mcn-{rid}', dom, text, ents)
RDC_DROP = {'Date_Time', 'Business_Title'}

@functools.cache
def _redact():
    return json.loads((RAW / 'redact' / 'pii_benchmark_full.json').read_text(encoding='utf-8'))

def _rdc_ents(r):
    ents = []
    for e in r['entities']:
        if e.get('start') is None or e['entity_type'] in RDC_DROP:
            continue
        assert r['text'][e['start']:e['end']] == e['entity_string'], (r['record_id'], e)
        ents.append({'start': e['start'], 'end': e['end'], 'type': e['entity_type']})
    ents.sort(key=lambda e: (e['start'], e['end']))
    return ents

def redact_ru():
    for i, r in enumerate(_redact()):
        if r['axes']['language'] == 'RU':
            yield (f'rdc-{i}', r['axes']['domain'], r['text'], _rdc_ents(r))

def redact_multi():
    rows = [(i, r) for i, r in enumerate(_redact()) if r['axes']['language'] != 'RU']
    keep = set(pick('redact-multi', [f'rdcm-{i}' for i, _ in rows], 1000))
    langs = Counter()
    for i, r in rows:
        if f'rdcm-{i}' not in keep:
            continue
        langs[r['axes']['language']] += 1
        yield (f'rdcm-{i}', r['axes']['language'], r['text'], _rdc_ents(r))
    META['redact-multi']['langs'] = dict(langs.most_common())
BUILDERS = {'alexen2': alexen2, 'nerel': nerel, 'factrueval': factrueval, 'rubai-ru': rubai_ru, 'multiconer-ru': multiconer_ru, 'redact-ru': redact_ru, 'redact-multi': redact_multi}
HF = 'https://huggingface.co/datasets/'

def _g(**groups):
    return {t: g for g, ts in groups.items() for t in ts.split()}
_RDC_LABELS = {'en': ['person', 'first name', 'surname', 'preferred name', 'organization', 'address', 'city', 'state', 'country of residence', 'location', 'place of birth', 'geolocation', 'email', 'phone number', 'emergency contact', 'ip address', 'social media handle', 'employee id', 'customer reference number', 'badge number', 'password', 'passport number', 'national id number', 'tax reference number', 'driver license number', 'credit card number', 'date of birth', 'age', 'gender', 'nationality', 'citizenship status', 'marital status', 'religion', 'political party', 'sexual orientation', 'trade union membership', 'politically exposed person', 'medical information', 'allergy information', 'sick leave record', 'criminal record', 'disciplinary action', 'performance assessment', 'professional background', 'salary', 'bank account statement'], 'ru': ['имя человека', 'имя', 'фамилия', 'предпочитаемое имя', 'организация', 'адрес', 'город', 'регион', 'страна проживания', 'место', 'место рождения', 'геолокация', 'электронная почта', 'номер телефона', 'контакт для экстренной связи', 'IP адрес', 'аккаунт в соцсети', 'табельный номер сотрудника', 'номер клиента', 'номер пропуска', 'пароль', 'номер паспорта', 'национальный идентификационный номер', 'налоговый номер', 'номер водительского удостоверения', 'номер банковской карты', 'дата рождения', 'возраст', 'пол', 'национальность', 'гражданство', 'семейное положение', 'религия', 'политическая партия', 'сексуальная ориентация', 'членство в профсоюзе', 'публичное должностное лицо', 'медицинские сведения', 'сведения об аллергии', 'сведения о больничных', 'судимость', 'дисциплинарное взыскание', 'оценка работы', 'профессиональный опыт', 'зарплата', 'выписка по счёту']}
_RDC_GROUPS = _g(PERSON='Full_Name First_Given_Name Last_Family_Name Preferred_Name', ADDRESS='Address_Personal Address_Work City State Location Country_of_Residence Place_of_Birth Geolocation_Data', CONTACT='Work_Email_Address Personal_Email_Address Telephone_Numbers_Personal Telephone_Numbers_Work Emergency_Contact_Details', NET='Static_IP_Address', ACCOUNT='Social_Media_Identifiers Employee_ID_Number Customer_Reference_Number Building_Badge_Card_Number', SECRET='Password', ID='National_Identification_Number Passport_Number Credit_Card_Numbers Tax_Reference_Number Driving_License_Number', ORG='Org_Name', DATE='Date_of_Birth', OTHER='Age Gender Nationality Citizenship_Status Marital_Status Religion Political_Party Sex_Orientation Trade_Union_Membership PEP_Status Medical_Information Allergy_Information Sickness_Day_Records Crime Disciplinary_Action Performance_Assessment Professional_Background Compensation_and_Salary Account_Statements')
META = {'alexen2': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'alexen2/pii-ner-ru-benchmark', 'license': 'not specified', 'mode': 'link', 'domain': 'call-centre style short sentences, 3 types; text re-joined from tokens', 'labels': {'en': ['person', 'phone number', 'email'], 'ru': ['имя человека', 'номер телефона', 'электронная почта']}, 'groups': _g(PERSON='PER', CONTACT='PHONE EMAIL')}, 'nerel': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'iluvvatar/NEREL', 'license': 'not specified', 'mode': 'link', 'domain': 'Russian news documents with nested entities: the main donor of ORGANIZATION', 'labels': {'en': ['person', 'organization', 'city', 'country', 'district', 'state or province', 'location', 'facility'], 'ru': ['имя человека', 'организация', 'город', 'страна', 'район', 'регион', 'местность', 'объект']}, 'groups': _g(PERSON='PERSON', ORG='ORGANIZATION', ADDRESS='CITY COUNTRY DISTRICT STATE_OR_PROVINCE LOCATION FACILITY')}, 'factrueval': {'lang': 'ru', 'kind': 'pii', 'source': 'https://github.com/dialogue-evaluation/factRuEval-2016', 'license': 'mit', 'mode': 'files', 'domain': '2016 news corpus, whole documents; second donor of organizations', 'labels': {'en': ['first name', 'surname', 'patronymic', 'nickname', 'organization', 'location'], 'ru': ['имя', 'фамилия', 'отчество', 'ник', 'организация', 'место']}, 'groups': _g(PERSON='name surname patronymic nickname', ORG='org_name', ADDRESS='loc_name')}, 'rubai-ru': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'islomov/rubai-NER-150K-Personal', 'license': 'apache-2.0', 'mode': 'files', 'domain': 'informal Uzbek-Russian messages, Russian slice: addresses and card numbers in prose', 'labels': {'en': ['person', 'phone number', 'address', 'document number', 'bank card number'], 'ru': ['имя человека', 'номер телефона', 'адрес', 'номер документа', 'номер банковской карты']}, 'groups': _g(PERSON='NAME', CONTACT='PHONE', ADDRESS='ADDRESS', ID='DOCUMENT_ID CARD_NUMBER')}, 'multiconer-ru': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'tomaarsen/MultiCoNER', 'license': 'cc-by-4.0', 'mode': 'files', 'domain': 'short low-context sentences and search queries: complex person and company names', 'labels': {'en': ['person', 'company', 'group or organization', 'location'], 'ru': ['имя человека', 'компания', 'группа или организация', 'место']}, 'groups': _g(PERSON='PER', ORG='CORP GRP', ADDRESS='LOC')}, 'redact-ru': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'guneeshv/REDACT-PII-Benchmark', 'license': 'other (gated, terms accepted)', 'mode': 'link', 'domain': 'controlled PII benchmark, Russian slice: 49 types, sensitive attributes, chats and forms', 'labels': _RDC_LABELS, 'groups': _RDC_GROUPS}, 'redact-multi': {'lang': 'multi', 'kind': 'pii', 'source': HF + 'guneeshv/REDACT-PII-Benchmark', 'license': 'other (gated, terms accepted)', 'mode': 'link', 'domain': 'same benchmark, 24 languages except Russian: same detectors on another alphabet', 'labels': _RDC_LABELS, 'groups': _RDC_GROUPS}}
if __name__ == '__main__':
    benchlib.main(BUILDERS, META)
