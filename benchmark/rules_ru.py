import os
import csv, ipaddress, json, re, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from benchlib import PROTOCOL, bench_sha256, machine
VERSION = '1.0'
ROOT = Path(os.environ.get('BENCHMARK_DATA', str(Path(__file__).resolve().parent.parent / '.local' / 'research'))).resolve()

def _dig(s):
    return re.sub('\\D', '', s)

def inn_ok(d):

    def c(w):
        return sum((int(x) * y for x, y in zip(d, w))) % 11 % 10
    if len(d) == 10:
        return c((2, 4, 10, 3, 5, 9, 4, 6, 8)) == int(d[9])
    if len(d) == 12:
        return c((7, 2, 4, 10, 3, 5, 9, 4, 6, 8)) == int(d[10]) and c((3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)) == int(d[11])
    return False

def snils_ok(d):
    if len(d) != 11 or len(set(d[:9])) == 1:
        return False
    s = sum((int(d[i]) * (9 - i) for i in range(9)))
    k = 0 if s in (100, 101) else s if s < 100 else 0 if s % 101 in (100, 101) else s % 101
    return k == int(d[9:])

def ogrn_ok(d):
    if len(d) == 13:
        return int(d[:12]) % 11 % 10 == int(d[12])
    if len(d) == 15:
        return int(d[:14]) % 13 % 10 == int(d[14])
    return False

def luhn_ok(d):
    s = 0
    for i, ch in enumerate(reversed(d)):
        n = int(ch)
        if i % 2:
            n = n * 2 - 9 if n * 2 > 9 else n * 2
        s += n
    return s % 10 == 0

def account_ok(acc, bik):
    pre = '0' + bik[4:6] if acc.startswith('301') else bik[6:9]
    return sum((int(x) * y % 10 for x, y in zip(pre + acc, [7, 1, 3] * 8))) % 10 == 0
RX = {'inn': re.compile('(?<!\\d)(?:\\d{12}|\\d{10})(?!\\d)'), 'snils': re.compile('(?<!\\d)\\d{3}[- ]?\\d{3}[- ]?\\d{3}[- ]?\\d{2}(?!\\d)'), 'ogrn': re.compile('(?<!\\d)\\d{13}(?!\\d)'), 'ogrnip': re.compile('(?<!\\d)\\d{15}(?!\\d)'), 'bik': re.compile('(?<!\\d)04\\d{7}(?!\\d)'), 'kpp': re.compile('(?<![\\dA-Z])\\d{4}[0-9A-Z]{2}\\d{3}(?![\\dA-Z])'), 'account': re.compile('(?<!\\d)\\d{20}(?!\\d)'), 'card': re.compile('(?<![\\d-])(?:\\d[ -]?){12,18}\\d(?![\\d-])'), 'passport_ctx': re.compile('(?<!\\d)\\d{4} ?\\d{6}(?!\\d)'), 'passport_fmt': re.compile('(?<!\\d)\\d{2} \\d{2} \\d{6}(?!\\d)'), 'phone_ru': re.compile('(?<![\\d+\\w])(?:\\+7|8)[ -]?\\(?\\d{3}\\)?[ -]?\\d{3}[ -]?\\d{2}[ -]?\\d{2}(?!\\d)'), 'phone_intl': re.compile('(?<![\\d+\\w])\\+\\d[\\d ()-]{6,18}\\d(?!\\d)'), 'email': re.compile('[\\w.%+-]+@[\\w-]+(?:\\.[\\w-]+)*\\.[a-zA-Zа-яА-Я]{2,}', re.UNICODE), 'ipv4': re.compile('(?<![\\d.])\\d{1,3}(?:\\.\\d{1,3}){3}(?![\\d.])'), 'ipv6': re.compile('(?<![:\\w.])(?:[0-9A-Fa-f]{0,4}:){2,7}[0-9A-Fa-f]{0,4}(?![:\\w.])'), 'mac': re.compile('(?<![\\w:.-])(?:(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}|(?:[0-9A-Fa-f]{4}\\.){2}[0-9A-Fa-f]{4})(?![\\w:.-])'), 'url': re.compile('\\b(?:https?|ftps?|ssh|sftp|git|wss?)://[^\\s<>\\"\'`\\\\)\\]}]+|\\bwww\\.[a-z0-9-]+(?:\\.[a-z0-9-]+)+[^\\s<>\\"\'`\\\\)\\]}]*', re.I), 'hostname': re.compile('(?<![\\w.@/-])(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\\.)+[a-z]{2,24}(?![\\w-])'), 'handle': re.compile('(?<![\\w@./-])@(?=[\\wа-яА-ЯёЁ-]*[a-zA-Zа-яА-ЯёЁ])[\\wа-яА-ЯёЁ-]{2,32}(?![\\w.@-])')}
_FORM = 'ООО|ОАО|ЗАО|ПАО|АО|ИП|НКО|АНО|ГБУ|ФГБУ|ФГУП|МУП|ГУП|ТОО|НПО|ГК|LLC|L\\.L\\.C\\.|Inc|Ltd|GmbH|S\\.A\\.|OÜ'
_CAPW = '[А-ЯЁA-Z][A-Za-zА-Яа-яЁё0-9&-]*'
RX['org_pre'] = re.compile(f"""(?<![\\w«\\"])(?:{_FORM})\\.?[ \\u00a0]*(?:[«\\"'][^«»\\"'\\n]{{2,80}}[»\\"']|{_CAPW}(?:[ \\u00a0]{_CAPW}){{0,3}})""")
RX['org_post'] = re.compile(f'(?<![\\w«\\"]){_CAPW}(?:[ \\u00a0]{_CAPW}){{0,3}},?[ \\u00a0](?:LLC|L\\.L\\.C\\.|Inc|Ltd|GmbH|S\\.A\\.|OÜ)\\.?(?![\\w])')
RX_LOGIN = [re.compile(p) for p in ('(?<![\\w.@-])[a-z]{1,2}\\.[a-z]{2,20}(?![\\w.@-])', '(?<![\\w.@-])[a-z]{3,20}\\.[a-z](?![\\w.@-])', '(?<![\\w.@-])[a-z]{3,20}_[a-z](?![\\w.@-])', '(?<![\\w.@-])(?:adm|admin|svc|sys|usr|user|oper|op|srv|bot|tech|support)_[a-z0-9]{2,20}(?![\\w.@-])', '(?<![\\w.@-])[a-z][\\w.-]{2,30}@(?![\\w-]+\\.[a-zA-Zа-яА-Я]{2,})')]
RX_SECRET = [(re.compile('\\bgh[pousr]_[A-Za-z0-9]{20,}'), 0), (re.compile('\\bgithub_pat_[A-Za-z0-9_]{20,}'), 0), (re.compile('\\bgl(?:pat-|sa_|cbt-|rt-|ptt-|dt-|oat-|feat-|imt-)[A-Za-z0-9_-]{16,}'), 0), (re.compile('\\bxox[abprs]-[A-Za-z0-9-]{10,}'), 0), (re.compile('\\b(?:AKIA|ASIA|AGPA|AIDA|AROA|ANPA|ANVA|ABIA|ACCA)[0-9A-Z]{12,}'), 0), (re.compile('\\bsk-(?:proj-|ant-|live-|test-)?[A-Za-z0-9_-]{16,}'), 0), (re.compile('\\bAIza[0-9A-Za-z_-]{30,}'), 0), (re.compile('\\bya29\\.[0-9A-Za-z_-]{20,}'), 0), (re.compile('\\beyJ[A-Za-z0-9_-]{5,}\\.[A-Za-z0-9_-]{5,}\\.[A-Za-z0-9_-]{5,}'), 0), (re.compile('-----BEGIN[ A-Z0-9]*PRIVATE KEY-----.*?-----END[ A-Z0-9]*PRIVATE KEY-----', re.S), 0), (re.compile('\\b[a-z][a-z0-9+.-]*://[^\\s:/@]+:[^\\s/@]{3,}@[^\\s\\"\'`<>]+', re.I), 0), (re.compile('(?i)\\bauthorization\\s*:\\s*(?:bearer|basic|token)\\s+([^\\s\\"\'`,;]{8,})'), 1), (re.compile('(?im)^[^\\s:]+:\\d{1,5}:[^\\s:]*:[^\\s:]+:(\\S{3,})$'), 1), (re.compile('(?i)(?:password|passwd|pwd|secret|token|api[_-]?key|apikey|access[_-]?key|auth[_-]?token|client[_-]?secret|privatekey|пароль|парол[ья])[\\w-]*\\s*(?:::?=|[:=])\\s*[\\"\'`]?([^\\s\\"\'`,;<>]{4,})'), 1), (re.compile('(?i)<([\\w-]*(?:token|secret|password|apikey))>\\s*([^<\\s]{6,})\\s*</\\1>'), 2)]
EXT = set('sh py md rs cc so pl ts js css html htm txt log json yaml yml xml csv tsv png jpg jpeg gif\nsvg pdf zip gz bz2 xz tar exe dll jar war go java c h cpp hpp ini conf cfg env lock sql sum mod toml\nbak tmp old out bin dat db key pem crt cer pub gpg asc in am ac cmake gradle properties jsonl ipynb\nphp rb swift kt scala lua vim el tex bib rst iso img dmg deb rpm apk cs vb fs ps1 bat cmd awk sed\nservice socket timer patch diff orig rej pid pyc pyo whl egg tgz zst lz4 avro parquet'.split())
TLD = set('com net org info biz edu gov mil int io ai app dev co me tv cc us uk de fr it es nl pl\nru su xn--p1ai by kz ua uz kg am az ge md tj tm lv lt ee fi se no dk cz sk hu ro bg gr tr cn jp kr\nin br mx ar cl ca au nz za il ae sa ir vn th id my sg hk tw ch at be pt ie is lu li mc name pro mobi\nasia tel travel jobs online site website space store shop cloud tech digital network systems\nsolutions services group team live life world today news blog wiki fun art design studio agency\ncompany center email host press pub run zone works one link click gg fm to ly sh st cx ws nu tk\nlocal lan internal intranet corp test example invalid localdomain'.split())

def _hosts(text):
    for m in RX['hostname'].finditer(text):
        s = m.group(0)
        if any((c.isupper() for c in text[m.start():m.end()])):
            continue
        labels = s.split('.')
        if labels[-1] in EXT:
            continue
        if labels[-1] in TLD or (len(labels) >= 3 and 2 <= len(labels[-1]) <= 6):
            yield (m.start(), m.end(), 'hostname')
PRIORITY = {'secret': 0, 'url': 1, 'email': 2, 'card': 3, 'account': 3, 'inn': 3, 'snils': 3, 'ogrn': 3, 'ogrnip': 3, 'passport': 3, 'phone': 3, 'bik': 4, 'kpp': 4, 'ipv4': 4, 'ipv6': 4, 'mac': 4, 'hostname': 5, 'org': 5, 'handle': 6, 'login': 7}
PASS_CTX = re.compile('(?i)паспорт|сери[яию]|passport')

def detect(text):
    c = []
    for rx, gi in RX_SECRET:
        for m in rx.finditer(text):
            c.append((m.start(gi), m.end(gi), 'secret'))
    for m in RX['url'].finditer(text):
        c.append((m.start(), m.end(), 'url'))
    for m in RX['email'].finditer(text):
        c.append((m.start(), m.end(), 'email'))
    for lab in ('inn', 'snils', 'ogrn', 'ogrnip', 'card'):
        ok = {'inn': inn_ok, 'snils': snils_ok, 'ogrn': ogrn_ok, 'ogrnip': ogrn_ok, 'card': luhn_ok}[lab]
        for m in RX[lab].finditer(text):
            d = _dig(m.group(0))
            if (lab != 'card' or 13 <= len(d) <= 19) and ok(d):
                c.append((m.start(), m.end(), lab))
    biks = [(m.start(), m.group(0)) for m in RX['bik'].finditer(text)]
    for pos, b in biks:
        c.append((pos, pos + 9, 'bik'))
    for m in RX['account'].finditer(text):
        near = [b for p, b in biks if abs(p - m.start()) < 200]
        if not near or any((account_ok(m.group(0), b) for b in near)):
            c.append((m.start(), m.end(), 'account'))
    for m in RX['kpp'].finditer(text):
        if re.search('(?i)кпп|kpp', text[max(0, m.start() - 30):m.start()]):
            c.append((m.start(), m.end(), 'kpp'))
    for m in RX['passport_fmt'].finditer(text):
        c.append((m.start(), m.end(), 'passport'))
    for m in RX['passport_ctx'].finditer(text):
        if PASS_CTX.search(text[max(0, m.start() - 40):m.start()]):
            c.append((m.start(), m.end(), 'passport'))
    for lab in ('phone_ru', 'phone_intl'):
        for m in RX[lab].finditer(text):
            if 8 <= len(_dig(m.group(0))) <= 15:
                c.append((m.start(), m.end(), 'phone'))
    for m in RX['ipv4'].finditer(text):
        try:
            ipaddress.IPv4Address(m.group(0))
        except ValueError:
            continue
        c.append((m.start(), m.end(), 'ipv4'))
    for m in RX['ipv6'].finditer(text):
        try:
            ipaddress.IPv6Address(m.group(0))
        except ValueError:
            continue
        c.append((m.start(), m.end(), 'ipv6'))
    for m in RX['mac'].finditer(text):
        c.append((m.start(), m.end(), 'mac'))
    c.extend(_hosts(text))
    for lab in ('org_pre', 'org_post'):
        for m in RX[lab].finditer(text):
            c.append((m.start(), m.end(), 'org'))
    for m in RX['handle'].finditer(text):
        c.append((m.start(), m.end(), 'handle'))
    for rx in RX_LOGIN:
        for m in rx.finditer(text):
            c.append((m.start(), m.end(), 'login'))
    out, taken = ([], [])
    for a, b, lab in sorted(c, key=lambda x: (PRIORITY[x[2]], -(x[1] - x[0]), x[0])):
        if a >= b or any((a < y and b > x for x, y in taken)):
            continue
        taken.append((a, b))
        out.append({'start': a, 'end': b, 'label': lab})
    out.sort(key=lambda s: s['start'])
    return out

def run(benches):
    for bench in benches:
        rows = list(csv.DictReader((ROOT / 'BENCH' / bench / 'bench.csv').open(newline='')))
        if not rows:
            print(f'rules-ru/{bench}: empty bench.csv, skipped')
            continue
        out = ROOT / 'RESULTS' / bench / 'pred.rules-ru.jsonl'
        out.parent.mkdir(parents=True, exist_ok=True)
        res, errs, nchars, t0 = ([], 0, 0, time.perf_counter())
        for r in rows:
            nchars += len(r['text'])
            t1 = time.perf_counter()
            try:
                spans, err = (detect(r['text']), None)
            except Exception as e:
                spans, err, errs = ([], f'{type(e).__name__}: {e}', errs + 1)
            res.append({'id': r['id'], 'spans': spans, 'ms': round((time.perf_counter() - t1) * 1000, 3), 'err': err})
        el = time.perf_counter() - t0
        sha = bench_sha256(ROOT / 'BENCH' / bench / 'bench.csv')
        meta = {'name': 'rules-ru', 'repo': 'SCRIPTS/rules_ru.py', 'revision': VERSION, 'family': 'rules', 'protocol': PROTOCOL, 'bench': bench, 'bench_sha256': sha, **machine(), 'device': 'cpu', 'rows': len(rows), 'chars': nchars, 'elapsed_s': round(el, 1), 'rows_per_s': round(len(rows) / el, 1), 'errors': errs, 'started': time.strftime('%Y-%m-%d %H:%M:%S')}
        with out.open('w') as fh:
            fh.write(json.dumps({'meta': meta}, ensure_ascii=False) + '\n')
            for o in res:
                fh.write(json.dumps(o, ensure_ascii=False) + '\n')
        by = {}
        for o in res:
            for s in o['spans']:
                by[s['label']] = by.get(s['label'], 0) + 1
        n = sum(by.values())
        print(f'rules-ru/{bench}: {len(rows)} rows, {nchars} characters, findings {n}, {el:.1f}s -> {out}')
        print('   ' + ', '.join((f'{k} {v}' for k, v in sorted(by.items(), key=lambda x: -x[1]))))

def selftest():

    def labs(t):
        return {s['label']: t[s['start']:s['end']] for s in detect(t)}
    assert inn_ok('7707083893') and inn_ok('500100732259') and (not inn_ok('7707083894'))
    assert snils_ok('11223344595') and (not snils_ok('11223344596'))
    assert ogrn_ok('1027700132195') and (not ogrn_ok('1027700132196'))
    assert ogrn_ok('304500116000157') and (not ogrn_ok('304500116000158'))
    assert luhn_ok('4111111111111111') and (not luhn_ok('4111111111111112'))
    assert account_ok('40702810900000005555', '044525225')
    assert not account_ok('40702810900000005556', '044525225')
    assert labs('ИНН 7707083893 в акте')['inn'] == '7707083893'
    assert 'inn' not in labs('ИНН 7707083894 в акте')
    assert labs('СНИЛС 112-233-445 95')['snils'] == '112-233-445 95'
    assert 'snils' not in labs('СНИЛС 112-233-445 96')
    assert labs('ОГРН 1027700132195')['ogrn'] == '1027700132195'
    assert labs('ОГРНИП 304500116000157')['ogrnip'] == '304500116000157'
    assert labs('КПП 770701001 у контрагента')['kpp'] == '770701001'
    assert 'kpp' not in labs('код 770701001 у контрагента')
    assert labs('БИК 044525225')['bik'] == '044525225'
    assert labs('БИК 044525225, счёт 40702810900000005555')['account'] == '40702810900000005555'
    assert 'account' not in labs('БИК 044525225, счёт 40702810900000005556')
    assert labs('счёт 40702810900000005556 без БИК')['account'] == '40702810900000005556'
    assert labs('карта 4111 1111 1111 1111')['card'] == '4111 1111 1111 1111'
    assert 'card' not in labs('карта 4111 1111 1111 1112')
    assert labs('паспорт 4509 123456')['passport'] == '4509 123456'
    assert labs('серия 45 09 123456')['passport'] == '45 09 123456'
    assert 'passport' not in labs('заказ 4509 123456 отгружен')
    assert labs('тел. +7 (926) 123-45-67')['phone'] == '+7 (926) 123-45-67'
    assert labs('звонить 89261234567')['phone'] == '89261234567'
    assert labs('call +442071234567')['phone'] == '+442071234567'
    assert labs('пишите на ivan.petrov@example.com')['email'] == 'ivan.petrov@example.com'
    assert labs('хост 10.20.30.40 упал')['ipv4'] == '10.20.30.40'
    assert 'ipv4' not in labs('версия 10.20.300.40')
    assert labs('адрес 2001:0db8:85a3:0000:0000:8a2e:0370:7334')['ipv6'].startswith('2001:')
    assert 'ipv6' not in labs('встреча в 03:14 и 05:20')
    assert labs('mac 00:1a:2b:3c:4d:5e')['mac'] == '00:1a:2b:3c:4d:5e'
    assert labs('см. https://example.com/a?b=1')['url'] == 'https://example.com/a?b=1'
    assert labs('сервер app-01.corp.example.com недоступен')['hostname'] == 'app-01.corp.example.com'
    assert 'hostname' not in labs('правь run.sh и main.py')
    assert labs('оплатил ООО «Ромашка-Сервис» вчера')['org'] == 'ООО «Ромашка-Сервис»'
    assert labs('подрядчик ЗАО "Вектор" сорвал срок')['org'] == 'ЗАО "Вектор"'
    assert labs('договор с ИП Иванов Пётр Сергеевич')['org'] == 'ИП Иванов Пётр Сергеевич'
    assert labs('vendor Acme Systems Inc. shipped')['org'] == 'Acme Systems Inc.'
    assert labs('НПО «Трофимов, Тихонов и Герасимова» подписало')['org'] == 'НПО «Трофимов, Тихонов и Герасимова»'
    assert 'org' not in labs('зарегистрировано как ООО. подробности ниже')
    assert 'org' not in labs('форма «ООО» и форма «АО» отличаются')
    assert labs('пиши @ivan_petrov')['handle'] == '@ivan_petrov'
    assert 'handle' not in labs('почта a@example.com')
    assert labs('логин a.ivanov сброшен')['login'] == 'a.ivanov'
    assert labs('логин ivanov_a сброшен')['login'] == 'ivanov_a'
    assert labs('создан adm_backup')['login'] == 'adm_backup'
    assert labs('учётка i.ivanov@ без домена')['login'] == 'i.ivanov@'
    for t, want in [('token ghp_abcdefghijklmnopqrstuvwxyz0123456789', 'ghp_abcdefghijklmnopqrstuvwxyz0123456789'), ('GITLAB glpat-ABCDEFGHIJKLMNOPQRST x', 'glpat-ABCDEFGHIJKLMNOPQRST'), ('slack xoxb-123456789012-abcdefghijkl', 'xoxb-123456789012-abcdefghijkl'), ('aws AKIAIOSFODNN7EXAMPLE', 'AKIAIOSFODNN7EXAMPLE'), ('key sk-abcdefghijklmnopqrstuvwx', 'sk-abcdefghijklmnopqrstuvwx'), ('g AIzaSyA0123456789abcdefghijklmnopqrstuvw', 'AIzaSyA0123456789abcdefghijklmnopqrstuvw'), ('oauth ya29.a0AfH6SMBabcdefghijklmnop', 'ya29.a0AfH6SMBabcdefghijklmnop'), ('jwt eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.dBjftJeZ4CVPmB92K27uhbUJU1p1r_wW1g', 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.dBjftJeZ4CVPmB92K27uhbUJU1p1r_wW1g'), ('dsn postgres://svc:s3cr3tpw@db.example.com:5432/app', 'postgres://svc:s3cr3tpw@db.example.com:5432/app'), ('Authorization: Bearer abcdef1234567890abcdef', 'abcdef1234567890abcdef'), ('PGPASSWORD=s3cr3tpw psql', 's3cr3tpw'), ('пароль: Qwerty12345', 'Qwerty12345'), ('db.example.com:5432:app:svc:s3cr3tpw', 's3cr3tpw'), ('<apiToken>\n  9f8e7d6c5b4a3210\n</apiToken>', '9f8e7d6c5b4a3210')]:
        assert labs(t).get('secret') == want, (t, labs(t))
    assert 'secret' in labs('-----BEGIN RSA PRIVATE KEY-----\nMIIBOgIBAAJB\n-----END RSA PRIVATE KEY-----')
    assert not detect('обычный текст без всякого, просто слова и запятые')
    print('selftest ok')
if __name__ == '__main__':
    args = sys.argv[1:]
    if '--selftest' in args:
        selftest()
    else:
        run(args or sorted((d.name for d in (ROOT / 'BENCH').iterdir() if (d / 'bench.csv').exists())))
