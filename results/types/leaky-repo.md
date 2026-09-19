# leaky-repo: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/leaky-repo.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 60/95 | 63.16% | 82.11% | 63.16% |
| composition:pplx | eligible | Passwords, keys & tokens | 81/95 | 85.26% | 92.63% | 85.26% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 85/95 | 89.47% | 98.95% | 89.47% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 88/95 | 92.63% | 98.95% | 92.63% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 88/95 | 92.63% | 98.95% | 92.63% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 85/95 | 89.47% | 98.95% | 89.47% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 65/95 | 68.42% | 89.47% | 64.21% |
| model:apararti | eligible | Passwords, keys & tokens | 67/95 | 70.53% | 84.21% | 60.00% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 51/95 | 53.68% | 78.95% | 45.26% |
| model:credsweeper-noml | eligible | Passwords, keys & tokens | 52/95 | 54.74% | 55.79% | 52.63% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:deepsecrets | eligible | Passwords, keys & tokens | 27/95 | 28.42% | 30.53% | 28.42% |
| model:detect-secrets | eligible | Passwords, keys & tokens | 31/95 | 32.63% | 34.74% | 32.63% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 33/95 | 34.74% | 42.11% | 27.37% |
| model:gitleaks | eligible | Passwords, keys & tokens | 22/95 | 23.16% | 23.16% | 23.16% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 21/95 | 22.11% | 30.53% | 22.11% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 47/95 | 49.47% | 56.84% | 49.47% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 11/95 | 11.58% | 14.74% | 11.58% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 48/95 | 50.53% | 77.89% | 50.53% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 40/95 | 42.11% | 58.95% | 42.11% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 40/95 | 42.11% | 51.58% | 42.11% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 60/95 | 63.16% | 82.11% | 63.16% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 49/95 | 51.58% | 60.00% | 51.58% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 16/95 | 16.84% | 18.95% | 16.84% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 31/95 | 32.63% | 41.05% | 32.63% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 17/95 | 17.89% | 18.95% | 17.89% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 51/95 | 53.68% | 64.21% | 53.68% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 24/95 | 25.26% | 42.11% | 17.89% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 47/95 | 49.47% | 76.84% | 22.11% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 33/95 | 34.74% | 66.32% | 1.05% |
| model:natasha | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 1.05% | 0.00% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 13/95 | 13.68% | 18.95% | 1.05% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 48/95 | 50.53% | 61.05% | 49.47% |
| model:nym-base | eligible | Passwords, keys & tokens | 60/95 | 63.16% | 83.16% | 34.74% |
| model:nym-small | eligible | Passwords, keys & tokens | 57/95 | 60.00% | 88.42% | 38.95% |
| model:openai-base | eligible | Passwords, keys & tokens | 57/95 | 60.00% | 70.53% | 50.53% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 56/95 | 58.95% | 90.53% | 31.58% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 52/95 | 54.74% | 85.26% | 23.16% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 72/95 | 75.79% | 83.16% | 62.11% |
| model:opf-ru | eligible | Passwords, keys & tokens | 76/95 | 80.00% | 91.58% | 65.26% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 54/95 | 56.84% | 76.84% | 47.37% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 73/95 | 76.84% | 82.11% | 73.68% |
| model:pplx | eligible | Passwords, keys & tokens | 81/95 | 85.26% | 92.63% | 85.26% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 31/95 | 32.63% | 70.53% | 9.47% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 5/95 | 5.26% | 11.58% | 2.11% |
| model:rules-ru | eligible | Passwords, keys & tokens | 33/95 | 34.74% | 36.84% | 34.74% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 4/95 | 4.21% | 4.21% | 4.21% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 14/95 | 14.74% | 25.26% | 12.63% |
| model:traciora | eligible | Passwords, keys & tokens | 58/95 | 61.05% | 81.05% | 44.21% |
