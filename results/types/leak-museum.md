# leak-museum: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/leak-museum.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 73/101 | 72.28% | 80.20% | 72.28% |
| composition:pplx | eligible | Passwords, keys & tokens | 83/101 | 82.18% | 83.17% | 79.21% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 96/101 | 95.05% | 98.02% | 93.07% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 96/101 | 95.05% | 98.02% | 95.05% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 96/101 | 95.05% | 98.02% | 95.05% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 96/101 | 95.05% | 98.02% | 93.07% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 69/101 | 68.32% | 76.24% | 63.37% |
| model:apararti | eligible | Passwords, keys & tokens | 75/101 | 74.26% | 75.25% | 70.30% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 27/101 | 26.73% | 38.61% | 16.83% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 1/101 | 0.99% | 0.99% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/101 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 52/101 | 51.49% | 59.41% | 34.65% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 23/101 | 22.77% | 28.71% | 22.77% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 57/101 | 56.44% | 60.40% | 56.44% |
| model:gliner-nvidia+ov100 | eligible | Passwords, keys & tokens | 56/101 | 55.45% | 59.41% | 55.45% |
| model:gliner-nvidia+sent300 | eligible | Passwords, keys & tokens | 57/101 | 56.44% | 61.39% | 56.44% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 17/101 | 16.83% | 16.83% | 16.83% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 60/101 | 59.41% | 75.25% | 59.41% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 55/101 | 54.46% | 61.39% | 54.46% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 46/101 | 45.54% | 49.50% | 45.54% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 73/101 | 72.28% | 80.20% | 72.28% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 44/101 | 43.56% | 44.55% | 43.56% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 19/101 | 18.81% | 18.81% | 18.81% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 41/101 | 40.59% | 44.55% | 40.59% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 9/101 | 8.91% | 10.89% | 8.91% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 53/101 | 52.48% | 54.46% | 52.48% |
| model:gliner25-fastino+nochunk | eligible | Passwords, keys & tokens | 52/101 | 51.49% | 53.47% | 51.49% |
| model:gliner25-fastino+ov100 | eligible | Passwords, keys & tokens | 54/101 | 53.47% | 55.45% | 53.47% |
| model:gliner25-fastino+sent300 | eligible | Passwords, keys & tokens | 55/101 | 54.46% | 58.42% | 54.46% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 28/101 | 27.72% | 36.63% | 21.78% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 39/101 | 38.61% | 46.53% | 22.77% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 23/101 | 22.77% | 42.57% | 0.99% |
| model:mmbert32k+nochunk | eligible | Passwords, keys & tokens | 22/101 | 21.78% | 41.58% | 0.00% |
| model:natasha | eligible | Passwords, keys & tokens | 4/101 | 3.96% | 3.96% | 3.96% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/101 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 6/101 | 5.94% | 7.92% | 1.98% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 65/101 | 64.36% | 70.30% | 64.36% |
| model:nym-base | eligible | Passwords, keys & tokens | 35/101 | 34.65% | 46.53% | 28.71% |
| model:nym-base+ov100 | eligible | Passwords, keys & tokens | 35/101 | 34.65% | 46.53% | 28.71% |
| model:nym-base+sent300 | eligible | Passwords, keys & tokens | 36/101 | 35.64% | 48.51% | 28.71% |
| model:openai-base | eligible | Passwords, keys & tokens | 57/101 | 56.44% | 63.37% | 51.49% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 56/101 | 55.45% | 62.38% | 31.68% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 31/101 | 30.69% | 39.60% | 17.82% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 71/101 | 70.30% | 74.26% | 64.36% |
| model:opf-ru | eligible | Passwords, keys & tokens | 78/101 | 77.23% | 85.15% | 60.40% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 62/101 | 61.39% | 71.29% | 49.50% |
| model:opf-ru-v2+ov100 | eligible | Passwords, keys & tokens | 63/101 | 62.38% | 72.28% | 47.52% |
| model:opf-ru-v2+sent300 | eligible | Passwords, keys & tokens | 64/101 | 63.37% | 73.27% | 51.49% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 84/101 | 83.17% | 90.10% | 77.23% |
| model:pplx | eligible | Passwords, keys & tokens | 83/101 | 82.18% | 83.17% | 79.21% |
| model:pplx+ov100 | eligible | Passwords, keys & tokens | 87/101 | 86.14% | 88.12% | 83.17% |
| model:pplx+sent300 | eligible | Passwords, keys & tokens | 83/101 | 82.18% | 83.17% | 78.22% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 27/101 | 26.73% | 49.50% | 7.92% |
| model:ru-legal-ner+ov100 | eligible | Passwords, keys & tokens | 26/101 | 25.74% | 48.51% | 7.92% |
| model:ru-legal-ner+sent300 | eligible | Passwords, keys & tokens | 25/101 | 24.75% | 48.51% | 8.91% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 12/101 | 11.88% | 16.83% | 8.91% |
| model:rules-ru | eligible | Passwords, keys & tokens | 62/101 | 61.39% | 63.37% | 61.39% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/101 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 5/101 | 4.95% | 4.95% | 4.95% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 15/101 | 14.85% | 28.71% | 11.88% |
| model:traciora | eligible | Passwords, keys & tokens | 64/101 | 63.37% | 71.29% | 52.48% |
