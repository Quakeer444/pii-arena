# synth-secrets-ru: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/synth-secrets-ru.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 346/581 | 59.55% | 64.89% | 56.11% |
| composition:pplx | eligible | Passwords, keys & tokens | 567/581 | 97.59% | 100.00% | 97.25% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 567/581 | 97.59% | 100.00% | 97.25% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 571/581 | 98.28% | 100.00% | 97.76% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 571/581 | 98.28% | 100.00% | 97.76% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 567/581 | 97.59% | 100.00% | 97.25% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 482/581 | 82.96% | 98.11% | 81.24% |
| model:apararti | eligible | Passwords, keys & tokens | 533/581 | 91.74% | 99.31% | 86.06% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 408/581 | 70.22% | 90.53% | 60.93% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/581 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/581 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 326/581 | 56.11% | 74.18% | 45.61% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 84/581 | 14.46% | 19.97% | 14.29% |
| model:gliner-multi-v21-ru | eligible | Passwords, keys & tokens | 94/581 | 16.18% | 22.03% | 15.83% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 358/581 | 61.62% | 63.86% | 61.62% |
| model:gliner-nvidia-ru | eligible | Passwords, keys & tokens | 246/581 | 42.34% | 43.03% | 42.34% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 125/581 | 21.51% | 23.41% | 21.51% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 414/581 | 71.26% | 85.20% | 69.02% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 236/581 | 40.62% | 47.50% | 40.62% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 186/581 | 32.01% | 34.94% | 32.01% |
| model:gliner-urchade-ru | eligible | Passwords, keys & tokens | 119/581 | 20.48% | 21.34% | 20.48% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 346/581 | 59.55% | 64.89% | 56.11% |
| model:gliner2-fastino-ru | eligible | Passwords, keys & tokens | 270/581 | 46.47% | 51.12% | 44.06% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 308/581 | 53.01% | 53.36% | 53.01% |
| model:gliner2-hivetrace-omni-ru | eligible | Passwords, keys & tokens | 242/581 | 41.65% | 41.82% | 41.65% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 6/581 | 1.03% | 1.03% | 1.03% |
| model:gliner2-hivetrace-uni-ru | eligible | Passwords, keys & tokens | 68/581 | 11.70% | 15.49% | 11.70% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 138/581 | 23.75% | 26.68% | 23.75% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 163/581 | 28.06% | 30.64% | 27.37% |
| model:gliner2-vladlinv-ru | eligible | Passwords, keys & tokens | 193/581 | 33.22% | 35.28% | 31.84% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 330/581 | 56.80% | 60.07% | 56.11% |
| model:gliner25-fastino-ru | eligible | Passwords, keys & tokens | 302/581 | 51.98% | 54.39% | 51.46% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 136/581 | 23.41% | 42.51% | 17.90% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 257/581 | 44.23% | 85.20% | 13.77% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 128/581 | 22.03% | 76.59% | 0.00% |
| model:natasha | eligible | Passwords, keys & tokens | 1/581 | 0.17% | 0.17% | 0.17% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/581 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 30/581 | 5.16% | 9.29% | 0.17% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 303/581 | 52.15% | 65.92% | 50.43% |
| model:nym-base | eligible | Passwords, keys & tokens | 396/581 | 68.16% | 96.39% | 44.92% |
| model:nym-small | eligible | Passwords, keys & tokens | 354/581 | 60.93% | 94.49% | 34.60% |
| model:openai-base | eligible | Passwords, keys & tokens | 533/581 | 91.74% | 97.93% | 87.61% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 419/581 | 72.12% | 96.56% | 43.72% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 311/581 | 53.53% | 85.20% | 25.13% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 547/581 | 94.15% | 99.31% | 88.30% |
| model:opf-ru | eligible | Passwords, keys & tokens | 463/581 | 79.69% | 99.83% | 66.09% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 470/581 | 80.90% | 97.42% | 74.35% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 566/581 | 97.42% | 99.66% | 94.66% |
| model:pplx | eligible | Passwords, keys & tokens | 567/581 | 97.59% | 100.00% | 97.25% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 207/581 | 35.63% | 91.05% | 3.44% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 75/581 | 12.91% | 17.90% | 11.19% |
| model:rules-ru | eligible | Passwords, keys & tokens | 473/581 | 81.41% | 81.93% | 81.24% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/581 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 4/581 | 0.69% | 0.69% | 0.69% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 165/581 | 28.40% | 59.04% | 17.04% |
| model:traciora | eligible | Passwords, keys & tokens | 449/581 | 77.28% | 97.07% | 58.69% |
