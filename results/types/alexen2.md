# alexen2: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/alexen2.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | People's names | 294/571 | 51.49% | 99.47% | 51.49% |
| composition:fastino | eligible | Phone numbers & email | 56/690 | 8.12% | 100.00% | 8.12% |
| composition:pplx | eligible | People's names | 289/571 | 50.61% | 88.44% | 40.98% |
| composition:pplx | eligible | Phone numbers & email | 412/690 | 59.71% | 100.00% | 56.23% |
| composition:pplx+fastino | eligible | People's names | 367/571 | 64.27% | 99.82% | 64.27% |
| composition:pplx+fastino | eligible | Phone numbers & email | 412/690 | 59.71% | 100.00% | 59.71% |
| composition:pplx+fastino+bardsai | eligible | People's names | 368/571 | 64.45% | 99.82% | 64.45% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 439/690 | 63.62% | 100.00% | 63.62% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 368/571 | 64.45% | 99.82% | 64.45% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 439/690 | 63.62% | 100.00% | 63.62% |
| composition:pplx+fastino+mmbert | eligible | People's names | 368/571 | 64.45% | 99.82% | 64.27% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 412/690 | 59.71% | 100.00% | 59.71% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 274/571 | 47.99% | 95.10% | 43.61% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 59/690 | 8.55% | 100.00% | 8.55% |
| model:apararti | eligible | People's names | 220/571 | 38.53% | 84.94% | 35.90% |
| model:apararti | eligible | Phone numbers & email | 58/690 | 8.41% | 98.99% | 8.26% |
| model:bardsai-eu | eligible | People's names | 243/571 | 42.56% | 88.97% | 40.46% |
| model:bardsai-eu | eligible | Phone numbers & email | 89/690 | 12.90% | 96.23% | 12.46% |
| model:davlan-mbert | eligible | People's names | 263/571 | 46.06% | 94.05% | 41.86% |
| model:davlan-mbert | eligible | Phone numbers & email | 0/690 | 0.00% | 4.20% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 282/571 | 49.39% | 96.32% | 45.71% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/690 | 0.00% | 3.62% | 0.00% |
| model:fef2-secret-ru | eligible | People's names | 271/571 | 47.46% | 96.15% | 45.36% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 9/690 | 1.30% | 54.64% | 1.16% |
| model:gliner-multi-v21 | eligible | People's names | 291/571 | 50.96% | 99.12% | 50.96% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 49/690 | 7.10% | 77.97% | 7.10% |
| model:gliner-multi-v21-ru | eligible | People's names | 288/571 | 50.44% | 98.60% | 50.44% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 49/690 | 7.10% | 72.03% | 7.10% |
| model:gliner-nvidia | eligible | People's names | 275/571 | 48.16% | 96.85% | 47.29% |
| model:gliner-nvidia | eligible | Phone numbers & email | 59/690 | 8.55% | 100.00% | 8.55% |
| model:gliner-nvidia-ru | eligible | People's names | 237/571 | 41.51% | 95.62% | 24.17% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 59/690 | 8.55% | 100.00% | 8.55% |
| model:gliner-pii-base | eligible | People's names | 253/571 | 44.31% | 89.67% | 44.31% |
| model:gliner-pii-base | eligible | Phone numbers & email | 55/690 | 7.97% | 98.55% | 7.97% |
| model:gliner-pii-edge | eligible | People's names | 221/571 | 38.70% | 85.99% | 38.00% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 56/690 | 8.12% | 98.55% | 8.12% |
| model:gliner-stream-pii | eligible | People's names | 254/571 | 44.48% | 94.22% | 44.13% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 25/690 | 3.62% | 77.25% | 3.48% |
| model:gliner-urchade | eligible | People's names | 294/571 | 51.49% | 99.47% | 51.49% |
| model:gliner-urchade | eligible | Phone numbers & email | 59/690 | 8.55% | 99.42% | 8.55% |
| model:gliner-urchade-ru | eligible | People's names | 55/571 | 9.63% | 39.58% | 9.63% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 59/690 | 8.55% | 98.84% | 8.55% |
| model:gliner2-fastino | eligible | People's names | 294/571 | 51.49% | 99.47% | 51.49% |
| model:gliner2-fastino | eligible | Phone numbers & email | 56/690 | 8.12% | 100.00% | 8.12% |
| model:gliner2-fastino-ru | eligible | People's names | 290/571 | 50.79% | 99.47% | 50.79% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 55/690 | 7.97% | 99.86% | 7.97% |
| model:gliner2-hivetrace-omni | eligible | People's names | 292/571 | 51.14% | 99.30% | 51.14% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 57/690 | 8.26% | 99.86% | 8.26% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 292/571 | 51.14% | 99.30% | 51.14% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 57/690 | 8.26% | 99.86% | 8.26% |
| model:gliner2-hivetrace-uni | eligible | People's names | 234/571 | 40.98% | 87.04% | 40.98% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 41/690 | 5.94% | 87.54% | 5.94% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 54/571 | 9.46% | 24.87% | 9.46% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 11/690 | 1.59% | 9.13% | 1.59% |
| model:gliner2-large | eligible | People's names | 218/571 | 38.18% | 86.16% | 38.18% |
| model:gliner2-large | eligible | Phone numbers & email | 56/690 | 8.12% | 99.57% | 8.12% |
| model:gliner2-vladlinv | eligible | People's names | 273/571 | 47.81% | 100.00% | 47.81% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 59/690 | 8.55% | 100.00% | 8.55% |
| model:gliner2-vladlinv-ru | eligible | People's names | 273/571 | 47.81% | 100.00% | 47.81% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 59/690 | 8.55% | 100.00% | 8.55% |
| model:gliner25-fastino | eligible | People's names | 287/571 | 50.26% | 99.12% | 50.26% |
| model:gliner25-fastino | eligible | Phone numbers & email | 53/690 | 7.68% | 100.00% | 7.68% |
| model:gliner25-fastino-ru | eligible | People's names | 287/571 | 50.26% | 98.60% | 50.26% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 55/690 | 7.97% | 100.00% | 7.97% |
| model:gravitee-small | eligible | People's names | 186/571 | 32.57% | 76.53% | 28.55% |
| model:gravitee-small | eligible | Phone numbers & email | 50/690 | 7.25% | 93.62% | 6.38% |
| model:kalyan-ettin | eligible | People's names | 100/571 | 17.51% | 89.14% | 7.01% |
| model:kalyan-ettin | eligible | Phone numbers & email | 79/690 | 11.45% | 93.62% | 8.84% |
| model:mmbert32k | eligible | People's names | 242/571 | 42.38% | 96.32% | 21.19% |
| model:mmbert32k | eligible | Phone numbers & email | 43/690 | 6.23% | 100.00% | 5.80% |
| model:natasha | eligible | People's names | 268/571 | 46.94% | 92.99% | 45.53% |
| model:natasha | eligible | Phone numbers & email | 0/690 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 60/571 | 10.51% | 93.17% | 8.58% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/690 | 0.00% | 18.26% | 0.00% |
| model:ner-ru-yqelz | eligible | People's names | 314/571 | 54.99% | 99.82% | 54.64% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 15/690 | 2.17% | 19.71% | 2.03% |
| model:nuner-zero | eligible | People's names | 293/571 | 51.31% | 98.25% | 14.36% |
| model:nuner-zero | eligible | Phone numbers & email | 59/690 | 8.55% | 100.00% | 5.65% |
| model:nym-base | eligible | People's names | 90/571 | 15.76% | 97.55% | 51.31% |
| model:nym-base | eligible | Phone numbers & email | 59/690 | 8.55% | 99.86% | 8.55% |
| model:nym-small | eligible | People's names | 70/571 | 12.26% | 93.52% | 45.88% |
| model:nym-small | eligible | Phone numbers & email | 59/690 | 8.55% | 99.86% | 8.55% |
| model:openai-base | eligible | People's names | 204/571 | 35.73% | 75.66% | 32.92% |
| model:openai-base | eligible | Phone numbers & email | 59/690 | 8.55% | 97.97% | 8.55% |
| model:openmed-multilingual | eligible | People's names | 37/571 | 6.48% | 74.96% | 19.96% |
| model:openmed-multilingual | eligible | Phone numbers & email | 52/690 | 7.54% | 99.71% | 7.68% |
| model:openmed-nemotron | eligible | People's names | 102/571 | 17.86% | 89.32% | 29.95% |
| model:openmed-nemotron | eligible | Phone numbers & email | 39/690 | 5.65% | 96.67% | 5.22% |
| model:opf-kz-ru | eligible | People's names | 218/571 | 38.18% | 84.59% | 35.20% |
| model:opf-kz-ru | eligible | Phone numbers & email | 58/690 | 8.41% | 98.84% | 8.41% |
| model:opf-ru | eligible | People's names | 241/571 | 42.21% | 92.99% | 37.13% |
| model:opf-ru | eligible | Phone numbers & email | 55/690 | 7.97% | 97.97% | 7.68% |
| model:opf-ru-v2 | eligible | People's names | 241/571 | 42.21% | 85.64% | 36.08% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 53/690 | 7.68% | 97.39% | 7.54% |
| model:pii-shield-onnx | eligible | People's names | 230/571 | 40.28% | 88.97% | 37.65% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 58/690 | 8.41% | 100.00% | 8.12% |
| model:pplx | eligible | People's names | 289/571 | 50.61% | 88.44% | 40.98% |
| model:pplx | eligible | Phone numbers & email | 412/690 | 59.71% | 100.00% | 56.23% |
| model:ru-legal-ner | eligible | People's names | 253/571 | 44.31% | 90.02% | 40.81% |
| model:ru-legal-ner | eligible | Phone numbers & email | 47/690 | 6.81% | 97.54% | 6.81% |
| model:ru-pii-ner | eligible | People's names | 273/571 | 47.81% | 100.00% | 47.81% |
| model:ru-pii-ner | eligible | Phone numbers & email | 59/690 | 8.55% | 100.00% | 8.55% |
| model:rules-ru | eligible | People's names | 0/571 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 59/690 | 8.55% | 100.00% | 8.55% |
| model:spacy-alrosait | eligible | People's names | 231/571 | 40.46% | 84.41% | 40.46% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/690 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | People's names | 280/571 | 49.04% | 97.02% | 48.16% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 4/690 | 0.58% | 5.07% | 0.58% |
| model:stanza-ru | eligible | People's names | 269/571 | 47.11% | 94.75% | 47.11% |
| model:stanza-ru | eligible | Phone numbers & email | 0/690 | 0.00% | 15.07% | 0.00% |
| model:traciora | eligible | People's names | 269/571 | 47.11% | 92.99% | 43.43% |
| model:traciora | eligible | Phone numbers & email | 57/690 | 8.26% | 99.86% | 7.97% |
