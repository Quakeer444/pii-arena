# dialogpii-multi: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/dialogpii-multi.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Documents & identifiers | 393/818 | 48.04% | 62.35% | 48.04% |
| composition:fastino | eligible | People's names | 4071/5083 | 80.09% | 82.94% | 80.01% |
| composition:fastino | eligible | Phone numbers & email | 429/750 | 57.20% | 75.87% | 57.07% |
| composition:fastino | eligible | Addresses & locations | 1401/1868 | 75.00% | 79.44% | 74.95% |
| composition:fastino | eligible | Organizations | 1120/1806 | 62.02% | 69.82% | 61.85% |
| composition:fastino | eligible | Network identifiers | 3/20 | 15.00% | 95.00% | 15.00% |
| composition:pplx | eligible | Documents & identifiers | 529/818 | 64.67% | 76.04% | 64.43% |
| composition:pplx | eligible | People's names | 4523/5083 | 88.98% | 93.98% | 88.67% |
| composition:pplx | eligible | Phone numbers & email | 478/750 | 63.73% | 76.80% | 62.40% |
| composition:pplx | eligible | Addresses & locations | 1067/1868 | 57.12% | 59.26% | 56.42% |
| composition:pplx | eligible | Organizations | 139/1806 | 7.70% | 13.01% | 7.70% |
| composition:pplx | eligible | Network identifiers | 4/20 | 20.00% | 55.00% | 20.00% |
| composition:pplx+fastino | eligible | Documents & identifiers | 545/818 | 66.63% | 81.17% | 66.38% |
| composition:pplx+fastino | eligible | People's names | 4777/5083 | 93.98% | 96.81% | 93.74% |
| composition:pplx+fastino | eligible | Phone numbers & email | 533/750 | 71.07% | 84.93% | 69.73% |
| composition:pplx+fastino | eligible | Addresses & locations | 1568/1868 | 83.94% | 86.30% | 83.40% |
| composition:pplx+fastino | eligible | Organizations | 1163/1806 | 64.40% | 72.65% | 64.23% |
| composition:pplx+fastino | eligible | Network identifiers | 6/20 | 30.00% | 95.00% | 30.00% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 557/818 | 68.09% | 81.91% | 67.85% |
| composition:pplx+fastino+bardsai | eligible | People's names | 4787/5083 | 94.18% | 97.03% | 93.98% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 537/750 | 71.60% | 85.73% | 70.40% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 1656/1868 | 88.65% | 91.38% | 87.63% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 1322/1806 | 73.20% | 81.84% | 72.43% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 6/20 | 30.00% | 100.00% | 30.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 559/818 | 68.34% | 84.96% | 67.97% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 4819/5083 | 94.81% | 97.66% | 94.71% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 539/750 | 71.87% | 87.20% | 70.67% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 1682/1868 | 90.04% | 93.68% | 87.96% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 1366/1806 | 75.64% | 87.21% | 73.53% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 6/20 | 30.00% | 100.00% | 30.00% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 550/818 | 67.24% | 84.35% | 66.63% |
| composition:pplx+fastino+mmbert | eligible | People's names | 4815/5083 | 94.73% | 97.56% | 94.26% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 535/750 | 71.33% | 86.80% | 70.00% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 1619/1868 | 86.67% | 91.76% | 84.58% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 1230/1806 | 68.11% | 81.17% | 65.89% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 6/20 | 30.00% | 100.00% | 30.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 376/818 | 45.97% | 61.61% | 44.62% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 3692/5083 | 72.63% | 79.30% | 71.87% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 358/750 | 47.73% | 69.07% | 47.33% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 897/1868 | 48.02% | 51.82% | 47.06% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 158/1806 | 8.75% | 15.50% | 7.64% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 2/20 | 10.00% | 40.00% | 10.00% |
| model:apararti | eligible | Documents & identifiers | 376/818 | 45.97% | 67.73% | 43.64% |
| model:apararti | eligible | People's names | 1776/5083 | 34.94% | 38.93% | 30.61% |
| model:apararti | eligible | Phone numbers & email | 323/750 | 43.07% | 62.27% | 41.33% |
| model:apararti | eligible | Addresses & locations | 562/1868 | 30.09% | 35.65% | 26.23% |
| model:apararti | eligible | Organizations | 149/1806 | 8.25% | 15.73% | 5.87% |
| model:apararti | eligible | Network identifiers | 1/20 | 5.00% | 25.00% | 5.00% |
| model:bardsai-eu | eligible | Documents & identifiers | 352/818 | 43.03% | 57.58% | 37.16% |
| model:bardsai-eu | eligible | People's names | 4019/5083 | 79.07% | 88.08% | 75.03% |
| model:bardsai-eu | eligible | Phone numbers & email | 173/750 | 23.07% | 65.07% | 18.13% |
| model:bardsai-eu | eligible | Addresses & locations | 1361/1868 | 72.86% | 78.80% | 68.36% |
| model:bardsai-eu | eligible | Organizations | 791/1806 | 43.80% | 58.03% | 40.86% |
| model:bardsai-eu | eligible | Network identifiers | 1/20 | 5.00% | 80.00% | 5.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 2/818 | 0.24% | 5.01% | 0.12% |
| model:davlan-mbert | eligible | People's names | 3751/5083 | 73.80% | 83.30% | 70.82% |
| model:davlan-mbert | eligible | Phone numbers & email | 10/750 | 1.33% | 12.80% | 0.53% |
| model:davlan-mbert | eligible | Addresses & locations | 1163/1868 | 62.26% | 67.61% | 59.96% |
| model:davlan-mbert | eligible | Organizations | 763/1806 | 42.25% | 57.81% | 38.48% |
| model:davlan-mbert | eligible | Network identifiers | 0/20 | 0.00% | 25.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 1/818 | 0.12% | 2.93% | 0.12% |
| model:davlan-xlmr | eligible | People's names | 4198/5083 | 82.59% | 92.62% | 79.82% |
| model:davlan-xlmr | eligible | Phone numbers & email | 16/750 | 2.13% | 10.40% | 2.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 1218/1868 | 65.20% | 70.61% | 60.92% |
| model:davlan-xlmr | eligible | Organizations | 838/1806 | 46.40% | 58.14% | 41.81% |
| model:davlan-xlmr | eligible | Network identifiers | 1/20 | 5.00% | 15.00% | 5.00% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 1/818 | 0.12% | 0.49% | 0.12% |
| model:fef2-secret-ru | eligible | People's names | 68/5083 | 1.34% | 1.48% | 0.89% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 1/750 | 0.13% | 0.27% | 0.13% |
| model:fef2-secret-ru | eligible | Addresses & locations | 6/1868 | 0.32% | 0.96% | 0.11% |
| model:fef2-secret-ru | eligible | Organizations | 2/1806 | 0.11% | 0.17% | 0.06% |
| model:fef2-secret-ru | eligible | Network identifiers | 0/20 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 260/818 | 31.78% | 41.32% | 31.78% |
| model:gliner-multi-v21 | eligible | People's names | 4008/5083 | 78.85% | 80.96% | 78.81% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 176/750 | 23.47% | 53.73% | 23.33% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 1216/1868 | 65.10% | 68.04% | 64.99% |
| model:gliner-multi-v21 | eligible | Organizations | 967/1806 | 53.54% | 61.85% | 53.49% |
| model:gliner-multi-v21 | eligible | Network identifiers | 0/20 | 0.00% | 35.00% | 0.00% |
| model:gliner-nvidia | eligible | Documents & identifiers | 347/818 | 42.42% | 50.73% | 42.42% |
| model:gliner-nvidia | eligible | People's names | 3267/5083 | 64.27% | 76.18% | 62.92% |
| model:gliner-nvidia | eligible | Phone numbers & email | 351/750 | 46.80% | 64.13% | 46.80% |
| model:gliner-nvidia | eligible | Addresses & locations | 1225/1868 | 65.58% | 69.16% | 65.58% |
| model:gliner-nvidia | eligible | Organizations | 729/1806 | 40.37% | 50.83% | 40.37% |
| model:gliner-nvidia | eligible | Network identifiers | 6/20 | 30.00% | 50.00% | 30.00% |
| model:gliner-pii-base | eligible | Documents & identifiers | 309/818 | 37.78% | 48.41% | 37.78% |
| model:gliner-pii-base | eligible | People's names | 3274/5083 | 64.41% | 66.71% | 64.39% |
| model:gliner-pii-base | eligible | Phone numbers & email | 325/750 | 43.33% | 53.47% | 43.33% |
| model:gliner-pii-base | eligible | Addresses & locations | 916/1868 | 49.04% | 52.03% | 49.04% |
| model:gliner-pii-base | eligible | Organizations | 690/1806 | 38.21% | 48.28% | 38.21% |
| model:gliner-pii-base | eligible | Network identifiers | 1/20 | 5.00% | 35.00% | 5.00% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 283/818 | 34.60% | 47.80% | 34.60% |
| model:gliner-pii-edge | eligible | People's names | 3227/5083 | 63.49% | 66.36% | 63.49% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 253/750 | 33.73% | 45.73% | 33.73% |
| model:gliner-pii-edge | eligible | Addresses & locations | 787/1868 | 42.13% | 45.72% | 42.13% |
| model:gliner-pii-edge | eligible | Organizations | 731/1806 | 40.48% | 50.83% | 40.42% |
| model:gliner-pii-edge | eligible | Network identifiers | 1/20 | 5.00% | 30.00% | 5.00% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 255/818 | 31.17% | 50.61% | 30.93% |
| model:gliner-stream-pii | eligible | People's names | 2313/5083 | 45.50% | 48.63% | 45.47% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 155/750 | 20.67% | 31.73% | 20.53% |
| model:gliner-stream-pii | eligible | Addresses & locations | 928/1868 | 49.68% | 57.98% | 49.63% |
| model:gliner-stream-pii | eligible | Organizations | 461/1806 | 25.53% | 37.38% | 25.36% |
| model:gliner-stream-pii | eligible | Network identifiers | 1/20 | 5.00% | 15.00% | 5.00% |
| model:gliner-urchade | eligible | Documents & identifiers | 273/818 | 33.37% | 40.83% | 33.37% |
| model:gliner-urchade | eligible | People's names | 4136/5083 | 81.37% | 83.55% | 81.35% |
| model:gliner-urchade | eligible | Phone numbers & email | 469/750 | 62.53% | 74.53% | 62.53% |
| model:gliner-urchade | eligible | Addresses & locations | 1348/1868 | 72.16% | 76.07% | 72.16% |
| model:gliner-urchade | eligible | Organizations | 1056/1806 | 58.47% | 65.73% | 58.47% |
| model:gliner-urchade | eligible | Network identifiers | 8/20 | 40.00% | 90.00% | 35.00% |
| model:gliner2-fastino | eligible | Documents & identifiers | 393/818 | 48.04% | 62.35% | 48.04% |
| model:gliner2-fastino | eligible | People's names | 4071/5083 | 80.09% | 82.94% | 80.01% |
| model:gliner2-fastino | eligible | Phone numbers & email | 429/750 | 57.20% | 75.87% | 57.07% |
| model:gliner2-fastino | eligible | Addresses & locations | 1401/1868 | 75.00% | 79.44% | 74.95% |
| model:gliner2-fastino | eligible | Organizations | 1120/1806 | 62.02% | 69.82% | 61.85% |
| model:gliner2-fastino | eligible | Network identifiers | 3/20 | 15.00% | 95.00% | 15.00% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 457/818 | 55.87% | 73.72% | 55.87% |
| model:gliner2-hivetrace-omni | eligible | People's names | 3688/5083 | 72.56% | 76.23% | 72.56% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 383/750 | 51.07% | 75.07% | 51.07% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 1334/1868 | 71.41% | 76.50% | 71.41% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 998/1806 | 55.26% | 64.45% | 55.26% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 3/20 | 15.00% | 85.00% | 15.00% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 306/818 | 37.41% | 50.37% | 37.41% |
| model:gliner2-hivetrace-uni | eligible | People's names | 3108/5083 | 61.14% | 64.39% | 61.13% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 253/750 | 33.73% | 59.73% | 33.60% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 994/1868 | 53.21% | 57.76% | 53.16% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 428/1806 | 23.70% | 38.26% | 23.59% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 2/20 | 10.00% | 65.00% | 10.00% |
| model:gliner2-large | eligible | Documents & identifiers | 300/818 | 36.67% | 48.04% | 36.67% |
| model:gliner2-large | eligible | People's names | 3199/5083 | 62.94% | 65.95% | 62.88% |
| model:gliner2-large | eligible | Phone numbers & email | 343/750 | 45.73% | 63.60% | 45.47% |
| model:gliner2-large | eligible | Addresses & locations | 1027/1868 | 54.98% | 58.62% | 54.98% |
| model:gliner2-large | eligible | Organizations | 805/1806 | 44.57% | 52.49% | 44.57% |
| model:gliner2-large | eligible | Network identifiers | 2/20 | 10.00% | 60.00% | 10.00% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 360/818 | 44.01% | 52.44% | 43.89% |
| model:gliner2-vladlinv | eligible | People's names | 3746/5083 | 73.70% | 81.00% | 73.60% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 342/750 | 45.60% | 59.07% | 45.47% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 409/1868 | 21.90% | 22.54% | 21.90% |
| model:gliner2-vladlinv | eligible | Organizations | 19/1806 | 1.05% | 2.10% | 1.05% |
| model:gliner2-vladlinv | eligible | Network identifiers | 0/20 | 0.00% | 15.00% | 0.00% |
| model:gliner25-fastino | eligible | Documents & identifiers | 396/818 | 48.41% | 60.64% | 48.41% |
| model:gliner25-fastino | eligible | People's names | 3797/5083 | 74.70% | 77.02% | 74.68% |
| model:gliner25-fastino | eligible | Phone numbers & email | 421/750 | 56.13% | 72.13% | 55.87% |
| model:gliner25-fastino | eligible | Addresses & locations | 916/1868 | 49.04% | 52.30% | 49.04% |
| model:gliner25-fastino | eligible | Organizations | 586/1806 | 32.45% | 37.43% | 32.45% |
| model:gliner25-fastino | eligible | Network identifiers | 3/20 | 15.00% | 90.00% | 15.00% |
| model:gravitee-small | eligible | Documents & identifiers | 89/818 | 10.88% | 20.05% | 9.90% |
| model:gravitee-small | eligible | People's names | 2831/5083 | 55.70% | 58.65% | 52.10% |
| model:gravitee-small | eligible | Phone numbers & email | 146/750 | 19.47% | 46.13% | 17.20% |
| model:gravitee-small | eligible | Addresses & locations | 671/1868 | 35.92% | 40.47% | 32.23% |
| model:gravitee-small | eligible | Organizations | 334/1806 | 18.49% | 28.13% | 15.17% |
| model:gravitee-small | eligible | Network identifiers | 0/20 | 0.00% | 25.00% | 0.00% |
| model:kalyan-ettin | eligible | Documents & identifiers | 150/818 | 18.34% | 34.96% | 6.72% |
| model:kalyan-ettin | eligible | People's names | 2182/5083 | 42.93% | 55.73% | 42.32% |
| model:kalyan-ettin | eligible | Phone numbers & email | 200/750 | 26.67% | 50.00% | 9.33% |
| model:kalyan-ettin | eligible | Addresses & locations | 670/1868 | 35.87% | 43.79% | 25.37% |
| model:kalyan-ettin | eligible | Organizations | 127/1806 | 7.03% | 17.33% | 3.93% |
| model:kalyan-ettin | eligible | Network identifiers | 0/20 | 0.00% | 15.00% | 0.00% |
| model:mmbert32k | eligible | Documents & identifiers | 270/818 | 33.01% | 68.58% | 10.64% |
| model:mmbert32k | eligible | People's names | 3526/5083 | 69.37% | 79.26% | 64.61% |
| model:mmbert32k | eligible | Phone numbers & email | 229/750 | 30.53% | 70.67% | 21.47% |
| model:mmbert32k | eligible | Addresses & locations | 874/1868 | 46.79% | 60.87% | 33.35% |
| model:mmbert32k | eligible | Organizations | 243/1806 | 13.46% | 44.46% | 5.65% |
| model:mmbert32k | eligible | Network identifiers | 0/20 | 0.00% | 90.00% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 4/818 | 0.49% | 1.96% | 0.24% |
| model:natasha | eligible | People's names | 784/5083 | 15.42% | 15.92% | 15.42% |
| model:natasha | eligible | Phone numbers & email | 1/750 | 0.13% | 0.53% | 0.13% |
| model:natasha | eligible | Addresses & locations | 34/1868 | 1.82% | 2.41% | 1.82% |
| model:natasha | eligible | Organizations | 49/1806 | 2.71% | 3.05% | 2.71% |
| model:natasha | eligible | Network identifiers | 0/20 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 21/818 | 2.57% | 5.87% | 2.57% |
| model:ner-ru-gherman | eligible | People's names | 3137/5083 | 61.72% | 80.58% | 59.22% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/750 | 0.00% | 14.80% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 934/1868 | 50.00% | 62.74% | 42.56% |
| model:ner-ru-gherman | eligible | Organizations | 48/1806 | 2.66% | 21.48% | 1.99% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/20 | 0.00% | 20.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 62/818 | 7.58% | 22.98% | 4.40% |
| model:ner-ru-yqelz | eligible | People's names | 3080/5083 | 60.59% | 65.65% | 54.48% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 73/750 | 9.73% | 27.20% | 6.13% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 1279/1868 | 68.47% | 76.18% | 62.85% |
| model:ner-ru-yqelz | eligible | Organizations | 1330/1806 | 73.64% | 87.71% | 66.22% |
| model:ner-ru-yqelz | eligible | Network identifiers | 3/20 | 15.00% | 85.00% | 10.00% |
| model:nuner-zero | eligible | Documents & identifiers | 392/818 | 47.92% | 59.29% | 34.96% |
| model:nuner-zero | eligible | People's names | 3887/5083 | 76.47% | 79.01% | 61.48% |
| model:nuner-zero | eligible | Phone numbers & email | 441/750 | 58.80% | 69.73% | 46.00% |
| model:nuner-zero | eligible | Addresses & locations | 851/1868 | 45.56% | 49.63% | 33.99% |
| model:nuner-zero | eligible | Organizations | 912/1806 | 50.50% | 60.13% | 18.66% |
| model:nuner-zero | eligible | Network identifiers | 4/20 | 20.00% | 90.00% | 20.00% |
| model:nym-base | eligible | Documents & identifiers | 317/818 | 38.75% | 58.19% | 34.23% |
| model:nym-base | eligible | People's names | 3494/5083 | 68.74% | 87.55% | 77.02% |
| model:nym-base | eligible | Phone numbers & email | 273/750 | 36.40% | 63.07% | 35.47% |
| model:nym-base | eligible | Addresses & locations | 1313/1868 | 70.29% | 77.41% | 68.25% |
| model:nym-base | eligible | Organizations | 343/1806 | 18.99% | 34.72% | 18.22% |
| model:nym-base | eligible | Network identifiers | 0/20 | 0.00% | 70.00% | 0.00% |
| model:nym-small | eligible | Documents & identifiers | 336/818 | 41.08% | 62.47% | 35.94% |
| model:nym-small | eligible | People's names | 3253/5083 | 64.00% | 82.04% | 72.58% |
| model:nym-small | eligible | Phone numbers & email | 277/750 | 36.93% | 59.73% | 33.87% |
| model:nym-small | eligible | Addresses & locations | 1221/1868 | 65.36% | 72.22% | 62.90% |
| model:nym-small | eligible | Organizations | 234/1806 | 12.96% | 29.62% | 12.24% |
| model:nym-small | eligible | Network identifiers | 1/20 | 5.00% | 85.00% | 0.00% |
| model:openai-base | eligible | Documents & identifiers | 330/818 | 40.34% | 55.50% | 39.61% |
| model:openai-base | eligible | People's names | 1957/5083 | 38.50% | 40.74% | 36.93% |
| model:openai-base | eligible | Phone numbers & email | 358/750 | 47.73% | 60.67% | 46.93% |
| model:openai-base | eligible | Addresses & locations | 500/1868 | 26.77% | 30.03% | 25.91% |
| model:openai-base | eligible | Organizations | 104/1806 | 5.76% | 9.19% | 5.09% |
| model:openai-base | eligible | Network identifiers | 2/20 | 10.00% | 20.00% | 5.00% |
| model:openmed-multilingual | eligible | Documents & identifiers | 252/818 | 30.81% | 57.33% | 22.37% |
| model:openmed-multilingual | eligible | People's names | 2782/5083 | 54.73% | 69.55% | 58.37% |
| model:openmed-multilingual | eligible | Phone numbers & email | 193/750 | 25.73% | 54.93% | 23.87% |
| model:openmed-multilingual | eligible | Addresses & locations | 826/1868 | 44.22% | 54.18% | 39.29% |
| model:openmed-multilingual | eligible | Organizations | 144/1806 | 7.97% | 25.14% | 6.48% |
| model:openmed-multilingual | eligible | Network identifiers | 0/20 | 0.00% | 30.00% | 0.00% |
| model:openmed-nemotron | eligible | Documents & identifiers | 100/818 | 12.22% | 28.00% | 4.40% |
| model:openmed-nemotron | eligible | People's names | 2472/5083 | 48.63% | 64.92% | 45.72% |
| model:openmed-nemotron | eligible | Phone numbers & email | 157/750 | 20.93% | 54.93% | 14.93% |
| model:openmed-nemotron | eligible | Addresses & locations | 619/1868 | 33.14% | 44.75% | 25.37% |
| model:openmed-nemotron | eligible | Organizations | 189/1806 | 10.47% | 29.07% | 6.59% |
| model:openmed-nemotron | eligible | Network identifiers | 0/20 | 0.00% | 25.00% | 0.00% |
| model:opf-kz-ru | eligible | Documents & identifiers | 402/818 | 49.14% | 65.40% | 45.97% |
| model:opf-kz-ru | eligible | People's names | 1227/5083 | 24.14% | 26.91% | 20.46% |
| model:opf-kz-ru | eligible | Phone numbers & email | 355/750 | 47.33% | 60.27% | 46.27% |
| model:opf-kz-ru | eligible | Addresses & locations | 486/1868 | 26.02% | 29.82% | 22.75% |
| model:opf-kz-ru | eligible | Organizations | 78/1806 | 4.32% | 7.75% | 3.54% |
| model:opf-kz-ru | eligible | Network identifiers | 2/20 | 10.00% | 25.00% | 5.00% |
| model:opf-ru | eligible | Documents & identifiers | 237/818 | 28.97% | 59.54% | 15.28% |
| model:opf-ru | eligible | People's names | 3272/5083 | 64.37% | 72.00% | 61.62% |
| model:opf-ru | eligible | Phone numbers & email | 240/750 | 32.00% | 72.80% | 30.00% |
| model:opf-ru | eligible | Addresses & locations | 630/1868 | 33.73% | 45.45% | 27.68% |
| model:opf-ru | eligible | Organizations | 237/1806 | 13.12% | 33.55% | 9.19% |
| model:opf-ru | eligible | Network identifiers | 0/20 | 0.00% | 80.00% | 0.00% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 201/818 | 24.57% | 50.73% | 16.75% |
| model:opf-ru-v2 | eligible | People's names | 1429/5083 | 28.11% | 30.02% | 25.54% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 220/750 | 29.33% | 51.60% | 27.20% |
| model:opf-ru-v2 | eligible | Addresses & locations | 364/1868 | 19.49% | 23.55% | 17.40% |
| model:opf-ru-v2 | eligible | Organizations | 128/1806 | 7.09% | 12.35% | 5.59% |
| model:opf-ru-v2 | eligible | Network identifiers | 0/20 | 0.00% | 15.00% | 0.00% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 570/818 | 69.68% | 85.45% | 63.08% |
| model:pii-shield-onnx | eligible | People's names | 3840/5083 | 75.55% | 79.83% | 64.29% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 546/750 | 72.80% | 91.20% | 65.47% |
| model:pii-shield-onnx | eligible | Addresses & locations | 1423/1868 | 76.18% | 82.39% | 66.22% |
| model:pii-shield-onnx | eligible | Organizations | 1291/1806 | 71.48% | 83.61% | 63.68% |
| model:pii-shield-onnx | eligible | Network identifiers | 17/20 | 85.00% | 90.00% | 75.00% |
| model:pplx | eligible | Documents & identifiers | 529/818 | 64.67% | 76.04% | 64.43% |
| model:pplx | eligible | People's names | 4523/5083 | 88.98% | 93.98% | 88.67% |
| model:pplx | eligible | Phone numbers & email | 478/750 | 63.73% | 76.80% | 62.40% |
| model:pplx | eligible | Addresses & locations | 1067/1868 | 57.12% | 59.26% | 56.42% |
| model:pplx | eligible | Organizations | 139/1806 | 7.70% | 13.01% | 7.70% |
| model:pplx | eligible | Network identifiers | 4/20 | 20.00% | 55.00% | 20.00% |
| model:ru-legal-ner | eligible | Documents & identifiers | 308/818 | 37.65% | 65.16% | 19.07% |
| model:ru-legal-ner | eligible | People's names | 2267/5083 | 44.60% | 48.36% | 34.59% |
| model:ru-legal-ner | eligible | Phone numbers & email | 286/750 | 38.13% | 76.40% | 29.20% |
| model:ru-legal-ner | eligible | Addresses & locations | 1051/1868 | 56.26% | 62.10% | 45.13% |
| model:ru-legal-ner | eligible | Organizations | 779/1806 | 43.13% | 57.14% | 31.73% |
| model:ru-legal-ner | eligible | Network identifiers | 5/20 | 25.00% | 80.00% | 15.00% |
| model:ru-pii-ner | eligible | Documents & identifiers | 367/818 | 44.87% | 54.28% | 44.62% |
| model:ru-pii-ner | eligible | People's names | 2492/5083 | 49.03% | 52.74% | 49.01% |
| model:ru-pii-ner | eligible | Phone numbers & email | 285/750 | 38.00% | 46.13% | 37.33% |
| model:ru-pii-ner | eligible | Addresses & locations | 459/1868 | 24.57% | 26.07% | 24.57% |
| model:ru-pii-ner | eligible | Organizations | 88/1806 | 4.87% | 7.31% | 4.82% |
| model:ru-pii-ner | eligible | Network identifiers | 0/20 | 0.00% | 5.00% | 0.00% |
| model:rules-ru | eligible | Documents & identifiers | 1/818 | 0.12% | 0.61% | 0.00% |
| model:rules-ru | eligible | People's names | 1/5083 | 0.02% | 0.02% | 0.02% |
| model:rules-ru | eligible | Phone numbers & email | 218/750 | 29.07% | 36.13% | 28.67% |
| model:rules-ru | eligible | Addresses & locations | 0/1868 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Organizations | 0/1806 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Network identifiers | 1/20 | 5.00% | 70.00% | 5.00% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/818 | 0.00% | 0.37% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 4/5083 | 0.08% | 0.08% | 0.08% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/750 | 0.00% | 0.27% | 0.00% |
| model:spacy-alrosait | eligible | Addresses & locations | 2/1868 | 0.11% | 0.21% | 0.11% |
| model:spacy-alrosait | eligible | Organizations | 0/1806 | 0.00% | 0.06% | 0.00% |
| model:spacy-alrosait | eligible | Network identifiers | 0/20 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 21/818 | 2.57% | 6.60% | 2.57% |
| model:spacy-ru-lg | eligible | People's names | 1433/5083 | 28.19% | 29.18% | 28.19% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 31/750 | 4.13% | 8.67% | 4.00% |
| model:spacy-ru-lg | eligible | Addresses & locations | 230/1868 | 12.31% | 13.65% | 12.31% |
| model:spacy-ru-lg | eligible | Organizations | 185/1806 | 10.24% | 12.02% | 10.19% |
| model:spacy-ru-lg | eligible | Network identifiers | 0/20 | 0.00% | 5.00% | 0.00% |
| model:stanza-ru | eligible | Documents & identifiers | 155/818 | 18.95% | 36.67% | 18.83% |
| model:stanza-ru | eligible | People's names | 3344/5083 | 65.79% | 68.33% | 65.75% |
| model:stanza-ru | eligible | Phone numbers & email | 60/750 | 8.00% | 12.40% | 7.87% |
| model:stanza-ru | eligible | Addresses & locations | 845/1868 | 45.24% | 49.41% | 45.24% |
| model:stanza-ru | eligible | Organizations | 744/1806 | 41.20% | 49.50% | 41.20% |
| model:stanza-ru | eligible | Network identifiers | 1/20 | 5.00% | 15.00% | 5.00% |
| model:traciora | eligible | Documents & identifiers | 148/818 | 18.09% | 40.59% | 8.56% |
| model:traciora | eligible | People's names | 2405/5083 | 47.31% | 52.35% | 42.34% |
| model:traciora | eligible | Phone numbers & email | 273/750 | 36.40% | 62.40% | 32.67% |
| model:traciora | eligible | Addresses & locations | 698/1868 | 37.37% | 42.93% | 33.08% |
| model:traciora | eligible | Organizations | 251/1806 | 13.90% | 25.91% | 11.35% |
| model:traciora | eligible | Network identifiers | 0/20 | 0.00% | 30.00% | 0.00% |
