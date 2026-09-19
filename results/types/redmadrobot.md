# redmadrobot: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/redmadrobot.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Bank accounts & cards | 199/202 | 98.51% | 98.51% | 98.02% |
| composition:fastino | eligible | Documents & identifiers | 1258/2055 | 61.22% | 63.55% | 61.02% |
| composition:fastino | eligible | People's names | 1057/1260 | 83.89% | 85.40% | 83.89% |
| composition:fastino | eligible | Phone numbers & email | 352/389 | 90.49% | 96.40% | 90.49% |
| composition:fastino | eligible | Addresses & locations | 1061/1249 | 84.95% | 90.79% | 84.95% |
| composition:fastino | eligible | Network identifiers | 152/361 | 42.11% | 54.29% | 42.11% |
| composition:pplx | eligible | Bank accounts & cards | 173/202 | 85.64% | 99.50% | 84.16% |
| composition:pplx | eligible | Documents & identifiers | 1793/2055 | 87.25% | 97.32% | 85.60% |
| composition:pplx | eligible | People's names | 1124/1260 | 89.21% | 90.56% | 86.59% |
| composition:pplx | eligible | Phone numbers & email | 312/389 | 80.21% | 98.46% | 79.69% |
| composition:pplx | eligible | Addresses & locations | 733/1249 | 58.69% | 61.73% | 55.64% |
| composition:pplx | eligible | Network identifiers | 215/361 | 59.56% | 67.87% | 59.28% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 199/202 | 98.51% | 100.00% | 98.51% |
| composition:pplx+fastino | eligible | Documents & identifiers | 1858/2055 | 90.41% | 98.00% | 89.68% |
| composition:pplx+fastino | eligible | People's names | 1215/1260 | 96.43% | 97.78% | 96.11% |
| composition:pplx+fastino | eligible | Phone numbers & email | 368/389 | 94.60% | 100.00% | 94.60% |
| composition:pplx+fastino | eligible | Addresses & locations | 1164/1249 | 93.19% | 97.28% | 93.03% |
| composition:pplx+fastino | eligible | Network identifiers | 258/361 | 71.47% | 86.15% | 71.47% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 200/202 | 99.01% | 100.00% | 99.01% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 1870/2055 | 91.00% | 98.15% | 90.36% |
| composition:pplx+fastino+bardsai | eligible | People's names | 1239/1260 | 98.33% | 99.68% | 98.25% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 368/389 | 94.60% | 100.00% | 94.60% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 1200/1249 | 96.08% | 99.12% | 95.44% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 259/361 | 71.75% | 91.97% | 71.75% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 201/202 | 99.50% | 100.00% | 99.01% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 1881/2055 | 91.53% | 98.54% | 90.85% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 1240/1260 | 98.41% | 99.76% | 98.33% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 369/389 | 94.86% | 100.00% | 94.86% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 1206/1249 | 96.56% | 99.52% | 95.76% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 283/361 | 78.39% | 98.61% | 77.84% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 200/202 | 99.01% | 100.00% | 98.51% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 1873/2055 | 91.14% | 98.49% | 90.36% |
| composition:pplx+fastino+mmbert | eligible | People's names | 1236/1260 | 98.10% | 99.52% | 97.62% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 369/389 | 94.86% | 100.00% | 94.86% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 1181/1249 | 94.56% | 98.48% | 93.67% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 280/361 | 77.56% | 98.61% | 77.01% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Bank accounts & cards | 166/202 | 82.18% | 94.06% | 79.70% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 1527/2055 | 74.31% | 83.70% | 70.61% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 1144/1260 | 90.79% | 92.14% | 89.13% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 321/389 | 82.52% | 97.69% | 82.78% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 705/1249 | 56.45% | 62.93% | 53.16% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 172/361 | 47.65% | 63.43% | 42.94% |
| model:apararti | eligible | Bank accounts & cards | 183/202 | 90.59% | 99.01% | 87.62% |
| model:apararti | eligible | Documents & identifiers | 1632/2055 | 79.42% | 88.61% | 74.21% |
| model:apararti | eligible | People's names | 993/1260 | 78.81% | 80.00% | 73.10% |
| model:apararti | eligible | Phone numbers & email | 283/389 | 72.75% | 90.23% | 73.26% |
| model:apararti | eligible | Addresses & locations | 626/1249 | 50.12% | 55.64% | 44.28% |
| model:apararti | eligible | Network identifiers | 212/361 | 58.73% | 66.20% | 57.62% |
| model:bardsai-eu | eligible | Bank accounts & cards | 102/202 | 50.50% | 75.25% | 36.63% |
| model:bardsai-eu | eligible | Documents & identifiers | 1009/2055 | 49.10% | 54.99% | 41.31% |
| model:bardsai-eu | eligible | People's names | 1158/1260 | 91.90% | 93.33% | 88.89% |
| model:bardsai-eu | eligible | Phone numbers & email | 139/389 | 35.73% | 91.00% | 30.08% |
| model:bardsai-eu | eligible | Addresses & locations | 948/1249 | 75.90% | 83.75% | 71.34% |
| model:bardsai-eu | eligible | Network identifiers | 113/361 | 31.30% | 61.50% | 29.09% |
| model:betterleaks | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | People's names | 0/1260 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Phone numbers & email | 0/389 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Addresses & locations | 0/1249 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Network identifiers | 0/361 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.05% | 0.00% |
| model:davlan-mbert | eligible | People's names | 1177/1260 | 93.41% | 94.92% | 90.16% |
| model:davlan-mbert | eligible | Phone numbers & email | 1/389 | 0.26% | 3.34% | 0.26% |
| model:davlan-mbert | eligible | Addresses & locations | 929/1249 | 74.38% | 81.02% | 71.18% |
| model:davlan-mbert | eligible | Network identifiers | 2/361 | 0.55% | 13.30% | 0.55% |
| model:davlan-mbert+cpu-int8 | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.15% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | People's names | 1141/1260 | 90.56% | 91.98% | 84.29% |
| model:davlan-mbert+cpu-int8 | eligible | Phone numbers & email | 1/389 | 0.26% | 2.83% | 0.26% |
| model:davlan-mbert+cpu-int8 | eligible | Addresses & locations | 849/1249 | 67.97% | 78.38% | 60.69% |
| model:davlan-mbert+cpu-int8 | eligible | Network identifiers | 1/361 | 0.28% | 2.22% | 0.28% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 1/2055 | 0.05% | 0.29% | 0.05% |
| model:davlan-xlmr | eligible | People's names | 1216/1260 | 96.51% | 97.86% | 95.32% |
| model:davlan-xlmr | eligible | Phone numbers & email | 1/389 | 0.26% | 3.86% | 0.26% |
| model:davlan-xlmr | eligible | Addresses & locations | 967/1249 | 77.42% | 87.11% | 73.98% |
| model:davlan-xlmr | eligible | Network identifiers | 1/361 | 0.28% | 2.22% | 0.28% |
| model:davlan-xlmr+cpu-int8 | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Documents & identifiers | 1/2055 | 0.05% | 0.15% | 0.05% |
| model:davlan-xlmr+cpu-int8 | eligible | People's names | 934/1260 | 74.13% | 75.56% | 56.27% |
| model:davlan-xlmr+cpu-int8 | eligible | Phone numbers & email | 1/389 | 0.26% | 1.29% | 0.26% |
| model:davlan-xlmr+cpu-int8 | eligible | Addresses & locations | 630/1249 | 50.44% | 65.57% | 31.06% |
| model:davlan-xlmr+cpu-int8 | eligible | Network identifiers | 1/361 | 0.28% | 0.83% | 0.28% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 114/202 | 56.44% | 67.82% | 48.51% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 946/2055 | 46.03% | 51.00% | 40.05% |
| model:fef2-secret-ru | eligible | People's names | 1041/1260 | 82.62% | 83.97% | 81.59% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 174/389 | 44.73% | 54.50% | 42.93% |
| model:fef2-secret-ru | eligible | Addresses & locations | 750/1249 | 60.05% | 69.82% | 58.13% |
| model:fef2-secret-ru | eligible | Network identifiers | 9/361 | 2.49% | 6.09% | 2.22% |
| model:fef2-secret-ru+cpu-int8 | eligible | Bank accounts & cards | 50/202 | 24.75% | 42.08% | 20.30% |
| model:fef2-secret-ru+cpu-int8 | eligible | Documents & identifiers | 671/2055 | 32.65% | 39.61% | 25.64% |
| model:fef2-secret-ru+cpu-int8 | eligible | People's names | 1049/1260 | 83.25% | 84.52% | 81.59% |
| model:fef2-secret-ru+cpu-int8 | eligible | Phone numbers & email | 131/389 | 33.68% | 48.59% | 32.65% |
| model:fef2-secret-ru+cpu-int8 | eligible | Addresses & locations | 731/1249 | 58.53% | 67.57% | 55.80% |
| model:fef2-secret-ru+cpu-int8 | eligible | Network identifiers | 5/361 | 1.39% | 3.88% | 1.11% |
| model:gitleaks | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | People's names | 0/1260 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Phone numbers & email | 0/389 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Addresses & locations | 0/1249 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Network identifiers | 0/361 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 8/202 | 3.96% | 5.45% | 3.96% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 61/2055 | 2.97% | 3.21% | 2.97% |
| model:gliner-multi-v21 | eligible | People's names | 925/1260 | 73.41% | 74.68% | 73.41% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 39/389 | 10.03% | 25.71% | 9.25% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 861/1249 | 68.94% | 73.90% | 68.78% |
| model:gliner-multi-v21 | eligible | Network identifiers | 68/361 | 18.84% | 36.29% | 18.56% |
| model:gliner-multi-v21+cpu-int8 | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | People's names | 0/1260 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Phone numbers & email | 0/389 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Addresses & locations | 0/1249 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Network identifiers | 0/361 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21-ru | eligible | Bank accounts & cards | 7/202 | 3.47% | 4.46% | 3.47% |
| model:gliner-multi-v21-ru | eligible | Documents & identifiers | 226/2055 | 11.00% | 11.09% | 11.00% |
| model:gliner-multi-v21-ru | eligible | People's names | 929/1260 | 73.73% | 75.00% | 73.73% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 50/389 | 12.85% | 27.76% | 10.03% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 861/1249 | 68.94% | 73.18% | 68.86% |
| model:gliner-multi-v21-ru | eligible | Network identifiers | 68/361 | 18.84% | 28.53% | 18.28% |
| model:gliner-multi-v21-ru+cpu-int8 | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21-ru+cpu-int8 | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21-ru+cpu-int8 | eligible | People's names | 0/1260 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21-ru+cpu-int8 | eligible | Phone numbers & email | 0/389 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21-ru+cpu-int8 | eligible | Addresses & locations | 0/1249 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21-ru+cpu-int8 | eligible | Network identifiers | 0/361 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia | eligible | Bank accounts & cards | 169/202 | 83.66% | 83.66% | 83.17% |
| model:gliner-nvidia | eligible | Documents & identifiers | 1024/2055 | 49.83% | 50.17% | 49.73% |
| model:gliner-nvidia | eligible | People's names | 1184/1260 | 93.97% | 95.48% | 93.97% |
| model:gliner-nvidia | eligible | Phone numbers & email | 354/389 | 91.00% | 91.77% | 91.00% |
| model:gliner-nvidia | eligible | Addresses & locations | 1001/1249 | 80.14% | 86.63% | 79.74% |
| model:gliner-nvidia | eligible | Network identifiers | 245/361 | 67.87% | 68.42% | 67.87% |
| model:gliner-nvidia+cpu-int8 | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | People's names | 0/1260 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Phone numbers & email | 0/389 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Addresses & locations | 0/1249 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Network identifiers | 0/361 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia-ru | eligible | Bank accounts & cards | 190/202 | 94.06% | 94.55% | 94.06% |
| model:gliner-nvidia-ru | eligible | Documents & identifiers | 1448/2055 | 70.46% | 70.95% | 70.46% |
| model:gliner-nvidia-ru | eligible | People's names | 1127/1260 | 89.44% | 90.95% | 89.44% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 350/389 | 89.97% | 90.75% | 89.97% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 921/1249 | 73.74% | 84.55% | 73.50% |
| model:gliner-nvidia-ru | eligible | Network identifiers | 245/361 | 67.87% | 68.70% | 67.87% |
| model:gliner-nvidia-ru+cpu-int8 | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia-ru+cpu-int8 | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia-ru+cpu-int8 | eligible | People's names | 0/1260 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia-ru+cpu-int8 | eligible | Phone numbers & email | 0/389 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia-ru+cpu-int8 | eligible | Addresses & locations | 0/1249 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia-ru+cpu-int8 | eligible | Network identifiers | 0/361 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 109/202 | 53.96% | 53.96% | 53.96% |
| model:gliner-pii-base | eligible | Documents & identifiers | 573/2055 | 27.88% | 28.03% | 27.88% |
| model:gliner-pii-base | eligible | People's names | 793/1260 | 62.94% | 64.13% | 62.94% |
| model:gliner-pii-base | eligible | Phone numbers & email | 315/389 | 80.98% | 82.52% | 80.98% |
| model:gliner-pii-base | eligible | Addresses & locations | 436/1249 | 34.91% | 45.88% | 34.75% |
| model:gliner-pii-base | eligible | Network identifiers | 209/361 | 57.89% | 68.42% | 57.62% |
| model:gliner-pii-base+cpu-int8 | eligible | Bank accounts & cards | 1/202 | 0.50% | 0.50% | 0.50% |
| model:gliner-pii-base+cpu-int8 | eligible | Documents & identifiers | 8/2055 | 0.39% | 0.44% | 0.39% |
| model:gliner-pii-base+cpu-int8 | eligible | People's names | 1/1260 | 0.08% | 0.08% | 0.08% |
| model:gliner-pii-base+cpu-int8 | eligible | Phone numbers & email | 6/389 | 1.54% | 1.54% | 1.54% |
| model:gliner-pii-base+cpu-int8 | eligible | Addresses & locations | 0/1249 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Network identifiers | 0/361 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 182/202 | 90.10% | 91.09% | 90.10% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 1417/2055 | 68.95% | 69.78% | 68.95% |
| model:gliner-pii-edge | eligible | People's names | 717/1260 | 56.90% | 57.14% | 56.90% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 323/389 | 83.03% | 83.55% | 83.03% |
| model:gliner-pii-edge | eligible | Addresses & locations | 453/1249 | 36.27% | 49.96% | 36.11% |
| model:gliner-pii-edge | eligible | Network identifiers | 186/361 | 51.52% | 75.35% | 51.25% |
| model:gliner-pii-edge+cpu-int8 | eligible | Bank accounts & cards | 40/202 | 19.80% | 31.68% | 19.80% |
| model:gliner-pii-edge+cpu-int8 | eligible | Documents & identifiers | 543/2055 | 26.42% | 30.41% | 26.33% |
| model:gliner-pii-edge+cpu-int8 | eligible | People's names | 184/1260 | 14.60% | 14.60% | 14.60% |
| model:gliner-pii-edge+cpu-int8 | eligible | Phone numbers & email | 75/389 | 19.28% | 31.11% | 19.28% |
| model:gliner-pii-edge+cpu-int8 | eligible | Addresses & locations | 179/1249 | 14.33% | 20.02% | 14.25% |
| model:gliner-pii-edge+cpu-int8 | eligible | Network identifiers | 31/361 | 8.59% | 21.33% | 7.20% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 37/202 | 18.32% | 96.04% | 18.32% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 848/2055 | 41.27% | 64.28% | 40.97% |
| model:gliner-stream-pii | eligible | People's names | 886/1260 | 70.32% | 71.83% | 70.32% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 251/389 | 64.52% | 78.66% | 64.52% |
| model:gliner-stream-pii | eligible | Addresses & locations | 607/1249 | 48.60% | 67.89% | 48.52% |
| model:gliner-stream-pii | eligible | Network identifiers | 173/361 | 47.92% | 69.81% | 47.92% |
| model:gliner-urchade | eligible | Bank accounts & cards | 177/202 | 87.62% | 88.12% | 87.62% |
| model:gliner-urchade | eligible | Documents & identifiers | 1335/2055 | 64.96% | 65.30% | 64.96% |
| model:gliner-urchade | eligible | People's names | 226/1260 | 17.94% | 17.94% | 17.94% |
| model:gliner-urchade | eligible | Phone numbers & email | 356/389 | 91.52% | 92.29% | 91.52% |
| model:gliner-urchade | eligible | Addresses & locations | 996/1249 | 79.74% | 83.35% | 79.74% |
| model:gliner-urchade | eligible | Network identifiers | 225/361 | 62.33% | 68.70% | 62.05% |
| model:gliner-urchade+cpu-int8 | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | People's names | 0/1260 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Phone numbers & email | 0/389 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Addresses & locations | 0/1249 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Network identifiers | 0/361 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade-ru | eligible | Bank accounts & cards | 156/202 | 77.23% | 77.72% | 76.73% |
| model:gliner-urchade-ru | eligible | Documents & identifiers | 1463/2055 | 71.19% | 71.68% | 71.19% |
| model:gliner-urchade-ru | eligible | People's names | 146/1260 | 11.59% | 11.67% | 11.59% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 332/389 | 85.35% | 85.60% | 85.35% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 1014/1249 | 81.18% | 83.75% | 81.18% |
| model:gliner-urchade-ru | eligible | Network identifiers | 197/361 | 54.57% | 58.17% | 54.29% |
| model:gliner-urchade-ru+cpu-int8 | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade-ru+cpu-int8 | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade-ru+cpu-int8 | eligible | People's names | 0/1260 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade-ru+cpu-int8 | eligible | Phone numbers & email | 0/389 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade-ru+cpu-int8 | eligible | Addresses & locations | 0/1249 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade-ru+cpu-int8 | eligible | Network identifiers | 0/361 | 0.00% | 0.00% | 0.00% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 199/202 | 98.51% | 98.51% | 98.02% |
| model:gliner2-fastino | eligible | Documents & identifiers | 1258/2055 | 61.22% | 63.55% | 61.02% |
| model:gliner2-fastino | eligible | People's names | 1057/1260 | 83.89% | 85.40% | 83.89% |
| model:gliner2-fastino | eligible | Phone numbers & email | 352/389 | 90.49% | 96.40% | 90.49% |
| model:gliner2-fastino | eligible | Addresses & locations | 1061/1249 | 84.95% | 90.79% | 84.95% |
| model:gliner2-fastino | eligible | Network identifiers | 152/361 | 42.11% | 54.29% | 42.11% |
| model:gliner2-fastino-ru | eligible | Bank accounts & cards | 196/202 | 97.03% | 97.03% | 96.53% |
| model:gliner2-fastino-ru | eligible | Documents & identifiers | 1503/2055 | 73.14% | 75.28% | 72.65% |
| model:gliner2-fastino-ru | eligible | People's names | 1166/1260 | 92.54% | 93.97% | 92.46% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 361/389 | 92.80% | 95.63% | 92.80% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 1040/1249 | 83.27% | 89.99% | 83.19% |
| model:gliner2-fastino-ru | eligible | Network identifiers | 154/361 | 42.66% | 49.86% | 42.66% |
| model:gliner2-hivetrace-omni | eligible | Bank accounts & cards | 198/202 | 98.02% | 98.02% | 97.52% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 938/2055 | 45.64% | 47.54% | 45.60% |
| model:gliner2-hivetrace-omni | eligible | People's names | 987/1260 | 78.33% | 79.84% | 78.33% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 352/389 | 90.49% | 92.80% | 90.49% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 878/1249 | 70.30% | 85.83% | 70.22% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 150/361 | 41.55% | 44.60% | 41.27% |
| model:gliner2-hivetrace-omni-ru | eligible | Bank accounts & cards | 196/202 | 97.03% | 97.03% | 96.53% |
| model:gliner2-hivetrace-omni-ru | eligible | Documents & identifiers | 1254/2055 | 61.02% | 63.21% | 60.88% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 847/1260 | 67.22% | 68.65% | 67.22% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 361/389 | 92.80% | 93.06% | 92.80% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 840/1249 | 67.25% | 86.63% | 67.25% |
| model:gliner2-hivetrace-omni-ru | eligible | Network identifiers | 159/361 | 44.04% | 46.81% | 43.77% |
| model:gliner2-hivetrace-uni | eligible | Bank accounts & cards | 64/202 | 31.68% | 36.63% | 31.19% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 1296/2055 | 63.07% | 65.74% | 63.02% |
| model:gliner2-hivetrace-uni | eligible | People's names | 550/1260 | 43.65% | 44.44% | 43.65% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 343/389 | 88.17% | 89.97% | 87.92% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 864/1249 | 69.18% | 75.66% | 69.18% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 13/361 | 3.60% | 7.48% | 3.60% |
| model:gliner2-hivetrace-uni-ru | eligible | Bank accounts & cards | 19/202 | 9.41% | 9.90% | 9.41% |
| model:gliner2-hivetrace-uni-ru | eligible | Documents & identifiers | 576/2055 | 28.03% | 28.86% | 28.03% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 604/1260 | 47.94% | 48.81% | 47.94% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 48/389 | 12.34% | 12.60% | 12.34% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 485/1249 | 38.83% | 40.67% | 38.83% |
| model:gliner2-hivetrace-uni-ru | eligible | Network identifiers | 3/361 | 0.83% | 1.66% | 0.83% |
| model:gliner2-large | eligible | Bank accounts & cards | 164/202 | 81.19% | 84.65% | 79.70% |
| model:gliner2-large | eligible | Documents & identifiers | 1103/2055 | 53.67% | 55.62% | 53.14% |
| model:gliner2-large | eligible | People's names | 792/1260 | 62.86% | 64.29% | 62.86% |
| model:gliner2-large | eligible | Phone numbers & email | 362/389 | 93.06% | 93.83% | 92.80% |
| model:gliner2-large | eligible | Addresses & locations | 785/1249 | 62.85% | 70.62% | 62.85% |
| model:gliner2-large | eligible | Network identifiers | 203/361 | 56.23% | 64.82% | 56.23% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 86/202 | 42.57% | 42.57% | 42.57% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 1281/2055 | 62.34% | 62.77% | 62.29% |
| model:gliner2-vladlinv | eligible | People's names | 800/1260 | 63.49% | 64.84% | 63.49% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 282/389 | 72.49% | 73.01% | 72.49% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 230/1249 | 18.41% | 18.73% | 18.41% |
| model:gliner2-vladlinv | eligible | Network identifiers | 41/361 | 11.36% | 11.63% | 11.36% |
| model:gliner2-vladlinv-ru | eligible | Bank accounts & cards | 151/202 | 74.75% | 74.75% | 74.75% |
| model:gliner2-vladlinv-ru | eligible | Documents & identifiers | 1589/2055 | 77.32% | 77.86% | 77.13% |
| model:gliner2-vladlinv-ru | eligible | People's names | 748/1260 | 59.37% | 60.40% | 59.29% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 280/389 | 71.98% | 72.24% | 71.98% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 243/1249 | 19.46% | 19.78% | 19.46% |
| model:gliner2-vladlinv-ru | eligible | Network identifiers | 23/361 | 6.37% | 6.37% | 6.37% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 110/202 | 54.46% | 55.94% | 53.47% |
| model:gliner25-fastino | eligible | Documents & identifiers | 463/2055 | 22.53% | 24.04% | 22.38% |
| model:gliner25-fastino | eligible | People's names | 823/1260 | 65.32% | 66.83% | 65.32% |
| model:gliner25-fastino | eligible | Phone numbers & email | 342/389 | 87.92% | 89.97% | 87.92% |
| model:gliner25-fastino | eligible | Addresses & locations | 487/1249 | 38.99% | 41.23% | 38.99% |
| model:gliner25-fastino | eligible | Network identifiers | 104/361 | 28.81% | 31.58% | 28.81% |
| model:gliner25-fastino-ru | eligible | Bank accounts & cards | 166/202 | 82.18% | 84.16% | 80.69% |
| model:gliner25-fastino-ru | eligible | Documents & identifiers | 1245/2055 | 60.58% | 63.70% | 59.76% |
| model:gliner25-fastino-ru | eligible | People's names | 944/1260 | 74.92% | 76.19% | 74.92% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 335/389 | 86.12% | 87.66% | 86.12% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 412/1249 | 32.99% | 35.79% | 32.99% |
| model:gliner25-fastino-ru | eligible | Network identifiers | 93/361 | 25.76% | 26.87% | 25.76% |
| model:gravitee-small | eligible | Bank accounts & cards | 139/202 | 68.81% | 91.58% | 60.40% |
| model:gravitee-small | eligible | Documents & identifiers | 832/2055 | 40.49% | 45.64% | 36.11% |
| model:gravitee-small | eligible | People's names | 941/1260 | 74.68% | 75.48% | 70.71% |
| model:gravitee-small | eligible | Phone numbers & email | 314/389 | 80.72% | 95.12% | 78.41% |
| model:gravitee-small | eligible | Addresses & locations | 742/1249 | 59.41% | 64.61% | 52.04% |
| model:gravitee-small | eligible | Network identifiers | 277/361 | 76.73% | 94.74% | 72.58% |
| model:gravitee-small+cpu-int8 | eligible | Bank accounts & cards | 145/202 | 71.78% | 93.07% | 62.38% |
| model:gravitee-small+cpu-int8 | eligible | Documents & identifiers | 884/2055 | 43.02% | 49.05% | 38.00% |
| model:gravitee-small+cpu-int8 | eligible | People's names | 962/1260 | 76.35% | 77.14% | 71.67% |
| model:gravitee-small+cpu-int8 | eligible | Phone numbers & email | 304/389 | 78.15% | 94.34% | 74.29% |
| model:gravitee-small+cpu-int8 | eligible | Addresses & locations | 784/1249 | 62.77% | 68.37% | 54.36% |
| model:gravitee-small+cpu-int8 | eligible | Network identifiers | 268/361 | 74.24% | 94.74% | 69.25% |
| model:kalyan-ettin | eligible | Bank accounts & cards | 93/202 | 46.04% | 67.33% | 32.18% |
| model:kalyan-ettin | eligible | Documents & identifiers | 705/2055 | 34.31% | 42.04% | 16.93% |
| model:kalyan-ettin | eligible | People's names | 899/1260 | 71.35% | 72.62% | 44.52% |
| model:kalyan-ettin | eligible | Phone numbers & email | 182/389 | 46.79% | 69.92% | 39.85% |
| model:kalyan-ettin | eligible | Addresses & locations | 397/1249 | 31.79% | 51.00% | 14.65% |
| model:kalyan-ettin | eligible | Network identifiers | 161/361 | 44.60% | 84.76% | 43.77% |
| model:kalyan-ettin+cpu-int8 | eligible | Bank accounts & cards | 11/202 | 5.45% | 31.68% | 0.50% |
| model:kalyan-ettin+cpu-int8 | eligible | Documents & identifiers | 200/2055 | 9.73% | 15.33% | 1.61% |
| model:kalyan-ettin+cpu-int8 | eligible | People's names | 579/1260 | 45.95% | 46.67% | 16.27% |
| model:kalyan-ettin+cpu-int8 | eligible | Phone numbers & email | 74/389 | 19.02% | 48.07% | 7.20% |
| model:kalyan-ettin+cpu-int8 | eligible | Addresses & locations | 91/1249 | 7.29% | 12.17% | 1.92% |
| model:kalyan-ettin+cpu-int8 | eligible | Network identifiers | 8/361 | 2.22% | 55.40% | 1.39% |
| model:mmbert32k | eligible | Bank accounts & cards | 80/202 | 39.60% | 96.53% | 37.13% |
| model:mmbert32k | eligible | Documents & identifiers | 1245/2055 | 60.58% | 77.18% | 22.48% |
| model:mmbert32k | eligible | People's names | 1058/1260 | 83.97% | 85.00% | 64.05% |
| model:mmbert32k | eligible | Phone numbers & email | 163/389 | 41.90% | 91.26% | 33.42% |
| model:mmbert32k | eligible | Addresses & locations | 596/1249 | 47.72% | 75.74% | 30.18% |
| model:mmbert32k | eligible | Network identifiers | 129/361 | 35.73% | 90.86% | 25.76% |
| model:mmbert32k+cpu-int8 | eligible | Bank accounts & cards | 47/202 | 23.27% | 95.05% | 0.50% |
| model:mmbert32k+cpu-int8 | eligible | Documents & identifiers | 1025/2055 | 49.88% | 74.70% | 1.12% |
| model:mmbert32k+cpu-int8 | eligible | People's names | 517/1260 | 41.03% | 41.51% | 11.90% |
| model:mmbert32k+cpu-int8 | eligible | Phone numbers & email | 45/389 | 11.57% | 74.55% | 1.80% |
| model:mmbert32k+cpu-int8 | eligible | Addresses & locations | 251/1249 | 20.10% | 41.07% | 2.88% |
| model:mmbert32k+cpu-int8 | eligible | Network identifiers | 15/361 | 4.16% | 84.49% | 1.39% |
| model:natasha | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 49/2055 | 2.38% | 5.79% | 2.24% |
| model:natasha | eligible | People's names | 897/1260 | 71.19% | 72.62% | 71.19% |
| model:natasha | eligible | Phone numbers & email | 4/389 | 1.03% | 2.31% | 1.03% |
| model:natasha | eligible | Addresses & locations | 727/1249 | 58.21% | 65.25% | 58.13% |
| model:natasha | eligible | Network identifiers | 1/361 | 0.28% | 0.55% | 0.28% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.19% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 1170/1260 | 92.86% | 94.44% | 89.60% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/389 | 0.00% | 25.45% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 759/1249 | 60.77% | 91.83% | 43.15% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/361 | 0.00% | 0.83% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.10% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | People's names | 1158/1260 | 91.90% | 93.41% | 83.41% |
| model:ner-ru-gherman+cpu-int8 | eligible | Phone numbers & email | 0/389 | 0.00% | 23.14% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Addresses & locations | 679/1249 | 54.36% | 87.27% | 40.11% |
| model:ner-ru-gherman+cpu-int8 | eligible | Network identifiers | 0/361 | 0.00% | 1.11% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Documents & identifiers | 0/2055 | 0.00% | 0.19% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | People's names | 1169/1260 | 92.78% | 94.29% | 89.29% |
| model:ner-ru-gherman-onnx | eligible | Phone numbers & email | 0/389 | 0.00% | 25.19% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Addresses & locations | 754/1249 | 60.37% | 92.07% | 43.31% |
| model:ner-ru-gherman-onnx | eligible | Network identifiers | 0/361 | 0.00% | 0.83% | 0.00% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 37/202 | 18.32% | 41.58% | 4.46% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 222/2055 | 10.80% | 19.61% | 8.22% |
| model:ner-ru-yqelz | eligible | People's names | 1115/1260 | 88.49% | 89.92% | 86.51% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 14/389 | 3.60% | 24.68% | 2.31% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 891/1249 | 71.34% | 78.14% | 68.78% |
| model:ner-ru-yqelz | eligible | Network identifiers | 12/361 | 3.32% | 26.32% | 1.66% |
| model:nuner-zero | eligible | Bank accounts & cards | 168/202 | 83.17% | 87.62% | 18.32% |
| model:nuner-zero | eligible | Documents & identifiers | 1026/2055 | 49.93% | 51.53% | 34.36% |
| model:nuner-zero | eligible | People's names | 664/1260 | 52.70% | 53.97% | 52.62% |
| model:nuner-zero | eligible | Phone numbers & email | 379/389 | 97.43% | 97.94% | 40.36% |
| model:nuner-zero | eligible | Addresses & locations | 840/1249 | 67.25% | 74.54% | 36.03% |
| model:nuner-zero | eligible | Network identifiers | 354/361 | 98.06% | 99.72% | 84.49% |
| model:nym-base | eligible | Bank accounts & cards | 177/202 | 87.62% | 99.50% | 81.19% |
| model:nym-base | eligible | Documents & identifiers | 1549/2055 | 75.38% | 82.87% | 68.32% |
| model:nym-base | eligible | People's names | 1200/1260 | 95.24% | 96.75% | 93.89% |
| model:nym-base | eligible | Phone numbers & email | 283/389 | 72.75% | 94.60% | 72.24% |
| model:nym-base | eligible | Addresses & locations | 940/1249 | 75.26% | 87.11% | 73.74% |
| model:nym-base | eligible | Network identifiers | 293/361 | 81.16% | 93.35% | 75.07% |
| model:nym-base+cpu-int8 | eligible | Bank accounts & cards | 171/202 | 84.65% | 99.50% | 76.24% |
| model:nym-base+cpu-int8 | eligible | Documents & identifiers | 1467/2055 | 71.39% | 79.17% | 62.43% |
| model:nym-base+cpu-int8 | eligible | People's names | 1158/1260 | 91.90% | 93.41% | 89.37% |
| model:nym-base+cpu-int8 | eligible | Phone numbers & email | 283/389 | 72.75% | 91.52% | 70.95% |
| model:nym-base+cpu-int8 | eligible | Addresses & locations | 836/1249 | 66.93% | 78.94% | 64.21% |
| model:nym-base+cpu-int8 | eligible | Network identifiers | 299/361 | 82.83% | 95.57% | 76.45% |
| model:nym-small | eligible | Bank accounts & cards | 157/202 | 77.72% | 96.53% | 76.24% |
| model:nym-small | eligible | Documents & identifiers | 1434/2055 | 69.78% | 77.71% | 62.43% |
| model:nym-small | eligible | People's names | 1162/1260 | 92.22% | 93.73% | 90.56% |
| model:nym-small | eligible | Phone numbers & email | 282/389 | 72.49% | 89.20% | 73.52% |
| model:nym-small | eligible | Addresses & locations | 875/1249 | 70.06% | 84.15% | 67.73% |
| model:nym-small | eligible | Network identifiers | 254/361 | 70.36% | 87.26% | 66.48% |
| model:openai-base | eligible | Bank accounts & cards | 165/202 | 81.68% | 90.59% | 81.19% |
| model:openai-base | eligible | Documents & identifiers | 1537/2055 | 74.79% | 81.61% | 72.94% |
| model:openai-base | eligible | People's names | 909/1260 | 72.14% | 73.17% | 70.00% |
| model:openai-base | eligible | Phone numbers & email | 288/389 | 74.04% | 88.43% | 72.75% |
| model:openai-base | eligible | Addresses & locations | 534/1249 | 42.75% | 46.92% | 40.51% |
| model:openai-base | eligible | Network identifiers | 162/361 | 44.88% | 50.14% | 44.04% |
| model:openai-base-onnx | eligible | Bank accounts & cards | 166/202 | 82.18% | 90.10% | 81.19% |
| model:openai-base-onnx | eligible | Documents & identifiers | 1536/2055 | 74.74% | 81.36% | 72.80% |
| model:openai-base-onnx | eligible | People's names | 911/1260 | 72.30% | 73.33% | 70.48% |
| model:openai-base-onnx | eligible | Phone numbers & email | 284/389 | 73.01% | 88.17% | 72.49% |
| model:openai-base-onnx | eligible | Addresses & locations | 536/1249 | 42.91% | 46.76% | 41.07% |
| model:openai-base-onnx | eligible | Network identifiers | 163/361 | 45.15% | 49.86% | 44.04% |
| model:openmed-multilingual | eligible | Bank accounts & cards | 151/202 | 74.75% | 95.05% | 71.78% |
| model:openmed-multilingual | eligible | Documents & identifiers | 913/2055 | 44.43% | 60.10% | 35.33% |
| model:openmed-multilingual | eligible | People's names | 739/1260 | 58.65% | 60.00% | 41.27% |
| model:openmed-multilingual | eligible | Phone numbers & email | 217/389 | 55.78% | 77.89% | 54.76% |
| model:openmed-multilingual | eligible | Addresses & locations | 343/1249 | 27.46% | 48.36% | 17.29% |
| model:openmed-multilingual | eligible | Network identifiers | 277/361 | 76.73% | 90.30% | 75.90% |
| model:openmed-nemotron | eligible | Bank accounts & cards | 123/202 | 60.89% | 73.27% | 51.98% |
| model:openmed-nemotron | eligible | Documents & identifiers | 446/2055 | 21.70% | 27.69% | 11.78% |
| model:openmed-nemotron | eligible | People's names | 960/1260 | 76.19% | 77.62% | 52.86% |
| model:openmed-nemotron | eligible | Phone numbers & email | 190/389 | 48.84% | 77.63% | 43.70% |
| model:openmed-nemotron | eligible | Addresses & locations | 516/1249 | 41.31% | 62.13% | 28.26% |
| model:openmed-nemotron | eligible | Network identifiers | 261/361 | 72.30% | 83.10% | 70.64% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 174/202 | 86.14% | 95.05% | 86.14% |
| model:opf-kz-ru | eligible | Documents & identifiers | 1666/2055 | 81.07% | 90.46% | 80.05% |
| model:opf-kz-ru | eligible | People's names | 858/1260 | 68.10% | 69.29% | 60.63% |
| model:opf-kz-ru | eligible | Phone numbers & email | 289/389 | 74.29% | 92.80% | 74.29% |
| model:opf-kz-ru | eligible | Addresses & locations | 354/1249 | 28.34% | 38.19% | 22.26% |
| model:opf-kz-ru | eligible | Network identifiers | 219/361 | 60.66% | 69.81% | 57.89% |
| model:opf-ru | eligible | Bank accounts & cards | 82/202 | 40.59% | 85.64% | 43.07% |
| model:opf-ru | eligible | Documents & identifiers | 1121/2055 | 54.55% | 74.01% | 41.56% |
| model:opf-ru | eligible | People's names | 994/1260 | 78.89% | 80.24% | 70.79% |
| model:opf-ru | eligible | Phone numbers & email | 251/389 | 64.52% | 89.97% | 62.98% |
| model:opf-ru | eligible | Addresses & locations | 439/1249 | 35.15% | 55.08% | 26.58% |
| model:opf-ru | eligible | Network identifiers | 27/361 | 7.48% | 56.79% | 4.43% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 142/202 | 70.30% | 86.63% | 68.81% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 1309/2055 | 63.70% | 78.54% | 58.05% |
| model:opf-ru-v2 | eligible | People's names | 927/1260 | 73.57% | 74.52% | 68.02% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 251/389 | 64.52% | 85.35% | 62.98% |
| model:opf-ru-v2 | eligible | Addresses & locations | 426/1249 | 34.11% | 40.91% | 30.02% |
| model:opf-ru-v2 | eligible | Network identifiers | 113/361 | 31.30% | 45.15% | 25.48% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 145/202 | 71.78% | 87.13% | 67.33% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 1046/2055 | 50.90% | 60.00% | 41.31% |
| model:pii-shield-onnx | eligible | People's names | 869/1260 | 68.97% | 70.08% | 62.06% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 284/389 | 73.01% | 79.69% | 72.49% |
| model:pii-shield-onnx | eligible | Addresses & locations | 716/1249 | 57.33% | 68.61% | 49.32% |
| model:pii-shield-onnx | eligible | Network identifiers | 197/361 | 54.57% | 80.06% | 50.42% |
| model:pplx | eligible | Bank accounts & cards | 173/202 | 85.64% | 99.50% | 84.16% |
| model:pplx | eligible | Documents & identifiers | 1793/2055 | 87.25% | 97.32% | 85.60% |
| model:pplx | eligible | People's names | 1124/1260 | 89.21% | 90.56% | 86.59% |
| model:pplx | eligible | Phone numbers & email | 312/389 | 80.21% | 98.46% | 79.69% |
| model:pplx | eligible | Addresses & locations | 733/1249 | 58.69% | 61.73% | 55.64% |
| model:pplx | eligible | Network identifiers | 215/361 | 59.56% | 67.87% | 59.28% |
| model:pplx+cpu-int8 | eligible | Bank accounts & cards | 190/202 | 94.06% | 100.00% | 93.07% |
| model:pplx+cpu-int8 | eligible | Documents & identifiers | 1868/2055 | 90.90% | 99.42% | 89.73% |
| model:pplx+cpu-int8 | eligible | People's names | 1214/1260 | 96.35% | 97.70% | 94.29% |
| model:pplx+cpu-int8 | eligible | Phone numbers & email | 321/389 | 82.52% | 99.23% | 82.01% |
| model:pplx+cpu-int8 | eligible | Addresses & locations | 966/1249 | 77.34% | 81.18% | 71.90% |
| model:pplx+cpu-int8 | eligible | Network identifiers | 279/361 | 77.29% | 90.30% | 77.01% |
| model:presidio-ru | eligible | Bank accounts & cards | 2/202 | 0.99% | 1.49% | 0.99% |
| model:presidio-ru | eligible | Documents & identifiers | 262/2055 | 12.75% | 13.04% | 12.75% |
| model:presidio-ru | eligible | People's names | 868/1260 | 68.89% | 70.32% | 68.89% |
| model:presidio-ru | eligible | Phone numbers & email | 235/389 | 60.41% | 61.95% | 60.41% |
| model:presidio-ru | eligible | Addresses & locations | 651/1249 | 52.12% | 62.77% | 51.96% |
| model:presidio-ru | eligible | Network identifiers | 282/361 | 78.12% | 85.32% | 77.56% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 115/202 | 56.93% | 78.22% | 29.70% |
| model:ru-legal-ner | eligible | Documents & identifiers | 1377/2055 | 67.01% | 79.17% | 59.42% |
| model:ru-legal-ner | eligible | People's names | 1038/1260 | 82.38% | 83.25% | 75.08% |
| model:ru-legal-ner | eligible | Phone numbers & email | 235/389 | 60.41% | 97.17% | 56.30% |
| model:ru-legal-ner | eligible | Addresses & locations | 521/1249 | 41.71% | 55.08% | 34.03% |
| model:ru-legal-ner | eligible | Network identifiers | 16/361 | 4.43% | 71.19% | 3.05% |
| model:ru-legal-ner+cpu-int8 | eligible | Bank accounts & cards | 117/202 | 57.92% | 78.22% | 28.71% |
| model:ru-legal-ner+cpu-int8 | eligible | Documents & identifiers | 1377/2055 | 67.01% | 78.88% | 59.56% |
| model:ru-legal-ner+cpu-int8 | eligible | People's names | 1043/1260 | 82.78% | 83.65% | 75.40% |
| model:ru-legal-ner+cpu-int8 | eligible | Phone numbers & email | 235/389 | 60.41% | 96.14% | 57.07% |
| model:ru-legal-ner+cpu-int8 | eligible | Addresses & locations | 525/1249 | 42.03% | 54.60% | 34.03% |
| model:ru-legal-ner+cpu-int8 | eligible | Network identifiers | 14/361 | 3.88% | 71.19% | 2.77% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 169/202 | 83.66% | 95.54% | 83.66% |
| model:ru-pii-ner | eligible | Documents & identifiers | 1890/2055 | 91.97% | 93.72% | 91.53% |
| model:ru-pii-ner | eligible | People's names | 1186/1260 | 94.13% | 95.56% | 93.89% |
| model:ru-pii-ner | eligible | Phone numbers & email | 273/389 | 70.18% | 80.98% | 69.41% |
| model:ru-pii-ner | eligible | Addresses & locations | 575/1249 | 46.04% | 47.72% | 45.96% |
| model:ru-pii-ner | eligible | Network identifiers | 134/361 | 37.12% | 47.65% | 36.84% |
| model:rules-ru | eligible | Bank accounts & cards | 62/202 | 30.69% | 31.19% | 30.69% |
| model:rules-ru | eligible | Documents & identifiers | 259/2055 | 12.60% | 12.70% | 12.60% |
| model:rules-ru | eligible | People's names | 3/1260 | 0.24% | 0.24% | 0.24% |
| model:rules-ru | eligible | Phone numbers & email | 235/389 | 60.41% | 64.52% | 60.41% |
| model:rules-ru | eligible | Addresses & locations | 5/1249 | 0.40% | 0.40% | 0.40% |
| model:rules-ru | eligible | Network identifiers | 240/361 | 66.48% | 76.45% | 66.48% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Documents & identifiers | 21/2055 | 1.02% | 1.02% | 1.02% |
| model:spacy-alrosait | eligible | People's names | 729/1260 | 57.86% | 59.13% | 57.86% |
| model:spacy-alrosait | eligible | Phone numbers & email | 3/389 | 0.77% | 1.54% | 0.77% |
| model:spacy-alrosait | eligible | Addresses & locations | 591/1249 | 47.32% | 55.32% | 47.32% |
| model:spacy-alrosait | eligible | Network identifiers | 1/361 | 0.28% | 0.28% | 0.28% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 0/202 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 48/2055 | 2.34% | 2.87% | 2.34% |
| model:spacy-ru-lg | eligible | People's names | 901/1260 | 71.51% | 72.94% | 71.51% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 43/389 | 11.05% | 15.42% | 10.80% |
| model:spacy-ru-lg | eligible | Addresses & locations | 681/1249 | 54.52% | 64.21% | 54.44% |
| model:spacy-ru-lg | eligible | Network identifiers | 31/361 | 8.59% | 13.30% | 8.59% |
| model:stanza-ru | eligible | Bank accounts & cards | 8/202 | 3.96% | 4.95% | 2.97% |
| model:stanza-ru | eligible | Documents & identifiers | 243/2055 | 11.82% | 19.81% | 11.63% |
| model:stanza-ru | eligible | People's names | 1177/1260 | 93.41% | 94.84% | 93.33% |
| model:stanza-ru | eligible | Phone numbers & email | 20/389 | 5.14% | 6.68% | 5.14% |
| model:stanza-ru | eligible | Addresses & locations | 898/1249 | 71.90% | 81.35% | 71.34% |
| model:stanza-ru | eligible | Network identifiers | 25/361 | 6.93% | 20.50% | 6.93% |
| model:traciora | eligible | Bank accounts & cards | 161/202 | 79.70% | 95.05% | 78.71% |
| model:traciora | eligible | Documents & identifiers | 1051/2055 | 51.14% | 64.33% | 36.93% |
| model:traciora | eligible | People's names | 982/1260 | 77.94% | 79.21% | 72.38% |
| model:traciora | eligible | Phone numbers & email | 300/389 | 77.12% | 93.32% | 75.06% |
| model:traciora | eligible | Addresses & locations | 652/1249 | 52.20% | 59.17% | 45.80% |
| model:traciora | eligible | Network identifiers | 124/361 | 34.35% | 50.69% | 29.64% |
