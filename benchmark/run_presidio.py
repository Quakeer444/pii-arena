import os
import csv, importlib.metadata, json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from benchlib import PROTOCOL, bench_sha256, machine
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngineProvider
from presidio_ru_recognizers import register_all_ru_recognizers
ROOT = Path(os.environ.get('BENCHMARK_DATA', str(Path(__file__).resolve().parent.parent / '.local' / 'research'))).resolve()
csv.field_size_limit(10 ** 7)
MODEL = 'ru_core_news_sm'

def build():
    nlp = NlpEngineProvider(nlp_configuration={'nlp_engine_name': 'spacy', 'models': [{'lang_code': 'ru', 'model_name': MODEL}]}).create_engine()
    reg = RecognizerRegistry(supported_languages=['ru'])
    reg.load_predefined_recognizers(languages=['ru'], nlp_engine=nlp)
    register_all_ru_recognizers(reg)
    return AnalyzerEngine(registry=reg, nlp_engine=nlp, supported_languages=['ru'])

def main(*benches):
    an = build()
    v = importlib.metadata.version
    rev = f"presidio-analyzer {v('presidio-analyzer')}, presidio-ru-recognizers {v('presidio-ru-recognizers')}, {MODEL} {v(MODEL)}"
    for bench in benches:
        rows = list(csv.DictReader((ROOT / 'BENCH' / bench / 'bench.csv').open(newline='')))
        res, errs, nchars, t0 = ([], 0, 0, time.perf_counter())
        for r in rows:
            nchars += len(r['text'])
            t1 = time.perf_counter()
            try:
                spans = [{'start': x.start, 'end': x.end, 'label': x.entity_type, 'score': round(float(x.score), 3)} for x in an.analyze(text=r['text'], language='ru')]
                err = None
            except Exception as e:
                spans, err, errs = ([], f'{type(e).__name__}: {e}', errs + 1)
            res.append({'id': r['id'], 'spans': spans, 'ms': round((time.perf_counter() - t1) * 1000, 3), 'err': err})
        el = time.perf_counter() - t0
        out = ROOT / 'RESULTS' / bench / 'pred.presidio-ru.jsonl'
        out.parent.mkdir(parents=True, exist_ok=True)
        meta = {'name': 'presidio-ru', 'repo': 'github.com/microsoft/presidio + brikkoAI/presidio-ru-recognizers', 'revision': rev, 'family': 'presidio', 'protocol': PROTOCOL, 'bench': bench, 'bench_sha256': bench_sha256(ROOT / 'BENCH' / bench / 'bench.csv'), **machine(), 'device': 'cpu', 'rows': len(rows), 'chars': nchars, 'elapsed_s': round(el, 1), 'rows_per_s': round(len(rows) / el, 1), 'errors': errs, 'started': time.strftime('%Y-%m-%d %H:%M:%S')}
        with out.open('w') as fh:
            fh.write(json.dumps({'meta': meta}, ensure_ascii=False) + '\n')
            for o in res:
                fh.write(json.dumps(o, ensure_ascii=False) + '\n')
        by = {}
        for o in res:
            for s in o['spans']:
                by[s['label']] = by.get(s['label'], 0) + 1
        print(f'presidio-ru/{bench}: {len(rows)} rows, findings {sum(by.values())}, errors {errs}, {el:.1f}s -> {out}')
        print('   ' + ', '.join((f'{k} {v}' for k, v in sorted(by.items(), key=lambda x: -x[1]))))
if __name__ == '__main__':
    main(*sys.argv[1:])
