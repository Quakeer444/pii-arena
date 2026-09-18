# dialogpii-en: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/dialogpii-en.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Documents & identifiers | 150/260 | 57.69% | 70.38% | 57.31% |
| composition:fastino | eligible | People's names | 1418/1558 | 91.01% | 93.77% | 91.01% |
| composition:fastino | eligible | Phone numbers & email | 61/200 | 30.50% | 85.50% | 30.50% |
| composition:fastino | eligible | Addresses & locations | 439/483 | 90.89% | 93.37% | 90.89% |
| composition:fastino | eligible | Organizations | 461/579 | 79.62% | 86.87% | 79.62% |
| composition:fastino | eligible | Network identifiers | 0/7 | 0.00% | 71.43% | 0.00% |
| composition:pplx | eligible | Documents & identifiers | 190/260 | 73.08% | 82.31% | 73.08% |
| composition:pplx | eligible | People's names | 1450/1558 | 93.07% | 96.66% | 93.07% |
| composition:pplx | eligible | Phone numbers & email | 120/200 | 60.00% | 77.50% | 60.00% |
| composition:pplx | eligible | Addresses & locations | 352/483 | 72.88% | 74.12% | 72.88% |
| composition:pplx | eligible | Organizations | 74/579 | 12.78% | 17.79% | 12.78% |
| composition:pplx | eligible | Network identifiers | 6/7 | 85.71% | 100.00% | 85.71% |
| composition:pplx+fastino | eligible | Documents & identifiers | 197/260 | 75.77% | 85.77% | 75.77% |
| composition:pplx+fastino | eligible | People's names | 1487/1558 | 95.44% | 98.14% | 95.44% |
| composition:pplx+fastino | eligible | Phone numbers & email | 140/200 | 70.00% | 88.50% | 70.00% |
| composition:pplx+fastino | eligible | Addresses & locations | 457/483 | 94.62% | 95.65% | 94.62% |
| composition:pplx+fastino | eligible | Organizations | 466/579 | 80.48% | 87.91% | 80.48% |
| composition:pplx+fastino | eligible | Network identifiers | 6/7 | 85.71% | 100.00% | 85.71% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 197/260 | 75.77% | 86.15% | 75.77% |
| composition:pplx+fastino+bardsai | eligible | People's names | 1487/1558 | 95.44% | 98.14% | 95.44% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 141/200 | 70.50% | 89.50% | 70.50% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 457/483 | 94.62% | 95.86% | 94.62% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 495/579 | 85.49% | 92.75% | 85.32% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 6/7 | 85.71% | 100.00% | 85.71% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 199/260 | 76.54% | 87.31% | 75.77% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 1489/1558 | 95.57% | 98.14% | 95.57% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 141/200 | 70.50% | 90.50% | 70.50% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 458/483 | 94.82% | 96.07% | 94.82% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 496/579 | 85.66% | 93.26% | 85.49% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 6/7 | 85.71% | 100.00% | 85.71% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 199/260 | 76.54% | 87.31% | 75.77% |
| composition:pplx+fastino+mmbert | eligible | People's names | 1489/1558 | 95.57% | 98.14% | 95.57% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 140/200 | 70.00% | 90.50% | 70.00% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 458/483 | 94.82% | 95.86% | 94.82% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 471/579 | 81.35% | 89.29% | 81.17% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 6/7 | 85.71% | 100.00% | 85.71% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 136/260 | 52.31% | 68.85% | 49.62% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 1382/1558 | 88.70% | 93.84% | 88.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 103/200 | 51.50% | 70.50% | 51.50% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 340/483 | 70.39% | 71.64% | 70.39% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 75/579 | 12.95% | 18.48% | 12.78% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 4/7 | 57.14% | 85.71% | 57.14% |
| model:apararti | eligible | Documents & identifiers | 161/260 | 61.92% | 78.08% | 60.00% |
| model:apararti | eligible | People's names | 1122/1558 | 72.02% | 75.16% | 70.28% |
| model:apararti | eligible | Phone numbers & email | 112/200 | 56.00% | 71.00% | 55.50% |
| model:apararti | eligible | Addresses & locations | 157/483 | 32.51% | 34.58% | 31.68% |
| model:apararti | eligible | Organizations | 49/579 | 8.46% | 11.40% | 6.39% |
| model:apararti | eligible | Network identifiers | 3/7 | 42.86% | 57.14% | 42.86% |
| model:bardsai-eu | eligible | Documents & identifiers | 121/260 | 46.54% | 63.85% | 40.77% |
| model:bardsai-eu | eligible | People's names | 1283/1558 | 82.35% | 90.63% | 80.94% |
| model:bardsai-eu | eligible | Phone numbers & email | 32/200 | 16.00% | 73.50% | 15.00% |
| model:bardsai-eu | eligible | Addresses & locations | 405/483 | 83.85% | 86.54% | 82.40% |
| model:bardsai-eu | eligible | Organizations | 371/579 | 64.08% | 71.16% | 62.18% |
| model:bardsai-eu | eligible | Network identifiers | 0/7 | 0.00% | 71.43% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 5/260 | 1.92% | 7.69% | 1.92% |
| model:davlan-mbert | eligible | People's names | 1225/1558 | 78.63% | 91.59% | 77.34% |
| model:davlan-mbert | eligible | Phone numbers & email | 4/200 | 2.00% | 13.50% | 2.00% |
| model:davlan-mbert | eligible | Addresses & locations | 352/483 | 72.88% | 75.36% | 71.84% |
| model:davlan-mbert | eligible | Organizations | 358/579 | 61.83% | 71.33% | 61.14% |
| model:davlan-mbert | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 4/260 | 1.54% | 4.23% | 1.54% |
| model:davlan-xlmr | eligible | People's names | 1265/1558 | 81.19% | 94.09% | 80.68% |
| model:davlan-xlmr | eligible | Phone numbers & email | 2/200 | 1.00% | 18.50% | 1.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 368/483 | 76.19% | 79.09% | 74.33% |
| model:davlan-xlmr | eligible | Organizations | 411/579 | 70.98% | 81.52% | 70.47% |
| model:davlan-xlmr | eligible | Network identifiers | 0/7 | 0.00% | 14.29% | 0.00% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 2/260 | 0.77% | 1.54% | 0.00% |
| model:fef2-secret-ru | eligible | People's names | 22/1558 | 1.41% | 1.80% | 1.09% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 2/200 | 1.00% | 5.00% | 1.00% |
| model:fef2-secret-ru | eligible | Addresses & locations | 6/483 | 1.24% | 1.45% | 0.83% |
| model:fef2-secret-ru | eligible | Organizations | 4/579 | 0.69% | 1.04% | 0.35% |
| model:fef2-secret-ru | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 92/260 | 35.38% | 42.31% | 35.38% |
| model:gliner-multi-v21 | eligible | People's names | 1375/1558 | 88.25% | 90.95% | 88.19% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 28/200 | 14.00% | 68.00% | 14.00% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 400/483 | 82.82% | 84.06% | 82.82% |
| model:gliner-multi-v21 | eligible | Organizations | 422/579 | 72.88% | 81.69% | 72.88% |
| model:gliner-multi-v21 | eligible | Network identifiers | 0/7 | 0.00% | 14.29% | 0.00% |
| model:gliner-nvidia | eligible | Documents & identifiers | 101/260 | 38.85% | 46.54% | 38.85% |
| model:gliner-nvidia | eligible | People's names | 1243/1558 | 79.78% | 91.40% | 77.15% |
| model:gliner-nvidia | eligible | Phone numbers & email | 116/200 | 58.00% | 71.00% | 58.00% |
| model:gliner-nvidia | eligible | Addresses & locations | 436/483 | 90.27% | 92.55% | 90.27% |
| model:gliner-nvidia | eligible | Organizations | 361/579 | 62.35% | 70.64% | 62.35% |
| model:gliner-nvidia | eligible | Network identifiers | 5/7 | 71.43% | 85.71% | 71.43% |
| model:gliner-nvidia+ov100 | eligible | Documents & identifiers | 100/260 | 38.46% | 45.00% | 38.46% |
| model:gliner-nvidia+ov100 | eligible | People's names | 1238/1558 | 79.46% | 91.46% | 76.70% |
| model:gliner-nvidia+ov100 | eligible | Phone numbers & email | 118/200 | 59.00% | 72.50% | 59.00% |
| model:gliner-nvidia+ov100 | eligible | Addresses & locations | 436/483 | 90.27% | 93.17% | 89.86% |
| model:gliner-nvidia+ov100 | eligible | Organizations | 366/579 | 63.21% | 71.16% | 63.21% |
| model:gliner-nvidia+ov100 | eligible | Network identifiers | 5/7 | 71.43% | 100.00% | 71.43% |
| model:gliner-nvidia+sent300 | eligible | Documents & identifiers | 119/260 | 45.77% | 56.54% | 45.77% |
| model:gliner-nvidia+sent300 | eligible | People's names | 1315/1558 | 84.40% | 94.99% | 79.40% |
| model:gliner-nvidia+sent300 | eligible | Phone numbers & email | 117/200 | 58.50% | 72.00% | 58.50% |
| model:gliner-nvidia+sent300 | eligible | Addresses & locations | 444/483 | 91.93% | 95.03% | 91.93% |
| model:gliner-nvidia+sent300 | eligible | Organizations | 393/579 | 67.88% | 75.99% | 67.88% |
| model:gliner-nvidia+sent300 | eligible | Network identifiers | 5/7 | 71.43% | 100.00% | 71.43% |
| model:gliner-pii-base | eligible | Documents & identifiers | 88/260 | 33.85% | 47.69% | 33.85% |
| model:gliner-pii-base | eligible | People's names | 1278/1558 | 82.03% | 85.11% | 81.96% |
| model:gliner-pii-base | eligible | Phone numbers & email | 49/200 | 24.50% | 68.00% | 24.50% |
| model:gliner-pii-base | eligible | Addresses & locations | 392/483 | 81.16% | 83.85% | 80.95% |
| model:gliner-pii-base | eligible | Organizations | 401/579 | 69.26% | 81.52% | 69.26% |
| model:gliner-pii-base | eligible | Network identifiers | 2/7 | 28.57% | 100.00% | 28.57% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 127/260 | 48.85% | 63.08% | 47.69% |
| model:gliner-pii-edge | eligible | People's names | 1267/1558 | 81.32% | 84.02% | 81.32% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 46/200 | 23.00% | 71.00% | 23.00% |
| model:gliner-pii-edge | eligible | Addresses & locations | 369/483 | 76.40% | 78.47% | 76.19% |
| model:gliner-pii-edge | eligible | Organizations | 386/579 | 66.67% | 79.97% | 66.67% |
| model:gliner-pii-edge | eligible | Network identifiers | 2/7 | 28.57% | 85.71% | 28.57% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 85/260 | 32.69% | 53.85% | 32.69% |
| model:gliner-stream-pii | eligible | People's names | 863/1558 | 55.39% | 58.15% | 55.39% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 79/200 | 39.50% | 52.50% | 39.50% |
| model:gliner-stream-pii | eligible | Addresses & locations | 370/483 | 76.60% | 80.12% | 76.60% |
| model:gliner-stream-pii | eligible | Organizations | 248/579 | 42.83% | 53.89% | 42.66% |
| model:gliner-stream-pii | eligible | Network identifiers | 2/7 | 28.57% | 57.14% | 28.57% |
| model:gliner-urchade | eligible | Documents & identifiers | 55/260 | 21.15% | 25.00% | 21.15% |
| model:gliner-urchade | eligible | People's names | 1375/1558 | 88.25% | 90.95% | 88.25% |
| model:gliner-urchade | eligible | Phone numbers & email | 73/200 | 36.50% | 80.00% | 36.50% |
| model:gliner-urchade | eligible | Addresses & locations | 403/483 | 83.44% | 84.47% | 83.44% |
| model:gliner-urchade | eligible | Organizations | 418/579 | 72.19% | 79.45% | 72.19% |
| model:gliner-urchade | eligible | Network identifiers | 3/7 | 42.86% | 100.00% | 42.86% |
| model:gliner2-fastino | eligible | Documents & identifiers | 150/260 | 57.69% | 70.38% | 57.31% |
| model:gliner2-fastino | eligible | People's names | 1418/1558 | 91.01% | 93.77% | 91.01% |
| model:gliner2-fastino | eligible | Phone numbers & email | 61/200 | 30.50% | 85.50% | 30.50% |
| model:gliner2-fastino | eligible | Addresses & locations | 439/483 | 90.89% | 93.37% | 90.89% |
| model:gliner2-fastino | eligible | Organizations | 461/579 | 79.62% | 86.87% | 79.62% |
| model:gliner2-fastino | eligible | Network identifiers | 0/7 | 0.00% | 71.43% | 0.00% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 162/260 | 62.31% | 75.77% | 62.31% |
| model:gliner2-hivetrace-omni | eligible | People's names | 1277/1558 | 81.96% | 85.43% | 81.96% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 53/200 | 26.50% | 76.00% | 26.50% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 426/483 | 88.20% | 91.10% | 87.99% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 405/579 | 69.95% | 76.68% | 69.95% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 0/7 | 0.00% | 71.43% | 0.00% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 126/260 | 48.46% | 60.38% | 48.46% |
| model:gliner2-hivetrace-uni | eligible | People's names | 1164/1558 | 74.71% | 78.18% | 74.71% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 53/200 | 26.50% | 75.50% | 26.50% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 374/483 | 77.43% | 80.54% | 77.23% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 265/579 | 45.77% | 60.45% | 45.77% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 0/7 | 0.00% | 71.43% | 0.00% |
| model:gliner2-large | eligible | Documents & identifiers | 110/260 | 42.31% | 48.85% | 42.31% |
| model:gliner2-large | eligible | People's names | 1393/1558 | 89.41% | 92.36% | 89.41% |
| model:gliner2-large | eligible | Phone numbers & email | 53/200 | 26.50% | 79.00% | 26.50% |
| model:gliner2-large | eligible | Addresses & locations | 418/483 | 86.54% | 88.41% | 86.54% |
| model:gliner2-large | eligible | Organizations | 434/579 | 74.96% | 85.32% | 74.96% |
| model:gliner2-large | eligible | Network identifiers | 0/7 | 0.00% | 71.43% | 0.00% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 103/260 | 39.62% | 48.08% | 38.85% |
| model:gliner2-vladlinv | eligible | People's names | 1386/1558 | 88.96% | 93.32% | 88.77% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 47/200 | 23.50% | 62.00% | 23.50% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 180/483 | 37.27% | 38.30% | 37.27% |
| model:gliner2-vladlinv | eligible | Organizations | 9/579 | 1.55% | 3.45% | 1.55% |
| model:gliner2-vladlinv | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:gliner25-fastino | eligible | Documents & identifiers | 130/260 | 50.00% | 61.54% | 49.62% |
| model:gliner25-fastino | eligible | People's names | 1357/1558 | 87.10% | 89.86% | 87.10% |
| model:gliner25-fastino | eligible | Phone numbers & email | 52/200 | 26.00% | 77.50% | 26.00% |
| model:gliner25-fastino | eligible | Addresses & locations | 288/483 | 59.63% | 61.70% | 59.42% |
| model:gliner25-fastino | eligible | Organizations | 303/579 | 52.33% | 56.48% | 52.33% |
| model:gliner25-fastino | eligible | Network identifiers | 0/7 | 0.00% | 71.43% | 0.00% |
| model:gliner25-fastino+nochunk | eligible | Documents & identifiers | 124/260 | 47.69% | 55.00% | 47.69% |
| model:gliner25-fastino+nochunk | eligible | People's names | 1037/1558 | 66.56% | 68.61% | 66.56% |
| model:gliner25-fastino+nochunk | eligible | Phone numbers & email | 44/200 | 22.00% | 76.00% | 22.00% |
| model:gliner25-fastino+nochunk | eligible | Addresses & locations | 360/483 | 74.53% | 77.43% | 74.12% |
| model:gliner25-fastino+nochunk | eligible | Organizations | 314/579 | 54.23% | 60.10% | 54.23% |
| model:gliner25-fastino+nochunk | eligible | Network identifiers | 0/7 | 0.00% | 71.43% | 0.00% |
| model:gliner25-fastino+ov100 | eligible | Documents & identifiers | 139/260 | 53.46% | 62.31% | 53.08% |
| model:gliner25-fastino+ov100 | eligible | People's names | 1345/1558 | 86.33% | 89.15% | 86.33% |
| model:gliner25-fastino+ov100 | eligible | Phone numbers & email | 51/200 | 25.50% | 77.50% | 25.50% |
| model:gliner25-fastino+ov100 | eligible | Addresses & locations | 302/483 | 62.53% | 64.80% | 62.32% |
| model:gliner25-fastino+ov100 | eligible | Organizations | 327/579 | 56.48% | 62.35% | 56.13% |
| model:gliner25-fastino+ov100 | eligible | Network identifiers | 0/7 | 0.00% | 71.43% | 0.00% |
| model:gliner25-fastino+sent300 | eligible | Documents & identifiers | 141/260 | 54.23% | 66.15% | 52.69% |
| model:gliner25-fastino+sent300 | eligible | People's names | 1374/1558 | 88.19% | 91.40% | 87.55% |
| model:gliner25-fastino+sent300 | eligible | Phone numbers & email | 50/200 | 25.00% | 79.50% | 25.00% |
| model:gliner25-fastino+sent300 | eligible | Addresses & locations | 278/483 | 57.56% | 59.63% | 57.35% |
| model:gliner25-fastino+sent300 | eligible | Organizations | 284/579 | 49.05% | 53.02% | 49.05% |
| model:gliner25-fastino+sent300 | eligible | Network identifiers | 0/7 | 0.00% | 71.43% | 0.00% |
| model:gravitee-small | eligible | Documents & identifiers | 45/260 | 17.31% | 26.54% | 16.54% |
| model:gravitee-small | eligible | People's names | 1363/1558 | 87.48% | 90.69% | 83.83% |
| model:gravitee-small | eligible | Phone numbers & email | 32/200 | 16.00% | 59.00% | 14.50% |
| model:gravitee-small | eligible | Addresses & locations | 378/483 | 78.26% | 82.40% | 76.40% |
| model:gravitee-small | eligible | Organizations | 218/579 | 37.65% | 49.91% | 34.89% |
| model:gravitee-small | eligible | Network identifiers | 0/7 | 0.00% | 57.14% | 0.00% |
| model:kalyan-ettin | eligible | Documents & identifiers | 76/260 | 29.23% | 45.38% | 16.54% |
| model:kalyan-ettin | eligible | People's names | 995/1558 | 63.86% | 84.85% | 71.89% |
| model:kalyan-ettin | eligible | Phone numbers & email | 51/200 | 25.50% | 61.00% | 19.00% |
| model:kalyan-ettin | eligible | Addresses & locations | 327/483 | 67.70% | 74.95% | 62.73% |
| model:kalyan-ettin | eligible | Organizations | 104/579 | 17.96% | 33.85% | 12.44% |
| model:kalyan-ettin | eligible | Network identifiers | 0/7 | 0.00% | 14.29% | 0.00% |
| model:mmbert32k | eligible | Documents & identifiers | 90/260 | 34.62% | 69.62% | 10.77% |
| model:mmbert32k | eligible | People's names | 1028/1558 | 65.98% | 78.11% | 67.27% |
| model:mmbert32k | eligible | Phone numbers & email | 33/200 | 16.50% | 72.00% | 14.00% |
| model:mmbert32k | eligible | Addresses & locations | 209/483 | 43.27% | 52.80% | 40.58% |
| model:mmbert32k | eligible | Organizations | 80/579 | 13.82% | 32.64% | 9.50% |
| model:mmbert32k | eligible | Network identifiers | 0/7 | 0.00% | 85.71% | 0.00% |
| model:mmbert32k+nochunk | eligible | Documents & identifiers | 100/260 | 38.46% | 71.54% | 8.85% |
| model:mmbert32k+nochunk | eligible | People's names | 474/1558 | 30.42% | 41.08% | 29.14% |
| model:mmbert32k+nochunk | eligible | Phone numbers & email | 33/200 | 16.50% | 58.50% | 12.50% |
| model:mmbert32k+nochunk | eligible | Addresses & locations | 175/483 | 36.23% | 45.76% | 31.88% |
| model:mmbert32k+nochunk | eligible | Organizations | 36/579 | 6.22% | 19.34% | 2.94% |
| model:mmbert32k+nochunk | eligible | Network identifiers | 0/7 | 0.00% | 85.71% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 2/260 | 0.77% | 1.54% | 0.77% |
| model:natasha | eligible | People's names | 177/1558 | 11.36% | 11.75% | 11.36% |
| model:natasha | eligible | Phone numbers & email | 0/200 | 0.00% | 0.50% | 0.00% |
| model:natasha | eligible | Addresses & locations | 62/483 | 12.84% | 13.46% | 12.84% |
| model:natasha | eligible | Organizations | 55/579 | 9.50% | 9.67% | 9.50% |
| model:natasha | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/260 | 0.00% | 4.23% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 1092/1558 | 70.09% | 91.91% | 69.38% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 2/200 | 1.00% | 21.00% | 1.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 285/483 | 59.01% | 71.01% | 49.07% |
| model:ner-ru-gherman | eligible | Organizations | 44/579 | 7.60% | 35.41% | 7.25% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/7 | 0.00% | 14.29% | 0.00% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 30/260 | 11.54% | 21.15% | 6.54% |
| model:ner-ru-yqelz | eligible | People's names | 931/1558 | 59.76% | 63.67% | 55.07% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 8/200 | 4.00% | 34.00% | 3.50% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 398/483 | 82.40% | 85.92% | 80.12% |
| model:ner-ru-yqelz | eligible | Organizations | 489/579 | 84.46% | 90.67% | 79.79% |
| model:ner-ru-yqelz | eligible | Network identifiers | 0/7 | 0.00% | 85.71% | 0.00% |
| model:nuner-zero | eligible | Documents & identifiers | 162/260 | 62.31% | 72.69% | 48.46% |
| model:nuner-zero | eligible | People's names | 1437/1558 | 92.23% | 95.12% | 71.63% |
| model:nuner-zero | eligible | Phone numbers & email | 131/200 | 65.50% | 80.00% | 19.50% |
| model:nuner-zero | eligible | Addresses & locations | 318/483 | 65.84% | 67.91% | 42.24% |
| model:nuner-zero | eligible | Organizations | 425/579 | 73.40% | 81.00% | 31.26% |
| model:nuner-zero | eligible | Network identifiers | 4/7 | 57.14% | 100.00% | 28.57% |
| model:nym-base | eligible | Documents & identifiers | 112/260 | 43.08% | 60.38% | 36.15% |
| model:nym-base | eligible | People's names | 1088/1558 | 69.83% | 92.23% | 79.27% |
| model:nym-base | eligible | Phone numbers & email | 47/200 | 23.50% | 64.00% | 22.00% |
| model:nym-base | eligible | Addresses & locations | 385/483 | 79.71% | 83.85% | 79.92% |
| model:nym-base | eligible | Organizations | 144/579 | 24.87% | 40.76% | 25.56% |
| model:nym-base | eligible | Network identifiers | 2/7 | 28.57% | 71.43% | 28.57% |
| model:nym-base+ov100 | eligible | Documents & identifiers | 114/260 | 43.85% | 61.92% | 35.77% |
| model:nym-base+ov100 | eligible | People's names | 1080/1558 | 69.32% | 91.46% | 78.50% |
| model:nym-base+ov100 | eligible | Phone numbers & email | 48/200 | 24.00% | 65.00% | 23.00% |
| model:nym-base+ov100 | eligible | Addresses & locations | 379/483 | 78.47% | 82.61% | 77.85% |
| model:nym-base+ov100 | eligible | Organizations | 124/579 | 21.42% | 36.79% | 21.59% |
| model:nym-base+ov100 | eligible | Network identifiers | 2/7 | 28.57% | 71.43% | 28.57% |
| model:nym-base+sent300 | eligible | Documents & identifiers | 118/260 | 45.38% | 62.31% | 40.00% |
| model:nym-base+sent300 | eligible | People's names | 1085/1558 | 69.64% | 91.46% | 79.01% |
| model:nym-base+sent300 | eligible | Phone numbers & email | 45/200 | 22.50% | 67.50% | 22.00% |
| model:nym-base+sent300 | eligible | Addresses & locations | 386/483 | 79.92% | 84.27% | 80.33% |
| model:nym-base+sent300 | eligible | Organizations | 164/579 | 28.32% | 44.56% | 27.98% |
| model:nym-base+sent300 | eligible | Network identifiers | 2/7 | 28.57% | 71.43% | 28.57% |
| model:openai-base | eligible | Documents & identifiers | 154/260 | 59.23% | 73.46% | 56.92% |
| model:openai-base | eligible | People's names | 1216/1558 | 78.05% | 80.30% | 77.60% |
| model:openai-base | eligible | Phone numbers & email | 111/200 | 55.50% | 68.50% | 56.00% |
| model:openai-base | eligible | Addresses & locations | 147/483 | 30.43% | 31.68% | 29.81% |
| model:openai-base | eligible | Organizations | 43/579 | 7.43% | 7.94% | 6.91% |
| model:openai-base | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:openmed-multilingual | eligible | Documents & identifiers | 116/260 | 44.62% | 66.15% | 35.00% |
| model:openmed-multilingual | eligible | People's names | 1098/1558 | 70.47% | 92.62% | 80.49% |
| model:openmed-multilingual | eligible | Phone numbers & email | 33/200 | 16.50% | 74.50% | 15.50% |
| model:openmed-multilingual | eligible | Addresses & locations | 357/483 | 73.91% | 79.09% | 73.08% |
| model:openmed-multilingual | eligible | Organizations | 130/579 | 22.45% | 47.50% | 20.38% |
| model:openmed-multilingual | eligible | Network identifiers | 2/7 | 28.57% | 85.71% | 28.57% |
| model:openmed-nemotron | eligible | Documents & identifiers | 59/260 | 22.69% | 39.23% | 16.15% |
| model:openmed-nemotron | eligible | People's names | 1063/1558 | 68.23% | 90.76% | 75.99% |
| model:openmed-nemotron | eligible | Phone numbers & email | 33/200 | 16.50% | 66.00% | 14.00% |
| model:openmed-nemotron | eligible | Addresses & locations | 333/483 | 68.94% | 75.57% | 67.08% |
| model:openmed-nemotron | eligible | Organizations | 90/579 | 15.54% | 28.32% | 12.61% |
| model:openmed-nemotron | eligible | Network identifiers | 1/7 | 14.29% | 57.14% | 14.29% |
| model:opf-kz-ru | eligible | Documents & identifiers | 166/260 | 63.85% | 78.85% | 61.54% |
| model:opf-kz-ru | eligible | People's names | 865/1558 | 55.52% | 59.88% | 53.66% |
| model:opf-kz-ru | eligible | Phone numbers & email | 113/200 | 56.50% | 69.50% | 55.50% |
| model:opf-kz-ru | eligible | Addresses & locations | 152/483 | 31.47% | 33.33% | 30.23% |
| model:opf-kz-ru | eligible | Organizations | 40/579 | 6.91% | 8.81% | 5.70% |
| model:opf-kz-ru | eligible | Network identifiers | 2/7 | 28.57% | 57.14% | 28.57% |
| model:opf-ru | eligible | Documents & identifiers | 97/260 | 37.31% | 65.38% | 18.08% |
| model:opf-ru | eligible | People's names | 1097/1558 | 70.41% | 78.88% | 69.38% |
| model:opf-ru | eligible | Phone numbers & email | 48/200 | 24.00% | 67.50% | 22.50% |
| model:opf-ru | eligible | Addresses & locations | 111/483 | 22.98% | 29.61% | 20.70% |
| model:opf-ru | eligible | Organizations | 42/579 | 7.25% | 10.02% | 5.35% |
| model:opf-ru | eligible | Network identifiers | 0/7 | 0.00% | 42.86% | 0.00% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 97/260 | 37.31% | 58.46% | 24.62% |
| model:opf-ru-v2 | eligible | People's names | 704/1558 | 45.19% | 47.37% | 43.58% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 55/200 | 27.50% | 55.00% | 26.50% |
| model:opf-ru-v2 | eligible | Addresses & locations | 116/483 | 24.02% | 25.26% | 23.40% |
| model:opf-ru-v2 | eligible | Organizations | 25/579 | 4.32% | 5.01% | 3.80% |
| model:opf-ru-v2 | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:opf-ru-v2+ov100 | eligible | Documents & identifiers | 106/260 | 40.77% | 60.00% | 32.31% |
| model:opf-ru-v2+ov100 | eligible | People's names | 737/1558 | 47.30% | 49.55% | 45.70% |
| model:opf-ru-v2+ov100 | eligible | Phone numbers & email | 54/200 | 27.00% | 52.00% | 26.50% |
| model:opf-ru-v2+ov100 | eligible | Addresses & locations | 112/483 | 23.19% | 25.05% | 23.40% |
| model:opf-ru-v2+ov100 | eligible | Organizations | 27/579 | 4.66% | 5.18% | 4.15% |
| model:opf-ru-v2+ov100 | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:opf-ru-v2+sent300 | eligible | Documents & identifiers | 115/260 | 44.23% | 63.85% | 33.85% |
| model:opf-ru-v2+sent300 | eligible | People's names | 676/1558 | 43.39% | 45.64% | 42.49% |
| model:opf-ru-v2+sent300 | eligible | Phone numbers & email | 64/200 | 32.00% | 58.00% | 29.50% |
| model:opf-ru-v2+sent300 | eligible | Addresses & locations | 127/483 | 26.29% | 27.54% | 25.67% |
| model:opf-ru-v2+sent300 | eligible | Organizations | 32/579 | 5.53% | 6.22% | 5.01% |
| model:opf-ru-v2+sent300 | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 40/260 | 15.38% | 33.08% | 8.85% |
| model:pii-shield-onnx | eligible | People's names | 219/1558 | 14.06% | 19.70% | 8.99% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 59/200 | 29.50% | 72.50% | 24.50% |
| model:pii-shield-onnx | eligible | Addresses & locations | 140/483 | 28.99% | 35.20% | 21.12% |
| model:pii-shield-onnx | eligible | Organizations | 85/579 | 14.68% | 22.97% | 11.23% |
| model:pii-shield-onnx | eligible | Network identifiers | 2/7 | 28.57% | 57.14% | 28.57% |
| model:pplx | eligible | Documents & identifiers | 190/260 | 73.08% | 82.31% | 73.08% |
| model:pplx | eligible | People's names | 1450/1558 | 93.07% | 96.66% | 93.07% |
| model:pplx | eligible | Phone numbers & email | 120/200 | 60.00% | 77.50% | 60.00% |
| model:pplx | eligible | Addresses & locations | 352/483 | 72.88% | 74.12% | 72.88% |
| model:pplx | eligible | Organizations | 74/579 | 12.78% | 17.79% | 12.78% |
| model:pplx | eligible | Network identifiers | 6/7 | 85.71% | 100.00% | 85.71% |
| model:pplx+ov100 | eligible | Documents & identifiers | 195/260 | 75.00% | 83.85% | 75.00% |
| model:pplx+ov100 | eligible | People's names | 1459/1558 | 93.65% | 96.66% | 93.65% |
| model:pplx+ov100 | eligible | Phone numbers & email | 125/200 | 62.50% | 78.00% | 62.50% |
| model:pplx+ov100 | eligible | Addresses & locations | 346/483 | 71.64% | 72.46% | 71.22% |
| model:pplx+ov100 | eligible | Organizations | 73/579 | 12.61% | 17.10% | 12.61% |
| model:pplx+ov100 | eligible | Network identifiers | 5/7 | 71.43% | 85.71% | 71.43% |
| model:pplx+sent300 | eligible | Documents & identifiers | 192/260 | 73.85% | 83.08% | 73.85% |
| model:pplx+sent300 | eligible | People's names | 1414/1558 | 90.76% | 95.89% | 90.44% |
| model:pplx+sent300 | eligible | Phone numbers & email | 114/200 | 57.00% | 77.00% | 57.00% |
| model:pplx+sent300 | eligible | Addresses & locations | 355/483 | 73.50% | 74.53% | 73.50% |
| model:pplx+sent300 | eligible | Organizations | 80/579 | 13.82% | 19.17% | 13.82% |
| model:pplx+sent300 | eligible | Network identifiers | 5/7 | 71.43% | 85.71% | 71.43% |
| model:ru-legal-ner | eligible | Documents & identifiers | 30/260 | 11.54% | 34.62% | 2.69% |
| model:ru-legal-ner | eligible | People's names | 102/1558 | 6.55% | 9.69% | 3.98% |
| model:ru-legal-ner | eligible | Phone numbers & email | 23/200 | 11.50% | 58.50% | 6.00% |
| model:ru-legal-ner | eligible | Addresses & locations | 34/483 | 7.04% | 11.80% | 3.93% |
| model:ru-legal-ner | eligible | Organizations | 12/579 | 2.07% | 6.39% | 0.52% |
| model:ru-legal-ner | eligible | Network identifiers | 0/7 | 0.00% | 42.86% | 0.00% |
| model:ru-legal-ner+ov100 | eligible | Documents & identifiers | 38/260 | 14.62% | 41.54% | 4.62% |
| model:ru-legal-ner+ov100 | eligible | People's names | 126/1558 | 8.09% | 12.32% | 4.62% |
| model:ru-legal-ner+ov100 | eligible | Phone numbers & email | 28/200 | 14.00% | 60.50% | 8.00% |
| model:ru-legal-ner+ov100 | eligible | Addresses & locations | 30/483 | 6.21% | 11.18% | 3.73% |
| model:ru-legal-ner+ov100 | eligible | Organizations | 10/579 | 1.73% | 4.66% | 1.04% |
| model:ru-legal-ner+ov100 | eligible | Network identifiers | 0/7 | 0.00% | 28.57% | 0.00% |
| model:ru-legal-ner+sent300 | eligible | Documents & identifiers | 50/260 | 19.23% | 41.92% | 4.62% |
| model:ru-legal-ner+sent300 | eligible | People's names | 293/1558 | 18.81% | 24.45% | 11.30% |
| model:ru-legal-ner+sent300 | eligible | Phone numbers & email | 47/200 | 23.50% | 65.50% | 15.00% |
| model:ru-legal-ner+sent300 | eligible | Addresses & locations | 76/483 | 15.73% | 22.98% | 9.73% |
| model:ru-legal-ner+sent300 | eligible | Organizations | 48/579 | 8.29% | 17.96% | 3.63% |
| model:ru-legal-ner+sent300 | eligible | Network identifiers | 0/7 | 0.00% | 100.00% | 0.00% |
| model:ru-pii-ner | eligible | Documents & identifiers | 151/260 | 58.08% | 68.08% | 58.08% |
| model:ru-pii-ner | eligible | People's names | 1198/1558 | 76.89% | 80.81% | 76.89% |
| model:ru-pii-ner | eligible | Phone numbers & email | 96/200 | 48.00% | 67.00% | 47.00% |
| model:ru-pii-ner | eligible | Addresses & locations | 175/483 | 36.23% | 36.44% | 36.23% |
| model:ru-pii-ner | eligible | Organizations | 39/579 | 6.74% | 7.25% | 6.74% |
| model:ru-pii-ner | eligible | Network identifiers | 0/7 | 0.00% | 14.29% | 0.00% |
| model:rules-ru | eligible | Documents & identifiers | 1/260 | 0.38% | 1.15% | 0.38% |
| model:rules-ru | eligible | People's names | 0/1558 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 7/200 | 3.50% | 50.50% | 3.50% |
| model:rules-ru | eligible | Addresses & locations | 0/483 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Organizations | 0/579 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Network identifiers | 2/7 | 28.57% | 85.71% | 28.57% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/260 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 4/1558 | 0.26% | 0.26% | 0.26% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/200 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Addresses & locations | 0/483 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Organizations | 0/579 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 2/260 | 0.77% | 2.31% | 0.77% |
| model:spacy-ru-lg | eligible | People's names | 346/1558 | 22.21% | 22.53% | 22.21% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 6/200 | 3.00% | 4.00% | 3.00% |
| model:spacy-ru-lg | eligible | Addresses & locations | 50/483 | 10.35% | 11.59% | 10.35% |
| model:spacy-ru-lg | eligible | Organizations | 20/579 | 3.45% | 3.80% | 3.45% |
| model:spacy-ru-lg | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:stanza-ru | eligible | Documents & identifiers | 82/260 | 31.54% | 55.38% | 31.15% |
| model:stanza-ru | eligible | People's names | 1442/1558 | 92.55% | 94.22% | 92.55% |
| model:stanza-ru | eligible | Phone numbers & email | 30/200 | 15.00% | 22.00% | 15.00% |
| model:stanza-ru | eligible | Addresses & locations | 420/483 | 86.96% | 88.82% | 86.75% |
| model:stanza-ru | eligible | Organizations | 459/579 | 79.27% | 82.38% | 79.27% |
| model:stanza-ru | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
| model:traciora | eligible | Documents & identifiers | 67/260 | 25.77% | 49.62% | 10.77% |
| model:traciora | eligible | People's names | 890/1558 | 57.12% | 61.17% | 55.58% |
| model:traciora | eligible | Phone numbers & email | 87/200 | 43.50% | 59.50% | 41.50% |
| model:traciora | eligible | Addresses & locations | 151/483 | 31.26% | 33.75% | 30.64% |
| model:traciora | eligible | Organizations | 49/579 | 8.46% | 11.74% | 6.04% |
| model:traciora | eligible | Network identifiers | 0/7 | 0.00% | 0.00% | 0.00% |
