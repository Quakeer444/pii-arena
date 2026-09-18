"""Check and rescore one stored prediction without overwriting reports."""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--dataset', required=True)
    parser.add_argument('--model', required=True)
    args = parser.parse_args()
    for name in (args.dataset, args.model):
        if not name or Path(name).name != name or name in ('.', '..'):
            parser.error('Dataset and model must be single path components')
    if any(os.environ.get(k) == '1' for k in ('ALLOW_ERR', 'ALLOW_STALE')):
        parser.error('Publication rescoring requires ALLOW_ERR and ALLOW_STALE to be unset')
    os.environ['BENCHMARK_DATA'] = str(args.data.resolve())
    sys.path.insert(0, str(ROOT / 'benchmark'))
    import score as S
    f = S.RESULTS / args.dataset / f'pred.{args.model}.jsonl'
    meta, predictions = S.read_pred(f)
    if bad := S.check_predictions(f, meta, predictions, complete=True, expected=args.dataset, expected_model=args.model):
        raise SystemExit(bad)
    _, counts = S.load_model(f, S.gold(args.dataset)[0], S.meta_of(args.dataset)['groups'])
    print(json.dumps({'dataset': args.dataset, 'model': args.model,
                      'missed': sum(counts['ofn']), 'gold_spans': sum(counts['ng']),
                      'fully_hidden': sum(counts['hid']), 'char_tp': sum(counts['tp']),
                      'char_fp': sum(counts['fp']), 'char_fn': sum(counts['fn']),
                      'dropped_spans': counts['bad'], 'train': args.dataset in S.dirty(args.model)}, indent=2))


if __name__ == '__main__':
    main()
