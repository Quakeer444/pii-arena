# Results at a glance

Frozen predictions: **2026-09-09**. The rows below cover the same **41 datasets and 227,466 normalized gold spans**. All are fixed unions, except the single-model rows. No disclosed training-source overlap was identified for these members; undisclosed overlap remains possible.

Model names: **PPLX** = `pplx`; **Fastino** = `gliner2-fastino`; **mmBERT** = `mmbert32k`; **BardsAI** = `bardsai-eu`. Exact repositories and revisions are in the [model catalog](../docs/models.md).

## Headline masking outcome

For **PPLX + Fastino + mmBERT + BardsAI**, detection and masking answer different questions:

| Diagnostic | Exact count | Rate |
|---|---:|---:|
| Normalized entities untouched | 3,254 / 227,466 | 1.43% |
| Normalized entities not fully hidden after boundary expansion | 12,728 / 227,466 | 5.60% |
| Normalized entities not fully hidden using raw offsets | 14,808 / 227,466 | 6.51% |
| Rows with annotations retaining exposed characters after expansion | 6,749 / 34,077 | 19.81% |
| Rows without annotations touched by a mask | 5,899 / 7,566 | 77.97% |
| Characters masked in rows without annotations | 574,028 / 2,895,905 | 19.82% |

Raw detector offsets fully cover 216,780 of 230,446 original annotations. This uses a different denominator from normalized masking. These are annotation-based measurements, not a production leak probability; rows without annotations are not guaranteed to be free of sensitive content.

## Complete-composition comparison

| Composition | Missed spans | Missed % | Residual after masking | Residual % | Macro missed % | Unannotated rows touched % | Unannotated characters masked % |
|---|---:|---:|---:|---:|---:|---:|---:|
| PPLX | 47,647 / 227,466 | 20.95% | 57,052 / 227,466 | 25.08% | 14.68% | 43.96% | 11.42% |
| Fastino GLiNER2 | 30,011 / 227,466 | 13.19% | 45,819 / 227,466 | 20.14% | 17.08% | 52.52% | 5.88% |
| PPLX + Fastino | 7,872 / 227,466 | 3.46% | 18,344 / 227,466 | 8.06% | 2.68% | 68.90% | 15.27% |
| PPLX + Fastino + mmBERT | 4,746 / 227,466 | 2.09% | 16,011 / 227,466 | 7.04% | 1.74% | 76.62% | 18.84% |
| PPLX + Fastino + BardsAI | 4,258 / 227,466 | 1.87% | 13,471 / 227,466 | 5.92% | 1.70% | 72.09% | 17.10% |
| PPLX + Fastino + mmBERT + BardsAI | 3,254 / 227,466 | 1.43% | 12,728 / 227,466 | 5.60% | 1.33% | 77.97% | 19.82% |

`Missed` means no predicted character touches the normalized gold span. `Residual` means at least one normalized gold character remains visible after word-boundary expansion. Macro gives each dataset equal weight. The unannotated columns use only rows with no gold spans; rows without annotations are not guaranteed to be free of sensitive content. Exact numerators are in [summary.csv](summary.csv).

## By language and task

| Composition | RU / PII | RU / secrets | EN / PII | EN / secrets | MULTI / PII |
|---|---:|---:|---:|---:|---:|
| PPLX | 25.82% | 0.00% | 16.57% | 3.47% | 12.74% |
| Fastino GLiNER2 | 12.91% | 35.11% | 7.43% | 23.12% | 16.70% |
| PPLX + Fastino | 3.56% | 0.00% | 1.57% | 1.04% | 4.61% |
| PPLX + Fastino + mmBERT | 1.97% | 0.00% | 1.03% | 0.39% | 3.19% |
| PPLX + Fastino + BardsAI | 1.48% | 0.00% | 1.12% | 0.37% | 3.47% |
| PPLX + Fastino + mmBERT + BardsAI | 1.11% | 0.00% | 0.83% | 0.11% | 2.73% |

**RU / secrets is one synthetic dataset.** There is no MULTI / secrets cut. MULTI is an aggregate of multilingual corpora, including some English; it does not certify every language. Counts and sources are in the [dataset catalog](../docs/datasets.md).

## Weighting sensitivity

The fixed compositions below are rescored without this project's six synthetic datasets and three corrupted copies. The remaining 32 datasets still include upstream synthetic material. No composition was re-selected for this cut.

| Composition | All 41 pooled | All 41 macro | Project synthetic | Corrupted copies | Remaining 32 pooled |
|---|---:|---:|---:|---:|---:|
| PPLX + Fastino | 7,872/227,466 (3.46%) | 2.68% | 121/49,452 (0.24%) | 268/7,486 (3.58%) | 7,483/170,528 (4.39%) |
| PPLX + Fastino + mmBERT | 4,746/227,466 (2.09%) | 1.74% | 47/49,452 (0.10%) | 128/7,486 (1.71%) | 4,571/170,528 (2.68%) |
| PPLX + Fastino + mmBERT + BardsAI | 3,254/227,466 (1.43%) | 1.33% | 38/49,452 (0.08%) | 97/7,486 (1.30%) | 3,119/170,528 (1.83%) |

The dev/test assignment remains frozen by source lineage and row identity. This sensitivity view changes only the reporting denominator; it does not create an independently held-out deployment result.

## Reference compute cost

| Composition | CPU seconds / 10k chars | GPU seconds / 10k chars | Qualification |
|---|---:|---:|---|
| PPLX | 9.1 | 2.2 | Derived from member throughput |
| Fastino GLiNER2 | 13.6 | 0.3 | Derived from member throughput |
| PPLX + Fastino | 22.7 | 2.5 | Derived from member throughput |
| PPLX + Fastino + mmBERT | 24.8 | 2.6 | Derived from member throughput |
| PPLX + Fastino + mmBERT + BardsAI | 32.8 | 10.7 | Different CPU conditions; GPU column includes CPU-only BardsAI |

CPU: AMD EPYC 9K84, W=24 processes, 16 threads each; calibrated through a same-condition PPLX reference at 1,100 chars/s. GPU: RTX 5090, W=2. BardsAI was measured with 8 CPU threads. Sequential composition cost is derived by summing inverse member throughput. These are throughput costs under load, **not isolated 16-thread service latency** or direct end-to-end composition measurements.

## Choosing a starting point

PPLX + Fastino is the smallest complete union highlighted here. Adding mmBERT lowers the observed missed count from 7,872 to 4,746 and supports CPU and GPU execution. Adding BardsAI as a fourth member leaves 3,254 untouched spans, with more masking and a CPU-only step. Choose against your own content and latency requirement; these are fixed candidates, not an optimized or independently held-out winner.

The tested two-of-three vote uses different members and has 40 eligible datasets, so it is excluded from these same-coverage charts. Its 59,252 misses out of 218,075 gold spans are available in the [ensemble report](ensemble.md). This does not establish that every voting scheme is inferior.

The pooled figures are descriptive. Use the per-dataset confidence intervals and paired comparisons before calling a difference reliable. Comparisons from reports do not supply a new pooled confidence interval.

## Explore the evidence

- [Every base model by language and task](by-language.md)
- [Full quality report, variants and quantization](report.md)
- [All fixed ensembles and paired comparisons](ensemble.md)
- [Secrets and masking tradeoffs](secrets.md)
- [Measured speed and hardware groups](speed.md)
- [Run metadata inventory](run-inventory.json)
- [Methods](../docs/methodology.md) and [limitations](../docs/limitations.md)
