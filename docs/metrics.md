# Metric and category contract

The result release uses scoring protocol **1**, snapshot schema **3**, threshold **0.5**, and the same frozen corpus hashes as the original comparison.

Run timing fields: new runs record `started_utc`/`finished_utc` (UTC, second resolution). Runs in the historical inventory that predate this convention keep only a legacy `started` field; it was written after the run completed in the recorder's local time, so it is retained as provenance but is not a reliable inference start time. No timestamps were backfilled.

## Units and boundaries

Offsets are zero-based Python character positions, with an inclusive start and exclusive end. They are not UTF-8 byte offsets or JavaScript UTF-16 code-unit offsets. Each prediction belongs to exactly one dataset row.

The normalized masking view trims whitespace, expands overlapping word boundaries using the scorer's word definition, and merges adjacent same-label spans. Both gold annotations and predictions are normalized. Predictions are retained at the published score threshold; scoreless spans are included. Two annotations with the same boundaries but different source labels remain separate units.

The raw-offset diagnostic applies retained detector intervals without boundary normalization. It is evaluated both against normalized gold and, separately, against original annotations. These are two different denominators. The CSV names keep the distinction explicit.

## Fields in the public CSVs

| Field | Meaning |
|---|---|
| `system` | `model:<configuration>` for a single detector; `composition:<name>` for a fixed union or vote |
| `dataset` | Frozen dataset identifier; input hash and source are in the catalog |
| `train` | Known training-source overlap; excluded from pooled comparisons when true |
| `label` | Original source annotation label, unchanged |
| `group` | Original protocol group, unchanged |
| `category` | Presentation category; does not affect matching |
| `gold` | Normalized annotation count |
| `original_gold` | Original annotation count before normalization |
| `characters` | Sum of normalized annotation lengths; overlaps count once per annotation |
| `hit` | Normalized annotations touched by at least one normalized predicted character |
| `hidden` | Normalized annotations completely covered by the normalized mask |
| `raw_hidden` | Normalized annotations completely covered by raw detector offsets |
| `original_hidden` | Original annotations completely covered by raw detector offsets |
| `covered_characters` | Covered normalized annotation characters, counted per annotation |

Use `hit / gold` for detected-span recall, `hidden / gold` for full hiding under the declared masker, and `(gold - hidden) / gold` for residual-span rate. Use `raw_hidden / gold` to compare raw and normalized masks on the same gold boundaries. Use `original_hidden / original_gold` for raw detection output evaluated against original annotations. An absent category is unmeasured, not perfect; a zero denominator has no percentage.

The category and original-label CSVs have no invented per-category precision or F1. The primary mask is label-blind: there is no unique way to assign an unmatched predicted character to a gold category. Correct entity typing requires a separate, explicitly mapped evaluation.

| Dataset field | Meaning |
|---|---|
| `char_tp`, `char_fp`, `char_fn` | Unique normalized character positions per row: gold and predicted, predicted only, gold only |
| `char_precision`, `char_recall`, `char_f1` | Micro scores derived from those exact character counts; values in [0, 1] |
| `positive_rows` | Rows with at least one original annotation |
| `residual_rows` | Rows with any normalized gold character uncovered by the normalized mask |
| `raw_residual_rows` | Rows with any normalized gold character uncovered by raw offsets |
| `raw_original_residual_rows` | Rows with any original annotated character uncovered by raw offsets |
| `negative_rows` | Rows with no original annotations |
| `negative_rows_touched` | Such rows with at least one character masked after normalization |
| `negative_characters` | All characters in rows without annotations |
| `negative_characters_masked` | Masked characters in those rows |

Character precision is `TP / (TP + FP)`, recall is `TP / (TP + FN)`, and F1 is their harmonic mean. The inherited scorer returns zero when a metric denominator is zero; retain the underlying counts when interpreting that convention. An annotation-free row is not guaranteed to be truly free of sensitive information.

## Presentation categories

The full dataset-specific map is stored in `snapshot.json` under `breakdowns.taxonomy`. Every retained source label has exactly one presentation category. Group assignments used by protocol 1 are preserved beside the new category; the presentation does not retroactively change source definitions.

| Family | Category | Assignment |
|---|---|---|
| Credentials | Passwords, keys & tokens | Source SECRET group, including source-labeled credential-like identifiers |
| Credentials | Logins & usernames | Explicit USERNAME, username, user_name and login labels |
| Personal & contextual data | Bank accounts & cards | Explicit card/account/routing/IBAN/BIC/CVC/CVV labels from the existing ID group |
| Personal & contextual data | Documents & identifiers | Remaining ID labels, including documents, government, vehicle and device identifiers |
| Personal & contextual data | People's names | PERSON group, including source-labeled name parts and nicknames |
| Personal & contextual data | Phone numbers & email | CONTACT group, including ambiguous source contact handles |
| Personal & contextual data | Addresses & locations | ADDRESS group, including places, facilities and coordinates |
| Personal & contextual data | Dates & times | DATE group plus retained generic DATE, TIME and date labels |
| Personal & contextual data | Organizations | ORG group |
| Personal & contextual data | Network identifiers | NET group |
| Personal & contextual data | Customer & employee IDs | ACCOUNT labels other than the explicit login labels |
| Personal & contextual data | Other sensitive attributes | Remaining OTHER labels, including retained health and demographic attributes |

This is a browsing taxonomy, not a legal assessment. It neither makes every organization name private nor declares every username a credential. Some source SECRET annotations describe salts, UUIDs, app IDs or resource identifiers. They remain evaluated according to the frozen annotation policy. We do not infer credential validity or silently relabel ambiguous source values from their text.

Sources do not share an exhaustive definition of personal data. Some original source labels were dropped during corpus conversion; the new view cannot recover unmeasured annotations. [Conversion details](sources.md) and [upstream comparison](comparison.md) are necessary context for the category percentages.

## Aggregation and display

Pooled category percentages sum counts over eligible datasets. Dataset-macro results average dataset percentages with equal weight. No training-source row enters a pooled result. A composition is evaluated only where every required member is present; a vote requires its entire declared membership.

The homepage fixes one composition, shows all its categories, and links every dataset. Its high/low examples require at least 100 spans per category/dataset cell, then take three highest and three lowest full-hiding rates; ties use descending sample size and ascending dataset/category identifiers. This cutoff is only a display policy. All smaller cells are available, and no new population confidence bounds are claimed.

An incomplete fraction that would round to 100.00% is shown as `>99.99%`, not 100%. Percentages below 0.01% with a nonzero numerator are shown as `<0.01%`. Exact counts remain authoritative.

The source-mix sensitivity cut excludes the same project-generated synthetic and corrupted datasets for all compositions. The dataset influence table subtracts each source separately to illustrate weighting; it does not replace the all-dataset result. Related source slices, repeated templates and upstream synthetic data limit independence.

## Precision of claims

Historical individual-model tables preserve reported rounding and bootstrap intervals. Newly added diagnostics are recomputed from saved predictions and checked against exact missed counts, exact selected-composition counts and the precision of the old rounded metrics. This verifies consistency with saved output, not the correctness of the original model inference or annotations.

The legacy normalized exact/overlap diagnostics are not conventional typed, one-to-one NER micro-F1. One prediction can cover several gold annotations. Use their declared coverage semantics and do not compare them to an upstream typed NER leaderboard as if they were the same metric.

No category plot supplies a new confidence interval. Existing row bootstrap intervals are conditional on a dataset and metric; the ensemble report's paired intervals concern character F1. They do not certify pooled full-hiding differences, all languages, or production leak rates.
