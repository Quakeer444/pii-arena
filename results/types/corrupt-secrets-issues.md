# corrupt-secrets-issues: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/corrupt-secrets-issues.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 103/288 | 35.76% | 64.58% | 34.38% |
| composition:pplx | eligible | Passwords, keys & tokens | 218/288 | 75.69% | 95.83% | 73.61% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 222/288 | 77.08% | 97.22% | 75.00% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 230/288 | 79.86% | 99.65% | 77.78% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 230/288 | 79.86% | 100.00% | 78.12% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 223/288 | 77.43% | 98.61% | 75.35% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 197/288 | 68.40% | 94.10% | 62.85% |
| model:apararti | eligible | Passwords, keys & tokens | 210/288 | 72.92% | 97.22% | 65.62% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 204/288 | 70.83% | 94.44% | 54.51% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/288 | 0.00% | 1.04% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/288 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 96/288 | 33.33% | 51.04% | 28.82% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 24/288 | 8.33% | 26.39% | 8.33% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 86/288 | 29.86% | 47.57% | 29.51% |
| model:gliner-nvidia+homoglyph | eligible | Passwords, keys & tokens | 86/288 | 29.86% | 47.57% | 29.51% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 22/288 | 7.64% | 13.54% | 7.64% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 152/288 | 52.78% | 86.46% | 45.14% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 80/288 | 27.78% | 55.90% | 26.74% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 99/288 | 34.38% | 55.21% | 34.38% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 103/288 | 35.76% | 64.58% | 34.38% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 47/288 | 16.32% | 30.21% | 16.32% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 15/288 | 5.21% | 14.93% | 4.86% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 33/288 | 11.46% | 29.86% | 11.46% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 12/288 | 4.17% | 9.72% | 3.47% |
| model:gliner2-vladlinv+homoglyph | eligible | Passwords, keys & tokens | 12/288 | 4.17% | 9.72% | 3.47% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 67/288 | 23.26% | 42.36% | 23.26% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 32/288 | 11.11% | 27.08% | 7.64% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 154/288 | 53.47% | 86.81% | 10.07% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 101/288 | 35.07% | 83.33% | 0.00% |
| model:natasha | eligible | Passwords, keys & tokens | 0/288 | 0.00% | 2.43% | 0.00% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/288 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+homoglyph | eligible | Passwords, keys & tokens | 0/288 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 57/288 | 19.79% | 33.68% | 0.35% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 118/288 | 40.97% | 70.49% | 37.50% |
| model:nym-base | eligible | Passwords, keys & tokens | 182/288 | 63.19% | 96.18% | 32.29% |
| model:nym-base+homoglyph | eligible | Passwords, keys & tokens | 182/288 | 63.19% | 96.18% | 32.29% |
| model:nym-small | eligible | Passwords, keys & tokens | 161/288 | 55.90% | 95.83% | 24.31% |
| model:openai-base | eligible | Passwords, keys & tokens | 196/288 | 68.06% | 89.58% | 61.11% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 155/288 | 53.82% | 89.58% | 11.81% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 179/288 | 62.15% | 90.28% | 19.44% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 211/288 | 73.26% | 95.49% | 66.32% |
| model:opf-ru | eligible | Passwords, keys & tokens | 204/288 | 70.83% | 97.57% | 59.38% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 202/288 | 70.14% | 93.06% | 61.46% |
| model:opf-ru-v2+homoglyph | eligible | Passwords, keys & tokens | 202/288 | 70.14% | 92.71% | 62.15% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 244/288 | 84.72% | 100.00% | 83.33% |
| model:pplx | eligible | Passwords, keys & tokens | 218/288 | 75.69% | 95.83% | 73.61% |
| model:pplx+homoglyph | eligible | Passwords, keys & tokens | 218/288 | 75.69% | 95.83% | 73.61% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 120/288 | 41.67% | 77.43% | 1.04% |
| model:ru-legal-ner+homoglyph | eligible | Passwords, keys & tokens | 119/288 | 41.32% | 77.08% | 1.04% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 56/288 | 19.44% | 26.39% | 13.89% |
| model:rules-ru | eligible | Passwords, keys & tokens | 118/288 | 40.97% | 59.72% | 40.97% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/288 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 8/288 | 2.78% | 5.56% | 2.43% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 60/288 | 20.83% | 47.22% | 15.97% |
| model:traciora | eligible | Passwords, keys & tokens | 200/288 | 69.44% | 94.44% | 51.04% |
