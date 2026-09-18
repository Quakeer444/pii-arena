import json
from pathlib import Path

def normalize_legacy_extra_special_tokens(path: str | Path) -> bool:
    path = Path(path)
    config = json.loads(path.read_text())
    legacy = config.get('extra_special_tokens')
    if not isinstance(legacy, list):
        return False
    additional = config.get('additional_special_tokens')
    if not isinstance(additional, list):
        additional = []
    config.pop('extra_special_tokens')
    config['additional_special_tokens'] = list(dict.fromkeys([*additional, *legacy]))
    if path.is_symlink():
        path.unlink()
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
    return True

def normalize_tokenizer_class(path: str | Path, tokenizer_class: str) -> bool:
    path = Path(path)
    target = path.resolve(strict=True)
    config = json.loads(target.read_text())
    if config.get('tokenizer_class') == tokenizer_class and 'backend' not in config:
        return False
    config['tokenizer_class'] = tokenizer_class
    config.pop('backend', None)
    target.write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
    return True

def cap_tokenizer_model_length(pipe) -> bool:
    tokenizer = getattr(pipe, 'tokenizer', None)
    config = getattr(getattr(pipe, 'model', None), 'config', None)
    maximum = getattr(config, 'max_position_embeddings', None)
    if tokenizer is None or not isinstance(maximum, int) or maximum <= 0:
        return False
    current = getattr(tokenizer, 'model_max_length', maximum)
    if not isinstance(current, int) or current <= 0:
        current = maximum
    tokenizer.model_max_length = min(current, maximum)
    return bool(getattr(tokenizer, 'is_fast', False))

def disable_modernbert_reference_compile(model) -> bool:
    inner = getattr(model, 'model', None)
    token_layer = getattr(inner, 'token_rep_layer', None)
    backbone = getattr(token_layer, 'bert_layer', None)
    backbone_model = getattr(backbone, 'model', backbone)
    config = getattr(backbone_model, 'config', None)
    if config is None or not hasattr(config, 'reference_compile'):
        return False
    config.reference_compile = False
    return True

def prepare_stream_tokenizer(repo: str, revision: str | None=None) -> bool:
    from huggingface_hub import snapshot_download
    snapshot = Path(snapshot_download(repo, revision=revision, allow_patterns=['tokenizer_config.json']))
    return normalize_legacy_extra_special_tokens(snapshot / 'tokenizer_config.json')
