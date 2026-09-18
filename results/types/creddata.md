# creddata: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/creddata.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 605/776 | 77.96% | 85.70% | 77.19% |
| composition:pplx | eligible | Passwords, keys & tokens | 672/776 | 86.60% | 94.20% | 80.28% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 724/776 | 93.30% | 98.32% | 91.88% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 738/776 | 95.10% | 99.23% | 94.59% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 743/776 | 95.75% | 99.87% | 95.23% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 732/776 | 94.33% | 99.87% | 93.04% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 692/776 | 89.18% | 96.39% | 86.86% |
| model:apararti | eligible | Passwords, keys & tokens | 731/776 | 94.20% | 97.55% | 90.34% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 501/776 | 64.56% | 75.77% | 54.38% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/776 | 0.00% | 0.13% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/776 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 492/776 | 63.40% | 65.59% | 57.09% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 158/776 | 20.36% | 24.48% | 20.36% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 608/776 | 78.35% | 81.96% | 78.35% |
| model:gliner-nvidia+ov100 | eligible | Passwords, keys & tokens | 610/776 | 78.61% | 82.22% | 78.61% |
| model:gliner-nvidia+sent300 | eligible | Passwords, keys & tokens | 610/776 | 78.61% | 82.86% | 78.61% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 135/776 | 17.40% | 18.94% | 17.40% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 621/776 | 80.03% | 92.14% | 78.99% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 604/776 | 77.84% | 85.44% | 77.45% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 450/776 | 57.99% | 62.37% | 57.99% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 605/776 | 77.96% | 85.70% | 77.19% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 385/776 | 49.61% | 51.93% | 49.61% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 177/776 | 22.81% | 23.84% | 22.81% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 342/776 | 44.07% | 47.81% | 44.07% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 437/776 | 56.31% | 59.41% | 56.31% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 637/776 | 82.09% | 86.34% | 81.57% |
| model:gliner25-fastino+nochunk | eligible | Passwords, keys & tokens | 637/776 | 82.09% | 86.47% | 81.57% |
| model:gliner25-fastino+ov100 | eligible | Passwords, keys & tokens | 637/776 | 82.09% | 86.60% | 81.44% |
| model:gliner25-fastino+sent300 | eligible | Passwords, keys & tokens | 639/776 | 82.35% | 87.11% | 81.83% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 302/776 | 38.92% | 49.48% | 29.51% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 604/776 | 77.84% | 92.01% | 54.38% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 471/776 | 60.70% | 89.43% | 13.14% |
| model:mmbert32k+nochunk | eligible | Passwords, keys & tokens | 469/776 | 60.44% | 89.05% | 13.14% |
| model:natasha | eligible | Passwords, keys & tokens | 0/776 | 0.00% | 0.52% | 0.00% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/776 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 334/776 | 43.04% | 54.77% | 12.50% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 503/776 | 64.82% | 74.10% | 64.43% |
| model:nym-base | eligible | Passwords, keys & tokens | 678/776 | 87.37% | 98.71% | 75.39% |
| model:nym-base+ov100 | eligible | Passwords, keys & tokens | 678/776 | 87.37% | 98.71% | 75.39% |
| model:nym-base+sent300 | eligible | Passwords, keys & tokens | 677/776 | 87.24% | 98.84% | 75.39% |
| model:openai-base | eligible | Passwords, keys & tokens | 686/776 | 88.40% | 91.11% | 83.89% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 588/776 | 75.77% | 91.24% | 37.11% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 530/776 | 68.30% | 85.70% | 26.03% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 740/776 | 95.36% | 97.94% | 91.62% |
| model:opf-ru | eligible | Passwords, keys & tokens | 719/776 | 92.65% | 97.04% | 82.99% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 705/776 | 90.85% | 95.62% | 81.83% |
| model:opf-ru-v2+ov100 | eligible | Passwords, keys & tokens | 706/776 | 90.98% | 95.49% | 82.73% |
| model:opf-ru-v2+sent300 | eligible | Passwords, keys & tokens | 703/776 | 90.59% | 95.62% | 81.96% |
| model:pplx | eligible | Passwords, keys & tokens | 672/776 | 86.60% | 94.20% | 80.28% |
| model:pplx+ov100 | eligible | Passwords, keys & tokens | 672/776 | 86.60% | 94.20% | 80.41% |
| model:pplx+sent300 | eligible | Passwords, keys & tokens | 666/776 | 85.82% | 93.81% | 79.64% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 529/776 | 68.17% | 89.95% | 19.07% |
| model:ru-legal-ner+ov100 | eligible | Passwords, keys & tokens | 529/776 | 68.17% | 89.95% | 19.07% |
| model:ru-legal-ner+sent300 | eligible | Passwords, keys & tokens | 525/776 | 67.65% | 89.82% | 18.69% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 268/776 | 34.54% | 38.92% | 23.32% |
| model:rules-ru | eligible | Passwords, keys & tokens | 295/776 | 38.02% | 39.69% | 37.37% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/776 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 80/776 | 10.31% | 10.82% | 10.18% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 96/776 | 12.37% | 20.36% | 6.96% |
| model:traciora | eligible | Passwords, keys & tokens | 709/776 | 91.37% | 97.55% | 75.52% |
