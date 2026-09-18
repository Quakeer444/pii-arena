# synth-env-configs: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/synth-env-configs.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 191/392 | 48.72% | 53.83% | 47.45% |
| composition:pplx | eligible | Passwords, keys & tokens | 385/392 | 98.21% | 100.00% | 97.96% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 385/392 | 98.21% | 100.00% | 97.96% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 387/392 | 98.72% | 100.00% | 98.47% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 387/392 | 98.72% | 100.00% | 98.47% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 385/392 | 98.21% | 100.00% | 97.96% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 268/392 | 68.37% | 97.96% | 66.84% |
| model:apararti | eligible | Passwords, keys & tokens | 307/392 | 78.32% | 99.23% | 75.51% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 223/392 | 56.89% | 89.80% | 45.15% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/392 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/392 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 225/392 | 57.40% | 91.07% | 47.96% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 81/392 | 20.66% | 23.21% | 20.66% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 173/392 | 44.13% | 45.15% | 44.13% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 71/392 | 18.11% | 20.66% | 17.86% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 247/392 | 63.01% | 68.62% | 61.22% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 166/392 | 42.35% | 48.21% | 42.35% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 109/392 | 27.81% | 27.81% | 27.81% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 191/392 | 48.72% | 53.83% | 47.45% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 212/392 | 54.08% | 54.08% | 54.08% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 2/392 | 0.51% | 0.51% | 0.51% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 29/392 | 7.40% | 7.40% | 7.40% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 119/392 | 30.36% | 32.14% | 29.85% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 194/392 | 49.49% | 50.26% | 49.23% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 159/392 | 40.56% | 76.79% | 33.16% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 183/392 | 46.68% | 92.35% | 20.15% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 99/392 | 25.26% | 86.99% | 0.26% |
| model:natasha | eligible | Passwords, keys & tokens | 0/392 | 0.00% | 0.26% | 0.00% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 1/392 | 0.26% | 0.26% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 6/392 | 1.53% | 15.56% | 0.00% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 147/392 | 37.50% | 41.07% | 36.99% |
| model:nym-base | eligible | Passwords, keys & tokens | 221/392 | 56.38% | 96.94% | 37.24% |
| model:openai-base | eligible | Passwords, keys & tokens | 303/392 | 77.30% | 95.15% | 75.00% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 252/392 | 64.29% | 98.98% | 51.79% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 212/392 | 54.08% | 91.33% | 32.65% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 326/392 | 83.16% | 99.74% | 81.12% |
| model:opf-ru | eligible | Passwords, keys & tokens | 264/392 | 67.35% | 99.49% | 62.50% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 261/392 | 66.58% | 97.96% | 63.52% |
| model:pplx | eligible | Passwords, keys & tokens | 385/392 | 98.21% | 100.00% | 97.96% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 112/392 | 28.57% | 86.22% | 1.02% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 40/392 | 10.20% | 12.24% | 9.69% |
| model:rules-ru | eligible | Passwords, keys & tokens | 375/392 | 95.66% | 95.92% | 95.66% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/392 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 5/392 | 1.28% | 1.28% | 1.28% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 73/392 | 18.62% | 48.72% | 9.44% |
| model:traciora | eligible | Passwords, keys & tokens | 263/392 | 67.09% | 99.49% | 58.93% |
