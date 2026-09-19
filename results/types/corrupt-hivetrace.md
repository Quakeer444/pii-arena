# corrupt-hivetrace: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/corrupt-hivetrace.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 31/95 | 32.63% | 41.05% | 32.63% |
| composition:fastino | eligible | Bank accounts & cards | 141/169 | 83.43% | 84.62% | 82.25% |
| composition:fastino | eligible | Documents & identifiers | 359/609 | 58.95% | 60.43% | 58.46% |
| composition:fastino | eligible | People's names | 183/228 | 80.26% | 85.09% | 79.82% |
| composition:fastino | eligible | Phone numbers & email | 324/390 | 83.08% | 93.33% | 82.82% |
| composition:fastino | eligible | Addresses & locations | 36/176 | 20.45% | 30.68% | 20.45% |
| composition:pplx | eligible | Passwords, keys & tokens | 92/95 | 96.84% | 97.89% | 86.32% |
| composition:pplx | eligible | Bank accounts & cards | 127/169 | 75.15% | 75.74% | 73.37% |
| composition:pplx | eligible | Documents & identifiers | 590/609 | 96.88% | 99.84% | 94.25% |
| composition:pplx | eligible | People's names | 203/228 | 89.04% | 96.05% | 80.26% |
| composition:pplx | eligible | Phone numbers & email | 384/390 | 98.46% | 99.49% | 97.18% |
| composition:pplx | eligible | Addresses & locations | 166/176 | 94.32% | 98.30% | 91.48% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 93/95 | 97.89% | 98.95% | 91.58% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 156/169 | 92.31% | 92.31% | 91.12% |
| composition:pplx+fastino | eligible | Documents & identifiers | 596/609 | 97.87% | 99.84% | 95.89% |
| composition:pplx+fastino | eligible | People's names | 219/228 | 96.05% | 98.25% | 92.54% |
| composition:pplx+fastino | eligible | Phone numbers & email | 386/390 | 98.97% | 100.00% | 98.21% |
| composition:pplx+fastino | eligible | Addresses & locations | 167/176 | 94.89% | 98.30% | 92.61% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 96.84% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 157/169 | 92.90% | 92.90% | 91.72% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 598/609 | 98.19% | 99.84% | 96.22% |
| composition:pplx+fastino+bardsai | eligible | People's names | 222/228 | 97.37% | 98.68% | 94.74% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 387/390 | 99.23% | 100.00% | 98.46% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 169/176 | 96.02% | 99.43% | 94.32% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 95/95 | 100.00% | 100.00% | 96.84% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 161/169 | 95.27% | 95.86% | 92.31% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 600/609 | 98.52% | 100.00% | 96.39% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 223/228 | 97.81% | 99.56% | 95.61% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 388/390 | 99.49% | 100.00% | 98.97% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 172/176 | 97.73% | 100.00% | 95.45% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 94/95 | 98.95% | 100.00% | 91.58% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 161/169 | 95.27% | 95.86% | 92.31% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 599/609 | 98.36% | 100.00% | 96.22% |
| composition:pplx+fastino+mmbert | eligible | People's names | 221/228 | 96.93% | 99.56% | 93.42% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 387/390 | 99.23% | 100.00% | 98.72% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 171/176 | 97.16% | 100.00% | 94.89% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 92/95 | 96.84% | 98.95% | 95.79% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Bank accounts & cards | 100/169 | 59.17% | 68.64% | 57.40% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 532/609 | 87.36% | 98.85% | 84.40% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 177/228 | 77.63% | 91.23% | 67.98% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 365/390 | 93.59% | 97.18% | 92.56% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 105/176 | 59.66% | 92.05% | 57.95% |
| model:apararti | eligible | Passwords, keys & tokens | 94/95 | 98.95% | 100.00% | 95.79% |
| model:apararti | eligible | Bank accounts & cards | 108/169 | 63.91% | 69.82% | 59.76% |
| model:apararti | eligible | Documents & identifiers | 541/609 | 88.83% | 95.07% | 82.76% |
| model:apararti | eligible | People's names | 162/228 | 71.05% | 76.75% | 63.16% |
| model:apararti | eligible | Phone numbers & email | 366/390 | 93.85% | 98.72% | 90.51% |
| model:apararti | eligible | Addresses & locations | 69/176 | 39.20% | 85.80% | 38.07% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 78/95 | 82.11% | 88.42% | 55.79% |
| model:bardsai-eu | eligible | Bank accounts & cards | 63/169 | 37.28% | 44.38% | 22.49% |
| model:bardsai-eu | eligible | Documents & identifiers | 437/609 | 71.76% | 79.47% | 58.46% |
| model:bardsai-eu | eligible | People's names | 185/228 | 81.14% | 85.53% | 72.81% |
| model:bardsai-eu | eligible | Phone numbers & email | 184/390 | 47.18% | 88.72% | 43.33% |
| model:bardsai-eu | eligible | Addresses & locations | 45/176 | 25.57% | 87.50% | 19.32% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | People's names | 173/228 | 75.88% | 84.21% | 57.46% |
| model:davlan-mbert | eligible | Phone numbers & email | 8/390 | 2.05% | 8.21% | 1.03% |
| model:davlan-mbert | eligible | Addresses & locations | 12/176 | 6.82% | 85.23% | 5.11% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 0/169 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 190/228 | 83.33% | 92.54% | 74.56% |
| model:davlan-xlmr | eligible | Phone numbers & email | 1/390 | 0.26% | 2.31% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 18/176 | 10.23% | 90.34% | 9.09% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 49/95 | 51.58% | 52.63% | 35.79% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 29/169 | 17.16% | 23.08% | 8.88% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 306/609 | 50.25% | 57.14% | 41.87% |
| model:fef2-secret-ru | eligible | People's names | 181/228 | 79.39% | 90.35% | 72.81% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 178/390 | 45.64% | 53.33% | 41.28% |
| model:fef2-secret-ru | eligible | Addresses & locations | 16/176 | 9.09% | 83.52% | 7.95% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 1/95 | 1.05% | 1.05% | 1.05% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 6/169 | 3.55% | 3.55% | 3.55% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 138/609 | 22.66% | 26.77% | 22.50% |
| model:gliner-multi-v21 | eligible | People's names | 187/228 | 82.02% | 87.72% | 82.02% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 103/390 | 26.41% | 54.62% | 25.90% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 32/176 | 18.18% | 86.93% | 15.91% |
| model:gliner-multi-v21-ru | eligible | Passwords, keys & tokens | 3/95 | 3.16% | 3.16% | 3.16% |
| model:gliner-multi-v21-ru | eligible | Bank accounts & cards | 4/169 | 2.37% | 2.37% | 2.37% |
| model:gliner-multi-v21-ru | eligible | Documents & identifiers | 207/609 | 33.99% | 39.08% | 33.66% |
| model:gliner-multi-v21-ru | eligible | People's names | 179/228 | 78.51% | 85.96% | 78.51% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 96/390 | 24.62% | 49.74% | 23.33% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 35/176 | 19.89% | 90.91% | 15.91% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 77/95 | 81.05% | 87.37% | 81.05% |
| model:gliner-nvidia | eligible | Bank accounts & cards | 108/169 | 63.91% | 71.01% | 63.91% |
| model:gliner-nvidia | eligible | Documents & identifiers | 417/609 | 68.47% | 74.88% | 68.47% |
| model:gliner-nvidia | eligible | People's names | 131/228 | 57.46% | 84.65% | 43.42% |
| model:gliner-nvidia | eligible | Phone numbers & email | 329/390 | 84.36% | 88.72% | 84.36% |
| model:gliner-nvidia | eligible | Addresses & locations | 78/176 | 44.32% | 64.20% | 43.18% |
| model:gliner-nvidia+homoglyph | eligible | Passwords, keys & tokens | 77/95 | 81.05% | 87.37% | 81.05% |
| model:gliner-nvidia+homoglyph | eligible | Bank accounts & cards | 108/169 | 63.91% | 71.01% | 63.91% |
| model:gliner-nvidia+homoglyph | eligible | Documents & identifiers | 418/609 | 68.64% | 75.21% | 68.47% |
| model:gliner-nvidia+homoglyph | eligible | People's names | 134/228 | 58.77% | 86.40% | 40.35% |
| model:gliner-nvidia+homoglyph | eligible | Phone numbers & email | 329/390 | 84.36% | 88.72% | 84.36% |
| model:gliner-nvidia+homoglyph | eligible | Addresses & locations | 80/176 | 45.45% | 67.05% | 44.89% |
| model:gliner-nvidia-ru | eligible | Passwords, keys & tokens | 61/95 | 64.21% | 65.26% | 64.21% |
| model:gliner-nvidia-ru | eligible | Bank accounts & cards | 110/169 | 65.09% | 71.01% | 64.50% |
| model:gliner-nvidia-ru | eligible | Documents & identifiers | 511/609 | 83.91% | 88.83% | 83.91% |
| model:gliner-nvidia-ru | eligible | People's names | 102/228 | 44.74% | 89.04% | 26.75% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 337/390 | 86.41% | 92.05% | 86.15% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 65/176 | 36.93% | 67.61% | 36.93% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 27/95 | 28.42% | 45.26% | 27.37% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 31/169 | 18.34% | 18.93% | 18.34% |
| model:gliner-pii-base | eligible | Documents & identifiers | 63/609 | 10.34% | 10.51% | 10.34% |
| model:gliner-pii-base | eligible | People's names | 101/228 | 44.30% | 46.05% | 44.30% |
| model:gliner-pii-base | eligible | Phone numbers & email | 250/390 | 64.10% | 65.90% | 64.10% |
| model:gliner-pii-base | eligible | Addresses & locations | 21/176 | 11.93% | 17.05% | 11.93% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 29/95 | 30.53% | 36.84% | 30.53% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 109/169 | 64.50% | 72.19% | 63.91% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 461/609 | 75.70% | 84.07% | 73.40% |
| model:gliner-pii-edge | eligible | People's names | 138/228 | 60.53% | 68.86% | 60.09% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 290/390 | 74.36% | 83.85% | 74.36% |
| model:gliner-pii-edge | eligible | Addresses & locations | 27/176 | 15.34% | 51.70% | 15.34% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 48/95 | 50.53% | 78.95% | 49.47% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 103/169 | 60.95% | 89.94% | 57.99% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 251/609 | 41.22% | 75.86% | 39.08% |
| model:gliner-stream-pii | eligible | People's names | 114/228 | 50.00% | 64.04% | 48.68% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 165/390 | 42.31% | 63.08% | 41.54% |
| model:gliner-stream-pii | eligible | Addresses & locations | 16/176 | 9.09% | 56.82% | 9.09% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 27/95 | 28.42% | 35.79% | 28.42% |
| model:gliner-urchade | eligible | Bank accounts & cards | 46/169 | 27.22% | 28.40% | 27.22% |
| model:gliner-urchade | eligible | Documents & identifiers | 325/609 | 53.37% | 56.49% | 53.20% |
| model:gliner-urchade | eligible | People's names | 206/228 | 90.35% | 96.93% | 90.35% |
| model:gliner-urchade | eligible | Phone numbers & email | 336/390 | 86.15% | 89.74% | 86.15% |
| model:gliner-urchade | eligible | Addresses & locations | 103/176 | 58.52% | 65.34% | 58.52% |
| model:gliner-urchade-ru | eligible | Passwords, keys & tokens | 20/95 | 21.05% | 27.37% | 21.05% |
| model:gliner-urchade-ru | eligible | Bank accounts & cards | 87/169 | 51.48% | 53.25% | 51.48% |
| model:gliner-urchade-ru | eligible | Documents & identifiers | 546/609 | 89.66% | 94.25% | 89.66% |
| model:gliner-urchade-ru | eligible | People's names | 84/228 | 36.84% | 39.04% | 36.84% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 315/390 | 80.77% | 81.54% | 80.77% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 101/176 | 57.39% | 67.05% | 57.39% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 31/95 | 32.63% | 41.05% | 32.63% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 141/169 | 83.43% | 84.62% | 82.25% |
| model:gliner2-fastino | eligible | Documents & identifiers | 359/609 | 58.95% | 60.43% | 58.46% |
| model:gliner2-fastino | eligible | People's names | 183/228 | 80.26% | 85.09% | 79.82% |
| model:gliner2-fastino | eligible | Phone numbers & email | 324/390 | 83.08% | 93.33% | 82.82% |
| model:gliner2-fastino | eligible | Addresses & locations | 36/176 | 20.45% | 30.68% | 20.45% |
| model:gliner2-fastino-ru | eligible | Passwords, keys & tokens | 43/95 | 45.26% | 53.68% | 41.05% |
| model:gliner2-fastino-ru | eligible | Bank accounts & cards | 161/169 | 95.27% | 97.04% | 94.67% |
| model:gliner2-fastino-ru | eligible | Documents & identifiers | 573/609 | 94.09% | 97.54% | 92.78% |
| model:gliner2-fastino-ru | eligible | People's names | 182/228 | 79.82% | 84.21% | 79.39% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 330/390 | 84.62% | 93.85% | 83.85% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 39/176 | 22.16% | 35.80% | 22.16% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 45/95 | 47.37% | 47.37% | 47.37% |
| model:gliner2-hivetrace-omni | eligible | Bank accounts & cards | 103/169 | 60.95% | 60.95% | 60.95% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 227/609 | 37.27% | 37.93% | 37.27% |
| model:gliner2-hivetrace-omni | eligible | People's names | 202/228 | 88.60% | 92.54% | 88.60% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 324/390 | 83.08% | 88.97% | 83.08% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 61/176 | 34.66% | 66.48% | 34.66% |
| model:gliner2-hivetrace-omni-ru | eligible | Passwords, keys & tokens | 13/95 | 13.68% | 13.68% | 13.68% |
| model:gliner2-hivetrace-omni-ru | eligible | Bank accounts & cards | 137/169 | 81.07% | 82.25% | 81.07% |
| model:gliner2-hivetrace-omni-ru | eligible | Documents & identifiers | 517/609 | 84.89% | 86.86% | 84.89% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 204/228 | 89.47% | 94.30% | 89.04% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 300/390 | 76.92% | 84.62% | 76.92% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 59/176 | 33.52% | 77.84% | 33.52% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 7/95 | 7.37% | 9.47% | 7.37% |
| model:gliner2-hivetrace-uni | eligible | Bank accounts & cards | 69/169 | 40.83% | 50.89% | 40.83% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 317/609 | 52.05% | 67.65% | 50.57% |
| model:gliner2-hivetrace-uni | eligible | People's names | 175/228 | 76.75% | 84.21% | 76.75% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 256/390 | 65.64% | 80.26% | 64.62% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 21/176 | 11.93% | 38.07% | 11.93% |
| model:gliner2-hivetrace-uni-ru | eligible | Passwords, keys & tokens | 14/95 | 14.74% | 20.00% | 14.74% |
| model:gliner2-hivetrace-uni-ru | eligible | Bank accounts & cards | 56/169 | 33.14% | 36.69% | 33.14% |
| model:gliner2-hivetrace-uni-ru | eligible | Documents & identifiers | 162/609 | 26.60% | 30.21% | 26.60% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 101/228 | 44.30% | 46.93% | 44.30% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 22/390 | 5.64% | 12.56% | 5.64% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 4/176 | 2.27% | 7.95% | 2.27% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 7/95 | 7.37% | 10.53% | 6.32% |
| model:gliner2-large | eligible | Bank accounts & cards | 71/169 | 42.01% | 44.38% | 42.01% |
| model:gliner2-large | eligible | Documents & identifiers | 282/609 | 46.31% | 48.11% | 46.31% |
| model:gliner2-large | eligible | People's names | 126/228 | 55.26% | 64.04% | 55.26% |
| model:gliner2-large | eligible | Phone numbers & email | 312/390 | 80.00% | 85.90% | 79.74% |
| model:gliner2-large | eligible | Addresses & locations | 33/176 | 18.75% | 79.55% | 18.75% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 17/95 | 17.89% | 29.47% | 16.84% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 94/169 | 55.62% | 57.99% | 55.03% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 267/609 | 43.84% | 45.98% | 43.19% |
| model:gliner2-vladlinv | eligible | People's names | 194/228 | 85.09% | 93.42% | 85.09% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 331/390 | 84.87% | 88.46% | 84.62% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 107/176 | 60.80% | 70.45% | 59.66% |
| model:gliner2-vladlinv+homoglyph | eligible | Passwords, keys & tokens | 17/95 | 17.89% | 29.47% | 16.84% |
| model:gliner2-vladlinv+homoglyph | eligible | Bank accounts & cards | 94/169 | 55.62% | 57.99% | 55.03% |
| model:gliner2-vladlinv+homoglyph | eligible | Documents & identifiers | 267/609 | 43.84% | 45.98% | 43.19% |
| model:gliner2-vladlinv+homoglyph | eligible | People's names | 194/228 | 85.09% | 93.42% | 85.09% |
| model:gliner2-vladlinv+homoglyph | eligible | Phone numbers & email | 335/390 | 85.90% | 88.97% | 85.64% |
| model:gliner2-vladlinv+homoglyph | eligible | Addresses & locations | 106/176 | 60.23% | 71.59% | 59.09% |
| model:gliner2-vladlinv-ru | eligible | Passwords, keys & tokens | 20/95 | 21.05% | 35.79% | 20.00% |
| model:gliner2-vladlinv-ru | eligible | Bank accounts & cards | 134/169 | 79.29% | 82.25% | 78.70% |
| model:gliner2-vladlinv-ru | eligible | Documents & identifiers | 347/609 | 56.98% | 59.77% | 56.49% |
| model:gliner2-vladlinv-ru | eligible | People's names | 195/228 | 85.53% | 91.67% | 85.53% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 331/390 | 84.87% | 88.46% | 84.62% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 112/176 | 63.64% | 72.73% | 62.50% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 2/95 | 2.11% | 2.11% | 2.11% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 12/169 | 7.10% | 7.10% | 6.51% |
| model:gliner25-fastino | eligible | Documents & identifiers | 151/609 | 24.79% | 26.93% | 24.14% |
| model:gliner25-fastino | eligible | People's names | 179/228 | 78.51% | 86.84% | 78.51% |
| model:gliner25-fastino | eligible | Phone numbers & email | 323/390 | 82.82% | 92.31% | 80.51% |
| model:gliner25-fastino | eligible | Addresses & locations | 120/176 | 68.18% | 88.64% | 68.18% |
| model:gliner25-fastino-ru | eligible | Passwords, keys & tokens | 2/95 | 2.11% | 2.11% | 2.11% |
| model:gliner25-fastino-ru | eligible | Bank accounts & cards | 23/169 | 13.61% | 14.79% | 13.02% |
| model:gliner25-fastino-ru | eligible | Documents & identifiers | 393/609 | 64.53% | 68.14% | 63.05% |
| model:gliner25-fastino-ru | eligible | People's names | 176/228 | 77.19% | 85.96% | 77.19% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 321/390 | 82.31% | 91.03% | 78.72% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 121/176 | 68.75% | 89.20% | 68.75% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 19/95 | 20.00% | 33.68% | 10.53% |
| model:gravitee-small | eligible | Bank accounts & cards | 119/169 | 70.41% | 75.15% | 58.58% |
| model:gravitee-small | eligible | Documents & identifiers | 410/609 | 67.32% | 73.73% | 54.84% |
| model:gravitee-small | eligible | People's names | 127/228 | 55.70% | 61.84% | 42.98% |
| model:gravitee-small | eligible | Phone numbers & email | 267/390 | 68.46% | 87.44% | 58.21% |
| model:gravitee-small | eligible | Addresses & locations | 101/176 | 57.39% | 90.34% | 48.30% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 84/95 | 88.42% | 97.89% | 38.95% |
| model:kalyan-ettin | eligible | Bank accounts & cards | 68/169 | 40.24% | 50.30% | 14.20% |
| model:kalyan-ettin | eligible | Documents & identifiers | 191/609 | 31.36% | 52.22% | 4.93% |
| model:kalyan-ettin | eligible | People's names | 40/228 | 17.54% | 76.32% | 17.98% |
| model:kalyan-ettin | eligible | Phone numbers & email | 233/390 | 59.74% | 86.41% | 44.36% |
| model:kalyan-ettin | eligible | Addresses & locations | 12/176 | 6.82% | 56.82% | 3.98% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 61/95 | 64.21% | 97.89% | 3.16% |
| model:mmbert32k | eligible | Bank accounts & cards | 102/169 | 60.36% | 73.96% | 34.91% |
| model:mmbert32k | eligible | Documents & identifiers | 451/609 | 74.06% | 98.03% | 35.80% |
| model:mmbert32k | eligible | People's names | 123/228 | 53.95% | 91.23% | 30.26% |
| model:mmbert32k | eligible | Phone numbers & email | 255/390 | 65.38% | 99.49% | 47.95% |
| model:mmbert32k | eligible | Addresses & locations | 38/176 | 21.59% | 98.30% | 5.68% |
| model:natasha | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Bank accounts & cards | 3/169 | 1.78% | 1.78% | 1.78% |
| model:natasha | eligible | Documents & identifiers | 8/609 | 1.31% | 1.31% | 1.31% |
| model:natasha | eligible | People's names | 125/228 | 54.82% | 62.28% | 43.42% |
| model:natasha | eligible | Phone numbers & email | 6/390 | 1.54% | 7.18% | 1.28% |
| model:natasha | eligible | Addresses & locations | 9/176 | 5.11% | 56.25% | 2.27% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 1/169 | 0.59% | 0.59% | 0.59% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 14/228 | 6.14% | 90.79% | 2.63% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 1/390 | 0.26% | 24.10% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 8/176 | 4.55% | 90.34% | 0.57% |
| model:ner-ru-gherman+homoglyph | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+homoglyph | eligible | Bank accounts & cards | 1/169 | 0.59% | 0.59% | 0.59% |
| model:ner-ru-gherman+homoglyph | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+homoglyph | eligible | People's names | 13/228 | 5.70% | 92.11% | 3.07% |
| model:ner-ru-gherman+homoglyph | eligible | Phone numbers & email | 1/390 | 0.26% | 25.13% | 0.00% |
| model:ner-ru-gherman+homoglyph | eligible | Addresses & locations | 8/176 | 4.55% | 93.75% | 1.70% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 39/95 | 41.05% | 52.63% | 4.21% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 28/169 | 16.57% | 23.08% | 14.20% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 42/609 | 6.90% | 12.15% | 3.28% |
| model:ner-ru-yqelz | eligible | People's names | 176/228 | 77.19% | 85.09% | 63.16% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 16/390 | 4.10% | 9.49% | 2.82% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 25/176 | 14.20% | 90.91% | 10.80% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 38/95 | 40.00% | 53.68% | 35.79% |
| model:nuner-zero | eligible | Bank accounts & cards | 87/169 | 51.48% | 63.31% | 50.30% |
| model:nuner-zero | eligible | Documents & identifiers | 411/609 | 67.49% | 82.27% | 57.64% |
| model:nuner-zero | eligible | People's names | 157/228 | 68.86% | 88.60% | 7.02% |
| model:nuner-zero | eligible | Phone numbers & email | 350/390 | 89.74% | 95.64% | 83.08% |
| model:nuner-zero | eligible | Addresses & locations | 78/176 | 44.32% | 97.16% | 3.98% |
| model:nym-base | eligible | Passwords, keys & tokens | 75/95 | 78.95% | 98.95% | 60.00% |
| model:nym-base | eligible | Bank accounts & cards | 152/169 | 89.94% | 94.08% | 81.66% |
| model:nym-base | eligible | Documents & identifiers | 565/609 | 92.78% | 98.85% | 81.12% |
| model:nym-base | eligible | People's names | 30/228 | 13.16% | 95.61% | 67.54% |
| model:nym-base | eligible | Phone numbers & email | 343/390 | 87.95% | 96.41% | 83.08% |
| model:nym-base | eligible | Addresses & locations | 27/176 | 15.34% | 97.16% | 20.45% |
| model:nym-base+homoglyph | eligible | Passwords, keys & tokens | 76/95 | 80.00% | 98.95% | 60.00% |
| model:nym-base+homoglyph | eligible | Bank accounts & cards | 152/169 | 89.94% | 94.08% | 82.25% |
| model:nym-base+homoglyph | eligible | Documents & identifiers | 565/609 | 92.78% | 98.85% | 81.12% |
| model:nym-base+homoglyph | eligible | People's names | 30/228 | 13.16% | 97.37% | 71.49% |
| model:nym-base+homoglyph | eligible | Phone numbers & email | 339/390 | 86.92% | 96.15% | 82.56% |
| model:nym-base+homoglyph | eligible | Addresses & locations | 27/176 | 15.34% | 97.16% | 21.59% |
| model:nym-small | eligible | Passwords, keys & tokens | 70/95 | 73.68% | 98.95% | 50.53% |
| model:nym-small | eligible | Bank accounts & cards | 120/169 | 71.01% | 86.98% | 63.31% |
| model:nym-small | eligible | Documents & identifiers | 452/609 | 74.22% | 95.73% | 66.83% |
| model:nym-small | eligible | People's names | 37/228 | 16.23% | 89.91% | 59.21% |
| model:nym-small | eligible | Phone numbers & email | 341/390 | 87.44% | 97.95% | 80.26% |
| model:nym-small | eligible | Addresses & locations | 28/176 | 15.91% | 98.86% | 18.18% |
| model:openai-base | eligible | Passwords, keys & tokens | 85/95 | 89.47% | 91.58% | 88.42% |
| model:openai-base | eligible | Bank accounts & cards | 78/169 | 46.15% | 47.34% | 43.79% |
| model:openai-base | eligible | Documents & identifiers | 426/609 | 69.95% | 77.67% | 67.32% |
| model:openai-base | eligible | People's names | 152/228 | 66.67% | 69.30% | 60.53% |
| model:openai-base | eligible | Phone numbers & email | 334/390 | 85.64% | 92.05% | 82.56% |
| model:openai-base | eligible | Addresses & locations | 69/176 | 39.20% | 76.70% | 45.45% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 80/95 | 84.21% | 93.68% | 27.37% |
| model:openmed-multilingual | eligible | Bank accounts & cards | 111/169 | 65.68% | 80.47% | 61.54% |
| model:openmed-multilingual | eligible | Documents & identifiers | 385/609 | 63.22% | 84.89% | 50.08% |
| model:openmed-multilingual | eligible | People's names | 13/228 | 5.70% | 64.91% | 22.81% |
| model:openmed-multilingual | eligible | Phone numbers & email | 297/390 | 76.15% | 94.36% | 68.72% |
| model:openmed-multilingual | eligible | Addresses & locations | 10/176 | 5.68% | 81.25% | 3.41% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 73/95 | 76.84% | 88.42% | 31.58% |
| model:openmed-nemotron | eligible | Bank accounts & cards | 65/169 | 38.46% | 44.38% | 20.12% |
| model:openmed-nemotron | eligible | Documents & identifiers | 154/609 | 25.29% | 40.39% | 7.72% |
| model:openmed-nemotron | eligible | People's names | 40/228 | 17.54% | 78.07% | 28.07% |
| model:openmed-nemotron | eligible | Phone numbers & email | 182/390 | 46.67% | 78.72% | 37.18% |
| model:openmed-nemotron | eligible | Addresses & locations | 21/176 | 11.93% | 85.80% | 10.80% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 89/95 | 93.68% | 95.79% | 90.53% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 95/169 | 56.21% | 59.17% | 50.89% |
| model:opf-kz-ru | eligible | Documents & identifiers | 526/609 | 86.37% | 96.72% | 84.73% |
| model:opf-kz-ru | eligible | People's names | 142/228 | 62.28% | 73.25% | 53.51% |
| model:opf-kz-ru | eligible | Phone numbers & email | 348/390 | 89.23% | 96.67% | 84.36% |
| model:opf-kz-ru | eligible | Addresses & locations | 21/176 | 11.93% | 72.16% | 9.66% |
| model:opf-ru | eligible | Passwords, keys & tokens | 89/95 | 93.68% | 96.84% | 78.95% |
| model:opf-ru | eligible | Bank accounts & cards | 83/169 | 49.11% | 69.23% | 43.79% |
| model:opf-ru | eligible | Documents & identifiers | 442/609 | 72.58% | 95.07% | 62.73% |
| model:opf-ru | eligible | People's names | 118/228 | 51.75% | 87.28% | 41.67% |
| model:opf-ru | eligible | Phone numbers & email | 312/390 | 80.00% | 96.15% | 75.13% |
| model:opf-ru | eligible | Addresses & locations | 15/176 | 8.52% | 90.34% | 2.27% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 90/95 | 94.74% | 95.79% | 87.37% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 81/169 | 47.93% | 62.13% | 40.24% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 453/609 | 74.38% | 96.22% | 69.62% |
| model:opf-ru-v2 | eligible | People's names | 149/228 | 65.35% | 75.88% | 53.95% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 312/390 | 80.00% | 91.28% | 75.64% |
| model:opf-ru-v2 | eligible | Addresses & locations | 53/176 | 30.11% | 81.25% | 32.95% |
| model:opf-ru-v2+homoglyph | eligible | Passwords, keys & tokens | 90/95 | 94.74% | 95.79% | 86.32% |
| model:opf-ru-v2+homoglyph | eligible | Bank accounts & cards | 84/169 | 49.70% | 63.31% | 41.42% |
| model:opf-ru-v2+homoglyph | eligible | Documents & identifiers | 454/609 | 74.55% | 96.06% | 69.29% |
| model:opf-ru-v2+homoglyph | eligible | People's names | 154/228 | 67.54% | 77.19% | 58.33% |
| model:opf-ru-v2+homoglyph | eligible | Phone numbers & email | 310/390 | 79.49% | 91.03% | 75.38% |
| model:opf-ru-v2+homoglyph | eligible | Addresses & locations | 53/176 | 30.11% | 78.41% | 32.39% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 92/95 | 96.84% | 97.89% | 91.58% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 98/169 | 57.99% | 66.86% | 44.38% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 476/609 | 78.16% | 85.71% | 62.40% |
| model:pii-shield-onnx | eligible | People's names | 123/228 | 53.95% | 89.47% | 56.14% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 377/390 | 96.67% | 98.72% | 93.59% |
| model:pii-shield-onnx | eligible | Addresses & locations | 23/176 | 13.07% | 84.09% | 10.23% |
| model:pplx | eligible | Passwords, keys & tokens | 92/95 | 96.84% | 97.89% | 86.32% |
| model:pplx | eligible | Bank accounts & cards | 127/169 | 75.15% | 75.74% | 73.37% |
| model:pplx | eligible | Documents & identifiers | 590/609 | 96.88% | 99.84% | 94.25% |
| model:pplx | eligible | People's names | 203/228 | 89.04% | 96.05% | 80.26% |
| model:pplx | eligible | Phone numbers & email | 384/390 | 98.46% | 99.49% | 97.18% |
| model:pplx | eligible | Addresses & locations | 166/176 | 94.32% | 98.30% | 91.48% |
| model:pplx+homoglyph | eligible | Passwords, keys & tokens | 92/95 | 96.84% | 97.89% | 87.37% |
| model:pplx+homoglyph | eligible | Bank accounts & cards | 128/169 | 75.74% | 76.33% | 73.96% |
| model:pplx+homoglyph | eligible | Documents & identifiers | 590/609 | 96.88% | 99.84% | 94.25% |
| model:pplx+homoglyph | eligible | People's names | 203/228 | 89.04% | 95.61% | 78.95% |
| model:pplx+homoglyph | eligible | Phone numbers & email | 383/390 | 98.21% | 99.49% | 97.18% |
| model:pplx+homoglyph | eligible | Addresses & locations | 168/176 | 95.45% | 98.30% | 92.05% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 70/95 | 73.68% | 95.79% | 8.42% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 91/169 | 53.85% | 57.99% | 44.97% |
| model:ru-legal-ner | eligible | Documents & identifiers | 527/609 | 86.54% | 92.94% | 71.43% |
| model:ru-legal-ner | eligible | People's names | 192/228 | 84.21% | 93.42% | 65.35% |
| model:ru-legal-ner | eligible | Phone numbers & email | 238/390 | 61.03% | 90.77% | 52.56% |
| model:ru-legal-ner | eligible | Addresses & locations | 30/176 | 17.05% | 87.50% | 13.07% |
| model:ru-legal-ner+homoglyph | eligible | Passwords, keys & tokens | 70/95 | 73.68% | 95.79% | 8.42% |
| model:ru-legal-ner+homoglyph | eligible | Bank accounts & cards | 92/169 | 54.44% | 58.58% | 45.56% |
| model:ru-legal-ner+homoglyph | eligible | Documents & identifiers | 529/609 | 86.86% | 92.78% | 71.92% |
| model:ru-legal-ner+homoglyph | eligible | People's names | 193/228 | 84.65% | 92.98% | 69.74% |
| model:ru-legal-ner+homoglyph | eligible | Phone numbers & email | 237/390 | 60.77% | 91.03% | 52.56% |
| model:ru-legal-ner+homoglyph | eligible | Addresses & locations | 23/176 | 13.07% | 85.23% | 10.23% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 23/95 | 24.21% | 26.32% | 20.00% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 138/169 | 81.66% | 84.62% | 78.70% |
| model:ru-pii-ner | eligible | Documents & identifiers | 504/609 | 82.76% | 89.49% | 79.97% |
| model:ru-pii-ner | eligible | People's names | 217/228 | 95.18% | 99.56% | 90.79% |
| model:ru-pii-ner | eligible | Phone numbers & email | 384/390 | 98.46% | 98.72% | 96.15% |
| model:ru-pii-ner | eligible | Addresses & locations | 123/176 | 69.89% | 88.64% | 68.18% |
| model:rules-ru | eligible | Passwords, keys & tokens | 11/95 | 11.58% | 13.68% | 11.58% |
| model:rules-ru | eligible | Bank accounts & cards | 57/169 | 33.73% | 35.50% | 30.77% |
| model:rules-ru | eligible | Documents & identifiers | 361/609 | 59.28% | 59.44% | 55.83% |
| model:rules-ru | eligible | People's names | 0/228 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 264/390 | 67.69% | 84.10% | 67.18% |
| model:rules-ru | eligible | Addresses & locations | 0/176 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/95 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 1/169 | 0.59% | 0.59% | 0.59% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/609 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 51/228 | 22.37% | 44.74% | 22.37% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/390 | 0.00% | 0.51% | 0.00% |
| model:spacy-alrosait | eligible | Addresses & locations | 61/176 | 34.66% | 57.95% | 34.66% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 6/95 | 6.32% | 6.32% | 6.32% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 9/169 | 5.33% | 5.33% | 5.33% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 23/609 | 3.78% | 3.78% | 3.78% |
| model:spacy-ru-lg | eligible | People's names | 133/228 | 58.33% | 67.54% | 58.33% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 27/390 | 6.92% | 6.92% | 6.92% |
| model:spacy-ru-lg | eligible | Addresses & locations | 9/176 | 5.11% | 75.57% | 5.11% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 15/95 | 15.79% | 33.68% | 13.68% |
| model:stanza-ru | eligible | Bank accounts & cards | 16/169 | 9.47% | 9.47% | 9.47% |
| model:stanza-ru | eligible | Documents & identifiers | 76/609 | 12.48% | 13.46% | 12.48% |
| model:stanza-ru | eligible | People's names | 204/228 | 89.47% | 91.67% | 89.47% |
| model:stanza-ru | eligible | Phone numbers & email | 31/390 | 7.95% | 12.31% | 7.18% |
| model:stanza-ru | eligible | Addresses & locations | 13/176 | 7.39% | 90.34% | 7.39% |
| model:traciora | eligible | Passwords, keys & tokens | 88/95 | 92.63% | 95.79% | 74.74% |
| model:traciora | eligible | Bank accounts & cards | 80/169 | 47.34% | 57.40% | 34.91% |
| model:traciora | eligible | Documents & identifiers | 450/609 | 73.89% | 92.12% | 55.01% |
| model:traciora | eligible | People's names | 173/228 | 75.88% | 87.72% | 68.42% |
| model:traciora | eligible | Phone numbers & email | 344/390 | 88.21% | 96.15% | 80.00% |
| model:traciora | eligible | Addresses & locations | 102/176 | 57.95% | 91.48% | 53.98% |
