# synth-secrets-en: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/synth-secrets-en.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 337/581 | 58.00% | 64.54% | 54.91% |
| composition:pplx | eligible | Passwords, keys & tokens | 566/581 | 97.42% | 99.83% | 97.07% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 566/581 | 97.42% | 99.83% | 97.07% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 569/581 | 97.93% | 100.00% | 97.59% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 569/581 | 97.93% | 100.00% | 97.59% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 567/581 | 97.59% | 100.00% | 97.07% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 479/581 | 82.44% | 97.59% | 80.03% |
| model:apararti | eligible | Passwords, keys & tokens | 511/581 | 87.95% | 97.07% | 80.38% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 427/581 | 73.49% | 92.94% | 62.13% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/581 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/581 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 309/581 | 53.18% | 71.08% | 43.37% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 106/581 | 18.24% | 25.13% | 17.73% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 360/581 | 61.96% | 64.37% | 61.96% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 181/581 | 31.15% | 34.60% | 30.64% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 410/581 | 70.57% | 83.65% | 68.67% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 240/581 | 41.31% | 48.54% | 41.31% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 162/581 | 27.88% | 30.64% | 27.88% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 337/581 | 58.00% | 64.54% | 54.91% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 315/581 | 54.22% | 54.56% | 54.22% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 5/581 | 0.86% | 0.86% | 0.86% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 103/581 | 17.73% | 19.45% | 17.56% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 146/581 | 25.13% | 27.02% | 24.27% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 314/581 | 54.04% | 56.80% | 53.01% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 269/581 | 46.30% | 70.91% | 37.35% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 279/581 | 48.02% | 85.54% | 16.01% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 121/581 | 20.83% | 78.31% | 0.00% |
| model:natasha | eligible | Passwords, keys & tokens | 0/581 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/581 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 33/581 | 5.68% | 11.36% | 0.34% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 309/581 | 53.18% | 64.37% | 51.29% |
| model:nym-base | eligible | Passwords, keys & tokens | 363/581 | 62.48% | 93.98% | 41.31% |
| model:nym-small | eligible | Passwords, keys & tokens | 333/581 | 57.31% | 93.29% | 29.60% |
| model:openai-base | eligible | Passwords, keys & tokens | 491/581 | 84.51% | 92.94% | 79.35% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 479/581 | 82.44% | 99.14% | 61.79% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 332/581 | 57.14% | 87.09% | 30.46% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 531/581 | 91.39% | 98.28% | 84.51% |
| model:opf-ru | eligible | Passwords, keys & tokens | 450/581 | 77.45% | 98.28% | 63.86% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 457/581 | 78.66% | 96.04% | 70.74% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 568/581 | 97.76% | 99.66% | 93.98% |
| model:pplx | eligible | Passwords, keys & tokens | 566/581 | 97.42% | 99.83% | 97.07% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 195/581 | 33.56% | 89.16% | 1.72% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 62/581 | 10.67% | 14.63% | 8.78% |
| model:rules-ru | eligible | Passwords, keys & tokens | 475/581 | 81.76% | 82.27% | 81.58% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/581 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 0/581 | 0.00% | 0.00% | 0.00% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 120/581 | 20.65% | 45.09% | 11.88% |
| model:traciora | eligible | Passwords, keys & tokens | 410/581 | 70.57% | 94.49% | 51.46% |
