# tonicai: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/tonicai.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Logins & usernames | 26/96 | 27.08% | 86.46% | 27.08% |
| composition:fastino | eligible | People's names | 1498/1530 | 97.91% | 98.04% | 97.84% |
| composition:fastino | eligible | Phone numbers & email | 363/365 | 99.45% | 100.00% | 99.45% |
| composition:fastino | eligible | Organizations | 341/426 | 80.05% | 84.74% | 79.81% |
| composition:pplx | eligible | Logins & usernames | 12/96 | 12.50% | 100.00% | 12.50% |
| composition:pplx | eligible | People's names | 1375/1530 | 89.87% | 89.87% | 87.19% |
| composition:pplx | eligible | Phone numbers & email | 365/365 | 100.00% | 100.00% | 98.36% |
| composition:pplx | eligible | Organizations | 73/426 | 17.14% | 18.54% | 16.43% |
| composition:pplx+fastino | eligible | Logins & usernames | 27/96 | 28.12% | 100.00% | 28.12% |
| composition:pplx+fastino | eligible | People's names | 1525/1530 | 99.67% | 99.67% | 99.54% |
| composition:pplx+fastino | eligible | Phone numbers & email | 365/365 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Organizations | 348/426 | 81.69% | 85.68% | 81.46% |
| composition:pplx+fastino+bardsai | eligible | Logins & usernames | 30/96 | 31.25% | 100.00% | 31.25% |
| composition:pplx+fastino+bardsai | eligible | People's names | 1525/1530 | 99.67% | 99.67% | 99.54% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 365/365 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 356/426 | 83.57% | 86.62% | 83.33% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Logins & usernames | 32/96 | 33.33% | 100.00% | 33.33% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 1526/1530 | 99.74% | 99.74% | 99.61% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 365/365 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 357/426 | 83.80% | 87.09% | 83.80% |
| composition:pplx+fastino+mmbert | eligible | Logins & usernames | 27/96 | 28.12% | 100.00% | 28.12% |
| composition:pplx+fastino+mmbert | eligible | People's names | 1526/1530 | 99.74% | 99.74% | 99.61% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 365/365 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 352/426 | 82.63% | 86.38% | 82.63% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Logins & usernames | 10/96 | 10.42% | 96.88% | 10.42% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 1383/1530 | 90.39% | 90.39% | 88.43% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 365/365 | 100.00% | 100.00% | 100.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 64/426 | 15.02% | 16.20% | 14.32% |
| model:apararti | eligible | Logins & usernames | 17/96 | 17.71% | 98.96% | 17.71% |
| model:apararti | eligible | People's names | 1034/1530 | 67.58% | 67.65% | 65.36% |
| model:apararti | eligible | Phone numbers & email | 365/365 | 100.00% | 100.00% | 99.45% |
| model:apararti | eligible | Organizations | 18/426 | 4.23% | 4.93% | 3.29% |
| model:bardsai-eu | eligible | Logins & usernames | 12/96 | 12.50% | 28.12% | 11.46% |
| model:bardsai-eu | eligible | People's names | 1114/1530 | 72.81% | 72.94% | 67.71% |
| model:bardsai-eu | eligible | Phone numbers & email | 5/365 | 1.37% | 99.45% | 0.27% |
| model:bardsai-eu | eligible | Organizations | 164/426 | 38.50% | 40.61% | 35.45% |
| model:davlan-mbert | eligible | Logins & usernames | 1/96 | 1.04% | 15.62% | 0.00% |
| model:davlan-mbert | eligible | People's names | 779/1530 | 50.92% | 50.98% | 49.67% |
| model:davlan-mbert | eligible | Phone numbers & email | 15/365 | 4.11% | 33.15% | 1.92% |
| model:davlan-mbert | eligible | Organizations | 159/426 | 37.32% | 38.50% | 34.74% |
| model:davlan-xlmr | eligible | Logins & usernames | 1/96 | 1.04% | 3.12% | 1.04% |
| model:davlan-xlmr | eligible | People's names | 1155/1530 | 75.49% | 75.49% | 72.22% |
| model:davlan-xlmr | eligible | Phone numbers & email | 1/365 | 0.27% | 27.40% | 0.27% |
| model:davlan-xlmr | eligible | Organizations | 190/426 | 44.60% | 46.01% | 42.72% |
| model:fef2-secret-ru | eligible | Logins & usernames | 3/96 | 3.12% | 4.17% | 0.00% |
| model:fef2-secret-ru | eligible | People's names | 29/1530 | 1.90% | 1.90% | 1.44% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 226/365 | 61.92% | 82.74% | 57.81% |
| model:fef2-secret-ru | eligible | Organizations | 6/426 | 1.41% | 2.11% | 1.41% |
| model:gliner-multi-v21 | eligible | Logins & usernames | 8/96 | 8.33% | 62.50% | 8.33% |
| model:gliner-multi-v21 | eligible | People's names | 1267/1530 | 82.81% | 82.94% | 82.81% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 1/365 | 0.27% | 88.77% | 0.27% |
| model:gliner-multi-v21 | eligible | Organizations | 323/426 | 75.82% | 77.93% | 75.82% |
| model:gliner-nvidia | eligible | Logins & usernames | 8/96 | 8.33% | 77.08% | 8.33% |
| model:gliner-nvidia | eligible | People's names | 1501/1530 | 98.10% | 98.10% | 98.04% |
| model:gliner-nvidia | eligible | Phone numbers & email | 346/365 | 94.79% | 100.00% | 94.79% |
| model:gliner-nvidia | eligible | Organizations | 290/426 | 68.08% | 71.83% | 68.08% |
| model:gliner-pii-base | eligible | Logins & usernames | 10/96 | 10.42% | 30.21% | 9.38% |
| model:gliner-pii-base | eligible | People's names | 494/1530 | 32.29% | 32.35% | 32.29% |
| model:gliner-pii-base | eligible | Phone numbers & email | 151/365 | 41.37% | 51.51% | 41.37% |
| model:gliner-pii-base | eligible | Organizations | 296/426 | 69.48% | 72.77% | 69.48% |
| model:gliner-pii-edge | eligible | Logins & usernames | 10/96 | 10.42% | 93.75% | 10.42% |
| model:gliner-pii-edge | eligible | People's names | 1381/1530 | 90.26% | 90.33% | 90.26% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 261/365 | 71.51% | 98.08% | 71.51% |
| model:gliner-pii-edge | eligible | Organizations | 293/426 | 68.78% | 73.00% | 68.54% |
| model:gliner-stream-pii | eligible | Logins & usernames | 9/96 | 9.38% | 88.54% | 9.38% |
| model:gliner-stream-pii | eligible | People's names | 1213/1530 | 79.28% | 79.35% | 79.28% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 78/365 | 21.37% | 92.05% | 21.37% |
| model:gliner-stream-pii | eligible | Organizations | 141/426 | 33.10% | 36.62% | 32.86% |
| model:gliner-urchade | eligible | Logins & usernames | 36/96 | 37.50% | 100.00% | 37.50% |
| model:gliner-urchade | eligible | People's names | 252/1530 | 16.47% | 16.47% | 16.47% |
| model:gliner-urchade | eligible | Phone numbers & email | 312/365 | 85.48% | 97.26% | 85.48% |
| model:gliner-urchade | eligible | Organizations | 312/426 | 73.24% | 74.41% | 73.24% |
| model:gliner2-fastino | eligible | Logins & usernames | 26/96 | 27.08% | 86.46% | 27.08% |
| model:gliner2-fastino | eligible | People's names | 1498/1530 | 97.91% | 98.04% | 97.84% |
| model:gliner2-fastino | eligible | Phone numbers & email | 363/365 | 99.45% | 100.00% | 99.45% |
| model:gliner2-fastino | eligible | Organizations | 341/426 | 80.05% | 84.74% | 79.81% |
| model:gliner2-hivetrace-omni | eligible | Logins & usernames | 11/96 | 11.46% | 77.08% | 11.46% |
| model:gliner2-hivetrace-omni | eligible | People's names | 1469/1530 | 96.01% | 96.21% | 96.01% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 362/365 | 99.18% | 99.73% | 99.18% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 317/426 | 74.41% | 78.87% | 74.41% |
| model:gliner2-hivetrace-uni | eligible | Logins & usernames | 5/96 | 5.21% | 20.83% | 5.21% |
| model:gliner2-hivetrace-uni | eligible | People's names | 1112/1530 | 72.68% | 72.75% | 72.68% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 361/365 | 98.90% | 100.00% | 98.90% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 152/426 | 35.68% | 38.50% | 35.68% |
| model:gliner2-large | eligible | Logins & usernames | 28/96 | 29.17% | 79.17% | 29.17% |
| model:gliner2-large | eligible | People's names | 1479/1530 | 96.67% | 96.80% | 96.60% |
| model:gliner2-large | eligible | Phone numbers & email | 361/365 | 98.90% | 99.73% | 98.90% |
| model:gliner2-large | eligible | Organizations | 347/426 | 81.46% | 84.51% | 81.22% |
| model:gliner2-vladlinv | eligible | Logins & usernames | 5/96 | 5.21% | 57.29% | 5.21% |
| model:gliner2-vladlinv | eligible | People's names | 1384/1530 | 90.46% | 90.52% | 90.46% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 360/365 | 98.63% | 98.63% | 98.63% |
| model:gliner2-vladlinv | eligible | Organizations | 46/426 | 10.80% | 11.03% | 10.80% |
| model:gliner25-fastino | eligible | Logins & usernames | 1/96 | 1.04% | 25.00% | 1.04% |
| model:gliner25-fastino | eligible | People's names | 1080/1530 | 70.59% | 70.65% | 70.52% |
| model:gliner25-fastino | eligible | Phone numbers & email | 364/365 | 99.73% | 100.00% | 99.73% |
| model:gliner25-fastino | eligible | Organizations | 306/426 | 71.83% | 74.65% | 71.60% |
| model:gravitee-small | eligible | Logins & usernames | 9/96 | 9.38% | 83.33% | 5.21% |
| model:gravitee-small | eligible | People's names | 1470/1530 | 96.08% | 96.08% | 95.62% |
| model:gravitee-small | eligible | Phone numbers & email | 365/365 | 100.00% | 100.00% | 99.45% |
| model:gravitee-small | eligible | Organizations | 144/426 | 33.80% | 39.67% | 28.87% |
| model:kalyan-ettin | eligible | Logins & usernames | 6/96 | 6.25% | 66.67% | 3.12% |
| model:kalyan-ettin | eligible | People's names | 1196/1530 | 78.17% | 78.24% | 65.75% |
| model:kalyan-ettin | eligible | Phone numbers & email | 362/365 | 99.18% | 100.00% | 93.70% |
| model:kalyan-ettin | eligible | Organizations | 104/426 | 24.41% | 31.22% | 12.91% |
| model:mmbert32k | eligible | Logins & usernames | 10/96 | 10.42% | 83.33% | 3.12% |
| model:mmbert32k | eligible | People's names | 1196/1530 | 78.17% | 78.30% | 77.39% |
| model:mmbert32k | eligible | Phone numbers & email | 191/365 | 52.33% | 99.73% | 41.64% |
| model:mmbert32k | eligible | Organizations | 104/426 | 24.41% | 33.57% | 18.31% |
| model:natasha | eligible | Logins & usernames | 6/96 | 6.25% | 50.00% | 0.00% |
| model:natasha | eligible | People's names | 228/1530 | 14.90% | 14.90% | 14.90% |
| model:natasha | eligible | Phone numbers & email | 0/365 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Organizations | 38/426 | 8.92% | 8.92% | 8.92% |
| model:ner-ru-gherman | eligible | Logins & usernames | 1/96 | 1.04% | 31.25% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 921/1530 | 60.20% | 60.26% | 59.28% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/365 | 0.00% | 61.10% | 0.00% |
| model:ner-ru-gherman | eligible | Organizations | 17/426 | 3.99% | 7.04% | 2.58% |
| model:ner-ru-yqelz | eligible | Logins & usernames | 1/96 | 1.04% | 2.08% | 0.00% |
| model:ner-ru-yqelz | eligible | People's names | 1057/1530 | 69.08% | 69.28% | 66.34% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 1/365 | 0.27% | 44.93% | 0.27% |
| model:ner-ru-yqelz | eligible | Organizations | 327/426 | 76.76% | 78.87% | 71.83% |
| model:nuner-zero | eligible | Logins & usernames | 15/96 | 15.62% | 100.00% | 15.62% |
| model:nuner-zero | eligible | People's names | 901/1530 | 58.89% | 58.95% | 58.89% |
| model:nuner-zero | eligible | Phone numbers & email | 357/365 | 97.81% | 100.00% | 97.53% |
| model:nuner-zero | eligible | Organizations | 358/426 | 84.04% | 85.68% | 65.73% |
| model:nym-base | eligible | Logins & usernames | 36/96 | 37.50% | 77.08% | 34.38% |
| model:nym-base | eligible | People's names | 846/1530 | 55.29% | 55.36% | 53.66% |
| model:nym-base | eligible | Phone numbers & email | 339/365 | 92.88% | 100.00% | 90.96% |
| model:nym-base | eligible | Organizations | 119/426 | 27.93% | 30.05% | 26.53% |
| model:nym-small | eligible | Logins & usernames | 34/96 | 35.42% | 88.54% | 34.38% |
| model:nym-small | eligible | People's names | 979/1530 | 63.99% | 63.99% | 63.40% |
| model:nym-small | eligible | Phone numbers & email | 359/365 | 98.36% | 99.73% | 98.36% |
| model:nym-small | eligible | Organizations | 127/426 | 29.81% | 32.16% | 27.70% |
| model:openai-base | eligible | Logins & usernames | 18/96 | 18.75% | 95.83% | 18.75% |
| model:openai-base | eligible | People's names | 1175/1530 | 76.80% | 76.80% | 76.14% |
| model:openai-base | eligible | Phone numbers & email | 365/365 | 100.00% | 100.00% | 100.00% |
| model:openai-base | eligible | Organizations | 22/426 | 5.16% | 5.63% | 4.93% |
| model:openmed-multilingual | eligible | Logins & usernames | 11/96 | 11.46% | 90.62% | 5.21% |
| model:openmed-multilingual | eligible | People's names | 1116/1530 | 72.94% | 72.94% | 68.50% |
| model:openmed-multilingual | eligible | Phone numbers & email | 343/365 | 93.97% | 100.00% | 92.05% |
| model:openmed-multilingual | eligible | Organizations | 63/426 | 14.79% | 20.42% | 12.44% |
| model:openmed-nemotron | eligible | Logins & usernames | 8/96 | 8.33% | 71.88% | 3.12% |
| model:openmed-nemotron | eligible | People's names | 1200/1530 | 78.43% | 78.50% | 73.59% |
| model:openmed-nemotron | eligible | Phone numbers & email | 355/365 | 97.26% | 100.00% | 95.89% |
| model:openmed-nemotron | eligible | Organizations | 64/426 | 15.02% | 19.01% | 10.09% |
| model:opf-kz-ru | eligible | Logins & usernames | 13/96 | 13.54% | 88.54% | 13.54% |
| model:opf-kz-ru | eligible | People's names | 901/1530 | 58.89% | 58.95% | 57.12% |
| model:opf-kz-ru | eligible | Phone numbers & email | 362/365 | 99.18% | 100.00% | 98.90% |
| model:opf-kz-ru | eligible | Organizations | 14/426 | 3.29% | 3.76% | 1.88% |
| model:opf-ru | eligible | Logins & usernames | 10/96 | 10.42% | 86.46% | 7.29% |
| model:opf-ru | eligible | People's names | 1043/1530 | 68.17% | 68.37% | 64.38% |
| model:opf-ru | eligible | Phone numbers & email | 356/365 | 97.53% | 100.00% | 97.53% |
| model:opf-ru | eligible | Organizations | 28/426 | 6.57% | 7.51% | 5.40% |
| model:opf-ru-v2 | eligible | Logins & usernames | 9/96 | 9.38% | 84.38% | 7.29% |
| model:opf-ru-v2 | eligible | People's names | 544/1530 | 35.56% | 35.62% | 34.51% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 361/365 | 98.90% | 100.00% | 98.90% |
| model:opf-ru-v2 | eligible | Organizations | 14/426 | 3.29% | 3.29% | 2.58% |
| model:pii-shield-onnx | eligible | Logins & usernames | 10/96 | 10.42% | 54.17% | 8.33% |
| model:pii-shield-onnx | eligible | People's names | 224/1530 | 14.64% | 14.71% | 10.20% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 361/365 | 98.90% | 99.73% | 97.81% |
| model:pii-shield-onnx | eligible | Organizations | 26/426 | 6.10% | 7.51% | 3.99% |
| model:pplx | eligible | Logins & usernames | 12/96 | 12.50% | 100.00% | 12.50% |
| model:pplx | eligible | People's names | 1375/1530 | 89.87% | 89.87% | 87.19% |
| model:pplx | eligible | Phone numbers & email | 365/365 | 100.00% | 100.00% | 98.36% |
| model:pplx | eligible | Organizations | 73/426 | 17.14% | 18.54% | 16.43% |
| model:ru-legal-ner | eligible | Logins & usernames | 5/96 | 5.21% | 56.25% | 0.00% |
| model:ru-legal-ner | eligible | People's names | 266/1530 | 17.39% | 17.45% | 11.31% |
| model:ru-legal-ner | eligible | Phone numbers & email | 272/365 | 74.52% | 99.73% | 63.29% |
| model:ru-legal-ner | eligible | Organizations | 65/426 | 15.26% | 19.95% | 7.04% |
| model:ru-pii-ner | eligible | Logins & usernames | 15/96 | 15.62% | 54.17% | 15.62% |
| model:ru-pii-ner | eligible | People's names | 818/1530 | 53.46% | 53.53% | 53.46% |
| model:ru-pii-ner | eligible | Phone numbers & email | 339/365 | 92.88% | 97.81% | 92.60% |
| model:ru-pii-ner | eligible | Organizations | 10/426 | 2.35% | 2.58% | 2.35% |
| model:rules-ru | eligible | Logins & usernames | 10/96 | 10.42% | 98.96% | 10.42% |
| model:rules-ru | eligible | People's names | 0/1530 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 362/365 | 99.18% | 99.73% | 99.18% |
| model:rules-ru | eligible | Organizations | 4/426 | 0.94% | 0.94% | 0.94% |
| model:spacy-alrosait | eligible | Logins & usernames | 0/96 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 1/1530 | 0.07% | 0.07% | 0.07% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/365 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Organizations | 0/426 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Logins & usernames | 0/96 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | People's names | 291/1530 | 19.02% | 19.02% | 19.02% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 7/365 | 1.92% | 1.92% | 1.92% |
| model:spacy-ru-lg | eligible | Organizations | 43/426 | 10.09% | 10.09% | 10.09% |
| model:stanza-ru | eligible | Logins & usernames | 17/96 | 17.71% | 27.08% | 17.71% |
| model:stanza-ru | eligible | People's names | 807/1530 | 52.75% | 52.81% | 52.75% |
| model:stanza-ru | eligible | Phone numbers & email | 91/365 | 24.93% | 24.93% | 24.93% |
| model:stanza-ru | eligible | Organizations | 163/426 | 38.26% | 38.26% | 38.26% |
| model:traciora | eligible | Logins & usernames | 14/96 | 14.58% | 88.54% | 12.50% |
| model:traciora | eligible | People's names | 785/1530 | 51.31% | 51.31% | 49.35% |
| model:traciora | eligible | Phone numbers & email | 364/365 | 99.73% | 100.00% | 99.73% |
| model:traciora | eligible | Organizations | 21/426 | 4.93% | 5.40% | 4.46% |
