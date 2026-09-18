# hivetrace: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/hivetrace.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 40/95 | 42.11% | 45.26% | 42.11% |
| composition:fastino | eligible | Bank accounts & cards | 153/169 | 90.53% | 90.53% | 90.53% |
| composition:fastino | eligible | Documents & identifiers | 339/609 | 55.67% | 56.32% | 55.67% |
| composition:fastino | eligible | People's names | 226/228 | 99.12% | 99.56% | 99.12% |
| composition:fastino | eligible | Phone numbers & email | 387/390 | 99.23% | 99.49% | 99.23% |
| composition:fastino | eligible | Addresses & locations | 50/176 | 28.41% | 35.23% | 28.41% |
| composition:pplx | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 89.47% |
| composition:pplx | eligible | Bank accounts & cards | 140/169 | 82.84% | 82.84% | 82.25% |
| composition:pplx | eligible | Documents & identifiers | 596/609 | 97.87% | 100.00% | 97.70% |
| composition:pplx | eligible | People's names | 199/228 | 87.28% | 94.74% | 73.68% |
| composition:pplx | eligible | Phone numbers & email | 389/390 | 99.74% | 100.00% | 98.97% |
| composition:pplx | eligible | Addresses & locations | 167/176 | 94.89% | 97.73% | 89.20% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 93.68% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 161/169 | 95.27% | 95.27% | 95.27% |
| composition:pplx+fastino | eligible | Documents & identifiers | 597/609 | 98.03% | 100.00% | 98.03% |
| composition:pplx+fastino | eligible | People's names | 227/228 | 99.56% | 99.56% | 99.56% |
| composition:pplx+fastino | eligible | Phone numbers & email | 390/390 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Addresses & locations | 171/176 | 97.16% | 98.86% | 92.61% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 163/169 | 96.45% | 96.45% | 95.86% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 598/609 | 98.19% | 100.00% | 98.19% |
| composition:pplx+fastino+bardsai | eligible | People's names | 228/228 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 390/390 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 171/176 | 97.16% | 100.00% | 96.59% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 164/169 | 97.04% | 97.04% | 96.45% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 598/609 | 98.19% | 100.00% | 98.19% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 228/228 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 390/390 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 174/176 | 98.86% | 100.00% | 96.59% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 93.68% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 164/169 | 97.04% | 97.04% | 96.45% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 597/609 | 98.03% | 100.00% | 98.03% |
| composition:pplx+fastino+mmbert | eligible | People's names | 228/228 | 100.00% | 100.00% | 99.56% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 390/390 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 174/176 | 98.86% | 100.00% | 95.45% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 100.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Bank accounts & cards | 138/169 | 81.66% | 81.66% | 80.47% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 595/609 | 97.70% | 99.84% | 97.21% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 216/228 | 94.74% | 98.68% | 88.16% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 387/390 | 99.23% | 99.74% | 99.23% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 151/176 | 85.80% | 97.16% | 82.95% |
| model:apararti | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 100.00% |
| model:apararti | eligible | Bank accounts & cards | 119/169 | 70.41% | 70.41% | 69.82% |
| model:apararti | eligible | Documents & identifiers | 594/609 | 97.54% | 99.01% | 95.57% |
| model:apararti | eligible | People's names | 191/228 | 83.77% | 87.72% | 80.26% |
| model:apararti | eligible | Phone numbers & email | 383/390 | 98.21% | 98.72% | 97.95% |
| model:apararti | eligible | Addresses & locations | 114/176 | 64.77% | 89.20% | 61.93% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 86/95 | 90.53% | 90.53% | 65.26% |
| model:bardsai-eu | eligible | Bank accounts & cards | 74/169 | 43.79% | 46.15% | 23.08% |
| model:bardsai-eu | eligible | Documents & identifiers | 464/609 | 76.19% | 82.27% | 59.28% |
| model:bardsai-eu | eligible | People's names | 223/228 | 97.81% | 98.25% | 97.37% |
| model:bardsai-eu | eligible | Phone numbers & email | 214/390 | 54.87% | 93.85% | 48.46% |
| model:bardsai-eu | eligible | Addresses & locations | 57/176 | 32.39% | 97.16% | 28.98% |
| model:betterleaks | eligible | Passwords, keys & tokens | 17/95 | 17.89% | 17.89% | 17.89% |
| model:betterleaks | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:credsweeper | eligible | Passwords, keys & tokens | 8/95 | 8.42% | 8.42% | 8.42% |
| model:credsweeper | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:credsweeper | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:credsweeper | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:credsweeper | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:credsweeper | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:credsweeper-noml | eligible | Passwords, keys & tokens | 11/95 | 11.58% | 11.58% | 11.58% |
| model:credsweeper-noml | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:credsweeper-noml | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:credsweeper-noml | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:credsweeper-noml | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:credsweeper-noml | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | People's names | 216/228 | 94.74% | 95.61% | 87.28% |
| model:davlan-mbert | eligible | Phone numbers & email | 7/390 | 1.79% | 5.90% | 1.54% |
| model:davlan-mbert | eligible | Addresses & locations | 12/176 | 6.82% | 96.02% | 6.25% |
| model:davlan-mbert+cpu-int8 | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | People's names | 215/228 | 94.30% | 94.74% | 83.33% |
| model:davlan-mbert+cpu-int8 | eligible | Phone numbers & email | 1/390 | 0.26% | 2.56% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Addresses & locations | 10/176 | 5.68% | 93.75% | 5.11% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 224/228 | 98.25% | 98.25% | 97.37% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/390 | 0.00% | 1.54% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 19/176 | 10.80% | 97.73% | 7.95% |
| model:davlan-xlmr+cpu-int8 | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | People's names | 197/228 | 86.40% | 90.79% | 66.23% |
| model:davlan-xlmr+cpu-int8 | eligible | Phone numbers & email | 0/390 | 0.00% | 0.51% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Addresses & locations | 10/176 | 5.68% | 82.95% | 3.41% |
| model:deepsecrets | eligible | Passwords, keys & tokens | 1/95 | 1.05% | 1.05% | 1.05% |
| model:deepsecrets | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:deepsecrets | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:deepsecrets | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:deepsecrets | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:deepsecrets | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:detect-secrets | eligible | Passwords, keys & tokens | 26/95 | 27.37% | 27.37% | 27.37% |
| model:detect-secrets | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:detect-secrets | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:detect-secrets | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:detect-secrets | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:detect-secrets | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 58/95 | 61.05% | 61.05% | 40.00% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 48/169 | 28.40% | 28.40% | 9.47% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 386/609 | 63.38% | 68.47% | 54.02% |
| model:fef2-secret-ru | eligible | People's names | 218/228 | 95.61% | 98.68% | 95.18% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 216/390 | 55.38% | 58.72% | 50.51% |
| model:fef2-secret-ru | eligible | Addresses & locations | 14/176 | 7.95% | 86.93% | 7.95% |
| model:fef2-secret-ru+cpu-int8 | eligible | Passwords, keys & tokens | 44/95 | 46.32% | 46.32% | 29.47% |
| model:fef2-secret-ru+cpu-int8 | eligible | Bank accounts & cards | 39/169 | 23.08% | 23.08% | 4.14% |
| model:fef2-secret-ru+cpu-int8 | eligible | Documents & identifiers | 269/609 | 44.17% | 51.89% | 29.72% |
| model:fef2-secret-ru+cpu-int8 | eligible | People's names | 219/228 | 96.05% | 99.12% | 96.05% |
| model:fef2-secret-ru+cpu-int8 | eligible | Phone numbers & email | 191/390 | 48.97% | 54.36% | 44.62% |
| model:fef2-secret-ru+cpu-int8 | eligible | Addresses & locations | 13/176 | 7.39% | 79.55% | 7.39% |
| model:gitleaks | eligible | Passwords, keys & tokens | 17/95 | 17.89% | 17.89% | 17.89% |
| model:gitleaks | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 3/95 | 3.16% | 3.16% | 3.16% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 10/169 | 5.92% | 5.92% | 5.92% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 214/609 | 35.14% | 35.80% | 35.14% |
| model:gliner-multi-v21 | eligible | People's names | 227/228 | 99.56% | 99.56% | 99.56% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 134/390 | 34.36% | 61.28% | 34.10% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 43/176 | 24.43% | 97.16% | 21.02% |
| model:gliner-multi-v21+cpu-int8 | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21-ru | eligible | Passwords, keys & tokens | 3/95 | 3.16% | 3.16% | 3.16% |
| model:gliner-multi-v21-ru | eligible | Bank accounts & cards | 6/169 | 3.55% | 3.55% | 3.55% |
| model:gliner-multi-v21-ru | eligible | Documents & identifiers | 284/609 | 46.63% | 46.63% | 46.63% |
| model:gliner-multi-v21-ru | eligible | People's names | 226/228 | 99.12% | 99.12% | 99.12% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 134/390 | 34.36% | 61.54% | 33.33% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 41/176 | 23.30% | 96.59% | 18.75% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 91/95 | 95.79% | 95.79% | 95.79% |
| model:gliner-nvidia | eligible | Bank accounts & cards | 141/169 | 83.43% | 83.43% | 83.43% |
| model:gliner-nvidia | eligible | Documents & identifiers | 502/609 | 82.43% | 83.91% | 82.27% |
| model:gliner-nvidia | eligible | People's names | 195/228 | 85.53% | 99.12% | 53.07% |
| model:gliner-nvidia | eligible | Phone numbers & email | 365/390 | 93.59% | 94.10% | 93.59% |
| model:gliner-nvidia | eligible | Addresses & locations | 117/176 | 66.48% | 74.43% | 66.48% |
| model:gliner-nvidia+cpu-int8 | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia-ru | eligible | Passwords, keys & tokens | 85/95 | 89.47% | 89.47% | 89.47% |
| model:gliner-nvidia-ru | eligible | Bank accounts & cards | 147/169 | 86.98% | 86.98% | 86.98% |
| model:gliner-nvidia-ru | eligible | Documents & identifiers | 586/609 | 96.22% | 98.03% | 96.22% |
| model:gliner-nvidia-ru | eligible | People's names | 218/228 | 95.61% | 99.56% | 15.79% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 378/390 | 96.92% | 97.44% | 96.92% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 97/176 | 55.11% | 69.89% | 55.11% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 30/95 | 31.58% | 46.32% | 30.53% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 44/169 | 26.04% | 26.04% | 26.04% |
| model:gliner-pii-base | eligible | Documents & identifiers | 96/609 | 15.76% | 15.76% | 15.76% |
| model:gliner-pii-base | eligible | People's names | 183/228 | 80.26% | 81.14% | 80.26% |
| model:gliner-pii-base | eligible | Phone numbers & email | 301/390 | 77.18% | 77.18% | 77.18% |
| model:gliner-pii-base | eligible | Addresses & locations | 30/176 | 17.05% | 24.43% | 17.05% |
| model:gliner-pii-base+cpu-int8 | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Bank accounts & cards | 5/169 | 2.96% | 2.96% | 2.96% |
| model:gliner-pii-base+cpu-int8 | eligible | Documents & identifiers | 37/609 | 6.08% | 6.08% | 6.08% |
| model:gliner-pii-base+cpu-int8 | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Phone numbers & email | 16/390 | 4.10% | 4.10% | 4.10% |
| model:gliner-pii-base+cpu-int8 | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 35/95 | 36.84% | 37.89% | 36.84% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 147/169 | 86.98% | 86.98% | 86.98% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 528/609 | 86.70% | 89.49% | 86.37% |
| model:gliner-pii-edge | eligible | People's names | 186/228 | 81.58% | 83.77% | 81.58% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 369/390 | 94.62% | 97.44% | 94.62% |
| model:gliner-pii-edge | eligible | Addresses & locations | 28/176 | 15.91% | 57.39% | 15.91% |
| model:gliner-pii-edge+cpu-int8 | eligible | Passwords, keys & tokens | 7/95 | 7.37% | 7.37% | 7.37% |
| model:gliner-pii-edge+cpu-int8 | eligible | Bank accounts & cards | 60/169 | 35.50% | 35.50% | 35.50% |
| model:gliner-pii-edge+cpu-int8 | eligible | Documents & identifiers | 373/609 | 61.25% | 69.29% | 60.92% |
| model:gliner-pii-edge+cpu-int8 | eligible | People's names | 16/228 | 7.02% | 14.47% | 7.02% |
| model:gliner-pii-edge+cpu-int8 | eligible | Phone numbers & email | 100/390 | 25.64% | 42.82% | 25.38% |
| model:gliner-pii-edge+cpu-int8 | eligible | Addresses & locations | 3/176 | 1.70% | 22.73% | 1.70% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 84/95 | 88.42% | 89.47% | 88.42% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 156/169 | 92.31% | 99.41% | 92.31% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 418/609 | 68.64% | 89.33% | 68.31% |
| model:gliner-stream-pii | eligible | People's names | 194/228 | 85.09% | 86.84% | 84.21% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 278/390 | 71.28% | 77.95% | 71.28% |
| model:gliner-stream-pii | eligible | Addresses & locations | 27/176 | 15.34% | 78.41% | 15.34% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 33/95 | 34.74% | 34.74% | 34.74% |
| model:gliner-urchade | eligible | Bank accounts & cards | 57/169 | 33.73% | 33.73% | 33.73% |
| model:gliner-urchade | eligible | Documents & identifiers | 362/609 | 59.44% | 60.76% | 59.44% |
| model:gliner-urchade | eligible | People's names | 228/228 | 100.00% | 100.00% | 100.00% |
| model:gliner-urchade | eligible | Phone numbers & email | 367/390 | 94.10% | 94.10% | 94.10% |
| model:gliner-urchade | eligible | Addresses & locations | 125/176 | 71.02% | 75.00% | 71.02% |
| model:gliner-urchade+cpu-int8 | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade-ru | eligible | Passwords, keys & tokens | 30/95 | 31.58% | 31.58% | 31.58% |
| model:gliner-urchade-ru | eligible | Bank accounts & cards | 97/169 | 57.40% | 57.40% | 57.40% |
| model:gliner-urchade-ru | eligible | Documents & identifiers | 581/609 | 95.40% | 97.21% | 95.40% |
| model:gliner-urchade-ru | eligible | People's names | 88/228 | 38.60% | 38.60% | 38.60% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 350/390 | 89.74% | 89.74% | 89.74% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 122/176 | 69.32% | 72.73% | 69.32% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 40/95 | 42.11% | 45.26% | 42.11% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 153/169 | 90.53% | 90.53% | 90.53% |
| model:gliner2-fastino | eligible | Documents & identifiers | 339/609 | 55.67% | 56.32% | 55.67% |
| model:gliner2-fastino | eligible | People's names | 226/228 | 99.12% | 99.56% | 99.12% |
| model:gliner2-fastino | eligible | Phone numbers & email | 387/390 | 99.23% | 99.49% | 99.23% |
| model:gliner2-fastino | eligible | Addresses & locations | 50/176 | 28.41% | 35.23% | 28.41% |
| model:gliner2-fastino-ru | eligible | Passwords, keys & tokens | 40/95 | 42.11% | 44.21% | 42.11% |
| model:gliner2-fastino-ru | eligible | Bank accounts & cards | 168/169 | 99.41% | 99.41% | 99.41% |
| model:gliner2-fastino-ru | eligible | Documents & identifiers | 597/609 | 98.03% | 99.84% | 98.03% |
| model:gliner2-fastino-ru | eligible | People's names | 224/228 | 98.25% | 98.68% | 98.25% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 388/390 | 99.49% | 99.74% | 99.49% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 49/176 | 27.84% | 35.80% | 27.84% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 53/95 | 55.79% | 55.79% | 55.79% |
| model:gliner2-hivetrace-omni | eligible | Bank accounts & cards | 107/169 | 63.31% | 63.31% | 63.31% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 249/609 | 40.89% | 41.54% | 40.89% |
| model:gliner2-hivetrace-omni | eligible | People's names | 227/228 | 99.56% | 100.00% | 99.56% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 383/390 | 98.21% | 98.46% | 98.21% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 79/176 | 44.89% | 67.61% | 44.89% |
| model:gliner2-hivetrace-omni-ru | eligible | Passwords, keys & tokens | 16/95 | 16.84% | 16.84% | 16.84% |
| model:gliner2-hivetrace-omni-ru | eligible | Bank accounts & cards | 149/169 | 88.17% | 88.17% | 88.17% |
| model:gliner2-hivetrace-omni-ru | eligible | Documents & identifiers | 568/609 | 93.27% | 94.75% | 93.27% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 227/228 | 99.56% | 100.00% | 99.56% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 364/390 | 93.33% | 93.59% | 93.33% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 77/176 | 43.75% | 73.30% | 43.75% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 8/95 | 8.42% | 8.42% | 8.42% |
| model:gliner2-hivetrace-uni | eligible | Bank accounts & cards | 96/169 | 56.80% | 56.80% | 56.80% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 437/609 | 71.76% | 74.88% | 71.43% |
| model:gliner2-hivetrace-uni | eligible | People's names | 218/228 | 95.61% | 95.61% | 95.61% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 373/390 | 95.64% | 95.90% | 95.64% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 18/176 | 10.23% | 26.70% | 10.23% |
| model:gliner2-hivetrace-uni-ru | eligible | Passwords, keys & tokens | 23/95 | 24.21% | 24.21% | 24.21% |
| model:gliner2-hivetrace-uni-ru | eligible | Bank accounts & cards | 86/169 | 50.89% | 50.89% | 50.89% |
| model:gliner2-hivetrace-uni-ru | eligible | Documents & identifiers | 236/609 | 38.75% | 38.92% | 38.75% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 104/228 | 45.61% | 45.61% | 45.61% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 33/390 | 8.46% | 8.46% | 8.46% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 1/176 | 0.57% | 1.14% | 0.57% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 14/95 | 14.74% | 14.74% | 14.74% |
| model:gliner2-large | eligible | Bank accounts & cards | 84/169 | 49.70% | 49.70% | 49.70% |
| model:gliner2-large | eligible | Documents & identifiers | 301/609 | 49.43% | 51.23% | 49.43% |
| model:gliner2-large | eligible | People's names | 167/228 | 73.25% | 78.07% | 73.25% |
| model:gliner2-large | eligible | Phone numbers & email | 374/390 | 95.90% | 95.90% | 95.90% |
| model:gliner2-large | eligible | Addresses & locations | 47/176 | 26.70% | 87.50% | 26.70% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 23/95 | 24.21% | 24.21% | 24.21% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 119/169 | 70.41% | 70.41% | 70.41% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 282/609 | 46.31% | 48.11% | 46.31% |
| model:gliner2-vladlinv | eligible | People's names | 226/228 | 99.12% | 99.12% | 99.12% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 376/390 | 96.41% | 96.41% | 96.41% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 122/176 | 69.32% | 81.25% | 68.18% |
| model:gliner2-vladlinv-ru | eligible | Passwords, keys & tokens | 28/95 | 29.47% | 29.47% | 29.47% |
| model:gliner2-vladlinv-ru | eligible | Bank accounts & cards | 151/169 | 89.35% | 89.35% | 89.35% |
| model:gliner2-vladlinv-ru | eligible | Documents & identifiers | 372/609 | 61.08% | 62.89% | 61.08% |
| model:gliner2-vladlinv-ru | eligible | People's names | 227/228 | 99.56% | 99.56% | 99.56% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 376/390 | 96.41% | 96.41% | 96.41% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 126/176 | 71.59% | 81.82% | 70.45% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 3/95 | 3.16% | 3.16% | 3.16% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 16/169 | 9.47% | 9.47% | 9.47% |
| model:gliner25-fastino | eligible | Documents & identifiers | 169/609 | 27.75% | 28.41% | 27.75% |
| model:gliner25-fastino | eligible | People's names | 226/228 | 99.12% | 99.56% | 99.12% |
| model:gliner25-fastino | eligible | Phone numbers & email | 382/390 | 97.95% | 97.95% | 97.95% |
| model:gliner25-fastino | eligible | Addresses & locations | 134/176 | 76.14% | 96.02% | 76.14% |
| model:gliner25-fastino-ru | eligible | Passwords, keys & tokens | 2/95 | 2.11% | 2.11% | 2.11% |
| model:gliner25-fastino-ru | eligible | Bank accounts & cards | 30/169 | 17.75% | 17.75% | 17.75% |
| model:gliner25-fastino-ru | eligible | Documents & identifiers | 433/609 | 71.10% | 72.91% | 71.10% |
| model:gliner25-fastino-ru | eligible | People's names | 227/228 | 99.56% | 100.00% | 99.56% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 379/390 | 97.18% | 97.18% | 97.18% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 132/176 | 75.00% | 93.18% | 74.43% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 21/95 | 22.11% | 33.68% | 12.63% |
| model:gravitee-small | eligible | Bank accounts & cards | 126/169 | 74.56% | 75.15% | 57.40% |
| model:gravitee-small | eligible | Documents & identifiers | 429/609 | 70.44% | 73.56% | 56.16% |
| model:gravitee-small | eligible | People's names | 148/228 | 64.91% | 71.05% | 55.70% |
| model:gravitee-small | eligible | Phone numbers & email | 280/390 | 71.79% | 88.21% | 63.08% |
| model:gravitee-small | eligible | Addresses & locations | 122/176 | 69.32% | 92.05% | 57.95% |
| model:gravitee-small+cpu-int8 | eligible | Passwords, keys & tokens | 19/95 | 20.00% | 31.58% | 11.58% |
| model:gravitee-small+cpu-int8 | eligible | Bank accounts & cards | 130/169 | 76.92% | 78.70% | 55.03% |
| model:gravitee-small+cpu-int8 | eligible | Documents & identifiers | 445/609 | 73.07% | 75.37% | 57.47% |
| model:gravitee-small+cpu-int8 | eligible | People's names | 153/228 | 67.11% | 75.00% | 56.14% |
| model:gravitee-small+cpu-int8 | eligible | Phone numbers & email | 288/390 | 73.85% | 88.46% | 66.15% |
| model:gravitee-small+cpu-int8 | eligible | Addresses & locations | 126/176 | 71.59% | 94.32% | 61.93% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 91/95 | 95.79% | 95.79% | 56.84% |
| model:kalyan-ettin | eligible | Bank accounts & cards | 106/169 | 62.72% | 66.86% | 34.32% |
| model:kalyan-ettin | eligible | Documents & identifiers | 253/609 | 41.54% | 53.04% | 5.42% |
| model:kalyan-ettin | eligible | People's names | 108/228 | 47.37% | 92.98% | 25.00% |
| model:kalyan-ettin | eligible | Phone numbers & email | 290/390 | 74.36% | 91.54% | 63.33% |
| model:kalyan-ettin | eligible | Addresses & locations | 9/176 | 5.11% | 66.48% | 1.14% |
| model:kingfisher | eligible | Passwords, keys & tokens | 17/95 | 17.89% | 17.89% | 17.89% |
| model:kingfisher | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:kingfisher | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:kingfisher | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:kingfisher | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:kingfisher | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 76/95 | 80.00% | 97.89% | 4.21% |
| model:mmbert32k | eligible | Bank accounts & cards | 122/169 | 72.19% | 76.92% | 53.85% |
| model:mmbert32k | eligible | Documents & identifiers | 553/609 | 90.80% | 99.01% | 54.52% |
| model:mmbert32k | eligible | People's names | 203/228 | 89.04% | 97.81% | 66.67% |
| model:mmbert32k | eligible | Phone numbers & email | 263/390 | 67.44% | 100.00% | 52.31% |
| model:mmbert32k | eligible | Addresses & locations | 29/176 | 16.48% | 98.30% | 2.27% |
| model:mmbert32k+cpu-int8 | eligible | Passwords, keys & tokens | 76/95 | 80.00% | 97.89% | 1.05% |
| model:mmbert32k+cpu-int8 | eligible | Bank accounts & cards | 106/169 | 62.72% | 68.05% | 3.55% |
| model:mmbert32k+cpu-int8 | eligible | Documents & identifiers | 498/609 | 81.77% | 97.87% | 2.13% |
| model:mmbert32k+cpu-int8 | eligible | People's names | 58/228 | 25.44% | 68.42% | 9.65% |
| model:mmbert32k+cpu-int8 | eligible | Phone numbers & email | 112/390 | 28.72% | 91.79% | 5.13% |
| model:mmbert32k+cpu-int8 | eligible | Addresses & locations | 5/176 | 2.84% | 72.16% | 0.00% |
| model:natasha | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 10/609 | 1.64% | 1.64% | 1.64% |
| model:natasha | eligible | People's names | 215/228 | 94.30% | 94.30% | 94.30% |
| model:natasha | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Addresses & locations | 10/176 | 5.68% | 70.45% | 5.68% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 6/228 | 2.63% | 98.25% | 2.63% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/390 | 0.00% | 27.69% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 9/176 | 5.11% | 98.30% | 2.27% |
| model:ner-ru-gherman+cpu-int8 | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | People's names | 5/228 | 2.19% | 97.81% | 1.75% |
| model:ner-ru-gherman+cpu-int8 | eligible | Phone numbers & email | 0/390 | 0.00% | 24.10% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Addresses & locations | 9/176 | 5.11% | 96.02% | 2.84% |
| model:ner-ru-gherman-onnx | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | People's names | 5/228 | 2.19% | 97.81% | 2.19% |
| model:ner-ru-gherman-onnx | eligible | Phone numbers & email | 0/390 | 0.00% | 27.44% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Addresses & locations | 9/176 | 5.11% | 98.30% | 2.27% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 51/95 | 53.68% | 53.68% | 3.16% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 41/169 | 24.26% | 26.63% | 20.12% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 72/609 | 11.82% | 14.12% | 5.09% |
| model:ner-ru-yqelz | eligible | People's names | 227/228 | 99.56% | 100.00% | 98.68% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 27/390 | 6.92% | 11.28% | 3.85% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 30/176 | 17.05% | 100.00% | 16.48% |
| model:noseyparker | eligible | Passwords, keys & tokens | 17/95 | 17.89% | 17.89% | 17.89% |
| model:noseyparker | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:noseyparker | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:noseyparker | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:noseyparker | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:noseyparker | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 53/95 | 55.79% | 65.26% | 51.58% |
| model:nuner-zero | eligible | Bank accounts & cards | 126/169 | 74.56% | 75.15% | 68.64% |
| model:nuner-zero | eligible | Documents & identifiers | 493/609 | 80.95% | 82.10% | 62.73% |
| model:nuner-zero | eligible | People's names | 228/228 | 100.00% | 100.00% | 3.51% |
| model:nuner-zero | eligible | Phone numbers & email | 377/390 | 96.67% | 96.92% | 89.23% |
| model:nuner-zero | eligible | Addresses & locations | 102/176 | 57.95% | 98.86% | 3.98% |
| model:nym-base | eligible | Passwords, keys & tokens | 80/95 | 84.21% | 98.95% | 71.58% |
| model:nym-base | eligible | Bank accounts & cards | 166/169 | 98.22% | 98.22% | 98.22% |
| model:nym-base | eligible | Documents & identifiers | 596/609 | 97.87% | 99.67% | 91.95% |
| model:nym-base | eligible | People's names | 14/228 | 6.14% | 99.56% | 98.25% |
| model:nym-base | eligible | Phone numbers & email | 353/390 | 90.51% | 97.44% | 90.26% |
| model:nym-base | eligible | Addresses & locations | 33/176 | 18.75% | 100.00% | 27.27% |
| model:nym-base+cpu-int8 | eligible | Passwords, keys & tokens | 82/95 | 86.32% | 98.95% | 70.53% |
| model:nym-base+cpu-int8 | eligible | Bank accounts & cards | 166/169 | 98.22% | 98.22% | 95.86% |
| model:nym-base+cpu-int8 | eligible | Documents & identifiers | 592/609 | 97.21% | 99.01% | 92.28% |
| model:nym-base+cpu-int8 | eligible | People's names | 16/228 | 7.02% | 99.56% | 97.81% |
| model:nym-base+cpu-int8 | eligible | Phone numbers & email | 361/390 | 92.56% | 97.44% | 91.79% |
| model:nym-base+cpu-int8 | eligible | Addresses & locations | 29/176 | 16.48% | 99.43% | 26.70% |
| model:nym-small | eligible | Passwords, keys & tokens | 78/95 | 82.11% | 100.00% | 66.32% |
| model:nym-small | eligible | Bank accounts & cards | 161/169 | 95.27% | 95.27% | 91.72% |
| model:nym-small | eligible | Documents & identifiers | 597/609 | 98.03% | 99.84% | 94.25% |
| model:nym-small | eligible | People's names | 17/228 | 7.46% | 98.68% | 97.37% |
| model:nym-small | eligible | Phone numbers & email | 378/390 | 96.92% | 99.23% | 95.64% |
| model:nym-small | eligible | Addresses & locations | 35/176 | 19.89% | 100.00% | 23.86% |
| model:openai-base | eligible | Passwords, keys & tokens | 94/95 | 98.95% | 98.95% | 98.95% |
| model:openai-base | eligible | Bank accounts & cards | 105/169 | 62.13% | 62.72% | 59.76% |
| model:openai-base | eligible | Documents & identifiers | 564/609 | 92.61% | 94.09% | 90.80% |
| model:openai-base | eligible | People's names | 192/228 | 84.21% | 86.40% | 82.02% |
| model:openai-base | eligible | Phone numbers & email | 374/390 | 95.90% | 96.15% | 95.90% |
| model:openai-base | eligible | Addresses & locations | 119/176 | 67.61% | 89.20% | 68.18% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 87/95 | 91.58% | 94.74% | 48.42% |
| model:openmed-multilingual | eligible | Bank accounts & cards | 153/169 | 90.53% | 90.53% | 89.94% |
| model:openmed-multilingual | eligible | Documents & identifiers | 538/609 | 88.34% | 92.12% | 79.64% |
| model:openmed-multilingual | eligible | People's names | 13/228 | 5.70% | 79.82% | 59.21% |
| model:openmed-multilingual | eligible | Phone numbers & email | 361/390 | 92.56% | 99.49% | 90.51% |
| model:openmed-multilingual | eligible | Addresses & locations | 11/176 | 6.25% | 92.61% | 6.25% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 88/95 | 92.63% | 92.63% | 36.84% |
| model:openmed-nemotron | eligible | Bank accounts & cards | 109/169 | 64.50% | 64.50% | 39.64% |
| model:openmed-nemotron | eligible | Documents & identifiers | 305/609 | 50.08% | 58.95% | 16.42% |
| model:openmed-nemotron | eligible | People's names | 39/228 | 17.11% | 93.42% | 67.54% |
| model:openmed-nemotron | eligible | Phone numbers & email | 302/390 | 77.44% | 91.03% | 63.85% |
| model:openmed-nemotron | eligible | Addresses & locations | 45/176 | 25.57% | 93.75% | 22.73% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 100.00% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 112/169 | 66.27% | 66.86% | 66.27% |
| model:opf-kz-ru | eligible | Documents & identifiers | 588/609 | 96.55% | 99.51% | 96.72% |
| model:opf-kz-ru | eligible | People's names | 192/228 | 84.21% | 88.16% | 78.07% |
| model:opf-kz-ru | eligible | Phone numbers & email | 376/390 | 96.41% | 98.46% | 94.87% |
| model:opf-kz-ru | eligible | Addresses & locations | 34/176 | 19.32% | 81.25% | 15.91% |
| model:opf-ru | eligible | Passwords, keys & tokens | 94/95 | 98.95% | 98.95% | 87.37% |
| model:opf-ru | eligible | Bank accounts & cards | 120/169 | 71.01% | 72.19% | 68.05% |
| model:opf-ru | eligible | Documents & identifiers | 580/609 | 95.24% | 99.18% | 88.18% |
| model:opf-ru | eligible | People's names | 202/228 | 88.60% | 97.81% | 79.82% |
| model:opf-ru | eligible | Phone numbers & email | 359/390 | 92.05% | 97.95% | 90.77% |
| model:opf-ru | eligible | Addresses & locations | 12/176 | 6.82% | 90.34% | 1.14% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 94/95 | 98.95% | 98.95% | 96.84% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 117/169 | 69.23% | 69.23% | 64.50% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 571/609 | 93.76% | 99.18% | 90.15% |
| model:opf-ru-v2 | eligible | People's names | 196/228 | 85.96% | 89.47% | 83.33% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 352/390 | 90.26% | 94.62% | 89.23% |
| model:opf-ru-v2 | eligible | Addresses & locations | 114/176 | 64.77% | 87.50% | 60.80% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 94/95 | 98.95% | 98.95% | 98.95% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 129/169 | 76.33% | 76.33% | 65.68% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 487/609 | 79.97% | 83.74% | 70.44% |
| model:pii-shield-onnx | eligible | People's names | 195/228 | 85.53% | 94.30% | 82.89% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 387/390 | 99.23% | 99.23% | 99.23% |
| model:pii-shield-onnx | eligible | Addresses & locations | 22/176 | 12.50% | 91.48% | 14.77% |
| model:pplx | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 89.47% |
| model:pplx | eligible | Bank accounts & cards | 140/169 | 82.84% | 82.84% | 82.25% |
| model:pplx | eligible | Documents & identifiers | 596/609 | 97.87% | 100.00% | 97.70% |
| model:pplx | eligible | People's names | 199/228 | 87.28% | 94.74% | 73.68% |
| model:pplx | eligible | Phone numbers & email | 389/390 | 99.74% | 100.00% | 98.97% |
| model:pplx | eligible | Addresses & locations | 167/176 | 94.89% | 97.73% | 89.20% |
| model:pplx+cpu-int8 | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 100.00% |
| model:pplx+cpu-int8 | eligible | Bank accounts & cards | 160/169 | 94.67% | 94.67% | 94.08% |
| model:pplx+cpu-int8 | eligible | Documents & identifiers | 598/609 | 98.19% | 100.00% | 97.37% |
| model:pplx+cpu-int8 | eligible | People's names | 221/228 | 96.93% | 99.12% | 83.77% |
| model:pplx+cpu-int8 | eligible | Phone numbers & email | 389/390 | 99.74% | 99.74% | 98.97% |
| model:pplx+cpu-int8 | eligible | Addresses & locations | 169/176 | 96.02% | 98.86% | 93.18% |
| model:presidio-ru | eligible | Passwords, keys & tokens | 9/95 | 9.47% | 9.47% | 5.26% |
| model:presidio-ru | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:presidio-ru | eligible | Documents & identifiers | 498/609 | 81.77% | 81.77% | 81.77% |
| model:presidio-ru | eligible | People's names | 224/228 | 98.25% | 98.68% | 97.81% |
| model:presidio-ru | eligible | Phone numbers & email | 378/390 | 96.92% | 96.92% | 96.92% |
| model:presidio-ru | eligible | Addresses & locations | 12/176 | 6.82% | 89.20% | 6.82% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 75/95 | 78.95% | 95.79% | 13.68% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 87/169 | 51.48% | 54.44% | 44.97% |
| model:ru-legal-ner | eligible | Documents & identifiers | 542/609 | 89.00% | 91.63% | 75.37% |
| model:ru-legal-ner | eligible | People's names | 222/228 | 97.37% | 98.25% | 95.18% |
| model:ru-legal-ner | eligible | Phone numbers & email | 247/390 | 63.33% | 92.31% | 55.38% |
| model:ru-legal-ner | eligible | Addresses & locations | 23/176 | 13.07% | 84.66% | 12.50% |
| model:ru-legal-ner+cpu-int8 | eligible | Passwords, keys & tokens | 75/95 | 78.95% | 94.74% | 9.47% |
| model:ru-legal-ner+cpu-int8 | eligible | Bank accounts & cards | 86/169 | 50.89% | 54.44% | 43.79% |
| model:ru-legal-ner+cpu-int8 | eligible | Documents & identifiers | 537/609 | 88.18% | 91.30% | 74.38% |
| model:ru-legal-ner+cpu-int8 | eligible | People's names | 221/228 | 96.93% | 97.81% | 94.74% |
| model:ru-legal-ner+cpu-int8 | eligible | Phone numbers & email | 244/390 | 62.56% | 92.56% | 53.85% |
| model:ru-legal-ner+cpu-int8 | eligible | Addresses & locations | 21/176 | 11.93% | 84.09% | 11.36% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 16/95 | 16.84% | 16.84% | 11.58% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 156/169 | 92.31% | 92.31% | 92.31% |
| model:ru-pii-ner | eligible | Documents & identifiers | 549/609 | 90.15% | 92.28% | 90.15% |
| model:ru-pii-ner | eligible | People's names | 226/228 | 99.12% | 99.12% | 99.12% |
| model:ru-pii-ner | eligible | Phone numbers & email | 385/390 | 98.72% | 98.72% | 98.72% |
| model:ru-pii-ner | eligible | Addresses & locations | 142/176 | 80.68% | 88.64% | 80.68% |
| model:rules-ru | eligible | Passwords, keys & tokens | 18/95 | 18.95% | 18.95% | 18.95% |
| model:rules-ru | eligible | Bank accounts & cards | 92/169 | 54.44% | 54.44% | 54.44% |
| model:rules-ru | eligible | Documents & identifiers | 584/609 | 95.89% | 95.89% | 95.89% |
| model:rules-ru | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 378/390 | 96.92% | 96.92% | 96.92% |
| model:rules-ru | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 212/228 | 92.98% | 93.86% | 92.98% |
| model:spacy-alrosait | eligible | Phone numbers & email | 1/390 | 0.26% | 0.51% | 0.26% |
| model:spacy-alrosait | eligible | Addresses & locations | 150/176 | 85.23% | 90.91% | 85.23% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 7/95 | 7.37% | 7.37% | 7.37% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 3/609 | 0.49% | 0.49% | 0.49% |
| model:spacy-ru-lg | eligible | People's names | 226/228 | 99.12% | 99.56% | 98.68% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 17/390 | 4.36% | 4.36% | 4.36% |
| model:spacy-ru-lg | eligible | Addresses & locations | 9/176 | 5.11% | 94.32% | 5.11% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 10/95 | 10.53% | 18.95% | 8.42% |
| model:stanza-ru | eligible | Bank accounts & cards | 19/169 | 11.24% | 11.24% | 11.24% |
| model:stanza-ru | eligible | Documents & identifiers | 99/609 | 16.26% | 16.42% | 16.26% |
| model:stanza-ru | eligible | People's names | 216/228 | 94.74% | 94.74% | 94.30% |
| model:stanza-ru | eligible | Phone numbers & email | 19/390 | 4.87% | 4.87% | 4.87% |
| model:stanza-ru | eligible | Addresses & locations | 20/176 | 11.36% | 89.20% | 11.36% |
| model:titus | eligible | Passwords, keys & tokens | 17/95 | 17.89% | 17.89% | 17.89% |
| model:titus | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:titus | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:titus | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:titus | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:titus | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:traciora | eligible | Passwords, keys & tokens | 91/95 | 95.79% | 95.79% | 90.53% |
| model:traciora | eligible | Bank accounts & cards | 89/169 | 52.66% | 53.25% | 47.93% |
| model:traciora | eligible | Documents & identifiers | 541/609 | 88.83% | 92.78% | 69.79% |
| model:traciora | eligible | People's names | 204/228 | 89.47% | 93.86% | 86.40% |
| model:traciora | eligible | Phone numbers & email | 371/390 | 95.13% | 96.92% | 90.51% |
| model:traciora | eligible | Addresses & locations | 132/176 | 75.00% | 90.34% | 73.30% |
| model:trufflehog | eligible | Passwords, keys & tokens | 1/95 | 1.05% | 1.05% | 1.05% |
| model:trufflehog | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:trufflehog | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:trufflehog | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:trufflehog | eligible | Phone numbers & email | 0/390 | 0.00% | 0.00% | 0.00% |
| model:trufflehog | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
