# Changelog

## Unreleased

Presentation only. No prediction, score, dataset hash, protocol or frozen date
changed: every number below is read from the same snapshot.

- The README now answers the two questions it never answered. A generated table
  and figure cover the 31 configurations with complete 41-dataset coverage
  (untouched annotations, full hiding, masking outside annotations, character
  F1), and two more cover measured cost: 45 CPU rows and 28 GPU rows, each from
  a single comparable machine group, in seconds per 10,000 characters.
- New `results/detectors.md` pools all 103 measured configurations, including
  partial coverage, Russian-label variants, chunking and quantization runs, each
  with its eligible dataset count and its measured cost.
- Four new figures: `detectors`, `cpu-speed`, `gpu-speed` and `speed-quality`.
  The eleven existing figures were redrawn in the same skin; assets now number
  15.
- Figures are written directly as SVG by `scripts/figures.py` instead of being
  plotted through matplotlib. Each one carries a light and a dark palette chosen
  by the reader's `prefers-color-scheme`, and the published bytes no longer
  depend on a plotting library's platform behavior. The `plots` dependency group
  is gone, so the publication rebuild needs no third-party package.
- `scripts/verify.py` checks the three new README blocks against the snapshot
  rows they are generated from, and the required asset count moved from 11 to 15.

## 1.0.3 - 2026-09-19

The CPU side of the frozen experiment is measured out. The experiment itself is
unchanged (2026-09-09): every new prediction ran the same protocol against the
same pinned model revisions and the same frozen dataset hashes, so this release
moves `result_revision` to 2026-09-19 and leaves `experiment_date` where it was.

- CPU coverage closed: dynamic int8 is 147/147 triples, up from 117/147, and the
  ONNX CPU queue is 61/61, up from 28/61. The CPU dispatcher stands at 501/506.
  The snapshot gains 91 quality rows and loses none: 2,137 to 2,228 measurements,
  2,500 to 2,591 run records, 2,423 to 2,514 breakdown results.
- `results/report.md`, section "int8 dynamic quantization against fp32": 14 model
  pairs became 18, each over its full set list. Pooled, 41.0% of gold spans are
  missed in fp32 against 69.4% in int8 over 1,199,483 spans. The three Russian
  GLiNER variants that had no int8 pair - `gliner-nvidia-ru`, `gliner-urchade-ru`
  and `gliner-multi-v21-ru` - read 100.0% missed under `quantize_dynamic` on every
  set they cover, the same collapse their non-Russian siblings already showed.
- Catalog holes closed: `nym-small` moved from 11 measured datasets to 41,
  `pii-shield-onnx` from 24 to 41, `ner-ru-gherman-onnx` from 4 to 9 and
  `openai-base-onnx` from 0 to 9. Speed rows went from 233 to 254 over 862
  pooled CPU sets.
- `docs/limitations.md` no longer states that the CPU queue was intentionally
  stopped. It now names what is left: two `gliner2-hivetrace-uni` speed triples,
  which only pool into the published row on the same AMD EPYC 9K84 machine group,
  and three legacy `pii-shield-onnx` records that are complete and error-free but
  carry no per-run dataset hash.
- `docs/methodology.md` no longer states that int8 has intentionally omitted runs,
  and `benchmark/models.toml` no longer describes `openai-base-onnx` as a CPU
  speed reference only, because it now carries quality rows.
- `scripts/verify.py` prints the snapshot totals it read instead of a hard-coded
  summary line, so a coverage change cannot leave a stale count in the output.

### Regenerated public artifacts

- `results/*` and `results/datasets/*`, `results/types/*`, the exact CSVs,
  `README.md` and the catalogs under `datasets/` were rebuilt from the stored
  predictions. The figures under `assets/` are byte-identical to 1.0.2: the new
  records are CPU variants, which no headline figure draws.

## 1.0.2 - 2026-09-18

Pre-release hardening from the 2026-09-17 third review. The frozen experiment
is untouched (2026-09-09), the code version and the result revision are now
separate fields of `results/snapshot.json` (`experiment_date`, `code_version`,
`result_revision`), and `CITATION.cff` no longer claims a version it does not
publish.

- Scanner span mapping (`capture-v2`, T01): the adapter accepts a
  capture-group Secret only when exactly one copy of it lies inside the
  confirmed Match range, or when the value occurs once in the reported line.
  With none or several copies the reported range is kept and the span records
  why (`unresolved_reason`: `capture-collision`, `decoded`, `native`), instead
  of landing on the first substring hit. Decoded findings keep the reported
  encoded-segment range and can no longer be moved onto a copy of the value in
  unrelated open text. Gitleaks was re-run at 8.30.1 on all ten of its
  datasets: 21 spans on 5 rows of `secrets-issues` moved, the other nine
  datasets are bit-identical, and 32 findings that used to be placed on
  another occurrence are now unresolved (`decoded`). Together with the 6
  already-unresolved findings of `secrets-rules`, 38 of 1,211 findings are
  unresolved, and every one of the 1,173 resolved findings carries exactly its
  reported Secret at the mapped span.
- Secrets numbers were regenerated from those predictions; the deltas are
  listed under "Regenerated public artifacts" below.
- Release gate (T02): a scan now requires a report of the expected schema -
  a missing, unparsable or field-less report stops the build instead of
  passing as a clean tree; history findings must name their commit; the pinned
  version is checked in both entry points; the snapshot digest exception names
  a published dataset run recorded in the run inventory or a reviewed
  aggregate report, so a well-formed digest line for an unknown path is not an
  exception; `--ignore-gitleaks-allow` and an empty ignore path are covered by
  a check that runs the real binary on a synthetic finding carrying an inline
  allow comment.
- Provenance (T03): `scripts/stratify.py` requires the SHA-256 of every
  prediction to equal the digest recorded in the snapshot `sources` map before
  it scores anything, and writes nothing when it refuses; `scripts/export.py`
  enforces the same frozen-input contract on every field a published number
  came from (`check_reuse`), and a deliberate rebuild remains
  `--recompute-compositions`. Both entry points are covered by
  `tests/test_stratify_frozen.py`.
- Swap rollback (T04): the renderer output that exists only in the live tree is
  copied into staging before any rename, so a failure there leaves the
  publication exactly as it was. Covered by `tests/test_export_swap.py`.
- Run status (T05): the run inventory carries `adapter_status`,
  `adapter_policy`, `unresolved_spans` and `unresolved_reasons` per run, and a
  `corrected-rerun` record without its own recorded policy fails verification.
  `historical pre-fix` labels in the secrets view name the members that
  actually ran, so a partial composition is no longer labeled after a scanner
  that took no part in it. The secrets report states how many findings are
  unresolved and that they are scored at the reported range.
- External corpora (T06): raw annotations are validated before normalization -
  offsets must be integers, non-empty and inside the text, types must be
  non-empty strings - so a mistyped annotation stops the run instead of
  leaving the denominator. Covered by `tests/test_scoring_contract.py`.
- Presentation labels (T07): `benchmark/score.py` and `benchmark/ens.py` no
  longer title a table `FP rows`/`False positives on rows with nothing to
  hide`; the columns read `rows touched` and `chars masked`, while the exact
  CSVs keep `fp_rows`/`fp_chars` as documented technical names.
  `scripts/verify.py` fails if a retired wording reappears in a published
  report.
- Tests: the documented usage example is now extracted from `docs/usage.md`
  and executed as published, and new modules cover the scanner mapping, the
  scan gate and the scoring contract; all of them run in `scripts/verify.py`.
- Figure determinism: the three heatmaps are drawn as vector cells
  (`pcolormesh`) instead of `imshow`, which embedded a resampled PNG whose
  bytes differ between macOS and Linux. Re-rendering `assets/coverage.svg`,
  `assets/dataset-heatmap.svg` and `assets/language-cuts.svg` is now
  byte-identical on both, so the `git diff --exit-code` release gate no longer
  depends on the platform the renderer ran on.
- `tests/test_stratify_frozen.py` was tracked but executed by nothing; it now
  runs in `scripts/verify.py` with the other checks.
- Version metadata is synchronized at 1.0.2.

### Regenerated public artifacts

- `results/secrets.md`, `results/report.md`, `results/ensemble.md`,
  `results/speed.md`, `results/datasets/*.md` and the exact CSVs were rebuilt
  from the stored predictions, so the renamed labels and the corrected
  gitleaks positions are what the publication states.
- Every number change is scoped to the corrected gitleaks rerun:
  `measurements.csv` moved 1 of 2,137 rows (`secrets-issues/gitleaks`,
  missed 132 → 130, hidden 44.8% → 45.5%, char P 0.445 → 0.428,
  R 0.722 → 0.727); `ensembles.csv` moved 4 of 615 rows (the gitleaks
  compositions on `secrets-issues`, each −2 missed); `speed.csv` moved 1 of
  233 rows (gitleaks CPU re-measured by the rerun, 1.72M → 1.79M chars/s);
  `composition-counts.json` moved 0 of 286 rows - the recomputed compositions
  matched the frozen reports exactly. The full delta table is in the
  pre-release verification log.

## 1.0.1 - 2026-09-17

Pre-release hardening from the 2026-09-16 publication audit and its re-review. This entry
corrects the scanner-coordinate defect found in the first hardening pass and re-exports the
public artifacts from the corrected predictions. The frozen experiment date (2026-09-09) and
all untouched model predictions are unchanged.

- Gitleaks coordinate fix completed (re-review R01): the adapter now converts Gitleaks 8.30.1
  UTF-8 byte Match columns to character offsets and locates the capture-group Secret inside the
  confirmed Match range. Values that exist only in Gitleaks-decoded content keep the reported
  native range and are counted as `unresolved_spans` in run metadata. Regression fixtures cover
  duplicated values after multi-byte text, second-occurrence selection, Match-prefix Secrets,
  multi-line findings and missing columns.
- Gitleaks predictions were re-run at 8.30.1 on all ten of its datasets with the fixed adapter:
  47 spans on 23 rows changed position versus the stored pre-fix predictions (secrets-issues:
  9 rows / 19 spans; secrets-rules: 14 rows / 28 spans), and 35 decoded-content findings are
  marked unresolved. Public scanner tables and every composition containing gitleaks were
  regenerated from these predictions; the gitleaks-only secrets-issues row changed from
  133 to 132 missed, secrets-rules from 29 to 18.
- detect-secrets was re-run at 1.5.0 and matched every stored span; its results are verified
  unchanged. betterleaks, trufflehog, noseyparker, titus and kingfisher have no binary
  available; credsweeper and deepsecrets re-runs resolved newer unpinned versions
  (1.18.4 / 2.1.1) that differ from the recorded ones. These scanners keep their stored
  pre-fix predictions, are labeled `historical pre-fix` next to their tables, and are listed
  in the new scanner-status and rerun-support tables in docs/reproduce.md (R06/R09).
- The documented scoring-contract example works again and is now executed end to end
  (corpus creation, CLI evaluator, exact expected output) by tests/test_usage_example.py
  in every verification run (R02).
- Export no longer loses composition-counts.json on a reuse-only run, checks staged
  completeness before switching directories, and swaps the two public directories as one
  consistent operation with rollback; covered by tests/test_export_swap.py (R03).
- CI checks out the full history, refuses to scan a shallow clone, and applies the same
  reviewed, content-bound exception policy to history findings, validated against the blob
  content of the commit that produced each finding (R04).
- The secret-scan allowlist validates PROVENANCE digest lines structurally against real
  module hashes and snapshot source lines structurally against the run-file layout; a stray
  api_key field with a valid SHA-256 shape is rejected (R05).
- All 2,500 inventory records now carry prediction digests, and the reuse contract covers
  every prediction file (R07). The secrets report names missed spans as untouched annotations,
  unannotated rows explicitly, and no longer calls pooled [k/N] compositions a floor for the
  full composition (R08).
- Scoring accepts a limit larger than the dataset as the whole slice and rejects an empty or
  non-object metadata record. Version metadata is synchronized at 1.0.1. Legacy `started`
  semantics are documented in the metric contract.
- README adds an "Evaluate your own detector" route with the input contract and expected
  output.

First hardening pass (2026-09-16, from the original audit):

- Rescoring now binds a prediction to its expected dataset and model identity: a valid prediction
  of dataset A no longer passes for dataset B, and a valid corpus hash no longer skips the
  rows/characters cross-checks (audit F01/F03).
- Prediction files must carry exactly one leading metadata record; span shapes, ids, labels and
  scores are validated on read, and duplicate gold row ids are rejected (F04).
- Scanner findings map to the occurrence the scanner reported; ambiguous repeated values are
  marked unresolved instead of guessed (F02; first pass - superseded by the byte-column fix
  above). detect-secrets was verified unchanged; the other eight scanners keep their stored
  pre-fix predictions (see the scanner-status table in docs/reproduce.md).
- The secret scan is a mandatory CI release gate with content-bound Gitleaks exceptions, and the
  candidate Git history is scanned separately (F05/F06).
- Speed tables rename per-row timings to amortized ms/row with explicit timing boundaries; the
  int8/fp32 overlap marker reads `CIs overlap` and states that this is not an equivalence test
  (F07/F08).
- Export records per-prediction digests in the reuse contract and public inventory, exports
  scanner settings, and writes the public projection through a staging swap (F10/F11/F12).
- Run metadata records started_utc/finished_utc (F13). Verification checks local link anchors
  against GitHub heading slugs (F14).
- README restructured around navigation, masking outcomes and the tradeoff table; all four result
  blocks are generated from the snapshot and verified against it. Clean-rows labels replaced with
  rows-without-annotations wording.

## 1.0.0 - 2026-09-10

- Initial frozen detector comparison under scoring protocol 1.
- Dataset snapshot identities are recorded in `datasets/catalog.json`.
- Aggregate result release is recorded in `results/snapshot.json`.
- Added schema 3 diagnostics by original label, presentation category and dataset without changing protocol 1 or frozen inputs.
- Expanded English README, SVG comparisons, exact CSVs and per-dataset category pages.
- Added a primary-source comparison of benchmark methods and a runnable scoring-format example.
- Reject truncated Natasha adapter responses instead of silently padding them with empty successful predictions.

Protocol versions define scoring behavior, dataset snapshots define frozen inputs, and result releases package measurements. Published result bundles are immutable. Corrections receive a new changelog entry and release instead of rewriting historical artifacts.
