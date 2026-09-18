import hashlib, json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from benchlib import BENCH, RAW
PATHS = {'hivetrace': ['hivetrace/domain-00000-of-00001.parquet', 'hivetrace/entity-00000-of-00001.parquet'], 'russian-pii-66k': ['train-00000-of-00001.parquet'], 'redmadrobot': ['redmadrobot-test.csv'], 'scanpatch': ['scanpatch/train.parquet', 'scanpatch/test.parquet'], 'alrosait': ['alrosait-pii-synthetic-ru.jsonl'], 'jayguard': ['jayguard/train.parquet'], 'nym-ru': ['nym-pii-test.jsonl', 'nym-pii-validation.jsonl'], 'nym-en': ['nym-pii-test.jsonl', 'nym-pii-validation.jsonl'], 'nym-multi': ['nym-pii-test.jsonl', 'nym-pii-validation.jsonl'], 'secrets-issues': ['issue-reports/test.csv', 'issue-reports/test_wild.csv'], 'secrets-rules': ['secret-rules/gitleaks_tpfp.jsonl', 'secret-rules/betterleaks_tpfp.jsonl'], 'alexen2': ['alexen2-pii-ner-ru-benchmark-test.parquet'], 'nerel': ['nerel/train.jsonl', 'nerel/dev.jsonl', 'nerel/test.jsonl'], 'factrueval': ['factrueval-2016/devset', 'factrueval-2016/testset'], 'rubai-ru': ['rubai/data.jsonl'], 'multiconer-ru': ['multiconer-v1/RU-Russian/ru_test.conll'], 'redact-ru': ['redact/pii_benchmark_full.json'], 'redact-multi': ['redact/pii_benchmark_full.json'], 'ameau01': ['it-support-tickets/train.parquet', 'it-support-tickets/pii.json', 'it-support-tickets/retention.json'], 'tonicai': ['tonicai-privacy-bench/ground_truth', 'tonicai-privacy-bench/tasks'], 'kiji-en': ['kiji/data/test-00000-of-00001.parquet'], 'kiji-multi': ['kiji/data/test-00000-of-00001.parquet'], 'arthur-passwords': ['arthur-passwords/sensitive_data_password.csv'], 'nemotron-pii': ['nemotron-pii/data/test-00000-of-00001.parquet'], 'tab-echr': ['tab-echr/echr_test.zip'], 'dialogpii-en': ['dialogpii/DialogPII.zip'], 'dialogpii-multi': ['dialogpii/DialogPII.zip'], 'gretel-multi': ['gretel-finance-test.parquet'], 'privy': ['privy/privy-dataset.zip'], 'creddata': ['creddata/meta', 'creddata/data'], 'leak-museum': ['leak-museum'], 'leaky-repo': ['leaky-repo']}
REV = {'secrets-issues': 'zenodo.19622962', 'dialogpii-en': 'zenodo.20863452', 'dialogpii-multi': 'zenodo.20863452', 'secrets-rules': 'gitleaks b58d3f10, betterleaks 95237cf8'}
SKIP = {'.git', '.cache'}

def files(rel):
    p = RAW / rel
    if p.is_file():
        return [p]
    return sorted((x for x in p.rglob('*') if x.is_file() and (not set(x.relative_to(p).parts) & SKIP)))

def revision(bench, paths):
    top = RAW / paths[0].split('/')[0]
    dl = top / '.cache' / 'huggingface' / 'download'
    for rel in paths:
        rest = rel.split('/', 1)[1] if '/' in rel else ''
        if not rest or not dl.is_dir():
            continue
        cands = [dl / (rest + '.metadata')] + (sorted((dl / rest).rglob('*.metadata')) if (dl / rest).is_dir() else [])
        for m in cands:
            if m.is_file():
                return 'hf ' + m.read_text().splitlines()[0]
    if (top / '.git').is_dir():
        p = subprocess.run(['git', '-C', str(top), 'rev-parse', 'HEAD'], capture_output=True, text=True)
        if p.returncode == 0:
            return 'git ' + p.stdout.strip()
    return REV.get(bench, '-')

def fingerprint(paths):
    h, n, size = (hashlib.sha256(), 0, 0)
    for rel in paths:
        for f in files(rel):
            h.update(f'{f.relative_to(RAW).as_posix()}\x00{hashlib.sha256(f.read_bytes()).hexdigest()}\n'.encode())
            n += 1
            size += f.stat().st_size
    return (h.hexdigest(), n, size)

def main(args):
    check = '--check' in args
    names = [a for a in args if a != '--check'] or sorted((d.name for d in BENCH.iterdir() if (d / 'meta.json').exists()))
    missing = []
    for name in names:
        meta = json.loads((BENCH / name / 'meta.json').read_text())
        paths = PATHS.get(meta.get('base') or name)
        if not paths:
            continue
        lost = [rel for rel in paths if not (RAW / rel).exists()]
        if lost:
            missing += [(name, rel) for rel in lost]
            continue
        if check:
            continue
        sha, n, size = fingerprint(paths)
        meta['raw'] = {'paths': paths, 'files': n, 'bytes': size, 'sha256': sha, 'revision': revision(name, paths)}
        (BENCH / name / 'meta.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1) + '\n')
        print(f"{name}: {n} files, {size / 1000000.0:.1f} MB, {sha[:12]}, {meta['raw']['revision']}")
    for name, rel in missing:
        print(f'! {name}: missing BENCH/raw/{rel}')
    if missing:
        sys.exit(1)
    if check:
        print('Raw sources verified')
if __name__ == '__main__':
    main(sys.argv[1:])
