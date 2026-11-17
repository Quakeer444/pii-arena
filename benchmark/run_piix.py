"""Run the released PIIX detector on one Arena dataset."""
import argparse
import sys
from pathlib import Path

NAME = "piix-560m"
REPO = "Tracer-ML/PIIX-560m"
REVISION = "26d15846b62cb2bd1822871946c884f73879ca47"
RELEASE_FILES = (
    "piix.py", "rules.py", "type_filter.py", "config.json",
    "tokenizer.json", "tokenizer_config.json", "model.safetensors",
)


def release_class(snapshot):
    # The release imports its helpers by their top-level names.
    for name in ("piix", "rules", "type_filter"):
        source = snapshot / f"{name}.py"
        if not source.is_file():
            raise FileNotFoundError(source)
        loaded = sys.modules.get(name)
        if loaded is not None and Path(getattr(loaded, "__file__", "") or "").resolve() != source.resolve():
            raise ImportError(f"{name} is already loaded from outside the PIIX release")
    sys.path.insert(0, str(snapshot))
    try:
        from piix import Redactor
    finally:
        sys.path.pop(0)
    return Redactor


def load(repo, labels, *, revision, device, batch, recall):
    from huggingface_hub import snapshot_download

    snapshot = Path(snapshot_download(repo, revision=revision, allow_patterns=list(RELEASE_FILES))).resolve()
    redactor = release_class(snapshot)(snapshot, device=device, batch=batch)

    def predict(texts):
        results = redactor.find(list(texts), types=labels, recall=recall)
        return [[{"start": a, "end": b, "label": "pii"} for a, b in result["mask"]] for result in results]

    return predict, redactor.model


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset")
    parser.add_argument("--recall", type=int, choices=(0, 8), default=0)
    parser.add_argument("--batch", type=int, default=32)
    args = parser.parse_args()
    if Path(args.dataset).name != args.dataset or args.dataset in ("", ".", ".."):
        parser.error("dataset must be a single Arena dataset ID")
    if args.batch < 1:
        parser.error("--batch must be positive")

    import run

    def loader(repo, labels, *, revision):
        return load(repo, labels, revision=revision, device=run.DEV, batch=args.batch, recall=args.recall)

    # Register for this invocation while the results release remains frozen.
    run.CFG[NAME] = {"repo": REPO, "revision": REVISION, "family": "piix", "labels": "en"}
    run.LOADERS["piix"] = loader
    run.PINNED += ("piix",)
    run.ZERO_SHOT += ("piix",)
    run.CHUNK = 0
    run.VARIANT = "r8" if args.recall == 8 else ""
    run.main(NAME, args.dataset, args.batch)


if __name__ == "__main__":
    main()
