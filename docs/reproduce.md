# Reproduce this release

**Running models on your own hardware?** Start with [the CPU/GPU benchmark guide](run-benchmarks.md) for input preparation, validation, execution plans and resumable local runs. This page distinguishes those new measurements from exact reproduction of the historical release.

Python 3.12 and [uv](https://docs.astral.sh/uv/) are required. Reading the Markdown tables and SVG figures requires no installation.

## Validate the public release

```sh
uv sync --frozen
uv run python scripts/verify.py
```

This validates the numeric snapshot, denominators, composition coverage, local links, local anchors, English publication prose, required artifacts and the private-directory boundary. It also runs the inherited scoring self-checks and deterministic-rule self-checks. It needs neither the private archive nor a GPU.

CI additionally runs the secret-scan release gate: `scripts/scan_secrets.py` scans the public projection with Gitleaks 8.30.1 against reviewed, content-bound exceptions, and a second pass scans the full candidate Git history. A clean working tree does not prove a clean history; findings in either scan fail the build instead of being suppressed.

## Rebuild tables and figures

```sh
uv sync --frozen
uv run python scripts/render.py
uv run python scripts/verify.py
```

The renderer consumes only `results/snapshot.json`. Verification checks that its embedded composition rows equal the companion `results/composition-counts.json`. It never uses screenshots or manually estimated bar lengths as data. SVG is the publication format: `scripts/figures.py` writes the markup directly, with no plotting dependency, so the published bytes stay identical across platforms. Each figure carries one palette for light readers and one for dark, selected by the reader's `prefers-color-scheme` setting.

Schema 3 adds exact diagnostics for every historical quality configuration and the recomputed compositions. The renderer also builds category/dataset CSVs, per-dataset category pages and the marked README result blocks. [Field definitions](metrics.md) distinguish raw and normalized boundaries.

## Reproduce one public CPU result end to end

Install Git, uv and Gitleaks 8.30.1, then run:

```sh
uv run python scripts/reproduce_cpu.py
```

The command creates an ignored workspace under `.local/`, clones Leak Museum at revision `6b1483a00cfa7bb47551b7304c1e2d4bc9a3a919`, rebuilds its 97-row corpus from source-relative annotation offsets, checks the frozen corpus SHA-256, runs Gitleaks and applies the strict scorer. It accepts only the exact expected result: 101 gold spans, 15 fully hidden, 86 missed, 876 true-positive characters, no false-positive characters and 2,418 false-negative characters.

This is a tested public reproduction route for one open CPU subset and baseline. It is separate from the frozen 41-dataset comparison and does not claim a fresh rerun of its full result matrix.

## Re-export from the preserved experiment

The prepared local workspace includes the complete archive. In a public clone, the archive is not included. Obtain permitted source artifacts before using this command; the repository does not claim that restricted corpora ship with the code.

```sh
uv run python scripts/export.py --data .local/research --recompute-compositions
uv run python scripts/render.py
```

Export reads frozen reports for all model configurations, preserves their exact missed counts and confidence intervals, and reads prediction metadata into an allowlisted public inventory. Key compositions are independently recomputed from saved predictions using the inherited scorer; a mismatch against the frozen report stops export. No detector inference is performed by these commands.

With `--recompute-compositions`, export also rebuilds the category diagnostics and checks them against the frozen model and composition results. Without that flag it reuses the existing breakdown only if its threshold, input catalog, source-report hashes and original results still match. To recompute only the diagnostics that this snapshot adds, run:

```sh
uv run python scripts/stratify.py --data .local/research
uv run python scripts/render.py
uv run python scripts/verify.py
```

This operation reads every saved quality prediction, reports progress by dataset/configuration and writes the snapshot only after successful validation. It can take several minutes. The threshold is taken from the snapshot, not a caller's `THRESH` environment variable.

`stratify.py` is a frozen-input path, not a rebuild: before it scores anything it requires the SHA-256 of every prediction it reads to equal the digest the snapshot records for that run in `sources`, and it updates only the schema version and the diagnostics. A changed prediction stops the run with the file named, before the snapshot is written. A deliberate rebuild is `scripts/export.py --recompute-compositions`, which rewrites the measurements, the source digests, the run inventory and the result revision together.

The initial preservation was verified separately by an archive manifest. Export from reports is not advertised as a complete rerun of every model's quality computation.

## Rescore a selected saved prediction

```sh
uv run python scripts/evaluate.py --data .local/research --dataset hivetrace --model pplx
```

This checks the protocol, dataset hash, row completeness and errors, and recomputes metrics without overwriting a report. You can point `--data` at another workspace containing `BENCH/<dataset>/bench.csv`, its original `meta.json`, and `RESULTS/<dataset>/pred.<model>.jsonl`.

## Run a detector again

Inference adapters are in `benchmark/`. Model revisions are pinned in `benchmark/models.toml`; observed runtime versions are in `results/run-inventory.json`. Use an isolated environment matching the selected run's versions and device. Different model families used different environments; the small publication environment intentionally does not install every inference dependency.

```sh
BENCHMARK_DATA=.local/research DEVICE=cpu THREADS=16 \
OUT=.local/new-predictions uv run --no-project python benchmark/run.py pplx hivetrace 16
```

Run this command inside the matching inference environment. The local archive retains the original environment setup and collected freezes. Raw-data builders are also retained in `benchmark/`; they write into the selected local workspace. Do not rebuild the frozen corpora in place when experimenting with another dependency version.


## Scanner adapter status

The 2026-09-18 `capture-v2` correction of `benchmark/run_leaks.py` settles how
a Gitleaks 8.30.1 report becomes a character span. Gitleaks reports 1-based
UTF-8 byte columns for the full regex Match, counted from the preceding
newline, while `Secret` is a capture group of that Match. The adapter rebuilds
the Match range, converts the columns to characters, and accepts the capture
only when one copy of the Secret lies inside it or when the value occurs once
in the reported line. Everything else keeps the reported range and is stored
as `unresolved` with a reason:

- `decoded` - Match and Secret come from a decoding pass (`decoded:base64`,
  `decode-depth:N`), so the columns describe the encoded segment of the file
  and the plaintext position is unknown.
- `capture-collision` - the Secret occurs zero or several times inside the
  Match, so the capture it came from is not recoverable from the report.
- `native` - the report carries no usable columns.

Run metadata records the count as `unresolved_spans` and the split as
`unresolved_reasons`; the run inventory carries both next to
`adapter_status`/`adapter_policy`, so a machine-readable consumer never has to
read this page to know which mapping produced a run.

How uncertainty enters a number: an unresolved span is scored at its reported
range, exactly like any other span, and is neither discarded nor treated as a
false positive - a native range can be the honest answer for a decoded
finding. Scanner rows are therefore comparable only when they carry the same
`adapter_policy`; a corrected run must not be silently pooled with a
pre-correction one.

| Scanner | Stored predictions | Evidence |
|---|---|---|
| `gitleaks` | replaced by a corrected rerun (capture-v2, 8.30.1) | every one of the 1,173 findings the corrected adapter resolves carries exactly its reported Secret; the rerun moved 21 spans on 5 rows of `secrets-issues` and left the other nine datasets identical; 38 findings stay unresolved and all of them are `decoded` (32 in `secrets-issues`, 6 in `secrets-rules`) |
| `detect-secrets` | unchanged | rerun at 1.5.0 matched every stored span |
| `betterleaks`, `trufflehog`, `noseyparker`, `titus`, `kingfisher` | historical, pre-correction | binaries unavailable for a rerun |
| `credsweeper`, `credsweeper-noml`, `deepsecrets` | historical, pre-correction | rerun resolved newer unpinned versions (1.18.4, 2.1.1) that differ from the recorded ones |

Scanner-only rows and any composition containing a `historical` scanner are
labeled `historical pre-fix` in the [secrets view](../results/secrets.md). The
label names the members that actually produced the row, so a composition whose
missing member never ran is not labeled after a scanner that took no part in
it. Corrected and historical results must not be mixed into one comparison
without reading these labels.

## Rerun support by loader

`historical environment only` means the recorded revision is not forced by the
loader at rerun time; a rerun in a fresh environment is not guaranteed to load
the exact recorded artifact.

| Family / route | Rerun status | What is enforced |
|---|---|---|
| `gitleaks` (and the tested CPU route above) | reproducible end to end | pinned binary version 8.30.1, frozen corpus hash, exact expected score |
| `opf`, `hf`, `pplx`, `gliner`, `gliner2`, `onnx`, `spacy` | revision pinned in `models.toml` | `run.py` refuses to download without a 40-character pinned revision; the loaded weights still depend on the matching historical runtime versions in `run-inventory.json` |
| `natasha`, `stanza`, `rupii` | historical environment only | the loader requests current package resources; the recorded package version is not enforced against the artifact |
| `detect-secrets`, `credsweeper`, `deepsecrets` (fallback `uv --with`) | historical environment only | the fallback does not pin the package version; recorded versions are in `run-inventory.json` |
| `presidio`, rules layer | historical environment only | stored predictions only |

For a supported path, verify what actually loaded: the prediction metadata
records the resolved revision and runtime versions, and `scripts/evaluate.py`
refuses a prediction whose identity or corpus hash does not match the run.
