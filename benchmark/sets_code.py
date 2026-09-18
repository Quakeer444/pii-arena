import collections, csv, hashlib, io, json, re, zipfile
from pathlib import Path
from benchlib import RAW, pick, ru
import benchlib
HF = 'https://huggingface.co/datasets/'
SECRET_LABELS = {'en': ['secret', 'password', 'api key', 'access token', 'private key'], 'ru': ['секрет', 'пароль', 'API ключ', 'токен доступа', 'приватный ключ']}

def _g(**groups):
    return {t: g for g, ts in groups.items() for t in ts.split()}
GRETEL_LANG = {'English': 'en', 'German': 'de', 'France': 'fr', 'Spanish': 'es', 'Italian': 'it', 'Dutch': 'nl', 'Swedish': 'sv'}
GRETEL_DOCS = {'IT support ticket', 'Customer support conversational log'}
GRETEL_HOT = {'password', 'api_key', 'user_name', 'ipv4', 'ipv6'}
GRETEL_DROP = {'date', 'time', 'date_time'}

def gretel_multi():
    import pyarrow.parquet as pq
    rows = []
    for r in pq.read_table(RAW / 'gretel-finance-test.parquet').to_pylist():
        spans = json.loads(r['pii_spans'])
        text = r['generated_text']
        if any((not 0 <= s['start'] < s['end'] <= len(text) for s in spans)):
            continue
        if r['document_type'] in GRETEL_DOCS or {s['label'] for s in spans} & GRETEL_HOT:
            rows.append((f"gr-{r['level_0']}", r, spans))
    keep = set(pick('gretel-multi', [rid for rid, _, _ in rows], 1500))
    langs = collections.Counter()
    for rid, r, spans in rows:
        if rid not in keep:
            continue
        langs[GRETEL_LANG[r['language']]] += 1
        ents = [{'start': s['start'], 'end': s['end'], 'type': s['label']} for s in spans if s['label'] not in GRETEL_DROP]
        yield (rid, r['document_type'], r['generated_text'], sorted(ents, key=lambda e: e['start']))
    META['gretel-multi']['langs'] = dict(langs.most_common())
PRIVY_G = _g(PERSON='PERSON', ADDRESS='LOCATION COORDINATE', CONTACT='EMAIL_ADDRESS PHONE_NUMBER', NET='URL IP_ADDRESS MAC_ADDRESS', ORG='ORGANIZATION', SECRET='PASSWORD', ID='CREDIT_CARD US_BANK_NUMBER IBAN_CODE IMEI US_PASSPORT US_DRIVER_LICENSE US_LICENSE_PLATE US_ITIN US_SSN')

def _privy_lines():
    with zipfile.ZipFile(RAW / 'privy' / 'privy-dataset.zip').open('test-large.json') as fh:
        yield from fh

def privy():
    n = sum((line == b'    {\n' for line in _privy_lines()))
    keep = set(pick('privy', [f'privy-{i}' for i in range(n)], 1500))
    i, buf = (-1, None)
    for line in _privy_lines():
        if line == b'    {\n':
            i += 1
            buf = [b'{'] if f'privy-{i}' in keep else None
        elif buf is not None:
            if line.startswith(b'    }'):
                o = json.loads(b''.join(buf + [b'}']).decode())
                ents = [{'start': s['start_position'], 'end': s['end_position'], 'type': s['entity_type']} for s in o['spans'] if s['entity_type'] in PRIVY_G]
                for e in ents:
                    assert o['full_text'][e['start']:e['end']], (i, e)
                yield (f'privy-{i}', '', o['full_text'], sorted(ents, key=lambda e: e['start']))
                buf = None
            else:
                buf.append(line)
CRED_MAX = 10000

def creddata():
    byfile = {}
    for f in sorted((RAW / 'creddata' / 'meta').glob('*.csv')):
        for r in csv.DictReader(f.open(newline='')):
            byfile.setdefault(r['FilePath'], []).append(r)
    rows, pos, neg = ({}, [], [])
    for p, meta_rows in sorted(byfile.items()):
        src = (RAW / 'creddata' / p).read_text(encoding='utf8').replace('\r\n', '\n').replace('\r', '\n')
        lines = src.split('\n')
        groups = {}
        for r in meta_rows:
            groups.setdefault((int(r['LineStart']), int(r['LineEnd'])), []).append(r)
        for (a, b), g in sorted(groups.items()):
            text = lines[a - 1] if a == b else '\n'.join(lines[a - 1:b])
            if not text.strip() or len(text) > CRED_MAX:
                continue
            off = 0 if a == b else len(text) - len(lines[b - 1])
            true_rows = [r for r in g if r['GroundTruth'] == 'T']
            ents = []
            for r in true_rows:
                if r['ValueStart'] in ('', '-1') or r['ValueEnd'] in ('', '-1'):
                    continue
                s, e = (int(r['ValueStart']), off + int(r['ValueEnd']))
                if not 0 <= s < e <= len(text) or not text[s:e].strip():
                    continue
                if a == b and '\n' in text[s:e]:
                    continue
                ents.append({'start': s, 'end': e, 'type': r['Category']})
            if true_rows and (not ents):
                continue
            rid = f"cred-{p.removeprefix('data/')}-{a}-{b}"
            ext = Path(p).suffix.lstrip('.') or 'noext'
            rows[rid] = (rid, ext, text, sorted(ents, key=lambda x: x['start']))
            (pos if ents else neg).append(rid)
    keep = set(pick('creddata-pos', pos, 750)) | set(pick('creddata-neg', neg, 750))
    for rid in sorted(keep):
        row = rows[rid]
        for e in row[3]:
            META['creddata']['groups'][e['type']] = 'SECRET'
        yield row
OFFSET_SPEC = json.loads(Path(__file__).with_name('corpus_offsets.json').read_text())
SKIPPED_BINARY = []

def _repo(name, prefix):
    root = RAW / name
    spec, found = (OFFSET_SPEC[name]['files'], set())
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root).as_posix()
        if not path.is_file() or rel.startswith('.git/'):
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode()
        except UnicodeDecodeError:
            text = None
        if text is None or '\x00' in text:
            SKIPPED_BINARY.append(f'{name}/{rel}')
            continue
        ents = []
        if entry := spec.get(rel):
            if hashlib.sha256(raw).hexdigest() != entry['sha256']:
                raise ValueError(f'{name}/{rel}: source fingerprint mismatch')
            found.add(rel)
            for a, b in entry['spans']:
                if not 0 <= a < b <= len(text) or not text[a:b].strip():
                    raise ValueError(f'{name}/{rel}: invalid frozen annotation offset')
                ents.append({'start': a, 'end': b, 'type': 'SECRET'})
        yield (f'{prefix}-{rel}', rel, text, ents)
    if missing := set(spec) - found:
        raise FileNotFoundError(f'{name}: annotated source files missing: {sorted(missing)}')

def leak_museum():
    yield from _repo('leak-museum', 'lm')

def leaky_repo():
    yield from _repo('leaky-repo', 'lr')
_SCRIPTS = ((12352, 12543, 'ja'), (19968, 40959, 'zh'), (44032, 55215, 'ko'), (1536, 1791, 'ar'), (2304, 2431, 'hi'), (880, 1023, 'el'), (1424, 1535, 'he'), (3584, 3711, 'th'), (1024, 1279, 'cyr'))
_STOP = {'de': 'der die das und ist nicht für mit sie ich auf den dem ein eine wird von zu bitte wurde', 'fr': 'le la les des est pour avec vous votre une dans nous que sur je pas au du merci être', 'es': 'el la los las de que para con una por del en no se ha su es este cuenta usuario', 'pt': 'o a os as de que para com uma por do da em não você seu sua obrigado conta', 'it': 'il lo la le di che per con una del nel non si sono alla della gli è utente', 'nl': 'de het een van is en voor met niet op je uw zijn aan dat wij naar bij', 'sv': 'och att det som en av för inte har till den var på jag vi är kan med', 'da': 'og at det som en af for ikke har til den var på jeg vi er kan med', 'fi': 'ja on ei että se hän oli olen tai kun mutta joka niin voi teidän', 'cs': 'a je se na to v že pro ne byl jsem které nebo prosím vás', 'pl': 'i w z na nie to jest się że do dla oraz jak proszę', 'ro': 'și de la în care nu pentru cu este să am fost sau vă rog', 'tr': 've bir bu için ile de da var yok mu bize hesap', 'hu': 'a az és hogy nem is meg egy van ki kérem', 'id': 'dan yang di untuk dengan tidak ini itu adalah anda', 'vi': 'và của là các không được cho trong bạn', 'en': 'the of and to in is are you your for that with this not was be have please'}
_STOP = {k: set(v.split()) for k, v in _STOP.items()}
_UKR = re.compile('[іїєґІЇЄҐ]')
_TOKEN = re.compile('[^\\W\\d_]+')

def _lang(text):
    if ru(text):
        return 'ru'
    alpha = sum((ch.isalpha() for ch in text))
    hist = collections.Counter()
    for ch in text:
        o = ord(ch)
        for a, b, name in _SCRIPTS:
            if a <= o <= b:
                hist[name] += 1
                break
    if hist:
        name, n = hist.most_common(1)[0]
        if hist['ja'] >= 3:
            name = 'ja'
        if n * 5 >= alpha:
            return 'uk' if name == 'cyr' and _UKR.search(text) else name
    words = {w.lower() for w in _TOKEN.findall(text)}
    best, hits = ('?', 0)
    for lang, stop in _STOP.items():
        k = len(words & stop)
        if k > hits:
            best, hits = (lang, k)
    return best

def _nym(rows_lang, name, prefix):
    rows = []
    for f in ('nym-pii-test.jsonl', 'nym-pii-validation.jsonl'):
        for i, line in enumerate((RAW / f).open()):
            o = json.loads(line)
            lang = _lang(o['text'])
            if rows_lang(lang):
                rows.append((f'{prefix}-{f[8]}{i}', lang, o))
    keep = set(pick(name, [rid for rid, _, _ in rows], 1500))
    langs = collections.Counter()
    for rid, lang, o in rows:
        if rid not in keep:
            continue
        langs[lang] += 1
        yield (rid, lang, o['text'], [{'start': e['start'], 'end': e['end'], 'type': e['label']} for e in o['entities']])
    if 'langs' in META[name]:
        META[name]['langs'] = dict(langs.most_common())

def nym_en():
    yield from _nym(lambda l: l == 'en', 'nym-en', 'nyme')

def nym_multi():
    yield from _nym(lambda l: l not in ('en', 'ru'), 'nym-multi', 'nymm')
NYM_LABELS = {'en': ['first name', 'surname', 'email', 'phone number', 'city', 'street', 'building number', 'zip code', 'country', 'username', 'password', 'api key', 'bank account number', 'tax identification number', 'id card number', 'social security number', 'credit card number', 'driver license number', 'date of birth', 'passport number', 'mac address', 'url', 'employee id', 'customer id', 'pin code', 'company name'], 'ru': ['имя', 'фамилия', 'электронная почта', 'номер телефона', 'город', 'улица', 'номер дома', 'почтовый индекс', 'страна', 'логин', 'пароль', 'API ключ', 'номер банковского счёта', 'ИНН', 'номер удостоверения личности', 'СНИЛС', 'номер кредитной карты', 'номер водительского удостоверения', 'дата рождения', 'номер паспорта', 'MAC адрес', 'ссылка', 'табельный номер сотрудника', 'номер клиента', 'PIN код', 'название компании']}
NYM_GROUPS = _g(PERSON='GIVEN_NAME SURNAME', ADDRESS='BUILDING_NUMBER CITY COUNTRY SECONDARY_ADDRESS STATE STREET_ADDRESS STREET_NAME ZIP_CODE', CONTACT='EMAIL PHONE FAX_NUMBER', NET='URL MAC_ADDRESS', ACCOUNT='USERNAME EMPLOYEE_ID CUSTOMER_ID', SECRET='API_KEY PASSWORD PIN', ID='ACCOUNT_NUMBER CREDIT_DEBIT_CARD CVV DRIVERS_LICENSE GOVERNMENT_ID IBAN LICENSE_PLATE MEDICAL_RECORD_NUMBER PASSPORT ROUTING_NUMBER SSN SWIFT_BIC TAX_ID', DATE='DATE_OF_BIRTH', ORG='COMPANY_NAME', OTHER='AGE DATE GENDER TIME')
BUILDERS = {'gretel-multi': gretel_multi, 'privy': privy, 'creddata': creddata, 'leak-museum': leak_museum, 'leaky-repo': leaky_repo, 'nym-en': nym_en, 'nym-multi': nym_multi}
META = {'gretel-multi': {'lang': 'multi', 'kind': 'pii', 'source': HF + 'gretelai/synthetic_pii_finance_multilingual', 'license': 'apache-2.0', 'mode': 'files', 'langs': {}, 'domain': 'finance documents in 7 languages: support tickets and rows with password, api_key, user_name, ipv4, ipv6', 'labels': {'en': ['person', 'first name', 'surname', 'company', 'street address', 'geo coordinates', 'email', 'phone number', 'date of birth', 'username', 'customer id', 'employee id', 'password', 'api key', 'pin code', 'ip address', 'bank account number', 'iban', 'swift bic code', 'bank routing number', 'social security number', 'passport number', 'driver license number', 'credit card number', 'card security code'], 'ru': ['имя человека', 'имя', 'фамилия', 'компания', 'адрес', 'координаты', 'электронная почта', 'номер телефона', 'дата рождения', 'логин', 'номер клиента', 'табельный номер сотрудника', 'пароль', 'API ключ', 'PIN код', 'IP адрес', 'номер банковского счёта', 'IBAN', 'SWIFT BIC', 'номер маршрутизации банка', 'SSN', 'номер паспорта', 'номер водительского удостоверения', 'номер кредитной карты', 'CVC код карты']}, 'groups': _g(PERSON='name first_name last_name', ORG='company', ADDRESS='street_address local_latlng', CONTACT='email phone_number', ACCOUNT='user_name customer_id employee_id', SECRET='password api_key account_pin', NET='ipv4 ipv6', DATE='date_of_birth', ID='iban bban swift_bic_code bank_routing_number ssn passport_number driver_license_number credit_card_number credit_card_security_code')}, 'privy': {'lang': 'en', 'kind': 'pii', 'source': HF + 'beki/privy', 'license': 'mit', 'mode': 'files', 'domain': 'JSON, SQL, XML and HTML payloads generated from OpenAPI specs; structured text, not prose', 'labels': {'en': ['person', 'location', 'geo coordinates', 'organization', 'email', 'phone number', 'url', 'ip address', 'mac address', 'password', 'credit card number', 'bank account number', 'iban', 'imei', 'passport number', 'driver license number', 'vehicle registration number', 'tax identification number', 'social security number'], 'ru': ['имя человека', 'адрес', 'координаты', 'организация', 'электронная почта', 'номер телефона', 'ссылка', 'IP адрес', 'MAC адрес', 'пароль', 'номер кредитной карты', 'номер банковского счёта', 'IBAN', 'IMEI', 'номер паспорта', 'номер водительского удостоверения', 'государственный номер автомобиля', 'ИНН', 'SSN']}, 'groups': PRIVY_G}, 'creddata': {'lang': 'en', 'kind': 'secrets', 'source': 'https://github.com/Samsung/CredData', 'license': "apache-2.0 (meta); file texts under their repositories' licenses", 'mode': 'link', 'domain': "real credentials in open source code: the marked line (or PEM block) as is, negatives are the same scanners' false positives and placeholders", 'rebuild': 'cd BENCH/raw/creddata && python download_data.py   # тянет файлы 297 репозиториев в data/, тексты чужих репозиториев в бенче не выкладываются', 'labels': SECRET_LABELS, 'groups': {}}, 'leak-museum': {'lang': 'en', 'kind': 'secrets', 'source': 'https://github.com/printemps-tokyo/leak-museum', 'license': 'mit', 'mode': 'files', 'domain': '27 exhibits of committed secrets: .env, k8s Secret, tfstate, .npmrc, .pgpass, HAR, keystore, .mcp.json; one row per text file, planted values from PLANTED.md', 'labels': SECRET_LABELS, 'groups': _g(SECRET='SECRET')}, 'leaky-repo': {'lang': 'en', 'kind': 'secrets', 'source': 'https://github.com/Plazmaz/leaky-repo', 'license': 'mit', 'mode': 'files', 'domain': 'a repo of mistakes: 44 config and dotfiles with leaked credentials, one row per file', 'labels': SECRET_LABELS, 'groups': _g(SECRET='SECRET')}, 'nym-en': {'lang': 'en', 'kind': 'pii', 'source': HF + 'Wismut/nym-pii-multilingual-data', 'license': 'mit', 'mode': 'files', 'domain': 'incidents and leaks, English rows: API_KEY, PASSWORD, USERNAME, MAC, 40 types', 'labels': NYM_LABELS, 'groups': NYM_GROUPS}, 'nym-multi': {'lang': 'multi', 'kind': 'pii', 'source': HF + 'Wismut/nym-pii-multilingual-data', 'license': 'mit', 'mode': 'files', 'langs': {}, 'domain': 'incidents and leaks, everything but Russian and English; language is a stopword and script heuristic, not a LID model', 'labels': NYM_LABELS, 'groups': NYM_GROUPS}}
if __name__ == '__main__':
    benchlib.main(BUILDERS, META)
    if SKIPPED_BINARY:
        print('Skipped binary files:', ', '.join(SKIPPED_BINARY))
