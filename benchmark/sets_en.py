import ast, csv, json, zipfile
import pyarrow.parquet as pq
from benchlib import RAW, find_all, pick
import benchlib
AMEAU = RAW / 'it-support-tickets'

def _ameau_fields(r):
    t = r['ticket']
    yield ('ticket.submitted_title', t['submitted_title'])
    yield ('ticket.submitted_description', t['submitted_description'])
    for i, c in enumerate(r['correspondence']):
        yield (f'correspondence[{i}].message', c['message'])
    d = r['diagnostics']
    yield ('diagnostics.summary', d['summary'])
    for i, e in enumerate(d['observed_errors']):
        yield (f'diagnostics.observed_errors[{i}]', e)
    for i, s in enumerate(d['steps']):
        for k in ('action', 'expected_result', 'observed_result', 'evidence'):
            yield (f'diagnostics.steps[{i}].{k}', s[k])
    yield ('root_cause', r['root_cause'])
    for i, s in enumerate(r['resolution']['steps']):
        yield (f'resolution.steps[{i}]', s)

def ameau01():
    pii = {t['ticket_id']: t['pii_instances'] for t in json.loads((AMEAU / 'pii.json').read_text())}
    ret = {t['ticket_id']: t['retain_instances'] for t in json.loads((AMEAU / 'retention.json').read_text())['tickets']}
    rows, pos, neg = ({}, [], [])
    for r in pq.read_table(AMEAU / 'train.parquet').to_pylist():
        tid = r['record_id']
        vals = {i['value'] for i in pii[tid]}
        for path, text in _ameau_fields(r):
            text, rid = (text or '', f'ameau-{tid}:{path}')
            mine = sorted((i for i in pii[tid] if path in i['occurrences']), key=lambda i: -len(i['value']))
            if mine:
                if any((i['value'] not in text for i in mine)):
                    continue
                pos.append(rid)
            elif any((v in text for v in vals)):
                continue
            elif not any((i['value'] in text for i in ret[tid])):
                continue
            else:
                neg.append(rid)
            rows[rid] = (path, text, mine)
    keep = set(pick('ameau01-pos', pos, 750)) | set(pick('ameau01-neg', neg, 750))
    for rid in sorted(keep):
        path, text, mine = rows[rid]
        seen, ents = ([], [])
        for i in mine:
            for a, b in find_all(text, i['value'], seen):
                ents.append({'start': a, 'end': b, 'type': i['type']})
        yield (rid, path.split('.')[0].split('[')[0], text, sorted(ents, key=lambda e: e['start']))

def tonicai():
    rows = {}
    for f in sorted((RAW / 'tonicai-privacy-bench' / 'ground_truth').glob('*_ground_truth_spans.jsonl')):
        for line in f.open():
            o = json.loads(line)
            rows[f"tnc-{o['meta']['row_id']}"] = o
    for rid in pick('tonicai', rows, 1500):
        o = rows[rid]
        for s in o['ground_truth_spans']:
            assert o['text'][s['start']:s['end']] == s['text'], (rid, s)
        yield (rid, 'slack' if 'thread_ts' in o['meta'] else 'email', o['text'], sorted(({'start': s['start'], 'end': s['end'], 'type': s['label']} for s in o['ground_truth_spans']), key=lambda e: e['start']))
KIJI_DROP = {'AGE', 'TITLE'}

def _kiji(name, langs, dom, k=1000):
    rows = {}
    for i, r in enumerate(pq.read_table(RAW / 'kiji' / 'data' / 'test-00000-of-00001.parquet').to_pylist()):
        if r['language'] in langs:
            rows[f'kiji-{i:04d}'] = r
    keep = pick(name, rows, k)
    _langs(name, [rows[i]['language'] for i in keep])
    for rid in keep:
        r = rows[rid]
        ents = []
        for e in r['privacy_mask']:
            assert r['text'][e['start']:e['end']] == e['value'], (rid, e)
            if e['label'] not in KIJI_DROP:
                ents.append({'start': e['start'], 'end': e['end'], 'type': e['label']})
        yield (rid, r[dom], r['text'], sorted(ents, key=lambda e: e['start']))

def _langs(name, langs):
    if 'langs' in META[name]:
        META[name]['langs'] = {k: langs.count(k) for k in sorted(set(langs))}

def kiji_en():
    return _kiji('kiji-en', ('English',), 'country')

def kiji_multi():
    return _kiji('kiji-multi', ('French', 'German', 'Spanish', 'Dutch', 'Danish'), 'language')

def arthur_passwords():
    with (RAW / 'arthur-passwords' / 'sensitive_data_password.csv').open(newline='') as fh:
        for i, r in enumerate(csv.DictReader(fh)):
            spans = ast.literal_eval(r['span_labels'])
            assert spans[0][0] == 0 and spans[-1][1] == len(r['text']), i
            yield (f'arth-{i:03d}', r['difficulty'], r['text'], [{'start': a, 'end': b, 'type': 'PASSWORD'} for a, b, lab in spans if lab.startswith('PASSWORD')])
NEMO_DROP = {'date', 'time', 'date_time', 'occupation', 'employment_status', 'education_level', 'race_ethnicity', 'language', 'gender', 'age', 'political_view', 'religious_belief', 'blood_type', 'sexuality'}

def nemotron_pii():
    f = pq.ParquetFile(RAW / 'nemotron-pii' / 'data' / 'test-00000-of-00001.parquet')
    keep = set(pick('nemotron-pii', [f'nemo-{i:06d}' for i in range(f.metadata.num_rows)], 1500))
    i = -1
    for batch in f.iter_batches(batch_size=2000, columns=['text', 'spans', 'document_format']):
        for r in batch.to_pylist():
            i += 1
            if f'nemo-{i:06d}' not in keep:
                continue
            ents = [e for e in ast.literal_eval(r['spans']) if e['label'] not in NEMO_DROP]
            if any((r['text'][e['start']:e['end']] != str(e['text']) for e in ents)):
                continue
            yield (f'nemo-{i:06d}', r['document_format'], r['text'], sorted(({'start': e['start'], 'end': e['end'], 'type': e['label']} for e in ents), key=lambda e: e['start']))

def tab_echr():
    with zipfile.ZipFile(RAW / 'tab-echr' / 'echr_test.zip') as z:
        docs = json.loads(z.read('echr_test.json'))
    per = {}
    for d in docs:
        if d['annotator_id'] in d['quality_checked']:
            per.setdefault(d['doc_id'], []).append(d)
    assert len(per) == len({d['doc_id'] for d in docs}), 'документ без проверенной разметки'
    for did in pick('tab-echr', per, 150):
        d = min(per[did], key=lambda x: x['annotator_id'])
        ents = []
        for m in d['entity_mentions']:
            assert d['text'][m['start_offset']:m['end_offset']] == m['span_text'], (did, m)
            if m['entity_type'] in TAB_KEEP:
                ents.append({'start': m['start_offset'], 'end': m['end_offset'], 'type': m['entity_type']})
        yield (f'tab-{did}', 'echr', d['text'], sorted(ents, key=lambda e: e['start']))
TAB_KEEP = {'PERSON', 'CODE', 'LOC', 'ORG'}
DPII_DROP = {'DATETIME', 'DATETIME_AGE', 'QUANTITY', 'PRODUCT', 'PROFESSION', 'PERSON_SOCIAL_RELATION', 'MISC'}

def _dialogpii(name, langs, k):
    rows = {}
    with zipfile.ZipFile(RAW / 'dialogpii' / 'DialogPII.zip') as z:
        for n in sorted((x for x in z.namelist() if '/transcripts/' in x and x.endswith('.json'))):
            o = json.loads(z.read(n))
            if o['language'] not in langs:
                continue
            for dl in o['dialogs']:
                text, ents = ('', [])
                for t in dl['dialog']['turns']:
                    text += ('\n' if text else '') + f"{t['speaker']}: "
                    for a in t['annotations']:
                        assert t['text'][a['start']:a['end']] == a['text'], (n, a)
                        if a['type'] not in DPII_DROP:
                            ents.append({'start': len(text) + a['start'], 'end': len(text) + a['end'], 'type': a['type']})
                    text += t['text']
                rows[f"dpii-{o['language']}-{o['scenario']}-{dl['chat_number']:03d}"] = (o['language'], o['scenario'], text, ents)
    keep = sorted((rid for lang in langs for rid in pick(f'{name}:{lang}', [i for i in rows if rows[i][0] == lang], k)))
    _langs(name, [rows[i][0] for i in keep])
    for rid in keep:
        _, dom, text, ents = rows[rid]
        yield (rid, dom, text, sorted(ents, key=lambda e: e['start']))

def dialogpii_en():
    return _dialogpii('dialogpii-en', ('EN',), 1000)

def dialogpii_multi():
    return _dialogpii('dialogpii-multi', ('AR', 'DE', 'FI', 'FR', 'HI', 'IT', 'PL', 'PT', 'SP', 'TR'), 50)
BUILDERS = {'ameau01': ameau01, 'tonicai': tonicai, 'kiji-en': kiji_en, 'kiji-multi': kiji_multi, 'arthur-passwords': arthur_passwords, 'nemotron-pii': nemotron_pii, 'tab-echr': tab_echr, 'dialogpii-en': dialogpii_en, 'dialogpii-multi': dialogpii_multi}
HF = 'https://huggingface.co/datasets/'

def _g(**groups):
    return {t: g for g, ts in groups.items() for t in ts.split()}
_KIJI_LABELS = {'en': ['first name', 'surname', 'city', 'street', 'building number', 'zip code', 'state', 'region', 'country', 'company name', 'organization', 'phone number', 'email', 'date of birth', 'url', 'domain', 'driver license number', 'social security number', 'security token', 'passport number', 'iban', 'password', 'national id number', 'license plate number', 'tax identification number', 'id card number', 'credit card number', 'username'], 'ru': ['имя', 'фамилия', 'город', 'улица', 'номер дома', 'почтовый индекс', 'штат', 'регион', 'страна', 'название компании', 'организация', 'номер телефона', 'электронная почта', 'дата рождения', 'ссылка', 'домен', 'номер водительского удостоверения', 'номер социального страхования', 'токен доступа', 'номер паспорта', 'IBAN', 'пароль', 'номер удостоверения личности', 'государственный номер автомобиля', 'ИНН', 'номер удостоверения личности', 'номер банковской карты', 'логин']}
_KIJI_GROUPS = _g(PERSON='FIRSTNAME SURNAME', ADDRESS='CITY STREET BUILDINGNUM BUILDNUM ZIP STATE REGION COUNTRY', ORG='COMPANYNAME ORGANIZATION', CONTACT='PHONENUMBER EMAIL', NET='URL DOMAIN', ACCOUNT='USERNAME', SECRET='PASSWORD SECURITYTOKEN', DATE='DATEOFBIRTH', ID='DRIVERLICENSENUM SSN PASSPORTID IBAN NATIONALID LICENSEPLATENUM TAXNUM IDCARDNUM CREDITCARDNUMBER')
_DPII_LABELS = {'en': ['person', 'email', 'phone number', 'identifier or document number', 'url', 'organization', 'city', 'street', 'house number', 'zip code', 'country', 'place'], 'ru': ['имя человека', 'электронная почта', 'номер телефона', 'номер документа или счёта', 'ссылка', 'организация', 'город', 'улица', 'номер дома', 'почтовый индекс', 'страна', 'место']}
_DPII_GROUPS = _g(PERSON='PERSON', CONTACT='PERSON_EMAIL CODE_PHONE', ID='CODE', NET='CODE_URL', ORG='ORG', ADDRESS='LOC_CITY LOC_STREET LOC_HOUSENUMBER LOC_ZIP LOC_COUNTRY LOC_OTHER')
META = {'ameau01': {'lang': 'en', 'kind': 'pii', 'source': HF + 'ameau01/synthetic-it-support-tickets', 'license': 'mit', 'mode': 'files', 'domain': 'ITSM incident fields: correspondence, diagnostics, resolution steps; negatives carry retained technical strings (app names, error codes, cert serials)', 'labels': {'en': ['person', 'username', 'hostname', 'ip address', 'employee id', 'email', 'phone number', 'office location'], 'ru': ['имя человека', 'логин', 'имя хоста', 'IP адрес', 'табельный номер сотрудника', 'электронная почта', 'номер телефона', 'город офиса']}, 'groups': _g(PERSON='person', ACCOUNT='username emp_id', NET='hostname ip', CONTACT='email phone', ADDRESS='location')}, 'tonicai': {'lang': 'en', 'kind': 'pii', 'source': HF + 'TonicAI/Privacy-Bench', 'license': 'cc-by-4.0', 'mode': 'files', 'domain': 'Slack and email exports of 21 personas; Slack handles <@U02CARLOS> are USERNAME', 'labels': {'en': ['first name', 'surname', 'email', 'username', 'organization'], 'ru': ['имя', 'фамилия', 'электронная почта', 'логин', 'организация']}, 'groups': _g(PERSON='NAME_GIVEN NAME_FAMILY', CONTACT='EMAIL_ADDRESS', ACCOUNT='USERNAME', ORG='ORGANIZATION')}, 'kiji-en': {'lang': 'en', 'kind': 'pii', 'source': HF + 'DataikuNLP/kiji-pii-training-data', 'license': 'apache-2.0', 'mode': 'files', 'domain': 'support requests, English slice of the test split, 26 types incl. SECURITYTOKEN', 'labels': _KIJI_LABELS, 'groups': _KIJI_GROUPS}, 'kiji-multi': {'lang': 'multi', 'kind': 'pii', 'source': HF + 'DataikuNLP/kiji-pii-training-data', 'license': 'apache-2.0', 'mode': 'files', 'langs': {}, 'domain': 'support requests, French, German, Spanish, Dutch and Danish slice of the test split', 'labels': _KIJI_LABELS, 'groups': _KIJI_GROUPS}, 'arthur-passwords': {'lang': 'en', 'kind': 'secrets', 'source': HF + 'Arthur-AI/arthur_sensitive_data_password', 'license': 'apache-2.0', 'mode': 'files', 'domain': 'passwords in prose, whole set: 294 rows with a password, 294 without', 'labels': {'en': ['password'], 'ru': ['пароль']}, 'groups': _g(SECRET='PASSWORD')}, 'nemotron-pii': {'lang': 'en', 'kind': 'pii', 'source': HF + 'nvidia/Nemotron-PII', 'license': 'cc-by-4.0', 'mode': 'files', 'domain': 'structured and unstructured documents of 29 industries, 41 PII types of 55', 'labels': {'en': ['first name', 'last name', 'email', 'url', 'phone number', 'fax number', 'username', 'customer id', 'employee id', 'password', 'api key', 'pin', 'http cookie', 'ip address', 'mac address', 'street address', 'city', 'county', 'state', 'postcode', 'country', 'coordinate', 'company name', 'date of birth', 'account number', 'bank routing number', 'swift bic', 'credit card number', 'card security code', 'social security number', 'tax identification number', 'national id number', 'medical record number', 'health plan beneficiary number', 'biometric identifier', 'certificate or license number', 'license plate number', 'vehicle identification number', 'device identifier', 'unique id'], 'ru': ['имя', 'фамилия', 'электронная почта', 'ссылка', 'номер телефона', 'номер факса', 'логин', 'номер клиента', 'табельный номер сотрудника', 'пароль', 'API ключ', 'PIN код', 'cookie', 'IP адрес', 'MAC адрес', 'адрес', 'город', 'округ', 'штат', 'почтовый индекс', 'страна', 'координаты', 'название компании', 'дата рождения', 'номер банковского счёта', 'код банка', 'SWIFT BIC', 'номер банковской карты', 'CVC код карты', 'номер социального страхования', 'ИНН', 'номер удостоверения личности', 'номер медицинской карты', 'номер полиса', 'биометрический идентификатор', 'номер лицензии', 'государственный номер автомобиля', 'VIN автомобиля', 'идентификатор устройства', 'уникальный идентификатор']}, 'groups': _g(PERSON='first_name last_name', CONTACT='email phone_number fax_number', NET='url ipv4 ipv6 mac_address', ACCOUNT='user_name customer_id employee_id', SECRET='password api_key pin http_cookie', ADDRESS='street_address city county state postcode country coordinate', ORG='company_name', DATE='date_of_birth', ID='account_number bank_routing_number swift_bic credit_debit_card cvv ssn tax_id national_id medical_record_number health_plan_beneficiary_number biometric_identifier certificate_license_number license_plate vehicle_identifier device_identifier unique_id')}, 'tab-echr': {'lang': 'en', 'kind': 'pii', 'source': HF + 'ildpil/text-anonymization-benchmark', 'license': 'mit', 'mode': 'files', 'domain': 'long ECHR court judgments, median 3.9k chars - the cut-long-text check', 'labels': {'en': ['person', 'identifier or document number', 'location', 'organization'], 'ru': ['имя человека', 'номер документа или счёта', 'место', 'организация']}, 'groups': _g(PERSON='PERSON', ID='CODE', ADDRESS='LOC', ORG='ORG')}, 'dialogpii-en': {'lang': 'en', 'kind': 'pii', 'source': 'https://zenodo.org/records/20863452', 'license': 'cc-by-4.0', 'mode': 'files', 'domain': 'English call transcripts of 8 scenarios, PII spread over the turns of one dialog', 'labels': _DPII_LABELS, 'groups': _DPII_GROUPS}, 'dialogpii-multi': {'lang': 'multi', 'kind': 'pii', 'source': 'https://zenodo.org/records/20863452', 'license': 'cc-by-4.0', 'mode': 'files', 'langs': {}, 'domain': 'call transcripts in 10 languages (no Russian), 50 dialogs per language, PII spread over the turns of one dialog', 'labels': _DPII_LABELS, 'groups': _DPII_GROUPS}}
if __name__ == '__main__':
    benchlib.main(BUILDERS, META)
