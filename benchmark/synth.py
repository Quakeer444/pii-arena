import base64, json, random, re, string
from pathlib import Path
import benchlib
SEED = 0
DIG, HEXD, UPPER = (string.digits, '0123456789abcdef', string.ascii_uppercase)
ALNUM = string.ascii_lowercase + string.digits
B62 = string.ascii_letters + string.digits
B64 = string.ascii_letters + string.digits + '+/'
B64U = string.ascii_letters + string.digits + '-_'
TYPES = ('person', 'phone', 'email', 'login', 'handle', 'hostname', 'ip', 'mac', 'url', 'org', 'address', 'employee_id', 'secret', 'password')
GRP_PII = {'person': 'PERSON', 'address': 'ADDRESS', 'phone': 'CONTACT', 'email': 'CONTACT', 'handle': 'CONTACT', 'login': 'ACCOUNT', 'employee_id': 'ACCOUNT', 'hostname': 'NET', 'ip': 'NET', 'mac': 'NET', 'url': 'NET', 'org': 'ORG', 'secret': 'SECRET', 'password': 'SECRET'}
GRP_SECRET = {'secret': 'SECRET', 'password': 'SECRET'}
MAIL_DOM = ('example.com', 'example.org', 'example.net', 'corp.example.test', 'office.example.local')
ZONE = ('prod.example.internal', 'stage.example.internal', 'test.example.internal', 'dc1.example.local', 'office.example.test')
SVC = ('app', 'api', 'web', 'db', 'proxy', 'gw', 'kafka', 'redis', 'backup', 'ldap', 'mail', 'fs')
ROLE_RU = ('ведущий инженер сопровождения', 'системный администратор', 'инженер первой линии', 'руководитель отдела сопровождения', 'администратор баз данных', 'специалист поддержки', 'инженер по сетям', 'аналитик сопровождения')
ROLE_EN = ('support engineer', 'system administrator', 'database administrator', 'network engineer', 'service desk specialist', 'team lead, operations')
TRL = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia'}

def rs(r, n, alpha):
    return ''.join((r.choice(alpha) for _ in range(n)))

def trl(s):
    return ''.join((TRL.get(c, TRL.get(c.lower(), c).upper() if c.isupper() else c) for c in s.lower()))

def emit(parts):
    text, ents, vals = ('', [], [])
    for p in parts:
        if isinstance(p, tuple):
            v, t = p
            assert t in TYPES, t
            ents.append({'start': len(text), 'end': len(text) + len(v), 'type': t})
            vals.append(v)
            text += v
        else:
            text += p
    for e, v in zip(ents, vals):
        assert text[e['start']:e['end']] == v, (v, e)
    return (text, ents)

def g_ip(r):
    return r.choice((f'10.{r.randint(0, 60)}.{r.randint(0, 255)}.{r.randint(1, 254)}', f'192.168.{r.randint(0, 60)}.{r.randint(1, 254)}', f'172.{r.randint(16, 31)}.{r.randint(0, 255)}.{r.randint(1, 254)}', f'192.0.2.{r.randint(1, 254)}', f'198.51.100.{r.randint(1, 254)}', f'203.0.113.{r.randint(1, 254)}'))

def g_host(r):
    return f'{r.choice(SVC)}-{r.randint(1, 24):02d}.{r.choice(ZONE)}'

def g_mac(r):
    return ':'.join((f'{b:02x}' for b in [2] + [r.randint(0, 255) for _ in range(5)]))

def g_url(r, tail=True):
    host = r.choice((f'wiki.{r.choice(ZONE)}', f'portal.{r.choice(MAIL_DOM)}', g_host(r), f'status.{r.choice(MAIL_DOM)}'))
    path = r.choice((f'/pages/{r.randint(1000, 99999)}', f'/d/{rs(r, 9, ALNUM)}/overview', f'/api/v2/items/{r.randint(1, 9999)}', f'/download/{rs(r, 6, ALNUM)}.zip'))
    return f'https://{host}{path}' if tail else f'https://{host}/'

def g_pw(r):
    stem = r.choice(('Qw3rty', 'Zr7pol', 'Mst4rk', 'Lp9tin', 'Vgx2sd', 'Prk8ml', 'Tnd5wq', 'Hbz3ru', 'Ksm6ta', 'Wdl1cf'))
    return stem + r.choice('!&*_-') + str(r.randint(10, 9999))

def _nm(f, meth, g):
    return (getattr(f, f'{meth}_{g}', None) or getattr(f, meth))()

def g_org(r, f):
    a, b = (f.last_name(), f.last_name())
    return r.choice((f'ООО «{a}»', f'АО «{a}-{b}»', f'НПО «{a}, {b} и партнёры»', f'ЗАО «{a}»', f'ОАО «{a}-{b}»', f'{a} Групп', f'{a} и партнёры', f'ИП {a}'))

def ident(r, f, ru=True):
    g = r.choice(('male', 'female')) if ru else ''
    first, last = (_nm(f, 'first_name', g), _nm(f, 'last_name', g))
    mid = _nm(f, 'middle_name', g) if ru else ''
    lf, ll = (trl(first).lower(), trl(last).lower())
    lf = re.sub('[^a-z]', '', lf) or 'user'
    ll = re.sub('[^a-z]', '', ll) or 'user'
    login = r.choice((f'{lf[0]}.{ll}', f'{ll}_{lf[0]}', f"{ll}.{lf[0]}{(trl(mid)[:1] or 'x').lower()}", f'adm_{ll}', f'svc-{ll}', f'{lf}{r.randint(1, 99)}'))
    full = f'{last} {first} {mid}'.strip() if r.random() < 0.5 else f'{first} {last}'
    return {'first': first, 'last': last, 'full': full, 'login': login, 'email': f'{login}@{r.choice(MAIL_DOM)}', 'handle': '@' + re.sub('[^a-z0-9_]', '_', login), 'phone': r.choice((f'+7 9{r.randint(10, 99)} {r.randint(100, 999)}-{r.randint(10, 99)}-{r.randint(10, 99)}', f'+7 (4{r.randint(10, 99)}) {r.randint(100, 999)}-{r.randint(10, 99)}-{r.randint(10, 99)}', f'8{r.randint(900, 999)}{r.randint(1000000, 9999999)}')), 'empid': r.choice((f'EMP-{r.randint(1000, 99999)}', f'таб. № {r.randint(1000, 999999):06d}', f'ID{r.randint(100000, 999999)}')), 'role': r.choice(ROLE_RU if ru else ROLE_EN)}

def _b64u(o):
    return base64.urlsafe_b64encode(json.dumps(o, separators=(',', ':')).encode()).decode().rstrip('=')

def g_jwt(r):
    head = _b64u({'alg': 'HS256', 'typ': 'JWT'})
    body = _b64u({'sub': rs(r, 12, ALNUM), 'name': 'svc', 'iat': r.randint(1700000000, 1790000000)})
    return f'{head}.{body}.{rs(r, 43, B64U)}'

def g_pem(r):
    kind = r.choice(('RSA PRIVATE KEY', 'OPENSSH PRIVATE KEY', 'EC PRIVATE KEY', 'PRIVATE KEY'))
    body = '\n'.join((rs(r, 64, B64) for _ in range(r.randint(3, 7))))
    return f'-----BEGIN {kind}-----\n{body}\n-----END {kind}-----'
TOKENS = (('GITHUB_TOKEN', lambda r: 'ghp_' + rs(r, 36, B62), 'secret'), ('GITHUB_OAUTH_TOKEN', lambda r: 'gho_' + rs(r, 36, B62), 'secret'), ('GITHUB_PAT', lambda r: 'github_pat_' + rs(r, 22, B62) + '_' + rs(r, 59, B62), 'secret'), ('GITLAB_TOKEN', lambda r: 'glpat-' + rs(r, 20, B62), 'secret'), ('GITLAB_AGENT_TOKEN', lambda r: 'glsa_' + rs(r, 20, B62) + '_' + rs(r, 8, HEXD), 'secret'), ('GITLAB_BUILD_TOKEN', lambda r: 'glcbt-' + rs(r, 20, B62), 'secret'), ('GITLAB_RUNNER_TOKEN', lambda r: 'glrt-' + rs(r, 20, B62), 'secret'), ('SLACK_BOT_TOKEN', lambda r: f'xoxb-{r.randint(10 ** 10, 10 ** 11)}-{r.randint(10 ** 10, 10 ** 11)}-' + rs(r, 24, B62), 'secret'), ('SLACK_USER_TOKEN', lambda r: f'xoxp-{r.randint(10 ** 10, 10 ** 11)}-{r.randint(10 ** 10, 10 ** 11)}-{r.randint(10 ** 10, 10 ** 11)}-' + rs(r, 32, HEXD), 'secret'), ('AWS_ACCESS_KEY_ID', lambda r: 'AKIA' + rs(r, 16, UPPER + DIG), 'secret'), ('AWS_SECRET_ACCESS_KEY', lambda r: rs(r, 40, B64), 'secret'), ('GOOGLE_API_KEY', lambda r: 'AIza' + rs(r, 35, B64U), 'secret'), ('LLM_API_KEY', lambda r: 'sk-' + rs(r, 48, B62), 'secret'), ('OAUTH_ACCESS_TOKEN', lambda r: 'ya29.' + rs(r, 78, B64U), 'secret'), ('SERVICE_JWT', g_jwt, 'secret'), ('PRIVATE_KEY', g_pem, 'secret'), ('SERVICE_PASSWORD', g_pw, 'password'), ('BOT_TOKEN', lambda r: f'001.{rs(r, 10, DIG)}.{rs(r, 10, DIG)}:{rs(r, 10, B62)}', 'secret'), ('SVC_TOKEN', lambda r: f"{r.choice(('svc', 'zk', 'tok'))}_{rs(r, 32, HEXD)}", 'secret'), ('LOCAL_API_KEY', lambda r: 'sk-local-' + rs(r, 24, B62), 'secret'))
_PH = re.compile('\\{(hex|alnum|b62|digits|upper|b64)(\\d+)\\}')
_ALPH = {'hex': HEXD, 'alnum': ALNUM, 'b62': B62, 'digits': DIG, 'upper': UPPER, 'b64': B64}

def _extra():
    p = Path(__file__).with_name('synth_extra.toml')
    if not p.exists():
        return ()
    import tomllib
    out = []
    for s in tomllib.loads(p.read_text()).get('secret', ()):
        tmpl, typ = (s['template'], s.get('type', 'secret'))
        assert typ in ('secret', 'password'), typ
        out.append((s.get('key', 'EXTRA_TOKEN'), lambda r, t=tmpl: _PH.sub(lambda m: rs(r, int(m[2]), _ALPH[m[1]]), t), typ))
    return tuple(out)
TOKENS += _extra()

def token(r, flat=False):
    while True:
        key, gen, typ = r.choice(TOKENS)
        val = gen(r)
        if not flat or '\n' not in val:
            return (key, val, typ)
ENV_FORMS = {1: None, 2: 'DATABASE_URL', 3: 'WIKI_URL'}

def snippet(r, ru, env=False):
    kind = r.choice(sorted(ENV_FORMS)) if env else r.randrange(9)
    pw, host, login = (g_pw(r), g_host(r), f'svc_{rs(r, 6, string.ascii_lowercase)}')
    if kind == 0:
        return (None, [f"{host}:5432:{r.choice(('billing', 'crm', 'reports'))}:{login}:", (pw, 'password')])
    if kind == 1:
        return (None, [r.choice(('export PGPASSWORD=', 'PGPASSWORD=')), (pw, 'password')])
    if kind == 2:
        scheme = r.choice(('postgres', 'mysql', 'mongodb', 'redis', 'amqp'))
        port = {'postgres': 5432, 'mysql': 3306, 'mongodb': 27017, 'redis': 6379, 'amqp': 5672}[scheme]
        return ('DATABASE_URL', [(f"{scheme}://{login}:{pw}@{host}:{port}/{r.choice(('billing', 'crm', 'main'))}", 'secret')])
    if kind == 3:
        return ('WIKI_URL', [(f'https://{login}:{pw}@wiki.{r.choice(ZONE)}/rest/api/content', 'secret')])
    if kind == 4:
        return (None, ['Authorization: Bearer ', (token(r, flat=True)[1] if r.random() < 0.5 else g_jwt(r), 'secret')])
    if kind == 5:
        b = base64.b64encode(f'{login}:{pw}'.encode()).decode()
        return (None, ['Authorization: Basic ', (b, 'secret')])
    if kind == 6:
        return (None, [f'org.apache.kafka.common.security.plain.PlainLoginModule required username="{login}" password="', (pw, 'password'), '";'])
    if kind == 7:
        return (None, [f'net use \\\\fs-0{r.randint(1, 4)}.{r.choice(ZONE)}\\share /user:corp\\{login} ', (pw, 'password')])
    lead = r.choice(('пароль: ', 'пасс: ', 'пароль от учётки - ', 'password=')) if ru else r.choice(('password: ', 'pass: ', 'the password is ', 'password='))
    return (None, [lead, (pw, 'password')])

def secret_parts(r, ru, env=False, flat=False):
    if r.random() < 0.55:
        key, val, typ = token(r, flat)
        return (key, [(val, typ)])
    return snippet(r, ru, env)

def g_uuid(r):
    return f"{rs(r, 8, HEXD)}-{rs(r, 4, HEXD)}-4{rs(r, 3, HEXD)}-{r.choice('89ab')}{rs(r, 3, HEXD)}-{rs(r, 12, HEXD)}"

def n_key(r):
    return f'{rs(r, 3, UPPER)}-{r.randint(1, 9999)}'

def n_ver(r):
    return f'{r.randint(0, 9)}.{r.randint(0, 24)}.{r.randint(0, 40)}'

def n_code(r):
    return r.choice((f'E_TIMEOUT_{r.randint(1000, 9999)}', 'HTTP 502', '0x80070005', f'ERR-{r.randint(100, 999)}'))

def n_sn(r):
    return f'SN-{rs(r, 2, UPPER)}-{r.randint(100000, 999999)}'

def n_sha(r):
    return rs(r, 40, HEXD)
NEG_PLACEHOLDER = (lambda r: '{{ env.' + r.choice(('API_TOKEN', 'DB_PASSWORD', 'SECRET_KEY')) + ' }}', lambda r: '${' + r.choice(('DB_PASSWORD', 'API_TOKEN', 'VAULT_SECRET', 'CI_JOB_TOKEN')) + '}', lambda r: r.choice(('<your_token>', '<PASTE_TOKEN_HERE>', '<api-key>')), lambda r: r.choice(('changeme', 'CHANGE_ME', 'REDACTED', '***', 'secret-goes-here', 'null')))
NEG_ITEMS = (('BUILD_SHA', n_sha), ('BUILD_REF', lambda r: rs(r, 7, HEXD)), ('IMAGE_DIGEST', lambda r: 'sha256:' + rs(r, 64, HEXD)), ('RELEASE', n_ver), ('REQUEST_ID', g_uuid), ('DEVICE_SN', n_sn), ('ERROR_CODE', n_code), ('TASK_KEY', n_key), ('SSH_AUTHORIZED_KEY', lambda r: 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQ' + rs(r, 180, B64) + ' deploy@ci'), ('LOGO_DATA_URI', lambda r: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA' + rs(r, 140, B64)))
SECRET_KEYS = ('API_TOKEN', 'DB_PASSWORD', 'SECRET_KEY', 'AUTH_TOKEN', 'PRIVATE_KEY')

def neg(r):
    return r.choice(NEG_PLACEHOLDER + tuple((fn for _, fn in NEG_ITEMS)))(r)
CHAT = {'ru': (('подняли стенд, доступ ниже', 'выкатил сборку, проверьте на тесте', 'не пускает в панель, смотрю логи', 'перевыпустил ключ, старый отозвал', 'деплой прошёл, ошибок нет', 'на проде тот же симптом, чиню'), ('вот ключ для выгрузки: ', 'держи доступ: ', 'временный токен: ', 'креды такие: ', 'для теста поставь ', 'старое значение было '), ('в конфиге стоит ', 'значение подставляется из ', 'в шаблоне сейчас ', 'собрал на коммите ', 'у нас версия ', 'падает с кодом ')), 'en': (('stage is up, access below', 'pushed the build, please check on test', 'cannot log into the panel, reading logs', 'rotated the key, old one revoked', 'deploy is green, no errors', 'same symptom on prod, working on it'), ('here is the export key: ', 'access: ', 'temporary token: ', 'creds are: ', 'for the test set ', 'the old value was '), ('the config has ', 'the value comes from ', 'the template currently holds ', 'built from commit ', 'we are on version ', 'it fails with '))}
COMMENT = {'ru': (('Воспроизвёл на стенде, симптом тот же.', 'Проверил после ротации, доступ есть.', 'Согласовал с сопровождением, чиню в этом спринте.', 'Похоже на регрессию после обновления.'), ('Дёргал ручку с токеном ', 'Для проверки использовал ', 'Подставил в переменную '), ('В шаблоне лежит ', 'Тут только плейсхолдер ', 'Связал с ')), 'en': (('Reproduced on stage, same symptom.', 'Checked after rotation, access is fine.', 'Agreed with support, fixing this sprint.', 'Looks like a regression after the update.'), ('Called the endpoint with ', 'Used for the check ', 'Put into the variable '), ('The template holds ', 'This is only a placeholder ', 'Linked to '))}
WIKI = {'ru': (('### Доступ к выгрузке\n\nВыгрузка забирается по расписанию раз в сутки, результат кладётся в общий каталог.', '### Ротация ключей\n\nКлюч сервисной учётки меняется раз в квартал, старое значение отзывается в тот же день.', '### Подключение к стенду\n\nСтенд поднимается по запросу и живёт до конца недели.'), ('Текущее значение: ', 'Ключ: ', 'Строка подключения: '), ('В шаблоне значение задано как ', 'Здесь всегда плейсхолдер ', 'Проверяйте сборку ')), 'en': (('### Export access\n\nThe export runs once a day and lands in the shared folder.', '### Key rotation\n\nThe service key is rotated quarterly, the old value is revoked the same day.', '### Stage access\n\nThe stage is created on request and lives until the end of the week.'), ('Current value: ', 'Key: ', 'Connection string: '), ('The template sets the value as ', 'This is always a placeholder ', 'Check the build '))}

def c_chat(r, lang, sec):
    plain, pay, negl = CHAT[lang]
    parts, h, m = ([], r.randint(9, 19), r.randint(0, 50))
    lines = r.randint(3, 6)
    said = r.sample(plain, min(lines, len(plain)))
    for k in range(lines):
        parts += [f'[{h:02d}:{m + k:02d}] ']
        if sec and k < len(sec):
            parts += [r.choice(pay), *sec[k][1], '\n']
        else:
            parts += [said[k] if r.random() < 0.6 else r.choice(negl) + neg(r), '\n']
    return ('chat', parts)

def c_comment(r, lang, sec):
    plain, pay, negl = COMMENT[lang]
    parts = [r.choice(plain), ' ']
    for sc in sec:
        parts += [r.choice(pay), *sc[1], '. ']
    for _ in range(r.randint(1, 3) if not sec else 1):
        parts += [r.choice(negl), neg(r), '. ']
    parts += [r.choice(plain), f' Хост стенда: {g_host(r)}, адрес {g_ip(r)}.\n' if lang == 'ru' else f' Stage host: {g_host(r)}, address {g_ip(r)}.\n']
    return ('comment', parts)

def c_wiki(r, lang, sec):
    head, pay, negl = WIKI[lang]
    parts = [r.choice(head), '\n\n']
    for sc in sec:
        parts += [r.choice(pay), *sc[1], '\n\n']
    for _ in range(r.randint(1, 3) if not sec else 1):
        parts += [r.choice(negl), neg(r), '\n\n']
    tail = 'Проверить доступ можно с хоста ' if lang == 'ru' else 'Access can be checked from host '
    parts += [tail, g_host(r), f' ({g_ip(r)}).\n']
    return ('wiki', parts)
ENV_PLAIN = (('APP_ENV', ('production', 'stage', 'test')), ('LOG_LEVEL', ('info', 'debug', 'warn')), ('HTTP_PORT', ('8080', '8443', '9000')), ('WORKERS', ('4', '8', '16')), ('TIMEOUT_SEC', ('30', '60', '120')), ('RETRY', ('3', '5')))

def c_env(r, lang, sec):
    parts = ['# ' + ('сервис выгрузки, стенд ' if lang == 'ru' else 'export service, env ') + r.choice(('test', 'stage', 'prod')) + '\n']
    parts += [f'DB_HOST={g_host(r)}\nAPP_BIND={g_ip(r)}\n']
    for k, vals in ENV_PLAIN:
        if r.random() < 0.6:
            parts += [f'{k}={r.choice(vals)}\n']
    for k in r.sample(SECRET_KEYS, 2):
        parts += [f'{k}={r.choice(NEG_PLACEHOLDER)(r)}\n']
    for k, fn in r.sample(NEG_ITEMS, 2):
        parts += [f'{k}={fn(r)}\n']
    for sc in sec or ():
        key, body = sc
        parts += [f'{key}=' if key else '', *body, '\n']
    return ('env', parts)

def c_log(r, lang, sec):
    parts = []
    for k in range(r.randint(3, 8)):
        stamp = f'2026-0{r.randint(1, 9)}-{r.randint(10, 28)}T{r.randint(10, 23)}:{r.randint(10, 59)}:{r.randint(10, 59)}Z'
        lvl = r.choice(('INFO', 'WARN', 'ERROR', 'DEBUG'))
        parts += [f'{stamp} {lvl} auth[{r.randint(1000, 9999)}]: ']
        if sec and k < len(sec):
            parts += ['upstream call, ', *sec[k][1], f' host={g_host(r)} src={g_ip(r)}\n']
        else:
            parts += [f"request id={g_uuid(r)} host={g_host(r)} src={g_ip(r)} build={n_ver(r)} status={r.choice(('200', '401', '502'))}\n"]
    return ('log', parts)
CARRIERS = (c_chat, c_comment, c_wiki, c_env, c_log)

def _secrets_rows(lang, n, prefix):
    r = random.Random(SEED)
    for i in range(n):
        carrier = CARRIERS[i % len(CARRIERS)]
        flat = carrier in (c_chat, c_log, c_env)
        sec = [secret_parts(r, lang == 'ru', carrier is c_env, flat) for _ in range(r.randint(1, 3))] if i % 2 == 0 else []
        dom, parts = carrier(r, lang, sec)
        text, ents = emit(parts)
        assert len(ents) == len(sec), (i, len(ents), len(sec))
        yield (f'{prefix}-{i:04d}', dom, text, ents)

def synth_secrets_ru():
    return _secrets_rows('ru', 600, 'secru')

def synth_secrets_en():
    return _secrets_rows('en', 600, 'secen')

def _faker():
    from faker import Faker
    fr, fe = (Faker('ru_RU'), Faker('en_US'))
    Faker.seed(SEED)
    return (fr, fe)

def plen(parts):
    return sum((len(p[0]) if isinstance(p, tuple) else len(p) for p in parts))

def p_ru(r, f, who, org):
    k = r.randrange(10)
    if k == 0:
        return ['Пользователь ', (who['full'], 'person'), ' (логин ', (who['login'], 'login'), ') не заходит в личный кабинет ', (g_url(r), 'url'), ' - страница отдаёт ', n_code(r), '.']
    if k == 1:
        return ['С хоста ', (g_host(r), 'hostname'), ' (', (g_ip(r), 'ip'), ') запросы к сервису отваливаются по таймауту, в ответе ', n_code(r), '.']
    if k == 2:
        return ['Заявка от ', (org, 'org'), ', адрес офиса: ', (f.address().replace('\n', ', '), 'address'), '.']
    if k == 3:
        return ['Контакт на стороне заказчика: ', (who['full'], 'person'), ', тел. ', (who['phone'], 'phone'), ', почта ', (who['email'], 'email'), ', в мессенджере ', (who['handle'], 'handle'), '.']
    if k == 4:
        return ['Табельный номер сотрудника - ', (who['empid'], 'employee_id'), f', доступ выдавали {r.randint(1, 28):02d}.0{r.randint(1, 9)}.2026.']
    if k == 5:
        return ['Проверили маршрут до ', (g_ip(r), 'ip'), ', MAC интерфейса ', (g_mac(r), 'mac'), ' совпадает с журналом коммутатора.']
    if k == 6:
        return ['Похожее обращение уже регистрировали как ', n_key(r), ', закрыли без решения, версия сборки ', n_ver(r), '.']
    if k == 7:
        return ['Просим восстановить доступ учётной записи ', (who['login'], 'login'), ' на сервере ', (g_host(r), 'hostname'), '.']
    if k == 8:
        return ['Для проверки завели временную учётку, пароль ', (g_pw(r), 'password'), ' - после входа сменим.']
    return ['Инструкция лежит в базе знаний ', (g_url(r), 'url'), ', раздел для ', (org, 'org'), '.']

def t_log_ru(r, who):
    stamp = f'2026-0{r.randint(1, 9)}-{r.randint(10, 28)} {r.randint(10, 23)}:{r.randint(10, 59)}:{r.randint(10, 59)},{r.randint(100, 999)}'
    lvl = r.choice(('ERROR', 'WARN', 'INFO'))
    return [f'{stamp} {lvl} [http-nio-8080-exec-{r.randint(1, 9)}] AuthFilter - ', r.choice(('login failed', 'session expired', 'upstream timeout')), ' user=', (who['login'], 'login'), ' src=', (g_ip(r), 'ip'), ' host=', (g_host(r), 'hostname'), f' code={n_code(r)}\n']

def synth_ru_tickets():
    r, (fr, _) = (random.Random(SEED), _faker())
    for i in range(400):
        a, b, c = (ident(r, fr), ident(r, fr), ident(r, fr))
        org = g_org(r, fr)
        target = r.randint(1000, 7000)
        parts = ['От: ', (a['full'], 'person'), ' <', (a['email'], 'email'), '>\n', 'Кому: ', ('support@' + r.choice(MAIL_DOM), 'email'), '\n']
        if r.random() < 0.4:
            parts += ['Копия: ', (c['full'], 'person'), ' <', (c['email'], 'email'), '>\n']
        parts += ['Тема: ', r.choice(('Не открывается портал на ', 'Ошибка авторизации на ', 'Не приходит выгрузка с ', 'Падает сервис на ')), (g_host(r), 'hostname'), '\n', f'Дата: {r.randint(1, 28):02d}.0{r.randint(1, 9)}.2026 {r.randint(9, 18)}:{r.randint(10, 59)}\n\n', r.choice(('Здравствуйте!', 'Добрый день!', 'Коллеги, добрый день!')), '\n\n']
        while plen(parts) < target:
            left = target - plen(parts)
            roll = r.random() if left > 900 else 0.0
            if roll < 0.45:
                parts += p_ru(r, fr, r.choice((a, b, c)), org) + ['\n\n']
            elif roll < 0.7:
                parts += ['Лог с сервера:\n\n']
                for _ in range(min(20, max(2, left // 150))):
                    parts += t_log_ru(r, r.choice((a, b)))
                parts += ['\n']
            elif roll < 0.85:
                parts += [f'{r.randint(1, 28):02d}.0{r.randint(1, 9)}.2026, {r.randint(9, 18)}:{r.randint(10, 59)}, ', (b['full'], 'person'), ' <', (b['email'], 'email'), '>:\n']
                for _ in range(min(8, max(2, left // 260))):
                    parts += ['> '] + p_ru(r, fr, r.choice((a, b, c)), org) + ['\n']
                parts += ['>\n\n']
            else:
                parts += ['Во вложении: ', ', '.join((r.choice(('скриншот_ошибки', 'выгрузка', 'лог_сервиса', 'трассировка')) + f'_{r.randint(1, 28):02d}09_{rs(r, 4, ALNUM)}.' + r.choice(('png', 'txt', 'log', 'zip', 'xlsx')) for _ in range(r.randint(1, 3)))), '.\n\n']
        parts += ['--\nС уважением,\n', (a['full'], 'person'), '\n', a['role'], ', ', (org, 'org'), '\n', 'тел. ', (a['phone'], 'phone'), f', доб. {r.randint(1000, 9999)}\n', (a['email'], 'email'), '\n', (a['empid'], 'employee_id'), '\n']
        text, ents = emit(parts)
        yield (f'tick-{i:04d}', 'email', text, ents)

def synth_wiki_tables():
    r, (fr, _) = (random.Random(SEED), _faker())
    for i in range(300):
        org = g_org(r, fr)
        parts = []
        if i % 3 == 2:
            parts += ['## Домены и DNS - ', (org, 'org'), '\n\n', f'Актуально на {r.randint(1, 28):02d}.0{r.randint(1, 9)}.2026. Изменения - через заявку в сопровождение.\n\n', '| домен | назначение | IP | MAC | панель |\n|---|---|---|---|---|\n']
            for _ in range(r.randint(3, 12)):
                parts += ['| ', (g_host(r), 'hostname'), ' | ', r.choice(('фронт', 'бэкенд', 'балансировщик', 'почтовый релей', 'файловый доступ')), ' | ', (g_ip(r), 'ip'), ' | ', (g_mac(r), 'mac'), ' | ', (g_url(r), 'url'), ' |\n']
            parts += ['\nСерийный номер шасси - ', n_sn(r), ', прошивка ', n_ver(r), '.\n']
        else:
            parts += ['## Контакты сопровождения - ', (org, 'org'), '\n\n', r.choice(('Дежурная смена отвечает в рабочие часы.', 'По вопросам доступа писать в чат сопровождения.', 'Эскалация - через руководителя отдела.')), '\n\n', '| ФИО | должность | почта | телефон | telegram | логин | таб. номер |\n', '|---|---|---|---|---|---|---|\n']
            for _ in range(r.randint(3, 12)):
                p = ident(r, fr)
                parts += ['| ', (p['full'], 'person'), ' | ', p['role'], ' | ', (p['email'], 'email'), ' | ', (p['phone'], 'phone'), ' | ', (p['handle'], 'handle'), ' | ', (p['login'], 'login'), ' | ', (p['empid'], 'employee_id'), ' |\n']
            parts += ['\nЗаявки на доступ - ', (g_url(r), 'url'), ', шаблон ', n_key(r), '.\n']
        text, ents = emit(parts)
        yield (f'wiki-{i:04d}', 'table', text, ents)
STACK_RU = ('java.lang.NullPointerException: Cannot invoke "String.length()" because "s" is null\n\tat com.example.svc.Router.route(Router.java:88)\n\tat com.example.svc.Handler.handle(Handler.java:41)\n', 'Traceback (most recent call last):\n  File "/opt/app/worker.py", line 212, in run\n    self._flush(batch)\nConnectionResetError: [Errno 104] Connection reset by peer\n')

def synth_jira_comments():
    r, (fr, fe) = (random.Random(SEED), _faker())
    for i in range(300):
        en = i % 10 >= 7
        f = fe if en else fr
        parts = []
        for n in range(1, r.randint(2, 4)):
            p = ident(r, f, ru=not en)
            parts += [f"## {('comment' if en else 'комментарий')} {n} | ", (p['full'], 'person'), '\n\n']
            parts += [r.choice(('Reproduced on stage ', 'Checked on host ', 'Same on ')) if en else r.choice(('Воспроизвёл на стенде ', 'Проверил на хосте ', 'То же самое на ')), (g_host(r), 'hostname'), ' (', (g_ip(r), 'ip'), '), ', f'linked to {rs(r, 3, UPPER)}-{r.randint(1, 9999)}.' if en else f'связал с {rs(r, 3, UPPER)}-{r.randint(1, 9999)}.', '\n\n']
            if r.random() < 0.6:
                head = snippet(r, not en)[1] if r.random() < 0.3 else ['Authorization: Bearer ', (token(r, flat=True)[1], 'secret')]
                parts += [f"curl -s -X {r.choice(('GET', 'POST'))} '{g_url(r)}' \\\n  -H '", *head, "' \\\n  -H 'Content-Type: application/json'\n\n"]
            if r.random() < 0.5:
                parts += ['Stack:\n\n' if en else 'Стек:\n\n', r.choice(STACK_RU), '\n']
            if r.random() < 0.4:
                parts += ['Contact: ' if en else 'Контакт: ', (p['email'], 'email'), ', ', (p['phone'], 'phone'), ', ', (p['login'], 'login'), '. Build ' if en else '. Сборка ', n_ver(r), '.\n\n']
        text, ents = emit(parts)
        yield (f'jira-{i:04d}', 'en' if en else 'ru', text, ents)
CFG_PLAIN = (('APP_ENV', 'production'), ('LOG_LEVEL', 'info'), ('HTTP_PORT', '8080'), ('WORKERS', '8'), ('TIMEOUT_SEC', '30'), ('CACHE_TTL', '600'))

def _cfg_items(r, pos):
    items = {k: ([v], False) for k, v in CFG_PLAIN if r.random() < 0.7}
    items['DB_HOST'], items['BIND_ADDR'] = (([g_host(r)], False), ([g_ip(r)], False))
    for k in r.sample(SECRET_KEYS, r.randint(2, 4)):
        items[k] = ([r.choice(NEG_PLACEHOLDER)(r)], False)
    for k, fn in r.sample(NEG_ITEMS, r.randint(1, 3)):
        items[k] = ([fn(r)], False)
    if pos:
        for _ in range(r.randint(1, 3)):
            key, body = secret_parts(r, False, env=True, flat=True)
            items[key or 'PGPASSWORD'] = (body if key else body[1:], True)
    out = [(k, v, sec) for k, (v, sec) in items.items()]
    r.shuffle(out)
    return out

def synth_env_configs():
    r, _ = (random.Random(SEED), None)
    for i in range(400):
        pos, fmt = (i % 2 == 0, ('env', 'j2', 'yaml', 'json', 'compose')[i % 5])
        items = _cfg_items(r, pos)
        parts = []
        if fmt == 'env':
            parts += [f"# service config, {r.choice(('prod', 'stage', 'test'))}\n"]
            for k, v, _ in items:
                parts += [f'{k}=', *v, '\n']
        elif fmt == 'j2':
            parts += ['{# rendered by the deploy job #}\n']
            for k, v, is_sec in items:
                parts += [f'{k}=', *(v if is_sec or r.random() < 0.4 else ['{{ env.' + k + ' }}']), '\n']
        elif fmt == 'yaml':
            parts += ['apiVersion: v1\nkind: ConfigMap\nmetadata:\n  name: app-config\ndata:\n']
            for k, v, _ in items:
                parts += [f'  {k.lower()}: "', *v, '"\n']
        elif fmt == 'json':
            parts += ['{\n']
            for n, (k, v, _) in enumerate(items):
                parts += [f'  "{k.lower()}": "', *v, '"' + (',\n' if n < len(items) - 1 else '\n')]
            parts += ['}\n']
        else:
            parts += [f'version: "3.9"\nservices:\n  api:\n    image: registry.example.internal/team/api:1.{r.randint(0, 9)}.{r.randint(0, 30)}\n    environment:\n']
            for k, v, _ in items:
                parts += [f'      - {k}=', *v, '\n']
        text, ents = emit(parts)
        assert bool(ents) == pos, (i, len(ents))
        yield (f'env-{i:04d}', fmt, text, ents)
LABEL = {'person': ('person', 'имя человека'), 'phone': ('phone number', 'номер телефона'), 'email': ('email', 'электронная почта'), 'login': ('username', 'логин'), 'handle': ('messenger handle', 'ник в мессенджере'), 'hostname': ('hostname', 'имя хоста'), 'ip': ('ip address', 'IP адрес'), 'mac': ('mac address', 'MAC адрес'), 'url': ('url', 'ссылка'), 'org': ('organization', 'организация'), 'address': ('address', 'адрес'), 'employee_id': ('employee id', 'табельный номер сотрудника'), 'secret': ('secret or api key', 'секрет или API ключ'), 'password': ('password', 'пароль')}
SRC = 'generated by SCRIPTS/synth.py, seed 0'

def _lab(types):
    return {'en': [LABEL[t][0] for t in types], 'ru': [LABEL[t][1] for t in types]}

def _meta(lang, kind, domain, types):
    return {'lang': lang, 'kind': kind, 'source': SRC, 'license': 'cc-by-4.0', 'mode': 'files', 'domain': domain, 'labels': _lab(types), 'groups': {t: GRP_PII[t] for t in types}}
SEC_T = ('secret', 'password')
PII_T = ('person', 'phone', 'email', 'login', 'handle', 'hostname', 'ip', 'mac', 'url', 'org', 'address', 'employee_id', 'password')
BUILDERS = {'synth-secrets-ru': synth_secrets_ru, 'synth-secrets-en': synth_secrets_en, 'synth-ru-tickets': synth_ru_tickets, 'synth-wiki-tables': synth_wiki_tables, 'synth-jira-comments': synth_jira_comments, 'synth-env-configs': synth_env_configs}
META = {'synth-secrets-ru': _meta('ru', 'secrets', 'invented secrets in Russian carriers: chat, task comment, wiki, .env, log; half the rows are hard negatives (placeholders, uuid, sha, public keys); hosts and IP are context, not gold', SEC_T), 'synth-secrets-en': _meta('en', 'secrets', 'the same five carriers in English: chat, task comment, wiki, .env, log; half the rows are hard negatives; hosts and IP are context, not gold', SEC_T), 'synth-ru-tickets': _meta('ru', 'pii', 'long Russian support emails: From/To/Subject headers, quoted replies, log blocks with IP and hostnames, attachment names, signature with role and phone, 1-8k chars', PII_T), 'synth-wiki-tables': _meta('ru', 'pii', 'Russian wiki markdown tables: contacts (name, role, email, phone, telegram, login, employee id) and host/DNS tables with IP, MAC and links', ('person', 'phone', 'email', 'login', 'handle', 'hostname', 'ip', 'mac', 'url', 'org', 'employee_id')), 'synth-jira-comments': _meta('ru', 'pii', 'issue tracker comments, 70% Russian and 30% English (per-row `domain`): `## комментарий N | Name`, curl with an Authorization header, stack traces, issue keys ABC-123 as negatives', ('person', 'phone', 'email', 'login', 'hostname', 'ip', 'url', 'secret', 'password')), 'synth-env-configs': _meta('en', 'secrets', 'config files: .env, .env.j2, YAML ConfigMap, JSON, docker-compose; half the rows carry only placeholders ({{ env.X }}, ${VAR}, changeme), half carry literal secrets', SEC_T)}
if __name__ == '__main__':
    benchlib.main(BUILDERS, META)
