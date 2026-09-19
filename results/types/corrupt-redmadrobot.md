# corrupt-redmadrobot: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/corrupt-redmadrobot.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Bank accounts & cards | 182/203 | 89.66% | 90.64% | 88.18% |
| composition:fastino | eligible | Documents & identifiers | 1177/2076 | 56.70% | 59.44% | 56.55% |
| composition:fastino | eligible | People's names | 831/1260 | 65.95% | 70.95% | 65.87% |
| composition:fastino | eligible | Phone numbers & email | 284/389 | 73.01% | 91.77% | 72.24% |
| composition:fastino | eligible | Addresses & locations | 853/1242 | 68.68% | 78.42% | 68.44% |
| composition:fastino | eligible | Network identifiers | 113/361 | 31.30% | 54.29% | 30.75% |
| composition:pplx | eligible | Bank accounts & cards | 166/203 | 81.77% | 99.51% | 79.31% |
| composition:pplx | eligible | Documents & identifiers | 1774/2076 | 85.45% | 96.82% | 82.95% |
| composition:pplx | eligible | People's names | 1125/1260 | 89.29% | 90.87% | 84.84% |
| composition:pplx | eligible | Phone numbers & email | 321/389 | 82.52% | 98.71% | 81.49% |
| composition:pplx | eligible | Addresses & locations | 751/1242 | 60.47% | 64.41% | 57.97% |
| composition:pplx | eligible | Network identifiers | 213/361 | 59.00% | 67.04% | 56.79% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 195/203 | 96.06% | 100.00% | 96.06% |
| composition:pplx+fastino | eligible | Documents & identifiers | 1852/2076 | 89.21% | 97.83% | 87.62% |
| composition:pplx+fastino | eligible | People's names | 1188/1260 | 94.29% | 96.35% | 92.22% |
| composition:pplx+fastino | eligible | Phone numbers & email | 355/389 | 91.26% | 100.00% | 90.75% |
| composition:pplx+fastino | eligible | Addresses & locations | 1080/1242 | 86.96% | 92.35% | 86.63% |
| composition:pplx+fastino | eligible | Network identifiers | 241/361 | 66.76% | 85.60% | 64.82% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 198/203 | 97.54% | 100.00% | 97.54% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 1877/2076 | 90.41% | 97.88% | 88.82% |
| composition:pplx+fastino+bardsai | eligible | People's names | 1202/1260 | 95.40% | 97.54% | 93.49% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 358/389 | 92.03% | 100.00% | 91.52% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 1125/1242 | 90.58% | 95.33% | 90.02% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 241/361 | 66.76% | 90.03% | 65.10% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 198/203 | 97.54% | 100.00% | 97.54% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 1890/2076 | 91.04% | 98.55% | 89.21% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 1216/1260 | 96.51% | 98.65% | 94.13% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 359/389 | 92.29% | 100.00% | 91.52% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 1148/1242 | 92.43% | 97.18% | 90.98% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 257/361 | 71.19% | 98.06% | 68.98% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 195/203 | 96.06% | 100.00% | 96.06% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 1868/2076 | 89.98% | 98.55% | 88.05% |
| composition:pplx+fastino+mmbert | eligible | People's names | 1211/1260 | 96.11% | 98.17% | 93.41% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 356/389 | 91.52% | 100.00% | 90.75% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 1115/1242 | 89.77% | 95.49% | 87.76% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 253/361 | 70.08% | 98.06% | 67.59% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Bank accounts & cards | 139/203 | 68.47% | 87.19% | 65.02% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 1316/2076 | 63.39% | 77.41% | 57.03% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 1006/1260 | 79.84% | 84.84% | 75.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 304/389 | 78.15% | 94.86% | 77.63% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 595/1242 | 47.91% | 58.13% | 44.77% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 161/361 | 44.60% | 60.66% | 41.00% |
| model:apararti | eligible | Bank accounts & cards | 138/203 | 67.98% | 91.63% | 70.94% |
| model:apararti | eligible | Documents & identifiers | 1407/2076 | 67.77% | 82.13% | 62.43% |
| model:apararti | eligible | People's names | 868/1260 | 68.89% | 71.27% | 59.60% |
| model:apararti | eligible | Phone numbers & email | 253/389 | 65.04% | 87.40% | 67.10% |
| model:apararti | eligible | Addresses & locations | 508/1242 | 40.90% | 52.98% | 34.70% |
| model:apararti | eligible | Network identifiers | 195/361 | 54.02% | 68.14% | 50.14% |
| model:bardsai-eu | eligible | Bank accounts & cards | 104/203 | 51.23% | 69.95% | 39.41% |
| model:bardsai-eu | eligible | Documents & identifiers | 967/2076 | 46.58% | 53.52% | 39.55% |
| model:bardsai-eu | eligible | People's names | 937/1260 | 74.37% | 76.83% | 67.46% |
| model:bardsai-eu | eligible | Phone numbers & email | 127/389 | 32.65% | 86.89% | 29.05% |
| model:bardsai-eu | eligible | Addresses & locations | 709/1242 | 57.09% | 66.02% | 48.79% |
| model:bardsai-eu | eligible | Network identifiers | 106/361 | 29.36% | 55.40% | 24.65% |
| model:davlan-mbert | eligible | Bank accounts & cards | 0/203 | 0.00% | 0.49% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 0/2076 | 0.00% | 0.10% | 0.00% |
| model:davlan-mbert | eligible | People's names | 1028/1260 | 81.59% | 83.33% | 70.16% |
| model:davlan-mbert | eligible | Phone numbers & email | 1/389 | 0.26% | 4.11% | 0.26% |
| model:davlan-mbert | eligible | Addresses & locations | 772/1242 | 62.16% | 71.74% | 53.06% |
| model:davlan-mbert | eligible | Network identifiers | 2/361 | 0.55% | 11.36% | 0.55% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 0/203 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 2/2076 | 0.10% | 0.34% | 0.05% |
| model:davlan-xlmr | eligible | People's names | 1059/1260 | 84.05% | 88.10% | 76.59% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/389 | 0.00% | 3.60% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 784/1242 | 63.12% | 78.34% | 56.12% |
| model:davlan-xlmr | eligible | Network identifiers | 2/361 | 0.55% | 2.77% | 0.55% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 89/203 | 43.84% | 54.68% | 39.41% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 763/2076 | 36.75% | 42.10% | 32.18% |
| model:fef2-secret-ru | eligible | People's names | 880/1260 | 69.84% | 70.87% | 66.35% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 128/389 | 32.90% | 50.39% | 28.79% |
| model:fef2-secret-ru | eligible | Addresses & locations | 599/1242 | 48.23% | 59.50% | 42.83% |
| model:fef2-secret-ru | eligible | Network identifiers | 7/361 | 1.94% | 7.76% | 1.66% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 6/203 | 2.96% | 3.94% | 2.96% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 44/2076 | 2.12% | 2.22% | 2.12% |
| model:gliner-multi-v21 | eligible | People's names | 636/1260 | 50.48% | 52.22% | 50.48% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 31/389 | 7.97% | 21.08% | 7.46% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 606/1242 | 48.79% | 54.35% | 48.63% |
| model:gliner-multi-v21 | eligible | Network identifiers | 62/361 | 17.17% | 37.95% | 17.17% |
| model:gliner-multi-v21-ru | eligible | Bank accounts & cards | 7/203 | 3.45% | 4.43% | 3.45% |
| model:gliner-multi-v21-ru | eligible | Documents & identifiers | 168/2076 | 8.09% | 8.29% | 8.09% |
| model:gliner-multi-v21-ru | eligible | People's names | 672/1260 | 53.33% | 55.40% | 53.33% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 31/389 | 7.97% | 22.37% | 6.17% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 606/1242 | 48.79% | 54.27% | 48.71% |
| model:gliner-multi-v21-ru | eligible | Network identifiers | 61/361 | 16.90% | 30.19% | 16.62% |
| model:gliner-nvidia | eligible | Bank accounts & cards | 135/203 | 66.50% | 68.97% | 66.50% |
| model:gliner-nvidia | eligible | Documents & identifiers | 862/2076 | 41.52% | 42.97% | 41.52% |
| model:gliner-nvidia | eligible | People's names | 965/1260 | 76.59% | 80.71% | 76.59% |
| model:gliner-nvidia | eligible | Phone numbers & email | 334/389 | 85.86% | 88.69% | 85.86% |
| model:gliner-nvidia | eligible | Addresses & locations | 748/1242 | 60.23% | 71.01% | 60.14% |
| model:gliner-nvidia | eligible | Network identifiers | 219/361 | 60.66% | 61.50% | 60.66% |
| model:gliner-nvidia+homoglyph | eligible | Bank accounts & cards | 135/203 | 66.50% | 68.97% | 66.50% |
| model:gliner-nvidia+homoglyph | eligible | Documents & identifiers | 862/2076 | 41.52% | 42.97% | 41.52% |
| model:gliner-nvidia+homoglyph | eligible | People's names | 997/1260 | 79.13% | 83.25% | 79.13% |
| model:gliner-nvidia+homoglyph | eligible | Phone numbers & email | 333/389 | 85.60% | 88.17% | 85.35% |
| model:gliner-nvidia+homoglyph | eligible | Addresses & locations | 778/1242 | 62.64% | 73.51% | 62.56% |
| model:gliner-nvidia+homoglyph | eligible | Network identifiers | 220/361 | 60.94% | 61.77% | 60.94% |
| model:gliner-nvidia-ru | eligible | Bank accounts & cards | 165/203 | 81.28% | 83.74% | 81.28% |
| model:gliner-nvidia-ru | eligible | Documents & identifiers | 1256/2076 | 60.50% | 61.75% | 60.50% |
| model:gliner-nvidia-ru | eligible | People's names | 911/1260 | 72.30% | 75.63% | 72.30% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 328/389 | 84.32% | 86.89% | 84.32% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 727/1242 | 58.53% | 71.01% | 58.45% |
| model:gliner-nvidia-ru | eligible | Network identifiers | 226/361 | 62.60% | 63.71% | 62.60% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 83/203 | 40.89% | 41.38% | 40.89% |
| model:gliner-pii-base | eligible | Documents & identifiers | 452/2076 | 21.77% | 22.01% | 21.77% |
| model:gliner-pii-base | eligible | People's names | 551/1260 | 43.73% | 46.43% | 43.73% |
| model:gliner-pii-base | eligible | Phone numbers & email | 273/389 | 70.18% | 73.26% | 69.92% |
| model:gliner-pii-base | eligible | Addresses & locations | 278/1242 | 22.38% | 30.84% | 22.14% |
| model:gliner-pii-base | eligible | Network identifiers | 170/361 | 47.09% | 57.06% | 47.09% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 158/203 | 77.83% | 84.24% | 77.83% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 1319/2076 | 63.54% | 67.05% | 63.20% |
| model:gliner-pii-edge | eligible | People's names | 553/1260 | 43.89% | 46.35% | 43.81% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 251/389 | 64.52% | 72.24% | 64.01% |
| model:gliner-pii-edge | eligible | Addresses & locations | 344/1242 | 27.70% | 41.63% | 27.21% |
| model:gliner-pii-edge | eligible | Network identifiers | 166/361 | 45.98% | 66.76% | 45.43% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 27/203 | 13.30% | 84.24% | 12.32% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 525/2076 | 25.29% | 51.49% | 24.61% |
| model:gliner-stream-pii | eligible | People's names | 566/1260 | 44.92% | 51.27% | 44.92% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 161/389 | 41.39% | 62.47% | 41.39% |
| model:gliner-stream-pii | eligible | Addresses & locations | 389/1242 | 31.32% | 53.70% | 31.24% |
| model:gliner-stream-pii | eligible | Network identifiers | 128/361 | 35.46% | 57.89% | 35.18% |
| model:gliner-urchade | eligible | Bank accounts & cards | 165/203 | 81.28% | 81.77% | 80.79% |
| model:gliner-urchade | eligible | Documents & identifiers | 1220/2076 | 58.77% | 60.12% | 58.77% |
| model:gliner-urchade | eligible | People's names | 238/1260 | 18.89% | 19.60% | 18.89% |
| model:gliner-urchade | eligible | Phone numbers & email | 334/389 | 85.86% | 88.95% | 85.60% |
| model:gliner-urchade | eligible | Addresses & locations | 804/1242 | 64.73% | 69.48% | 64.65% |
| model:gliner-urchade | eligible | Network identifiers | 190/361 | 52.63% | 62.33% | 52.63% |
| model:gliner-urchade-ru | eligible | Bank accounts & cards | 146/203 | 71.92% | 72.41% | 71.43% |
| model:gliner-urchade-ru | eligible | Documents & identifiers | 1429/2076 | 68.83% | 70.18% | 68.83% |
| model:gliner-urchade-ru | eligible | People's names | 141/1260 | 11.19% | 11.51% | 11.11% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 303/389 | 77.89% | 79.95% | 77.89% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 818/1242 | 65.86% | 69.57% | 65.70% |
| model:gliner-urchade-ru | eligible | Network identifiers | 162/361 | 44.88% | 49.58% | 44.88% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 182/203 | 89.66% | 90.64% | 88.18% |
| model:gliner2-fastino | eligible | Documents & identifiers | 1177/2076 | 56.70% | 59.44% | 56.55% |
| model:gliner2-fastino | eligible | People's names | 831/1260 | 65.95% | 70.95% | 65.87% |
| model:gliner2-fastino | eligible | Phone numbers & email | 284/389 | 73.01% | 91.77% | 72.24% |
| model:gliner2-fastino | eligible | Addresses & locations | 853/1242 | 68.68% | 78.42% | 68.44% |
| model:gliner2-fastino | eligible | Network identifiers | 113/361 | 31.30% | 54.29% | 30.75% |
| model:gliner2-fastino-ru | eligible | Bank accounts & cards | 180/203 | 88.67% | 88.67% | 87.19% |
| model:gliner2-fastino-ru | eligible | Documents & identifiers | 1468/2076 | 70.71% | 72.88% | 70.28% |
| model:gliner2-fastino-ru | eligible | People's names | 946/1260 | 75.08% | 77.06% | 74.92% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 302/389 | 77.63% | 90.23% | 77.38% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 873/1242 | 70.29% | 79.07% | 69.97% |
| model:gliner2-fastino-ru | eligible | Network identifiers | 114/361 | 31.58% | 45.15% | 31.02% |
| model:gliner2-hivetrace-omni | eligible | Bank accounts & cards | 179/203 | 88.18% | 88.18% | 87.68% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 844/2076 | 40.66% | 42.68% | 40.66% |
| model:gliner2-hivetrace-omni | eligible | People's names | 778/1260 | 61.75% | 67.94% | 61.75% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 295/389 | 75.84% | 83.29% | 75.84% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 682/1242 | 54.91% | 73.67% | 54.83% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 115/361 | 31.86% | 36.57% | 31.58% |
| model:gliner2-hivetrace-omni-ru | eligible | Bank accounts & cards | 178/203 | 87.68% | 87.68% | 87.19% |
| model:gliner2-hivetrace-omni-ru | eligible | Documents & identifiers | 1178/2076 | 56.74% | 58.82% | 56.65% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 728/1260 | 57.78% | 60.40% | 57.78% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 315/389 | 80.98% | 87.40% | 80.98% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 664/1242 | 53.46% | 75.52% | 53.38% |
| model:gliner2-hivetrace-omni-ru | eligible | Network identifiers | 118/361 | 32.69% | 36.29% | 32.41% |
| model:gliner2-hivetrace-uni | eligible | Bank accounts & cards | 50/203 | 24.63% | 33.50% | 23.65% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 1143/2076 | 55.06% | 61.85% | 54.43% |
| model:gliner2-hivetrace-uni | eligible | People's names | 447/1260 | 35.48% | 38.81% | 35.48% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 234/389 | 60.15% | 77.63% | 60.15% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 647/1242 | 52.09% | 66.99% | 52.01% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 13/361 | 3.60% | 9.97% | 3.60% |
| model:gliner2-hivetrace-uni-ru | eligible | Bank accounts & cards | 12/203 | 5.91% | 5.91% | 5.91% |
| model:gliner2-hivetrace-uni-ru | eligible | Documents & identifiers | 494/2076 | 23.80% | 25.63% | 23.75% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 465/1260 | 36.90% | 38.65% | 36.90% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 24/389 | 6.17% | 12.08% | 6.17% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 354/1242 | 28.50% | 34.54% | 28.50% |
| model:gliner2-hivetrace-uni-ru | eligible | Network identifiers | 4/361 | 1.11% | 2.49% | 1.11% |
| model:gliner2-large | eligible | Bank accounts & cards | 137/203 | 67.49% | 72.91% | 67.00% |
| model:gliner2-large | eligible | Documents & identifiers | 972/2076 | 46.82% | 49.95% | 46.48% |
| model:gliner2-large | eligible | People's names | 608/1260 | 48.25% | 50.00% | 48.25% |
| model:gliner2-large | eligible | Phone numbers & email | 310/389 | 79.69% | 87.15% | 79.69% |
| model:gliner2-large | eligible | Addresses & locations | 602/1242 | 48.47% | 57.41% | 48.31% |
| model:gliner2-large | eligible | Network identifiers | 149/361 | 41.27% | 57.34% | 41.00% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 76/203 | 37.44% | 37.93% | 36.95% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 1170/2076 | 56.36% | 57.37% | 56.17% |
| model:gliner2-vladlinv | eligible | People's names | 615/1260 | 48.81% | 50.24% | 48.81% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 253/389 | 65.04% | 66.84% | 64.52% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 138/1242 | 11.11% | 11.43% | 11.11% |
| model:gliner2-vladlinv | eligible | Network identifiers | 33/361 | 9.14% | 9.70% | 9.14% |
| model:gliner2-vladlinv+homoglyph | eligible | Bank accounts & cards | 76/203 | 37.44% | 37.93% | 36.95% |
| model:gliner2-vladlinv+homoglyph | eligible | Documents & identifiers | 1164/2076 | 56.07% | 57.03% | 55.88% |
| model:gliner2-vladlinv+homoglyph | eligible | People's names | 659/1260 | 52.30% | 53.81% | 52.30% |
| model:gliner2-vladlinv+homoglyph | eligible | Phone numbers & email | 254/389 | 65.30% | 66.84% | 64.78% |
| model:gliner2-vladlinv+homoglyph | eligible | Addresses & locations | 158/1242 | 12.72% | 13.12% | 12.72% |
| model:gliner2-vladlinv+homoglyph | eligible | Network identifiers | 33/361 | 9.14% | 9.70% | 9.14% |
| model:gliner2-vladlinv-ru | eligible | Bank accounts & cards | 139/203 | 68.47% | 69.95% | 68.47% |
| model:gliner2-vladlinv-ru | eligible | Documents & identifiers | 1510/2076 | 72.74% | 74.08% | 72.21% |
| model:gliner2-vladlinv-ru | eligible | People's names | 582/1260 | 46.19% | 47.38% | 46.19% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 249/389 | 64.01% | 66.32% | 63.50% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 153/1242 | 12.32% | 12.64% | 12.32% |
| model:gliner2-vladlinv-ru | eligible | Network identifiers | 16/361 | 4.43% | 4.99% | 4.43% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 96/203 | 47.29% | 49.75% | 46.80% |
| model:gliner25-fastino | eligible | Documents & identifiers | 466/2076 | 22.45% | 23.84% | 22.25% |
| model:gliner25-fastino | eligible | People's names | 617/1260 | 48.97% | 53.25% | 48.89% |
| model:gliner25-fastino | eligible | Phone numbers & email | 267/389 | 68.64% | 81.49% | 68.38% |
| model:gliner25-fastino | eligible | Addresses & locations | 283/1242 | 22.79% | 26.17% | 22.79% |
| model:gliner25-fastino | eligible | Network identifiers | 92/361 | 25.48% | 32.13% | 24.38% |
| model:gliner25-fastino-ru | eligible | Bank accounts & cards | 151/203 | 74.38% | 78.33% | 72.41% |
| model:gliner25-fastino-ru | eligible | Documents & identifiers | 1185/2076 | 57.08% | 60.36% | 56.02% |
| model:gliner25-fastino-ru | eligible | People's names | 721/1260 | 57.22% | 59.13% | 57.22% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 269/389 | 69.15% | 79.43% | 68.38% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 213/1242 | 17.15% | 19.00% | 17.15% |
| model:gliner25-fastino-ru | eligible | Network identifiers | 86/361 | 23.82% | 26.04% | 22.99% |
| model:gravitee-small | eligible | Bank accounts & cards | 140/203 | 68.97% | 91.13% | 62.07% |
| model:gravitee-small | eligible | Documents & identifiers | 794/2076 | 38.25% | 44.46% | 33.91% |
| model:gravitee-small | eligible | People's names | 797/1260 | 63.25% | 64.21% | 57.38% |
| model:gravitee-small | eligible | Phone numbers & email | 265/389 | 68.12% | 86.89% | 64.52% |
| model:gravitee-small | eligible | Addresses & locations | 671/1242 | 54.03% | 60.63% | 46.30% |
| model:gravitee-small | eligible | Network identifiers | 264/361 | 73.13% | 92.24% | 68.14% |
| model:kalyan-ettin | eligible | Bank accounts & cards | 39/203 | 19.21% | 52.71% | 11.82% |
| model:kalyan-ettin | eligible | Documents & identifiers | 440/2076 | 21.19% | 28.71% | 9.92% |
| model:kalyan-ettin | eligible | People's names | 654/1260 | 51.90% | 55.24% | 28.65% |
| model:kalyan-ettin | eligible | Phone numbers & email | 136/389 | 34.96% | 64.27% | 26.74% |
| model:kalyan-ettin | eligible | Addresses & locations | 270/1242 | 21.74% | 38.57% | 9.82% |
| model:kalyan-ettin | eligible | Network identifiers | 139/361 | 38.50% | 79.22% | 32.96% |
| model:mmbert32k | eligible | Bank accounts & cards | 68/203 | 33.50% | 97.54% | 24.14% |
| model:mmbert32k | eligible | Documents & identifiers | 1065/2076 | 51.30% | 78.18% | 16.91% |
| model:mmbert32k | eligible | People's names | 865/1260 | 68.65% | 75.87% | 36.35% |
| model:mmbert32k | eligible | Phone numbers & email | 149/389 | 38.30% | 84.32% | 26.99% |
| model:mmbert32k | eligible | Addresses & locations | 574/1242 | 46.22% | 76.73% | 25.36% |
| model:mmbert32k | eligible | Network identifiers | 99/361 | 27.42% | 90.86% | 17.17% |
| model:natasha | eligible | Bank accounts & cards | 0/203 | 0.00% | 0.49% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 33/2076 | 1.59% | 3.76% | 1.54% |
| model:natasha | eligible | People's names | 534/1260 | 42.38% | 43.41% | 36.11% |
| model:natasha | eligible | Phone numbers & email | 3/389 | 0.77% | 4.37% | 0.77% |
| model:natasha | eligible | Addresses & locations | 465/1242 | 37.44% | 44.85% | 34.70% |
| model:natasha | eligible | Network identifiers | 4/361 | 1.11% | 2.49% | 1.11% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 0/203 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 5/2076 | 0.24% | 0.63% | 0.10% |
| model:ner-ru-gherman | eligible | People's names | 1063/1260 | 84.37% | 86.03% | 66.19% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/389 | 0.00% | 21.08% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 627/1242 | 50.48% | 81.32% | 33.66% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/361 | 0.00% | 0.83% | 0.00% |
| model:ner-ru-gherman+homoglyph | eligible | Bank accounts & cards | 0/203 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+homoglyph | eligible | Documents & identifiers | 5/2076 | 0.24% | 0.63% | 0.10% |
| model:ner-ru-gherman+homoglyph | eligible | People's names | 1077/1260 | 85.48% | 87.14% | 73.17% |
| model:ner-ru-gherman+homoglyph | eligible | Phone numbers & email | 0/389 | 0.00% | 21.34% | 0.00% |
| model:ner-ru-gherman+homoglyph | eligible | Addresses & locations | 646/1242 | 52.01% | 83.25% | 36.63% |
| model:ner-ru-gherman+homoglyph | eligible | Network identifiers | 0/361 | 0.00% | 0.83% | 0.00% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 14/203 | 6.90% | 32.02% | 2.46% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 212/2076 | 10.21% | 17.82% | 8.09% |
| model:ner-ru-yqelz | eligible | People's names | 847/1260 | 67.22% | 70.00% | 56.11% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 9/389 | 2.31% | 28.28% | 1.80% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 711/1242 | 57.25% | 67.15% | 50.97% |
| model:ner-ru-yqelz | eligible | Network identifiers | 6/361 | 1.66% | 21.33% | 0.28% |
| model:nuner-zero | eligible | Bank accounts & cards | 94/203 | 46.31% | 78.82% | 14.78% |
| model:nuner-zero | eligible | Documents & identifiers | 804/2076 | 38.73% | 47.06% | 29.91% |
| model:nuner-zero | eligible | People's names | 416/1260 | 33.02% | 35.71% | 33.02% |
| model:nuner-zero | eligible | Phone numbers & email | 339/389 | 87.15% | 96.14% | 40.36% |
| model:nuner-zero | eligible | Addresses & locations | 564/1242 | 45.41% | 60.14% | 26.41% |
| model:nuner-zero | eligible | Network identifiers | 326/361 | 90.30% | 99.45% | 81.16% |
| model:nym-base | eligible | Bank accounts & cards | 151/203 | 74.38% | 96.06% | 66.01% |
| model:nym-base | eligible | Documents & identifiers | 1383/2076 | 66.62% | 79.29% | 54.34% |
| model:nym-base | eligible | People's names | 1097/1260 | 87.06% | 89.68% | 81.27% |
| model:nym-base | eligible | Phone numbers & email | 298/389 | 76.61% | 95.63% | 74.29% |
| model:nym-base | eligible | Addresses & locations | 757/1242 | 60.95% | 75.44% | 57.81% |
| model:nym-base | eligible | Network identifiers | 256/361 | 70.91% | 86.43% | 66.20% |
| model:nym-base+homoglyph | eligible | Bank accounts & cards | 151/203 | 74.38% | 96.06% | 66.01% |
| model:nym-base+homoglyph | eligible | Documents & identifiers | 1384/2076 | 66.67% | 79.34% | 54.38% |
| model:nym-base+homoglyph | eligible | People's names | 1107/1260 | 87.86% | 90.48% | 83.41% |
| model:nym-base+homoglyph | eligible | Phone numbers & email | 295/389 | 75.84% | 95.37% | 73.78% |
| model:nym-base+homoglyph | eligible | Addresses & locations | 788/1242 | 63.45% | 77.46% | 60.63% |
| model:nym-base+homoglyph | eligible | Network identifiers | 259/361 | 71.75% | 86.98% | 67.87% |
| model:nym-small | eligible | Bank accounts & cards | 120/203 | 59.11% | 96.06% | 53.69% |
| model:nym-small | eligible | Documents & identifiers | 1168/2076 | 56.26% | 73.41% | 47.59% |
| model:nym-small | eligible | People's names | 996/1260 | 79.05% | 83.02% | 71.19% |
| model:nym-small | eligible | Phone numbers & email | 283/389 | 72.75% | 97.17% | 70.18% |
| model:nym-small | eligible | Addresses & locations | 667/1242 | 53.70% | 73.59% | 49.28% |
| model:nym-small | eligible | Network identifiers | 214/361 | 59.28% | 78.39% | 52.08% |
| model:openai-base | eligible | Bank accounts & cards | 131/203 | 64.53% | 76.85% | 63.05% |
| model:openai-base | eligible | Documents & identifiers | 1142/2076 | 55.01% | 65.22% | 53.61% |
| model:openai-base | eligible | People's names | 795/1260 | 63.10% | 64.60% | 58.41% |
| model:openai-base | eligible | Phone numbers & email | 243/389 | 62.47% | 81.23% | 63.24% |
| model:openai-base | eligible | Addresses & locations | 414/1242 | 33.33% | 38.89% | 31.16% |
| model:openai-base | eligible | Network identifiers | 141/361 | 39.06% | 44.32% | 37.67% |
| model:openmed-multilingual | eligible | Bank accounts & cards | 110/203 | 54.19% | 92.12% | 44.33% |
| model:openmed-multilingual | eligible | Documents & identifiers | 692/2076 | 33.33% | 50.05% | 22.93% |
| model:openmed-multilingual | eligible | People's names | 552/1260 | 43.81% | 47.06% | 26.67% |
| model:openmed-multilingual | eligible | Phone numbers & email | 166/389 | 42.67% | 80.21% | 40.10% |
| model:openmed-multilingual | eligible | Addresses & locations | 242/1242 | 19.48% | 38.00% | 11.27% |
| model:openmed-multilingual | eligible | Network identifiers | 237/361 | 65.65% | 86.15% | 58.17% |
| model:openmed-nemotron | eligible | Bank accounts & cards | 78/203 | 38.42% | 64.53% | 27.59% |
| model:openmed-nemotron | eligible | Documents & identifiers | 273/2076 | 13.15% | 22.64% | 5.92% |
| model:openmed-nemotron | eligible | People's names | 775/1260 | 61.51% | 66.43% | 32.94% |
| model:openmed-nemotron | eligible | Phone numbers & email | 123/389 | 31.62% | 72.75% | 26.99% |
| model:openmed-nemotron | eligible | Addresses & locations | 381/1242 | 30.68% | 54.03% | 18.84% |
| model:openmed-nemotron | eligible | Network identifiers | 194/361 | 53.74% | 81.16% | 47.09% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 131/203 | 64.53% | 90.15% | 64.04% |
| model:opf-kz-ru | eligible | Documents & identifiers | 1445/2076 | 69.61% | 84.68% | 68.11% |
| model:opf-kz-ru | eligible | People's names | 711/1260 | 56.43% | 58.97% | 44.76% |
| model:opf-kz-ru | eligible | Phone numbers & email | 248/389 | 63.75% | 90.49% | 64.52% |
| model:opf-kz-ru | eligible | Addresses & locations | 283/1242 | 22.79% | 36.31% | 17.71% |
| model:opf-kz-ru | eligible | Network identifiers | 184/361 | 50.97% | 67.31% | 41.00% |
| model:opf-ru | eligible | Bank accounts & cards | 52/203 | 25.62% | 71.92% | 21.18% |
| model:opf-ru | eligible | Documents & identifiers | 867/2076 | 41.76% | 65.70% | 28.76% |
| model:opf-ru | eligible | People's names | 822/1260 | 65.24% | 69.44% | 51.27% |
| model:opf-ru | eligible | Phone numbers & email | 197/389 | 50.64% | 90.75% | 48.59% |
| model:opf-ru | eligible | Addresses & locations | 377/1242 | 30.35% | 52.74% | 21.50% |
| model:opf-ru | eligible | Network identifiers | 23/361 | 6.37% | 57.89% | 1.39% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 108/203 | 53.20% | 78.33% | 49.26% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 1027/2076 | 49.47% | 68.83% | 41.14% |
| model:opf-ru-v2 | eligible | People's names | 677/1260 | 53.73% | 57.46% | 41.27% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 205/389 | 52.70% | 77.38% | 52.19% |
| model:opf-ru-v2 | eligible | Addresses & locations | 336/1242 | 27.05% | 38.08% | 22.71% |
| model:opf-ru-v2 | eligible | Network identifiers | 98/361 | 27.15% | 44.32% | 23.27% |
| model:opf-ru-v2+homoglyph | eligible | Bank accounts & cards | 110/203 | 54.19% | 77.83% | 49.26% |
| model:opf-ru-v2+homoglyph | eligible | Documents & identifiers | 1031/2076 | 49.66% | 68.88% | 41.18% |
| model:opf-ru-v2+homoglyph | eligible | People's names | 705/1260 | 55.95% | 59.60% | 45.71% |
| model:opf-ru-v2+homoglyph | eligible | Phone numbers & email | 204/389 | 52.44% | 77.12% | 52.70% |
| model:opf-ru-v2+homoglyph | eligible | Addresses & locations | 329/1242 | 26.49% | 36.96% | 23.43% |
| model:opf-ru-v2+homoglyph | eligible | Network identifiers | 94/361 | 26.04% | 44.32% | 23.27% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 113/203 | 55.67% | 81.28% | 42.86% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 867/2076 | 41.76% | 54.09% | 33.62% |
| model:pii-shield-onnx | eligible | People's names | 884/1260 | 70.16% | 74.52% | 56.83% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 316/389 | 81.23% | 96.14% | 76.35% |
| model:pii-shield-onnx | eligible | Addresses & locations | 634/1242 | 51.05% | 68.52% | 39.77% |
| model:pii-shield-onnx | eligible | Network identifiers | 195/361 | 54.02% | 83.38% | 47.37% |
| model:pplx | eligible | Bank accounts & cards | 166/203 | 81.77% | 99.51% | 79.31% |
| model:pplx | eligible | Documents & identifiers | 1774/2076 | 85.45% | 96.82% | 82.95% |
| model:pplx | eligible | People's names | 1125/1260 | 89.29% | 90.87% | 84.84% |
| model:pplx | eligible | Phone numbers & email | 321/389 | 82.52% | 98.71% | 81.49% |
| model:pplx | eligible | Addresses & locations | 751/1242 | 60.47% | 64.41% | 57.97% |
| model:pplx | eligible | Network identifiers | 213/361 | 59.00% | 67.04% | 56.79% |
| model:pplx+homoglyph | eligible | Bank accounts & cards | 166/203 | 81.77% | 99.51% | 79.31% |
| model:pplx+homoglyph | eligible | Documents & identifiers | 1779/2076 | 85.69% | 97.06% | 83.04% |
| model:pplx+homoglyph | eligible | People's names | 1120/1260 | 88.89% | 90.48% | 84.92% |
| model:pplx+homoglyph | eligible | Phone numbers & email | 320/389 | 82.26% | 98.71% | 81.75% |
| model:pplx+homoglyph | eligible | Addresses & locations | 751/1242 | 60.47% | 64.49% | 57.73% |
| model:pplx+homoglyph | eligible | Network identifiers | 215/361 | 59.56% | 67.59% | 57.34% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 115/203 | 56.65% | 82.27% | 31.53% |
| model:ru-legal-ner | eligible | Documents & identifiers | 1355/2076 | 65.27% | 79.14% | 54.48% |
| model:ru-legal-ner | eligible | People's names | 916/1260 | 72.70% | 74.37% | 57.46% |
| model:ru-legal-ner | eligible | Phone numbers & email | 264/389 | 67.87% | 94.60% | 60.93% |
| model:ru-legal-ner | eligible | Addresses & locations | 548/1242 | 44.12% | 60.87% | 30.84% |
| model:ru-legal-ner | eligible | Network identifiers | 11/361 | 3.05% | 65.93% | 2.77% |
| model:ru-legal-ner+homoglyph | eligible | Bank accounts & cards | 114/203 | 56.16% | 81.77% | 31.53% |
| model:ru-legal-ner+homoglyph | eligible | Documents & identifiers | 1351/2076 | 65.08% | 78.61% | 54.53% |
| model:ru-legal-ner+homoglyph | eligible | People's names | 914/1260 | 72.54% | 74.13% | 59.29% |
| model:ru-legal-ner+homoglyph | eligible | Phone numbers & email | 266/389 | 68.38% | 94.86% | 62.21% |
| model:ru-legal-ner+homoglyph | eligible | Addresses & locations | 516/1242 | 41.55% | 56.60% | 29.55% |
| model:ru-legal-ner+homoglyph | eligible | Network identifiers | 11/361 | 3.05% | 65.10% | 2.49% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 146/203 | 71.92% | 88.18% | 69.95% |
| model:ru-pii-ner | eligible | Documents & identifiers | 1737/2076 | 83.67% | 89.11% | 80.88% |
| model:ru-pii-ner | eligible | People's names | 1142/1260 | 90.63% | 92.14% | 87.62% |
| model:ru-pii-ner | eligible | Phone numbers & email | 265/389 | 68.12% | 80.46% | 67.35% |
| model:ru-pii-ner | eligible | Addresses & locations | 615/1242 | 49.52% | 53.14% | 48.55% |
| model:ru-pii-ner | eligible | Network identifiers | 129/361 | 35.73% | 49.58% | 35.18% |
| model:rules-ru | eligible | Bank accounts & cards | 28/203 | 13.79% | 13.79% | 13.30% |
| model:rules-ru | eligible | Documents & identifiers | 179/2076 | 8.62% | 8.82% | 8.29% |
| model:rules-ru | eligible | People's names | 3/1260 | 0.24% | 0.24% | 0.24% |
| model:rules-ru | eligible | Phone numbers & email | 163/389 | 41.90% | 66.07% | 41.65% |
| model:rules-ru | eligible | Addresses & locations | 2/1242 | 0.16% | 0.24% | 0.16% |
| model:rules-ru | eligible | Network identifiers | 159/361 | 44.04% | 51.80% | 43.21% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 0/203 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Documents & identifiers | 14/2076 | 0.67% | 0.77% | 0.67% |
| model:spacy-alrosait | eligible | People's names | 276/1260 | 21.90% | 22.62% | 21.90% |
| model:spacy-alrosait | eligible | Phone numbers & email | 2/389 | 0.51% | 0.51% | 0.51% |
| model:spacy-alrosait | eligible | Addresses & locations | 263/1242 | 21.18% | 25.36% | 21.18% |
| model:spacy-alrosait | eligible | Network identifiers | 1/361 | 0.28% | 0.28% | 0.28% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 0/203 | 0.00% | 0.49% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 54/2076 | 2.60% | 4.48% | 2.60% |
| model:spacy-ru-lg | eligible | People's names | 638/1260 | 50.63% | 51.83% | 50.63% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 20/389 | 5.14% | 7.71% | 5.14% |
| model:spacy-ru-lg | eligible | Addresses & locations | 466/1242 | 37.52% | 47.10% | 37.36% |
| model:spacy-ru-lg | eligible | Network identifiers | 24/361 | 6.65% | 10.80% | 6.65% |
| model:stanza-ru | eligible | Bank accounts & cards | 6/203 | 2.96% | 5.42% | 1.97% |
| model:stanza-ru | eligible | Documents & identifiers | 279/2076 | 13.44% | 21.82% | 13.29% |
| model:stanza-ru | eligible | People's names | 1084/1260 | 86.03% | 87.62% | 86.03% |
| model:stanza-ru | eligible | Phone numbers & email | 20/389 | 5.14% | 10.03% | 4.63% |
| model:stanza-ru | eligible | Addresses & locations | 803/1242 | 64.65% | 79.15% | 64.09% |
| model:stanza-ru | eligible | Network identifiers | 28/361 | 7.76% | 32.13% | 6.93% |
| model:traciora | eligible | Bank accounts & cards | 122/203 | 60.10% | 90.64% | 53.69% |
| model:traciora | eligible | Documents & identifiers | 848/2076 | 40.85% | 60.21% | 26.30% |
| model:traciora | eligible | People's names | 870/1260 | 69.05% | 72.14% | 56.90% |
| model:traciora | eligible | Phone numbers & email | 268/389 | 68.89% | 92.03% | 67.61% |
| model:traciora | eligible | Addresses & locations | 588/1242 | 47.34% | 58.86% | 38.89% |
| model:traciora | eligible | Network identifiers | 116/361 | 32.13% | 50.42% | 23.55% |
