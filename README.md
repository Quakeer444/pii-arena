# PII & Secrets Detection Benchmark

**An independent, reproducible benchmark for choosing PII and secret detection tools.**

[![Live Leaderboard](https://img.shields.io/badge/Live-Leaderboard-2dd4bf?style=for-the-badge&logo=vercel&logoColor=06110f)](https://pii-secrets-benchmark.vercel.app/leaderboard)
[![Methodology](https://img.shields.io/badge/Read-Methodology-1f2937?style=for-the-badge)](docs/methodology.md)
[![Reproduce](https://img.shields.io/badge/Run-Reproduction-1f2937?style=for-the-badge)](docs/reproduce.md)
[![Datasets](https://img.shields.io/badge/Browse-Datasets-1f2937?style=for-the-badge)](docs/datasets.md)

[![MIT License](https://img.shields.io/badge/license-MIT-334155)](LICENSE)
![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-334155)
![Datasets 41](https://img.shields.io/badge/datasets-41-334155)
![Annotations 227K+](https://img.shields.io/badge/annotations-227K%2B-334155)
![Snapshot Sep 2026](https://img.shields.io/badge/snapshot-Sep%202026-334155)

![PII and secrets detector leaderboard with language and task filters](assets/leaderboard-preview.png)

Find the right detector for **PII**, **secrets**, **English**, **Russian** or **multilingual** text. The leaderboard ranks complete masking first, then exposes detection, extra masking and measured speed as separate decision dimensions.

| Snapshot | Value |
|---|---:|
| Datasets | **41** |
| Input rows | **41,643** |
| Normalized gold annotations | **227,466** |
| Saved prediction runs | **2,591** |
| Frozen experiment | **2026-09-09** |

<!-- BEGIN SNAPSHOT -->
The frozen experiment contains **41 datasets**, **41,643 rows**, **227,466 normalized gold spans** and **2,591 saved prediction runs**. The catalog has 62 execution records, including label variants, mirrors, scanners and rules.
<!-- END SNAPSHOT -->

**Scope:** This is a descriptive comparison under one declared masking protocol, not a production-safety certification.

## Top complete-coverage detectors

All rows below cover the same 41 retained datasets. **Fully Hidden** is the primary metric: every character of the normalized gold annotation must be covered after word-boundary expansion.

| Detector | Fully Hidden ↑ | Detected / Overlapped ↑ | Extra Masking ↓ |
|---|---:|---:|---:|
| `gliner2-fastino` | **79.86%** | 86.81% | 5.88% |
| `pplx` | **74.92%** | 79.05% | 11.42% |
| `nuner-zero` | **71.63%** | 78.78% | 3.94% |
| `bardsai-eu` | **66.62%** | 81.37% | 7.72% |
| `gliner2-large` | **65.65%** | 71.98% | 3.51% |

[Open the live leaderboard](https://pii-secrets-benchmark.vercel.app/leaderboard) to change the language/task slice, include partial coverage, sort every metric, open detector profiles and share the exact filtered URL.

## Compare trade-offs, not one marketing score

![Detector comparison with complete masking and trade-off views](assets/comparison-preview.png)

The comparison view uses the shared eligible dataset intersection for every selected detector. It exposes complete masking, any-overlap detection, extra masking, character F1, per-type outcomes and measured throughput without collapsing them into an arbitrary composite score.

## Find your result

| Your question | Start here |
|---|---|
| Which detector should I choose? | [Live leaderboard](https://pii-secrets-benchmark.vercel.app/leaderboard) · [Detector profiles](https://pii-secrets-benchmark.vercel.app/detectors) |
| How do individual detectors compare? | [Interactive compare](https://pii-secrets-benchmark.vercel.app/compare) · [Models by language and task](results/by-language.md) |
| What happens to names, passwords, IDs and other types? | [Data-type explorer](https://pii-secrets-benchmark.vercel.app/entities) · [Exact type outcomes](results/by-entity.md) |
| Where are the weak datasets? | [Dataset explorer](https://pii-secrets-benchmark.vercel.app/datasets) · [Dataset report](results/by-dataset.md) |
| What is the quality / masking / speed trade-off? | [Performance explorer](https://pii-secrets-benchmark.vercel.app/performance) · [Ensembles](results/ensemble.md) |
| Where are the machine-readable results? | [Summary CSV](results/summary.csv) · [Category CSV](results/category-metrics.csv) · [Metric definitions](docs/metrics.md) |
| How do I score my own detector? | [Evaluate your detector](#evaluate-your-own-detector) - one command, expected output included |

## Detection is not complete masking

Reference composition: **PPLX + Fastino GLiNER2 + mmBERT + BardsAI**.
This fixed union illustrates behavior across the same datasets. It is not an independently selected winner.

<!-- BEGIN HEADLINE OUTCOMES -->
| Outcome | Exact count | Rate |
|---|---:|---:|
| Normalized annotations fully hidden | 214,738 / 227,466 | 94.40% |
| Normalized annotations detected / overlapped | 224,212 / 227,466 | 98.57% |
| Characters masked in unannotated rows | 574,028 / 2,895,905 | 19.82% |
| Annotated rows with residual gold characters | 6,749 / 34,077 | 19.81% |
| Unannotated rows touched by a mask | 5,899 / 7,566 | 77.97% |
<!-- END HEADLINE OUTCOMES -->

Full hiding uses the published **word-boundary expansion**. Raw detector offsets give a different result; see [raw-offset diagnostics](results/overview.md#headline-masking-outcome).

**Detected / overlapped** only means at least one predicted character intersects the gold annotation. It does not mean the sensitive value was safely hidden.

**Rows without annotations are not guaranteed to contain no sensitive content.** Their masking rate is not a human-confirmed false-alarm rate. None of these percentages is a production leak probability.

## Compare complete configurations

The same dataset coverage and normalized annotation denominator are used in every row below. Higher is better for Fully Hidden and Detected; lower is better for Extra Masking. The columns express different objectives and are intentionally not collapsed into one score.

<!-- BEGIN COMPOSITION COMPARISON -->
| Fixed configuration | Fully hidden ↑ | Detected / overlapped ↑ | Extra masking ↓ |
|---|---:|---:|---:|
| PPLX | 74.92% | 79.05% | 11.42% |
| Fastino GLiNER2 | 79.86% | 86.81% | 5.88% |
| PPLX + Fastino | 91.94% | 96.54% | 15.27% |
| PPLX + Fastino + mmBERT | 92.96% | 97.91% | 18.84% |
| PPLX + Fastino + BardsAI | 94.08% | 98.13% | 17.10% |
| PPLX + Fastino + mmBERT + BardsAI | 94.40% | 98.57% | 19.82% |
<!-- END COMPOSITION COMPARISON -->

[Exact numerators, macro averages and language cuts](results/overview.md) · [Original comparison CSV](results/summary.csv)

![Comparison of residual normalized annotations and masking in rows without annotations; exact values are available in the linked results overview](assets/overview.svg)

The chart's "unannotated rows" label means **rows without gold annotations**, not independently verified clean content. More complete hiding can require substantially more masking. Compare both outcomes, not recall alone.

PPLX is `pplx`; Fastino is `gliner2-fastino`; mmBERT is `mmbert32k`; BardsAI is `bardsai-eu`. Repositories, revisions, variants and training-source evidence are in the [model catalog](docs/models.md).

## Explore failure patterns

The type and dataset views use the **same reference composition throughout**. They do not choose a different model for each favorable cell. Dataset pages also link to other measured configurations and their eligibility status.

<details>
<summary><strong>By data type: full hiding versus any overlap</strong></summary>

![Normalized full hiding and any-overlap detection by data category for the fixed reference composition](assets/entity-types.svg)

[Full type-level tables](results/by-entity.md) · [Category metrics CSV](results/category-metrics.csv) · [Original-label metrics CSV](results/entity-metrics.csv)

</details>

<details>
<summary><strong>All datasets: inspect weak results, not just pooled averages</strong></summary>

![Full-hiding heatmap across every retained dataset and data category for the same fixed reference composition](assets/dataset-heatmap.svg)

[Dataset outcomes](results/by-dataset.md) · [Dataset metrics CSV](results/dataset-metrics.csv) · [Source acquisition and conversion caveats](docs/sources.md)

</details>

<details>
<summary><strong>High and low observed coverage examples</strong></summary>

<!-- BEGIN DATASET EXAMPLES -->
| Diagnostic example | Dataset | Data type | Fully hidden / gold | Fully hidden |
|---|---|---|---:|---:|
| High observed coverage | [synth-ru-tickets](results/types/synth-ru-tickets.md) | Logins & usernames | 7,565 / 7,565 | 100.00% |
| High observed coverage | [synth-wiki-tables](results/types/synth-wiki-tables.md) | Phone numbers & email | 4,791 / 4,791 | 100.00% |
| High observed coverage | [synth-ru-tickets](results/types/synth-ru-tickets.md) | Phone numbers & email | 3,149 / 3,149 | 100.00% |
| Low observed coverage | [rubai-ru](results/types/rubai-ru.md) | Bank accounts & cards | 168 / 1,054 | 15.94% |
| Low observed coverage | [rubai-ru](results/types/rubai-ru.md) | Documents & identifiers | 53 / 268 | 19.78% |
| Low observed coverage | [rubai-ru](results/types/rubai-ru.md) | Addresses & locations | 469 / 1,501 | 31.25% |
<!-- END DATASET EXAMPLES -->

These are the three highest and three lowest category/dataset cells with at least 100 normalized annotations, using a fixed ordering and tie-breaking rule. This is a display rule, not a confidence bound. Smaller cells remain available in the complete tables. Zero observed failures is not zero population risk.

</details>

## Understand the scope before choosing a detector

**Language coverage:** Russian secrets have only one synthetic dataset. There is no multilingual-secrets cut. MULTI pools source languages, including some English, and is not a per-language guarantee.

**Training and selection:** known training-source overlaps are excluded where applicable; undisclosed overlap remains possible. Fixed compositions were inspected on this benchmark, not selected on an independent deployment holdout. Missing measurements are not zero misses.

**Dataset weighting:** project-generated synthetic sets and corrupted copies affect pooled results. [Sensitivity results](results/overview.md#weighting-sensitivity) keep the same compositions and show the effect of excluding those cuts. The remaining sources still include upstream synthetic material.

**Scanner scope:** scanner coverage is narrower than the full matrix, and some outputs have coarser boundaries. The adapters evaluate retained text inputs, not every feature of whole-repository scanning.

**Compute:** [speed measurements](results/speed.md) report their hardware and concurrency. The per-row `p50` / `p95` columns are amortized batch allocations, not individual request latency. Composition costs are derived from member throughput, not measured end-to-end latency. BardsAI is CPU-only in the tested ONNX configuration; its GPU-composition cost is a mixed-device estimate.

[Metric contract](docs/metrics.md) · [Methodology](docs/methodology.md) · [All limitations](docs/limitations.md) · [Comparison with other evaluation methods](docs/comparison.md)

## Quick start

### Regenerate and validate the publication

The commands below use a POSIX shell and the repository's uv environment. This checks the public artifacts; it does **not** rerun model inference.

```sh
uv sync --frozen --group plots
uv run python scripts/verify.py
uv run --group plots python scripts/render.py
uv run python scripts/verify.py
```

### Reproduce one public CPU result

Requires **Git**, **uv** and **Gitleaks 8.30.1** on PATH, plus access to the public source repository.

```sh
uv run python scripts/reproduce_cpu.py
```


### Evaluate your own detector

One corpus CSV, one metadata record, one prediction record per input row - then a single command prints exact missed, full-hiding and character counts:

```sh
uv run python scripts/evaluate.py --data <workspace> --dataset <name> --model <name>
```

The full runnable example - writing a tiny corpus and prediction, running the scorer, and the exact expected JSON output - is in the [usage guide](docs/usage.md#try-the-scoring-contract). Offsets are zero-based Python character positions with an inclusive start and exclusive end, as defined in the [metric contract](docs/metrics.md#units-and-boundaries). Rows with no findings still need an empty prediction record.

## Evidence and reusable data

| Resource | What it contains |
|---|---|
| [Overview](results/overview.md) | Exact masking counts, complete compositions and weighting sensitivity |
| [Full report](results/report.md) · [Ensembles](results/ensemble.md) | Detailed historical metrics, variants and available paired comparisons |
| [Secrets](results/secrets.md) · [Speed](results/speed.md) | Specialized detector behavior and measurement conditions |
| [Entity CSV](results/entity-metrics.csv) · [Category CSV](results/category-metrics.csv) · [Dataset CSV](results/dataset-metrics.csv) | Machine-readable breakdowns; read the metric contract before aggregating |
| [Dataset catalog](datasets/catalog.json) · [Run inventory](results/run-inventory.json) | Retained provenance, source/corpus identity and safe execution metadata |
| [Numeric snapshot](results/snapshot.json) | The larger machine-readable input used to regenerate publication views |

## Contributing, citation and licensing

Use [CONTRIBUTING.md](CONTRIBUTING.md) for contributions and [CITATION.cff](CITATION.cff) when citing this result version. Follow [SECURITY.md](SECURITY.md) for sensitive reports; never post real credentials or private corpus rows in issues.

The project's own code and original publication material use the [MIT license](LICENSE), with third-party notices in [NOTICE](NOTICE) and [LICENSES](LICENSES/README.md). Dataset and model terms are separate. Corpus text, raw predictions, credentials and downloaded weights are not part of the public publication tree.
