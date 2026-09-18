import json, os, struct, subprocess, sys
from pathlib import Path
from huggingface_hub import snapshot_download
HERE = Path(__file__).resolve().parent
MODELS = Path(os.environ.get('BENCHMARK_DATA', str(HERE.parent / '.local/research'))).resolve() / 'MODELS'

def main(repo: str, revision: str | None=None) -> Path:
    out = MODELS / (repo.split('/')[-1] + '-hf')
    if (out / 'config.json').exists():
        print('Already prepared:', out)
        return out
    snap = Path(snapshot_download(repo, revision=revision, allow_patterns=['config.json', 'model.safetensors']))
    root = json.loads((snap / 'config.json').read_text())
    src = snap
    if 'architectures' in root:
        src = Path(snapshot_download(repo, revision=revision, allow_patterns=['original/*'])) / 'original'
    subprocess.run([sys.executable, str(HERE / 'conv.py'), '--input_dir', str(src), '--output_dir', str(out)], check=True)
    names = json.loads((src / 'config.json').read_text()).get('ner_class_names')
    if names is None:
        names = [root['id2label'][str(i)] for i in range(len(root['id2label']))]
    f = next(out.glob('model*.safetensors'))
    with f.open('rb') as fh:
        hdr = json.loads(fh.read(struct.unpack('<Q', fh.read(8))[0]))
    assert hdr['score.weight']['shape'][0] == len(names)
    cfg = json.loads((out / 'config.json').read_text())
    cfg['id2label'] = {str(i): x for i, x in enumerate(names)}
    cfg['label2id'] = {x: i for i, x in enumerate(names)}
    (out / 'config.json').write_text(json.dumps(cfg, indent=2, ensure_ascii=False))
    (out / 'source.json').write_text(json.dumps({'repo': repo, 'sha': snap.name}))
    print('ok:', out, len(names), 'labels')
    return out
if __name__ == '__main__':
    main(*sys.argv[1:3])
