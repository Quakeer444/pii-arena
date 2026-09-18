import csv, importlib.metadata as md, json, os, re, resource, sys, time, unicodedata
from pathlib import Path
if os.environ.get('THREADS'):
    os.environ['OMP_NUM_THREADS'] = os.environ['THREADS']
from benchlib import PROTOCOL, bench_sha256, machine
try:
    import tomllib
except ImportError:
    import tomli as tomllib
E = os.environ.get
ROOT = Path(os.environ.get('BENCHMARK_DATA', str(Path(__file__).resolve().parent.parent / '.local' / 'research'))).resolve()
BENCH, MODELS = (ROOT / 'BENCH', ROOT / 'MODELS')
RESULTS = Path(E('OUT') or ROOT / 'RESULTS')
CFG = tomllib.loads((Path(__file__).with_name('models.toml')).read_text())['models']
CHUNK = int(E('CHUNK', '600'))
CHUNK_MODE, OVERLAP = (E('CHUNK_MODE', 'char'), int(E('OVERLAP', '100')))
VARIANT, NORMALIZE, QUANT = (E('VARIANT', ''), E('NORMALIZE', 'none'), E('QUANT', 'none'))
THRESH, LIMIT, THREADS = (float(E('THRESH', '0.1')), int(E('LIMIT', '0')), int(E('THREADS', '0')))
ZERO_SHOT = ('gliner', 'gliner2')
QUANTABLE = ('hf', 'pplx', 'gliner')
CPU_NATIVE = ('natasha', 'spacy')
PINNED = ('opf', 'hf', 'pplx', 'gliner', 'gliner2', 'onnx', 'spacy')
PKG = {'natasha': 'natasha', 'stanza': 'stanza', 'rupii': 'ru_pii_ner'}
NO_QUANT = '-'
csv.field_size_limit(10 ** 7)
torch = None

def _torch():
    global torch
    if torch is None:
        import torch as module
        torch = module
        if THREADS:
            torch.set_num_threads(THREADS)
    return torch
if E('DEVICE') == 'cpu':
    DEV = 'cpu'
else:
    DEV = E('DEVICE') or ('cuda' if _torch().cuda.is_available() else 'cpu')
_WORD = re.compile('\\w+')
_SENT = re.compile('[.!?…]\\s|\\n')
_LAT2CYR = dict(zip('aeopcxykmthbAEOPCXYKMTHB', 'аеорсхукмтнвАЕОРСХУКМТНВ'))
_CYR2LAT = {v: k for k, v in _LAT2CYR.items()}

def rows(bench):
    for r in csv.DictReader((BENCH / bench / 'bench.csv').open(newline='')):
        yield (r['id'], r['text'])

def zs_labels(bench, lang):
    p = BENCH / bench / 'meta.json'
    if not p.exists():
        sys.exit(f'Missing {p}: zero-shot labels require the dataset meta.json labels field')
    return json.loads(p.read_text())['labels'][lang]

def chunks(text):
    if not CHUNK:
        return [(0, text)]
    if CHUNK_MODE == 'overlap':
        step = max(1, CHUNK - OVERLAP)
        return [(p, text[p:p + CHUNK]) for p in range(0, max(1, len(text)), step)]
    out, pos = ([], 0)
    while len(text) - pos > CHUNK:
        cut = -1
        if CHUNK_MODE == 'sent':
            ends = [m.end() for m in _SENT.finditer(text, pos + 1, pos + CHUNK)]
            cut = ends[-1] if ends else -1
        if cut < 0:
            cut = text.rfind('\n', pos + 1, pos + CHUNK)
        if cut < 0:
            cut = text.rfind(' ', pos + 1, pos + CHUNK)
        if cut < 0:
            cut = pos + CHUNK
        out.append((pos, text[pos:cut]))
        pos = cut
    out.append((pos, text[pos:]))
    return out

def normalize(text):
    if NORMALIZE == 'homoglyph':
        out = list(text)
        for m in _WORD.finditer(text):
            w = m.group()
            lat = sum((c.isascii() and c.isalpha() for c in w))
            cyr = sum((c.isalpha() and (not c.isascii()) for c in w))
            tab = _LAT2CYR if cyr > lat else _CYR2LAT if lat > cyr else None
            if tab:
                out[m.start():m.end()] = [tab.get(c, c) for c in w]
        return (''.join(out), None)
    if NORMALIZE == 'nfkc':
        out, back = ([], [])
        for i, ch in enumerate(text):
            s = unicodedata.normalize('NFKC', ch) or ch
            out.append(s)
            back += [i] * len(s)
        return (''.join(out), back)
    return (text, None)

def to_source(back, a, b):
    if not back or b <= a:
        return (a, b)
    return (back[min(a, len(back) - 1)], back[min(b, len(back)) - 1] + 1)

def clip(s, n):
    a, b = (max(0, int(s['start'])), min(int(s['end']), n))
    return None if b <= a else (a, b)

def _span(e):
    lab = e['entity_group']
    for p in ('E-', 'S-', 'B-', 'I-', 'L-', 'U-'):
        lab = lab.removeprefix(p)
    out = {'start': int(e['start']), 'end': int(e['end']), 'label': lab}
    if e.get('score') is not None:
        out['score'] = round(float(e['score']), 4)
    return out

def _hf(path, _labels, **kw):
    from transformers import pipeline
    from tokenizer_compat import cap_tokenizer_model_length
    model = str(path) if isinstance(path, (str, Path)) else path
    pipe = pipeline('token-classification', model=model, aggregation_strategy='simple', device=kw.pop('device', 0 if DEV == 'cuda' else -1), **kw)
    use_stride = cap_tokenizer_model_length(pipe)

    def predict(texts):
        call = {'batch_size': len(texts)}
        if use_stride:
            call['stride'] = 64
        return [[_span(e) for e in out] for out in pipe(texts, **call)]
    return (predict, pipe.model)

def _opf(repo, labels, **kw):
    import prep
    rev = kw.pop('revision', None)
    path = MODELS / (repo.split('/')[-1] + '-hf')
    if not (path / 'config.json').exists():
        prep.main(repo, rev)
    got = json.loads((path / 'source.json').read_text())['sha']
    if rev and got != rev:
        sys.exit(f'{repo}: local export revision {got}, catalog revision {rev}; remove {path}')
    return _hf(path, labels, **kw)

def _pplx(repo, _labels, **kw):
    torch = _torch()
    import transformers.modeling_utils as mu
    from transformers import AutoModel
    orig = mu.PreTrainedModel.post_init

    def safe(self):
        if getattr(self, '_keep_in_fp32_modules_strict', None):
            self._keep_in_fp32_modules_strict = [m for m in self._keep_in_fp32_modules_strict if not m.startswith('viterbi.')]
        return orig(self)
    mu.PreTrainedModel.post_init = safe
    m = AutoModel.from_pretrained(repo, trust_remote_code=True, torch_dtype=torch.float32, revision=kw.get('revision')).to(DEV).eval()

    def predict(texts):
        out = []
        for t in texts:
            spans, _ = m.predict(t)
            out.append([{'start': s.start, 'end': s.end, 'label': s.label} for s in spans])
        return out
    return (predict, m)

def _gliner(repo, labels, **kw):
    if repo == 'knowledgator/gliner-stream-pii-v1.0':
        from tokenizer_compat import prepare_stream_tokenizer
        prepare_stream_tokenizer(repo, kw.get('revision'))
    from gliner import GLiNER
    m = GLiNER.from_pretrained(repo, revision=kw.get('revision'))
    if repo == 'knowledgator/gliner-pii-edge-v1.0':
        from tokenizer_compat import disable_modernbert_reference_compile
        if not disable_modernbert_reference_compile(m):
            raise RuntimeError('gliner-pii-edge ModernBERT backbone not found')
    m = m.to(DEV).eval()

    def predict(texts):
        res = m.batch_predict_entities(texts, labels, threshold=THRESH)
        return [[{'start': int(e['start']), 'end': int(e['end']), 'label': e['label'], 'score': round(float(e.get('score', 0.0)), 4)} for e in r] for r in res]
    return (predict, getattr(m, 'model', None))

def _gliner2(repo, labels, **kw):
    from gliner2 import AutoExtractor
    m = AutoExtractor.from_pretrained(repo, revision=kw.get('revision'))
    if DEV == 'cuda':
        m = m.cuda()
    m.eval()

    def one(r):
        return [{'start': int(it['start']), 'end': int(it['end']), 'label': lab, 'score': round(float(it.get('confidence', 0.0)), 4)} for lab, items in r['entities'].items() for it in items]

    def predict(texts):
        kw = dict(include_spans=True, include_confidence=True, threshold=THRESH)
        if hasattr(m, 'batch_extract_entities'):
            return [one(r) for r in m.batch_extract_entities(texts, labels, batch_size=len(texts), **kw)]
        return [one(m.extract_entities(t, labels, **kw)) for t in texts]
    return (predict, m)

def _rupii(_repo, _labels, **_kw):
    from ru_pii_ner import load
    m = load()

    def predict(texts):
        return [[{'start': int(e['start']), 'end': int(e['end']), 'label': e['entity_group']} for e in m.predict(t)] for t in texts]
    return (predict, getattr(m, 'model', None))

def _tok(path, revision=None):
    from transformers import AutoTokenizer, PreTrainedTokenizerFast
    try:
        return AutoTokenizer.from_pretrained(path, revision=revision)
    except ValueError:
        return PreTrainedTokenizerFast.from_pretrained(path, tokenizer_class=None, revision=revision, extra_special_tokens={})

def _onnx(repo, labels, subfolder='onnx', **kw):
    from optimum.onnxruntime import ORTModelForTokenClassification
    model = ORTModelForTokenClassification.from_pretrained(repo, subfolder=subfolder, provider='CPUExecutionProvider', **kw)
    predict, _ = _hf(model, labels, tokenizer=_tok(repo, kw.get('revision')), device=-1)
    return (predict, None)

def _natasha(_repo, _labels, **_kw):
    from natasha import NewsEmbedding, NewsNERTagger
    tagger = NewsNERTagger(NewsEmbedding())

    def predict(texts):
        indexed = [(i, text) for i, text in enumerate(texts) if text.strip()]
        out = [[] for _ in texts]
        if indexed:
            markups = tagger.map([text for _, text in indexed])
            for (i, _), markup in zip(indexed, markups, strict=True):
                out[i] = [{'start': s.start, 'end': s.stop, 'label': s.type} for s in markup.spans]
        return out
    return (predict, None)

def _spacy(repo, _labels, **kw):
    import spacy
    from huggingface_hub import snapshot_download
    path = Path(snapshot_download(repo, revision=kw.get('revision'), ignore_patterns=['*.whl']))
    keep = ('tok2vec', 'transformer', 'ner')
    names = json.loads((path / 'meta.json').read_text())['pipeline']
    nlp = spacy.load(path, exclude=[n for n in names if n not in keep])

    def predict(texts):
        return [[{'start': e.start_char, 'end': e.end_char, 'label': e.label_} for e in d.ents] for d in nlp.pipe(texts)]
    return (predict, None)

def _stanza(_repo, _labels, **_kw):
    import stanza
    nlp = stanza.Pipeline('ru', processors='tokenize,ner', use_gpu=DEV == 'cuda', verbose=False)

    def predict(texts):
        out = []
        for t in texts:
            if not t.strip():
                out.append([])
                continue
            out.append([{'start': e.start_char, 'end': e.end_char, 'label': e.type} for e in nlp(t).ents])
        return out
    return (predict, None)
LOADERS = {'opf': _opf, 'hf': _hf, 'pplx': _pplx, 'gliner': _gliner, 'gliner2': _gliner2, 'rupii': _rupii, 'onnx': _onnx, 'natasha': _natasha, 'spacy': _spacy, 'stanza': _stanza}

def revision(cfg):
    try:
        if cfg['family'] == 'opf':
            return json.loads((MODELS / (cfg['repo'].split('/')[-1] + '-hf') / 'source.json').read_text())['sha']
        if cfg['family'] in PINNED:
            return cfg['revision']
        return f"{PKG[cfg['family']]} {md.version(PKG[cfg['family']])}"
    except Exception as e:
        return f'unknown ({type(e).__name__})'

def versions():
    out = {}
    for p in ('torch', 'transformers', 'gliner', 'gliner2', 'optimum', 'onnxruntime', 'peft', 'ru_pii_ner', 'natasha', 'slovnet', 'spacy', 'stanza'):
        try:
            out[p] = md.version(p)
        except md.PackageNotFoundError:
            pass
    return out

def rss_mb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return round(r / (1 << 20) if sys.platform == 'darwin' else r / 1024, 1)

def main(name, bench, batch='16'):
    global DEV
    started_utc = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    cfg, batch = (CFG[name], int(batch))
    if cfg['family'] not in CPU_NATIVE:
        _torch()
    if cfg['family'] == 'onnx':
        DEV = 'cpu'
    lang = cfg.get('labels', 'en')
    labels = zs_labels(bench, lang) if cfg['family'] in ZERO_SHOT else None
    kw = {k: v for k, v in cfg.items() if k in ('subfolder', 'file_name', 'trust_remote_code')}
    if cfg['family'] in PINNED:
        if len(cfg.get('revision', '')) != 40:
            sys.exit(f'{name}: models.toml has no pinned revision; refusing an unpinned model download')
        kw['revision'] = cfg['revision']
    predict, module = LOADERS[cfg['family']](cfg['repo'], labels, **kw)
    params = sum((p.numel() for p in module.parameters())) if module is not None else None
    quant = QUANT if cfg['family'] in QUANTABLE and module is not None else NO_QUANT
    if quant in ('none', ''):
        quant = NO_QUANT
    if quant == 'int8':
        keep = {n.split('.')[0] for n in getattr(module, '_keep_in_fp32_modules_strict', None) or ()}
        targets = [c for n, c in module.named_children() if n not in keep] if keep else [module]
        for t in targets:
            torch.ao.quantization.quantize_dynamic(t, {torch.nn.Linear}, dtype=torch.qint8, inplace=True)
    data = list(rows(bench))[:LIMIT or None]
    norm = [normalize(text) for _, text in data]
    pieces = [(i, off, piece) for i, (t, _) in enumerate(norm) for off, piece in chunks(t)]
    spans, ms, errs = ([[] for _ in data], [0.0] * len(data), [None] * len(data))
    clipped = dropped = 0
    t0 = time.perf_counter()
    for k in range(0, len(pieces), batch):
        part = pieces[k:k + batch]
        t1 = time.perf_counter()
        try:
            outs = predict([p for _, _, p in part])
            if len(outs) != len(part):
                raise RuntimeError(f'predict returned {len(outs)} outputs for {len(part)} inputs')
        except Exception:
            outs = []
            for _, _, p in part:
                try:
                    outs.append(predict([p])[0])
                except Exception as e:
                    outs.append(e)
        dt = (time.perf_counter() - t1) * 1000 / len(part)
        for (i, off, piece), out in zip(part, outs):
            ms[i] += dt
            if isinstance(out, Exception):
                errs[i] = repr(out)[:200]
                continue
            for s in out:
                if (ab := clip(s, len(piece))) is None:
                    dropped += 1
                    continue
                clipped += ab != (s['start'], s['end'])
                a, b = to_source(norm[i][1], ab[0] + off, ab[1] + off)
                spans[i].append({**s, 'start': a, 'end': b})
        if k // batch % 20 == 0:
            print(f'[{name}/{bench}] {k + len(part)}/{len(pieces)} chunks in {time.perf_counter() - t0:.0f}s', flush=True)
    elapsed = time.perf_counter() - t0
    chars = sum((len(text) for _, text in data))
    sha = bench_sha256(BENCH / bench / 'bench.csv')
    meta = {'name': name, 'repo': cfg['repo'], 'revision': revision(cfg), 'family': cfg['family'], 'protocol': PROTOCOL, 'bench': bench, 'bench_sha256': sha, 'variant': VARIANT, 'device': DEV, 'gpu': torch.cuda.get_device_name(0) if DEV == 'cuda' else None, **machine(), 'params': params, 'threads': THREADS or None, 'quant': quant, 'rss_mb': rss_mb(), 'batch': batch, 'chunk': CHUNK, 'chunk_mode': CHUNK_MODE, 'overlap': OVERLAP, 'normalize': NORMALIZE, 'threshold': THRESH, 'labels_lang': lang, 'labels': labels, 'limit': LIMIT or None, 'versions': versions(), 'rows': len(data), 'pieces': len(pieces), 'chars': chars, 'clipped': clipped, 'dropped': dropped, 'elapsed_s': round(elapsed, 1), 'rows_per_s': round(len(data) / elapsed, 2), 'chars_per_s': round(chars / elapsed, 1), 'errors': sum((e is not None for e in errs)), 'started_utc': started_utc, 'finished_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    (RESULTS / bench).mkdir(parents=True, exist_ok=True)
    out = RESULTS / bench / f"pred.{name}{('+' + VARIANT if VARIANT else '')}.jsonl"
    with out.open('w') as fh:
        fh.write(json.dumps({'meta': meta}, ensure_ascii=False) + '\n')
        for (rid, _), sp, t, err in zip(data, spans, ms, errs):
            fh.write(json.dumps({'id': rid, 'spans': sp, 'ms': round(t, 1), 'err': err}, ensure_ascii=False) + '\n')
    print(f"[{name}/{bench}] complete: {len(data)} rows in {elapsed:.0f}s, errors {meta['errors']}, clipped at chunk boundary {clipped}, empty spans dropped {dropped} -> {out}", flush=True)
if __name__ == '__main__':
    main(*sys.argv[1:4])
