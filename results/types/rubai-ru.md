# rubai-ru: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/rubai-ru.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Bank accounts & cards | 50/1054 | 4.74% | 75.52% | 4.74% |
| composition:fastino | eligible | Documents & identifiers | 39/268 | 14.55% | 93.66% | 14.55% |
| composition:fastino | eligible | People's names | 144/430 | 33.49% | 98.60% | 33.49% |
| composition:fastino | eligible | Phone numbers & email | 8/205 | 3.90% | 91.71% | 3.90% |
| composition:fastino | eligible | Addresses & locations | 11/1501 | 0.73% | 49.30% | 0.73% |
| composition:pplx | eligible | Bank accounts & cards | 72/1054 | 6.83% | 100.00% | 6.83% |
| composition:pplx | eligible | Documents & identifiers | 41/268 | 15.30% | 97.01% | 15.30% |
| composition:pplx | eligible | People's names | 145/430 | 33.72% | 98.84% | 33.49% |
| composition:pplx | eligible | Phone numbers & email | 15/205 | 7.32% | 99.51% | 7.32% |
| composition:pplx | eligible | Addresses & locations | 97/1501 | 6.46% | 99.87% | 6.46% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 72/1054 | 6.83% | 100.00% | 6.83% |
| composition:pplx+fastino | eligible | Documents & identifiers | 41/268 | 15.30% | 97.39% | 15.30% |
| composition:pplx+fastino | eligible | People's names | 147/430 | 34.19% | 99.53% | 34.19% |
| composition:pplx+fastino | eligible | Phone numbers & email | 15/205 | 7.32% | 99.51% | 7.32% |
| composition:pplx+fastino | eligible | Addresses & locations | 98/1501 | 6.53% | 99.87% | 6.53% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 168/1054 | 15.94% | 100.00% | 15.94% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 53/268 | 19.78% | 97.39% | 19.78% |
| composition:pplx+fastino+bardsai | eligible | People's names | 147/430 | 34.19% | 99.77% | 34.19% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 70/205 | 34.15% | 100.00% | 34.15% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 469/1501 | 31.25% | 100.00% | 31.25% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 168/1054 | 15.94% | 100.00% | 15.94% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 53/268 | 19.78% | 97.39% | 19.78% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 147/430 | 34.19% | 99.77% | 34.19% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 70/205 | 34.15% | 100.00% | 34.15% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 469/1501 | 31.25% | 100.00% | 31.25% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 72/1054 | 6.83% | 100.00% | 6.83% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 41/268 | 15.30% | 97.39% | 15.30% |
| composition:pplx+fastino+mmbert | eligible | People's names | 147/430 | 34.19% | 99.77% | 34.19% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 15/205 | 7.32% | 99.51% | 7.32% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 98/1501 | 6.53% | 100.00% | 6.53% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Bank accounts & cards | 64/1054 | 6.07% | 99.72% | 6.26% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 39/268 | 14.55% | 94.03% | 14.55% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 139/430 | 32.33% | 96.74% | 32.09% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 9/205 | 4.39% | 99.51% | 4.39% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 14/1501 | 0.93% | 99.67% | 0.93% |
| model:apararti | eligible | Bank accounts & cards | 57/1054 | 5.41% | 100.00% | 5.98% |
| model:apararti | eligible | Documents & identifiers | 38/268 | 14.18% | 93.66% | 13.43% |
| model:apararti | eligible | People's names | 60/430 | 13.95% | 64.88% | 10.47% |
| model:apararti | eligible | Phone numbers & email | 8/205 | 3.90% | 100.00% | 4.39% |
| model:apararti | eligible | Addresses & locations | 38/1501 | 2.53% | 99.53% | 2.40% |
| model:bardsai-eu | eligible | Bank accounts & cards | 104/1054 | 9.87% | 89.09% | 7.12% |
| model:bardsai-eu | eligible | Documents & identifiers | 48/268 | 17.91% | 88.81% | 14.55% |
| model:bardsai-eu | eligible | People's names | 138/430 | 32.09% | 97.21% | 32.09% |
| model:bardsai-eu | eligible | Phone numbers & email | 61/205 | 29.76% | 98.05% | 29.76% |
| model:bardsai-eu | eligible | Addresses & locations | 277/1501 | 18.45% | 98.80% | 18.25% |
| model:davlan-mbert | eligible | Bank accounts & cards | 0/1054 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 0/268 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | People's names | 139/430 | 32.33% | 98.84% | 29.77% |
| model:davlan-mbert | eligible | Phone numbers & email | 0/205 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Addresses & locations | 1/1501 | 0.07% | 98.67% | 0.07% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 0/1054 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 0/268 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 143/430 | 33.26% | 98.37% | 33.02% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/205 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 11/1501 | 0.73% | 99.00% | 0.73% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 26/1054 | 2.47% | 43.45% | 1.52% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 30/268 | 11.19% | 58.96% | 9.70% |
| model:fef2-secret-ru | eligible | People's names | 144/430 | 33.49% | 99.77% | 33.49% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 1/205 | 0.49% | 15.12% | 0.49% |
| model:fef2-secret-ru | eligible | Addresses & locations | 0/1501 | 0.00% | 96.74% | 0.00% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 45/1054 | 4.27% | 73.24% | 4.27% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 11/268 | 4.10% | 37.69% | 4.10% |
| model:gliner-multi-v21 | eligible | People's names | 144/430 | 33.49% | 97.44% | 33.49% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 8/205 | 3.90% | 97.07% | 3.90% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 1/1501 | 0.07% | 99.73% | 0.07% |
| model:gliner-multi-v21-ru | eligible | Bank accounts & cards | 38/1054 | 3.61% | 66.03% | 3.61% |
| model:gliner-multi-v21-ru | eligible | Documents & identifiers | 9/268 | 3.36% | 25.75% | 3.36% |
| model:gliner-multi-v21-ru | eligible | People's names | 139/430 | 32.33% | 95.81% | 32.33% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 8/205 | 3.90% | 96.59% | 3.90% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 1/1501 | 0.07% | 99.73% | 0.07% |
| model:gliner-nvidia | eligible | Bank accounts & cards | 52/1054 | 4.93% | 76.28% | 4.93% |
| model:gliner-nvidia | eligible | Documents & identifiers | 39/268 | 14.55% | 91.42% | 14.55% |
| model:gliner-nvidia | eligible | People's names | 133/430 | 30.93% | 94.88% | 30.93% |
| model:gliner-nvidia | eligible | Phone numbers & email | 9/205 | 4.39% | 96.10% | 4.39% |
| model:gliner-nvidia | eligible | Addresses & locations | 15/1501 | 1.00% | 74.95% | 1.00% |
| model:gliner-nvidia-ru | eligible | Bank accounts & cards | 32/1054 | 3.04% | 66.22% | 3.04% |
| model:gliner-nvidia-ru | eligible | Documents & identifiers | 34/268 | 12.69% | 81.72% | 12.69% |
| model:gliner-nvidia-ru | eligible | People's names | 122/430 | 28.37% | 93.49% | 21.63% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 9/205 | 4.39% | 95.12% | 4.39% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 12/1501 | 0.80% | 74.42% | 0.80% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 51/1054 | 4.84% | 75.43% | 4.84% |
| model:gliner-pii-base | eligible | Documents & identifiers | 28/268 | 10.45% | 77.24% | 10.45% |
| model:gliner-pii-base | eligible | People's names | 125/430 | 29.07% | 87.44% | 29.07% |
| model:gliner-pii-base | eligible | Phone numbers & email | 7/205 | 3.41% | 80.49% | 3.41% |
| model:gliner-pii-base | eligible | Addresses & locations | 1/1501 | 0.07% | 44.17% | 0.07% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 49/1054 | 4.65% | 74.95% | 4.65% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 38/268 | 14.18% | 93.28% | 14.18% |
| model:gliner-pii-edge | eligible | People's names | 119/430 | 27.67% | 86.05% | 27.67% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 7/205 | 3.41% | 81.95% | 3.41% |
| model:gliner-pii-edge | eligible | Addresses & locations | 6/1501 | 0.40% | 68.89% | 0.40% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 20/1054 | 1.90% | 97.15% | 1.90% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 32/268 | 11.94% | 72.39% | 11.94% |
| model:gliner-stream-pii | eligible | People's names | 92/430 | 21.40% | 66.74% | 21.40% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 1/205 | 0.49% | 73.17% | 0.49% |
| model:gliner-stream-pii | eligible | Addresses & locations | 0/1501 | 0.00% | 87.48% | 0.00% |
| model:gliner-urchade | eligible | Bank accounts & cards | 51/1054 | 4.84% | 73.34% | 4.84% |
| model:gliner-urchade | eligible | Documents & identifiers | 32/268 | 11.94% | 70.52% | 11.94% |
| model:gliner-urchade | eligible | People's names | 143/430 | 33.26% | 98.37% | 33.26% |
| model:gliner-urchade | eligible | Phone numbers & email | 9/205 | 4.39% | 99.51% | 4.39% |
| model:gliner-urchade | eligible | Addresses & locations | 13/1501 | 0.87% | 74.95% | 0.87% |
| model:gliner-urchade-ru | eligible | Bank accounts & cards | 51/1054 | 4.84% | 74.95% | 4.84% |
| model:gliner-urchade-ru | eligible | Documents & identifiers | 28/268 | 10.45% | 55.22% | 10.45% |
| model:gliner-urchade-ru | eligible | People's names | 5/430 | 1.16% | 16.98% | 1.16% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 9/205 | 4.39% | 99.02% | 4.39% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 14/1501 | 0.93% | 75.42% | 0.93% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 50/1054 | 4.74% | 75.52% | 4.74% |
| model:gliner2-fastino | eligible | Documents & identifiers | 39/268 | 14.55% | 93.66% | 14.55% |
| model:gliner2-fastino | eligible | People's names | 144/430 | 33.49% | 98.60% | 33.49% |
| model:gliner2-fastino | eligible | Phone numbers & email | 8/205 | 3.90% | 91.71% | 3.90% |
| model:gliner2-fastino | eligible | Addresses & locations | 11/1501 | 0.73% | 49.30% | 0.73% |
| model:gliner2-fastino-ru | eligible | Bank accounts & cards | 50/1054 | 4.74% | 75.33% | 4.74% |
| model:gliner2-fastino-ru | eligible | Documents & identifiers | 38/268 | 14.18% | 92.91% | 14.18% |
| model:gliner2-fastino-ru | eligible | People's names | 142/430 | 33.02% | 97.91% | 33.02% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 8/205 | 3.90% | 91.71% | 3.90% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 10/1501 | 0.67% | 47.90% | 0.67% |
| model:gliner2-hivetrace-omni | eligible | Bank accounts & cards | 50/1054 | 4.74% | 72.20% | 4.74% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 40/268 | 14.93% | 97.01% | 14.93% |
| model:gliner2-hivetrace-omni | eligible | People's names | 141/430 | 32.79% | 97.21% | 32.79% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 8/205 | 3.90% | 91.71% | 3.90% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 12/1501 | 0.80% | 63.42% | 0.80% |
| model:gliner2-hivetrace-omni-ru | eligible | Bank accounts & cards | 48/1054 | 4.55% | 64.90% | 4.55% |
| model:gliner2-hivetrace-omni-ru | eligible | Documents & identifiers | 40/268 | 14.93% | 95.52% | 14.93% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 142/430 | 33.02% | 97.44% | 33.02% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 8/205 | 3.90% | 91.71% | 3.90% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 12/1501 | 0.80% | 62.89% | 0.80% |
| model:gliner2-hivetrace-uni | eligible | Bank accounts & cards | 11/1054 | 1.04% | 11.20% | 1.04% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 33/268 | 12.31% | 66.04% | 12.31% |
| model:gliner2-hivetrace-uni | eligible | People's names | 115/430 | 26.74% | 87.21% | 26.74% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 6/205 | 2.93% | 75.12% | 2.93% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 1/1501 | 0.07% | 58.03% | 0.07% |
| model:gliner2-hivetrace-uni-ru | eligible | Bank accounts & cards | 1/1054 | 0.09% | 3.32% | 0.09% |
| model:gliner2-hivetrace-uni-ru | eligible | Documents & identifiers | 36/268 | 13.43% | 87.69% | 13.43% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 87/430 | 20.23% | 71.16% | 20.23% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 0/205 | 0.00% | 3.41% | 0.00% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 0/1501 | 0.00% | 35.04% | 0.00% |
| model:gliner2-large | eligible | Bank accounts & cards | 50/1054 | 4.74% | 76.66% | 4.74% |
| model:gliner2-large | eligible | Documents & identifiers | 40/268 | 14.93% | 94.03% | 14.93% |
| model:gliner2-large | eligible | People's names | 124/430 | 28.84% | 86.28% | 28.84% |
| model:gliner2-large | eligible | Phone numbers & email | 8/205 | 3.90% | 91.71% | 3.90% |
| model:gliner2-large | eligible | Addresses & locations | 1/1501 | 0.07% | 98.53% | 0.07% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 49/1054 | 4.65% | 69.64% | 4.65% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 29/268 | 10.82% | 67.91% | 10.82% |
| model:gliner2-vladlinv | eligible | People's names | 138/430 | 32.09% | 96.51% | 32.09% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 9/205 | 4.39% | 96.10% | 4.39% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 11/1501 | 0.73% | 82.94% | 0.73% |
| model:gliner2-vladlinv-ru | eligible | Bank accounts & cards | 46/1054 | 4.36% | 63.57% | 4.36% |
| model:gliner2-vladlinv-ru | eligible | Documents & identifiers | 28/268 | 10.45% | 51.12% | 10.45% |
| model:gliner2-vladlinv-ru | eligible | People's names | 137/430 | 31.86% | 96.51% | 31.86% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 7/205 | 3.41% | 92.68% | 3.41% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 11/1501 | 0.73% | 83.34% | 0.73% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 68/1054 | 6.45% | 98.77% | 6.45% |
| model:gliner25-fastino | eligible | Documents & identifiers | 38/268 | 14.18% | 82.46% | 14.18% |
| model:gliner25-fastino | eligible | People's names | 144/430 | 33.49% | 98.60% | 33.49% |
| model:gliner25-fastino | eligible | Phone numbers & email | 9/205 | 4.39% | 99.51% | 4.39% |
| model:gliner25-fastino | eligible | Addresses & locations | 15/1501 | 1.00% | 99.73% | 1.00% |
| model:gliner25-fastino-ru | eligible | Bank accounts & cards | 66/1054 | 6.26% | 97.91% | 6.26% |
| model:gliner25-fastino-ru | eligible | Documents & identifiers | 38/268 | 14.18% | 85.45% | 14.18% |
| model:gliner25-fastino-ru | eligible | People's names | 144/430 | 33.49% | 98.37% | 33.49% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 9/205 | 4.39% | 99.51% | 4.39% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 15/1501 | 1.00% | 99.60% | 1.00% |
| model:gravitee-small | eligible | Bank accounts & cards | 23/1054 | 2.18% | 53.61% | 1.42% |
| model:gravitee-small | eligible | Documents & identifiers | 4/268 | 1.49% | 6.34% | 1.12% |
| model:gravitee-small | eligible | People's names | 30/430 | 6.98% | 30.93% | 4.42% |
| model:gravitee-small | eligible | Phone numbers & email | 6/205 | 2.93% | 75.12% | 2.93% |
| model:gravitee-small | eligible | Addresses & locations | 61/1501 | 4.06% | 83.94% | 3.33% |
| model:kalyan-ettin | eligible | Bank accounts & cards | 31/1054 | 2.94% | 58.06% | 2.37% |
| model:kalyan-ettin | eligible | Documents & identifiers | 3/268 | 1.12% | 21.64% | 0.75% |
| model:kalyan-ettin | eligible | People's names | 58/430 | 13.49% | 87.91% | 8.14% |
| model:kalyan-ettin | eligible | Phone numbers & email | 1/205 | 0.49% | 38.05% | 0.49% |
| model:kalyan-ettin | eligible | Addresses & locations | 0/1501 | 0.00% | 75.02% | 0.00% |
| model:mmbert32k | eligible | Bank accounts & cards | 31/1054 | 2.94% | 99.81% | 2.66% |
| model:mmbert32k | eligible | Documents & identifiers | 36/268 | 13.43% | 85.82% | 1.49% |
| model:mmbert32k | eligible | People's names | 121/430 | 28.14% | 97.21% | 12.79% |
| model:mmbert32k | eligible | Phone numbers & email | 8/205 | 3.90% | 99.51% | 4.39% |
| model:mmbert32k | eligible | Addresses & locations | 0/1501 | 0.00% | 99.80% | 0.00% |
| model:natasha | eligible | Bank accounts & cards | 0/1054 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 11/268 | 4.10% | 12.69% | 2.24% |
| model:natasha | eligible | People's names | 139/430 | 32.33% | 98.60% | 32.33% |
| model:natasha | eligible | Phone numbers & email | 0/205 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Addresses & locations | 0/1501 | 0.00% | 93.20% | 0.00% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 0/1054 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/268 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 61/430 | 14.19% | 96.05% | 13.02% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/205 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 0/1501 | 0.00% | 99.93% | 0.00% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 0/1054 | 0.00% | 2.85% | 0.00% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 6/268 | 2.24% | 8.21% | 1.12% |
| model:ner-ru-yqelz | eligible | People's names | 143/430 | 33.26% | 97.44% | 32.56% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 0/205 | 0.00% | 3.41% | 0.00% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 7/1501 | 0.47% | 97.80% | 0.47% |
| model:nuner-zero | eligible | Bank accounts & cards | 63/1054 | 5.98% | 87.29% | 1.90% |
| model:nuner-zero | eligible | Documents & identifiers | 41/268 | 15.30% | 95.15% | 15.30% |
| model:nuner-zero | eligible | People's names | 142/430 | 33.02% | 98.14% | 16.28% |
| model:nuner-zero | eligible | Phone numbers & email | 9/205 | 4.39% | 98.54% | 0.00% |
| model:nuner-zero | eligible | Addresses & locations | 6/1501 | 0.40% | 99.87% | 0.00% |
| model:nym-base | eligible | Bank accounts & cards | 70/1054 | 6.64% | 99.91% | 6.64% |
| model:nym-base | eligible | Documents & identifiers | 39/268 | 14.55% | 92.91% | 13.43% |
| model:nym-base | eligible | People's names | 63/430 | 14.65% | 96.05% | 30.23% |
| model:nym-base | eligible | Phone numbers & email | 9/205 | 4.39% | 99.51% | 4.39% |
| model:nym-base | eligible | Addresses & locations | 2/1501 | 0.13% | 98.80% | 0.07% |
| model:nym-small | eligible | Bank accounts & cards | 67/1054 | 6.36% | 99.91% | 6.36% |
| model:nym-small | eligible | Documents & identifiers | 38/268 | 14.18% | 93.28% | 14.18% |
| model:nym-small | eligible | People's names | 59/430 | 13.72% | 94.88% | 28.37% |
| model:nym-small | eligible | Phone numbers & email | 9/205 | 4.39% | 100.00% | 4.39% |
| model:nym-small | eligible | Addresses & locations | 0/1501 | 0.00% | 98.73% | 0.00% |
| model:openai-base | eligible | Bank accounts & cards | 70/1054 | 6.64% | 98.20% | 7.12% |
| model:openai-base | eligible | Documents & identifiers | 42/268 | 15.67% | 94.40% | 15.67% |
| model:openai-base | eligible | People's names | 71/430 | 16.51% | 61.16% | 15.35% |
| model:openai-base | eligible | Phone numbers & email | 8/205 | 3.90% | 99.02% | 4.88% |
| model:openai-base | eligible | Addresses & locations | 714/1501 | 47.57% | 97.80% | 47.24% |
| model:openmed-multilingual | eligible | Bank accounts & cards | 47/1054 | 4.46% | 100.00% | 4.93% |
| model:openmed-multilingual | eligible | Documents & identifiers | 37/268 | 13.81% | 90.30% | 11.94% |
| model:openmed-multilingual | eligible | People's names | 46/430 | 10.70% | 71.40% | 8.37% |
| model:openmed-multilingual | eligible | Phone numbers & email | 7/205 | 3.41% | 99.51% | 3.41% |
| model:openmed-multilingual | eligible | Addresses & locations | 0/1501 | 0.00% | 93.27% | 0.00% |
| model:openmed-nemotron | eligible | Bank accounts & cards | 35/1054 | 3.32% | 81.88% | 2.18% |
| model:openmed-nemotron | eligible | Documents & identifiers | 3/268 | 1.12% | 15.30% | 0.37% |
| model:openmed-nemotron | eligible | People's names | 56/430 | 13.02% | 82.33% | 13.26% |
| model:openmed-nemotron | eligible | Phone numbers & email | 5/205 | 2.44% | 90.73% | 2.44% |
| model:openmed-nemotron | eligible | Addresses & locations | 1/1501 | 0.07% | 98.40% | 0.07% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 53/1054 | 5.03% | 100.00% | 5.12% |
| model:opf-kz-ru | eligible | Documents & identifiers | 37/268 | 13.81% | 93.28% | 13.43% |
| model:opf-kz-ru | eligible | People's names | 38/430 | 8.84% | 53.72% | 6.28% |
| model:opf-kz-ru | eligible | Phone numbers & email | 8/205 | 3.90% | 100.00% | 3.90% |
| model:opf-kz-ru | eligible | Addresses & locations | 10/1501 | 0.67% | 98.33% | 0.67% |
| model:opf-ru | eligible | Bank accounts & cards | 34/1054 | 3.23% | 96.96% | 2.56% |
| model:opf-ru | eligible | Documents & identifiers | 38/268 | 14.18% | 93.28% | 8.96% |
| model:opf-ru | eligible | People's names | 116/430 | 26.98% | 94.65% | 23.49% |
| model:opf-ru | eligible | Phone numbers & email | 7/205 | 3.41% | 100.00% | 2.93% |
| model:opf-ru | eligible | Addresses & locations | 0/1501 | 0.00% | 99.33% | 0.00% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 57/1054 | 5.41% | 99.72% | 5.50% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 36/268 | 13.43% | 91.42% | 8.58% |
| model:opf-ru-v2 | eligible | People's names | 69/430 | 16.05% | 68.14% | 12.56% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 6/205 | 2.93% | 99.51% | 3.41% |
| model:opf-ru-v2 | eligible | Addresses & locations | 20/1501 | 1.33% | 98.33% | 1.27% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 68/1054 | 6.45% | 96.02% | 6.26% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 24/268 | 8.96% | 50.00% | 4.48% |
| model:pii-shield-onnx | eligible | People's names | 81/430 | 18.84% | 82.79% | 14.42% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 3/205 | 1.46% | 78.05% | 0.98% |
| model:pii-shield-onnx | eligible | Addresses & locations | 1/1501 | 0.07% | 92.67% | 0.07% |
| model:pplx | eligible | Bank accounts & cards | 72/1054 | 6.83% | 100.00% | 6.83% |
| model:pplx | eligible | Documents & identifiers | 41/268 | 15.30% | 97.01% | 15.30% |
| model:pplx | eligible | People's names | 145/430 | 33.72% | 98.84% | 33.49% |
| model:pplx | eligible | Phone numbers & email | 15/205 | 7.32% | 99.51% | 7.32% |
| model:pplx | eligible | Addresses & locations | 97/1501 | 6.46% | 99.87% | 6.46% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 35/1054 | 3.32% | 84.63% | 1.71% |
| model:ru-legal-ner | eligible | Documents & identifiers | 32/268 | 11.94% | 69.40% | 8.58% |
| model:ru-legal-ner | eligible | People's names | 155/430 | 36.05% | 98.37% | 34.42% |
| model:ru-legal-ner | eligible | Phone numbers & email | 8/205 | 3.90% | 94.63% | 3.90% |
| model:ru-legal-ner | eligible | Addresses & locations | 3/1501 | 0.20% | 94.34% | 0.20% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 70/1054 | 6.64% | 99.91% | 6.45% |
| model:ru-pii-ner | eligible | Documents & identifiers | 40/268 | 14.93% | 96.27% | 14.93% |
| model:ru-pii-ner | eligible | People's names | 141/430 | 32.79% | 97.67% | 32.79% |
| model:ru-pii-ner | eligible | Phone numbers & email | 9/205 | 4.39% | 99.02% | 4.39% |
| model:ru-pii-ner | eligible | Addresses & locations | 17/1501 | 1.13% | 89.74% | 1.13% |
| model:rules-ru | eligible | Bank accounts & cards | 6/1054 | 0.57% | 9.49% | 0.57% |
| model:rules-ru | eligible | Documents & identifiers | 0/268 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | People's names | 0/430 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 0/205 | 0.00% | 9.27% | 0.00% |
| model:rules-ru | eligible | Addresses & locations | 0/1501 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 1/1054 | 0.09% | 5.41% | 0.09% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/268 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 80/430 | 18.60% | 75.81% | 18.60% |
| model:spacy-alrosait | eligible | Phone numbers & email | 1/205 | 0.49% | 10.73% | 0.49% |
| model:spacy-alrosait | eligible | Addresses & locations | 10/1501 | 0.67% | 89.21% | 0.67% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 0/1054 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 1/268 | 0.37% | 0.37% | 0.37% |
| model:spacy-ru-lg | eligible | People's names | 139/430 | 32.33% | 97.44% | 32.33% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 0/205 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Addresses & locations | 0/1501 | 0.00% | 92.67% | 0.00% |
| model:stanza-ru | eligible | Bank accounts & cards | 3/1054 | 0.28% | 0.47% | 0.28% |
| model:stanza-ru | eligible | Documents & identifiers | 39/268 | 14.55% | 89.55% | 14.55% |
| model:stanza-ru | eligible | People's names | 146/430 | 33.95% | 99.77% | 33.95% |
| model:stanza-ru | eligible | Phone numbers & email | 0/205 | 0.00% | 0.49% | 0.00% |
| model:stanza-ru | eligible | Addresses & locations | 0/1501 | 0.00% | 98.27% | 0.00% |
| model:traciora | eligible | Bank accounts & cards | 47/1054 | 4.46% | 100.00% | 4.46% |
| model:traciora | eligible | Documents & identifiers | 29/268 | 10.82% | 84.33% | 2.99% |
| model:traciora | eligible | People's names | 80/430 | 18.60% | 78.60% | 13.95% |
| model:traciora | eligible | Phone numbers & email | 6/205 | 2.93% | 98.54% | 3.90% |
| model:traciora | eligible | Addresses & locations | 84/1501 | 5.60% | 99.67% | 5.60% |
