# redact-multi: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/redact-multi.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 19/32 | 59.38% | 65.62% | 59.38% |
| composition:fastino | eligible | Bank accounts & cards | 51/138 | 36.96% | 54.35% | 36.96% |
| composition:fastino | eligible | Documents & identifiers | 699/829 | 84.32% | 86.01% | 84.20% |
| composition:fastino | eligible | People's names | 9534/10870 | 87.71% | 90.93% | 87.69% |
| composition:fastino | eligible | Phone numbers & email | 2445/2524 | 96.87% | 98.69% | 96.59% |
| composition:fastino | eligible | Addresses & locations | 1416/2107 | 67.20% | 89.56% | 66.92% |
| composition:fastino | eligible | Dates & times | 611/628 | 97.29% | 98.73% | 97.29% |
| composition:fastino | eligible | Organizations | 850/1017 | 83.58% | 90.46% | 83.38% |
| composition:fastino | eligible | Network identifiers | 100/111 | 90.09% | 91.89% | 90.09% |
| composition:fastino | eligible | Customer & employee IDs | 1344/2669 | 50.36% | 51.70% | 50.24% |
| composition:fastino | eligible | Other sensitive attributes | 975/1939 | 50.28% | 63.74% | 50.03% |
| composition:pplx | eligible | Passwords, keys & tokens | 29/32 | 90.62% | 96.88% | 90.62% |
| composition:pplx | eligible | Bank accounts & cards | 69/138 | 50.00% | 98.55% | 47.83% |
| composition:pplx | eligible | Documents & identifiers | 799/829 | 96.38% | 99.03% | 94.81% |
| composition:pplx | eligible | People's names | 10711/10870 | 98.54% | 99.47% | 94.70% |
| composition:pplx | eligible | Phone numbers & email | 2466/2524 | 97.70% | 99.45% | 96.59% |
| composition:pplx | eligible | Addresses & locations | 1559/2107 | 73.99% | 77.12% | 72.24% |
| composition:pplx | eligible | Dates & times | 615/628 | 97.93% | 100.00% | 96.18% |
| composition:pplx | eligible | Organizations | 65/1017 | 6.39% | 9.24% | 5.90% |
| composition:pplx | eligible | Network identifiers | 107/111 | 96.40% | 99.10% | 93.69% |
| composition:pplx | eligible | Customer & employee IDs | 2539/2669 | 95.13% | 96.63% | 93.67% |
| composition:pplx | eligible | Other sensitive attributes | 929/1939 | 47.91% | 56.27% | 44.46% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 29/32 | 90.62% | 96.88% | 90.62% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 75/138 | 54.35% | 98.55% | 52.17% |
| composition:pplx+fastino | eligible | Documents & identifiers | 806/829 | 97.23% | 99.40% | 95.90% |
| composition:pplx+fastino | eligible | People's names | 10754/10870 | 98.93% | 99.74% | 96.05% |
| composition:pplx+fastino | eligible | Phone numbers & email | 2484/2524 | 98.42% | 99.80% | 97.70% |
| composition:pplx+fastino | eligible | Addresses & locations | 1955/2107 | 92.79% | 96.92% | 91.46% |
| composition:pplx+fastino | eligible | Dates & times | 619/628 | 98.57% | 100.00% | 97.29% |
| composition:pplx+fastino | eligible | Organizations | 876/1017 | 86.14% | 92.53% | 85.55% |
| composition:pplx+fastino | eligible | Network identifiers | 110/111 | 99.10% | 100.00% | 96.40% |
| composition:pplx+fastino | eligible | Customer & employee IDs | 2579/2669 | 96.63% | 97.68% | 95.50% |
| composition:pplx+fastino | eligible | Other sensitive attributes | 1227/1939 | 63.28% | 77.26% | 60.39% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 29/32 | 90.62% | 96.88% | 90.62% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 79/138 | 57.25% | 98.55% | 55.07% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 811/829 | 97.83% | 99.52% | 96.50% |
| composition:pplx+fastino+bardsai | eligible | People's names | 10768/10870 | 99.06% | 99.83% | 96.54% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 2485/2524 | 98.45% | 99.84% | 97.74% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 2018/2107 | 95.78% | 99.15% | 93.17% |
| composition:pplx+fastino+bardsai | eligible | Dates & times | 623/628 | 99.20% | 100.00% | 97.93% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 978/1017 | 96.17% | 99.21% | 93.31% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 110/111 | 99.10% | 100.00% | 96.40% |
| composition:pplx+fastino+bardsai | eligible | Customer & employee IDs | 2620/2669 | 98.16% | 99.66% | 96.74% |
| composition:pplx+fastino+bardsai | eligible | Other sensitive attributes | 1288/1939 | 66.43% | 80.40% | 62.76% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 29/32 | 90.62% | 96.88% | 90.62% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 81/138 | 58.70% | 100.00% | 55.80% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 811/829 | 97.83% | 99.88% | 96.74% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 10776/10870 | 99.14% | 99.87% | 97.24% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 2489/2524 | 98.61% | 100.00% | 97.78% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 2027/2107 | 96.20% | 99.67% | 93.36% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Dates & times | 623/628 | 99.20% | 100.00% | 97.93% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 987/1017 | 97.05% | 99.90% | 94.30% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 110/111 | 99.10% | 100.00% | 96.40% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Customer & employee IDs | 2626/2669 | 98.39% | 99.96% | 96.97% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Other sensitive attributes | 1332/1939 | 68.70% | 86.38% | 63.28% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 29/32 | 90.62% | 96.88% | 90.62% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 78/138 | 56.52% | 100.00% | 53.62% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 808/829 | 97.47% | 99.88% | 96.26% |
| composition:pplx+fastino+mmbert | eligible | People's names | 10766/10870 | 99.04% | 99.84% | 96.33% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 2488/2524 | 98.57% | 100.00% | 97.74% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 1993/2107 | 94.59% | 99.34% | 92.03% |
| composition:pplx+fastino+mmbert | eligible | Dates & times | 621/628 | 98.89% | 100.00% | 97.29% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 913/1017 | 89.77% | 99.21% | 87.32% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 110/111 | 99.10% | 100.00% | 96.40% |
| composition:pplx+fastino+mmbert | eligible | Customer & employee IDs | 2586/2669 | 96.89% | 99.81% | 95.54% |
| composition:pplx+fastino+mmbert | eligible | Other sensitive attributes | 1283/1939 | 66.17% | 84.79% | 60.91% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 26/32 | 81.25% | 93.75% | 81.25% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Bank accounts & cards | 37/138 | 26.81% | 58.70% | 24.64% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 706/829 | 85.16% | 92.64% | 78.65% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 9637/10870 | 88.66% | 95.54% | 85.96% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 2437/2524 | 96.55% | 99.29% | 95.44% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 1091/2107 | 51.78% | 73.75% | 50.78% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Dates & times | 571/628 | 90.92% | 94.59% | 90.29% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 107/1017 | 10.52% | 22.62% | 9.44% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 104/111 | 93.69% | 98.20% | 90.99% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Customer & employee IDs | 1600/2669 | 59.95% | 74.86% | 56.73% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Other sensitive attributes | 609/1939 | 31.41% | 38.94% | 29.09% |
| model:apararti | eligible | Passwords, keys & tokens | 24/32 | 75.00% | 87.50% | 56.25% |
| model:apararti | eligible | Bank accounts & cards | 61/138 | 44.20% | 64.49% | 37.68% |
| model:apararti | eligible | Documents & identifiers | 754/829 | 90.95% | 96.98% | 87.58% |
| model:apararti | eligible | People's names | 8143/10870 | 74.91% | 78.33% | 69.25% |
| model:apararti | eligible | Phone numbers & email | 2405/2524 | 95.29% | 98.53% | 93.74% |
| model:apararti | eligible | Addresses & locations | 1058/2107 | 50.21% | 61.51% | 46.70% |
| model:apararti | eligible | Dates & times | 580/628 | 92.36% | 97.93% | 89.49% |
| model:apararti | eligible | Organizations | 145/1017 | 14.26% | 25.66% | 11.70% |
| model:apararti | eligible | Network identifiers | 89/111 | 80.18% | 90.99% | 73.87% |
| model:apararti | eligible | Customer & employee IDs | 2092/2669 | 78.38% | 87.56% | 70.96% |
| model:apararti | eligible | Other sensitive attributes | 269/1939 | 13.87% | 21.14% | 9.28% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 16/32 | 50.00% | 78.12% | 40.62% |
| model:bardsai-eu | eligible | Bank accounts & cards | 38/138 | 27.54% | 41.30% | 18.84% |
| model:bardsai-eu | eligible | Documents & identifiers | 709/829 | 85.52% | 90.47% | 75.63% |
| model:bardsai-eu | eligible | People's names | 10299/10870 | 94.75% | 97.76% | 89.79% |
| model:bardsai-eu | eligible | Phone numbers & email | 1269/2524 | 50.28% | 98.30% | 40.73% |
| model:bardsai-eu | eligible | Addresses & locations | 1716/2107 | 81.44% | 95.63% | 75.65% |
| model:bardsai-eu | eligible | Dates & times | 589/628 | 93.79% | 97.45% | 91.08% |
| model:bardsai-eu | eligible | Organizations | 880/1017 | 86.53% | 93.51% | 80.73% |
| model:bardsai-eu | eligible | Network identifiers | 66/111 | 59.46% | 82.88% | 45.95% |
| model:bardsai-eu | eligible | Customer & employee IDs | 1946/2669 | 72.91% | 89.77% | 61.90% |
| model:bardsai-eu | eligible | Other sensitive attributes | 758/1939 | 39.09% | 48.94% | 32.08% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/32 | 0.00% | 3.12% | 0.00% |
| model:davlan-mbert | eligible | Bank accounts & cards | 1/138 | 0.72% | 1.45% | 0.72% |
| model:davlan-mbert | eligible | Documents & identifiers | 2/829 | 0.24% | 0.84% | 0.00% |
| model:davlan-mbert | eligible | People's names | 10069/10870 | 92.63% | 96.77% | 86.64% |
| model:davlan-mbert | eligible | Phone numbers & email | 9/2524 | 0.36% | 9.03% | 0.12% |
| model:davlan-mbert | eligible | Addresses & locations | 1270/2107 | 60.28% | 95.35% | 55.62% |
| model:davlan-mbert | eligible | Dates & times | 1/628 | 0.16% | 0.16% | 0.00% |
| model:davlan-mbert | eligible | Organizations | 727/1017 | 71.48% | 91.54% | 65.39% |
| model:davlan-mbert | eligible | Network identifiers | 0/111 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Customer & employee IDs | 28/2669 | 1.05% | 4.87% | 0.04% |
| model:davlan-mbert | eligible | Other sensitive attributes | 181/1939 | 9.33% | 14.29% | 6.09% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/32 | 0.00% | 3.12% | 0.00% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 0/138 | 0.00% | 1.45% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 3/829 | 0.36% | 0.97% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 10276/10870 | 94.54% | 97.97% | 89.48% |
| model:davlan-xlmr | eligible | Phone numbers & email | 5/2524 | 0.20% | 25.28% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 1293/2107 | 61.37% | 95.54% | 56.95% |
| model:davlan-xlmr | eligible | Dates & times | 1/628 | 0.16% | 0.16% | 0.00% |
| model:davlan-xlmr | eligible | Organizations | 887/1017 | 87.22% | 95.97% | 82.79% |
| model:davlan-xlmr | eligible | Network identifiers | 0/111 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Customer & employee IDs | 42/2669 | 1.57% | 5.43% | 0.86% |
| model:davlan-xlmr | eligible | Other sensitive attributes | 186/1939 | 9.59% | 14.49% | 6.70% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 8/32 | 25.00% | 37.50% | 21.88% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 0/138 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 15/829 | 1.81% | 2.05% | 1.45% |
| model:fef2-secret-ru | eligible | People's names | 1329/10870 | 12.23% | 14.33% | 10.29% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 819/2524 | 32.45% | 47.98% | 29.36% |
| model:fef2-secret-ru | eligible | Addresses & locations | 32/2107 | 1.52% | 4.27% | 0.90% |
| model:fef2-secret-ru | eligible | Dates & times | 0/628 | 0.00% | 0.16% | 0.00% |
| model:fef2-secret-ru | eligible | Organizations | 43/1017 | 4.23% | 8.16% | 4.13% |
| model:fef2-secret-ru | eligible | Network identifiers | 0/111 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Customer & employee IDs | 419/2669 | 15.70% | 21.51% | 12.78% |
| model:fef2-secret-ru | eligible | Other sensitive attributes | 13/1939 | 0.67% | 1.03% | 0.41% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 6/32 | 18.75% | 31.25% | 18.75% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 10/138 | 7.25% | 10.87% | 7.25% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 83/829 | 10.01% | 10.74% | 10.01% |
| model:gliner-multi-v21 | eligible | People's names | 9735/10870 | 89.56% | 90.29% | 89.48% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 647/2524 | 25.63% | 47.74% | 25.63% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 1114/2107 | 52.87% | 84.86% | 52.59% |
| model:gliner-multi-v21 | eligible | Dates & times | 451/628 | 71.82% | 72.93% | 71.82% |
| model:gliner-multi-v21 | eligible | Organizations | 844/1017 | 82.99% | 90.76% | 82.79% |
| model:gliner-multi-v21 | eligible | Network identifiers | 68/111 | 61.26% | 62.16% | 61.26% |
| model:gliner-multi-v21 | eligible | Customer & employee IDs | 269/2669 | 10.08% | 13.53% | 10.08% |
| model:gliner-multi-v21 | eligible | Other sensitive attributes | 620/1939 | 31.98% | 40.07% | 31.82% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 24/32 | 75.00% | 84.38% | 75.00% |
| model:gliner-nvidia | eligible | Bank accounts & cards | 30/138 | 21.74% | 41.30% | 21.74% |
| model:gliner-nvidia | eligible | Documents & identifiers | 543/829 | 65.50% | 68.28% | 65.50% |
| model:gliner-nvidia | eligible | People's names | 6793/10870 | 62.49% | 91.63% | 61.04% |
| model:gliner-nvidia | eligible | Phone numbers & email | 2031/2524 | 80.47% | 97.27% | 80.39% |
| model:gliner-nvidia | eligible | Addresses & locations | 1198/2107 | 56.86% | 87.76% | 56.81% |
| model:gliner-nvidia | eligible | Dates & times | 570/628 | 90.76% | 93.79% | 90.76% |
| model:gliner-nvidia | eligible | Organizations | 710/1017 | 69.81% | 81.51% | 69.81% |
| model:gliner-nvidia | eligible | Network identifiers | 99/111 | 89.19% | 91.89% | 89.19% |
| model:gliner-nvidia | eligible | Customer & employee IDs | 1466/2669 | 54.93% | 57.29% | 54.85% |
| model:gliner-nvidia | eligible | Other sensitive attributes | 750/1939 | 38.68% | 48.53% | 38.63% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 4/32 | 12.50% | 18.75% | 12.50% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 18/138 | 13.04% | 15.22% | 13.04% |
| model:gliner-pii-base | eligible | Documents & identifiers | 336/829 | 40.53% | 41.38% | 40.53% |
| model:gliner-pii-base | eligible | People's names | 853/10870 | 7.85% | 13.19% | 7.85% |
| model:gliner-pii-base | eligible | Phone numbers & email | 2097/2524 | 83.08% | 86.13% | 83.04% |
| model:gliner-pii-base | eligible | Addresses & locations | 959/2107 | 45.51% | 60.32% | 45.42% |
| model:gliner-pii-base | eligible | Dates & times | 200/628 | 31.85% | 32.96% | 31.85% |
| model:gliner-pii-base | eligible | Organizations | 568/1017 | 55.85% | 68.83% | 55.85% |
| model:gliner-pii-base | eligible | Network identifiers | 98/111 | 88.29% | 91.89% | 88.29% |
| model:gliner-pii-base | eligible | Customer & employee IDs | 828/2669 | 31.02% | 31.66% | 30.84% |
| model:gliner-pii-base | eligible | Other sensitive attributes | 425/1939 | 21.92% | 30.27% | 21.82% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 13/32 | 40.62% | 71.88% | 40.62% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 50/138 | 36.23% | 56.52% | 36.23% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 415/829 | 50.06% | 51.75% | 50.06% |
| model:gliner-pii-edge | eligible | People's names | 3175/10870 | 29.21% | 31.40% | 29.02% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 2095/2524 | 83.00% | 88.00% | 82.96% |
| model:gliner-pii-edge | eligible | Addresses & locations | 1114/2107 | 52.87% | 68.72% | 52.87% |
| model:gliner-pii-edge | eligible | Dates & times | 255/628 | 40.61% | 41.88% | 40.61% |
| model:gliner-pii-edge | eligible | Organizations | 506/1017 | 49.75% | 58.80% | 49.66% |
| model:gliner-pii-edge | eligible | Network identifiers | 98/111 | 88.29% | 91.89% | 88.29% |
| model:gliner-pii-edge | eligible | Customer & employee IDs | 1253/2669 | 46.95% | 49.34% | 46.80% |
| model:gliner-pii-edge | eligible | Other sensitive attributes | 568/1939 | 29.29% | 41.88% | 29.19% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 1/32 | 3.12% | 18.75% | 3.12% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 17/138 | 12.32% | 39.86% | 12.32% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 280/829 | 33.78% | 41.25% | 33.66% |
| model:gliner-stream-pii | eligible | People's names | 4105/10870 | 37.76% | 53.73% | 37.34% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 1079/2524 | 42.75% | 51.03% | 42.75% |
| model:gliner-stream-pii | eligible | Addresses & locations | 639/2107 | 30.33% | 43.14% | 30.33% |
| model:gliner-stream-pii | eligible | Dates & times | 410/628 | 65.29% | 71.34% | 65.29% |
| model:gliner-stream-pii | eligible | Organizations | 274/1017 | 26.94% | 36.38% | 26.84% |
| model:gliner-stream-pii | eligible | Network identifiers | 84/111 | 75.68% | 77.48% | 75.68% |
| model:gliner-stream-pii | eligible | Customer & employee IDs | 826/2669 | 30.95% | 33.98% | 30.91% |
| model:gliner-stream-pii | eligible | Other sensitive attributes | 472/1939 | 24.34% | 32.75% | 24.24% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 20/32 | 62.50% | 71.88% | 62.50% |
| model:gliner-urchade | eligible | Bank accounts & cards | 49/138 | 35.51% | 55.80% | 35.51% |
| model:gliner-urchade | eligible | Documents & identifiers | 586/829 | 70.69% | 72.01% | 70.69% |
| model:gliner-urchade | eligible | People's names | 10168/10870 | 93.54% | 93.89% | 93.50% |
| model:gliner-urchade | eligible | Phone numbers & email | 2406/2524 | 95.32% | 97.62% | 95.29% |
| model:gliner-urchade | eligible | Addresses & locations | 1603/2107 | 76.08% | 84.01% | 76.08% |
| model:gliner-urchade | eligible | Dates & times | 558/628 | 88.85% | 91.56% | 88.85% |
| model:gliner-urchade | eligible | Organizations | 914/1017 | 89.87% | 91.45% | 89.87% |
| model:gliner-urchade | eligible | Network identifiers | 101/111 | 90.99% | 91.89% | 90.99% |
| model:gliner-urchade | eligible | Customer & employee IDs | 1308/2669 | 49.01% | 49.49% | 48.89% |
| model:gliner-urchade | eligible | Other sensitive attributes | 1039/1939 | 53.58% | 65.24% | 53.48% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 19/32 | 59.38% | 65.62% | 59.38% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 51/138 | 36.96% | 54.35% | 36.96% |
| model:gliner2-fastino | eligible | Documents & identifiers | 699/829 | 84.32% | 86.01% | 84.20% |
| model:gliner2-fastino | eligible | People's names | 9534/10870 | 87.71% | 90.93% | 87.69% |
| model:gliner2-fastino | eligible | Phone numbers & email | 2445/2524 | 96.87% | 98.69% | 96.59% |
| model:gliner2-fastino | eligible | Addresses & locations | 1416/2107 | 67.20% | 89.56% | 66.92% |
| model:gliner2-fastino | eligible | Dates & times | 611/628 | 97.29% | 98.73% | 97.29% |
| model:gliner2-fastino | eligible | Organizations | 850/1017 | 83.58% | 90.46% | 83.38% |
| model:gliner2-fastino | eligible | Network identifiers | 100/111 | 90.09% | 91.89% | 90.09% |
| model:gliner2-fastino | eligible | Customer & employee IDs | 1344/2669 | 50.36% | 51.70% | 50.24% |
| model:gliner2-fastino | eligible | Other sensitive attributes | 975/1939 | 50.28% | 63.74% | 50.03% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 20/32 | 62.50% | 71.88% | 62.50% |
| model:gliner2-hivetrace-omni | eligible | Bank accounts & cards | 73/138 | 52.90% | 71.74% | 52.90% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 646/829 | 77.93% | 79.61% | 77.93% |
| model:gliner2-hivetrace-omni | eligible | People's names | 9510/10870 | 87.49% | 91.01% | 87.47% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 2434/2524 | 96.43% | 98.22% | 96.16% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 1338/2107 | 63.50% | 88.09% | 63.50% |
| model:gliner2-hivetrace-omni | eligible | Dates & times | 585/628 | 93.15% | 95.22% | 93.15% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 825/1017 | 81.12% | 87.51% | 81.12% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 97/111 | 87.39% | 89.19% | 87.39% |
| model:gliner2-hivetrace-omni | eligible | Customer & employee IDs | 1520/2669 | 56.95% | 57.92% | 56.95% |
| model:gliner2-hivetrace-omni | eligible | Other sensitive attributes | 887/1939 | 45.75% | 55.13% | 45.64% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 14/32 | 43.75% | 53.12% | 43.75% |
| model:gliner2-hivetrace-uni | eligible | Bank accounts & cards | 47/138 | 34.06% | 53.62% | 34.06% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 704/829 | 84.92% | 88.66% | 84.92% |
| model:gliner2-hivetrace-uni | eligible | People's names | 9218/10870 | 84.80% | 87.26% | 84.78% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 2403/2524 | 95.21% | 97.42% | 94.93% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 1424/2107 | 67.58% | 83.44% | 67.54% |
| model:gliner2-hivetrace-uni | eligible | Dates & times | 493/628 | 78.50% | 81.21% | 78.50% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 312/1017 | 30.68% | 41.10% | 30.68% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 57/111 | 51.35% | 51.35% | 51.35% |
| model:gliner2-hivetrace-uni | eligible | Customer & employee IDs | 1661/2669 | 62.23% | 64.41% | 62.23% |
| model:gliner2-hivetrace-uni | eligible | Other sensitive attributes | 216/1939 | 11.14% | 16.04% | 11.14% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 7/32 | 21.88% | 31.25% | 21.88% |
| model:gliner2-large | eligible | Bank accounts & cards | 44/138 | 31.88% | 52.90% | 31.88% |
| model:gliner2-large | eligible | Documents & identifiers | 423/829 | 51.03% | 52.71% | 51.03% |
| model:gliner2-large | eligible | People's names | 7029/10870 | 64.66% | 66.85% | 64.64% |
| model:gliner2-large | eligible | Phone numbers & email | 2397/2524 | 94.97% | 96.87% | 94.69% |
| model:gliner2-large | eligible | Addresses & locations | 1151/2107 | 54.63% | 76.17% | 54.58% |
| model:gliner2-large | eligible | Dates & times | 543/628 | 86.46% | 90.29% | 86.46% |
| model:gliner2-large | eligible | Organizations | 728/1017 | 71.58% | 81.61% | 71.58% |
| model:gliner2-large | eligible | Network identifiers | 97/111 | 87.39% | 89.19% | 87.39% |
| model:gliner2-large | eligible | Customer & employee IDs | 1063/2669 | 39.83% | 41.36% | 39.75% |
| model:gliner2-large | eligible | Other sensitive attributes | 771/1939 | 39.76% | 49.10% | 39.66% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 14/32 | 43.75% | 50.00% | 43.75% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 6/138 | 4.35% | 6.52% | 4.35% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 153/829 | 18.46% | 18.82% | 18.46% |
| model:gliner2-vladlinv | eligible | People's names | 7322/10870 | 67.36% | 69.55% | 67.30% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 2104/2524 | 83.36% | 84.59% | 83.12% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 615/2107 | 29.19% | 30.47% | 29.19% |
| model:gliner2-vladlinv | eligible | Dates & times | 580/628 | 92.36% | 93.95% | 92.36% |
| model:gliner2-vladlinv | eligible | Organizations | 9/1017 | 0.88% | 1.67% | 0.88% |
| model:gliner2-vladlinv | eligible | Network identifiers | 21/111 | 18.92% | 19.82% | 18.92% |
| model:gliner2-vladlinv | eligible | Customer & employee IDs | 362/2669 | 13.56% | 14.01% | 13.56% |
| model:gliner2-vladlinv | eligible | Other sensitive attributes | 80/1939 | 4.13% | 5.52% | 4.13% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 3/32 | 9.38% | 12.50% | 9.38% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 16/138 | 11.59% | 13.77% | 11.59% |
| model:gliner25-fastino | eligible | Documents & identifiers | 116/829 | 13.99% | 14.60% | 13.99% |
| model:gliner25-fastino | eligible | People's names | 9725/10870 | 89.47% | 91.30% | 89.45% |
| model:gliner25-fastino | eligible | Phone numbers & email | 2420/2524 | 95.88% | 97.54% | 95.60% |
| model:gliner25-fastino | eligible | Addresses & locations | 1411/2107 | 66.97% | 85.81% | 66.87% |
| model:gliner25-fastino | eligible | Dates & times | 65/628 | 10.35% | 10.51% | 10.35% |
| model:gliner25-fastino | eligible | Organizations | 831/1017 | 81.71% | 88.59% | 81.71% |
| model:gliner25-fastino | eligible | Network identifiers | 94/111 | 84.68% | 86.49% | 84.68% |
| model:gliner25-fastino | eligible | Customer & employee IDs | 285/2669 | 10.68% | 11.58% | 10.68% |
| model:gliner25-fastino | eligible | Other sensitive attributes | 491/1939 | 25.32% | 32.28% | 25.32% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 11/32 | 34.38% | 56.25% | 31.25% |
| model:gravitee-small | eligible | Bank accounts & cards | 35/138 | 25.36% | 37.68% | 23.19% |
| model:gravitee-small | eligible | Documents & identifiers | 369/829 | 44.51% | 48.97% | 41.38% |
| model:gravitee-small | eligible | People's names | 8359/10870 | 76.90% | 79.48% | 72.11% |
| model:gravitee-small | eligible | Phone numbers & email | 2036/2524 | 80.67% | 93.30% | 78.88% |
| model:gravitee-small | eligible | Addresses & locations | 1217/2107 | 57.76% | 70.48% | 52.97% |
| model:gravitee-small | eligible | Dates & times | 534/628 | 85.03% | 89.97% | 80.57% |
| model:gravitee-small | eligible | Organizations | 503/1017 | 49.46% | 65.00% | 44.15% |
| model:gravitee-small | eligible | Network identifiers | 91/111 | 81.98% | 90.99% | 79.28% |
| model:gravitee-small | eligible | Customer & employee IDs | 157/2669 | 5.88% | 9.25% | 4.65% |
| model:gravitee-small | eligible | Other sensitive attributes | 273/1939 | 14.08% | 22.23% | 11.40% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 10/32 | 31.25% | 81.25% | 15.62% |
| model:kalyan-ettin | eligible | Bank accounts & cards | 21/138 | 15.22% | 26.81% | 12.32% |
| model:kalyan-ettin | eligible | Documents & identifiers | 288/829 | 34.74% | 47.89% | 10.13% |
| model:kalyan-ettin | eligible | People's names | 5530/10870 | 50.87% | 77.65% | 55.29% |
| model:kalyan-ettin | eligible | Phone numbers & email | 1905/2524 | 75.48% | 93.86% | 74.29% |
| model:kalyan-ettin | eligible | Addresses & locations | 891/2107 | 42.29% | 75.56% | 35.79% |
| model:kalyan-ettin | eligible | Dates & times | 384/628 | 61.15% | 85.19% | 55.57% |
| model:kalyan-ettin | eligible | Organizations | 219/1017 | 21.53% | 48.57% | 12.49% |
| model:kalyan-ettin | eligible | Network identifiers | 82/111 | 73.87% | 90.09% | 68.47% |
| model:kalyan-ettin | eligible | Customer & employee IDs | 501/2669 | 18.77% | 50.84% | 10.75% |
| model:kalyan-ettin | eligible | Other sensitive attributes | 279/1939 | 14.39% | 20.73% | 7.43% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 11/32 | 34.38% | 93.75% | 12.50% |
| model:mmbert32k | eligible | Bank accounts & cards | 37/138 | 26.81% | 83.33% | 9.42% |
| model:mmbert32k | eligible | Documents & identifiers | 526/829 | 63.45% | 94.09% | 15.92% |
| model:mmbert32k | eligible | People's names | 9889/10870 | 90.98% | 95.84% | 82.52% |
| model:mmbert32k | eligible | Phone numbers & email | 1214/2524 | 48.10% | 99.09% | 35.22% |
| model:mmbert32k | eligible | Addresses & locations | 940/2107 | 44.61% | 71.95% | 29.62% |
| model:mmbert32k | eligible | Dates & times | 535/628 | 85.19% | 100.00% | 72.61% |
| model:mmbert32k | eligible | Organizations | 260/1017 | 25.57% | 84.76% | 16.13% |
| model:mmbert32k | eligible | Network identifiers | 74/111 | 66.67% | 100.00% | 26.13% |
| model:mmbert32k | eligible | Customer & employee IDs | 365/2669 | 13.68% | 94.19% | 2.21% |
| model:mmbert32k | eligible | Other sensitive attributes | 414/1939 | 21.35% | 48.01% | 5.67% |
| model:natasha | eligible | Passwords, keys & tokens | 0/32 | 0.00% | 6.25% | 0.00% |
| model:natasha | eligible | Bank accounts & cards | 0/138 | 0.00% | 0.72% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 16/829 | 1.93% | 1.93% | 1.33% |
| model:natasha | eligible | People's names | 505/10870 | 4.65% | 4.92% | 4.65% |
| model:natasha | eligible | Phone numbers & email | 0/2524 | 0.00% | 0.32% | 0.00% |
| model:natasha | eligible | Addresses & locations | 123/2107 | 5.84% | 12.48% | 5.84% |
| model:natasha | eligible | Dates & times | 0/628 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Organizations | 93/1017 | 9.14% | 12.00% | 9.14% |
| model:natasha | eligible | Network identifiers | 0/111 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Customer & employee IDs | 195/2669 | 7.31% | 8.77% | 7.31% |
| model:natasha | eligible | Other sensitive attributes | 15/1939 | 0.77% | 1.60% | 0.77% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/32 | 0.00% | 6.25% | 0.00% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 0/138 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 1/829 | 0.12% | 0.48% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 6895/10870 | 63.43% | 95.70% | 56.46% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 4/2524 | 0.16% | 27.34% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 1204/2107 | 57.14% | 94.07% | 49.36% |
| model:ner-ru-gherman | eligible | Dates & times | 1/628 | 0.16% | 0.16% | 0.00% |
| model:ner-ru-gherman | eligible | Organizations | 50/1017 | 4.92% | 33.24% | 0.39% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/111 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Customer & employee IDs | 38/2669 | 1.42% | 4.16% | 0.04% |
| model:ner-ru-gherman | eligible | Other sensitive attributes | 148/1939 | 7.63% | 11.24% | 2.63% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 2/32 | 6.25% | 9.38% | 3.12% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 7/138 | 5.07% | 26.09% | 2.90% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 24/829 | 2.90% | 4.58% | 0.72% |
| model:ner-ru-yqelz | eligible | People's names | 8013/10870 | 73.72% | 79.02% | 64.57% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 4/2524 | 0.16% | 12.48% | 0.08% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 1271/2107 | 60.32% | 94.68% | 55.01% |
| model:ner-ru-yqelz | eligible | Dates & times | 7/628 | 1.11% | 1.59% | 0.80% |
| model:ner-ru-yqelz | eligible | Organizations | 664/1017 | 65.29% | 85.84% | 54.77% |
| model:ner-ru-yqelz | eligible | Network identifiers | 1/111 | 0.90% | 2.70% | 0.90% |
| model:ner-ru-yqelz | eligible | Customer & employee IDs | 31/2669 | 1.16% | 5.17% | 0.71% |
| model:ner-ru-yqelz | eligible | Other sensitive attributes | 445/1939 | 22.95% | 39.56% | 16.86% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 19/32 | 59.38% | 75.00% | 59.38% |
| model:nuner-zero | eligible | Bank accounts & cards | 18/138 | 13.04% | 33.33% | 7.97% |
| model:nuner-zero | eligible | Documents & identifiers | 330/829 | 39.81% | 42.34% | 34.14% |
| model:nuner-zero | eligible | People's names | 8707/10870 | 80.10% | 82.01% | 50.88% |
| model:nuner-zero | eligible | Phone numbers & email | 2394/2524 | 94.85% | 97.86% | 65.89% |
| model:nuner-zero | eligible | Addresses & locations | 1569/2107 | 74.47% | 87.71% | 47.18% |
| model:nuner-zero | eligible | Dates & times | 497/628 | 79.14% | 87.10% | 64.65% |
| model:nuner-zero | eligible | Organizations | 798/1017 | 78.47% | 85.94% | 16.22% |
| model:nuner-zero | eligible | Network identifiers | 104/111 | 93.69% | 99.10% | 93.69% |
| model:nuner-zero | eligible | Customer & employee IDs | 1428/2669 | 53.50% | 56.80% | 52.42% |
| model:nuner-zero | eligible | Other sensitive attributes | 924/1939 | 47.65% | 63.90% | 34.76% |
| model:nym-base | eligible | Passwords, keys & tokens | 21/32 | 65.62% | 90.62% | 53.12% |
| model:nym-base | eligible | Bank accounts & cards | 36/138 | 26.09% | 46.38% | 25.36% |
| model:nym-base | eligible | Documents & identifiers | 700/829 | 84.44% | 91.92% | 80.10% |
| model:nym-base | eligible | People's names | 7186/10870 | 66.11% | 96.07% | 87.05% |
| model:nym-base | eligible | Phone numbers & email | 1881/2524 | 74.52% | 95.76% | 72.58% |
| model:nym-base | eligible | Addresses & locations | 1228/2107 | 58.28% | 93.07% | 55.20% |
| model:nym-base | eligible | Dates & times | 586/628 | 93.31% | 100.00% | 89.49% |
| model:nym-base | eligible | Organizations | 739/1017 | 72.66% | 81.51% | 68.93% |
| model:nym-base | eligible | Network identifiers | 45/111 | 40.54% | 51.35% | 28.83% |
| model:nym-base | eligible | Customer & employee IDs | 585/2669 | 21.92% | 29.64% | 18.62% |
| model:nym-base | eligible | Other sensitive attributes | 585/1939 | 30.17% | 38.73% | 24.39% |
| model:nym-small | eligible | Passwords, keys & tokens | 13/32 | 40.62% | 84.38% | 15.62% |
| model:nym-small | eligible | Bank accounts & cards | 41/138 | 29.71% | 70.29% | 26.81% |
| model:nym-small | eligible | Documents & identifiers | 704/829 | 84.92% | 92.28% | 78.77% |
| model:nym-small | eligible | People's names | 6731/10870 | 61.92% | 90.34% | 81.43% |
| model:nym-small | eligible | Phone numbers & email | 2035/2524 | 80.63% | 93.50% | 77.34% |
| model:nym-small | eligible | Addresses & locations | 1223/2107 | 58.04% | 92.88% | 55.53% |
| model:nym-small | eligible | Dates & times | 559/628 | 89.01% | 95.70% | 84.08% |
| model:nym-small | eligible | Organizations | 697/1017 | 68.53% | 81.02% | 65.29% |
| model:nym-small | eligible | Network identifiers | 45/111 | 40.54% | 49.55% | 29.73% |
| model:nym-small | eligible | Customer & employee IDs | 611/2669 | 22.89% | 33.50% | 19.30% |
| model:nym-small | eligible | Other sensitive attributes | 568/1939 | 29.29% | 38.06% | 23.83% |
| model:openai-base | eligible | Passwords, keys & tokens | 25/32 | 78.12% | 87.50% | 65.62% |
| model:openai-base | eligible | Bank accounts & cards | 55/138 | 39.86% | 54.35% | 34.78% |
| model:openai-base | eligible | Documents & identifiers | 711/829 | 85.77% | 90.83% | 82.75% |
| model:openai-base | eligible | People's names | 8885/10870 | 81.74% | 83.22% | 79.02% |
| model:openai-base | eligible | Phone numbers & email | 2385/2524 | 94.49% | 97.07% | 93.03% |
| model:openai-base | eligible | Addresses & locations | 972/2107 | 46.13% | 56.19% | 43.19% |
| model:openai-base | eligible | Dates & times | 547/628 | 87.10% | 90.92% | 85.03% |
| model:openai-base | eligible | Organizations | 119/1017 | 11.70% | 16.81% | 10.13% |
| model:openai-base | eligible | Network identifiers | 66/111 | 59.46% | 70.27% | 53.15% |
| model:openai-base | eligible | Customer & employee IDs | 1612/2669 | 60.40% | 68.30% | 55.86% |
| model:openai-base | eligible | Other sensitive attributes | 209/1939 | 10.78% | 14.75% | 8.56% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 18/32 | 56.25% | 87.50% | 34.38% |
| model:openmed-multilingual | eligible | Bank accounts & cards | 37/138 | 26.81% | 52.17% | 22.46% |
| model:openmed-multilingual | eligible | Documents & identifiers | 650/829 | 78.41% | 86.01% | 69.12% |
| model:openmed-multilingual | eligible | People's names | 6298/10870 | 57.94% | 85.40% | 65.79% |
| model:openmed-multilingual | eligible | Phone numbers & email | 2274/2524 | 90.10% | 98.38% | 87.44% |
| model:openmed-multilingual | eligible | Addresses & locations | 942/2107 | 44.71% | 80.78% | 39.44% |
| model:openmed-multilingual | eligible | Dates & times | 519/628 | 82.64% | 94.11% | 78.18% |
| model:openmed-multilingual | eligible | Organizations | 225/1017 | 22.12% | 47.79% | 14.85% |
| model:openmed-multilingual | eligible | Network identifiers | 86/111 | 77.48% | 93.69% | 71.17% |
| model:openmed-multilingual | eligible | Customer & employee IDs | 1024/2669 | 38.37% | 62.12% | 29.75% |
| model:openmed-multilingual | eligible | Other sensitive attributes | 384/1939 | 19.80% | 32.96% | 12.17% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 15/32 | 46.88% | 81.25% | 18.75% |
| model:openmed-nemotron | eligible | Bank accounts & cards | 23/138 | 16.67% | 41.30% | 10.14% |
| model:openmed-nemotron | eligible | Documents & identifiers | 245/829 | 29.55% | 44.51% | 11.94% |
| model:openmed-nemotron | eligible | People's names | 5982/10870 | 55.03% | 84.66% | 62.55% |
| model:openmed-nemotron | eligible | Phone numbers & email | 2144/2524 | 84.94% | 97.07% | 81.42% |
| model:openmed-nemotron | eligible | Addresses & locations | 689/2107 | 32.70% | 68.01% | 26.86% |
| model:openmed-nemotron | eligible | Dates & times | 469/628 | 74.68% | 87.42% | 67.83% |
| model:openmed-nemotron | eligible | Organizations | 268/1017 | 26.35% | 58.41% | 16.42% |
| model:openmed-nemotron | eligible | Network identifiers | 85/111 | 76.58% | 91.89% | 72.07% |
| model:openmed-nemotron | eligible | Customer & employee IDs | 414/2669 | 15.51% | 36.76% | 10.04% |
| model:openmed-nemotron | eligible | Other sensitive attributes | 300/1939 | 15.47% | 25.32% | 7.68% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 24/32 | 75.00% | 84.38% | 65.62% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 68/138 | 49.28% | 71.01% | 48.55% |
| model:opf-kz-ru | eligible | Documents & identifiers | 750/829 | 90.47% | 95.54% | 88.90% |
| model:opf-kz-ru | eligible | People's names | 7232/10870 | 66.53% | 70.73% | 61.36% |
| model:opf-kz-ru | eligible | Phone numbers & email | 2409/2524 | 95.44% | 98.69% | 93.82% |
| model:opf-kz-ru | eligible | Addresses & locations | 955/2107 | 45.33% | 57.95% | 42.48% |
| model:opf-kz-ru | eligible | Dates & times | 556/628 | 88.54% | 97.29% | 85.51% |
| model:opf-kz-ru | eligible | Organizations | 88/1017 | 8.65% | 17.01% | 6.98% |
| model:opf-kz-ru | eligible | Network identifiers | 81/111 | 72.97% | 87.39% | 58.56% |
| model:opf-kz-ru | eligible | Customer & employee IDs | 2088/2669 | 78.23% | 86.51% | 71.79% |
| model:opf-kz-ru | eligible | Other sensitive attributes | 237/1939 | 12.22% | 17.38% | 8.92% |
| model:opf-ru | eligible | Passwords, keys & tokens | 21/32 | 65.62% | 93.75% | 56.25% |
| model:opf-ru | eligible | Bank accounts & cards | 35/138 | 25.36% | 65.22% | 15.94% |
| model:opf-ru | eligible | Documents & identifiers | 551/829 | 66.47% | 84.92% | 44.99% |
| model:opf-ru | eligible | People's names | 8536/10870 | 78.53% | 87.01% | 71.84% |
| model:opf-ru | eligible | Phone numbers & email | 2241/2524 | 88.79% | 97.70% | 85.22% |
| model:opf-ru | eligible | Addresses & locations | 414/2107 | 19.65% | 54.01% | 14.14% |
| model:opf-ru | eligible | Dates & times | 475/628 | 75.64% | 88.06% | 71.18% |
| model:opf-ru | eligible | Organizations | 96/1017 | 9.44% | 29.40% | 5.90% |
| model:opf-ru | eligible | Network identifiers | 15/111 | 13.51% | 48.65% | 5.41% |
| model:opf-ru | eligible | Customer & employee IDs | 664/2669 | 24.88% | 67.93% | 13.15% |
| model:opf-ru | eligible | Other sensitive attributes | 272/1939 | 14.03% | 25.68% | 6.65% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 20/32 | 62.50% | 78.12% | 46.88% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 30/138 | 21.74% | 40.58% | 18.12% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 543/829 | 65.50% | 83.23% | 48.97% |
| model:opf-ru-v2 | eligible | People's names | 7720/10870 | 71.02% | 73.97% | 66.72% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 2236/2524 | 88.59% | 95.48% | 86.41% |
| model:opf-ru-v2 | eligible | Addresses & locations | 579/2107 | 27.48% | 46.46% | 24.21% |
| model:opf-ru-v2 | eligible | Dates & times | 8/628 | 1.27% | 7.17% | 0.32% |
| model:opf-ru-v2 | eligible | Organizations | 102/1017 | 10.03% | 21.73% | 8.16% |
| model:opf-ru-v2 | eligible | Network identifiers | 97/111 | 87.39% | 93.69% | 81.98% |
| model:opf-ru-v2 | eligible | Customer & employee IDs | 472/2669 | 17.68% | 49.49% | 10.90% |
| model:opf-ru-v2 | eligible | Other sensitive attributes | 162/1939 | 8.35% | 12.64% | 4.38% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 26/32 | 81.25% | 90.62% | 78.12% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 81/138 | 58.70% | 73.91% | 52.90% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 667/829 | 80.46% | 87.33% | 65.98% |
| model:pii-shield-onnx | eligible | People's names | 7381/10870 | 67.90% | 75.46% | 55.79% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 2172/2524 | 86.05% | 98.42% | 81.70% |
| model:pii-shield-onnx | eligible | Addresses & locations | 1230/2107 | 58.38% | 80.97% | 51.40% |
| model:pii-shield-onnx | eligible | Dates & times | 302/628 | 48.09% | 83.28% | 46.34% |
| model:pii-shield-onnx | eligible | Organizations | 553/1017 | 54.38% | 76.20% | 46.12% |
| model:pii-shield-onnx | eligible | Network identifiers | 94/111 | 84.68% | 97.30% | 79.28% |
| model:pii-shield-onnx | eligible | Customer & employee IDs | 2463/2669 | 92.28% | 96.89% | 85.95% |
| model:pii-shield-onnx | eligible | Other sensitive attributes | 1088/1939 | 56.11% | 72.61% | 48.07% |
| model:pplx | eligible | Passwords, keys & tokens | 29/32 | 90.62% | 96.88% | 90.62% |
| model:pplx | eligible | Bank accounts & cards | 69/138 | 50.00% | 98.55% | 47.83% |
| model:pplx | eligible | Documents & identifiers | 799/829 | 96.38% | 99.03% | 94.81% |
| model:pplx | eligible | People's names | 10711/10870 | 98.54% | 99.47% | 94.70% |
| model:pplx | eligible | Phone numbers & email | 2466/2524 | 97.70% | 99.45% | 96.59% |
| model:pplx | eligible | Addresses & locations | 1559/2107 | 73.99% | 77.12% | 72.24% |
| model:pplx | eligible | Dates & times | 615/628 | 97.93% | 100.00% | 96.18% |
| model:pplx | eligible | Organizations | 65/1017 | 6.39% | 9.24% | 5.90% |
| model:pplx | eligible | Network identifiers | 107/111 | 96.40% | 99.10% | 93.69% |
| model:pplx | eligible | Customer & employee IDs | 2539/2669 | 95.13% | 96.63% | 93.67% |
| model:pplx | eligible | Other sensitive attributes | 929/1939 | 47.91% | 56.27% | 44.46% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 12/32 | 37.50% | 87.50% | 18.75% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 55/138 | 39.86% | 76.09% | 28.26% |
| model:ru-legal-ner | eligible | Documents & identifiers | 454/829 | 54.76% | 73.94% | 27.26% |
| model:ru-legal-ner | eligible | People's names | 4357/10870 | 40.08% | 49.47% | 27.18% |
| model:ru-legal-ner | eligible | Phone numbers & email | 1589/2524 | 62.96% | 96.95% | 57.45% |
| model:ru-legal-ner | eligible | Addresses & locations | 757/2107 | 35.93% | 64.02% | 26.58% |
| model:ru-legal-ner | eligible | Dates & times | 274/628 | 43.63% | 69.90% | 40.92% |
| model:ru-legal-ner | eligible | Organizations | 287/1017 | 28.22% | 58.60% | 17.70% |
| model:ru-legal-ner | eligible | Network identifiers | 17/111 | 15.32% | 58.56% | 9.91% |
| model:ru-legal-ner | eligible | Customer & employee IDs | 509/2669 | 19.07% | 69.13% | 9.59% |
| model:ru-legal-ner | eligible | Other sensitive attributes | 672/1939 | 34.66% | 56.63% | 22.12% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 7/32 | 21.88% | 40.62% | 21.88% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 47/138 | 34.06% | 53.62% | 32.61% |
| model:ru-pii-ner | eligible | Documents & identifiers | 632/829 | 76.24% | 78.89% | 74.91% |
| model:ru-pii-ner | eligible | People's names | 7270/10870 | 66.88% | 69.32% | 66.24% |
| model:ru-pii-ner | eligible | Phone numbers & email | 1862/2524 | 73.77% | 77.14% | 72.35% |
| model:ru-pii-ner | eligible | Addresses & locations | 426/2107 | 20.22% | 26.53% | 20.08% |
| model:ru-pii-ner | eligible | Dates & times | 499/628 | 79.46% | 83.60% | 76.91% |
| model:ru-pii-ner | eligible | Organizations | 81/1017 | 7.96% | 10.82% | 7.47% |
| model:ru-pii-ner | eligible | Network identifiers | 35/111 | 31.53% | 31.53% | 27.93% |
| model:ru-pii-ner | eligible | Customer & employee IDs | 1742/2669 | 65.27% | 67.93% | 63.66% |
| model:ru-pii-ner | eligible | Other sensitive attributes | 187/1939 | 9.64% | 12.33% | 8.25% |
| model:rules-ru | eligible | Passwords, keys & tokens | 4/32 | 12.50% | 15.62% | 12.50% |
| model:rules-ru | eligible | Bank accounts & cards | 4/138 | 2.90% | 2.90% | 2.90% |
| model:rules-ru | eligible | Documents & identifiers | 10/829 | 1.21% | 1.21% | 1.21% |
| model:rules-ru | eligible | People's names | 27/10870 | 0.25% | 0.29% | 0.25% |
| model:rules-ru | eligible | Phone numbers & email | 2211/2524 | 87.60% | 88.91% | 87.12% |
| model:rules-ru | eligible | Addresses & locations | 4/2107 | 0.19% | 0.24% | 0.19% |
| model:rules-ru | eligible | Dates & times | 1/628 | 0.16% | 0.16% | 0.16% |
| model:rules-ru | eligible | Organizations | 43/1017 | 4.23% | 6.88% | 4.23% |
| model:rules-ru | eligible | Network identifiers | 88/111 | 79.28% | 81.08% | 76.58% |
| model:rules-ru | eligible | Customer & employee IDs | 147/2669 | 5.51% | 6.41% | 5.40% |
| model:rules-ru | eligible | Other sensitive attributes | 4/1939 | 0.21% | 0.46% | 0.21% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/32 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 0/138 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/829 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 3/10870 | 0.03% | 0.05% | 0.03% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/2524 | 0.00% | 0.12% | 0.00% |
| model:spacy-alrosait | eligible | Addresses & locations | 0/2107 | 0.00% | 0.47% | 0.00% |
| model:spacy-alrosait | eligible | Dates & times | 0/628 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Organizations | 0/1017 | 0.00% | 0.29% | 0.00% |
| model:spacy-alrosait | eligible | Network identifiers | 0/111 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Customer & employee IDs | 0/2669 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Other sensitive attributes | 0/1939 | 0.00% | 0.05% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 2/32 | 6.25% | 9.38% | 6.25% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 0/138 | 0.00% | 0.72% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 17/829 | 2.05% | 2.05% | 2.05% |
| model:spacy-ru-lg | eligible | People's names | 1024/10870 | 9.42% | 10.31% | 9.41% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 38/2524 | 1.51% | 1.66% | 1.51% |
| model:spacy-ru-lg | eligible | Addresses & locations | 176/2107 | 8.35% | 17.70% | 8.31% |
| model:spacy-ru-lg | eligible | Dates & times | 9/628 | 1.43% | 3.66% | 1.43% |
| model:spacy-ru-lg | eligible | Organizations | 145/1017 | 14.26% | 18.78% | 14.16% |
| model:spacy-ru-lg | eligible | Network identifiers | 2/111 | 1.80% | 1.80% | 1.80% |
| model:spacy-ru-lg | eligible | Customer & employee IDs | 43/2669 | 1.61% | 1.80% | 1.61% |
| model:spacy-ru-lg | eligible | Other sensitive attributes | 104/1939 | 5.36% | 7.68% | 5.36% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 3/32 | 9.38% | 31.25% | 9.38% |
| model:stanza-ru | eligible | Bank accounts & cards | 6/138 | 4.35% | 11.59% | 3.62% |
| model:stanza-ru | eligible | Documents & identifiers | 67/829 | 8.08% | 11.22% | 7.12% |
| model:stanza-ru | eligible | People's names | 7546/10870 | 69.42% | 71.56% | 69.02% |
| model:stanza-ru | eligible | Phone numbers & email | 107/2524 | 4.24% | 5.19% | 4.24% |
| model:stanza-ru | eligible | Addresses & locations | 874/2107 | 41.48% | 68.34% | 41.29% |
| model:stanza-ru | eligible | Dates & times | 10/628 | 1.59% | 4.62% | 1.27% |
| model:stanza-ru | eligible | Organizations | 533/1017 | 52.41% | 68.14% | 52.31% |
| model:stanza-ru | eligible | Network identifiers | 2/111 | 1.80% | 4.50% | 1.80% |
| model:stanza-ru | eligible | Customer & employee IDs | 130/2669 | 4.87% | 41.48% | 4.20% |
| model:stanza-ru | eligible | Other sensitive attributes | 417/1939 | 21.51% | 32.80% | 20.63% |
| model:traciora | eligible | Passwords, keys & tokens | 18/32 | 56.25% | 75.00% | 40.62% |
| model:traciora | eligible | Bank accounts & cards | 16/138 | 11.59% | 25.36% | 10.87% |
| model:traciora | eligible | Documents & identifiers | 403/829 | 48.61% | 64.05% | 27.14% |
| model:traciora | eligible | People's names | 7386/10870 | 67.95% | 72.64% | 61.57% |
| model:traciora | eligible | Phone numbers & email | 2275/2524 | 90.13% | 96.12% | 86.89% |
| model:traciora | eligible | Addresses & locations | 895/2107 | 42.48% | 55.20% | 37.92% |
| model:traciora | eligible | Dates & times | 31/628 | 4.94% | 30.25% | 1.11% |
| model:traciora | eligible | Organizations | 112/1017 | 11.01% | 23.89% | 8.55% |
| model:traciora | eligible | Network identifiers | 61/111 | 54.95% | 76.58% | 51.35% |
| model:traciora | eligible | Customer & employee IDs | 575/2669 | 21.54% | 38.10% | 14.91% |
| model:traciora | eligible | Other sensitive attributes | 183/1939 | 9.44% | 13.77% | 5.26% |
