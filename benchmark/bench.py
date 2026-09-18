import csv, json, re
import pyarrow.parquet as pq
from benchlib import RAW, find_all, pick, ru
import benchlib
SAMPLES = json.loads(benchlib.SAMPLES_F.read_text())

def hivetrace():
    for f in ('domain-00000-of-00001.parquet', 'entity-00000-of-00001.parquet'):
        for r in pq.read_table(RAW / 'hivetrace' / f).to_pylist():
            for e in r['entities']:
                assert r['text'][e['start']:e['end']] == e['text'], (r['id'], e)
            yield (r['id'], r['domain'], r['text'], [{'start': e['start'], 'end': e['end'], 'type': e['type']} for e in r['entities']])

def russian_pii_66k():
    t = pq.read_table(RAW / 'train-00000-of-00001.parquet')
    for i in SAMPLES['russian-pii-66k']:
        r = t.slice(i, 1).to_pylist()[0]
        for e in r['privacy_mask']:
            assert r['source_text'][e['start']:e['end']] == e['value'], (i, e)
        yield (f'ru66k-{i}', '', r['source_text'], [{'start': e['start'], 'end': e['end'], 'type': e['label']} for e in r['privacy_mask']])

def redmadrobot():
    for i, r in enumerate(csv.DictReader((RAW / 'redmadrobot-test.csv').open(newline=''))):
        text, pos, offs = (r['text'], 0, [])
        for tok in json.loads(r['tokens']):
            m = re.compile(re.escape(tok), re.I).search(text, pos)
            assert m and m.start() - pos <= 3, (i, tok, text[pos:pos + 40])
            offs.append(m.span())
            pos = m.end()
        ents, prev = ([], 'O')
        for (a, b), tag in zip(offs, json.loads(r['ner_tags'])):
            if tag != 'O' and tag.startswith('I-') and (prev != 'O') and (tag[2:] == prev[2:]):
                ents[-1]['end'] = b
            elif tag != 'O':
                ents.append({'start': a, 'end': b, 'type': tag[2:]})
            prev = tag
        yield (f'rmr-{i}', '', text, ents)

def scanpatch():
    rows = []
    for f in ('train.parquet', 'test.parquet'):
        for i, r in enumerate(pq.read_table(RAW / 'scanpatch' / f).to_pylist()):
            if ru(r['text']):
                rows.append((f'scp-{f[:2]}{i}', r))
    keep = set(pick('scanpatch', [rid for rid, _ in rows], 1500))
    for rid, r in rows:
        if rid not in keep:
            continue
        ents = {(a, b, t) for a, b, t in zip(r['entity_starts'], r['entity_ends'], r['entity_labels'])}
        yield (rid, r['source'], r['text'], [{'start': a, 'end': b, 'type': t} for a, b, t in sorted(ents)])

def alrosait():
    rows = [json.loads(line) for line in (RAW / 'alrosait-pii-synthetic-ru.jsonl').open()]
    keep = set(pick('alrosait', [r['id'] for r in rows], 1500))
    for r in rows:
        if r['id'] not in keep:
            continue
        seen, ents = ([], [])
        for e in r['entities']:
            for a, b in find_all(r['text'], e['text'], seen):
                ents.append({'start': a, 'end': b, 'type': e['type']})
        assert len(ents) >= len(r['entities']), r['id']
        yield (r['id'], r['domain'], r['text'], sorted(ents, key=lambda e: e['start']))
JG_DROP = {'PET', 'THEO', 'FICT', 'PUBLIC_PLACES'}
JG_MAP = {'PERSON': 'PER', 'PUBLIC_PER': 'PER', 'PUBLIC_PERSON': 'PER', 'PER_PUBLIC': 'PER'}

def jayguard():
    for i, r in enumerate(pq.read_table(RAW / 'jayguard' / 'train.parquet').to_pylist()):
        text, offs = ('', [])
        for tok in r['tokens']:
            if text:
                text += ' '
            offs.append((len(text), len(text) + len(tok)))
            text += tok
        ents, prev = ([], 'O')
        for (a, b), tag in zip(offs, r['ner_tags']):
            t = JG_MAP.get(tag[2:], tag[2:]) if tag != 'O' else 'O'
            if tag.startswith('I-') and ents and (prev == t):
                ents[-1]['end'] = b
            elif tag != 'O':
                ents.append({'start': a, 'end': b, 'type': t})
            prev = t
        yield (f'jg-{i}', '', text, [e for e in ents if e['type'] not in JG_DROP])

def nym_ru():
    rows = []
    for f in ('nym-pii-test.jsonl', 'nym-pii-validation.jsonl'):
        for i, line in enumerate((RAW / f).open()):
            o = json.loads(line)
            if ru(o['text']):
                rows.append((f'nym-{f[8]}{i}', o))
    keep = set(pick('nym-ru', [rid for rid, _ in rows], 1500))
    for rid, o in rows:
        if rid not in keep:
            continue
        yield (rid, '', o['text'], [{'start': e['start'], 'end': e['end'], 'type': e['label']} for e in o['entities']])

def secrets_issues():
    groups = {}
    for f, idc in (('test.csv', 'Issue_id'), ('test_wild.csv', 'issue_url')):
        for r in csv.DictReader((RAW / 'issue-reports' / f).open(newline='')):
            g = groups.setdefault(f'iss-{r[idc]}', {'text': r['text'], 'pos': [], 'n': 0})
            assert g['text'] == r['text'], idc
            g['n'] += 1
            if r['label'] == '1':
                g['pos'].append(r['candidate_string'])
    fit = {k: g for k, g in groups.items() if len(g['text']) <= 10000}
    pos = [k for k, g in fit.items() if g['pos']]
    neg = [k for k, g in fit.items() if not g['pos']]
    keep = set(pick('secrets-issues-pos', pos, 750)) | set(pick('secrets-issues-neg', neg, 750))
    for rid in sorted(keep):
        g = groups[rid]
        seen, ents = ([], [])
        for cand in g['pos']:
            for a, b in find_all(g['text'], cand, seen):
                ents.append({'start': a, 'end': b, 'type': 'SECRET'})
        if g['pos'] and (not ents):
            continue
        yield (rid, 'issue', g['text'], sorted(ents, key=lambda e: e['start']))

def secrets_rules():
    rows, seen_text = ({}, set())
    for f in ('gitleaks_tpfp.jsonl', 'betterleaks_tpfp.jsonl'):
        src = f.split('_')[0]
        for i, line in enumerate((RAW / 'secret-rules' / f).open()):
            o = json.loads(line)
            if o['text'] in seen_text:
                continue
            seen_text.add(o['text'])
            rows[f'{src[:2]}-{i}'] = (src, o)
    pos = [k for k, (_, o) in rows.items() if o['label'] == 'tp']
    neg = [k for k, (_, o) in rows.items() if o['label'] != 'tp']
    keep = set(pick('secrets-rules-pos', pos, 750)) | set(pick('secrets-rules-neg', neg, 750))
    for rid in sorted(keep):
        src, o = rows[rid]
        seen, ents = ([], [])
        if o['label'] == 'tp':
            try:
                found = json.loads(o['findings'] or '[]')
            except json.JSONDecodeError:
                found = []
            for fi in found:
                for a, b in find_all(o['text'], fi['Secret'], seen):
                    ents.append({'start': a, 'end': b, 'type': 'SECRET'})
            if not ents:
                continue
        yield (rid, src, o['text'], sorted(ents, key=lambda e: e['start']))
BUILDERS = {'hivetrace': hivetrace, 'russian-pii-66k': russian_pii_66k, 'redmadrobot': redmadrobot, 'scanpatch': scanpatch, 'alrosait': alrosait, 'jayguard': jayguard, 'nym-ru': nym_ru, 'secrets-issues': secrets_issues, 'secrets-rules': secrets_rules}
HF = 'https://huggingface.co/datasets/'
_SECRET_LABELS = {'en': ['secret', 'password', 'api key', 'access token', 'private key'], 'ru': ['секрет', 'пароль', 'API ключ', 'токен доступа', 'приватный ключ']}

def _g(**groups):
    return {t: g for g, ts in groups.items() for t in ts.split()}
META = {'hivetrace': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'hivetrace/pii-bench', 'license': 'apache-2.0', 'mode': 'files', 'domain': 'support requests and chats, 13 types, the only set with KPP/OGRN/CVC', 'labels': {'en': ['person', 'address', 'phone number', 'email', 'passport number', 'tax identification number', 'social insurance number', 'tax registration code', 'company registration number', 'individual entrepreneur registration number', 'bank card number', 'card security code', 'api key or token'], 'ru': ['имя человека', 'адрес', 'номер телефона', 'электронная почта', 'номер паспорта', 'ИНН', 'СНИЛС', 'КПП', 'ОГРН', 'ОГРНИП', 'номер банковской карты', 'CVC код карты', 'API ключ или токен']}, 'groups': _g(PERSON='NAME', ADDRESS='ADDRESS', CONTACT='PHONE_NUMBER EMAIL', ID='PASSPORT_NUMBER INN SNILS KPP OGRN OGRNIP BANK_CARD_NUMBER CVC', SECRET='TOKEN')}, 'russian-pii-66k': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'wolframko/russian-pii-66k', 'license': 'not specified', 'mode': 'link', 'domain': 'synthetic Russian sentences: passwords, usernames, dates of birth, accounts', 'labels': {'en': ['first name', 'surname', 'email', 'phone number', 'city', 'street', 'building number', 'zip code', 'username', 'password', 'bank account number', 'tax identification number', 'id card number', 'social security number', 'credit card number', 'driver license number', 'date of birth'], 'ru': ['имя', 'фамилия', 'электронная почта', 'номер телефона', 'город', 'улица', 'номер дома', 'почтовый индекс', 'логин', 'пароль', 'номер банковского счёта', 'ИНН', 'номер удостоверения личности', 'СНИЛС', 'номер кредитной карты', 'номер водительского удостоверения', 'дата рождения']}, 'groups': _g(PERSON='GIVENNAME SURNAME', CONTACT='TELEPHONENUM EMAIL', ADDRESS='CITY STREET BUILDINGNUM ZIPCODE', ACCOUNT='USERNAME', SECRET='PASSWORD', ID='ACCOUNTNUM TAXNUM IDCARDNUM SOCIALNUM CREDITCARDNUMBER DRIVERLICENSENUM', DATE='DATEOFBIRTH')}, 'redmadrobot': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'redmadrobot-rnd/pii_benchmark', 'license': 'mit', 'mode': 'files', 'domain': 'production-like requests with substituted PII: Russian documents, URL, IP', 'labels': {'en': ['first name', 'last name', 'middle name', 'passport number', 'driver license number', 'medical insurance number', 'military id number', 'birth certificate number', 'tax identification number', 'social insurance number', 'credit card number', 'phone number', 'email', 'url', 'ip address', 'country', 'region', 'district', 'city', 'street', 'house number'], 'ru': ['имя', 'фамилия', 'отчество', 'номер паспорта', 'номер водительского удостоверения', 'номер полиса ОМС', 'номер военного билета', 'номер свидетельства о рождении', 'ИНН', 'СНИЛС', 'номер банковской карты', 'номер телефона', 'электронная почта', 'ссылка', 'IP адрес', 'страна', 'регион', 'район', 'город', 'улица', 'номер дома']}, 'groups': _g(PERSON='FIRST_NAME LAST_NAME MIDDLE_NAME', CONTACT='PHONE EMAIL', ADDRESS='COUNTRY REGION DISTRICT CITY STREET HOUSE', NET='URL IP_ADDRESS', ID='PASSPORT DRIVER_LICENSE OMS MILITARY_ID BIRTH_CERTIFICATE CREDIT_CARD INN SNILS')}, 'scanpatch': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'scanpatch/pii-ner-corpus-synthetic-controlled', 'license': 'mit', 'mode': 'files', 'domain': 'controlled synthetic Russian text: IP inside prose, SNILS, INN, 11 address subtypes, organizations', 'labels': {'en': ['person', 'first name', 'surname', 'middle name', 'nickname', 'address', 'city', 'street', 'house number', 'zip code', 'region', 'district', 'country', 'phone number', 'email', 'ip address', 'tax identification number', 'social insurance number', 'id card number', 'vehicle registration number', 'military id number', 'organization'], 'ru': ['имя человека', 'имя', 'фамилия', 'отчество', 'ник', 'адрес', 'город', 'улица', 'номер дома', 'почтовый индекс', 'регион', 'район', 'страна', 'номер телефона', 'электронная почта', 'IP адрес', 'ИНН', 'СНИЛС', 'номер документа', 'государственный номер автомобиля', 'номер военного билета', 'организация']}, 'groups': _g(PERSON='name first_name last_name middle_name name_initials nickname', ADDRESS='address address_apartment address_building address_city address_country address_district address_geolocation address_house address_postal_code address_region address_street', CONTACT='mobile_phone email', NET='ip', ID='tin snils document_number vehicle_number military_individual_number', ORG='organization', OTHER='date')}, 'alrosait': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'alrosait/pii-synthetic-ru', 'license': 'mit', 'mode': 'files', 'domain': 'names and addresses in free speech with typos, 1026 negatives', 'labels': {'en': ['person', 'address'], 'ru': ['имя человека', 'адрес']}, 'groups': _g(PERSON='NAME', ADDRESS='ADDRESS')}, 'jayguard': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'just-ai/jayguard-ner-benchmark', 'license': 'mit (yaml) / apache-2.0 (card text)', 'mode': 'files', 'domain': 'real anonymized support chats; text re-joined from tokens', 'labels': {'en': ['person', 'address', 'city', 'country'], 'ru': ['имя человека', 'адрес', 'город', 'страна']}, 'groups': _g(PERSON='PER', ADDRESS='STREET_ADDRESS GPE')}, 'nym-ru': {'lang': 'ru', 'kind': 'pii', 'source': HF + 'Wismut/nym-pii-multilingual-data', 'license': 'mit', 'mode': 'files', 'domain': 'incidents and leaks: API_KEY, PASSWORD, USERNAME, MAC, company names, 40 types', 'labels': {'en': ['first name', 'surname', 'email', 'phone number', 'city', 'street', 'building number', 'zip code', 'country', 'username', 'password', 'api key', 'bank account number', 'tax identification number', 'id card number', 'social security number', 'credit card number', 'driver license number', 'date of birth', 'passport number', 'mac address', 'url', 'employee id', 'customer id', 'pin code', 'company name'], 'ru': ['имя', 'фамилия', 'электронная почта', 'номер телефона', 'город', 'улица', 'номер дома', 'почтовый индекс', 'страна', 'логин', 'пароль', 'API ключ', 'номер банковского счёта', 'ИНН', 'номер удостоверения личности', 'СНИЛС', 'номер кредитной карты', 'номер водительского удостоверения', 'дата рождения', 'номер паспорта', 'MAC адрес', 'ссылка', 'табельный номер сотрудника', 'номер клиента', 'PIN код', 'название компании']}, 'groups': _g(PERSON='GIVEN_NAME SURNAME', ADDRESS='BUILDING_NUMBER CITY COUNTRY SECONDARY_ADDRESS STATE STREET_ADDRESS STREET_NAME ZIP_CODE', CONTACT='EMAIL PHONE FAX_NUMBER', NET='URL MAC_ADDRESS', ACCOUNT='USERNAME EMPLOYEE_ID CUSTOMER_ID', SECRET='API_KEY PASSWORD PIN', ID='ACCOUNT_NUMBER CREDIT_DEBIT_CARD CVV DRIVERS_LICENSE GOVERNMENT_ID IBAN LICENSE_PLATE MEDICAL_RECORD_NUMBER PASSPORT ROUTING_NUMBER SSN SWIFT_BIC TAX_ID', DATE='DATE_OF_BIRTH', ORG='COMPANY_NAME', OTHER='AGE DATE GENDER TIME')}, 'secrets-issues': {'lang': 'en', 'kind': 'secrets', 'source': 'https://zenodo.org/records/19622962', 'license': 'cc-by-4.0', 'mode': 'files', 'domain': 'real GitHub issues with leaked secrets and hard negatives, up to 10k chars', 'labels': _SECRET_LABELS, 'groups': _g(SECRET='SECRET')}, 'secrets-rules': {'lang': 'en', 'kind': 'secrets', 'source': 'https://github.com/gitleaks/gitleaks + https://github.com/betterleaks/betterleaks (rule test cases)', 'license': 'mit', 'mode': 'files', 'domain': 'provider token formats: true and false positive test cases of two scanners', 'labels': _SECRET_LABELS, 'groups': _g(SECRET='SECRET')}}
if __name__ == '__main__':
    import importlib
    for mod in ('sets_ru', 'sets_en', 'sets_code', 'synth'):
        try:
            m = importlib.import_module(mod)
        except ModuleNotFoundError as e:
            if e.name != mod:
                raise
            continue
        BUILDERS |= m.BUILDERS
        META |= m.META
    benchlib.main(BUILDERS, META)
