# Bugs and errors

## 2026-09-22 - Onboarding rejected frozen corpora that contain CR

- File: `scripts/onboarding.py`, character total around line 148
- Problem: `check_dataset` counted `len(text)` from a `newline=""` read. Four hash-correct datasets (`kiji-en`, `corrupt-hivetrace`, `secrets-issues`, `corrupt-secrets-issues`) failed the catalog character check, so `prepare --datasets all` copied nothing.
- Fix: character totals subtract one per CRLF, matching `scripts/export.py`, which counted after universal-newline translation. Annotation offsets still use the untranslated CSV text. Published catalog numbers are unchanged.
- Status: fixed

## 2026-09-21 - Scanner status missing from the site

- File: `site/scripts/sync-benchmark.mjs`, record build around line 105
- Problem: interactive profiles and comparison showed scanner scores without `adapter_status`, `adapter_policy` or unresolved counts from `results/run-inventory.json`.
- Fix: each scanner result is joined to its run. A slice sums only the runs inside it; the full inventory stays separate. Mixed-policy comparisons leave historical pre-fix scanners out until the reader includes them.
- Status: fixed

## 2026-09-21 - Filtered CSV repeated the `family` header

- File: `site/lib/benchmark.ts`, `filteredCsv` around line 370
- Problem: the export scope and the detector family both used the header `family`, so a dict reader kept only the detector value.
- Fix: the columns are `filter_family` and `system_family`.
- Status: fixed

## 2026-09-21 - `task=all` dropped on thematic pages

- File: `site/lib/explorer-url.ts`, `writeExplorerSearch` around line 94
- Problem: serialization treated `all` as the default and removed it. PII and secrets pages then restored their own default.
- Fix: the task parameter is always written.
- Status: fixed

## 2026-09-21 - Comparison CSV stored unused leaderboard filters

- File: `site/lib/benchmark.ts`, `compareExportContext` around line 378
- Problem: a comparison download copied leaderboard search, family, coverage and sort even though those controls do not select or order the comparison rows.
- Fix: the comparison file records `view=compare`, `rowOrder=selection`, the selected detectors and the shared dataset ids. Search and sort stay out.
- Status: fixed

## 2026-09-21 - Composition card showed only the first member revision

- File: `site/scripts/sync-benchmark.mjs`, system build around line 56
- Problem: upstream, revision and flags for a composition came from its first member, and the result card presented that pin as the ensemble version.
- Fix: a composition stores `participants` for every member and leaves the single revision empty. The card lists each member pin and the publication result revision.
- Status: fixed

## 2026-09-21 - Strict rescoring accepted a prediction without a fingerprint

- File: `scripts/evaluate.py`, around line 29
- Problem: `evaluate.py` printed ordinary scores when `protocol` or `bench_sha256` was missing, so a same-length text change could pass unmarked.
- Fix: the strict command refuses that input. `--legacy` still scores it and marks `legacy` plus the limitation. A wrong fingerprint still fails. Published historical runs are not rescored by this change.
- Status: fixed

## 2026-09-21 - Extra masking example used a labeled row

- File: `site/components/benchmark-explorer.tsx`, methodology example around line 2100
- Problem: the Extra masking sample highlighted `Account:` on a row that contains an email. The metric denominator is characters in rows that have no labels.
- Fix: the sample is a separate unlabeled row, `Hello there`, shown as 5 / 11, and the email row is called out as excluded.
- Status: fixed

## 2026-09-21 - CPU table said different workloads were comparable

- File: `README.md`, CPU cost section around line 116
- Problem: the CPU introduction said one machine group made the rows comparable, while the same table shows different dataset counts.
- Fix: the README, the CPU figure note and `results/detectors.md` call the numbers saved throughput on one reference machine group, not a same-input comparison or request latency.
- Status: fixed
