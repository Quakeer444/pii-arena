import collections, csv, functools, json, math, multiprocessing, os, random, re, statistics, sys, zlib
from pathlib import Path
try:
    import tomllib
except ImportError:
    import tomli as tomllib
sys.path.insert(0, str(Path(__file__).resolve().parent))
from benchlib import PROTOCOL, bench_sha256
ROOT = Path(os.environ.get('BENCHMARK_DATA', str(Path(__file__).resolve().parent.parent / '.local' / 'research'))).resolve()
BENCH, RESULTS = (ROOT / 'BENCH', ROOT / 'RESULTS')
CFG = tomllib.loads((Path(__file__).with_name('models.toml')).read_text())['models']
csv.field_size_limit(10 ** 7)
B = 1000
_WORD = re.compile('\\w+')
GROUPS = ('PERSON', 'ADDRESS', 'CONTACT', 'ID', 'NET', 'ACCOUNT', 'SECRET', 'ORG', 'DATE', 'OTHER')
LADDER = (0.5, 0.3, 0.2, 0.1)
THRESH = float(os.environ.get('THRESH', '0.5'))
UNKNOWN = collections.defaultdict(collections.Counter)
LINE_GRAN = set()
BAD_SPANS = collections.Counter()
LEGACY = collections.defaultdict(set)
ONNX_CUDA = set()
NO_QUANT = '-'
_MAP = {'PERSON': ['private_person', 'person', 'name', 'first name', 'last name', 'surname', 'middle name', 'nickname', 'имя человека', 'имя', 'фамилия', 'отчество', 'ник', 'имя пользователя', 'FIRSTNAME', 'LASTNAME', 'MIDDLENAME', 'PREFIX', 'first_name', 'last_name', 'middle_name', 'PER', 'PERSON', 'ФИО', 'Имя держателя карты'], 'ADDRESS': ['private_address', 'address', 'city', 'street', 'building number', 'house number', 'zip code', 'postal code', 'country', 'region', 'district', 'state', 'county', 'secondary address', 'geolocation', 'place of birth', 'адрес', 'город', 'улица', 'номер дома', 'почтовый индекс', 'страна', 'регион', 'район', 'STREET', 'BUILDINGNUMBER', 'CITY', 'COUNTY', 'STATE', 'ZIPCODE', 'SECONDARYADDRESS', 'street_address', 'postcode', 'coordinate', 'ADDRESS', 'LOCATION', 'Полный адрес', 'Место рождения'], 'CONTACT': ['private_phone', 'private_email', 'phone', 'phone number', 'email', 'e-mail', 'fax number', 'telegram', 'handle', 'номер телефона', 'электронная почта', 'номер факса', 'PHONE', 'PHONE_NUMBER', 'PHONE_RF', 'EMAIL', 'EMAIL_ADDRESS', 'phone_number', 'fax_number', 'Номер телефона', 'Email'], 'NET': ['ip_address', 'private_url', 'ip', 'ip address', 'url', 'link', 'mac address', 'hostname', 'host name', 'domain', 'domain name', 'IP адрес', 'ссылка', 'MAC адрес', 'домен', 'имя хоста', 'IPADDRESS', 'IP_ADDRESS', 'MACADDRESS', 'MAC_ADDRESS', 'DOMAIN_NAME', 'URL', 'ipv4', 'ipv6', 'mac', 'mac_address'], 'ACCOUNT': ['username', 'login', 'user name', 'employee id', 'customer id', 'account name', 'emp', 'логин', 'табельный номер сотрудника', 'номер клиента', 'USERNAME', 'ACCOUNTNAME', 'user_name', 'employee_id', 'customer_id'], 'SECRET': ['secret', 'password', 'api key', 'api key or token', 'access token', 'token', 'private key', 'pin', 'pin code', 'credentials', 'one-time code', 'секрет', 'пароль', 'API ключ', 'API ключ или токен', 'токен доступа', 'приватный ключ', 'PIN код', 'одноразовый код', 'PASSWORD', 'PIN', 'api_key', 'http_cookie', 'Пароли', 'API ключи', 'Одноразовые коды', 'Кодовые слова'], 'ORG': ['org', 'organization', 'company name', 'company', 'организация', 'название компании', 'ORG', 'ORGANIZATION', 'COMPANY_NAME', 'company_name', 'Наименование банка'], 'DATE': ['date of birth', 'дата рождения', 'DATEOFBIRTH', 'DATE_OF_BIRTH', 'date_of_birth', 'Дата рождения'], 'ID': ['account_number', 'payment_card', 'iban', 'id_card_number', 'social_number', 'tax_number', 'driver_license_number', 'personal_id', 'vehicle_plate', 'ru_inn', 'ru_snils', 'ru_kpp', 'ru_ogrn', 'ru_passport', 'ru_bank_account', 'ru_bik', 'ru_drv_license', 'ru_osago', 'ru_sts', 'ru_vin', 'passport', 'snils', 'inn', 'card', 'ogrn', 'ogrnip', 'kpp', 'bik', 'account', 'passport number', 'tax identification number', 'social insurance number', 'tax registration code', 'company registration number', 'individual entrepreneur registration number', 'bank card number', 'card security code', 'bank account number', 'id card number', 'social security number', 'credit card number', 'driver license number', 'medical insurance number', 'military id number', 'birth certificate number', 'vehicle registration number', 'national id', 'license plate', 'номер паспорта', 'ИНН', 'СНИЛС', 'КПП', 'ОГРН', 'ОГРНИП', 'номер банковской карты', 'CVC код карты', 'номер банковского счёта', 'номер удостоверения личности', 'номер кредитной карты', 'номер водительского удостоверения', 'номер полиса ОМС', 'номер военного билета', 'номер свидетельства о рождении', 'номер документа', 'государственный номер автомобиля', 'SSN', 'CREDITCARD', 'CVV', 'IBAN', 'BIC', 'BANKACCOUNT', 'IMEI', 'VRM', 'VIN', 'MASKEDNUMBER', 'BITCOINADDRESS', 'ETHEREUMADDRESS', 'LITECOINADDRESS', 'ssn', 'tax_id', 'credit_debit_card', 'cvv', 'national_id', 'bank_routing_number', 'certificate_license_number', 'license_plate', 'unique_id', 'swift_bic', 'medical_record_number', 'health_plan_beneficiary_number', 'device_identifier', 'vehicle_identifier', 'biometric_identifier', 'BANK_ACCOUNT', 'PASSPORT', 'OGRN', 'OGRNIP', 'INN', 'INN_RU', 'SNILS', 'KPP', 'CARD', 'PASSPORT_RF', 'BANK_ACCOUNT_RF', 'CREDIT_CARD', 'IBAN_CODE', 'US_SSN', 'US_PASSPORT', 'US_DRIVER_LICENSE', 'US_BANK_NUMBER', 'UK_NHS', 'MEDICAL_LICENSE', 'NRP', 'CRYPTO', 'CVV/CVC', 'Водительское удостоверение', 'Данные об автомобиле клиента', 'Данные об организации/юридическом лице (ИНН, КПП, ОГРН, БИК, адреса, расчётный счёт)', 'Номер банковского счета', 'Номер карты', 'СНИЛС клиента', 'Сведения об ИНН', 'Паспортные данные', 'Содержимое магнитной полосы', 'Свидетельство о рождении', 'Серия и номер вида на жительство', 'Временное удостоверение личности', 'Разрешение на работу / визу', 'Дата окончания срока действия карты'], 'OTHER': ['other_pii', 'private_date', 'date', 'time', 'age', 'gender', 'sex', 'occupation', 'job title', 'position', 'PII', 'DATE', 'TIME', 'AGE', 'GENDER', 'SEX', 'POSITION', 'CASE_NUMBER', 'DATE_TIME', 'OCCUPATION', 'JOBTITLE', 'JOBDEPARTMENT', 'EYECOLOR', 'HEIGHT', 'ORDINALDIRECTION', 'USERAGENT', 'AMOUNT', 'CURRENCY', 'CURRENCYCODE', 'CURRENCYNAME', 'CURRENCYSYMBOL', 'CREDITCARDISSUER', 'GPSCOORDINATES', 'date_time', 'education_level', 'employment_status', 'language', 'political_view', 'race_ethnicity', 'religious_belief', 'sexuality', 'Гражданство и названия стран', 'Дата регистрации по месту жительства или пребывания']}
PRED_G = {lab: g for g, labs in _MAP.items() for lab in labs}

@functools.cache
def meta_of(bench):
    f = BENCH / bench / 'meta.json'
    if not f.exists():
        sys.exit(f'{f}: missing meta.json: required for gold groups and report cuts')
    meta = json.loads(f.read_text())
    # T06: a dataset is validated where it is read. An unusable meta used to
    # surface much later as an ungrouped label or a wrong report cut.
    if meta.get('lang') not in ('ru', 'en', 'multi') or meta.get('kind') not in ('pii', 'secrets'):
        sys.exit(f"{f}: lang must be one of ru/en/multi and kind one of pii/secrets, got {meta.get('lang')!r}/{meta.get('kind')!r}")
    groups = meta.get('groups')
    if not isinstance(groups, dict) or not groups or not all(isinstance(k, str) and k and isinstance(v, str) and v for k, v in groups.items()):
        sys.exit(f'{f}: groups must map every label to a non-empty group name')
    return meta

def check_gold(f, rid, text, raw):
    """T06: validate the raw annotation of a corpus CSV before normalization.

    `norm` drops a span it cannot use, so an empty or out-of-range annotation
    used to leave the denominator instead of stopping the run: the row is
    named here instead. Labels unknown to the dataset `groups` are not an
    error - they are counted as OTHER and reported by the scorer."""
    try:
        entities = json.loads(raw)
    except ValueError as error:
        sys.exit(f'{f}: row {rid!r}: entities is not valid JSON: {error}')
    if not isinstance(entities, list):
        sys.exit(f'{f}: row {rid!r}: entities must be a list of annotation objects')
    for e in entities:
        a, b = (e.get('start'), e.get('end')) if isinstance(e, dict) else (None, None)
        if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, int) or not isinstance(b, int):
            sys.exit(f'{f}: row {rid!r}: annotation offsets must be integers: {e!r}')
        if not 0 <= a < b <= len(text):
            sys.exit(f'{f}: row {rid!r}: annotation [{a},{b}) is empty or outside the {len(text)}-character text: {e!r}')
        if not isinstance(e.get('type'), str) or not e['type']:
            sys.exit(f'{f}: row {rid!r}: annotation type must be a non-empty string: {e!r}')
    return entities

@functools.cache
def gold(bench):
    out, dom = ({}, {})
    source = BENCH / bench / 'bench.csv'
    for r in csv.DictReader(source.open(newline='')):
        if r['id'] in out:
            sys.exit(f"{source}: duplicate row id {r['id']!r}")
        out[r['id']] = (r['text'], check_gold(source, r['id'], r['text'], r['entities']))
        dom[r['id']] = r.get('domain', '')
    return (out, dom)

@functools.cache
def gold_norm(bench):
    return {rid: norm(t, e, 'type') for rid, (t, e) in gold(bench)[0].items()}

@functools.cache
def chars_of(bench, limit=0):
    texts = [t for t, _ in gold(bench)[0].values()]
    return sum((len(t) for t in (texts[:limit] if limit else texts)))

def norm(text, spans, key, bad=None):
    words = [m.span() for m in _WORD.finditer(text)]
    out = []
    for sp in spans:
        a, b = (sp['start'], sp['end'])
        if not 0 <= a < b <= len(text):
            if bad is not None:
                bad[0] += 1
            continue
        while a < b and text[a].isspace():
            a += 1
        while b > a and text[b - 1].isspace():
            b -= 1
        if a >= b:
            continue
        for wa, wb in words:
            if wa < b and wb > a:
                a, b = (min(a, wa), max(b, wb))
        out.append([a, b, sp[key]])
    out.sort()
    merged = []
    for a, b, lab in out:
        if merged and lab == merged[-1][2] and (a - merged[-1][1] <= 1):
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b, lab])
    return [tuple(x) for x in merged]

def keep(spans, thr=None):
    t = THRESH if thr is None else thr
    return [s for s in spans if s.get('score') is None or s['score'] >= t]

def chars(spans, grp=None):
    s = set()
    for a, b, lab in spans:
        g = grp(lab) if grp else None
        s |= {(p, g) if grp else p for p in range(a, b)}
    return s

def prf(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    return (p, r, 2 * p * r / (p + r) if p + r else 0.0)

def read_pred(f):
    meta, pred = ({}, {})
    for n, line in enumerate(Path(f).open(), 1):
        o = json.loads(line)
        if 'meta' in o:
            if meta or pred:
                sys.exit(f'{f}: line {n}: the metadata record must come first and be the only one')
            meta = o['meta']
            if not isinstance(meta, dict) or not meta:
                sys.exit(f'{f}: line {n}: the metadata record must be a non-empty object')
        elif not isinstance(o.get('id'), str):
            sys.exit(f"{f}: line {n}: prediction row without a string id")
        elif o['id'] in pred:
            sys.exit(f"{f}: row {o['id']} was written twice")
        else:
            spans = o.get('spans')
            if not isinstance(spans, list):
                sys.exit(f"{f}: row {o['id']} has no spans list")
            for s in spans:
                for k in ('start', 'end'):
                    if isinstance(s.get(k), bool) or not isinstance(s.get(k), int):
                        sys.exit(f"{f}: row {o['id']}: span {k} is not an integer")
                if not isinstance(s.get('label'), str):
                    sys.exit(f"{f}: row {o['id']}: span label is not a string")
                if (sc := s.get('score')) is not None and (isinstance(sc, bool) or not isinstance(sc, (int, float)) or not math.isfinite(sc)):
                    sys.exit(f"{f}: row {o['id']}: span score is not a finite number")
            pred[o['id']] = o
    if not meta:
        sys.exit(f'{f}: no metadata record')
    return (meta, pred)

def base_of(name):
    return name.split('+')[0]

@functools.cache
def _canon(bench):
    base = meta_of(bench).get('base') or bench
    if not (BENCH / base / 'bench.csv').exists():
        base = bench
    first = {}
    return (base, {rid: first.setdefault(text, rid) for rid, (text, _) in sorted(gold(base)[0].items())})

def fold(bench, rid):
    base, canon = _canon(bench)
    return 'test' if zlib.crc32(f'{base}:{canon.get(rid, rid)}'.encode()) & 1 else 'dev'

@functools.cache
def dirty(model):
    cfg = CFG.get(base_of(model), {})
    named = set(cfg.get('contaminated', []))
    for c in CFG.values():
        if cfg.get('repo') and c.get('repo') == cfg['repo']:
            named |= set(c.get('contaminated', []))
    srcs = {meta_of(b)['source'] for b in named if (BENCH / b / 'meta.json').exists()}
    return named | {d.name for d in BENCH.iterdir() if (d / 'meta.json').exists() and meta_of(d.name)['source'] in srcs}

def check_data(f, meta, expected=None):
    b = meta.get('bench')
    if not b or Path(b).name != b or not (BENCH / b / 'bench.csv').exists():
        return f'{f}: prediction metadata does not identify an available dataset'
    if expected is not None and b != expected:
        return f'{f}: run was made on dataset {b!r}, expected {expected!r}'
    if meta.get('protocol') not in (None, PROTOCOL):
        return f"{f}: run protocol {meta['protocol']}, current {PROTOCOL}"
    if meta.get('bench_sha256'):
        if meta['bench_sha256'] != bench_sha256(BENCH / b / 'bench.csv'):
            return f'{f}: computed from another dataset version: {b} (dataset fingerprint mismatch)'
    total = len(gold(b)[0])
    # A limit larger than the dataset produced the whole slice; compare against
    # what the run actually contains, not against the limit itself.
    limit = min(meta['limit'], total) if isinstance(meta.get('limit'), int) and meta['limit'] > 0 else (meta.get('limit') or 0)
    want_rows = limit or total
    chars = chars_of(b, limit)
    if meta.get('rows') is not None and meta['rows'] != want_rows:
        return f"{f}: rows in run {meta['rows']}, in dataset {want_rows}"
    if meta.get('chars') is not None and meta['chars'] != chars:
        return f"{f}: characters in run {meta['chars']}, in dataset {chars} - dataset text changed"
    return ''

def check_predictions(f, meta, pred, complete=False, expected=None, expected_model=None):
    if bad := check_data(f, meta, expected):
        return bad
    if expected_model is not None:
        got = meta.get('name', '') + ('+' + meta['variant'] if meta.get('variant') else '')
        if got != expected_model:
            return f"{f}: run metadata identifies {got!r}, expected {expected_model!r}"
    if complete and meta.get('limit'):
        return f'{f}: partial run cannot be used for quality'
    ids = list(gold(meta['bench'])[0])
    limit = meta.get('limit')
    expected_ids = set(ids if complete or not limit else ids[:min(limit, len(ids))])
    missing, extra = (expected_ids - set(pred), set(pred) - expected_ids)
    errs = [o for o in pred.values() if o.get('err')]
    if missing or extra or errs:
        msg = f'{f}: missing {len(missing)}, extra {len(extra)}, err {len(errs)}'
        if errs:
            msg += f", example: {errs[0]['err'][:120]}"
        return msg
    return ''


def quality_preds(bench):
    out, stale = ([], [])
    for f in sorted((RESULTS / bench).glob('pred.*.jsonl')):
        meta, pred = read_pred(f)
        if (bad := check_predictions(f, meta, pred, complete=not meta.get('limit'), expected=bench, expected_model=f.stem[5:])):
            stale.append(bad)
        elif not meta.get('limit'):
            if not meta.get('protocol') or not meta.get('bench_sha256'):
                LEGACY[bench].add(f.stem[5:])
            out.append(f)
    if stale and (not os.environ.get('ALLOW_STALE')):
        sys.exit('\n'.join(['incompatible predictions; rerun these files:', *stale]))
    for s in stale:
        print('!', s)
    return out

def load_model(f, g, gg):
    meta, pred = read_pred(f)
    name = Path(f).stem[5:]
    if msg := check_predictions(f, meta, pred, complete=True, expected=Path(f).parent.name, expected_model=name):
        if not os.environ.get('ALLOW_ERR'):
            sys.exit(msg)
        print('!', msg)
    ids = sorted(g)
    st = {'tp': [], 'fp': [], 'fn': [], 'ttp': [], 'tfp': [], 'tfn': [], 'etp': [], 'efp': [], 'efn': [], 'otp': [], 'ofp': [], 'ofn': [], 'hid': [], 'ng': [], 'neg_fire': 0, 'neg_chars': 0}
    rec = collections.defaultdict(lambda: [0, 0])
    miss_g = collections.defaultdict(lambda: [0, 0])
    scored = False
    ms = []
    bad = [0]
    for rid in ids:
        text, gents = g[rid]
        o = pred.get(rid, {'spans': []})
        scored = scored or any((s.get('score') is not None for s in o['spans']))
        gs, ps = (norm(text, gents, 'type'), norm(text, keep(o['spans']), 'label', bad))
        for _, _, lab in ps:
            if lab not in PRED_G:
                UNKNOWN[lab][name] += 1
        gc, pc = (chars(gs), chars(ps))
        st['tp'].append(len(gc & pc))
        st['fp'].append(len(pc - gc))
        st['fn'].append(len(gc - pc))
        gt, pt = (chars(gs, lambda t: gg.get(t, 'OTHER')), chars(ps, lambda lab: PRED_G.get(lab, 'OTHER')))
        st['ttp'].append(len(gt & pt))
        st['tfp'].append(len(pt - gt))
        st['tfn'].append(len(gt - pt))
        ge, pe = ([(a, b) for a, b, _ in gs], {(a, b) for a, b, _ in ps})
        exact = sum((1 for x in ge if x in pe))
        st['etp'].append(exact)
        st['efn'].append(len(ge) - exact)
        st['efp'].append(len(pe - set(ge)))
        hit = sum((1 for a, b in ge if any((x < b and y > a for x, y in pe))))
        st['otp'].append(hit)
        st['ofn'].append(len(ge) - hit)
        st['ofp'].append(sum((1 for x, y in pe if not any((x < b and y > a for a, b in ge)))))
        st['hid'].append(sum((1 for a, b in ge if all((p in pc for p in range(a, b))))))
        st['ng'].append(len(ge))
        for a, b, t in gs:
            rec[t][0] += len(set(range(a, b)) & pc)
            rec[t][1] += b - a
            grp = miss_g[gg.get(t, 'OTHER')]
            grp[0] += not any((x < b and y > a for x, y in pe))
            grp[1] += 1
        if not gents:
            st['neg_fire'] += bool(pc)
            st['neg_chars'] += len(pc)
        if 'ms' in o:
            ms.append(o['ms'])
    if meta.get('granularity') == 'line':
        LINE_GRAN.add(name)
    BAD_SPANS[name] += bad[0]
    st['bad'] = bad[0]
    st['rec'] = {t: v[0] / v[1] for t, v in rec.items()}
    st['miss_g'] = dict(miss_g)
    st['scored'] = scored
    st['ms'] = statistics.median(ms) if ms else None
    st['meta'] = meta
    st['ids'] = ids
    return (name, st)

def missed_at(g, f, thr):
    _, pred = read_pred(f)
    miss = 0
    for rid, (text, gents) in g.items():
        pe = [(a, b) for a, b, _ in norm(text, keep(pred.get(rid, {'spans': []})['spans'], thr), 'label')]
        for a, b, _ in norm(text, gents, 'type'):
            miss += not any((x < b and y > a for x, y in pe))
    return miss

def f1_of(st, idx, k=''):
    tp, fp, fn = (st[k + 'tp'], st[k + 'fp'], st[k + 'fn'])
    return prf(sum(map(tp.__getitem__, idx)), sum(map(fp.__getitem__, idx)), sum(map(fn.__getitem__, idx)))[2]

def bootstrap(models, n):
    rng = random.Random(0)
    f1s, miss = ({m: [] for m in models}, {m: [] for m in models})
    for _ in range(B):
        idx = rng.choices(range(n), k=n)
        for m, st in models.items():
            f1s[m].append(f1_of(st, idx))
            ng = sum(map(st['ng'].__getitem__, idx))
            miss[m].append(sum(map(st['ofn'].__getitem__, idx)) / ng if ng else 0.0)
    return (f1s, miss)

def ties(order, bmiss):
    out = []
    for a, b in zip(order, order[1:]):
        lo, hi = ci([x - y for x, y in zip(bmiss[a], bmiss[b])])
        if lo <= 0 <= hi:
            out.append(f'{a} ≈ {b}')
    return out

def ci(vals):
    v = sorted(vals)
    return (v[int(B * 0.025)], v[int(B * 0.975)])

def fmt_params(n):
    if not n:
        return '-'
    return f'{n / 1000000000.0:.1f}B' if n >= 1000000000.0 else f'{n / 1000000.0:.0f}M'

def pct(part, whole):
    return f'{part / whole:.1%}' if whole else '-'

def score(bench):
    g, dom = gold(bench)
    mj = meta_of(bench)
    gg = mj['groups']
    n = len(g)
    files = {Path(f).stem[5:]: f for f in quality_preds(bench)}
    models = dict((load_model(f, g, gg) for f in files.values()))
    if not models:
        return {}
    print(f'[{bench}] {len(models)} models, bootstrap {B}x{n}...', flush=True)
    boots, bmiss = bootstrap(models, n)
    full = list(range(n))
    point = {m: f1_of(st, full) for m, st in models.items()}
    nspans = sum((len(v) for v in gold_norm(bench).values()))
    missed = {m: sum(st['ofn']) for m, st in models.items()}
    hidden = {m: sum(st['hid']) for m, st in models.items()}
    order = sorted(models, key=lambda m: (missed[m], -point[m]))
    pairs = ties(order, bmiss)
    nneg = sum((1 for _, e in g.values() if not e))
    gchars = sum((len(chars(v)) for v in gold_norm(bench).values()))
    tchars = sum((len(t) for t, _ in g.values()))
    lines = [f"# BENCH/{bench} - {mj['lang']} / {mj['kind']} ({n} rows, {nspans} spans, {nneg} negatives)", '', f'Main metric: **missed** - gold spans no predicted character touched. Score threshold {THRESH:g}; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P {gchars / tchars:.3f} ({1 - gchars / tchars:.1%} of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.', '', '| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    summary = {}
    for m in order:
        st = models[m]
        P, R, F = prf(sum(st['tp']), sum(st['fp']), sum(st['fn']))
        lo, hi = ci(boots[m])
        mlo, mhi = ci(bmiss[m])
        eF, oF, tF = (f1_of(st, full, 'e'), f1_of(st, full, 'o'), f1_of(st, full, 't'))
        train = 'train' if bench in dirty(m) else ''
        ms = f"{st['ms']:.0f}" if st['ms'] is not None else '-'
        lines.append(f"| {m} | **{missed[m]}** | {pct(missed[m], nspans)} [{mlo:.1%}, {mhi:.1%}] | {pct(hidden[m], nspans)} | {F:.3f} [{lo:.3f}, {hi:.3f}] | {P:.3f} | {R:.3f} | {eF:.3f} | {oF:.3f} | {tF:.3f} | {st['neg_fire']}/{nneg} | {st['neg_chars']} | {st['bad']} | {ms} | {fmt_params(st['meta'].get('params'))} | {train} |")
        summary[m] = {'missed': missed[m], 'spans': nspans, 'mlo': mlo, 'mhi': mhi, 'hidden': hidden[m], 'f1': F, 'lo': lo, 'hi': hi, 'tp': sum(st['tp']), 'fp': sum(st['fp']), 'fn': sum(st['fn']), 'fire': st['neg_fire'], 'nneg': nneg, 'negchars': st['neg_chars'], 'train': bool(train)}
    lines += ['', 'Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: ' + ('; '.join(pairs) or 'all neighbours differ'), '']
    if (leg := sorted(LEGACY[bench] & set(models))):
        lines += [f"Legacy runs on this set: {', '.join(leg)}. Their meta carries no `protocol` and no `bench_sha256`, so the version of the text they were taken from is confirmed only by the row and character counts, not by a fingerprint.", '']
    line_g = sorted(LINE_GRAN & set(models))
    if line_g:
        lines += [f"{', '.join(line_g)} mark a whole line at a time (`granularity` in the meta line), so their char P / R / F1 and entity exact are not comparable with the rest; their missed count is.", '']
    gs = [x for x in GROUPS if any((x in st['miss_g'] for st in models.values()))]
    lines += ['## Missed by group', '', '| model | ' + ' | '.join(gs) + ' |', '|---|' + '---|' * len(gs), '| spans in gold | ' + ' | '.join((str(models[order[0]]['miss_g'].get(x, [0, 0])[1]) for x in gs)) + ' |']
    for m in order:
        cells = []
        for x in gs:
            miss, tot = models[m]['miss_g'].get(x, (0, 0))
            cells.append(f'{miss} ({pct(miss, tot)})' if tot else '-')
        lines.append(f'| {m} | ' + ' | '.join(cells) + ' |')
    types = sorted({t for st in models.values() for t in st['rec']})
    lines += ['', '## Char recall by gold type', '', '| type | group | ' + ' | '.join(order) + ' |', '|---|---|' + '---|' * len(order)]
    for t in types:
        lines.append(f"| {t} | {gg.get(t, 'OTHER')} | " + ' | '.join((f"{models[m]['rec'].get(t, 0):.3f}" for m in order)) + ' |')
    doms = sorted({d for d in dom.values() if d})
    if doms:
        ids = models[order[0]]['ids']
        lines += ['', '## char F1 by domain', '', '| domain | n | ' + ' | '.join(order) + ' |', '|---|---|' + '---|' * len(order)]
        for d in doms:
            idx = [i for i, rid in enumerate(ids) if dom[rid] == d]
            lines.append(f'| {d} | {len(idx)} | ' + ' | '.join((f'{f1_of(models[m], idx):.3f}' for m in order)) + ' |')
    scored = [m for m in order if models[m]['scored']]
    if scored:
        lines += ['', '## Missed at thresholds ' + ' / '.join((f'{t:g}' for t in LADDER)), '', 'Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.', '', '| model | ' + ' | '.join((f'{t:g}' for t in LADDER)) + ' |', '|---|' + '---|' * len(LADDER)]
        for m in scored:
            cells = [f'{(k := missed_at(g, files[m], t))} ({pct(k, nspans)})' for t in LADDER]
            lines.append(f'| {m} | ' + ' | '.join(cells) + ' |')
    lines += ['', 'Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.']
    (RESULTS / bench / 'REPORT.md').write_text('\n'.join(lines) + '\n')
    return summary

def quant_of(meta):
    q = meta.get('quant') or NO_QUANT
    return NO_QUANT if q in ('none', 'n/a') else q

def speed_runs(benches):
    runs = collections.defaultdict(lambda: {'chars': 0, 'rows': 0, 'secs': 0.0, 'sets': 0, 'ms': [], 'rss': 0.0})
    for b in benches:
        for f in sorted((RESULTS / b).glob('pred.*.jsonl')):
            meta, pred = read_pred(f)
            if not meta.get('elapsed_s'):
                continue
            if meta.get('family') == 'onnx' and meta.get('device') == 'cuda':
                ONNX_CUDA.add(f.stem[5:])
                continue
            hw = meta.get('gpu') or (meta.get('cpu') if meta.get('device') == 'cpu' else None) or '-'
            key = (f.stem[5:], meta.get('device') or '?', hw, str(meta.get('threads') or '-'), str(meta.get('workers') or '-'), quant_of(meta), meta.get('variant') or '-')
            r = runs[key]
            r['chars'] += meta.get('chars') or chars_of(b, meta.get('limit') or 0)
            r['rows'] += meta.get('rows') or 0
            r['secs'] += meta['elapsed_s']
            r['sets'] += 1
            r['rss'] = max(r['rss'], meta.get('rss_mb') or 0.0)
            r['ms'] += [o['ms'] for o in pred.values() if o.get('ms') is not None]
    out = []
    for k, v in runs.items():
        ms = sorted(v['ms'])
        out.append({'name': k[0], 'dev': k[1], 'hw': k[2], 'thr': k[3], 'w': k[4], 'quant': k[5], 'var': k[6], 'rss': f"{v['rss']:.0f}" if v['rss'] else '-', 'machine': (k[1], k[2], k[3], k[4]), 'chars': v['chars'], 'secs': v['secs'], 'cps': v['chars'] / v['secs'], 'rps': v['rows'] / v['secs'], 'sets': v['sets'], 'p50': ms[len(ms) // 2] if ms else None, 'p95': ms[int(len(ms) * 0.95)] if ms else None})
    return out

def speed_of(device, benches):
    tot = collections.defaultdict(lambda: [0, 0.0])
    for x in speed_runs(benches):
        if x['dev'] != device or x['quant'] != NO_QUANT:
            continue
        t = tot[x['machine'], x['name']]
        t[0] += x['chars']
        t[1] += x['secs']
    per = collections.defaultdict(dict)
    for (mach, name), (c, s) in tot.items():
        if s:
            per[mach][name] = c / s
    return dict(per)

def speed(benches):
    rows = speed_runs(benches)
    if not rows:
        return rows
    base = {(x['machine'], x['var'], x['quant']): x['cps'] for x in rows if base_of(x['name']) == 'pplx'}
    out = ['# Speed', '', 'Chars/s = chars / elapsed_s pooled over the sets of the run, rows/s the same way. `chars` comes from the meta line of the prediction file, or is counted from `bench.csv` for older runs. `x pplx` is the speed relative to the `pplx` run made under the same conditions - same machine (device + gpu or cpu model + threads + W), same cutting variant, same quantization; a row with no such pplx run carries `-`. `gpu / cpu` names the accelerator or, on CPU, the processor model (older files carry `-` and fall into one machine). `W` is how many run.py processes shared the node (`meta.workers`): every number here is batch throughput under that load, not the latency of one request - that takes a separate W=1, batch=1 run. Amortized ms/row p50 / p95 are quantiles of the per-row share of measured compute, not individually timed request latency: for model runs the batch time is divided across the pieces of the row and summed over its pieces, for scanners the whole run time is divided by the row count, so every row of a scanner run carries the same value. Timing boundaries differ between the paths: model timing covers the inference loop only (model load, text preparation, normalization and chunk-list construction happen outside `elapsed_s`), scanner timing includes process start and the whole scan. `rss MB` is the largest peak among the runs pooled into the row. Partial runs (`meta.limit`) are here but not in the quality tables.', '']
    if ONNX_CUDA:
        out += [f"Left out: {', '.join(sorted(ONNX_CUDA))} - onnx runs whose meta says `cuda`. The graph always goes through `CPUExecutionProvider`, so the run was CPU-bound while the meta names a GPU and no processor: there is no machine to attribute the speed to. Their quality numbers stay in the reports.", '']
    for dev in sorted({x['dev'] for x in rows}):
        part = sorted((x for x in rows if x['dev'] == dev), key=lambda x: (x['machine'], -x['cps']))
        out += [f'## {dev}', '', '| model | chars/s | rows/s | x pplx | amortized ms/row p50 | p95 | gpu / cpu | threads | W | quant | variant | rss MB | sets |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
        for x in part:
            bs = base.get((x['machine'], x['var'], x['quant']))
            rel = f"{x['cps'] / bs:.2f}" if bs else '-'
            p50 = f"{x['p50']:.0f}" if x['p50'] is not None else '-'
            p95 = f"{x['p95']:.0f}" if x['p95'] is not None else '-'
            out.append(f"| {x['name']} | {x['cps']:.0f} | {x['rps']:.2f} | {rel} | {p50} | {p95} | {x['hw']} | {x['thr']} | {x['w']} | {x['quant']} | {x['var']} | {x['rss']} | {x['sets']} |")
        out.append('')
    (RESULTS / 'SPEED.md').write_text('\n'.join(out) + '\n')
    return rows
QUANT_SUF = '+cpu-int8'

def quant_pairs(benches, data, rows):
    agg = collections.defaultdict(lambda: {'sets': 0, 'spans': 0, 'a': 0, 'q': 0, 'over': True})
    for b in benches:
        for m in data[b]:
            if not m.endswith(QUANT_SUF) or (base := m[:-len(QUANT_SUF)]) not in data[b]:
                continue
            x, y = (data[b][base], data[b][m])
            if x['train'] or y['train']:
                continue
            r = agg[base]
            r['sets'] += 1
            r['spans'] += x['spans']
            r['a'] += x['missed']
            r['q'] += y['missed']
            r['over'] &= x['mlo'] <= y['mhi'] and y['mlo'] <= x['mhi']
    if not agg:
        return []
    cps = {}
    for x in rows:
        for suf, kind in ((QUANT_SUF, 'int8'), ('+cpu-speed', 'fp32')):
            if x['dev'] == 'cpu' and x['name'].endswith(suf):
                cps[x['name'][:-len(suf)], x['machine'], kind] = x['cps']
    fast = {n: v / f for (n, mach, k), v in cps.items() if k == 'int8' and (f := cps.get((n, mach, 'fp32')))}
    out = ['## int8 dynamic quantization against fp32', '', "One model against itself: `<model>+cpu-int8` (`torch.quantization.quantize_dynamic`, CPU, 16 threads, full sets) against the model's own fp32 run on the same sets, same text, same cutting. `missed` is pooled over the sets where both runs exist and neither is contaminated. `delta` reads `CIs overlap` when the two marginal 95% bootstrap intervals of missed % overlap on every one of those sets. Overlapping marginal intervals are not a paired test of the difference and not an equivalence test; no direction is claimed for such pairs. `x fp32 speed` compares the int8 run with the fp32 CPU run of the same model on the same machine (device + processor + threads + W); it is `-` when there is no such pair. That speed pair is not clean: the fp32 CPU run is the `cpu-speed` slice of 100 rows per set while int8 covers the full sets, so the row mix differs.", '', '| model | sets | gold spans | missed fp32 | missed int8 | delta | x fp32 speed |', '|---|---|---|---|---|---|---|']
    for base, r in sorted(agg.items(), key=lambda kv: (kv[1]['q'] - kv[1]['a']) / kv[1]['spans']):
        pa, pq = (r['a'] / r['spans'] * 100, r['q'] / r['spans'] * 100)
        delta = 'CIs overlap' if r['over'] else f'{pq - pa:+.1f} pp'
        out.append(f"| {base} | {r['sets']} | {r['spans']} | {pa:.1f}% | {pq:.1f}% | {delta} | {(f'{fast[base]:.2f}x' if base in fast else '-')} |")
    tot = [sum((r[k] for r in agg.values())) for k in ('spans', 'a', 'q')]
    out += ['', f'Pooled over all {len(agg)} pairs: {tot[1] / tot[0]:.1%} missed in fp32 against {tot[2] / tot[0]:.1%} in int8 over {tot[0]} gold spans.', '']
    return out

def section(lang, kind, benches, data):
    names = sorted({m for b in benches for m in data[b]})
    if not names:
        return []
    pooled, macro = ({}, {})
    for m in names:
        miss = tot = cov = 0
        rates = []
        for b in benches:
            d = data[b].get(m)
            if not d or d['train']:
                continue
            miss += d['missed']
            tot += d['spans']
            cov += 1
            if d['spans']:
                rates.append(d['missed'] / d['spans'])
        pooled[m] = (miss / tot if tot else None, cov, miss, tot)
        macro[m] = statistics.fmean(rates) if rates else None
    names.sort(key=lambda m: (pooled[m][0] is None, pooled[m][0] or 0.0))
    n = len(benches)
    out = [f"## {lang} / {kind} ({n} set{'s' * (n > 1)}: {', '.join(benches)})", '', '### Missed spans (main metric)', '', '| model | ' + ' | '.join(benches) + ' | pooled | macro | coverage |', '|---|' + '---|' * (n + 3)]
    for m in names:
        cells = []
        for b in benches:
            d = data[b].get(m)
            cells.append('-' if not d else 'train' if d['train'] else f"{pct(d['missed'], d['spans'])} ({d['missed']})")
        p, cov, miss, tot = pooled[m]
        cells += [f'**{p:.1%}** ({miss}/{tot})' if p is not None else '-', f'{macro[m]:.1%}' if macro[m] is not None else '-', f'{cov}/{n}']
        out.append(f'| {m} | ' + ' | '.join(cells) + ' |')
    out += ['', '### Fully hidden spans, residual and over-masked characters (pooled, reference)', '', '| model | hidden | char R | char P |', '|---|---|---|---|']
    for m in names:
        hid = tot = tp = fp = fn = 0
        for b in benches:
            d = data[b].get(m)
            if not d or d['train']:
                continue
            hid += d['hidden']
            tot += d['spans']
            tp += d['tp']
            fp += d['fp']
            fn += d['fn']
        P, R, _ = prf(tp, fp, fn)
        out.append(f'| {m} | {pct(hid, tot)} | {R:.3f} | {P:.3f} |')
    out += ['', '### char F1 [95% CI], reference', '', '| model | ' + ' | '.join(benches) + ' |', '|---|' + '---|' * n]
    for m in names:
        cells = []
        for b in benches:
            d = data[b].get(m)
            cells.append('-' if not d else 'train' if d['train'] else f"{d['f1']:.3f} [{d['lo']:.3f}, {d['hi']:.3f}]")
        out.append(f'| {m} | ' + ' | '.join(cells) + ' |')
    if any((d['nneg'] for b in benches for d in data[b].values())):
        # T07: rows without annotations are not rows with nothing to hide.
        out += ['', '### Masking on rows without annotations', '', 'The source left these rows unannotated; that is not evidence that they hold no sensitive content, so this is not a false-alarm rate. `n/m (c chars)` - n of m unannotated rows were touched by a mask, masking c characters in them.', '', '| model | ' + ' | '.join(benches) + ' |', '|---|' + '---|' * n]
        for m in names:
            cells = []
            for b in benches:
                d = data[b].get(m)
                cells.append('-' if not d else f"{d['fire']}/{d['nneg']} ({d['negchars']} chars)" if d['nneg'] else 'no negatives')
            out.append(f'| {m} | ' + ' | '.join(cells) + ' |')
    return out + ['']

def score_one(args):
    bench, thresh = args
    global THRESH
    THRESH = thresh
    BAD_SPANS.clear()
    UNKNOWN.clear()
    LINE_GRAN.clear()
    summary = score(bench)
    return (bench, summary, {'legacy': LEGACY[bench], 'line': set(LINE_GRAN), 'bad': dict(BAD_SPANS), 'unknown': {k: dict(v) for k, v in UNKNOWN.items()}})

def merge(ex, bench):
    LEGACY[bench] |= ex['legacy']
    LINE_GRAN.update(ex['line'])
    for f, c in ex['bad'].items():
        BAD_SPANS[f] += c
    for lab, per in ex['unknown'].items():
        for m, c in per.items():
            UNKNOWN[lab][m] += c

def summarize(benches):
    jobs = int(os.environ.get('JOBS') or min(os.cpu_count() or 1, 8))
    data = {}
    if jobs > 1 and len(benches) > 1:
        with multiprocessing.Pool(min(jobs, len(benches))) as pool:
            for bench, s, ex in pool.imap_unordered(score_one, [(b, THRESH) for b in benches]):
                data[bench] = s
                merge(ex, bench)
    else:
        data = {b: score(b) for b in benches}
    benches = [b for b in benches if data[b]]
    out = ['# Benchmark summary', '', f'Main metric: **missed spans** - a gold span no predicted character touched, as % of the gold spans of the set (count in brackets). Score threshold {THRESH:g}; spans without a score always count. Char F1 is reference only.', '', 'Sections are the cuts declared in `BENCH/<set>/meta.json`: language, then kind. `pooled` is missed spans summed over the sets of the cut where the model has predictions and is not contaminated, divided by the spans of those sets; `coverage` says over how many sets of the cut that is. `macro` is the plain mean of the per-set missed rates over the same sets: there one set weighs as one set, while in `pooled` the largest sets of the cut decide. `train` - the model was trained on the source of the set, it is left out of both. Models are sorted by pooled missed. `hidden` - gold spans covered entirely (over normalized predictions: the prediction is stretched to whole words first, so this is the ceiling of what a masker hides), over the same sets as `pooled`; char R shows the residual sensitive characters (1 - R) and char P the over-masking. A mask-everything baseline has 0 missed, 100% hidden and char P equal to the share of sensitive characters in the text; the per-set reports print it together with the 95% bootstrap intervals of missed %.', '']
    for lang in ('ru', 'en', 'multi'):
        for kind in ('pii', 'secrets'):
            part = [b for b in benches if meta_of(b)['lang'] == lang and meta_of(b)['kind'] == kind]
            if part:
                out += section(lang, kind, part, data)
    if LINE_GRAN:
        out += [f"{', '.join(sorted(LINE_GRAN))} mark a whole line at a time (`granularity` in the meta line of the prediction file): their char F1 is not comparable with the rest, their missed count is.", '']
    if (leg := sorted({m for s in LEGACY.values() for m in s})):
        out += [f"Legacy runs, counted but not fingerprinted: {', '.join(leg)}. Their meta has no `protocol` and no `bench_sha256`; that they were taken from the current text of the set is confirmed by the row and character counts only. The per-set reports name the sets.", '']
    srows = speed(benches) or []
    if ONNX_CUDA:
        out += [f"{', '.join(sorted(ONNX_CUDA))} - onnx runs whose meta says `cuda`. The graph always goes through `CPUExecutionProvider`, so the run was CPU-bound: quality counts, speed is left out of `SPEED.md` because the meta names a GPU and no processor.", '']
    out += quant_pairs(benches, data, srows)
    out += ['Per-set reports are in the subdirectories. Speed is in `SPEED.md`, ensembles in `ENSEMBLE.md`, the secrets view in `SECRETS.md`.', '']
    (RESULTS / 'REPORT.md').write_text('\n'.join(out) + '\n')
    print('\n'.join(out))
    if (bad := {m: c for m, c in BAD_SPANS.items() if c}):
        print('\nOut-of-text intervals dropped from quality:')
        for m, c in sorted(bad.items(), key=lambda kv: -kv[1]):
            print(f'  {m}: {c}')
    if UNKNOWN:
        print('\nUnmapped labels assigned to OTHER:')
        for lab, per in sorted(UNKNOWN.items(), key=lambda kv: -sum(kv[1].values())):
            print(f'  {lab!r}: {sum(per.values())} spans; ' + ', '.join((f'{m} {c}' for m, c in per.most_common())))
    else:
        print('\nAll labels are mapped.')
if __name__ == '__main__':
    args = sys.argv[1:]
    if '--thresh' in args:
        i = args.index('--thresh')
        THRESH = float(args[i + 1])
        del args[i:i + 2]
    summarize(args or [d.name for d in sorted(BENCH.iterdir()) if d.is_dir() and (RESULTS / d.name).exists()])
