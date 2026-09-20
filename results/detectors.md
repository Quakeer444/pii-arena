# Every detector configuration

Pooled outcomes for 103 measured configurations at threshold 0.5. Every number below comes from the saved predictions of the frozen experiment. Runs on a known training source are excluded from these pools, so the eligible dataset count is part of the result and configurations with different counts are not directly comparable.

`Untouched` means no predicted character reaches the normalized annotation. `Fully hidden` means every character of the annotation is masked after word-boundary expansion. `Masked outside annotations` is the share of characters masked in rows that carry no annotation; those rows are not verified clean content. Speed columns come from the two reference machine groups below and are blank when a configuration was never run there.

![Pooled outcomes for every complete-coverage detector](../assets/detectors.svg)

## Complete coverage: all 41 datasets

| Detector | Family | Eligible sets | Untouched / gold | Untouched | Fully hidden | Masked outside annotations | Char F1 | CPU s/10k | GPU s/10k |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| gliner2-fastino | gliner2 | 41/41 | 30,011 / 227,466 | 13.19% | 79.86% | 5.88% | 0.763 | 14.93 | 0.27 |
| bardsai-eu | onnx | 41/41 | 42,383 / 227,466 | 18.63% | 66.62% | 7.72% | 0.703 | - | - |
| pplx | pplx | 41/41 | 47,647 / 227,466 | 20.95% | 74.92% | 11.42% | 0.716 | 9.94 | 2.20 |
| nuner-zero | gliner | 41/41 | 48,263 / 227,466 | 21.22% | 71.63% | 3.94% | 0.760 | 20.12 | 0.38 |
| mmbert32k | hf | 41/41 | 48,833 / 227,466 | 21.47% | 50.17% | 10.33% | 0.613 | 2.32 | 0.18 |
| gliner-urchade | gliner | 41/41 | 62,517 / 227,466 | 27.48% | 65.51% | 3.79% | 0.687 | 9.68 | 0.20 |
| gliner2-large | gliner2 | 41/41 | 63,732 / 227,466 | 28.02% | 65.65% | 3.51% | 0.685 | 24.69 | 0.61 |
| apararti | opf | 41/41 | 67,711 / 227,466 | 29.77% | 62.49% | 11.16% | 0.658 | 4.09 | 1.69 |
| pii-shield-onnx | onnx | 41/41 | 69,057 / 227,466 | 30.36% | 56.43% | 38.92% | 0.416 | - | - |
| gliner25-fastino | gliner2 | 41/41 | 70,219 / 227,466 | 30.87% | 62.77% | 7.33% | 0.696 | 12.47 | 0.15 |
| gliner-pii-edge | gliner | 41/41 | 72,103 / 227,466 | 31.70% | 57.10% | 9.54% | 0.629 | 6.88 | 5.80 |
| ru-legal-ner | hf | 41/41 | 78,588 / 227,466 | 34.55% | 44.15% | 12.56% | 0.449 | 0.20 | 0.13 |
| openai-base | opf | 41/41 | 78,725 / 227,466 | 34.61% | 59.69% | 8.83% | 0.657 | 4.21 | 1.80 |
| opf-kz-ru | opf | 41/41 | 79,257 / 227,466 | 34.84% | 56.51% | 10.90% | 0.634 | 3.39 | 1.59 |
| gliner-stream-pii | gliner | 41/41 | 82,302 / 227,466 | 36.18% | 51.67% | 3.55% | 0.636 | 8.20 | 0.21 |
| gliner-multi-v21 | gliner | 41/41 | 90,767 / 227,466 | 39.90% | 51.28% | 2.71% | 0.537 | 9.89 | 0.19 |
| traciora | opf | 41/41 | 92,030 / 227,466 | 40.46% | 48.60% | 7.51% | 0.638 | 3.29 | 1.36 |
| ru-pii-ner | rupii | 41/41 | 97,121 / 227,466 | 42.70% | 53.11% | 2.73% | 0.599 | 1.42 | - |
| opf-ru-v2 | opf | 41/41 | 97,473 / 227,466 | 42.85% | 47.51% | 6.70% | 0.629 | 3.47 | - |
| davlan-xlmr | hf | 41/41 | 110,716 / 227,466 | 48.67% | 44.00% | 0.71% | 0.501 | 2.26 | 0.14 |
| stanza-ru | stanza | 41/41 | 111,122 / 227,466 | 48.85% | 43.41% | 16.11% | 0.326 | 8.35 | - |
| gliner-pii-base | gliner | 41/41 | 112,527 / 227,466 | 49.47% | 44.64% | 1.86% | 0.550 | 5.24 | 0.16 |
| gravitee-small | hf | 41/41 | 112,622 / 227,466 | 49.51% | 42.98% | 5.36% | 0.496 | 0.66 | - |
| ner-ru-yqelz | hf | 41/41 | 114,298 / 227,466 | 50.25% | 39.74% | 9.17% | 0.445 | 7.08 | 0.18 |
| gliner2-vladlinv | gliner2 | 41/41 | 114,622 / 227,466 | 50.39% | 46.09% | 0.91% | 0.572 | 14.49 | 0.17 |
| davlan-mbert | hf | 41/41 | 116,270 / 227,466 | 51.12% | 41.98% | 0.94% | 0.481 | 2.51 | 0.15 |
| ner-ru-gherman | hf | 41/41 | 116,497 / 227,466 | 51.22% | 27.63% | 0.28% | 0.453 | 2.48 | 0.15 |
| fef2-secret-ru | hf | 41/41 | 128,858 / 227,466 | 56.65% | 35.60% | 2.17% | 0.530 | 3.05 | 0.15 |
| spacy-ru-lg | spacy | 41/41 | 156,139 / 227,466 | 68.64% | 26.75% | 3.25% | 0.326 | 0.19 | - |
| natasha | natasha | 41/41 | 163,696 / 227,466 | 71.97% | 24.15% | 1.07% | 0.316 | 0.08 | - |
| rules-ru | rules | 41/41 | 169,760 / 227,466 | 74.63% | 24.48% | 6.96% | 0.506 | - | - |

## Partial coverage, label variants, chunking and quantization

A `-ru` suffix switches zero-shot labels to Russian with the same weights, so those runs apply only to Russian cuts. `+sent300`, `+ov100` and `+nochunk` are cutting variants, `+cpu-int8` and `+cpu-speed` are CPU execution variants. A smaller dataset count is a missing measurement, never a zero-miss result.

| Detector | Family | Eligible sets | Untouched / gold | Untouched | Fully hidden | Masked outside annotations | Char F1 | CPU s/10k | GPU s/10k |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| gliner-nvidia | gliner | 40/41 | 55,538 / 218,075 | 25.47% | 63.97% | 4.92% | 0.677 | 22.62 | 0.37 |
| openmed-nemotron | hf | 40/41 | 64,103 / 218,075 | 29.39% | 48.55% | 12.23% | 0.574 | 3.04 | 0.87 |
| opf-ru | opf | 40/41 | 74,621 / 222,661 | 33.51% | 49.51% | 9.41% | 0.595 | 3.52 | 1.12 |
| kalyan-ettin | hf | 40/41 | 74,974 / 218,075 | 34.38% | 43.35% | 7.57% | 0.579 | 1.14 | - |
| gliner2-hivetrace-omni | gliner2 | 39/41 | 41,214 / 213,591 | 19.30% | 74.82% | 3.12% | 0.760 | 14.79 | 0.29 |
| gliner2-hivetrace-uni | gliner2 | 39/41 | 95,890 / 213,591 | 44.89% | 49.89% | 1.27% | 0.571 | 2.92 | - |
| spacy-alrosait | spacy | 39/41 | 180,353 / 216,896 | 83.15% | 14.35% | 0.12% | 0.238 | 0.19 | - |
| nym-base | hf | 38/41 | 35,754 / 206,216 | 17.34% | 64.53% | 9.15% | 0.672 | 3.21 | 0.14 |
| nym-small | onnx | 38/41 | 39,158 / 206,216 | 18.99% | 62.82% | 9.82% | 0.673 | - | - |
| openmed-multilingual | hf | 38/41 | 58,119 / 211,692 | 27.45% | 51.75% | 11.92% | 0.626 | 3.25 | 0.84 |
| gliner2-fastino-ru | gliner2 | 19/41 | 18,300 / 136,419 | 13.41% | 77.70% | 2.16% | 0.816 | 8.90 | - |
| gliner2-hivetrace-omni-ru | gliner2 | 19/41 | 29,721 / 136,419 | 21.79% | 71.70% | 3.07% | 0.808 | 8.60 | - |
| gliner25-fastino-ru | gliner2 | 19/41 | 36,443 / 136,419 | 26.71% | 64.57% | 3.37% | 0.792 | 7.69 | - |
| gliner-nvidia-ru | gliner | 19/41 | 53,269 / 136,419 | 39.05% | 50.97% | 1.80% | 0.641 | 20.00 | - |
| gliner-urchade-ru | gliner | 19/41 | 62,081 / 136,419 | 45.51% | 45.35% | 1.30% | 0.637 | 6.22 | - |
| gliner-multi-v21-ru | gliner | 19/41 | 64,690 / 136,419 | 47.42% | 43.02% | 1.60% | 0.553 | 6.71 | - |
| gliner2-vladlinv-ru | gliner2 | 19/41 | 72,584 / 136,419 | 53.21% | 42.50% | 1.61% | 0.586 | 17.57 | - |
| gliner2-hivetrace-uni-ru | gliner2 | 19/41 | 103,744 / 136,419 | 76.05% | 21.59% | 1.16% | 0.281 | 2.04 | - |
| nym-base+sent300 | hf | 11/41 | 14,114 / 92,332 | 15.29% | 67.31% | 8.02% | 0.670 | - | - |
| gliner25-fastino+ov100 | gliner2 | 11/41 | 20,874 / 92,332 | 22.61% | 70.46% | 6.12% | 0.747 | - | - |
| nym-base+ov100 | hf | 11/41 | 21,493 / 92,332 | 23.28% | 63.27% | 6.73% | 0.620 | - | - |
| gliner25-fastino+sent300 | gliner2 | 11/41 | 21,554 / 92,332 | 23.34% | 71.99% | 7.56% | 0.725 | - | - |
| pplx+sent300 | pplx | 11/41 | 28,830 / 92,332 | 31.22% | 65.39% | 8.97% | 0.687 | - | - |
| ru-legal-ner+sent300 | hf | 11/41 | 30,513 / 92,332 | 33.05% | 43.64% | 10.02% | 0.512 | - | - |
| pplx+ov100 | pplx | 11/41 | 33,130 / 92,332 | 35.88% | 61.81% | 8.18% | 0.675 | - | - |
| ru-legal-ner+ov100 | hf | 11/41 | 36,198 / 92,332 | 39.20% | 38.48% | 9.95% | 0.479 | - | - |
| mmbert32k+nochunk | hf | 11/41 | 44,764 / 92,332 | 48.48% | 21.11% | 6.78% | 0.412 | - | - |
| gliner25-fastino+nochunk | gliner2 | 11/41 | 46,503 / 92,332 | 50.36% | 46.89% | 3.93% | 0.562 | - | - |
| opf-ru-v2+sent300 | opf | 11/41 | 47,334 / 92,332 | 51.27% | 41.91% | 3.21% | 0.573 | - | - |
| opf-ru-v2+ov100 | opf | 11/41 | 50,073 / 92,332 | 54.23% | 37.94% | 3.09% | 0.551 | - | - |
| gliner-nvidia+sent300 | gliner | 10/41 | 13,215 / 82,941 | 15.93% | 75.06% | 4.73% | 0.756 | - | - |
| gliner-nvidia+ov100 | gliner | 10/41 | 28,600 / 82,941 | 34.48% | 56.87% | 3.75% | 0.630 | - | - |
| pplx+cpu-int8 | pplx | 9/41 | 2,639 / 72,095 | 3.66% | 93.12% | 13.53% | 0.698 | - | - |
| openai-base-onnx | onnx | 9/41 | 16,829 / 72,095 | 23.34% | 70.86% | 3.20% | 0.713 | - | - |
| ru-legal-ner+cpu-int8 | hf | 9/41 | 25,254 / 72,095 | 35.03% | 36.07% | 8.12% | 0.453 | - | - |
| mmbert32k+cpu-int8 | hf | 9/41 | 26,169 / 72,095 | 36.30% | 21.91% | 6.87% | 0.416 | - | - |
| gravitee-small+cpu-int8 | hf | 9/41 | 34,949 / 72,095 | 48.48% | 43.54% | 3.65% | 0.506 | - | - |
| ner-ru-gherman-onnx | onnx | 9/41 | 45,789 / 72,095 | 63.51% | 19.10% | 0.12% | 0.355 | - | - |
| fef2-secret-ru+cpu-int8 | hf | 9/41 | 47,144 / 72,095 | 65.39% | 27.12% | 0.50% | 0.443 | - | - |
| ner-ru-gherman+cpu-int8 | hf | 9/41 | 48,624 / 72,095 | 67.44% | 17.49% | 0.11% | 0.322 | - | - |
| davlan-mbert+cpu-int8 | hf | 9/41 | 50,159 / 72,095 | 69.57% | 24.56% | 0.76% | 0.350 | - | - |
| davlan-xlmr+cpu-int8 | hf | 9/41 | 53,745 / 72,095 | 74.55% | 18.67% | 0.26% | 0.287 | - | - |
| gliner-pii-edge+cpu-int8 | gliner | 9/41 | 63,718 / 72,095 | 88.38% | 9.58% | 0.49% | 0.149 | - | - |
| gliner-pii-base+cpu-int8 | gliner | 9/41 | 71,651 / 72,095 | 99.38% | 0.61% | 0.00% | 0.011 | - | - |
| gitleaks | leaks | 9/41 | 33,436 / 33,633 | 99.41% | 0.51% | 0.45% | 0.132 | - | - |
| gliner-multi-v21+cpu-int8 | gliner | 9/41 | 72,095 / 72,095 | 100.00% | 0.00% | 0.00% | 0.000 | - | - |
| gliner-urchade+cpu-int8 | gliner | 9/41 | 72,095 / 72,095 | 100.00% | 0.00% | 0.00% | 0.000 | - | - |
| nym-base+cpu-int8 | hf | 8/41 | 15,707 / 62,598 | 25.09% | 59.79% | 5.04% | 0.607 | - | - |
| kalyan-ettin+cpu-int8 | hf | 8/41 | 39,806 / 62,704 | 63.48% | 20.89% | 2.63% | 0.344 | - | - |
| betterleaks | leaks | 8/41 | 33,356 / 33,538 | 99.46% | 0.44% | 0.56% | 0.117 | - | - |
| gliner-nvidia+cpu-int8 | gliner | 8/41 | 62,704 / 62,704 | 100.00% | 0.00% | 0.00% | 0.000 | - | - |
| gliner25-fastino-ru+nochunk | gliner2 | 5/41 | 38,785 / 74,859 | 51.81% | 45.53% | 1.59% | 0.577 | - | - |
| credsweeper-noml | leaks | 4/41 | 1,876 / 2,796 | 67.10% | 30.36% | 2.92% | 0.541 | - | - |
| detect-secrets | leaks | 4/41 | 2,321 / 2,796 | 83.01% | 16.74% | 4.03% | 0.366 | - | - |
| deepsecrets | leaks | 4/41 | 2,324 / 2,796 | 83.12% | 15.49% | 1.15% | 0.325 | - | - |
| gliner-multi-v21-ru+cpu-int8 | gliner | 4/41 | 48,779 / 48,779 | 100.00% | 0.00% | 0.00% | 0.000 | - | - |
| gliner-nvidia-ru+cpu-int8 | gliner | 4/41 | 48,779 / 48,779 | 100.00% | 0.00% | 0.00% | 0.000 | - | - |
| gliner-urchade-ru+cpu-int8 | gliner | 4/41 | 48,779 / 48,779 | 100.00% | 0.00% | 0.00% | 0.000 | - | - |
| pplx+homoglyph | pplx | 3/41 | 815 / 7,486 | 10.89% | 81.93% | 7.62% | 0.552 | - | - |
| nym-base+homoglyph | hf | 3/41 | 957 / 7,486 | 12.78% | 71.53% | 4.91% | 0.592 | - | - |
| ru-legal-ner+homoglyph | hf | 3/41 | 1,753 / 7,486 | 23.42% | 59.24% | 11.07% | 0.387 | - | - |
| gliner-nvidia+homoglyph | gliner | 3/41 | 2,467 / 7,486 | 32.95% | 60.87% | 2.86% | 0.579 | - | - |
| opf-ru-v2+homoglyph | opf | 3/41 | 2,509 / 7,486 | 33.52% | 51.03% | 2.76% | 0.564 | - | - |
| gliner2-vladlinv+homoglyph | gliner2 | 3/41 | 3,969 / 7,486 | 53.02% | 45.00% | 0.07% | 0.471 | - | - |
| ner-ru-gherman+homoglyph | hf | 3/41 | 4,781 / 7,486 | 63.87% | 23.39% | 0.17% | 0.318 | - | - |
| credsweeper | leaks | 3/41 | 1,905 / 2,701 | 70.53% | 27.36% | 2.23% | 0.526 | - | - |
| trufflehog | leaks | 3/41 | 2,468 / 2,701 | 91.37% | 7.89% | 0.72% | 0.202 | - | - |
| noseyparker | leaks | 3/41 | 2,476 / 2,701 | 91.67% | 7.59% | 1.65% | 0.320 | - | - |
| ru-legal-ner+cpu | hf | 2/41 | 3,652 / 18,205 | 20.06% | 62.97% | 1.70% | 0.788 | - | - |
| presidio-ru | presidio | 2/41 | 3,426 / 7,183 | 47.70% | 47.63% | 2.98% | 0.594 | - | - |
| titus | leaks | 2/41 | 1,852 / 1,955 | 94.73% | 4.45% | 0.84% | 0.352 | - | - |
| kingfisher | leaks | 2/41 | 1,892 / 1,955 | 96.78% | 2.92% | 0.80% | 0.365 | - | - |

## Measured CPU speed

AMD EPYC 9K84, 16 threads per process, 24 concurrent workers. Batch throughput under that load, not the latency of one request. Amortized ms/row quantiles are the per-row share of measured compute, not individually timed requests.

![Measured CPU throughput per detector](../assets/cpu-speed.svg)

| Detector | Seconds / 10k chars | Chars / s | Rows / s | Amortized ms/row p50 | p95 | Peak RSS MB | Datasets |
|---|---:|---:|---:|---:|---:|---:|---:|
| natasha | 0.08 | 130,799 | 83.33 | 3 | 49 | 209 | 9 |
| spacy-alrosait | 0.19 | 53,307 | 33.96 | 9 | 121 | 1,492 | 9 |
| spacy-ru-lg | 0.19 | 52,320 | 33.33 | 7 | 128 | 1,494 | 9 |
| ru-legal-ner | 0.20 | 50,942 | 28.99 | 11 | 134 | 903 | 8 |
| gravitee-small | 0.66 | 15,141 | 9.65 | 40 | 485 | 1,065 | 9 |
| kalyan-ettin | 1.14 | 8,742 | 5.57 | 65 | 873 | 1,148 | 9 |
| ru-pii-ner | 1.42 | 7,053 | 4.49 | 64 | 1,023 | 2,774 | 9 |
| gliner2-hivetrace-uni-ru | 2.04 | 4,906 | 4.04 | 106 | 1,025 | 2,088 | 4 |
| davlan-xlmr | 2.26 | 4,431 | 2.82 | 90 | 1,552 | 1,612 | 9 |
| mmbert32k | 2.32 | 4,313 | 2.75 | 85 | 1,514 | 1,856 | 9 |
| ner-ru-gherman | 2.48 | 4,026 | 2.56 | 118 | 1,659 | 1,332 | 9 |
| davlan-mbert | 2.51 | 3,983 | 2.54 | 109 | 1,686 | 1,367 | 9 |
| gliner2-hivetrace-uni | 2.92 | 3,424 | 1.74 | 242 | 2,108 | 2,495 | 7 |
| openmed-nemotron | 3.04 | 3,287 | 2.09 | 118 | 1,844 | 2,848 | 9 |
| fef2-secret-ru | 3.05 | 3,278 | 2.09 | 113 | 2,073 | 1,395 | 9 |
| nym-base | 3.21 | 3,116 | 1.45 | 168 | 3,014 | 2,053 | 6 |
| openmed-multilingual | 3.25 | 3,076 | 1.96 | 117 | 2,130 | 2,783 | 9 |
| traciora | 3.29 | 3,040 | 1.94 | 130 | 1,977 | 3,544 | 9 |
| opf-kz-ru | 3.39 | 2,950 | 1.88 | 128 | 2,165 | 3,807 | 9 |
| opf-ru-v2 | 3.47 | 2,886 | 1.64 | 197 | 2,264 | 3,626 | 8 |
| opf-ru | 3.52 | 2,839 | 1.66 | 149 | 2,145 | 3,721 | 8 |
| apararti | 4.09 | 2,446 | 1.56 | 158 | 2,499 | 3,999 | 9 |
| openai-base | 4.21 | 2,378 | 1.51 | 159 | 2,679 | 4,188 | 9 |
| gliner-pii-base | 5.24 | 1,907 | 1.21 | 310 | 3,302 | 3,054 | 9 |
| gliner-urchade-ru | 6.22 | 1,608 | 1.32 | 333 | 2,893 | 3,141 | 4 |
| gliner-multi-v21-ru | 6.71 | 1,491 | 1.23 | 332 | 3,447 | 3,122 | 4 |
| gliner-pii-edge | 6.88 | 1,454 | 0.93 | 435 | 3,678 | 3,842 | 9 |
| ner-ru-yqelz | 7.08 | 1,413 | 0.90 | 298 | 4,727 | 2,506 | 9 |
| gliner25-fastino-ru | 7.69 | 1,301 | 1.07 | 499 | 3,438 | 3,157 | 4 |
| gliner-stream-pii | 8.20 | 1,219 | 0.78 | 453 | 5,465 | 5,957 | 9 |
| stanza-ru | 8.35 | 1,198 | 0.76 | 257 | 6,290 | 1,467 | 9 |
| gliner2-hivetrace-omni-ru | 8.60 | 1,163 | 0.96 | 683 | 3,647 | 3,330 | 4 |
| gliner2-fastino-ru | 8.90 | 1,123 | 0.92 | 697 | 3,585 | 3,324 | 4 |
| gliner-urchade | 9.68 | 1,033 | 0.66 | 437 | 6,519 | 3,139 | 9 |
| gliner-multi-v21 | 9.89 | 1,011 | 0.64 | 483 | 6,741 | 3,244 | 9 |
| pplx | 9.94 | 1,006 | 0.52 | 642 | 7,479 | 4,133 | 7 |
| gliner25-fastino | 12.47 | 802 | 0.51 | 714 | 8,092 | 4,490 | 9 |
| gliner2-vladlinv | 14.49 | 690 | 0.44 | 860 | 9,428 | 4,536 | 9 |
| gliner2-hivetrace-omni | 14.79 | 676 | 0.43 | 865 | 9,516 | 4,567 | 9 |
| gliner2-fastino | 14.93 | 670 | 0.43 | 914 | 10,073 | 4,665 | 9 |
| gliner2-vladlinv-ru | 17.57 | 569 | 2.64 | 373 | 942 | 3,155 | 3 |
| gliner-nvidia-ru | 20.00 | 500 | 0.41 | 1,223 | 8,802 | 4,266 | 4 |
| nuner-zero | 20.12 | 497 | 0.32 | 1,573 | 12,582 | 4,263 | 9 |
| gliner-nvidia | 22.62 | 442 | 0.26 | 2,184 | 15,780 | 4,259 | 8 |
| gliner2-large | 24.69 | 405 | 0.26 | 2,079 | 14,714 | 5,969 | 9 |

## Measured GPU speed

NVIDIA GeForce RTX 5090, 2 concurrent workers. BardsAI has no row: its ONNX graph runs on CPU only.

![Measured GPU throughput per detector](../assets/gpu-speed.svg)

| Detector | Seconds / 10k chars | Chars / s | Rows / s | Amortized ms/row p50 | p95 | Peak RSS MB | Datasets |
|---|---:|---:|---:|---:|---:|---:|---:|
| ru-legal-ner | 0.13 | 76,562 | 135.32 | 3 | 29 | 1,367 | 40 |
| davlan-xlmr | 0.14 | 73,674 | 130.22 | 4 | 30 | 2,184 | 40 |
| nym-base | 0.14 | 72,492 | 128.13 | 4 | 30 | 2,456 | 40 |
| davlan-mbert | 0.15 | 68,000 | 120.19 | 4 | 32 | 1,522 | 40 |
| fef2-secret-ru | 0.15 | 66,971 | 140.02 | 4 | 24 | 1,547 | 35 |
| ner-ru-gherman | 0.15 | 66,682 | 117.86 | 4 | 33 | 1,541 | 40 |
| gliner25-fastino | 0.15 | 65,451 | 115.68 | 4 | 35 | 2,856 | 40 |
| gliner-pii-base | 0.16 | 63,679 | 112.55 | 4 | 37 | 2,123 | 40 |
| gliner2-vladlinv | 0.17 | 57,801 | 102.16 | 4 | 39 | 3,229 | 40 |
| ner-ru-yqelz | 0.18 | 56,345 | 99.59 | 5 | 38 | 3,300 | 40 |
| mmbert32k | 0.18 | 54,765 | 96.80 | 4 | 40 | 2,434 | 40 |
| gliner-multi-v21 | 0.19 | 53,869 | 95.21 | 5 | 39 | 3,182 | 40 |
| gliner-urchade | 0.20 | 49,158 | 86.89 | 5 | 46 | 3,140 | 40 |
| gliner-stream-pii | 0.21 | 48,113 | 64.04 | 7 | 61 | 4,868 | 11 |
| gliner2-fastino | 0.27 | 37,693 | 66.62 | 7 | 57 | 3,348 | 40 |
| gliner2-hivetrace-omni | 0.29 | 34,790 | 67.59 | 7 | 56 | 3,334 | 30 |
| gliner-nvidia | 0.37 | 26,888 | 47.52 | 9 | 80 | 4,255 | 40 |
| nuner-zero | 0.38 | 26,176 | 46.27 | 10 | 82 | 4,287 | 40 |
| gliner2-large | 0.61 | 16,474 | 29.12 | 16 | 130 | 4,506 | 40 |
| openmed-multilingual | 0.84 | 11,953 | 17.15 | 30 | 211 | 3,821 | 31 |
| openmed-nemotron | 0.87 | 11,447 | 16.42 | 31 | 222 | 3,821 | 31 |
| opf-ru | 1.12 | 8,946 | 12.83 | 42 | 275 | 3,817 | 31 |
| traciora | 1.36 | 7,361 | 11.17 | 52 | 347 | 3,814 | 10 |
| opf-kz-ru | 1.59 | 6,275 | 11.09 | 59 | 298 | 3,814 | 40 |
| apararti | 1.69 | 5,933 | 10.49 | 62 | 320 | 3,815 | 40 |
| openai-base | 1.80 | 5,543 | 7.95 | 71 | 437 | 3,814 | 31 |
| pplx | 2.20 | 4,551 | 8.04 | 60 | 426 | 4,234 | 40 |
| gliner-pii-edge | 5.80 | 1,723 | 9.29 | 22 | 435 | 1,685 | 6 |

## Cost against quality

![Detector quality against measured cost](../assets/speed-quality.svg)

Other machines, quantized runs, scanners and every historical measurement condition are in [speed.md](speed.md). Per-language results are in [by-language.md](by-language.md), exact per-dataset counts in [dataset-metrics.csv](dataset-metrics.csv), and execution metadata in [run-inventory.json](run-inventory.json).
