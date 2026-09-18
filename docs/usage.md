# Use the benchmark

## Read before installing

Choose [a data type](../results/by-entity.md), [a dataset](../results/by-dataset.md) or [a language/task cut](../results/by-language.md). Inspect the full-hiding rate, exact denominator and unnecessary masking together. A detector that touches nearly every annotation may still leave characters exposed.

The homepage uses a fixed four-member composition for category diagnostics. Other complete compositions are compared in the [overview](../results/overview.md). The [detector catalog](models.md) identifies the actual upstream repositories and revisions. This repository provides measurements and inference adapters; it does not install every detector as one production SDK.

## Validate the published numbers

Install Python 3.12 and [uv](https://docs.astral.sh/uv/), then run from the repository root:

```sh
uv sync --frozen
uv run python scripts/verify.py
```

The command checks numeric invariants, category aggregation, local links, publication boundaries and scoring regressions. It needs neither model downloads nor the private archive. It should end with `Publication verification passed.` This does not rerun historical inference.

## Reproduce a real detector

Prerequisites: Git and Gitleaks **8.30.1** on PATH. Obtain that exact binary from the [upstream release](https://github.com/gitleaks/gitleaks/releases/tag/v8.30.1); verify it with `gitleaks version`. The Python environment has no inference dependencies for this route.

```sh
uv run python scripts/reproduce_cpu.py
```

This acquires the frozen Leak Museum revision in `.local/reproduction/leak-museum-gitleaks/`, rebuilds and fingerprints the corpus, runs Gitleaks, and compares the exact score with the frozen expectation. The final JSON contains the corpus SHA-256, missed/gold/fully-hidden counts and character TP/FP/FN. Any mismatch stops the command. Secret-scanner findings are test data; no credential is authenticated against a service.

If the binary is elsewhere, set `GITLEAKS_BIN` to its executable path. If the source cannot be downloaded, the command stops at acquisition; a public network connection is required. A successful run establishes one source-to-score example, not reproduction of the complete detector matrix.

## Try the scoring contract

This small, deliberately artificial example requires no model. It writes a dataset and a prediction into `.local/usage-example/`, then uses the same scorer as the benchmark. The prediction covers only one character of a two-word annotation. Word expansion hides the first word; the second remains exposed.

```sh
uv run python - <<'PY'
import csv
import hashlib
import json
from pathlib import Path

work = Path('.local/usage-example')
bench = work / 'BENCH/example'
result = work / 'RESULTS/example'
bench.mkdir(parents=True, exist_ok=True)
result.mkdir(parents=True, exist_ok=True)
text = 'Contact Sample Person today.'
start = text.index('Sample')
end = start + len('Sample Person')
with (bench / 'bench.csv').open('w', newline='') as stream:
    writer = csv.writer(stream)
    writer.writerow(['id', 'domain', 'text', 'entities'])
    writer.writerow(['one', 'demo', text, json.dumps([
        {'start': start, 'end': end, 'type': 'PERSON'}])])
(bench / 'meta.json').write_text(json.dumps({
    'lang': 'en', 'kind': 'pii', 'source': 'local synthetic example',
    'groups': {'PERSON': 'PERSON'}}))
meta = {'name': 'demo', 'bench': 'example', 'protocol': 1,
        'bench_sha256': hashlib.sha256((bench / 'bench.csv').read_bytes()).hexdigest()}
prediction = {'id': 'one', 'spans': [
    {'start': start, 'end': start + 1, 'label': 'person', 'score': 1.0}]}
(result / 'pred.demo.jsonl').write_text(
    json.dumps({'meta': meta}) + '\n' + json.dumps(prediction) + '\n')
PY
uv run python scripts/evaluate.py --data .local/usage-example --dataset example --model demo
```

Expected output:

```json
{
  "dataset": "example",
  "model": "demo",
  "missed": 0,
  "gold_spans": 1,
  "fully_hidden": 0,
  "char_tp": 6,
  "char_fp": 0,
  "char_fn": 7,
  "dropped_spans": 0,
  "train": false
}
```

Expected interpretation: one gold span, zero untouched spans, zero fully hidden spans. The normalized mask covers `Sample`, while `Person` and the space between them remain exposed. The example checks output-format integration; it is not a learned detector or an additional benchmark result.

To score a new detector, replace the prediction row with its actual offsets and labels, keeping one prediction record per input row, even for empty output. Add the real model revision, runtime versions and execution parameters to metadata as described in [Contributing](../CONTRIBUTING.md). Inference errors must be recorded and must fail scoring, rather than becoming empty successful predictions.

Do not paste production tickets or usable credentials into public issues. Local prediction and corpus files stay under `.local/`. The public snapshot is a frozen release; scoring a new local experiment does not automatically add it to published results.

## Read exact metrics programmatically

This prints eligible four-member composition results for logins and usernames, including each dataset's count:

```sh
uv run python - <<'PY'
import csv
from pathlib import Path

with Path('results/category-metrics.csv').open() as stream:
    for row in csv.DictReader(stream):
        if (row['system'] == 'composition:pplx+fastino+bardsai+mmbert'
                and row['category'] == 'logins' and row['train'] == 'False'):
            print(row['dataset'], row['hidden'], '/', row['gold'])
PY
```

[category-metrics.csv](../results/category-metrics.csv) groups the original labels for browsing. [entity-metrics.csv](../results/entity-metrics.csv) preserves each source label. [dataset-metrics.csv](../results/dataset-metrics.csv) contains character precision/recall/F1 and row-level masking outcomes. Every field is defined in the [metric contract](metrics.md).

## Regenerate or extend

To regenerate public artifacts, follow [reproduction](reproduce.md). To refresh the type-level diagnostics from the preserved local experiment, run `uv run python scripts/stratify.py` before rendering. This is a frozen-input path: it reads the frozen corpora and the saved predictions, and it refuses a prediction whose SHA-256 no longer matches the digest the snapshot records for that run, so diagnostics cannot be rebuilt on top of edited inputs. It runs no detector inference and changes nothing else in the release. A deliberate rebuild of the result bundle is `uv run python scripts/export.py --recompute-compositions`.

Fresh model inference requires the selected family's actual environment; consult the recorded runtime versions and detector catalog. The publication does not provide a guessed universal lockfile for historical model families. Start with the tested CPU route or a permitted custom dataset and a working detector environment, then contribute its exact metadata and measurements.
