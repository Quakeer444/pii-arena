# nemotron-pii: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/nemotron-pii.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 294/375 | 78.40% | 94.40% | 78.40% |
| composition:fastino | eligible | Logins & usernames | 218/229 | 95.20% | 96.94% | 95.20% |
| composition:fastino | eligible | Bank accounts & cards | 630/698 | 90.26% | 90.26% | 90.26% |
| composition:fastino | eligible | Documents & identifiers | 861/886 | 97.18% | 97.52% | 97.18% |
| composition:fastino | eligible | People's names | 2118/2245 | 94.34% | 94.48% | 94.34% |
| composition:fastino | eligible | Phone numbers & email | 1189/1199 | 99.17% | 99.67% | 99.17% |
| composition:fastino | eligible | Addresses & locations | 1368/1468 | 93.19% | 98.84% | 91.83% |
| composition:fastino | eligible | Dates & times | 276/277 | 99.64% | 99.64% | 99.64% |
| composition:fastino | eligible | Organizations | 821/843 | 97.39% | 99.29% | 97.39% |
| composition:fastino | eligible | Network identifiers | 315/762 | 41.34% | 44.36% | 41.34% |
| composition:fastino | eligible | Customer & employee IDs | 400/409 | 97.80% | 97.80% | 97.80% |
| composition:pplx | eligible | Passwords, keys & tokens | 324/375 | 86.40% | 97.07% | 85.87% |
| composition:pplx | eligible | Logins & usernames | 229/229 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Bank accounts & cards | 679/698 | 97.28% | 97.28% | 97.28% |
| composition:pplx | eligible | Documents & identifiers | 884/886 | 99.77% | 100.00% | 99.77% |
| composition:pplx | eligible | People's names | 2234/2245 | 99.51% | 99.51% | 99.47% |
| composition:pplx | eligible | Phone numbers & email | 1191/1199 | 99.33% | 99.33% | 99.33% |
| composition:pplx | eligible | Addresses & locations | 1160/1468 | 79.02% | 79.97% | 78.88% |
| composition:pplx | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 99.28% |
| composition:pplx | eligible | Organizations | 57/843 | 6.76% | 12.57% | 6.76% |
| composition:pplx | eligible | Network identifiers | 650/762 | 85.30% | 90.94% | 85.17% |
| composition:pplx | eligible | Customer & employee IDs | 409/409 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 328/375 | 87.47% | 98.40% | 87.47% |
| composition:pplx+fastino | eligible | Logins & usernames | 229/229 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 682/698 | 97.71% | 97.71% | 97.71% |
| composition:pplx+fastino | eligible | Documents & identifiers | 885/886 | 99.89% | 100.00% | 99.89% |
| composition:pplx+fastino | eligible | People's names | 2240/2245 | 99.78% | 99.78% | 99.78% |
| composition:pplx+fastino | eligible | Phone numbers & email | 1192/1199 | 99.42% | 99.83% | 99.42% |
| composition:pplx+fastino | eligible | Addresses & locations | 1443/1468 | 98.30% | 99.39% | 98.30% |
| composition:pplx+fastino | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Organizations | 821/843 | 97.39% | 99.41% | 97.39% |
| composition:pplx+fastino | eligible | Network identifiers | 700/762 | 91.86% | 94.23% | 91.86% |
| composition:pplx+fastino | eligible | Customer & employee IDs | 409/409 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 329/375 | 87.73% | 98.67% | 87.73% |
| composition:pplx+fastino+bardsai | eligible | Logins & usernames | 229/229 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 692/698 | 99.14% | 99.14% | 99.00% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 885/886 | 99.89% | 100.00% | 99.89% |
| composition:pplx+fastino+bardsai | eligible | People's names | 2242/2245 | 99.87% | 99.91% | 99.82% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 1192/1199 | 99.42% | 99.83% | 99.42% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 1447/1468 | 98.57% | 99.59% | 98.57% |
| composition:pplx+fastino+bardsai | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 836/843 | 99.17% | 99.88% | 98.93% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 700/762 | 91.86% | 96.85% | 91.86% |
| composition:pplx+fastino+bardsai | eligible | Customer & employee IDs | 409/409 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 331/375 | 88.27% | 100.00% | 87.73% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Logins & usernames | 229/229 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 695/698 | 99.57% | 99.57% | 99.14% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 885/886 | 99.89% | 100.00% | 99.89% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 2242/2245 | 99.87% | 99.91% | 99.82% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 1192/1199 | 99.42% | 99.83% | 99.42% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 1447/1468 | 98.57% | 99.59% | 98.57% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 837/843 | 99.29% | 99.88% | 99.05% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 709/762 | 93.04% | 100.00% | 92.39% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Customer & employee IDs | 409/409 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 331/375 | 88.27% | 100.00% | 87.47% |
| composition:pplx+fastino+mmbert | eligible | Logins & usernames | 229/229 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 691/698 | 99.00% | 99.00% | 98.14% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 885/886 | 99.89% | 100.00% | 99.89% |
| composition:pplx+fastino+mmbert | eligible | People's names | 2240/2245 | 99.78% | 99.78% | 99.78% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 1192/1199 | 99.42% | 99.83% | 99.42% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 1443/1468 | 98.30% | 99.46% | 98.30% |
| composition:pplx+fastino+mmbert | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 826/843 | 97.98% | 99.88% | 97.86% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 708/762 | 92.91% | 100.00% | 92.26% |
| composition:pplx+fastino+mmbert | eligible | Customer & employee IDs | 409/409 | 100.00% | 100.00% | 100.00% |
| model:apararti | eligible | Passwords, keys & tokens | 284/375 | 75.73% | 91.47% | 71.20% |
| model:apararti | eligible | Logins & usernames | 203/229 | 88.65% | 89.96% | 85.59% |
| model:apararti | eligible | Bank accounts & cards | 640/698 | 91.69% | 92.84% | 91.40% |
| model:apararti | eligible | Documents & identifiers | 867/886 | 97.86% | 98.98% | 96.73% |
| model:apararti | eligible | People's names | 1976/2245 | 88.02% | 88.06% | 87.13% |
| model:apararti | eligible | Phone numbers & email | 1155/1199 | 96.33% | 97.08% | 96.08% |
| model:apararti | eligible | Addresses & locations | 602/1468 | 41.01% | 43.53% | 40.19% |
| model:apararti | eligible | Dates & times | 276/277 | 99.64% | 99.64% | 99.64% |
| model:apararti | eligible | Organizations | 44/843 | 5.22% | 7.95% | 4.51% |
| model:apararti | eligible | Network identifiers | 380/762 | 49.87% | 59.84% | 47.24% |
| model:apararti | eligible | Customer & employee IDs | 372/409 | 90.95% | 93.15% | 88.51% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 214/375 | 57.07% | 77.07% | 40.27% |
| model:bardsai-eu | eligible | Logins & usernames | 204/229 | 89.08% | 91.70% | 83.41% |
| model:bardsai-eu | eligible | Bank accounts & cards | 552/698 | 79.08% | 88.40% | 56.45% |
| model:bardsai-eu | eligible | Documents & identifiers | 812/886 | 91.65% | 96.05% | 80.70% |
| model:bardsai-eu | eligible | People's names | 2175/2245 | 96.88% | 96.93% | 95.50% |
| model:bardsai-eu | eligible | Phone numbers & email | 508/1199 | 42.37% | 99.17% | 34.78% |
| model:bardsai-eu | eligible | Addresses & locations | 1329/1468 | 90.53% | 94.48% | 89.92% |
| model:bardsai-eu | eligible | Dates & times | 272/277 | 98.19% | 99.28% | 98.19% |
| model:bardsai-eu | eligible | Organizations | 751/843 | 89.09% | 91.22% | 87.78% |
| model:bardsai-eu | eligible | Network identifiers | 197/762 | 25.85% | 72.97% | 25.33% |
| model:bardsai-eu | eligible | Customer & employee IDs | 350/409 | 85.57% | 87.29% | 69.44% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/375 | 0.00% | 0.80% | 0.00% |
| model:davlan-mbert | eligible | Logins & usernames | 66/229 | 28.82% | 31.00% | 18.34% |
| model:davlan-mbert | eligible | Bank accounts & cards | 0/698 | 0.00% | 0.14% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 0/886 | 0.00% | 0.79% | 0.00% |
| model:davlan-mbert | eligible | People's names | 2189/2245 | 97.51% | 97.51% | 96.70% |
| model:davlan-mbert | eligible | Phone numbers & email | 13/1199 | 1.08% | 8.09% | 0.50% |
| model:davlan-mbert | eligible | Addresses & locations | 1037/1468 | 70.64% | 84.06% | 70.50% |
| model:davlan-mbert | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Organizations | 728/843 | 86.36% | 91.22% | 85.53% |
| model:davlan-mbert | eligible | Network identifiers | 0/762 | 0.00% | 14.17% | 0.00% |
| model:davlan-mbert | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Passwords, keys & tokens | 2/375 | 0.53% | 0.80% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Logins & usernames | 54/229 | 23.58% | 25.33% | 12.66% |
| model:davlan-mbert+cpu-int8 | eligible | Bank accounts & cards | 1/698 | 0.14% | 0.29% | 0.14% |
| model:davlan-mbert+cpu-int8 | eligible | Documents & identifiers | 0/886 | 0.00% | 0.11% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | People's names | 2096/2245 | 93.36% | 93.45% | 92.12% |
| model:davlan-mbert+cpu-int8 | eligible | Phone numbers & email | 1/1199 | 0.08% | 4.59% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Addresses & locations | 1018/1468 | 69.35% | 83.04% | 68.80% |
| model:davlan-mbert+cpu-int8 | eligible | Dates & times | 0/277 | 0.00% | 0.36% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Organizations | 689/843 | 81.73% | 89.21% | 80.19% |
| model:davlan-mbert+cpu-int8 | eligible | Network identifiers | 0/762 | 0.00% | 4.20% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.24% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 1/375 | 0.27% | 1.07% | 0.00% |
| model:davlan-xlmr | eligible | Logins & usernames | 105/229 | 45.85% | 50.66% | 35.81% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 0/698 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 0/886 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 2218/2245 | 98.80% | 98.80% | 98.44% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/1199 | 0.00% | 17.10% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 1079/1468 | 73.50% | 85.01% | 72.34% |
| model:davlan-xlmr | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Organizations | 781/843 | 92.65% | 95.02% | 91.93% |
| model:davlan-xlmr | eligible | Network identifiers | 0/762 | 0.00% | 8.79% | 0.00% |
| model:davlan-xlmr | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Passwords, keys & tokens | 0/375 | 0.00% | 0.53% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Logins & usernames | 23/229 | 10.04% | 11.79% | 0.87% |
| model:davlan-xlmr+cpu-int8 | eligible | Bank accounts & cards | 0/698 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Documents & identifiers | 0/886 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | People's names | 1456/2245 | 64.86% | 64.90% | 54.48% |
| model:davlan-xlmr+cpu-int8 | eligible | Phone numbers & email | 0/1199 | 0.00% | 2.09% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Addresses & locations | 921/1468 | 62.74% | 74.25% | 56.47% |
| model:davlan-xlmr+cpu-int8 | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Organizations | 440/843 | 52.19% | 71.41% | 39.86% |
| model:davlan-xlmr+cpu-int8 | eligible | Network identifiers | 0/762 | 0.00% | 3.67% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 149/375 | 39.73% | 52.53% | 36.53% |
| model:fef2-secret-ru | eligible | Logins & usernames | 91/229 | 39.74% | 41.05% | 33.19% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 10/698 | 1.43% | 1.72% | 0.86% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 75/886 | 8.47% | 9.93% | 6.77% |
| model:fef2-secret-ru | eligible | People's names | 334/2245 | 14.88% | 15.01% | 11.71% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 512/1199 | 42.70% | 55.05% | 39.78% |
| model:fef2-secret-ru | eligible | Addresses & locations | 198/1468 | 13.49% | 15.53% | 13.01% |
| model:fef2-secret-ru | eligible | Dates & times | 0/277 | 0.00% | 0.72% | 0.00% |
| model:fef2-secret-ru | eligible | Organizations | 11/843 | 1.30% | 1.66% | 1.19% |
| model:fef2-secret-ru | eligible | Network identifiers | 0/762 | 0.00% | 0.66% | 0.00% |
| model:fef2-secret-ru | eligible | Customer & employee IDs | 23/409 | 5.62% | 6.60% | 4.40% |
| model:fef2-secret-ru+cpu-int8 | eligible | Passwords, keys & tokens | 133/375 | 35.47% | 48.80% | 30.40% |
| model:fef2-secret-ru+cpu-int8 | eligible | Logins & usernames | 78/229 | 34.06% | 36.68% | 26.64% |
| model:fef2-secret-ru+cpu-int8 | eligible | Bank accounts & cards | 5/698 | 0.72% | 1.00% | 0.29% |
| model:fef2-secret-ru+cpu-int8 | eligible | Documents & identifiers | 38/886 | 4.29% | 6.66% | 2.93% |
| model:fef2-secret-ru+cpu-int8 | eligible | People's names | 364/2245 | 16.21% | 16.30% | 12.61% |
| model:fef2-secret-ru+cpu-int8 | eligible | Phone numbers & email | 308/1199 | 25.69% | 48.62% | 22.69% |
| model:fef2-secret-ru+cpu-int8 | eligible | Addresses & locations | 161/1468 | 10.97% | 12.40% | 9.81% |
| model:fef2-secret-ru+cpu-int8 | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru+cpu-int8 | eligible | Organizations | 13/843 | 1.54% | 1.90% | 1.30% |
| model:fef2-secret-ru+cpu-int8 | eligible | Network identifiers | 0/762 | 0.00% | 0.26% | 0.00% |
| model:fef2-secret-ru+cpu-int8 | eligible | Customer & employee IDs | 17/409 | 4.16% | 4.40% | 1.71% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 147/375 | 39.20% | 43.20% | 39.20% |
| model:gliner-multi-v21 | eligible | Logins & usernames | 199/229 | 86.90% | 88.21% | 86.90% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 366/698 | 52.44% | 52.58% | 52.44% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 585/886 | 66.03% | 66.14% | 66.03% |
| model:gliner-multi-v21 | eligible | People's names | 2097/2245 | 93.41% | 93.41% | 93.41% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 368/1199 | 30.69% | 59.80% | 30.28% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 1267/1468 | 86.31% | 92.17% | 85.08% |
| model:gliner-multi-v21 | eligible | Dates & times | 268/277 | 96.75% | 96.75% | 96.75% |
| model:gliner-multi-v21 | eligible | Organizations | 117/843 | 13.88% | 17.44% | 13.88% |
| model:gliner-multi-v21 | eligible | Network identifiers | 64/762 | 8.40% | 29.79% | 8.40% |
| model:gliner-multi-v21 | eligible | Customer & employee IDs | 64/409 | 15.65% | 15.65% | 15.65% |
| model:gliner-multi-v21+cpu-int8 | eligible | Passwords, keys & tokens | 0/375 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Logins & usernames | 0/229 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Bank accounts & cards | 0/698 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Documents & identifiers | 0/886 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | People's names | 0/2245 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Phone numbers & email | 0/1199 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Addresses & locations | 0/1468 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Organizations | 0/843 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Network identifiers | 0/762 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia | train | Passwords, keys & tokens | 328/375 | 87.47% | 87.73% | 87.47% |
| model:gliner-nvidia | train | Logins & usernames | 220/229 | 96.07% | 100.00% | 96.07% |
| model:gliner-nvidia | train | Bank accounts & cards | 692/698 | 99.14% | 99.14% | 99.14% |
| model:gliner-nvidia | train | Documents & identifiers | 885/886 | 99.89% | 99.89% | 99.89% |
| model:gliner-nvidia | train | People's names | 2237/2245 | 99.64% | 99.69% | 99.64% |
| model:gliner-nvidia | train | Phone numbers & email | 1039/1199 | 86.66% | 99.58% | 86.66% |
| model:gliner-nvidia | train | Addresses & locations | 1457/1468 | 99.25% | 99.59% | 99.11% |
| model:gliner-nvidia | train | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:gliner-nvidia | train | Organizations | 822/843 | 97.51% | 99.29% | 97.51% |
| model:gliner-nvidia | train | Network identifiers | 436/762 | 57.22% | 58.92% | 57.22% |
| model:gliner-nvidia | train | Customer & employee IDs | 408/409 | 99.76% | 99.76% | 99.76% |
| model:gliner-nvidia+cpu-int8 | train | Passwords, keys & tokens | 0/375 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | train | Logins & usernames | 0/229 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | train | Bank accounts & cards | 0/698 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | train | Documents & identifiers | 0/886 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | train | People's names | 0/2245 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | train | Phone numbers & email | 0/1199 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | train | Addresses & locations | 0/1468 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | train | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | train | Organizations | 0/843 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | train | Network identifiers | 0/762 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | train | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+ov100 | train | Passwords, keys & tokens | 328/375 | 87.47% | 90.40% | 87.47% |
| model:gliner-nvidia+ov100 | train | Logins & usernames | 222/229 | 96.94% | 100.00% | 96.94% |
| model:gliner-nvidia+ov100 | train | Bank accounts & cards | 692/698 | 99.14% | 99.14% | 99.14% |
| model:gliner-nvidia+ov100 | train | Documents & identifiers | 885/886 | 99.89% | 99.89% | 99.89% |
| model:gliner-nvidia+ov100 | train | People's names | 2238/2245 | 99.69% | 99.73% | 99.69% |
| model:gliner-nvidia+ov100 | train | Phone numbers & email | 1044/1199 | 87.07% | 99.75% | 87.07% |
| model:gliner-nvidia+ov100 | train | Addresses & locations | 1458/1468 | 99.32% | 99.59% | 99.18% |
| model:gliner-nvidia+ov100 | train | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:gliner-nvidia+ov100 | train | Organizations | 828/843 | 98.22% | 99.29% | 98.22% |
| model:gliner-nvidia+ov100 | train | Network identifiers | 436/762 | 57.22% | 61.68% | 57.22% |
| model:gliner-nvidia+ov100 | train | Customer & employee IDs | 408/409 | 99.76% | 99.76% | 99.76% |
| model:gliner-nvidia+sent300 | train | Passwords, keys & tokens | 329/375 | 87.73% | 88.00% | 87.73% |
| model:gliner-nvidia+sent300 | train | Logins & usernames | 223/229 | 97.38% | 100.00% | 97.38% |
| model:gliner-nvidia+sent300 | train | Bank accounts & cards | 692/698 | 99.14% | 99.14% | 99.14% |
| model:gliner-nvidia+sent300 | train | Documents & identifiers | 880/886 | 99.32% | 99.32% | 99.32% |
| model:gliner-nvidia+sent300 | train | People's names | 2235/2245 | 99.55% | 99.64% | 99.55% |
| model:gliner-nvidia+sent300 | train | Phone numbers & email | 1062/1199 | 88.57% | 99.83% | 88.57% |
| model:gliner-nvidia+sent300 | train | Addresses & locations | 1456/1468 | 99.18% | 99.66% | 99.11% |
| model:gliner-nvidia+sent300 | train | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:gliner-nvidia+sent300 | train | Organizations | 830/843 | 98.46% | 99.64% | 98.46% |
| model:gliner-nvidia+sent300 | train | Network identifiers | 436/762 | 57.22% | 58.40% | 57.22% |
| model:gliner-nvidia+sent300 | train | Customer & employee IDs | 403/409 | 98.53% | 98.53% | 98.53% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 246/375 | 65.60% | 81.07% | 65.33% |
| model:gliner-pii-base | eligible | Logins & usernames | 170/229 | 74.24% | 78.60% | 74.24% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 677/698 | 96.99% | 96.99% | 96.99% |
| model:gliner-pii-base | eligible | Documents & identifiers | 835/886 | 94.24% | 94.81% | 94.24% |
| model:gliner-pii-base | eligible | People's names | 1427/2245 | 63.56% | 63.70% | 63.56% |
| model:gliner-pii-base | eligible | Phone numbers & email | 1169/1199 | 97.50% | 98.50% | 97.50% |
| model:gliner-pii-base | eligible | Addresses & locations | 1275/1468 | 86.85% | 90.33% | 86.78% |
| model:gliner-pii-base | eligible | Dates & times | 275/277 | 99.28% | 99.28% | 99.28% |
| model:gliner-pii-base | eligible | Organizations | 641/843 | 76.04% | 82.56% | 76.04% |
| model:gliner-pii-base | eligible | Network identifiers | 261/762 | 34.25% | 44.36% | 34.25% |
| model:gliner-pii-base | eligible | Customer & employee IDs | 392/409 | 95.84% | 95.84% | 95.84% |
| model:gliner-pii-base+cpu-int8 | eligible | Passwords, keys & tokens | 3/375 | 0.80% | 0.80% | 0.80% |
| model:gliner-pii-base+cpu-int8 | eligible | Logins & usernames | 0/229 | 0.00% | 0.44% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Bank accounts & cards | 89/698 | 12.75% | 12.75% | 12.75% |
| model:gliner-pii-base+cpu-int8 | eligible | Documents & identifiers | 66/886 | 7.45% | 7.45% | 7.45% |
| model:gliner-pii-base+cpu-int8 | eligible | People's names | 6/2245 | 0.27% | 0.27% | 0.27% |
| model:gliner-pii-base+cpu-int8 | eligible | Phone numbers & email | 12/1199 | 1.00% | 1.00% | 1.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Addresses & locations | 45/1468 | 3.07% | 3.07% | 3.07% |
| model:gliner-pii-base+cpu-int8 | eligible | Dates & times | 4/277 | 1.44% | 1.44% | 1.44% |
| model:gliner-pii-base+cpu-int8 | eligible | Organizations | 4/843 | 0.47% | 0.47% | 0.47% |
| model:gliner-pii-base+cpu-int8 | eligible | Network identifiers | 0/762 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Customer & employee IDs | 26/409 | 6.36% | 6.36% | 6.36% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 250/375 | 66.67% | 81.60% | 65.87% |
| model:gliner-pii-edge | eligible | Logins & usernames | 114/229 | 49.78% | 68.12% | 49.78% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 631/698 | 90.40% | 90.54% | 90.40% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 664/886 | 74.94% | 75.40% | 74.83% |
| model:gliner-pii-edge | eligible | People's names | 1597/2245 | 71.14% | 71.45% | 71.14% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 1134/1199 | 94.58% | 97.00% | 94.58% |
| model:gliner-pii-edge | eligible | Addresses & locations | 1200/1468 | 81.74% | 84.67% | 81.74% |
| model:gliner-pii-edge | eligible | Dates & times | 273/277 | 98.56% | 98.56% | 98.56% |
| model:gliner-pii-edge | eligible | Organizations | 456/843 | 54.09% | 66.90% | 54.09% |
| model:gliner-pii-edge | eligible | Network identifiers | 261/762 | 34.25% | 83.86% | 33.86% |
| model:gliner-pii-edge | eligible | Customer & employee IDs | 331/409 | 80.93% | 80.93% | 80.93% |
| model:gliner-pii-edge+cpu-int8 | eligible | Passwords, keys & tokens | 76/375 | 20.27% | 22.67% | 20.27% |
| model:gliner-pii-edge+cpu-int8 | eligible | Logins & usernames | 7/229 | 3.06% | 3.06% | 3.06% |
| model:gliner-pii-edge+cpu-int8 | eligible | Bank accounts & cards | 171/698 | 24.50% | 25.50% | 24.50% |
| model:gliner-pii-edge+cpu-int8 | eligible | Documents & identifiers | 191/886 | 21.56% | 22.12% | 21.56% |
| model:gliner-pii-edge+cpu-int8 | eligible | People's names | 106/2245 | 4.72% | 4.72% | 4.72% |
| model:gliner-pii-edge+cpu-int8 | eligible | Phone numbers & email | 103/1199 | 8.59% | 10.84% | 8.59% |
| model:gliner-pii-edge+cpu-int8 | eligible | Addresses & locations | 513/1468 | 34.95% | 38.22% | 34.88% |
| model:gliner-pii-edge+cpu-int8 | eligible | Dates & times | 215/277 | 77.62% | 77.62% | 77.62% |
| model:gliner-pii-edge+cpu-int8 | eligible | Organizations | 17/843 | 2.02% | 3.32% | 1.90% |
| model:gliner-pii-edge+cpu-int8 | eligible | Network identifiers | 14/762 | 1.84% | 6.82% | 1.84% |
| model:gliner-pii-edge+cpu-int8 | eligible | Customer & employee IDs | 137/409 | 33.50% | 33.50% | 33.50% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 310/375 | 82.67% | 84.27% | 82.67% |
| model:gliner-stream-pii | eligible | Logins & usernames | 224/229 | 97.82% | 97.82% | 97.82% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 542/698 | 77.65% | 97.85% | 77.65% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 838/886 | 94.58% | 97.18% | 94.58% |
| model:gliner-stream-pii | eligible | People's names | 2197/2245 | 97.86% | 97.95% | 97.86% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 1128/1199 | 94.08% | 97.00% | 94.08% |
| model:gliner-stream-pii | eligible | Addresses & locations | 1410/1468 | 96.05% | 97.41% | 95.98% |
| model:gliner-stream-pii | eligible | Dates & times | 275/277 | 99.28% | 99.28% | 99.28% |
| model:gliner-stream-pii | eligible | Organizations | 732/843 | 86.83% | 92.88% | 86.83% |
| model:gliner-stream-pii | eligible | Network identifiers | 398/762 | 52.23% | 65.62% | 52.23% |
| model:gliner-stream-pii | eligible | Customer & employee IDs | 405/409 | 99.02% | 99.02% | 99.02% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 284/375 | 75.73% | 93.07% | 75.73% |
| model:gliner-urchade | eligible | Logins & usernames | 181/229 | 79.04% | 79.04% | 79.04% |
| model:gliner-urchade | eligible | Bank accounts & cards | 670/698 | 95.99% | 95.99% | 95.99% |
| model:gliner-urchade | eligible | Documents & identifiers | 851/886 | 96.05% | 96.16% | 96.05% |
| model:gliner-urchade | eligible | People's names | 557/2245 | 24.81% | 24.81% | 24.81% |
| model:gliner-urchade | eligible | Phone numbers & email | 1148/1199 | 95.75% | 99.42% | 95.75% |
| model:gliner-urchade | eligible | Addresses & locations | 1308/1468 | 89.10% | 90.87% | 89.10% |
| model:gliner-urchade | eligible | Dates & times | 275/277 | 99.28% | 99.28% | 99.28% |
| model:gliner-urchade | eligible | Organizations | 478/843 | 56.70% | 58.84% | 56.70% |
| model:gliner-urchade | eligible | Network identifiers | 421/762 | 55.25% | 63.12% | 55.25% |
| model:gliner-urchade | eligible | Customer & employee IDs | 392/409 | 95.84% | 95.84% | 95.84% |
| model:gliner-urchade+cpu-int8 | eligible | Passwords, keys & tokens | 0/375 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Logins & usernames | 0/229 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Bank accounts & cards | 0/698 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Documents & identifiers | 0/886 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | People's names | 0/2245 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Phone numbers & email | 0/1199 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Addresses & locations | 0/1468 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Organizations | 0/843 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Network identifiers | 0/762 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 294/375 | 78.40% | 94.40% | 78.40% |
| model:gliner2-fastino | eligible | Logins & usernames | 218/229 | 95.20% | 96.94% | 95.20% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 630/698 | 90.26% | 90.26% | 90.26% |
| model:gliner2-fastino | eligible | Documents & identifiers | 861/886 | 97.18% | 97.52% | 97.18% |
| model:gliner2-fastino | eligible | People's names | 2118/2245 | 94.34% | 94.48% | 94.34% |
| model:gliner2-fastino | eligible | Phone numbers & email | 1189/1199 | 99.17% | 99.67% | 99.17% |
| model:gliner2-fastino | eligible | Addresses & locations | 1368/1468 | 93.19% | 98.84% | 91.83% |
| model:gliner2-fastino | eligible | Dates & times | 276/277 | 99.64% | 99.64% | 99.64% |
| model:gliner2-fastino | eligible | Organizations | 821/843 | 97.39% | 99.29% | 97.39% |
| model:gliner2-fastino | eligible | Network identifiers | 315/762 | 41.34% | 44.36% | 41.34% |
| model:gliner2-fastino | eligible | Customer & employee IDs | 400/409 | 97.80% | 97.80% | 97.80% |
| model:gliner2-hivetrace-omni | train | Passwords, keys & tokens | 302/375 | 80.53% | 90.93% | 80.53% |
| model:gliner2-hivetrace-omni | train | Logins & usernames | 179/229 | 78.17% | 90.83% | 78.17% |
| model:gliner2-hivetrace-omni | train | Bank accounts & cards | 676/698 | 96.85% | 96.85% | 96.85% |
| model:gliner2-hivetrace-omni | train | Documents & identifiers | 848/886 | 95.71% | 95.71% | 95.71% |
| model:gliner2-hivetrace-omni | train | People's names | 2213/2245 | 98.57% | 98.84% | 98.57% |
| model:gliner2-hivetrace-omni | train | Phone numbers & email | 1191/1199 | 99.33% | 99.67% | 99.33% |
| model:gliner2-hivetrace-omni | train | Addresses & locations | 1402/1468 | 95.50% | 96.59% | 95.44% |
| model:gliner2-hivetrace-omni | train | Dates & times | 276/277 | 99.64% | 99.64% | 99.64% |
| model:gliner2-hivetrace-omni | train | Organizations | 816/843 | 96.80% | 97.98% | 96.80% |
| model:gliner2-hivetrace-omni | train | Network identifiers | 219/762 | 28.74% | 29.00% | 28.74% |
| model:gliner2-hivetrace-omni | train | Customer & employee IDs | 405/409 | 99.02% | 99.02% | 99.02% |
| model:gliner2-hivetrace-uni | train | Passwords, keys & tokens | 265/375 | 70.67% | 73.07% | 70.67% |
| model:gliner2-hivetrace-uni | train | Logins & usernames | 178/229 | 77.73% | 96.07% | 77.73% |
| model:gliner2-hivetrace-uni | train | Bank accounts & cards | 532/698 | 76.22% | 76.22% | 76.22% |
| model:gliner2-hivetrace-uni | train | Documents & identifiers | 864/886 | 97.52% | 97.63% | 97.52% |
| model:gliner2-hivetrace-uni | train | People's names | 1783/2245 | 79.42% | 79.47% | 79.42% |
| model:gliner2-hivetrace-uni | train | Phone numbers & email | 1189/1199 | 99.17% | 99.25% | 99.17% |
| model:gliner2-hivetrace-uni | train | Addresses & locations | 1224/1468 | 83.38% | 84.13% | 83.31% |
| model:gliner2-hivetrace-uni | train | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:gliner2-hivetrace-uni | train | Organizations | 134/843 | 15.90% | 22.06% | 15.90% |
| model:gliner2-hivetrace-uni | train | Network identifiers | 77/762 | 10.10% | 10.24% | 10.10% |
| model:gliner2-hivetrace-uni | train | Customer & employee IDs | 407/409 | 99.51% | 99.51% | 99.51% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 275/375 | 73.33% | 94.40% | 72.27% |
| model:gliner2-large | eligible | Logins & usernames | 214/229 | 93.45% | 96.94% | 93.01% |
| model:gliner2-large | eligible | Bank accounts & cards | 654/698 | 93.70% | 94.13% | 93.70% |
| model:gliner2-large | eligible | Documents & identifiers | 844/886 | 95.26% | 95.60% | 95.26% |
| model:gliner2-large | eligible | People's names | 2071/2245 | 92.25% | 92.25% | 92.25% |
| model:gliner2-large | eligible | Phone numbers & email | 1188/1199 | 99.08% | 99.67% | 99.08% |
| model:gliner2-large | eligible | Addresses & locations | 1381/1468 | 94.07% | 96.59% | 93.87% |
| model:gliner2-large | eligible | Dates & times | 274/277 | 98.92% | 98.92% | 98.92% |
| model:gliner2-large | eligible | Organizations | 823/843 | 97.63% | 98.93% | 97.63% |
| model:gliner2-large | eligible | Network identifiers | 446/762 | 58.53% | 60.50% | 58.53% |
| model:gliner2-large | eligible | Customer & employee IDs | 393/409 | 96.09% | 96.09% | 96.09% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 262/375 | 69.87% | 77.87% | 69.87% |
| model:gliner2-vladlinv | eligible | Logins & usernames | 206/229 | 89.96% | 90.39% | 89.96% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 420/698 | 60.17% | 60.32% | 60.17% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 789/886 | 89.05% | 89.16% | 89.05% |
| model:gliner2-vladlinv | eligible | People's names | 2157/2245 | 96.08% | 96.08% | 96.08% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 1113/1199 | 92.83% | 92.91% | 92.83% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 310/1468 | 21.12% | 21.12% | 21.05% |
| model:gliner2-vladlinv | eligible | Dates & times | 276/277 | 99.64% | 99.64% | 99.64% |
| model:gliner2-vladlinv | eligible | Organizations | 5/843 | 0.59% | 1.30% | 0.59% |
| model:gliner2-vladlinv | eligible | Network identifiers | 35/762 | 4.59% | 4.59% | 4.59% |
| model:gliner2-vladlinv | eligible | Customer & employee IDs | 389/409 | 95.11% | 95.11% | 95.11% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 294/375 | 78.40% | 89.07% | 78.40% |
| model:gliner25-fastino | eligible | Logins & usernames | 185/229 | 80.79% | 92.14% | 80.79% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 514/698 | 73.64% | 73.78% | 73.64% |
| model:gliner25-fastino | eligible | Documents & identifiers | 517/886 | 58.35% | 58.58% | 58.35% |
| model:gliner25-fastino | eligible | People's names | 2097/2245 | 93.41% | 93.59% | 93.41% |
| model:gliner25-fastino | eligible | Phone numbers & email | 1188/1199 | 99.08% | 99.58% | 99.08% |
| model:gliner25-fastino | eligible | Addresses & locations | 634/1468 | 43.19% | 46.25% | 42.57% |
| model:gliner25-fastino | eligible | Dates & times | 108/277 | 38.99% | 38.99% | 38.99% |
| model:gliner25-fastino | eligible | Organizations | 222/843 | 26.33% | 32.50% | 26.33% |
| model:gliner25-fastino | eligible | Network identifiers | 459/762 | 60.24% | 60.76% | 60.24% |
| model:gliner25-fastino | eligible | Customer & employee IDs | 392/409 | 95.84% | 95.84% | 95.84% |
| model:gliner25-fastino+nochunk | eligible | Passwords, keys & tokens | 297/375 | 79.20% | 90.40% | 79.20% |
| model:gliner25-fastino+nochunk | eligible | Logins & usernames | 190/229 | 82.97% | 91.27% | 80.79% |
| model:gliner25-fastino+nochunk | eligible | Bank accounts & cards | 533/698 | 76.36% | 76.50% | 76.36% |
| model:gliner25-fastino+nochunk | eligible | Documents & identifiers | 537/886 | 60.61% | 60.84% | 60.61% |
| model:gliner25-fastino+nochunk | eligible | People's names | 2020/2245 | 89.98% | 90.24% | 89.98% |
| model:gliner25-fastino+nochunk | eligible | Phone numbers & email | 1188/1199 | 99.08% | 99.17% | 99.08% |
| model:gliner25-fastino+nochunk | eligible | Addresses & locations | 814/1468 | 55.45% | 58.04% | 55.18% |
| model:gliner25-fastino+nochunk | eligible | Dates & times | 138/277 | 49.82% | 49.82% | 49.82% |
| model:gliner25-fastino+nochunk | eligible | Organizations | 378/843 | 44.84% | 48.75% | 44.84% |
| model:gliner25-fastino+nochunk | eligible | Network identifiers | 481/762 | 63.12% | 64.04% | 63.12% |
| model:gliner25-fastino+nochunk | eligible | Customer & employee IDs | 392/409 | 95.84% | 95.84% | 95.84% |
| model:gliner25-fastino+ov100 | eligible | Passwords, keys & tokens | 297/375 | 79.20% | 92.00% | 79.20% |
| model:gliner25-fastino+ov100 | eligible | Logins & usernames | 187/229 | 81.66% | 92.58% | 81.22% |
| model:gliner25-fastino+ov100 | eligible | Bank accounts & cards | 524/698 | 75.07% | 75.64% | 75.07% |
| model:gliner25-fastino+ov100 | eligible | Documents & identifiers | 528/886 | 59.59% | 59.82% | 59.48% |
| model:gliner25-fastino+ov100 | eligible | People's names | 2101/2245 | 93.59% | 93.81% | 93.59% |
| model:gliner25-fastino+ov100 | eligible | Phone numbers & email | 1188/1199 | 99.08% | 99.58% | 99.08% |
| model:gliner25-fastino+ov100 | eligible | Addresses & locations | 680/1468 | 46.32% | 49.46% | 45.64% |
| model:gliner25-fastino+ov100 | eligible | Dates & times | 116/277 | 41.88% | 41.88% | 41.52% |
| model:gliner25-fastino+ov100 | eligible | Organizations | 212/843 | 25.15% | 30.49% | 25.03% |
| model:gliner25-fastino+ov100 | eligible | Network identifiers | 464/762 | 60.89% | 62.20% | 60.89% |
| model:gliner25-fastino+ov100 | eligible | Customer & employee IDs | 392/409 | 95.84% | 95.84% | 95.84% |
| model:gliner25-fastino+sent300 | eligible | Passwords, keys & tokens | 281/375 | 74.93% | 83.73% | 74.93% |
| model:gliner25-fastino+sent300 | eligible | Logins & usernames | 179/229 | 78.17% | 91.70% | 78.17% |
| model:gliner25-fastino+sent300 | eligible | Bank accounts & cards | 497/698 | 71.20% | 71.35% | 71.20% |
| model:gliner25-fastino+sent300 | eligible | Documents & identifiers | 503/886 | 56.77% | 56.88% | 56.77% |
| model:gliner25-fastino+sent300 | eligible | People's names | 2142/2245 | 95.41% | 95.72% | 95.41% |
| model:gliner25-fastino+sent300 | eligible | Phone numbers & email | 1188/1199 | 99.08% | 99.58% | 99.08% |
| model:gliner25-fastino+sent300 | eligible | Addresses & locations | 513/1468 | 34.95% | 38.35% | 34.20% |
| model:gliner25-fastino+sent300 | eligible | Dates & times | 70/277 | 25.27% | 25.27% | 25.27% |
| model:gliner25-fastino+sent300 | eligible | Organizations | 226/843 | 26.81% | 34.05% | 26.81% |
| model:gliner25-fastino+sent300 | eligible | Network identifiers | 380/762 | 49.87% | 51.57% | 49.87% |
| model:gliner25-fastino+sent300 | eligible | Customer & employee IDs | 385/409 | 94.13% | 94.13% | 94.13% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 286/375 | 76.27% | 85.07% | 72.27% |
| model:gravitee-small | eligible | Logins & usernames | 56/229 | 24.45% | 27.95% | 18.78% |
| model:gravitee-small | eligible | Bank accounts & cards | 656/698 | 93.98% | 94.99% | 92.98% |
| model:gravitee-small | eligible | Documents & identifiers | 254/886 | 28.67% | 31.15% | 27.31% |
| model:gravitee-small | eligible | People's names | 1975/2245 | 87.97% | 88.15% | 87.39% |
| model:gravitee-small | eligible | Phone numbers & email | 1146/1199 | 95.58% | 97.41% | 95.41% |
| model:gravitee-small | eligible | Addresses & locations | 1090/1468 | 74.25% | 77.86% | 72.82% |
| model:gravitee-small | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:gravitee-small | eligible | Organizations | 555/843 | 65.84% | 74.85% | 63.11% |
| model:gravitee-small | eligible | Network identifiers | 379/762 | 49.74% | 90.42% | 48.43% |
| model:gravitee-small | eligible | Customer & employee IDs | 15/409 | 3.67% | 3.91% | 3.18% |
| model:gravitee-small+cpu-int8 | eligible | Passwords, keys & tokens | 276/375 | 73.60% | 82.67% | 70.40% |
| model:gravitee-small+cpu-int8 | eligible | Logins & usernames | 52/229 | 22.71% | 27.95% | 17.90% |
| model:gravitee-small+cpu-int8 | eligible | Bank accounts & cards | 653/698 | 93.55% | 94.41% | 92.12% |
| model:gravitee-small+cpu-int8 | eligible | Documents & identifiers | 255/886 | 28.78% | 30.70% | 27.31% |
| model:gravitee-small+cpu-int8 | eligible | People's names | 1951/2245 | 86.90% | 86.99% | 86.50% |
| model:gravitee-small+cpu-int8 | eligible | Phone numbers & email | 1143/1199 | 95.33% | 97.41% | 94.66% |
| model:gravitee-small+cpu-int8 | eligible | Addresses & locations | 1069/1468 | 72.82% | 76.29% | 71.25% |
| model:gravitee-small+cpu-int8 | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:gravitee-small+cpu-int8 | eligible | Organizations | 562/843 | 66.67% | 75.33% | 63.46% |
| model:gravitee-small+cpu-int8 | eligible | Network identifiers | 353/762 | 46.33% | 87.93% | 44.62% |
| model:gravitee-small+cpu-int8 | eligible | Customer & employee IDs | 14/409 | 3.42% | 3.42% | 2.44% |
| model:kalyan-ettin | train | Passwords, keys & tokens | 361/375 | 96.27% | 98.40% | 94.13% |
| model:kalyan-ettin | train | Logins & usernames | 228/229 | 99.56% | 99.56% | 95.63% |
| model:kalyan-ettin | train | Bank accounts & cards | 689/698 | 98.71% | 99.14% | 96.70% |
| model:kalyan-ettin | train | Documents & identifiers | 857/886 | 96.73% | 99.21% | 94.24% |
| model:kalyan-ettin | train | People's names | 2161/2245 | 96.26% | 96.48% | 95.90% |
| model:kalyan-ettin | train | Phone numbers & email | 1175/1199 | 98.00% | 99.42% | 96.83% |
| model:kalyan-ettin | train | Addresses & locations | 1386/1468 | 94.41% | 96.59% | 93.94% |
| model:kalyan-ettin | train | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:kalyan-ettin | train | Organizations | 666/843 | 79.00% | 95.14% | 76.16% |
| model:kalyan-ettin | train | Network identifiers | 470/762 | 61.68% | 98.56% | 58.53% |
| model:kalyan-ettin | train | Customer & employee IDs | 408/409 | 99.76% | 99.76% | 97.80% |
| model:kalyan-ettin+cpu-int8 | train | Passwords, keys & tokens | 269/375 | 71.73% | 85.87% | 46.40% |
| model:kalyan-ettin+cpu-int8 | train | Logins & usernames | 180/229 | 78.60% | 88.65% | 48.91% |
| model:kalyan-ettin+cpu-int8 | train | Bank accounts & cards | 461/698 | 66.05% | 79.94% | 33.67% |
| model:kalyan-ettin+cpu-int8 | train | Documents & identifiers | 544/886 | 61.40% | 82.28% | 39.50% |
| model:kalyan-ettin+cpu-int8 | train | People's names | 1955/2245 | 87.08% | 87.31% | 79.15% |
| model:kalyan-ettin+cpu-int8 | train | Phone numbers & email | 804/1199 | 67.06% | 94.33% | 41.12% |
| model:kalyan-ettin+cpu-int8 | train | Addresses & locations | 920/1468 | 62.67% | 74.18% | 55.86% |
| model:kalyan-ettin+cpu-int8 | train | Dates & times | 69/277 | 24.91% | 91.70% | 18.77% |
| model:kalyan-ettin+cpu-int8 | train | Organizations | 447/843 | 53.02% | 80.31% | 44.13% |
| model:kalyan-ettin+cpu-int8 | train | Network identifiers | 75/762 | 9.84% | 81.23% | 4.72% |
| model:kalyan-ettin+cpu-int8 | train | Customer & employee IDs | 350/409 | 85.57% | 89.00% | 61.86% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 183/375 | 48.80% | 84.27% | 7.20% |
| model:mmbert32k | eligible | Logins & usernames | 171/229 | 74.67% | 82.53% | 48.47% |
| model:mmbert32k | eligible | Bank accounts & cards | 535/698 | 76.65% | 90.54% | 29.08% |
| model:mmbert32k | eligible | Documents & identifiers | 496/886 | 55.98% | 97.63% | 9.48% |
| model:mmbert32k | eligible | People's names | 2037/2245 | 90.73% | 90.78% | 89.44% |
| model:mmbert32k | eligible | Phone numbers & email | 793/1199 | 66.14% | 99.25% | 45.87% |
| model:mmbert32k | eligible | Addresses & locations | 607/1468 | 41.35% | 54.97% | 38.22% |
| model:mmbert32k | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 99.28% |
| model:mmbert32k | eligible | Organizations | 313/843 | 37.13% | 82.21% | 32.98% |
| model:mmbert32k | eligible | Network identifiers | 116/762 | 15.22% | 99.61% | 8.14% |
| model:mmbert32k | eligible | Customer & employee IDs | 295/409 | 72.13% | 85.09% | 13.20% |
| model:mmbert32k+cpu-int8 | eligible | Passwords, keys & tokens | 172/375 | 45.87% | 81.60% | 1.33% |
| model:mmbert32k+cpu-int8 | eligible | Logins & usernames | 82/229 | 35.81% | 53.71% | 3.06% |
| model:mmbert32k+cpu-int8 | eligible | Bank accounts & cards | 411/698 | 58.88% | 90.26% | 3.44% |
| model:mmbert32k+cpu-int8 | eligible | Documents & identifiers | 358/886 | 40.41% | 95.94% | 1.02% |
| model:mmbert32k+cpu-int8 | eligible | People's names | 970/2245 | 43.21% | 43.79% | 34.48% |
| model:mmbert32k+cpu-int8 | eligible | Phone numbers & email | 234/1199 | 19.52% | 84.49% | 2.75% |
| model:mmbert32k+cpu-int8 | eligible | Addresses & locations | 438/1468 | 29.84% | 49.05% | 22.75% |
| model:mmbert32k+cpu-int8 | eligible | Dates & times | 88/277 | 31.77% | 94.95% | 3.97% |
| model:mmbert32k+cpu-int8 | eligible | Organizations | 163/843 | 19.34% | 50.53% | 7.95% |
| model:mmbert32k+cpu-int8 | eligible | Network identifiers | 4/762 | 0.52% | 90.68% | 0.00% |
| model:mmbert32k+cpu-int8 | eligible | Customer & employee IDs | 304/409 | 74.33% | 89.73% | 1.47% |
| model:mmbert32k+nochunk | eligible | Passwords, keys & tokens | 170/375 | 45.33% | 83.47% | 4.53% |
| model:mmbert32k+nochunk | eligible | Logins & usernames | 156/229 | 68.12% | 79.48% | 39.30% |
| model:mmbert32k+nochunk | eligible | Bank accounts & cards | 509/698 | 72.92% | 90.83% | 24.93% |
| model:mmbert32k+nochunk | eligible | Documents & identifiers | 493/886 | 55.64% | 96.73% | 7.11% |
| model:mmbert32k+nochunk | eligible | People's names | 1930/2245 | 85.97% | 86.06% | 83.83% |
| model:mmbert32k+nochunk | eligible | Phone numbers & email | 665/1199 | 55.46% | 97.66% | 38.20% |
| model:mmbert32k+nochunk | eligible | Addresses & locations | 521/1468 | 35.49% | 48.37% | 30.93% |
| model:mmbert32k+nochunk | eligible | Dates & times | 273/277 | 98.56% | 100.00% | 96.03% |
| model:mmbert32k+nochunk | eligible | Organizations | 220/843 | 26.10% | 71.53% | 20.17% |
| model:mmbert32k+nochunk | eligible | Network identifiers | 85/762 | 11.15% | 98.56% | 5.77% |
| model:mmbert32k+nochunk | eligible | Customer & employee IDs | 309/409 | 75.55% | 88.02% | 11.25% |
| model:natasha | eligible | Passwords, keys & tokens | 0/375 | 0.00% | 3.73% | 0.00% |
| model:natasha | eligible | Logins & usernames | 2/229 | 0.87% | 1.31% | 0.87% |
| model:natasha | eligible | Bank accounts & cards | 0/698 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 3/886 | 0.34% | 0.34% | 0.11% |
| model:natasha | eligible | People's names | 288/2245 | 12.83% | 12.83% | 12.83% |
| model:natasha | eligible | Phone numbers & email | 0/1199 | 0.00% | 0.17% | 0.00% |
| model:natasha | eligible | Addresses & locations | 338/1468 | 23.02% | 23.43% | 23.02% |
| model:natasha | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Organizations | 56/843 | 6.64% | 7.35% | 6.64% |
| model:natasha | eligible | Network identifiers | 0/762 | 0.00% | 0.92% | 0.00% |
| model:natasha | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 4/375 | 1.07% | 1.87% | 0.00% |
| model:ner-ru-gherman | eligible | Logins & usernames | 53/229 | 23.14% | 39.74% | 7.42% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 0/698 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/886 | 0.00% | 0.11% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 2095/2245 | 93.32% | 93.94% | 92.38% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/1199 | 0.00% | 20.68% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 842/1468 | 57.36% | 77.66% | 55.04% |
| model:ner-ru-gherman | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Organizations | 3/843 | 0.36% | 15.18% | 0.12% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/762 | 0.00% | 2.10% | 0.00% |
| model:ner-ru-gherman | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Passwords, keys & tokens | 4/375 | 1.07% | 1.60% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Logins & usernames | 47/229 | 20.52% | 34.93% | 5.68% |
| model:ner-ru-gherman+cpu-int8 | eligible | Bank accounts & cards | 0/698 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Documents & identifiers | 0/886 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | People's names | 2012/2245 | 89.62% | 90.07% | 88.64% |
| model:ner-ru-gherman+cpu-int8 | eligible | Phone numbers & email | 0/1199 | 0.00% | 15.18% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Addresses & locations | 819/1468 | 55.79% | 71.39% | 55.18% |
| model:ner-ru-gherman+cpu-int8 | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Organizations | 1/843 | 0.12% | 14.35% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Network identifiers | 0/762 | 0.00% | 1.57% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Passwords, keys & tokens | 4/375 | 1.07% | 1.87% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Logins & usernames | 49/229 | 21.40% | 37.99% | 6.11% |
| model:ner-ru-gherman-onnx | eligible | Bank accounts & cards | 0/698 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Documents & identifiers | 0/886 | 0.00% | 0.11% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | People's names | 2089/2245 | 93.05% | 93.50% | 92.12% |
| model:ner-ru-gherman-onnx | eligible | Phone numbers & email | 0/1199 | 0.00% | 20.10% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Addresses & locations | 842/1468 | 57.36% | 77.11% | 55.59% |
| model:ner-ru-gherman-onnx | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Organizations | 2/843 | 0.24% | 14.59% | 0.12% |
| model:ner-ru-gherman-onnx | eligible | Network identifiers | 0/762 | 0.00% | 2.10% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 64/375 | 17.07% | 25.07% | 13.33% |
| model:ner-ru-yqelz | eligible | Logins & usernames | 65/229 | 28.38% | 33.19% | 15.72% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 179/698 | 25.64% | 30.52% | 14.76% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 57/886 | 6.43% | 10.05% | 2.82% |
| model:ner-ru-yqelz | eligible | People's names | 1604/2245 | 71.45% | 71.54% | 68.29% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 16/1199 | 1.33% | 14.26% | 0.75% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 1149/1468 | 78.27% | 84.67% | 74.52% |
| model:ner-ru-yqelz | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Organizations | 644/843 | 76.39% | 83.63% | 69.40% |
| model:ner-ru-yqelz | eligible | Network identifiers | 24/762 | 3.15% | 25.46% | 2.23% |
| model:ner-ru-yqelz | eligible | Customer & employee IDs | 3/409 | 0.73% | 1.22% | 0.24% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 304/375 | 81.07% | 95.73% | 77.87% |
| model:nuner-zero | eligible | Logins & usernames | 212/229 | 92.58% | 92.58% | 92.58% |
| model:nuner-zero | eligible | Bank accounts & cards | 672/698 | 96.28% | 96.56% | 70.92% |
| model:nuner-zero | eligible | Documents & identifiers | 862/886 | 97.29% | 97.29% | 90.07% |
| model:nuner-zero | eligible | People's names | 748/2245 | 33.32% | 33.32% | 33.05% |
| model:nuner-zero | eligible | Phone numbers & email | 1179/1199 | 98.33% | 99.83% | 84.40% |
| model:nuner-zero | eligible | Addresses & locations | 1373/1468 | 93.53% | 95.23% | 56.61% |
| model:nuner-zero | eligible | Dates & times | 276/277 | 99.64% | 99.64% | 99.64% |
| model:nuner-zero | eligible | Organizations | 588/843 | 69.75% | 75.80% | 14.47% |
| model:nuner-zero | eligible | Network identifiers | 741/762 | 97.24% | 99.61% | 97.11% |
| model:nuner-zero | eligible | Customer & employee IDs | 401/409 | 98.04% | 98.04% | 98.04% |
| model:nym-base | eligible | Passwords, keys & tokens | 277/375 | 73.87% | 96.00% | 60.53% |
| model:nym-base | eligible | Logins & usernames | 216/229 | 94.32% | 95.63% | 93.45% |
| model:nym-base | eligible | Bank accounts & cards | 686/698 | 98.28% | 98.85% | 96.56% |
| model:nym-base | eligible | Documents & identifiers | 673/886 | 75.96% | 79.46% | 68.17% |
| model:nym-base | eligible | People's names | 2199/2245 | 97.95% | 98.08% | 97.77% |
| model:nym-base | eligible | Phone numbers & email | 1011/1199 | 84.32% | 99.33% | 82.40% |
| model:nym-base | eligible | Addresses & locations | 1261/1468 | 85.90% | 96.05% | 86.65% |
| model:nym-base | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:nym-base | eligible | Organizations | 525/843 | 62.28% | 77.22% | 61.92% |
| model:nym-base | eligible | Network identifiers | 276/762 | 36.22% | 55.64% | 34.91% |
| model:nym-base | eligible | Customer & employee IDs | 393/409 | 96.09% | 96.58% | 89.98% |
| model:nym-base+cpu-int8 | eligible | Passwords, keys & tokens | 269/375 | 71.73% | 94.40% | 58.93% |
| model:nym-base+cpu-int8 | eligible | Logins & usernames | 209/229 | 91.27% | 93.89% | 86.46% |
| model:nym-base+cpu-int8 | eligible | Bank accounts & cards | 683/698 | 97.85% | 99.14% | 94.56% |
| model:nym-base+cpu-int8 | eligible | Documents & identifiers | 693/886 | 78.22% | 84.76% | 69.30% |
| model:nym-base+cpu-int8 | eligible | People's names | 2154/2245 | 95.95% | 96.08% | 95.41% |
| model:nym-base+cpu-int8 | eligible | Phone numbers & email | 1023/1199 | 85.32% | 99.33% | 83.32% |
| model:nym-base+cpu-int8 | eligible | Addresses & locations | 1197/1468 | 81.54% | 92.10% | 81.81% |
| model:nym-base+cpu-int8 | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:nym-base+cpu-int8 | eligible | Organizations | 432/843 | 51.25% | 68.45% | 49.35% |
| model:nym-base+cpu-int8 | eligible | Network identifiers | 298/762 | 39.11% | 66.80% | 36.22% |
| model:nym-base+cpu-int8 | eligible | Customer & employee IDs | 389/409 | 95.11% | 95.60% | 83.37% |
| model:nym-base+ov100 | eligible | Passwords, keys & tokens | 275/375 | 73.33% | 96.27% | 61.07% |
| model:nym-base+ov100 | eligible | Logins & usernames | 217/229 | 94.76% | 95.63% | 93.45% |
| model:nym-base+ov100 | eligible | Bank accounts & cards | 683/698 | 97.85% | 98.57% | 95.99% |
| model:nym-base+ov100 | eligible | Documents & identifiers | 673/886 | 75.96% | 79.46% | 67.49% |
| model:nym-base+ov100 | eligible | People's names | 2196/2245 | 97.82% | 97.95% | 97.64% |
| model:nym-base+ov100 | eligible | Phone numbers & email | 1014/1199 | 84.57% | 99.42% | 82.65% |
| model:nym-base+ov100 | eligible | Addresses & locations | 1265/1468 | 86.17% | 96.12% | 86.99% |
| model:nym-base+ov100 | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:nym-base+ov100 | eligible | Organizations | 508/843 | 60.26% | 74.97% | 60.02% |
| model:nym-base+ov100 | eligible | Network identifiers | 270/762 | 35.43% | 55.51% | 33.60% |
| model:nym-base+ov100 | eligible | Customer & employee IDs | 394/409 | 96.33% | 97.07% | 87.78% |
| model:nym-base+sent300 | eligible | Passwords, keys & tokens | 278/375 | 74.13% | 97.33% | 61.87% |
| model:nym-base+sent300 | eligible | Logins & usernames | 220/229 | 96.07% | 96.94% | 94.32% |
| model:nym-base+sent300 | eligible | Bank accounts & cards | 687/698 | 98.42% | 99.28% | 96.13% |
| model:nym-base+sent300 | eligible | Documents & identifiers | 669/886 | 75.51% | 80.02% | 67.38% |
| model:nym-base+sent300 | eligible | People's names | 2201/2245 | 98.04% | 98.08% | 97.82% |
| model:nym-base+sent300 | eligible | Phone numbers & email | 1028/1199 | 85.74% | 99.33% | 84.40% |
| model:nym-base+sent300 | eligible | Addresses & locations | 1264/1468 | 86.10% | 95.98% | 86.85% |
| model:nym-base+sent300 | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:nym-base+sent300 | eligible | Organizations | 575/843 | 68.21% | 80.78% | 68.21% |
| model:nym-base+sent300 | eligible | Network identifiers | 306/762 | 40.16% | 65.49% | 37.66% |
| model:nym-base+sent300 | eligible | Customer & employee IDs | 387/409 | 94.62% | 95.60% | 87.29% |
| model:nym-small | eligible | Passwords, keys & tokens | 278/375 | 74.13% | 95.73% | 61.60% |
| model:nym-small | eligible | Logins & usernames | 205/229 | 89.52% | 91.70% | 85.15% |
| model:nym-small | eligible | Bank accounts & cards | 689/698 | 98.71% | 99.14% | 96.99% |
| model:nym-small | eligible | Documents & identifiers | 660/886 | 74.49% | 82.84% | 68.40% |
| model:nym-small | eligible | People's names | 2166/2245 | 96.48% | 96.53% | 96.17% |
| model:nym-small | eligible | Phone numbers & email | 1141/1199 | 95.16% | 99.33% | 93.24% |
| model:nym-small | eligible | Addresses & locations | 1246/1468 | 84.88% | 94.21% | 85.63% |
| model:nym-small | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:nym-small | eligible | Organizations | 472/843 | 55.99% | 72.00% | 56.70% |
| model:nym-small | eligible | Network identifiers | 296/762 | 38.85% | 65.35% | 36.48% |
| model:nym-small | eligible | Customer & employee IDs | 382/409 | 93.40% | 94.38% | 86.80% |
| model:openai-base | eligible | Passwords, keys & tokens | 275/375 | 73.33% | 85.60% | 70.67% |
| model:openai-base | eligible | Logins & usernames | 203/229 | 88.65% | 88.65% | 87.34% |
| model:openai-base | eligible | Bank accounts & cards | 588/698 | 84.24% | 85.10% | 83.38% |
| model:openai-base | eligible | Documents & identifiers | 832/886 | 93.91% | 95.26% | 92.66% |
| model:openai-base | eligible | People's names | 2017/2245 | 89.84% | 89.89% | 89.62% |
| model:openai-base | eligible | Phone numbers & email | 1121/1199 | 93.49% | 94.50% | 93.58% |
| model:openai-base | eligible | Addresses & locations | 484/1468 | 32.97% | 35.08% | 32.63% |
| model:openai-base | eligible | Dates & times | 272/277 | 98.19% | 98.56% | 98.19% |
| model:openai-base | eligible | Organizations | 27/843 | 3.20% | 3.91% | 2.73% |
| model:openai-base | eligible | Network identifiers | 285/762 | 37.40% | 41.73% | 36.35% |
| model:openai-base | eligible | Customer & employee IDs | 342/409 | 83.62% | 84.84% | 81.66% |
| model:openai-base-onnx | eligible | Passwords, keys & tokens | 275/375 | 73.33% | 85.07% | 70.93% |
| model:openai-base-onnx | eligible | Logins & usernames | 203/229 | 88.65% | 88.65% | 87.34% |
| model:openai-base-onnx | eligible | Bank accounts & cards | 589/698 | 84.38% | 85.24% | 83.67% |
| model:openai-base-onnx | eligible | Documents & identifiers | 835/886 | 94.24% | 95.37% | 93.12% |
| model:openai-base-onnx | eligible | People's names | 2016/2245 | 89.80% | 89.84% | 89.67% |
| model:openai-base-onnx | eligible | Phone numbers & email | 1123/1199 | 93.66% | 94.50% | 93.58% |
| model:openai-base-onnx | eligible | Addresses & locations | 488/1468 | 33.24% | 35.35% | 32.56% |
| model:openai-base-onnx | eligible | Dates & times | 273/277 | 98.56% | 98.92% | 98.56% |
| model:openai-base-onnx | eligible | Organizations | 28/843 | 3.32% | 4.27% | 2.97% |
| model:openai-base-onnx | eligible | Network identifiers | 281/762 | 36.88% | 41.73% | 35.70% |
| model:openai-base-onnx | eligible | Customer & employee IDs | 346/409 | 84.60% | 85.57% | 81.66% |
| model:openmed-multilingual | train | Passwords, keys & tokens | 366/375 | 97.60% | 99.47% | 96.27% |
| model:openmed-multilingual | train | Logins & usernames | 227/229 | 99.13% | 100.00% | 95.20% |
| model:openmed-multilingual | train | Bank accounts & cards | 696/698 | 99.71% | 99.86% | 99.57% |
| model:openmed-multilingual | train | Documents & identifiers | 878/886 | 99.10% | 99.55% | 98.76% |
| model:openmed-multilingual | train | People's names | 2184/2245 | 97.28% | 97.42% | 96.79% |
| model:openmed-multilingual | train | Phone numbers & email | 1189/1199 | 99.17% | 99.42% | 98.75% |
| model:openmed-multilingual | train | Addresses & locations | 1379/1468 | 93.94% | 96.19% | 94.41% |
| model:openmed-multilingual | train | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:openmed-multilingual | train | Organizations | 611/843 | 72.48% | 90.51% | 69.87% |
| model:openmed-multilingual | train | Network identifiers | 758/762 | 99.48% | 100.00% | 98.95% |
| model:openmed-multilingual | train | Customer & employee IDs | 408/409 | 99.76% | 100.00% | 99.27% |
| model:openmed-nemotron | train | Passwords, keys & tokens | 370/375 | 98.67% | 99.20% | 98.13% |
| model:openmed-nemotron | train | Logins & usernames | 228/229 | 99.56% | 100.00% | 99.13% |
| model:openmed-nemotron | train | Bank accounts & cards | 697/698 | 99.86% | 99.86% | 99.14% |
| model:openmed-nemotron | train | Documents & identifiers | 876/886 | 98.87% | 99.55% | 98.19% |
| model:openmed-nemotron | train | People's names | 2216/2245 | 98.71% | 98.98% | 98.40% |
| model:openmed-nemotron | train | Phone numbers & email | 1189/1199 | 99.17% | 99.42% | 98.92% |
| model:openmed-nemotron | train | Addresses & locations | 1409/1468 | 95.98% | 97.68% | 95.57% |
| model:openmed-nemotron | train | Dates & times | 277/277 | 100.00% | 100.00% | 100.00% |
| model:openmed-nemotron | train | Organizations | 715/843 | 84.82% | 92.76% | 83.27% |
| model:openmed-nemotron | train | Network identifiers | 757/762 | 99.34% | 100.00% | 99.21% |
| model:openmed-nemotron | train | Customer & employee IDs | 408/409 | 99.76% | 99.76% | 98.53% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 288/375 | 76.80% | 92.00% | 74.93% |
| model:opf-kz-ru | eligible | Logins & usernames | 189/229 | 82.53% | 84.72% | 80.79% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 645/698 | 92.41% | 94.13% | 93.12% |
| model:opf-kz-ru | eligible | Documents & identifiers | 869/886 | 98.08% | 99.32% | 97.74% |
| model:opf-kz-ru | eligible | People's names | 1887/2245 | 84.05% | 84.19% | 83.03% |
| model:opf-kz-ru | eligible | Phone numbers & email | 1163/1199 | 97.00% | 98.25% | 96.91% |
| model:opf-kz-ru | eligible | Addresses & locations | 557/1468 | 37.94% | 41.35% | 37.13% |
| model:opf-kz-ru | eligible | Dates & times | 276/277 | 99.64% | 99.64% | 99.64% |
| model:opf-kz-ru | eligible | Organizations | 33/843 | 3.91% | 5.69% | 2.61% |
| model:opf-kz-ru | eligible | Network identifiers | 420/762 | 55.12% | 69.82% | 53.02% |
| model:opf-kz-ru | eligible | Customer & employee IDs | 377/409 | 92.18% | 93.89% | 89.49% |
| model:opf-ru | eligible | Passwords, keys & tokens | 293/375 | 78.13% | 94.93% | 66.93% |
| model:opf-ru | eligible | Logins & usernames | 218/229 | 95.20% | 97.38% | 89.96% |
| model:opf-ru | eligible | Bank accounts & cards | 542/698 | 77.65% | 87.97% | 54.30% |
| model:opf-ru | eligible | Documents & identifiers | 676/886 | 76.30% | 93.45% | 59.14% |
| model:opf-ru | eligible | People's names | 1961/2245 | 87.35% | 87.39% | 86.15% |
| model:opf-ru | eligible | Phone numbers & email | 1112/1199 | 92.74% | 97.00% | 91.24% |
| model:opf-ru | eligible | Addresses & locations | 375/1468 | 25.54% | 38.76% | 22.48% |
| model:opf-ru | eligible | Dates & times | 273/277 | 98.56% | 99.64% | 98.56% |
| model:opf-ru | eligible | Organizations | 53/843 | 6.29% | 11.39% | 4.74% |
| model:opf-ru | eligible | Network identifiers | 58/762 | 7.61% | 45.93% | 2.36% |
| model:opf-ru | eligible | Customer & employee IDs | 299/409 | 73.11% | 79.71% | 46.70% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 259/375 | 69.07% | 86.40% | 61.60% |
| model:opf-ru-v2 | eligible | Logins & usernames | 171/229 | 74.67% | 76.42% | 66.38% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 579/698 | 82.95% | 86.96% | 69.63% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 587/886 | 66.25% | 87.70% | 47.18% |
| model:opf-ru-v2 | eligible | People's names | 1723/2245 | 76.75% | 76.75% | 75.59% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 1096/1199 | 91.41% | 94.83% | 90.41% |
| model:opf-ru-v2 | eligible | Addresses & locations | 397/1468 | 27.04% | 33.11% | 25.07% |
| model:opf-ru-v2 | eligible | Dates & times | 0/277 | 0.00% | 0.36% | 0.00% |
| model:opf-ru-v2 | eligible | Organizations | 28/843 | 3.32% | 4.15% | 2.97% |
| model:opf-ru-v2 | eligible | Network identifiers | 137/762 | 17.98% | 31.36% | 15.62% |
| model:opf-ru-v2 | eligible | Customer & employee IDs | 288/409 | 70.42% | 75.55% | 49.14% |
| model:opf-ru-v2+ov100 | eligible | Passwords, keys & tokens | 267/375 | 71.20% | 86.67% | 64.27% |
| model:opf-ru-v2+ov100 | eligible | Logins & usernames | 170/229 | 74.24% | 75.98% | 66.81% |
| model:opf-ru-v2+ov100 | eligible | Bank accounts & cards | 578/698 | 82.81% | 87.11% | 71.20% |
| model:opf-ru-v2+ov100 | eligible | Documents & identifiers | 579/886 | 65.35% | 87.13% | 47.52% |
| model:opf-ru-v2+ov100 | eligible | People's names | 1722/2245 | 76.70% | 76.75% | 75.46% |
| model:opf-ru-v2+ov100 | eligible | Phone numbers & email | 1088/1199 | 90.74% | 94.66% | 89.91% |
| model:opf-ru-v2+ov100 | eligible | Addresses & locations | 387/1468 | 26.36% | 31.88% | 23.91% |
| model:opf-ru-v2+ov100 | eligible | Dates & times | 0/277 | 0.00% | 0.36% | 0.00% |
| model:opf-ru-v2+ov100 | eligible | Organizations | 24/843 | 2.85% | 3.80% | 2.61% |
| model:opf-ru-v2+ov100 | eligible | Network identifiers | 130/762 | 17.06% | 31.36% | 15.22% |
| model:opf-ru-v2+ov100 | eligible | Customer & employee IDs | 288/409 | 70.42% | 74.57% | 45.23% |
| model:opf-ru-v2+sent300 | eligible | Passwords, keys & tokens | 258/375 | 68.80% | 86.40% | 62.93% |
| model:opf-ru-v2+sent300 | eligible | Logins & usernames | 183/229 | 79.91% | 81.66% | 73.80% |
| model:opf-ru-v2+sent300 | eligible | Bank accounts & cards | 570/698 | 81.66% | 86.39% | 72.64% |
| model:opf-ru-v2+sent300 | eligible | Documents & identifiers | 591/886 | 66.70% | 90.52% | 49.77% |
| model:opf-ru-v2+sent300 | eligible | People's names | 1774/2245 | 79.02% | 79.02% | 78.13% |
| model:opf-ru-v2+sent300 | eligible | Phone numbers & email | 1107/1199 | 92.33% | 94.75% | 91.16% |
| model:opf-ru-v2+sent300 | eligible | Addresses & locations | 387/1468 | 26.36% | 32.56% | 24.59% |
| model:opf-ru-v2+sent300 | eligible | Dates & times | 0/277 | 0.00% | 0.36% | 0.00% |
| model:opf-ru-v2+sent300 | eligible | Organizations | 29/843 | 3.44% | 4.74% | 3.08% |
| model:opf-ru-v2+sent300 | eligible | Network identifiers | 141/762 | 18.50% | 30.58% | 14.96% |
| model:opf-ru-v2+sent300 | eligible | Customer & employee IDs | 314/409 | 76.77% | 81.17% | 55.75% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 158/375 | 42.13% | 61.33% | 37.60% |
| model:pii-shield-onnx | eligible | Logins & usernames | 102/229 | 44.54% | 49.34% | 22.27% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 275/698 | 39.40% | 49.43% | 24.50% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 402/886 | 45.37% | 62.19% | 29.23% |
| model:pii-shield-onnx | eligible | People's names | 467/2245 | 20.80% | 21.07% | 12.92% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 1044/1199 | 87.07% | 96.91% | 78.57% |
| model:pii-shield-onnx | eligible | Addresses & locations | 545/1468 | 37.13% | 48.09% | 32.63% |
| model:pii-shield-onnx | eligible | Dates & times | 249/277 | 89.89% | 98.56% | 89.89% |
| model:pii-shield-onnx | eligible | Organizations | 42/843 | 4.98% | 8.78% | 2.73% |
| model:pii-shield-onnx | eligible | Network identifiers | 384/762 | 50.39% | 97.90% | 43.96% |
| model:pii-shield-onnx | eligible | Customer & employee IDs | 82/409 | 20.05% | 23.47% | 9.05% |
| model:pplx | eligible | Passwords, keys & tokens | 324/375 | 86.40% | 97.07% | 85.87% |
| model:pplx | eligible | Logins & usernames | 229/229 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Bank accounts & cards | 679/698 | 97.28% | 97.28% | 97.28% |
| model:pplx | eligible | Documents & identifiers | 884/886 | 99.77% | 100.00% | 99.77% |
| model:pplx | eligible | People's names | 2234/2245 | 99.51% | 99.51% | 99.47% |
| model:pplx | eligible | Phone numbers & email | 1191/1199 | 99.33% | 99.33% | 99.33% |
| model:pplx | eligible | Addresses & locations | 1160/1468 | 79.02% | 79.97% | 78.88% |
| model:pplx | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 99.28% |
| model:pplx | eligible | Organizations | 57/843 | 6.76% | 12.57% | 6.76% |
| model:pplx | eligible | Network identifiers | 650/762 | 85.30% | 90.94% | 85.17% |
| model:pplx | eligible | Customer & employee IDs | 409/409 | 100.00% | 100.00% | 100.00% |
| model:pplx+cpu-int8 | eligible | Passwords, keys & tokens | 335/375 | 89.33% | 100.00% | 88.53% |
| model:pplx+cpu-int8 | eligible | Logins & usernames | 229/229 | 100.00% | 100.00% | 99.56% |
| model:pplx+cpu-int8 | eligible | Bank accounts & cards | 696/698 | 99.71% | 99.71% | 99.57% |
| model:pplx+cpu-int8 | eligible | Documents & identifiers | 884/886 | 99.77% | 100.00% | 99.66% |
| model:pplx+cpu-int8 | eligible | People's names | 2242/2245 | 99.87% | 99.87% | 99.82% |
| model:pplx+cpu-int8 | eligible | Phone numbers & email | 1189/1199 | 99.17% | 99.42% | 99.17% |
| model:pplx+cpu-int8 | eligible | Addresses & locations | 1380/1468 | 94.01% | 94.75% | 93.60% |
| model:pplx+cpu-int8 | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 99.64% |
| model:pplx+cpu-int8 | eligible | Organizations | 413/843 | 48.99% | 61.92% | 48.99% |
| model:pplx+cpu-int8 | eligible | Network identifiers | 671/762 | 88.06% | 98.95% | 87.80% |
| model:pplx+cpu-int8 | eligible | Customer & employee IDs | 409/409 | 100.00% | 100.00% | 100.00% |
| model:pplx+ov100 | eligible | Passwords, keys & tokens | 329/375 | 87.73% | 98.40% | 87.20% |
| model:pplx+ov100 | eligible | Logins & usernames | 229/229 | 100.00% | 100.00% | 100.00% |
| model:pplx+ov100 | eligible | Bank accounts & cards | 681/698 | 97.56% | 97.56% | 97.56% |
| model:pplx+ov100 | eligible | Documents & identifiers | 884/886 | 99.77% | 100.00% | 99.77% |
| model:pplx+ov100 | eligible | People's names | 2236/2245 | 99.60% | 99.60% | 99.55% |
| model:pplx+ov100 | eligible | Phone numbers & email | 1192/1199 | 99.42% | 99.42% | 99.42% |
| model:pplx+ov100 | eligible | Addresses & locations | 1186/1468 | 80.79% | 81.88% | 80.72% |
| model:pplx+ov100 | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 99.28% |
| model:pplx+ov100 | eligible | Organizations | 60/843 | 7.12% | 13.40% | 7.12% |
| model:pplx+ov100 | eligible | Network identifiers | 640/762 | 83.99% | 91.08% | 83.86% |
| model:pplx+ov100 | eligible | Customer & employee IDs | 409/409 | 100.00% | 100.00% | 100.00% |
| model:pplx+sent300 | eligible | Passwords, keys & tokens | 310/375 | 82.67% | 96.80% | 81.33% |
| model:pplx+sent300 | eligible | Logins & usernames | 229/229 | 100.00% | 100.00% | 99.56% |
| model:pplx+sent300 | eligible | Bank accounts & cards | 680/698 | 97.42% | 97.56% | 97.42% |
| model:pplx+sent300 | eligible | Documents & identifiers | 868/886 | 97.97% | 98.65% | 97.74% |
| model:pplx+sent300 | eligible | People's names | 2218/2245 | 98.80% | 98.80% | 98.66% |
| model:pplx+sent300 | eligible | Phone numbers & email | 1178/1199 | 98.25% | 99.00% | 97.91% |
| model:pplx+sent300 | eligible | Addresses & locations | 1227/1468 | 83.58% | 85.29% | 83.45% |
| model:pplx+sent300 | eligible | Dates & times | 277/277 | 100.00% | 100.00% | 99.28% |
| model:pplx+sent300 | eligible | Organizations | 103/843 | 12.22% | 21.47% | 12.22% |
| model:pplx+sent300 | eligible | Network identifiers | 548/762 | 71.92% | 85.96% | 71.92% |
| model:pplx+sent300 | eligible | Customer & employee IDs | 405/409 | 99.02% | 99.02% | 99.02% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 127/375 | 33.87% | 59.20% | 12.27% |
| model:ru-legal-ner | eligible | Logins & usernames | 89/229 | 38.86% | 45.41% | 11.79% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 273/698 | 39.11% | 54.30% | 13.47% |
| model:ru-legal-ner | eligible | Documents & identifiers | 375/886 | 42.33% | 72.46% | 16.37% |
| model:ru-legal-ner | eligible | People's names | 652/2245 | 29.04% | 29.22% | 18.84% |
| model:ru-legal-ner | eligible | Phone numbers & email | 540/1199 | 45.04% | 94.83% | 37.28% |
| model:ru-legal-ner | eligible | Addresses & locations | 203/1468 | 13.83% | 27.86% | 10.49% |
| model:ru-legal-ner | eligible | Dates & times | 67/277 | 24.19% | 80.14% | 24.19% |
| model:ru-legal-ner | eligible | Organizations | 19/843 | 2.25% | 8.19% | 0.71% |
| model:ru-legal-ner | eligible | Network identifiers | 10/762 | 1.31% | 54.20% | 1.05% |
| model:ru-legal-ner | eligible | Customer & employee IDs | 134/409 | 32.76% | 42.05% | 10.02% |
| model:ru-legal-ner+cpu-int8 | eligible | Passwords, keys & tokens | 122/375 | 32.53% | 57.87% | 12.00% |
| model:ru-legal-ner+cpu-int8 | eligible | Logins & usernames | 96/229 | 41.92% | 50.22% | 14.85% |
| model:ru-legal-ner+cpu-int8 | eligible | Bank accounts & cards | 267/698 | 38.25% | 52.58% | 13.32% |
| model:ru-legal-ner+cpu-int8 | eligible | Documents & identifiers | 373/886 | 42.10% | 71.44% | 16.82% |
| model:ru-legal-ner+cpu-int8 | eligible | People's names | 681/2245 | 30.33% | 30.60% | 20.00% |
| model:ru-legal-ner+cpu-int8 | eligible | Phone numbers & email | 529/1199 | 44.12% | 95.08% | 36.20% |
| model:ru-legal-ner+cpu-int8 | eligible | Addresses & locations | 200/1468 | 13.62% | 27.93% | 10.01% |
| model:ru-legal-ner+cpu-int8 | eligible | Dates & times | 73/277 | 26.35% | 79.42% | 26.35% |
| model:ru-legal-ner+cpu-int8 | eligible | Organizations | 19/843 | 2.25% | 8.54% | 0.83% |
| model:ru-legal-ner+cpu-int8 | eligible | Network identifiers | 10/762 | 1.31% | 55.38% | 1.18% |
| model:ru-legal-ner+cpu-int8 | eligible | Customer & employee IDs | 132/409 | 32.27% | 42.05% | 9.54% |
| model:ru-legal-ner+ov100 | eligible | Passwords, keys & tokens | 136/375 | 36.27% | 62.67% | 12.53% |
| model:ru-legal-ner+ov100 | eligible | Logins & usernames | 83/229 | 36.24% | 46.29% | 13.10% |
| model:ru-legal-ner+ov100 | eligible | Bank accounts & cards | 280/698 | 40.11% | 54.44% | 14.90% |
| model:ru-legal-ner+ov100 | eligible | Documents & identifiers | 376/886 | 42.44% | 72.91% | 16.14% |
| model:ru-legal-ner+ov100 | eligible | People's names | 643/2245 | 28.64% | 28.91% | 18.71% |
| model:ru-legal-ner+ov100 | eligible | Phone numbers & email | 529/1199 | 44.12% | 95.00% | 36.45% |
| model:ru-legal-ner+ov100 | eligible | Addresses & locations | 197/1468 | 13.42% | 26.50% | 10.01% |
| model:ru-legal-ner+ov100 | eligible | Dates & times | 71/277 | 25.63% | 79.06% | 25.63% |
| model:ru-legal-ner+ov100 | eligible | Organizations | 19/843 | 2.25% | 6.41% | 0.83% |
| model:ru-legal-ner+ov100 | eligible | Network identifiers | 9/762 | 1.18% | 54.07% | 0.92% |
| model:ru-legal-ner+ov100 | eligible | Customer & employee IDs | 135/409 | 33.01% | 42.30% | 10.76% |
| model:ru-legal-ner+sent300 | eligible | Passwords, keys & tokens | 154/375 | 41.07% | 67.47% | 15.47% |
| model:ru-legal-ner+sent300 | eligible | Logins & usernames | 127/229 | 55.46% | 61.57% | 24.02% |
| model:ru-legal-ner+sent300 | eligible | Bank accounts & cards | 326/698 | 46.70% | 60.74% | 17.77% |
| model:ru-legal-ner+sent300 | eligible | Documents & identifiers | 432/886 | 48.76% | 77.77% | 21.11% |
| model:ru-legal-ner+sent300 | eligible | People's names | 930/2245 | 41.43% | 41.60% | 28.33% |
| model:ru-legal-ner+sent300 | eligible | Phone numbers & email | 750/1199 | 62.55% | 98.83% | 54.55% |
| model:ru-legal-ner+sent300 | eligible | Addresses & locations | 295/1468 | 20.10% | 37.33% | 16.55% |
| model:ru-legal-ner+sent300 | eligible | Dates & times | 72/277 | 25.99% | 96.39% | 25.99% |
| model:ru-legal-ner+sent300 | eligible | Organizations | 45/843 | 5.34% | 14.71% | 1.66% |
| model:ru-legal-ner+sent300 | eligible | Network identifiers | 11/762 | 1.44% | 78.61% | 1.44% |
| model:ru-legal-ner+sent300 | eligible | Customer & employee IDs | 158/409 | 38.63% | 50.37% | 12.47% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 164/375 | 43.73% | 49.07% | 42.40% |
| model:ru-pii-ner | eligible | Logins & usernames | 206/229 | 89.96% | 90.39% | 89.96% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 563/698 | 80.66% | 80.95% | 80.52% |
| model:ru-pii-ner | eligible | Documents & identifiers | 809/886 | 91.31% | 91.87% | 91.20% |
| model:ru-pii-ner | eligible | People's names | 2090/2245 | 93.10% | 93.10% | 93.05% |
| model:ru-pii-ner | eligible | Phone numbers & email | 1076/1199 | 89.74% | 90.41% | 89.41% |
| model:ru-pii-ner | eligible | Addresses & locations | 447/1468 | 30.45% | 31.20% | 30.45% |
| model:ru-pii-ner | eligible | Dates & times | 269/277 | 97.11% | 99.64% | 97.11% |
| model:ru-pii-ner | eligible | Organizations | 41/843 | 4.86% | 5.58% | 4.86% |
| model:ru-pii-ner | eligible | Network identifiers | 90/762 | 11.81% | 13.65% | 11.68% |
| model:ru-pii-ner | eligible | Customer & employee IDs | 368/409 | 89.98% | 89.98% | 89.73% |
| model:rules-ru | eligible | Passwords, keys & tokens | 28/375 | 7.47% | 20.80% | 7.47% |
| model:rules-ru | eligible | Logins & usernames | 19/229 | 8.30% | 8.30% | 8.30% |
| model:rules-ru | eligible | Bank accounts & cards | 31/698 | 4.44% | 5.01% | 4.44% |
| model:rules-ru | eligible | Documents & identifiers | 9/886 | 1.02% | 2.14% | 0.90% |
| model:rules-ru | eligible | People's names | 0/2245 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 884/1199 | 73.73% | 73.81% | 73.73% |
| model:rules-ru | eligible | Addresses & locations | 2/1468 | 0.14% | 0.14% | 0.07% |
| model:rules-ru | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Organizations | 15/843 | 1.78% | 1.78% | 1.78% |
| model:rules-ru | eligible | Network identifiers | 700/762 | 91.86% | 91.86% | 91.86% |
| model:rules-ru | eligible | Customer & employee IDs | 8/409 | 1.96% | 1.96% | 1.96% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/375 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Logins & usernames | 0/229 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 0/698 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/886 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 0/2245 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/1199 | 0.00% | 0.08% | 0.00% |
| model:spacy-alrosait | eligible | Addresses & locations | 0/1468 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Organizations | 0/843 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Network identifiers | 0/762 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Customer & employee IDs | 0/409 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 2/375 | 0.53% | 0.80% | 0.53% |
| model:spacy-ru-lg | eligible | Logins & usernames | 4/229 | 1.75% | 1.75% | 1.75% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 28/698 | 4.01% | 4.01% | 4.01% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 17/886 | 1.92% | 2.03% | 1.92% |
| model:spacy-ru-lg | eligible | People's names | 462/2245 | 20.58% | 20.58% | 20.58% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 14/1199 | 1.17% | 1.17% | 1.17% |
| model:spacy-ru-lg | eligible | Addresses & locations | 302/1468 | 20.57% | 22.00% | 20.57% |
| model:spacy-ru-lg | eligible | Dates & times | 0/277 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Organizations | 174/843 | 20.64% | 21.00% | 20.64% |
| model:spacy-ru-lg | eligible | Network identifiers | 18/762 | 2.36% | 2.49% | 2.36% |
| model:spacy-ru-lg | eligible | Customer & employee IDs | 2/409 | 0.49% | 0.49% | 0.49% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 48/375 | 12.80% | 38.93% | 12.27% |
| model:stanza-ru | eligible | Logins & usernames | 59/229 | 25.76% | 27.51% | 24.45% |
| model:stanza-ru | eligible | Bank accounts & cards | 61/698 | 8.74% | 9.89% | 8.74% |
| model:stanza-ru | eligible | Documents & identifiers | 123/886 | 13.88% | 29.80% | 11.51% |
| model:stanza-ru | eligible | People's names | 2117/2245 | 94.30% | 94.30% | 94.30% |
| model:stanza-ru | eligible | Phone numbers & email | 54/1199 | 4.50% | 5.50% | 4.50% |
| model:stanza-ru | eligible | Addresses & locations | 1045/1468 | 71.19% | 80.59% | 71.05% |
| model:stanza-ru | eligible | Dates & times | 0/277 | 0.00% | 3.61% | 0.00% |
| model:stanza-ru | eligible | Organizations | 809/843 | 95.97% | 97.15% | 95.73% |
| model:stanza-ru | eligible | Network identifiers | 32/762 | 4.20% | 7.61% | 4.20% |
| model:stanza-ru | eligible | Customer & employee IDs | 72/409 | 17.60% | 24.94% | 17.60% |
| model:traciora | eligible | Passwords, keys & tokens | 222/375 | 59.20% | 72.80% | 50.13% |
| model:traciora | eligible | Logins & usernames | 171/229 | 74.67% | 76.86% | 59.39% |
| model:traciora | eligible | Bank accounts & cards | 473/698 | 67.77% | 72.49% | 48.14% |
| model:traciora | eligible | Documents & identifiers | 540/886 | 60.95% | 75.28% | 41.99% |
| model:traciora | eligible | People's names | 1710/2245 | 76.17% | 76.26% | 74.48% |
| model:traciora | eligible | Phone numbers & email | 1023/1199 | 85.32% | 91.33% | 83.24% |
| model:traciora | eligible | Addresses & locations | 447/1468 | 30.45% | 34.88% | 29.09% |
| model:traciora | eligible | Dates & times | 2/277 | 0.72% | 45.13% | 0.36% |
| model:traciora | eligible | Organizations | 24/843 | 2.85% | 5.22% | 2.25% |
| model:traciora | eligible | Network identifiers | 106/762 | 13.91% | 31.76% | 12.07% |
| model:traciora | eligible | Customer & employee IDs | 211/409 | 51.59% | 54.28% | 32.03% |
