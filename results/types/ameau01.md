# ameau01: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/ameau01.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Logins & usernames | 604/627 | 96.33% | 96.33% | 96.33% |
| composition:fastino | eligible | People's names | 381/382 | 99.74% | 100.00% | 99.48% |
| composition:fastino | eligible | Phone numbers & email | 140/141 | 99.29% | 99.29% | 99.29% |
| composition:fastino | eligible | Addresses & locations | 164/184 | 89.13% | 89.13% | 89.13% |
| composition:fastino | eligible | Network identifiers | 663/777 | 85.33% | 85.33% | 85.33% |
| composition:fastino | eligible | Customer & employee IDs | 129/131 | 98.47% | 98.47% | 98.47% |
| composition:pplx | eligible | Logins & usernames | 601/627 | 95.85% | 95.85% | 94.90% |
| composition:pplx | eligible | People's names | 380/382 | 99.48% | 99.74% | 99.21% |
| composition:pplx | eligible | Phone numbers & email | 138/141 | 97.87% | 97.87% | 97.87% |
| composition:pplx | eligible | Addresses & locations | 47/184 | 25.54% | 25.54% | 25.54% |
| composition:pplx | eligible | Network identifiers | 537/777 | 69.11% | 71.04% | 68.34% |
| composition:pplx | eligible | Customer & employee IDs | 127/131 | 96.95% | 99.24% | 96.95% |
| composition:pplx+fastino | eligible | Logins & usernames | 619/627 | 98.72% | 98.72% | 98.72% |
| composition:pplx+fastino | eligible | People's names | 381/382 | 99.74% | 100.00% | 99.48% |
| composition:pplx+fastino | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Addresses & locations | 167/184 | 90.76% | 90.76% | 90.76% |
| composition:pplx+fastino | eligible | Network identifiers | 723/777 | 93.05% | 93.69% | 93.05% |
| composition:pplx+fastino | eligible | Customer & employee IDs | 131/131 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Logins & usernames | 621/627 | 99.04% | 99.20% | 98.88% |
| composition:pplx+fastino+bardsai | eligible | People's names | 381/382 | 99.74% | 100.00% | 99.48% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 183/184 | 99.46% | 99.46% | 98.91% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 739/777 | 95.11% | 95.88% | 94.59% |
| composition:pplx+fastino+bardsai | eligible | Customer & employee IDs | 131/131 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Logins & usernames | 621/627 | 99.04% | 99.52% | 98.88% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 381/382 | 99.74% | 100.00% | 99.74% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 183/184 | 99.46% | 99.46% | 98.91% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 749/777 | 96.40% | 99.36% | 95.37% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Customer & employee IDs | 131/131 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Logins & usernames | 619/627 | 98.72% | 99.36% | 98.72% |
| composition:pplx+fastino+mmbert | eligible | People's names | 381/382 | 99.74% | 100.00% | 99.74% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 170/184 | 92.39% | 92.39% | 92.39% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 735/777 | 94.59% | 99.10% | 93.95% |
| composition:pplx+fastino+mmbert | eligible | Customer & employee IDs | 131/131 | 100.00% | 100.00% | 100.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Logins & usernames | 591/627 | 94.26% | 94.42% | 93.30% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 379/382 | 99.21% | 100.00% | 99.21% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 138/141 | 97.87% | 98.58% | 97.87% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 48/184 | 26.09% | 26.09% | 26.09% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 370/777 | 47.62% | 50.19% | 47.49% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Customer & employee IDs | 125/131 | 95.42% | 97.71% | 95.42% |
| model:apararti | eligible | Logins & usernames | 393/627 | 62.68% | 63.00% | 55.02% |
| model:apararti | eligible | People's names | 361/382 | 94.50% | 96.86% | 94.24% |
| model:apararti | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 100.00% |
| model:apararti | eligible | Addresses & locations | 10/184 | 5.43% | 5.43% | 5.43% |
| model:apararti | eligible | Network identifiers | 276/777 | 35.52% | 39.90% | 33.85% |
| model:apararti | eligible | Customer & employee IDs | 114/131 | 87.02% | 90.08% | 78.63% |
| model:bardsai-eu | eligible | Logins & usernames | 193/627 | 30.78% | 31.58% | 19.14% |
| model:bardsai-eu | eligible | People's names | 377/382 | 98.69% | 99.48% | 98.43% |
| model:bardsai-eu | eligible | Phone numbers & email | 23/141 | 16.31% | 96.45% | 14.18% |
| model:bardsai-eu | eligible | Addresses & locations | 174/184 | 94.57% | 94.57% | 93.48% |
| model:bardsai-eu | eligible | Network identifiers | 160/777 | 20.59% | 32.30% | 17.76% |
| model:bardsai-eu | eligible | Customer & employee IDs | 75/131 | 57.25% | 68.70% | 28.24% |
| model:davlan-mbert | eligible | Logins & usernames | 84/627 | 13.40% | 14.04% | 8.13% |
| model:davlan-mbert | eligible | People's names | 379/382 | 99.21% | 99.74% | 97.64% |
| model:davlan-mbert | eligible | Phone numbers & email | 6/141 | 4.26% | 17.73% | 2.13% |
| model:davlan-mbert | eligible | Addresses & locations | 179/184 | 97.28% | 97.28% | 97.28% |
| model:davlan-mbert | eligible | Network identifiers | 6/777 | 0.77% | 10.81% | 0.26% |
| model:davlan-mbert | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Logins & usernames | 46/627 | 7.34% | 8.61% | 3.83% |
| model:davlan-mbert+cpu-int8 | eligible | People's names | 369/382 | 96.60% | 99.48% | 95.03% |
| model:davlan-mbert+cpu-int8 | eligible | Phone numbers & email | 1/141 | 0.71% | 8.51% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Addresses & locations | 176/184 | 95.65% | 95.65% | 95.65% |
| model:davlan-mbert+cpu-int8 | eligible | Network identifiers | 1/777 | 0.13% | 7.98% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Logins & usernames | 206/627 | 32.85% | 33.97% | 23.13% |
| model:davlan-xlmr | eligible | People's names | 377/382 | 98.69% | 99.21% | 97.38% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/141 | 0.00% | 10.64% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 178/184 | 96.74% | 96.74% | 96.20% |
| model:davlan-xlmr | eligible | Network identifiers | 7/777 | 0.90% | 1.16% | 0.77% |
| model:davlan-xlmr | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Logins & usernames | 11/627 | 1.75% | 1.75% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | People's names | 266/382 | 69.63% | 82.46% | 56.28% |
| model:davlan-xlmr+cpu-int8 | eligible | Phone numbers & email | 0/141 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Addresses & locations | 143/184 | 77.72% | 77.72% | 70.11% |
| model:davlan-xlmr+cpu-int8 | eligible | Network identifiers | 0/777 | 0.00% | 0.13% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Logins & usernames | 28/627 | 4.47% | 4.94% | 3.19% |
| model:fef2-secret-ru | eligible | People's names | 46/382 | 12.04% | 17.54% | 9.95% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 105/141 | 74.47% | 77.30% | 72.34% |
| model:fef2-secret-ru | eligible | Addresses & locations | 4/184 | 2.17% | 2.17% | 2.17% |
| model:fef2-secret-ru | eligible | Network identifiers | 8/777 | 1.03% | 1.67% | 0.64% |
| model:fef2-secret-ru | eligible | Customer & employee IDs | 55/131 | 41.98% | 47.33% | 39.69% |
| model:fef2-secret-ru+cpu-int8 | eligible | Logins & usernames | 24/627 | 3.83% | 4.47% | 2.71% |
| model:fef2-secret-ru+cpu-int8 | eligible | People's names | 63/382 | 16.49% | 23.30% | 11.52% |
| model:fef2-secret-ru+cpu-int8 | eligible | Phone numbers & email | 91/141 | 64.54% | 75.89% | 59.57% |
| model:fef2-secret-ru+cpu-int8 | eligible | Addresses & locations | 3/184 | 1.63% | 1.63% | 1.09% |
| model:fef2-secret-ru+cpu-int8 | eligible | Network identifiers | 3/777 | 0.39% | 1.29% | 0.13% |
| model:fef2-secret-ru+cpu-int8 | eligible | Customer & employee IDs | 41/131 | 31.30% | 35.11% | 29.01% |
| model:gliner-multi-v21 | eligible | Logins & usernames | 414/627 | 66.03% | 66.19% | 66.03% |
| model:gliner-multi-v21 | eligible | People's names | 369/382 | 96.60% | 96.60% | 96.34% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 22/141 | 15.60% | 56.74% | 15.60% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 146/184 | 79.35% | 79.35% | 79.35% |
| model:gliner-multi-v21 | eligible | Network identifiers | 382/777 | 49.16% | 49.16% | 49.16% |
| model:gliner-multi-v21 | eligible | Customer & employee IDs | 57/131 | 43.51% | 43.51% | 43.51% |
| model:gliner-multi-v21+cpu-int8 | eligible | Logins & usernames | 0/627 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | People's names | 0/382 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Phone numbers & email | 0/141 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Addresses & locations | 0/184 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Network identifiers | 0/777 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia | eligible | Logins & usernames | 594/627 | 94.74% | 94.74% | 94.74% |
| model:gliner-nvidia | eligible | People's names | 365/382 | 95.55% | 99.48% | 93.98% |
| model:gliner-nvidia | eligible | Phone numbers & email | 133/141 | 94.33% | 97.16% | 94.33% |
| model:gliner-nvidia | eligible | Addresses & locations | 181/184 | 98.37% | 98.37% | 98.37% |
| model:gliner-nvidia | eligible | Network identifiers | 456/777 | 58.69% | 58.69% | 58.69% |
| model:gliner-nvidia | eligible | Customer & employee IDs | 129/131 | 98.47% | 98.47% | 98.47% |
| model:gliner-nvidia+cpu-int8 | eligible | Logins & usernames | 0/627 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | People's names | 0/382 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Phone numbers & email | 0/141 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Addresses & locations | 0/184 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Network identifiers | 0/777 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base | eligible | Logins & usernames | 534/627 | 85.17% | 85.17% | 85.17% |
| model:gliner-pii-base | eligible | People's names | 115/382 | 30.10% | 30.37% | 30.10% |
| model:gliner-pii-base | eligible | Phone numbers & email | 136/141 | 96.45% | 96.45% | 96.45% |
| model:gliner-pii-base | eligible | Addresses & locations | 124/184 | 67.39% | 67.39% | 67.39% |
| model:gliner-pii-base | eligible | Network identifiers | 658/777 | 84.68% | 84.68% | 84.68% |
| model:gliner-pii-base | eligible | Customer & employee IDs | 130/131 | 99.24% | 99.24% | 99.24% |
| model:gliner-pii-base+cpu-int8 | eligible | Logins & usernames | 0/627 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | People's names | 3/382 | 0.79% | 0.79% | 0.79% |
| model:gliner-pii-base+cpu-int8 | eligible | Phone numbers & email | 5/141 | 3.55% | 3.55% | 3.55% |
| model:gliner-pii-base+cpu-int8 | eligible | Addresses & locations | 0/184 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Network identifiers | 0/777 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Customer & employee IDs | 7/131 | 5.34% | 5.34% | 5.34% |
| model:gliner-pii-edge | eligible | Logins & usernames | 575/627 | 91.71% | 91.87% | 91.71% |
| model:gliner-pii-edge | eligible | People's names | 141/382 | 36.91% | 37.96% | 36.91% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 132/141 | 93.62% | 95.04% | 93.62% |
| model:gliner-pii-edge | eligible | Addresses & locations | 176/184 | 95.65% | 95.65% | 95.65% |
| model:gliner-pii-edge | eligible | Network identifiers | 465/777 | 59.85% | 59.85% | 59.85% |
| model:gliner-pii-edge | eligible | Customer & employee IDs | 131/131 | 100.00% | 100.00% | 100.00% |
| model:gliner-pii-edge+cpu-int8 | eligible | Logins & usernames | 77/627 | 12.28% | 12.76% | 12.28% |
| model:gliner-pii-edge+cpu-int8 | eligible | People's names | 4/382 | 1.05% | 1.57% | 1.05% |
| model:gliner-pii-edge+cpu-int8 | eligible | Phone numbers & email | 17/141 | 12.06% | 14.89% | 12.06% |
| model:gliner-pii-edge+cpu-int8 | eligible | Addresses & locations | 8/184 | 4.35% | 4.35% | 4.35% |
| model:gliner-pii-edge+cpu-int8 | eligible | Network identifiers | 6/777 | 0.77% | 1.03% | 0.77% |
| model:gliner-pii-edge+cpu-int8 | eligible | Customer & employee IDs | 21/131 | 16.03% | 16.03% | 16.03% |
| model:gliner-stream-pii | eligible | Logins & usernames | 597/627 | 95.22% | 95.53% | 95.22% |
| model:gliner-stream-pii | eligible | People's names | 355/382 | 92.93% | 96.86% | 92.93% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 101/141 | 71.63% | 91.49% | 71.63% |
| model:gliner-stream-pii | eligible | Addresses & locations | 118/184 | 64.13% | 64.13% | 64.13% |
| model:gliner-stream-pii | eligible | Network identifiers | 544/777 | 70.01% | 70.01% | 70.01% |
| model:gliner-stream-pii | eligible | Customer & employee IDs | 129/131 | 98.47% | 98.47% | 98.47% |
| model:gliner-urchade | eligible | Logins & usernames | 510/627 | 81.34% | 81.34% | 81.34% |
| model:gliner-urchade | eligible | People's names | 380/382 | 99.48% | 99.74% | 99.21% |
| model:gliner-urchade | eligible | Phone numbers & email | 112/141 | 79.43% | 92.91% | 79.43% |
| model:gliner-urchade | eligible | Addresses & locations | 115/184 | 62.50% | 62.50% | 62.50% |
| model:gliner-urchade | eligible | Network identifiers | 516/777 | 66.41% | 66.41% | 66.41% |
| model:gliner-urchade | eligible | Customer & employee IDs | 97/131 | 74.05% | 74.05% | 74.05% |
| model:gliner-urchade+cpu-int8 | eligible | Logins & usernames | 0/627 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | People's names | 0/382 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Phone numbers & email | 0/141 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Addresses & locations | 0/184 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Network identifiers | 0/777 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:gliner2-fastino | eligible | Logins & usernames | 604/627 | 96.33% | 96.33% | 96.33% |
| model:gliner2-fastino | eligible | People's names | 381/382 | 99.74% | 100.00% | 99.48% |
| model:gliner2-fastino | eligible | Phone numbers & email | 140/141 | 99.29% | 99.29% | 99.29% |
| model:gliner2-fastino | eligible | Addresses & locations | 164/184 | 89.13% | 89.13% | 89.13% |
| model:gliner2-fastino | eligible | Network identifiers | 663/777 | 85.33% | 85.33% | 85.33% |
| model:gliner2-fastino | eligible | Customer & employee IDs | 129/131 | 98.47% | 98.47% | 98.47% |
| model:gliner2-hivetrace-omni | eligible | Logins & usernames | 541/627 | 86.28% | 86.28% | 86.28% |
| model:gliner2-hivetrace-omni | eligible | People's names | 381/382 | 99.74% | 100.00% | 99.48% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 100.00% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 170/184 | 92.39% | 92.39% | 92.39% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 757/777 | 97.43% | 97.43% | 97.43% |
| model:gliner2-hivetrace-omni | eligible | Customer & employee IDs | 131/131 | 100.00% | 100.00% | 100.00% |
| model:gliner2-hivetrace-uni | eligible | Logins & usernames | 359/627 | 57.26% | 57.42% | 57.26% |
| model:gliner2-hivetrace-uni | eligible | People's names | 374/382 | 97.91% | 98.17% | 97.64% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 135/141 | 95.74% | 95.74% | 95.74% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 2/184 | 1.09% | 1.09% | 1.09% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 35/777 | 4.50% | 4.50% | 4.50% |
| model:gliner2-hivetrace-uni | eligible | Customer & employee IDs | 24/131 | 18.32% | 18.32% | 18.32% |
| model:gliner2-large | eligible | Logins & usernames | 458/627 | 73.05% | 73.21% | 73.05% |
| model:gliner2-large | eligible | People's names | 379/382 | 99.21% | 99.48% | 98.95% |
| model:gliner2-large | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 100.00% |
| model:gliner2-large | eligible | Addresses & locations | 145/184 | 78.80% | 78.80% | 78.80% |
| model:gliner2-large | eligible | Network identifiers | 458/777 | 58.94% | 58.94% | 58.94% |
| model:gliner2-large | eligible | Customer & employee IDs | 126/131 | 96.18% | 96.18% | 96.18% |
| model:gliner2-vladlinv | eligible | Logins & usernames | 296/627 | 47.21% | 47.21% | 47.21% |
| model:gliner2-vladlinv | eligible | People's names | 365/382 | 95.55% | 95.81% | 95.29% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 124/141 | 87.94% | 87.94% | 87.94% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 2/184 | 1.09% | 1.09% | 1.09% |
| model:gliner2-vladlinv | eligible | Network identifiers | 33/777 | 4.25% | 4.25% | 4.25% |
| model:gliner2-vladlinv | eligible | Customer & employee IDs | 57/131 | 43.51% | 43.51% | 43.51% |
| model:gliner25-fastino | eligible | Logins & usernames | 484/627 | 77.19% | 77.19% | 77.19% |
| model:gliner25-fastino | eligible | People's names | 381/382 | 99.74% | 100.00% | 99.48% |
| model:gliner25-fastino | eligible | Phone numbers & email | 137/141 | 97.16% | 97.16% | 97.16% |
| model:gliner25-fastino | eligible | Addresses & locations | 118/184 | 64.13% | 64.13% | 64.13% |
| model:gliner25-fastino | eligible | Network identifiers | 453/777 | 58.30% | 58.30% | 58.30% |
| model:gliner25-fastino | eligible | Customer & employee IDs | 52/131 | 39.69% | 39.69% | 39.69% |
| model:gravitee-small | eligible | Logins & usernames | 152/627 | 24.24% | 25.36% | 17.38% |
| model:gravitee-small | eligible | People's names | 372/382 | 97.38% | 99.74% | 31.94% |
| model:gravitee-small | eligible | Phone numbers & email | 135/141 | 95.74% | 97.16% | 95.04% |
| model:gravitee-small | eligible | Addresses & locations | 159/184 | 86.41% | 86.41% | 86.41% |
| model:gravitee-small | eligible | Network identifiers | 228/777 | 29.34% | 30.12% | 29.34% |
| model:gravitee-small | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:gravitee-small+cpu-int8 | eligible | Logins & usernames | 165/627 | 26.32% | 27.11% | 18.66% |
| model:gravitee-small+cpu-int8 | eligible | People's names | 372/382 | 97.38% | 100.00% | 33.25% |
| model:gravitee-small+cpu-int8 | eligible | Phone numbers & email | 135/141 | 95.74% | 97.16% | 94.33% |
| model:gravitee-small+cpu-int8 | eligible | Addresses & locations | 147/184 | 79.89% | 79.89% | 79.89% |
| model:gravitee-small+cpu-int8 | eligible | Network identifiers | 229/777 | 29.47% | 29.99% | 29.47% |
| model:gravitee-small+cpu-int8 | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:kalyan-ettin | eligible | Logins & usernames | 489/627 | 77.99% | 79.74% | 62.36% |
| model:kalyan-ettin | eligible | People's names | 35/382 | 9.16% | 98.17% | 60.47% |
| model:kalyan-ettin | eligible | Phone numbers & email | 129/141 | 91.49% | 95.74% | 91.49% |
| model:kalyan-ettin | eligible | Addresses & locations | 136/184 | 73.91% | 73.91% | 72.83% |
| model:kalyan-ettin | eligible | Network identifiers | 172/777 | 22.14% | 35.78% | 21.88% |
| model:kalyan-ettin | eligible | Customer & employee IDs | 63/131 | 48.09% | 81.68% | 35.11% |
| model:kalyan-ettin+cpu-int8 | eligible | Logins & usernames | 224/627 | 35.73% | 38.44% | 14.35% |
| model:kalyan-ettin+cpu-int8 | eligible | People's names | 33/382 | 8.64% | 85.34% | 11.78% |
| model:kalyan-ettin+cpu-int8 | eligible | Phone numbers & email | 80/141 | 56.74% | 91.49% | 34.75% |
| model:kalyan-ettin+cpu-int8 | eligible | Addresses & locations | 40/184 | 21.74% | 21.74% | 21.20% |
| model:kalyan-ettin+cpu-int8 | eligible | Network identifiers | 1/777 | 0.13% | 8.37% | 0.13% |
| model:kalyan-ettin+cpu-int8 | eligible | Customer & employee IDs | 17/131 | 12.98% | 35.11% | 3.82% |
| model:mmbert32k | eligible | Logins & usernames | 432/627 | 68.90% | 71.93% | 49.44% |
| model:mmbert32k | eligible | People's names | 373/382 | 97.64% | 100.00% | 97.64% |
| model:mmbert32k | eligible | Phone numbers & email | 103/141 | 73.05% | 99.29% | 41.84% |
| model:mmbert32k | eligible | Addresses & locations | 33/184 | 17.93% | 17.93% | 17.93% |
| model:mmbert32k | eligible | Network identifiers | 181/777 | 23.29% | 80.44% | 8.88% |
| model:mmbert32k | eligible | Customer & employee IDs | 45/131 | 34.35% | 86.26% | 11.45% |
| model:mmbert32k+cpu-int8 | eligible | Logins & usernames | 170/627 | 27.11% | 30.14% | 5.58% |
| model:mmbert32k+cpu-int8 | eligible | People's names | 192/382 | 50.26% | 70.94% | 50.52% |
| model:mmbert32k+cpu-int8 | eligible | Phone numbers & email | 18/141 | 12.77% | 84.40% | 2.84% |
| model:mmbert32k+cpu-int8 | eligible | Addresses & locations | 29/184 | 15.76% | 15.76% | 14.67% |
| model:mmbert32k+cpu-int8 | eligible | Network identifiers | 22/777 | 2.83% | 62.68% | 0.26% |
| model:mmbert32k+cpu-int8 | eligible | Customer & employee IDs | 5/131 | 3.82% | 87.02% | 0.00% |
| model:natasha | eligible | Logins & usernames | 1/627 | 0.16% | 0.16% | 0.16% |
| model:natasha | eligible | People's names | 59/382 | 15.45% | 15.71% | 15.45% |
| model:natasha | eligible | Phone numbers & email | 0/141 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Addresses & locations | 15/184 | 8.15% | 8.15% | 8.15% |
| model:natasha | eligible | Network identifiers | 13/777 | 1.67% | 1.67% | 1.67% |
| model:natasha | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Logins & usernames | 57/627 | 9.09% | 12.76% | 4.63% |
| model:ner-ru-gherman | eligible | People's names | 2/382 | 0.52% | 100.00% | 0.52% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/141 | 0.00% | 19.86% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 176/184 | 95.65% | 95.65% | 95.65% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/777 | 0.00% | 0.26% | 0.00% |
| model:ner-ru-gherman | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Logins & usernames | 33/627 | 5.26% | 8.13% | 1.44% |
| model:ner-ru-gherman+cpu-int8 | eligible | People's names | 1/382 | 0.26% | 100.00% | 0.26% |
| model:ner-ru-gherman+cpu-int8 | eligible | Phone numbers & email | 0/141 | 0.00% | 13.48% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Addresses & locations | 173/184 | 94.02% | 94.02% | 94.02% |
| model:ner-ru-gherman+cpu-int8 | eligible | Network identifiers | 0/777 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Logins & usernames | 52/627 | 8.29% | 11.64% | 4.31% |
| model:ner-ru-gherman-onnx | eligible | People's names | 2/382 | 0.52% | 100.00% | 0.52% |
| model:ner-ru-gherman-onnx | eligible | Phone numbers & email | 0/141 | 0.00% | 17.73% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Addresses & locations | 176/184 | 95.65% | 95.65% | 95.65% |
| model:ner-ru-gherman-onnx | eligible | Network identifiers | 0/777 | 0.00% | 0.13% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Logins & usernames | 197/627 | 31.42% | 32.85% | 24.56% |
| model:ner-ru-yqelz | eligible | People's names | 354/382 | 92.67% | 97.91% | 87.96% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 1/141 | 0.71% | 11.35% | 0.00% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 176/184 | 95.65% | 96.20% | 95.65% |
| model:ner-ru-yqelz | eligible | Network identifiers | 140/777 | 18.02% | 23.29% | 15.57% |
| model:ner-ru-yqelz | eligible | Customer & employee IDs | 1/131 | 0.76% | 2.29% | 0.76% |
| model:nuner-zero | eligible | Logins & usernames | 551/627 | 87.88% | 88.04% | 87.72% |
| model:nuner-zero | eligible | People's names | 377/382 | 98.69% | 99.48% | 0.26% |
| model:nuner-zero | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 96.45% |
| model:nuner-zero | eligible | Addresses & locations | 140/184 | 76.09% | 76.09% | 75.54% |
| model:nuner-zero | eligible | Network identifiers | 559/777 | 71.94% | 71.94% | 71.94% |
| model:nuner-zero | eligible | Customer & employee IDs | 123/131 | 93.89% | 93.89% | 93.89% |
| model:nym-base | eligible | Logins & usernames | 535/627 | 85.33% | 85.81% | 82.62% |
| model:nym-base | eligible | People's names | 5/382 | 1.31% | 100.00% | 98.95% |
| model:nym-base | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 100.00% |
| model:nym-base | eligible | Addresses & locations | 139/184 | 75.54% | 75.54% | 75.54% |
| model:nym-base | eligible | Network identifiers | 59/777 | 7.59% | 10.68% | 6.18% |
| model:nym-base | eligible | Customer & employee IDs | 131/131 | 100.00% | 100.00% | 100.00% |
| model:nym-base+cpu-int8 | eligible | Logins & usernames | 440/627 | 70.18% | 71.61% | 65.39% |
| model:nym-base+cpu-int8 | eligible | People's names | 4/382 | 1.05% | 99.74% | 96.60% |
| model:nym-base+cpu-int8 | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 100.00% |
| model:nym-base+cpu-int8 | eligible | Addresses & locations | 104/184 | 56.52% | 56.52% | 56.52% |
| model:nym-base+cpu-int8 | eligible | Network identifiers | 68/777 | 8.75% | 12.61% | 6.18% |
| model:nym-base+cpu-int8 | eligible | Customer & employee IDs | 130/131 | 99.24% | 100.00% | 99.24% |
| model:nym-small | eligible | Logins & usernames | 413/627 | 65.87% | 66.51% | 63.16% |
| model:nym-small | eligible | People's names | 5/382 | 1.31% | 99.74% | 99.21% |
| model:nym-small | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 99.29% |
| model:nym-small | eligible | Addresses & locations | 154/184 | 83.70% | 83.70% | 82.61% |
| model:nym-small | eligible | Network identifiers | 18/777 | 2.32% | 3.09% | 1.42% |
| model:nym-small | eligible | Customer & employee IDs | 130/131 | 99.24% | 100.00% | 99.24% |
| model:openai-base | eligible | Logins & usernames | 411/627 | 65.55% | 65.55% | 62.36% |
| model:openai-base | eligible | People's names | 366/382 | 95.81% | 96.34% | 95.81% |
| model:openai-base | eligible | Phone numbers & email | 137/141 | 97.16% | 97.16% | 97.16% |
| model:openai-base | eligible | Addresses & locations | 3/184 | 1.63% | 1.63% | 1.09% |
| model:openai-base | eligible | Network identifiers | 218/777 | 28.06% | 30.12% | 26.90% |
| model:openai-base | eligible | Customer & employee IDs | 69/131 | 52.67% | 61.83% | 48.85% |
| model:openai-base-onnx | eligible | Logins & usernames | 405/627 | 64.59% | 64.59% | 62.84% |
| model:openai-base-onnx | eligible | People's names | 364/382 | 95.29% | 96.34% | 95.55% |
| model:openai-base-onnx | eligible | Phone numbers & email | 137/141 | 97.16% | 97.16% | 97.16% |
| model:openai-base-onnx | eligible | Addresses & locations | 3/184 | 1.63% | 1.63% | 1.09% |
| model:openai-base-onnx | eligible | Network identifiers | 217/777 | 27.93% | 30.24% | 26.77% |
| model:openai-base-onnx | eligible | Customer & employee IDs | 69/131 | 52.67% | 62.60% | 48.09% |
| model:openmed-multilingual | eligible | Logins & usernames | 458/627 | 73.05% | 73.68% | 58.37% |
| model:openmed-multilingual | eligible | People's names | 23/382 | 6.02% | 99.74% | 96.86% |
| model:openmed-multilingual | eligible | Phone numbers & email | 140/141 | 99.29% | 99.29% | 97.87% |
| model:openmed-multilingual | eligible | Addresses & locations | 141/184 | 76.63% | 76.63% | 76.09% |
| model:openmed-multilingual | eligible | Network identifiers | 286/777 | 36.81% | 45.43% | 33.98% |
| model:openmed-multilingual | eligible | Customer & employee IDs | 131/131 | 100.00% | 100.00% | 100.00% |
| model:openmed-nemotron | eligible | Logins & usernames | 454/627 | 72.41% | 73.21% | 56.94% |
| model:openmed-nemotron | eligible | People's names | 2/382 | 0.52% | 99.74% | 97.91% |
| model:openmed-nemotron | eligible | Phone numbers & email | 138/141 | 97.87% | 99.29% | 95.74% |
| model:openmed-nemotron | eligible | Addresses & locations | 113/184 | 61.41% | 61.41% | 61.41% |
| model:openmed-nemotron | eligible | Network identifiers | 222/777 | 28.57% | 33.20% | 27.16% |
| model:openmed-nemotron | eligible | Customer & employee IDs | 35/131 | 26.72% | 61.07% | 25.19% |
| model:opf-kz-ru | eligible | Logins & usernames | 311/627 | 49.60% | 50.08% | 42.11% |
| model:opf-kz-ru | eligible | People's names | 336/382 | 87.96% | 93.19% | 86.91% |
| model:opf-kz-ru | eligible | Phone numbers & email | 141/141 | 100.00% | 100.00% | 100.00% |
| model:opf-kz-ru | eligible | Addresses & locations | 6/184 | 3.26% | 3.26% | 3.26% |
| model:opf-kz-ru | eligible | Network identifiers | 239/777 | 30.76% | 35.01% | 29.34% |
| model:opf-kz-ru | eligible | Customer & employee IDs | 106/131 | 80.92% | 89.31% | 71.76% |
| model:opf-ru | eligible | Logins & usernames | 542/627 | 86.44% | 86.76% | 76.71% |
| model:opf-ru | eligible | People's names | 345/382 | 90.31% | 97.91% | 90.05% |
| model:opf-ru | eligible | Phone numbers & email | 140/141 | 99.29% | 100.00% | 97.16% |
| model:opf-ru | eligible | Addresses & locations | 6/184 | 3.26% | 3.26% | 3.26% |
| model:opf-ru | eligible | Network identifiers | 85/777 | 10.94% | 31.27% | 5.53% |
| model:opf-ru | eligible | Customer & employee IDs | 8/131 | 6.11% | 31.30% | 4.58% |
| model:opf-ru-v2 | eligible | Logins & usernames | 212/627 | 33.81% | 35.25% | 26.16% |
| model:opf-ru-v2 | eligible | People's names | 353/382 | 92.41% | 93.98% | 91.88% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 135/141 | 95.74% | 97.16% | 95.74% |
| model:opf-ru-v2 | eligible | Addresses & locations | 1/184 | 0.54% | 0.54% | 0.54% |
| model:opf-ru-v2 | eligible | Network identifiers | 233/777 | 29.99% | 33.08% | 29.47% |
| model:opf-ru-v2 | eligible | Customer & employee IDs | 19/131 | 14.50% | 35.88% | 6.11% |
| model:pii-shield-onnx | eligible | Logins & usernames | 108/627 | 17.22% | 18.82% | 10.21% |
| model:pii-shield-onnx | eligible | People's names | 151/382 | 39.53% | 68.59% | 31.94% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 131/141 | 92.91% | 97.16% | 89.36% |
| model:pii-shield-onnx | eligible | Addresses & locations | 33/184 | 17.93% | 17.93% | 15.76% |
| model:pii-shield-onnx | eligible | Network identifiers | 582/777 | 74.90% | 90.86% | 64.48% |
| model:pii-shield-onnx | eligible | Customer & employee IDs | 44/131 | 33.59% | 48.09% | 19.85% |
| model:pplx | eligible | Logins & usernames | 601/627 | 95.85% | 95.85% | 94.90% |
| model:pplx | eligible | People's names | 380/382 | 99.48% | 99.74% | 99.21% |
| model:pplx | eligible | Phone numbers & email | 138/141 | 97.87% | 97.87% | 97.87% |
| model:pplx | eligible | Addresses & locations | 47/184 | 25.54% | 25.54% | 25.54% |
| model:pplx | eligible | Network identifiers | 537/777 | 69.11% | 71.04% | 68.34% |
| model:pplx | eligible | Customer & employee IDs | 127/131 | 96.95% | 99.24% | 96.95% |
| model:pplx+cpu-int8 | eligible | Logins & usernames | 612/627 | 97.61% | 97.61% | 97.29% |
| model:pplx+cpu-int8 | eligible | People's names | 381/382 | 99.74% | 99.74% | 99.21% |
| model:pplx+cpu-int8 | eligible | Phone numbers & email | 140/141 | 99.29% | 100.00% | 99.29% |
| model:pplx+cpu-int8 | eligible | Addresses & locations | 147/184 | 79.89% | 79.89% | 79.89% |
| model:pplx+cpu-int8 | eligible | Network identifiers | 707/777 | 90.99% | 93.31% | 90.48% |
| model:pplx+cpu-int8 | eligible | Customer & employee IDs | 131/131 | 100.00% | 100.00% | 100.00% |
| model:ru-legal-ner | eligible | Logins & usernames | 208/627 | 33.17% | 35.57% | 14.04% |
| model:ru-legal-ner | eligible | People's names | 66/382 | 17.28% | 31.41% | 11.78% |
| model:ru-legal-ner | eligible | Phone numbers & email | 68/141 | 48.23% | 97.87% | 35.46% |
| model:ru-legal-ner | eligible | Addresses & locations | 13/184 | 7.07% | 7.07% | 5.43% |
| model:ru-legal-ner | eligible | Network identifiers | 12/777 | 1.54% | 16.47% | 1.42% |
| model:ru-legal-ner | eligible | Customer & employee IDs | 0/131 | 0.00% | 51.91% | 0.00% |
| model:ru-legal-ner+cpu-int8 | eligible | Logins & usernames | 214/627 | 34.13% | 36.84% | 15.31% |
| model:ru-legal-ner+cpu-int8 | eligible | People's names | 73/382 | 19.11% | 37.17% | 13.35% |
| model:ru-legal-ner+cpu-int8 | eligible | Phone numbers & email | 69/141 | 48.94% | 96.45% | 34.04% |
| model:ru-legal-ner+cpu-int8 | eligible | Addresses & locations | 12/184 | 6.52% | 6.52% | 5.43% |
| model:ru-legal-ner+cpu-int8 | eligible | Network identifiers | 16/777 | 2.06% | 16.86% | 1.93% |
| model:ru-legal-ner+cpu-int8 | eligible | Customer & employee IDs | 0/131 | 0.00% | 51.15% | 0.00% |
| model:ru-pii-ner | eligible | Logins & usernames | 180/627 | 28.71% | 28.87% | 28.71% |
| model:ru-pii-ner | eligible | People's names | 365/382 | 95.55% | 96.07% | 95.55% |
| model:ru-pii-ner | eligible | Phone numbers & email | 119/141 | 84.40% | 85.82% | 84.40% |
| model:ru-pii-ner | eligible | Addresses & locations | 7/184 | 3.80% | 3.80% | 3.80% |
| model:ru-pii-ner | eligible | Network identifiers | 212/777 | 27.28% | 27.41% | 27.28% |
| model:ru-pii-ner | eligible | Customer & employee IDs | 114/131 | 87.02% | 87.02% | 87.02% |
| model:rules-ru | eligible | Logins & usernames | 41/627 | 6.54% | 6.54% | 6.54% |
| model:rules-ru | eligible | People's names | 0/382 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 120/141 | 85.11% | 85.11% | 85.11% |
| model:rules-ru | eligible | Addresses & locations | 0/184 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Network identifiers | 205/777 | 26.38% | 26.38% | 26.38% |
| model:rules-ru | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Logins & usernames | 0/627 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 0/382 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/141 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Addresses & locations | 0/184 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Network identifiers | 0/777 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Customer & employee IDs | 0/131 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Logins & usernames | 49/627 | 7.81% | 7.81% | 7.81% |
| model:spacy-ru-lg | eligible | People's names | 39/382 | 10.21% | 10.21% | 10.21% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 2/141 | 1.42% | 1.42% | 1.42% |
| model:spacy-ru-lg | eligible | Addresses & locations | 8/184 | 4.35% | 4.35% | 4.35% |
| model:spacy-ru-lg | eligible | Network identifiers | 22/777 | 2.83% | 2.83% | 2.83% |
| model:spacy-ru-lg | eligible | Customer & employee IDs | 3/131 | 2.29% | 2.29% | 2.29% |
| model:stanza-ru | eligible | Logins & usernames | 56/627 | 8.93% | 8.93% | 8.93% |
| model:stanza-ru | eligible | People's names | 368/382 | 96.34% | 98.95% | 96.07% |
| model:stanza-ru | eligible | Phone numbers & email | 7/141 | 4.96% | 4.96% | 4.96% |
| model:stanza-ru | eligible | Addresses & locations | 150/184 | 81.52% | 81.52% | 81.52% |
| model:stanza-ru | eligible | Network identifiers | 259/777 | 33.33% | 57.92% | 10.94% |
| model:stanza-ru | eligible | Customer & employee IDs | 6/131 | 4.58% | 85.50% | 4.58% |
| model:traciora | eligible | Logins & usernames | 345/627 | 55.02% | 55.98% | 43.22% |
| model:traciora | eligible | People's names | 334/382 | 87.43% | 91.62% | 84.82% |
| model:traciora | eligible | Phone numbers & email | 135/141 | 95.74% | 97.16% | 95.74% |
| model:traciora | eligible | Addresses & locations | 2/184 | 1.09% | 1.09% | 1.09% |
| model:traciora | eligible | Network identifiers | 174/777 | 22.39% | 28.06% | 21.49% |
| model:traciora | eligible | Customer & employee IDs | 14/131 | 10.69% | 41.22% | 7.63% |
