# alrosait: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/alrosait.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | People's names | 974/987 | 98.68% | 99.70% | 98.48% |
| composition:fastino | eligible | Addresses & locations | 487/875 | 55.66% | 74.29% | 55.43% |
| composition:pplx | eligible | People's names | 980/987 | 99.29% | 99.49% | 97.16% |
| composition:pplx | eligible | Addresses & locations | 820/875 | 93.71% | 99.43% | 90.63% |
| composition:pplx+fastino | eligible | People's names | 986/987 | 99.90% | 99.90% | 99.80% |
| composition:pplx+fastino | eligible | Addresses & locations | 838/875 | 95.77% | 99.89% | 94.74% |
| composition:pplx+fastino+bardsai | eligible | People's names | 987/987 | 100.00% | 100.00% | 99.90% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 842/875 | 96.23% | 99.89% | 96.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 987/987 | 100.00% | 100.00% | 99.90% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 842/875 | 96.23% | 99.89% | 96.34% |
| composition:pplx+fastino+mmbert | eligible | People's names | 987/987 | 100.00% | 100.00% | 99.80% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 838/875 | 95.77% | 99.89% | 94.97% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 925/987 | 93.72% | 99.29% | 90.58% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 733/875 | 83.77% | 98.86% | 82.86% |
| model:apararti | eligible | People's names | 750/987 | 75.99% | 88.15% | 67.27% |
| model:apararti | eligible | Addresses & locations | 519/875 | 59.31% | 91.31% | 57.03% |
| model:bardsai-eu | eligible | People's names | 942/987 | 95.44% | 97.97% | 88.96% |
| model:bardsai-eu | eligible | Addresses & locations | 286/875 | 32.69% | 96.11% | 30.63% |
| model:betterleaks | eligible | People's names | 0/987 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Addresses & locations | 0/875 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | People's names | 926/987 | 93.82% | 97.57% | 77.30% |
| model:davlan-mbert | eligible | Addresses & locations | 54/875 | 6.17% | 95.09% | 6.06% |
| model:davlan-xlmr | eligible | People's names | 953/987 | 96.56% | 98.07% | 88.45% |
| model:davlan-xlmr | eligible | Addresses & locations | 92/875 | 10.51% | 98.17% | 9.94% |
| model:fef2-secret-ru | eligible | People's names | 945/987 | 95.74% | 98.78% | 86.02% |
| model:fef2-secret-ru | eligible | Addresses & locations | 86/875 | 9.83% | 94.06% | 9.49% |
| model:gitleaks | eligible | People's names | 0/987 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Addresses & locations | 0/875 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21 | eligible | People's names | 983/987 | 99.59% | 99.90% | 99.59% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 351/875 | 40.11% | 99.09% | 31.43% |
| model:gliner-multi-v21-ru | eligible | People's names | 972/987 | 98.48% | 98.89% | 98.48% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 348/875 | 39.77% | 99.54% | 31.09% |
| model:gliner-nvidia | eligible | People's names | 764/987 | 77.41% | 92.00% | 74.87% |
| model:gliner-nvidia | eligible | Addresses & locations | 584/875 | 66.74% | 79.09% | 66.63% |
| model:gliner-nvidia-ru | eligible | People's names | 569/987 | 57.65% | 86.12% | 40.73% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 559/875 | 63.89% | 79.43% | 63.89% |
| model:gliner-pii-base | eligible | People's names | 789/987 | 79.94% | 88.15% | 79.94% |
| model:gliner-pii-base | eligible | Addresses & locations | 162/875 | 18.51% | 39.77% | 18.51% |
| model:gliner-pii-edge | eligible | People's names | 753/987 | 76.29% | 89.67% | 74.97% |
| model:gliner-pii-edge | eligible | Addresses & locations | 185/875 | 21.14% | 53.60% | 21.14% |
| model:gliner-stream-pii | eligible | People's names | 622/987 | 63.02% | 82.27% | 58.46% |
| model:gliner-stream-pii | eligible | Addresses & locations | 218/875 | 24.91% | 71.89% | 24.80% |
| model:gliner-urchade | eligible | People's names | 984/987 | 99.70% | 99.90% | 99.70% |
| model:gliner-urchade | eligible | Addresses & locations | 697/875 | 79.66% | 84.00% | 79.66% |
| model:gliner-urchade-ru | eligible | People's names | 165/987 | 16.72% | 16.72% | 16.72% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 705/875 | 80.57% | 82.63% | 80.57% |
| model:gliner2-fastino | eligible | People's names | 974/987 | 98.68% | 99.70% | 98.48% |
| model:gliner2-fastino | eligible | Addresses & locations | 487/875 | 55.66% | 74.29% | 55.43% |
| model:gliner2-fastino-ru | eligible | People's names | 959/987 | 97.16% | 99.09% | 96.96% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 498/875 | 56.91% | 72.69% | 56.80% |
| model:gliner2-hivetrace-omni | eligible | People's names | 980/987 | 99.29% | 99.90% | 99.29% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 487/875 | 55.66% | 77.49% | 55.66% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 977/987 | 98.99% | 99.90% | 98.99% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 491/875 | 56.11% | 77.83% | 56.11% |
| model:gliner2-hivetrace-uni | eligible | People's names | 778/987 | 78.82% | 86.12% | 78.82% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 254/875 | 29.03% | 58.29% | 28.91% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 484/987 | 49.04% | 51.77% | 49.04% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 43/875 | 4.91% | 10.63% | 4.91% |
| model:gliner2-large | eligible | People's names | 659/987 | 66.77% | 82.07% | 66.57% |
| model:gliner2-large | eligible | Addresses & locations | 294/875 | 33.60% | 94.51% | 31.20% |
| model:gliner2-vladlinv | eligible | People's names | 965/987 | 97.77% | 99.29% | 97.06% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 724/875 | 82.74% | 94.74% | 80.23% |
| model:gliner2-vladlinv-ru | eligible | People's names | 962/987 | 97.47% | 99.19% | 96.66% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 723/875 | 82.63% | 94.40% | 80.11% |
| model:gliner25-fastino | eligible | People's names | 963/987 | 97.57% | 99.39% | 97.06% |
| model:gliner25-fastino | eligible | Addresses & locations | 658/875 | 75.20% | 99.77% | 74.86% |
| model:gliner25-fastino-ru | eligible | People's names | 941/987 | 95.34% | 98.58% | 95.04% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 672/875 | 76.80% | 99.54% | 76.57% |
| model:gravitee-small | eligible | People's names | 324/987 | 32.83% | 43.36% | 22.49% |
| model:gravitee-small | eligible | Addresses & locations | 531/875 | 60.69% | 91.77% | 54.74% |
| model:kalyan-ettin | eligible | People's names | 337/987 | 34.14% | 89.87% | 13.88% |
| model:kalyan-ettin | eligible | Addresses & locations | 34/875 | 3.89% | 57.83% | 2.06% |
| model:mmbert32k | eligible | People's names | 708/987 | 71.73% | 97.47% | 36.58% |
| model:mmbert32k | eligible | Addresses & locations | 111/875 | 12.69% | 99.09% | 0.91% |
| model:natasha | eligible | People's names | 914/987 | 92.60% | 95.85% | 86.93% |
| model:natasha | eligible | Addresses & locations | 18/875 | 2.06% | 60.23% | 1.94% |
| model:ner-ru-gherman | eligible | People's names | 32/987 | 3.24% | 97.57% | 2.63% |
| model:ner-ru-gherman | eligible | Addresses & locations | 1/875 | 0.11% | 94.63% | 0.00% |
| model:ner-ru-yqelz | eligible | People's names | 958/987 | 97.06% | 98.68% | 93.52% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 66/875 | 7.54% | 99.20% | 7.20% |
| model:nuner-zero | eligible | People's names | 973/987 | 98.58% | 99.09% | 7.40% |
| model:nuner-zero | eligible | Addresses & locations | 478/875 | 54.63% | 99.66% | 0.00% |
| model:nym-base | eligible | People's names | 90/987 | 9.12% | 98.89% | 94.83% |
| model:nym-base | eligible | Addresses & locations | 249/875 | 28.46% | 99.89% | 30.63% |
| model:nym-small | eligible | People's names | 99/987 | 10.03% | 97.47% | 91.29% |
| model:nym-small | eligible | Addresses & locations | 233/875 | 26.63% | 99.66% | 28.46% |
| model:openai-base | eligible | People's names | 764/987 | 77.41% | 83.89% | 74.06% |
| model:openai-base | eligible | Addresses & locations | 611/875 | 69.83% | 90.86% | 70.40% |
| model:openmed-multilingual | eligible | People's names | 125/987 | 12.66% | 68.29% | 20.97% |
| model:openmed-multilingual | eligible | Addresses & locations | 38/875 | 4.34% | 94.29% | 2.63% |
| model:openmed-nemotron | eligible | People's names | 235/987 | 23.81% | 89.67% | 38.91% |
| model:openmed-nemotron | eligible | Addresses & locations | 76/875 | 8.69% | 89.60% | 8.00% |
| model:opf-kz-ru | eligible | People's names | 655/987 | 66.36% | 79.84% | 54.61% |
| model:opf-kz-ru | eligible | Addresses & locations | 165/875 | 18.86% | 90.74% | 17.60% |
| model:opf-ru | eligible | People's names | 739/987 | 74.87% | 98.28% | 65.75% |
| model:opf-ru | eligible | Addresses & locations | 110/875 | 12.57% | 99.43% | 0.23% |
| model:opf-ru-v2 | eligible | People's names | 747/987 | 75.68% | 87.84% | 67.38% |
| model:opf-ru-v2 | eligible | Addresses & locations | 539/875 | 61.60% | 90.51% | 61.14% |
| model:pii-shield-onnx | eligible | People's names | 766/987 | 77.61% | 92.71% | 71.73% |
| model:pii-shield-onnx | eligible | Addresses & locations | 216/875 | 24.69% | 81.60% | 22.74% |
| model:pplx | eligible | People's names | 980/987 | 99.29% | 99.49% | 97.16% |
| model:pplx | eligible | Addresses & locations | 820/875 | 93.71% | 99.43% | 90.63% |
| model:ru-legal-ner | eligible | People's names | 957/987 | 96.96% | 98.78% | 92.30% |
| model:ru-legal-ner | eligible | Addresses & locations | 392/875 | 44.80% | 93.49% | 40.34% |
| model:ru-pii-ner | eligible | People's names | 976/987 | 98.89% | 99.39% | 98.78% |
| model:ru-pii-ner | eligible | Addresses & locations | 778/875 | 88.91% | 92.11% | 88.91% |
| model:rules-ru | eligible | People's names | 0/987 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Addresses & locations | 0/875 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | train | People's names | 985/987 | 99.80% | 99.90% | 99.80% |
| model:spacy-alrosait | train | Addresses & locations | 874/875 | 99.89% | 100.00% | 99.89% |
| model:spacy-ru-lg | eligible | People's names | 889/987 | 90.07% | 98.07% | 76.80% |
| model:spacy-ru-lg | eligible | Addresses & locations | 6/875 | 0.69% | 71.66% | 0.69% |
| model:stanza-ru | eligible | People's names | 963/987 | 97.57% | 97.87% | 94.12% |
| model:stanza-ru | eligible | Addresses & locations | 58/875 | 6.63% | 93.49% | 6.63% |
| model:traciora | eligible | People's names | 787/987 | 79.74% | 92.60% | 72.85% |
| model:traciora | eligible | Addresses & locations | 643/875 | 73.49% | 91.89% | 72.23% |
