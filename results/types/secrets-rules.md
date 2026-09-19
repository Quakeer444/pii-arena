# secrets-rules: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/secrets-rules.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 652/746 | 87.40% | 95.44% | 85.25% |
| composition:pplx | eligible | Passwords, keys & tokens | 697/746 | 93.43% | 96.11% | 84.99% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 730/746 | 97.86% | 99.33% | 97.32% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 737/746 | 98.79% | 99.73% | 98.79% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 740/746 | 99.20% | 100.00% | 98.93% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 736/746 | 98.66% | 100.00% | 97.59% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 709/746 | 95.04% | 97.05% | 91.55% |
| model:apararti | eligible | Passwords, keys & tokens | 737/746 | 98.79% | 99.60% | 97.45% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 613/746 | 82.17% | 90.21% | 65.68% |
| model:betterleaks | train | Passwords, keys & tokens | 719/746 | 96.38% | 96.38% | 96.11% |
| model:credsweeper | eligible | Passwords, keys & tokens | 570/746 | 76.41% | 77.21% | 76.14% |
| model:credsweeper-noml | eligible | Passwords, keys & tokens | 613/746 | 82.17% | 83.11% | 81.90% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 1/746 | 0.13% | 0.13% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/746 | 0.00% | 0.00% | 0.00% |
| model:deepsecrets | eligible | Passwords, keys & tokens | 305/746 | 40.88% | 42.09% | 40.88% |
| model:detect-secrets | eligible | Passwords, keys & tokens | 341/746 | 45.71% | 45.71% | 45.71% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 321/746 | 43.03% | 50.40% | 35.12% |
| model:gitleaks | train | Passwords, keys & tokens | 728/746 | 97.59% | 97.59% | 97.32% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 11/746 | 1.47% | 3.22% | 1.34% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 489/746 | 65.55% | 66.62% | 65.55% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 155/746 | 20.78% | 22.12% | 20.11% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 661/746 | 88.61% | 98.26% | 84.85% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 584/746 | 78.28% | 95.04% | 77.75% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 348/746 | 46.65% | 50.54% | 46.51% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 652/746 | 87.40% | 95.44% | 85.25% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 134/746 | 17.96% | 17.96% | 17.96% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 103/746 | 13.81% | 14.88% | 13.81% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 32/746 | 4.29% | 5.36% | 4.29% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 306/746 | 41.02% | 44.24% | 40.35% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 671/746 | 89.95% | 94.24% | 88.87% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 434/746 | 58.18% | 72.92% | 40.75% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 429/746 | 57.51% | 85.39% | 12.87% |
| model:kingfisher | train | Passwords, keys & tokens | 348/746 | 46.65% | 46.65% | 45.71% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 421/746 | 56.43% | 93.83% | 0.94% |
| model:natasha | eligible | Passwords, keys & tokens | 0/746 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 1/746 | 0.13% | 0.13% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 140/746 | 18.77% | 28.02% | 1.74% |
| model:noseyparker | eligible | Passwords, keys & tokens | 121/746 | 16.22% | 16.22% | 16.22% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 490/746 | 65.68% | 72.52% | 61.53% |
| model:nym-base | eligible | Passwords, keys & tokens | 621/746 | 83.24% | 98.93% | 54.69% |
| model:nym-small | eligible | Passwords, keys & tokens | 590/746 | 79.09% | 97.32% | 30.97% |
| model:openai-base | eligible | Passwords, keys & tokens | 731/746 | 97.99% | 99.06% | 97.18% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 553/746 | 74.13% | 87.94% | 27.88% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 478/746 | 64.08% | 85.25% | 11.39% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 734/746 | 98.39% | 99.33% | 97.18% |
| model:opf-ru | eligible | Passwords, keys & tokens | 734/746 | 98.39% | 99.60% | 93.16% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 725/746 | 97.18% | 98.79% | 95.71% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 735/746 | 98.53% | 99.87% | 97.99% |
| model:pplx | eligible | Passwords, keys & tokens | 697/746 | 93.43% | 96.11% | 84.99% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 485/746 | 65.01% | 96.92% | 5.36% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 74/746 | 9.92% | 14.34% | 5.76% |
| model:rules-ru | eligible | Passwords, keys & tokens | 556/746 | 74.53% | 75.60% | 74.40% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/746 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 50/746 | 6.70% | 7.24% | 6.70% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 74/746 | 9.92% | 19.97% | 7.10% |
| model:titus | train | Passwords, keys & tokens | 322/746 | 43.16% | 43.57% | 42.90% |
| model:traciora | eligible | Passwords, keys & tokens | 727/746 | 97.45% | 99.87% | 93.83% |
| model:trufflehog | eligible | Passwords, keys & tokens | 176/746 | 23.59% | 25.20% | 22.92% |
