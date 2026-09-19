# privy: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/privy.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 29/30 | 96.67% | 96.67% | 96.67% |
| composition:fastino | eligible | Bank accounts & cards | 120/122 | 98.36% | 98.36% | 98.36% |
| composition:fastino | eligible | Documents & identifiers | 217/276 | 78.62% | 78.62% | 78.62% |
| composition:fastino | eligible | People's names | 400/428 | 93.46% | 93.93% | 92.99% |
| composition:fastino | eligible | Phone numbers & email | 85/87 | 97.70% | 97.70% | 97.70% |
| composition:fastino | eligible | Addresses & locations | 467/699 | 66.81% | 72.53% | 65.95% |
| composition:fastino | eligible | Organizations | 69/79 | 87.34% | 93.67% | 86.08% |
| composition:fastino | eligible | Network identifiers | 84/178 | 47.19% | 47.19% | 47.19% |
| composition:pplx | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Documents & identifiers | 273/276 | 98.91% | 99.64% | 98.91% |
| composition:pplx | eligible | People's names | 422/428 | 98.60% | 98.60% | 97.43% |
| composition:pplx | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Addresses & locations | 651/699 | 93.13% | 95.57% | 92.56% |
| composition:pplx | eligible | Organizations | 13/79 | 16.46% | 30.38% | 16.46% |
| composition:pplx | eligible | Network identifiers | 146/178 | 82.02% | 98.31% | 82.02% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Documents & identifiers | 273/276 | 98.91% | 99.64% | 98.91% |
| composition:pplx+fastino | eligible | People's names | 427/428 | 99.77% | 99.77% | 99.30% |
| composition:pplx+fastino | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Addresses & locations | 684/699 | 97.85% | 98.43% | 97.00% |
| composition:pplx+fastino | eligible | Organizations | 73/79 | 92.41% | 96.20% | 91.14% |
| composition:pplx+fastino | eligible | Network identifiers | 148/178 | 83.15% | 98.88% | 83.15% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 273/276 | 98.91% | 99.64% | 98.91% |
| composition:pplx+fastino+bardsai | eligible | People's names | 427/428 | 99.77% | 99.77% | 99.30% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 685/699 | 98.00% | 98.43% | 97.00% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 75/79 | 94.94% | 97.47% | 92.41% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 148/178 | 83.15% | 98.88% | 83.15% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 273/276 | 98.91% | 100.00% | 98.91% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 427/428 | 99.77% | 99.77% | 99.30% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 689/699 | 98.57% | 99.00% | 97.57% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 77/79 | 97.47% | 100.00% | 96.20% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 165/178 | 92.70% | 98.88% | 92.70% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 273/276 | 98.91% | 100.00% | 98.91% |
| composition:pplx+fastino+mmbert | eligible | People's names | 427/428 | 99.77% | 99.77% | 99.30% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 688/699 | 98.43% | 99.00% | 97.57% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 76/79 | 96.20% | 100.00% | 94.94% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 165/178 | 92.70% | 98.88% | 92.70% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Bank accounts & cards | 120/122 | 98.36% | 98.36% | 98.36% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 260/276 | 94.20% | 96.74% | 89.49% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 415/428 | 96.96% | 97.66% | 96.26% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 475/699 | 67.95% | 77.54% | 66.81% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 20/79 | 25.32% | 40.51% | 26.58% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 131/178 | 73.60% | 90.45% | 69.10% |
| model:apararti | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 96.67% |
| model:apararti | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| model:apararti | eligible | Documents & identifiers | 258/276 | 93.48% | 95.65% | 92.39% |
| model:apararti | eligible | People's names | 381/428 | 89.02% | 90.19% | 87.15% |
| model:apararti | eligible | Phone numbers & email | 84/87 | 96.55% | 97.70% | 96.55% |
| model:apararti | eligible | Addresses & locations | 322/699 | 46.07% | 56.08% | 43.92% |
| model:apararti | eligible | Organizations | 19/79 | 24.05% | 39.24% | 26.58% |
| model:apararti | eligible | Network identifiers | 99/178 | 55.62% | 70.22% | 51.69% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 18/30 | 60.00% | 60.00% | 40.00% |
| model:bardsai-eu | eligible | Bank accounts & cards | 72/122 | 59.02% | 59.02% | 13.11% |
| model:bardsai-eu | eligible | Documents & identifiers | 84/276 | 30.43% | 39.49% | 16.67% |
| model:bardsai-eu | eligible | People's names | 199/428 | 46.50% | 47.90% | 39.72% |
| model:bardsai-eu | eligible | Phone numbers & email | 26/87 | 29.89% | 71.26% | 29.89% |
| model:bardsai-eu | eligible | Addresses & locations | 187/699 | 26.75% | 42.06% | 23.61% |
| model:bardsai-eu | eligible | Organizations | 45/79 | 56.96% | 69.62% | 51.90% |
| model:bardsai-eu | eligible | Network identifiers | 34/178 | 19.10% | 63.48% | 17.42% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/30 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Bank accounts & cards | 0/122 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 0/276 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | People's names | 340/428 | 79.44% | 81.31% | 77.80% |
| model:davlan-mbert | eligible | Phone numbers & email | 3/87 | 3.45% | 27.59% | 2.30% |
| model:davlan-mbert | eligible | Addresses & locations | 173/699 | 24.75% | 43.92% | 23.46% |
| model:davlan-mbert | eligible | Organizations | 56/79 | 70.89% | 84.81% | 70.89% |
| model:davlan-mbert | eligible | Network identifiers | 3/178 | 1.69% | 3.37% | 1.12% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/30 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 0/122 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 0/276 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 280/428 | 65.42% | 67.29% | 55.61% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/87 | 0.00% | 13.79% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 156/699 | 22.32% | 41.63% | 20.46% |
| model:davlan-xlmr | eligible | Organizations | 64/79 | 81.01% | 92.41% | 79.75% |
| model:davlan-xlmr | eligible | Network identifiers | 3/178 | 1.69% | 6.74% | 1.12% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 20/30 | 66.67% | 66.67% | 60.00% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 1/122 | 0.82% | 0.82% | 0.82% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 1/276 | 0.36% | 0.36% | 0.00% |
| model:fef2-secret-ru | eligible | People's names | 52/428 | 12.15% | 13.08% | 10.28% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 33/87 | 37.93% | 41.38% | 36.78% |
| model:fef2-secret-ru | eligible | Addresses & locations | 6/699 | 0.86% | 1.57% | 0.86% |
| model:fef2-secret-ru | eligible | Organizations | 9/79 | 11.39% | 21.52% | 11.39% |
| model:fef2-secret-ru | eligible | Network identifiers | 0/178 | 0.00% | 0.56% | 0.00% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 9/30 | 30.00% | 30.00% | 30.00% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 15/122 | 12.30% | 12.30% | 12.30% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 26/276 | 9.42% | 9.78% | 9.42% |
| model:gliner-multi-v21 | eligible | People's names | 379/428 | 88.55% | 88.79% | 88.32% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 10/87 | 11.49% | 60.92% | 11.49% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 215/699 | 30.76% | 34.76% | 30.47% |
| model:gliner-multi-v21 | eligible | Organizations | 67/79 | 84.81% | 91.14% | 84.81% |
| model:gliner-multi-v21 | eligible | Network identifiers | 24/178 | 13.48% | 15.73% | 13.48% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| model:gliner-nvidia | eligible | Bank accounts & cards | 113/122 | 92.62% | 92.62% | 92.62% |
| model:gliner-nvidia | eligible | Documents & identifiers | 212/276 | 76.81% | 77.17% | 76.81% |
| model:gliner-nvidia | eligible | People's names | 388/428 | 90.65% | 95.56% | 81.54% |
| model:gliner-nvidia | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| model:gliner-nvidia | eligible | Addresses & locations | 443/699 | 63.38% | 70.39% | 62.66% |
| model:gliner-nvidia | eligible | Organizations | 73/79 | 92.41% | 94.94% | 92.41% |
| model:gliner-nvidia | eligible | Network identifiers | 150/178 | 84.27% | 84.27% | 84.27% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 25/30 | 83.33% | 83.33% | 83.33% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 103/122 | 84.43% | 84.43% | 84.43% |
| model:gliner-pii-base | eligible | Documents & identifiers | 149/276 | 53.99% | 53.99% | 53.99% |
| model:gliner-pii-base | eligible | People's names | 277/428 | 64.72% | 65.42% | 64.25% |
| model:gliner-pii-base | eligible | Phone numbers & email | 85/87 | 97.70% | 97.70% | 97.70% |
| model:gliner-pii-base | eligible | Addresses & locations | 268/699 | 38.34% | 39.06% | 38.05% |
| model:gliner-pii-base | eligible | Organizations | 62/79 | 78.48% | 86.08% | 78.48% |
| model:gliner-pii-base | eligible | Network identifiers | 124/178 | 69.66% | 69.66% | 69.66% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 27/30 | 90.00% | 90.00% | 90.00% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 94/122 | 77.05% | 77.05% | 77.05% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 118/276 | 42.75% | 43.12% | 42.75% |
| model:gliner-pii-edge | eligible | People's names | 209/428 | 48.83% | 49.53% | 48.83% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 56/87 | 64.37% | 65.52% | 64.37% |
| model:gliner-pii-edge | eligible | Addresses & locations | 264/699 | 37.77% | 41.77% | 37.48% |
| model:gliner-pii-edge | eligible | Organizations | 49/79 | 62.03% | 73.42% | 62.03% |
| model:gliner-pii-edge | eligible | Network identifiers | 105/178 | 58.99% | 74.16% | 58.99% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 28/30 | 93.33% | 93.33% | 93.33% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 79/122 | 64.75% | 64.75% | 64.75% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 196/276 | 71.01% | 73.55% | 71.01% |
| model:gliner-stream-pii | eligible | People's names | 259/428 | 60.51% | 61.21% | 60.51% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 78/87 | 89.66% | 89.66% | 89.66% |
| model:gliner-stream-pii | eligible | Addresses & locations | 446/699 | 63.81% | 66.38% | 63.52% |
| model:gliner-stream-pii | eligible | Organizations | 70/79 | 88.61% | 93.67% | 88.61% |
| model:gliner-stream-pii | eligible | Network identifiers | 100/178 | 56.18% | 58.43% | 56.18% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 29/30 | 96.67% | 96.67% | 96.67% |
| model:gliner-urchade | eligible | Bank accounts & cards | 80/122 | 65.57% | 65.57% | 65.57% |
| model:gliner-urchade | eligible | Documents & identifiers | 128/276 | 46.38% | 46.38% | 46.38% |
| model:gliner-urchade | eligible | People's names | 372/428 | 86.92% | 87.15% | 86.68% |
| model:gliner-urchade | eligible | Phone numbers & email | 78/87 | 89.66% | 90.80% | 89.66% |
| model:gliner-urchade | eligible | Addresses & locations | 220/699 | 31.47% | 32.05% | 31.47% |
| model:gliner-urchade | eligible | Organizations | 73/79 | 92.41% | 96.20% | 91.14% |
| model:gliner-urchade | eligible | Network identifiers | 146/178 | 82.02% | 89.33% | 82.02% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 29/30 | 96.67% | 96.67% | 96.67% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 120/122 | 98.36% | 98.36% | 98.36% |
| model:gliner2-fastino | eligible | Documents & identifiers | 217/276 | 78.62% | 78.62% | 78.62% |
| model:gliner2-fastino | eligible | People's names | 400/428 | 93.46% | 93.93% | 92.99% |
| model:gliner2-fastino | eligible | Phone numbers & email | 85/87 | 97.70% | 97.70% | 97.70% |
| model:gliner2-fastino | eligible | Addresses & locations | 467/699 | 66.81% | 72.53% | 65.95% |
| model:gliner2-fastino | eligible | Organizations | 69/79 | 87.34% | 93.67% | 86.08% |
| model:gliner2-fastino | eligible | Network identifiers | 84/178 | 47.19% | 47.19% | 47.19% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 28/30 | 93.33% | 93.33% | 93.33% |
| model:gliner2-hivetrace-omni | eligible | Bank accounts & cards | 112/122 | 91.80% | 91.80% | 91.80% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 206/276 | 74.64% | 75.36% | 74.64% |
| model:gliner2-hivetrace-omni | eligible | People's names | 413/428 | 96.50% | 96.73% | 96.26% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 84/87 | 96.55% | 96.55% | 96.55% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 395/699 | 56.51% | 60.23% | 56.22% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 74/79 | 93.67% | 94.94% | 92.41% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 93/178 | 52.25% | 52.25% | 52.25% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 19/30 | 63.33% | 63.33% | 63.33% |
| model:gliner2-hivetrace-uni | eligible | Bank accounts & cards | 114/122 | 93.44% | 93.44% | 93.44% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 242/276 | 87.68% | 87.68% | 87.68% |
| model:gliner2-hivetrace-uni | eligible | People's names | 381/428 | 89.02% | 89.25% | 89.02% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 85/87 | 97.70% | 97.70% | 97.70% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 144/699 | 20.60% | 25.75% | 20.60% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 26/79 | 32.91% | 34.18% | 32.91% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 68/178 | 38.20% | 38.20% | 38.20% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 29/30 | 96.67% | 96.67% | 96.67% |
| model:gliner2-large | eligible | Bank accounts & cards | 110/122 | 90.16% | 90.16% | 90.16% |
| model:gliner2-large | eligible | Documents & identifiers | 165/276 | 59.78% | 60.51% | 59.78% |
| model:gliner2-large | eligible | People's names | 404/428 | 94.39% | 95.09% | 94.39% |
| model:gliner2-large | eligible | Phone numbers & email | 85/87 | 97.70% | 97.70% | 97.70% |
| model:gliner2-large | eligible | Addresses & locations | 259/699 | 37.05% | 46.92% | 36.77% |
| model:gliner2-large | eligible | Organizations | 62/79 | 78.48% | 82.28% | 78.48% |
| model:gliner2-large | eligible | Network identifiers | 112/178 | 62.92% | 62.92% | 62.92% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 27/30 | 90.00% | 90.00% | 90.00% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 39/122 | 31.97% | 31.97% | 31.97% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 141/276 | 51.09% | 51.09% | 51.09% |
| model:gliner2-vladlinv | eligible | People's names | 349/428 | 81.54% | 83.18% | 81.54% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 61/87 | 70.11% | 70.11% | 70.11% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 9/699 | 1.29% | 1.57% | 1.29% |
| model:gliner2-vladlinv | eligible | Organizations | 0/79 | 0.00% | 0.00% | 0.00% |
| model:gliner2-vladlinv | eligible | Network identifiers | 7/178 | 3.93% | 3.93% | 3.93% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 24/30 | 80.00% | 80.00% | 80.00% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 49/122 | 40.16% | 40.16% | 40.16% |
| model:gliner25-fastino | eligible | Documents & identifiers | 46/276 | 16.67% | 16.67% | 16.67% |
| model:gliner25-fastino | eligible | People's names | 402/428 | 93.93% | 94.16% | 93.69% |
| model:gliner25-fastino | eligible | Phone numbers & email | 84/87 | 96.55% | 96.55% | 96.55% |
| model:gliner25-fastino | eligible | Addresses & locations | 400/699 | 57.22% | 61.66% | 56.94% |
| model:gliner25-fastino | eligible | Organizations | 62/79 | 78.48% | 82.28% | 77.22% |
| model:gliner25-fastino | eligible | Network identifiers | 95/178 | 53.37% | 53.37% | 53.37% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| model:gravitee-small | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| model:gravitee-small | eligible | Documents & identifiers | 275/276 | 99.64% | 100.00% | 99.28% |
| model:gravitee-small | eligible | People's names | 424/428 | 99.07% | 99.30% | 98.83% |
| model:gravitee-small | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| model:gravitee-small | eligible | Addresses & locations | 690/699 | 98.71% | 99.28% | 97.28% |
| model:gravitee-small | eligible | Organizations | 78/79 | 98.73% | 100.00% | 97.47% |
| model:gravitee-small | eligible | Network identifiers | 178/178 | 100.00% | 100.00% | 100.00% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 96.67% |
| model:kalyan-ettin | eligible | Bank accounts & cards | 105/122 | 86.07% | 86.07% | 48.36% |
| model:kalyan-ettin | eligible | Documents & identifiers | 153/276 | 55.43% | 68.12% | 34.42% |
| model:kalyan-ettin | eligible | People's names | 265/428 | 61.92% | 87.38% | 72.90% |
| model:kalyan-ettin | eligible | Phone numbers & email | 83/87 | 95.40% | 100.00% | 87.36% |
| model:kalyan-ettin | eligible | Addresses & locations | 348/699 | 49.79% | 69.96% | 46.35% |
| model:kalyan-ettin | eligible | Organizations | 4/79 | 5.06% | 40.51% | 3.80% |
| model:kalyan-ettin | eligible | Network identifiers | 65/178 | 36.52% | 63.48% | 35.39% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 14/30 | 46.67% | 46.67% | 13.33% |
| model:mmbert32k | eligible | Bank accounts & cards | 121/122 | 99.18% | 99.18% | 37.70% |
| model:mmbert32k | eligible | Documents & identifiers | 202/276 | 73.19% | 90.58% | 16.67% |
| model:mmbert32k | eligible | People's names | 285/428 | 66.59% | 67.99% | 66.12% |
| model:mmbert32k | eligible | Phone numbers & email | 85/87 | 97.70% | 98.85% | 82.76% |
| model:mmbert32k | eligible | Addresses & locations | 332/699 | 47.50% | 69.38% | 28.61% |
| model:mmbert32k | eligible | Organizations | 16/79 | 20.25% | 73.42% | 29.11% |
| model:mmbert32k | eligible | Network identifiers | 92/178 | 51.69% | 94.94% | 29.21% |
| model:natasha | eligible | Passwords, keys & tokens | 0/30 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Bank accounts & cards | 0/122 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 5/276 | 1.81% | 1.81% | 1.81% |
| model:natasha | eligible | People's names | 58/428 | 13.55% | 13.79% | 13.55% |
| model:natasha | eligible | Phone numbers & email | 0/87 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Addresses & locations | 71/699 | 10.16% | 10.87% | 10.01% |
| model:natasha | eligible | Organizations | 33/79 | 41.77% | 46.84% | 41.77% |
| model:natasha | eligible | Network identifiers | 1/178 | 0.56% | 0.56% | 0.56% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/30 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 0/122 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/276 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 242/428 | 56.54% | 85.28% | 56.31% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/87 | 0.00% | 25.29% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 149/699 | 21.32% | 36.34% | 20.89% |
| model:ner-ru-gherman | eligible | Organizations | 0/79 | 0.00% | 18.99% | 0.00% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/178 | 0.00% | 0.56% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 1/30 | 3.33% | 3.33% | 0.00% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 14/122 | 11.48% | 11.48% | 0.00% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 10/276 | 3.62% | 6.52% | 0.36% |
| model:ner-ru-yqelz | eligible | People's names | 163/428 | 38.08% | 40.65% | 32.71% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 1/87 | 1.15% | 20.69% | 1.15% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 205/699 | 29.33% | 48.21% | 24.75% |
| model:ner-ru-yqelz | eligible | Organizations | 51/79 | 64.56% | 89.87% | 53.16% |
| model:ner-ru-yqelz | eligible | Network identifiers | 1/178 | 0.56% | 11.24% | 0.00% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| model:nuner-zero | eligible | Bank accounts & cards | 97/122 | 79.51% | 79.51% | 79.51% |
| model:nuner-zero | eligible | Documents & identifiers | 155/276 | 56.16% | 57.61% | 50.00% |
| model:nuner-zero | eligible | People's names | 382/428 | 89.25% | 89.49% | 58.64% |
| model:nuner-zero | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| model:nuner-zero | eligible | Addresses & locations | 483/699 | 69.10% | 76.25% | 38.05% |
| model:nuner-zero | eligible | Organizations | 68/79 | 86.08% | 89.87% | 2.53% |
| model:nuner-zero | eligible | Network identifiers | 154/178 | 86.52% | 89.33% | 79.78% |
| model:nym-base | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| model:nym-base | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| model:nym-base | eligible | Documents & identifiers | 271/276 | 98.19% | 100.00% | 96.38% |
| model:nym-base | eligible | People's names | 297/428 | 69.39% | 99.30% | 99.07% |
| model:nym-base | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| model:nym-base | eligible | Addresses & locations | 543/699 | 77.68% | 91.27% | 75.39% |
| model:nym-base | eligible | Organizations | 73/79 | 92.41% | 97.47% | 93.67% |
| model:nym-base | eligible | Network identifiers | 160/178 | 89.89% | 98.31% | 90.45% |
| model:nym-small | eligible | Passwords, keys & tokens | 27/30 | 90.00% | 90.00% | 80.00% |
| model:nym-small | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| model:nym-small | eligible | Documents & identifiers | 275/276 | 99.64% | 100.00% | 94.93% |
| model:nym-small | eligible | People's names | 310/428 | 72.43% | 99.07% | 97.90% |
| model:nym-small | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| model:nym-small | eligible | Addresses & locations | 464/699 | 66.38% | 84.69% | 62.80% |
| model:nym-small | eligible | Organizations | 65/79 | 82.28% | 96.20% | 86.08% |
| model:nym-small | eligible | Network identifiers | 152/178 | 85.39% | 93.82% | 77.53% |
| model:openai-base | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 93.33% |
| model:openai-base | eligible | Bank accounts & cards | 112/122 | 91.80% | 91.80% | 87.70% |
| model:openai-base | eligible | Documents & identifiers | 240/276 | 86.96% | 89.13% | 85.51% |
| model:openai-base | eligible | People's names | 371/428 | 86.68% | 87.62% | 85.51% |
| model:openai-base | eligible | Phone numbers & email | 83/87 | 95.40% | 96.55% | 95.40% |
| model:openai-base | eligible | Addresses & locations | 279/699 | 39.91% | 48.21% | 37.91% |
| model:openai-base | eligible | Organizations | 21/79 | 26.58% | 32.91% | 25.32% |
| model:openai-base | eligible | Network identifiers | 76/178 | 42.70% | 54.49% | 42.13% |
| model:openmed-multilingual | train | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 96.67% |
| model:openmed-multilingual | train | Bank accounts & cards | 87/122 | 71.31% | 71.31% | 71.31% |
| model:openmed-multilingual | train | Documents & identifiers | 222/276 | 80.43% | 80.80% | 79.35% |
| model:openmed-multilingual | train | People's names | 424/428 | 99.07% | 99.53% | 98.83% |
| model:openmed-multilingual | train | Phone numbers & email | 0/87 | 0.00% | 2.30% | 0.00% |
| model:openmed-multilingual | train | Addresses & locations | 684/699 | 97.85% | 99.00% | 97.00% |
| model:openmed-multilingual | train | Organizations | 75/79 | 94.94% | 98.73% | 96.20% |
| model:openmed-multilingual | train | Network identifiers | 40/178 | 22.47% | 22.47% | 20.79% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 26/30 | 86.67% | 86.67% | 33.33% |
| model:openmed-nemotron | eligible | Bank accounts & cards | 90/122 | 73.77% | 73.77% | 10.66% |
| model:openmed-nemotron | eligible | Documents & identifiers | 121/276 | 43.84% | 52.17% | 24.28% |
| model:openmed-nemotron | eligible | People's names | 181/428 | 42.29% | 70.79% | 57.01% |
| model:openmed-nemotron | eligible | Phone numbers & email | 82/87 | 94.25% | 100.00% | 87.36% |
| model:openmed-nemotron | eligible | Addresses & locations | 198/699 | 28.33% | 42.92% | 25.89% |
| model:openmed-nemotron | eligible | Organizations | 6/79 | 7.59% | 27.85% | 2.53% |
| model:openmed-nemotron | eligible | Network identifiers | 95/178 | 53.37% | 66.29% | 51.69% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 93.33% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| model:opf-kz-ru | eligible | Documents & identifiers | 262/276 | 94.93% | 97.10% | 93.84% |
| model:opf-kz-ru | eligible | People's names | 368/428 | 85.98% | 87.38% | 84.58% |
| model:opf-kz-ru | eligible | Phone numbers & email | 85/87 | 97.70% | 100.00% | 97.70% |
| model:opf-kz-ru | eligible | Addresses & locations | 308/699 | 44.06% | 55.94% | 41.92% |
| model:opf-kz-ru | eligible | Organizations | 15/79 | 18.99% | 27.85% | 18.99% |
| model:opf-kz-ru | eligible | Network identifiers | 111/178 | 62.36% | 74.16% | 58.99% |
| model:opf-ru | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| model:opf-ru | eligible | Bank accounts & cards | 121/122 | 99.18% | 99.18% | 95.08% |
| model:opf-ru | eligible | Documents & identifiers | 216/276 | 78.26% | 89.49% | 50.00% |
| model:opf-ru | eligible | People's names | 390/428 | 91.12% | 94.86% | 90.42% |
| model:opf-ru | eligible | Phone numbers & email | 83/87 | 95.40% | 97.70% | 95.40% |
| model:opf-ru | eligible | Addresses & locations | 254/699 | 36.34% | 56.37% | 31.90% |
| model:opf-ru | eligible | Organizations | 15/79 | 18.99% | 36.71% | 13.92% |
| model:opf-ru | eligible | Network identifiers | 28/178 | 15.73% | 60.11% | 11.80% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 96.67% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 118/122 | 96.72% | 96.72% | 75.41% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 201/276 | 72.83% | 83.70% | 55.43% |
| model:opf-ru-v2 | eligible | People's names | 291/428 | 67.99% | 68.69% | 66.36% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 82/87 | 94.25% | 98.85% | 89.66% |
| model:opf-ru-v2 | eligible | Addresses & locations | 186/699 | 26.61% | 40.49% | 23.32% |
| model:opf-ru-v2 | eligible | Organizations | 11/79 | 13.92% | 27.85% | 15.19% |
| model:opf-ru-v2 | eligible | Network identifiers | 52/178 | 29.21% | 47.19% | 24.16% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 26/30 | 86.67% | 86.67% | 70.00% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 114/122 | 93.44% | 93.44% | 72.13% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 203/276 | 73.55% | 77.17% | 66.30% |
| model:pii-shield-onnx | eligible | People's names | 266/428 | 62.15% | 64.49% | 56.07% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 81/87 | 93.10% | 98.85% | 77.01% |
| model:pii-shield-onnx | eligible | Addresses & locations | 367/699 | 52.50% | 63.09% | 48.93% |
| model:pii-shield-onnx | eligible | Organizations | 36/79 | 45.57% | 64.56% | 41.77% |
| model:pii-shield-onnx | eligible | Network identifiers | 121/178 | 67.98% | 91.57% | 66.29% |
| model:pplx | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Bank accounts & cards | 122/122 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Documents & identifiers | 273/276 | 98.91% | 99.64% | 98.91% |
| model:pplx | eligible | People's names | 422/428 | 98.60% | 98.60% | 97.43% |
| model:pplx | eligible | Phone numbers & email | 87/87 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Addresses & locations | 651/699 | 93.13% | 95.57% | 92.56% |
| model:pplx | eligible | Organizations | 13/79 | 16.46% | 30.38% | 16.46% |
| model:pplx | eligible | Network identifiers | 146/178 | 82.02% | 98.31% | 82.02% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 22/30 | 73.33% | 73.33% | 20.00% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 111/122 | 90.98% | 90.98% | 17.21% |
| model:ru-legal-ner | eligible | Documents & identifiers | 172/276 | 62.32% | 71.01% | 41.30% |
| model:ru-legal-ner | eligible | People's names | 112/428 | 26.17% | 31.78% | 20.33% |
| model:ru-legal-ner | eligible | Phone numbers & email | 60/87 | 68.97% | 97.70% | 59.77% |
| model:ru-legal-ner | eligible | Addresses & locations | 145/699 | 20.74% | 36.34% | 16.45% |
| model:ru-legal-ner | eligible | Organizations | 13/79 | 16.46% | 43.04% | 12.66% |
| model:ru-legal-ner | eligible | Network identifiers | 33/178 | 18.54% | 78.65% | 14.61% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 17/30 | 56.67% | 56.67% | 53.33% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 113/122 | 92.62% | 92.62% | 81.97% |
| model:ru-pii-ner | eligible | Documents & identifiers | 219/276 | 79.35% | 81.16% | 77.90% |
| model:ru-pii-ner | eligible | People's names | 311/428 | 72.66% | 74.30% | 72.66% |
| model:ru-pii-ner | eligible | Phone numbers & email | 75/87 | 86.21% | 89.66% | 85.06% |
| model:ru-pii-ner | eligible | Addresses & locations | 162/699 | 23.18% | 33.62% | 22.89% |
| model:ru-pii-ner | eligible | Organizations | 10/79 | 12.66% | 15.19% | 12.66% |
| model:ru-pii-ner | eligible | Network identifiers | 29/178 | 16.29% | 19.10% | 15.73% |
| model:rules-ru | eligible | Passwords, keys & tokens | 0/30 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Bank accounts & cards | 54/122 | 44.26% | 44.26% | 40.16% |
| model:rules-ru | eligible | Documents & identifiers | 33/276 | 11.96% | 11.96% | 11.96% |
| model:rules-ru | eligible | People's names | 0/428 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 43/87 | 49.43% | 49.43% | 49.43% |
| model:rules-ru | eligible | Addresses & locations | 0/699 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Organizations | 3/79 | 3.80% | 7.59% | 3.80% |
| model:rules-ru | eligible | Network identifiers | 156/178 | 87.64% | 87.64% | 87.64% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/30 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 0/122 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/276 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 0/428 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/87 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Addresses & locations | 0/699 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Organizations | 0/79 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Network identifiers | 0/178 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 0/30 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 0/122 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 4/276 | 1.45% | 1.45% | 1.45% |
| model:spacy-ru-lg | eligible | People's names | 24/428 | 5.61% | 5.84% | 5.61% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 2/87 | 2.30% | 2.30% | 2.30% |
| model:spacy-ru-lg | eligible | Addresses & locations | 19/699 | 2.72% | 5.01% | 2.43% |
| model:spacy-ru-lg | eligible | Organizations | 11/79 | 13.92% | 17.72% | 13.92% |
| model:spacy-ru-lg | eligible | Network identifiers | 1/178 | 0.56% | 0.56% | 0.56% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 3/30 | 10.00% | 10.00% | 10.00% |
| model:stanza-ru | eligible | Bank accounts & cards | 0/122 | 0.00% | 0.00% | 0.00% |
| model:stanza-ru | eligible | Documents & identifiers | 2/276 | 0.72% | 2.90% | 0.72% |
| model:stanza-ru | eligible | People's names | 125/428 | 29.21% | 32.24% | 28.97% |
| model:stanza-ru | eligible | Phone numbers & email | 2/87 | 2.30% | 2.30% | 2.30% |
| model:stanza-ru | eligible | Addresses & locations | 58/699 | 8.30% | 26.47% | 8.30% |
| model:stanza-ru | eligible | Organizations | 19/79 | 24.05% | 51.90% | 24.05% |
| model:stanza-ru | eligible | Network identifiers | 2/178 | 1.12% | 2.25% | 1.12% |
| model:traciora | eligible | Passwords, keys & tokens | 30/30 | 100.00% | 100.00% | 90.00% |
| model:traciora | eligible | Bank accounts & cards | 113/122 | 92.62% | 92.62% | 50.00% |
| model:traciora | eligible | Documents & identifiers | 117/276 | 42.39% | 60.87% | 22.46% |
| model:traciora | eligible | People's names | 389/428 | 90.89% | 91.82% | 88.79% |
| model:traciora | eligible | Phone numbers & email | 52/87 | 59.77% | 80.46% | 56.32% |
| model:traciora | eligible | Addresses & locations | 175/699 | 25.04% | 35.34% | 20.46% |
| model:traciora | eligible | Organizations | 23/79 | 29.11% | 37.97% | 27.85% |
| model:traciora | eligible | Network identifiers | 47/178 | 26.40% | 48.31% | 21.35% |
