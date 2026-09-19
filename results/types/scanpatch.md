# scanpatch: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/scanpatch.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Documents & identifiers | 496/655 | 75.73% | 80.00% | 75.73% |
| composition:fastino | eligible | People's names | 3469/3798 | 91.34% | 95.29% | 91.34% |
| composition:fastino | eligible | Phone numbers & email | 578/588 | 98.30% | 99.15% | 98.13% |
| composition:fastino | eligible | Addresses & locations | 1186/1637 | 72.45% | 88.58% | 71.41% |
| composition:fastino | eligible | Dates & times | 6/650 | 0.92% | 0.92% | 0.92% |
| composition:fastino | eligible | Organizations | 222/277 | 80.14% | 85.20% | 80.14% |
| composition:fastino | eligible | Network identifiers | 507/1103 | 45.97% | 59.11% | 45.87% |
| composition:pplx | eligible | Documents & identifiers | 565/655 | 86.26% | 92.06% | 86.26% |
| composition:pplx | eligible | People's names | 3763/3798 | 99.08% | 99.37% | 97.95% |
| composition:pplx | eligible | Phone numbers & email | 585/588 | 99.49% | 99.66% | 99.32% |
| composition:pplx | eligible | Addresses & locations | 1014/1637 | 61.94% | 67.75% | 61.51% |
| composition:pplx | eligible | Dates & times | 473/650 | 72.77% | 74.92% | 72.62% |
| composition:pplx | eligible | Organizations | 24/277 | 8.66% | 10.11% | 8.30% |
| composition:pplx | eligible | Network identifiers | 1025/1103 | 92.93% | 94.02% | 91.93% |
| composition:pplx+fastino | eligible | Documents & identifiers | 581/655 | 88.70% | 93.28% | 88.70% |
| composition:pplx+fastino | eligible | People's names | 3787/3798 | 99.71% | 99.87% | 99.34% |
| composition:pplx+fastino | eligible | Phone numbers & email | 585/588 | 99.49% | 99.66% | 99.32% |
| composition:pplx+fastino | eligible | Addresses & locations | 1434/1637 | 87.60% | 94.69% | 87.60% |
| composition:pplx+fastino | eligible | Dates & times | 474/650 | 72.92% | 75.08% | 72.77% |
| composition:pplx+fastino | eligible | Organizations | 231/277 | 83.39% | 88.45% | 83.39% |
| composition:pplx+fastino | eligible | Network identifiers | 1054/1103 | 95.56% | 98.01% | 95.38% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 602/655 | 91.91% | 95.42% | 91.30% |
| composition:pplx+fastino+bardsai | eligible | People's names | 3789/3798 | 99.76% | 99.92% | 99.55% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 585/588 | 99.49% | 99.66% | 99.32% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 1498/1637 | 91.51% | 98.41% | 91.26% |
| composition:pplx+fastino+bardsai | eligible | Dates & times | 474/650 | 72.92% | 75.08% | 72.77% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 247/277 | 89.17% | 93.50% | 88.81% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 1059/1103 | 96.01% | 98.19% | 95.83% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 611/655 | 93.28% | 96.64% | 92.06% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 3791/3798 | 99.82% | 99.95% | 99.68% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 585/588 | 99.49% | 99.66% | 99.32% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 1505/1637 | 91.94% | 99.08% | 91.51% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Dates & times | 561/650 | 86.31% | 96.00% | 81.54% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 251/277 | 90.61% | 96.03% | 88.81% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 1063/1103 | 96.37% | 99.64% | 96.10% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 590/655 | 90.08% | 96.03% | 89.01% |
| composition:pplx+fastino+mmbert | eligible | People's names | 3790/3798 | 99.79% | 99.92% | 99.55% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 585/588 | 99.49% | 99.66% | 99.32% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 1457/1637 | 89.00% | 97.25% | 88.15% |
| composition:pplx+fastino+mmbert | eligible | Dates & times | 561/650 | 86.31% | 96.00% | 81.54% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 237/277 | 85.56% | 93.14% | 84.12% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 1059/1103 | 96.01% | 99.64% | 95.74% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 512/655 | 78.17% | 87.94% | 76.95% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 3559/3798 | 93.71% | 97.81% | 92.52% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 567/588 | 96.43% | 98.81% | 95.58% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 890/1637 | 54.37% | 68.36% | 52.60% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Dates & times | 5/650 | 0.77% | 2.77% | 0.46% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 61/277 | 22.02% | 28.88% | 18.77% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 653/1103 | 59.20% | 81.87% | 55.85% |
| model:apararti | eligible | Documents & identifiers | 574/655 | 87.63% | 95.42% | 84.12% |
| model:apararti | eligible | People's names | 2900/3798 | 76.36% | 80.28% | 69.09% |
| model:apararti | eligible | Phone numbers & email | 570/588 | 96.94% | 99.15% | 95.75% |
| model:apararti | eligible | Addresses & locations | 975/1637 | 59.56% | 67.75% | 54.61% |
| model:apararti | eligible | Dates & times | 460/650 | 70.77% | 80.77% | 68.46% |
| model:apararti | eligible | Organizations | 82/277 | 29.60% | 37.91% | 19.49% |
| model:apararti | eligible | Network identifiers | 921/1103 | 83.50% | 97.01% | 78.79% |
| model:bardsai-eu | eligible | Documents & identifiers | 440/655 | 67.18% | 83.21% | 60.46% |
| model:bardsai-eu | eligible | People's names | 3733/3798 | 98.29% | 98.74% | 92.58% |
| model:bardsai-eu | eligible | Phone numbers & email | 355/588 | 60.37% | 95.75% | 54.59% |
| model:bardsai-eu | eligible | Addresses & locations | 1238/1637 | 75.63% | 91.39% | 72.57% |
| model:bardsai-eu | eligible | Dates & times | 17/650 | 2.62% | 3.08% | 2.62% |
| model:bardsai-eu | eligible | Organizations | 210/277 | 75.81% | 81.95% | 72.56% |
| model:bardsai-eu | eligible | Network identifiers | 327/1103 | 29.65% | 46.78% | 26.75% |
| model:betterleaks | eligible | Documents & identifiers | 0/655 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | People's names | 0/3798 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Phone numbers & email | 0/588 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Addresses & locations | 0/1637 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Organizations | 0/277 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Network identifiers | 0/1103 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 7/655 | 1.07% | 1.68% | 0.76% |
| model:davlan-mbert | eligible | People's names | 3699/3798 | 97.39% | 98.31% | 92.15% |
| model:davlan-mbert | eligible | Phone numbers & email | 2/588 | 0.34% | 1.87% | 0.17% |
| model:davlan-mbert | eligible | Addresses & locations | 957/1637 | 58.46% | 79.96% | 56.51% |
| model:davlan-mbert | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Organizations | 195/277 | 70.40% | 73.29% | 68.95% |
| model:davlan-mbert | eligible | Network identifiers | 0/1103 | 0.00% | 0.09% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 3/655 | 0.46% | 0.61% | 0.46% |
| model:davlan-xlmr | eligible | People's names | 3715/3798 | 97.81% | 98.42% | 93.18% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/588 | 0.00% | 8.16% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 1145/1637 | 69.95% | 86.26% | 67.26% |
| model:davlan-xlmr | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Organizations | 206/277 | 74.37% | 78.34% | 73.65% |
| model:davlan-xlmr | eligible | Network identifiers | 0/1103 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 300/655 | 45.80% | 57.56% | 44.12% |
| model:fef2-secret-ru | eligible | People's names | 3664/3798 | 96.47% | 97.87% | 93.47% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 228/588 | 38.78% | 43.88% | 38.10% |
| model:fef2-secret-ru | eligible | Addresses & locations | 772/1637 | 47.16% | 77.95% | 45.39% |
| model:fef2-secret-ru | eligible | Dates & times | 5/650 | 0.77% | 0.77% | 0.77% |
| model:fef2-secret-ru | eligible | Organizations | 209/277 | 75.45% | 80.51% | 73.65% |
| model:fef2-secret-ru | eligible | Network identifiers | 0/1103 | 0.00% | 0.09% | 0.00% |
| model:gitleaks | eligible | Documents & identifiers | 0/655 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | People's names | 0/3798 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Phone numbers & email | 0/588 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Addresses & locations | 0/1637 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Organizations | 0/277 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Network identifiers | 0/1103 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 113/655 | 17.25% | 17.56% | 17.25% |
| model:gliner-multi-v21 | eligible | People's names | 2852/3798 | 75.09% | 79.67% | 74.67% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 192/588 | 32.65% | 42.18% | 31.80% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 932/1637 | 56.93% | 70.86% | 56.87% |
| model:gliner-multi-v21 | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21 | eligible | Organizations | 195/277 | 70.40% | 75.81% | 70.40% |
| model:gliner-multi-v21 | eligible | Network identifiers | 379/1103 | 34.36% | 39.26% | 34.36% |
| model:gliner-multi-v21-ru | eligible | Documents & identifiers | 228/655 | 34.81% | 36.03% | 34.81% |
| model:gliner-multi-v21-ru | eligible | People's names | 2148/3798 | 56.56% | 58.24% | 56.53% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 126/588 | 21.43% | 28.40% | 20.92% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 979/1637 | 59.80% | 74.47% | 59.56% |
| model:gliner-multi-v21-ru | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21-ru | eligible | Organizations | 187/277 | 67.51% | 71.84% | 67.51% |
| model:gliner-multi-v21-ru | eligible | Network identifiers | 337/1103 | 30.55% | 34.72% | 30.55% |
| model:gliner-nvidia | eligible | Documents & identifiers | 450/655 | 68.70% | 69.92% | 68.70% |
| model:gliner-nvidia | eligible | People's names | 2325/3798 | 61.22% | 91.84% | 61.19% |
| model:gliner-nvidia | eligible | Phone numbers & email | 462/588 | 78.57% | 82.14% | 78.57% |
| model:gliner-nvidia | eligible | Addresses & locations | 975/1637 | 59.56% | 78.31% | 59.56% |
| model:gliner-nvidia | eligible | Dates & times | 4/650 | 0.62% | 0.77% | 0.62% |
| model:gliner-nvidia | eligible | Organizations | 209/277 | 75.45% | 81.95% | 75.45% |
| model:gliner-nvidia | eligible | Network identifiers | 565/1103 | 51.22% | 53.76% | 51.22% |
| model:gliner-nvidia-ru | eligible | Documents & identifiers | 487/655 | 74.35% | 76.64% | 74.35% |
| model:gliner-nvidia-ru | eligible | People's names | 1789/3798 | 47.10% | 75.36% | 47.08% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 439/588 | 74.66% | 78.40% | 74.66% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 954/1637 | 58.28% | 79.29% | 58.28% |
| model:gliner-nvidia-ru | eligible | Dates & times | 6/650 | 0.92% | 0.92% | 0.92% |
| model:gliner-nvidia-ru | eligible | Organizations | 185/277 | 66.79% | 72.20% | 66.79% |
| model:gliner-nvidia-ru | eligible | Network identifiers | 449/1103 | 40.71% | 42.61% | 40.71% |
| model:gliner-pii-base | eligible | Documents & identifiers | 172/655 | 26.26% | 27.48% | 26.26% |
| model:gliner-pii-base | eligible | People's names | 423/3798 | 11.14% | 14.74% | 11.14% |
| model:gliner-pii-base | eligible | Phone numbers & email | 473/588 | 80.44% | 81.63% | 80.44% |
| model:gliner-pii-base | eligible | Addresses & locations | 511/1637 | 31.22% | 52.66% | 29.87% |
| model:gliner-pii-base | eligible | Dates & times | 5/650 | 0.77% | 1.08% | 0.77% |
| model:gliner-pii-base | eligible | Organizations | 180/277 | 64.98% | 72.20% | 64.98% |
| model:gliner-pii-base | eligible | Network identifiers | 517/1103 | 46.87% | 48.78% | 46.87% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 411/655 | 62.75% | 76.64% | 62.29% |
| model:gliner-pii-edge | eligible | People's names | 2677/3798 | 70.48% | 77.80% | 69.43% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 509/588 | 86.56% | 88.95% | 86.56% |
| model:gliner-pii-edge | eligible | Addresses & locations | 651/1637 | 39.77% | 66.65% | 39.10% |
| model:gliner-pii-edge | eligible | Dates & times | 31/650 | 4.77% | 6.00% | 4.77% |
| model:gliner-pii-edge | eligible | Organizations | 202/277 | 72.92% | 77.26% | 72.92% |
| model:gliner-pii-edge | eligible | Network identifiers | 482/1103 | 43.70% | 48.69% | 43.52% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 112/655 | 17.10% | 29.16% | 17.10% |
| model:gliner-stream-pii | eligible | People's names | 1927/3798 | 50.74% | 56.42% | 49.47% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 273/588 | 46.43% | 58.84% | 46.43% |
| model:gliner-stream-pii | eligible | Addresses & locations | 590/1637 | 36.04% | 64.32% | 36.04% |
| model:gliner-stream-pii | eligible | Dates & times | 9/650 | 1.38% | 6.31% | 1.38% |
| model:gliner-stream-pii | eligible | Organizations | 124/277 | 44.77% | 50.90% | 44.77% |
| model:gliner-stream-pii | eligible | Network identifiers | 345/1103 | 31.28% | 52.58% | 31.28% |
| model:gliner-urchade | eligible | Documents & identifiers | 250/655 | 38.17% | 38.17% | 38.17% |
| model:gliner-urchade | eligible | People's names | 3050/3798 | 80.31% | 88.18% | 80.07% |
| model:gliner-urchade | eligible | Phone numbers & email | 510/588 | 86.73% | 88.27% | 86.73% |
| model:gliner-urchade | eligible | Addresses & locations | 1181/1637 | 72.14% | 83.63% | 72.08% |
| model:gliner-urchade | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade | eligible | Organizations | 250/277 | 90.25% | 92.42% | 90.25% |
| model:gliner-urchade | eligible | Network identifiers | 566/1103 | 51.31% | 52.22% | 51.31% |
| model:gliner-urchade-ru | eligible | Documents & identifiers | 499/655 | 76.18% | 78.32% | 76.18% |
| model:gliner-urchade-ru | eligible | People's names | 1035/3798 | 27.25% | 33.36% | 27.22% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 463/588 | 78.74% | 81.29% | 78.74% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 1201/1637 | 73.37% | 84.12% | 73.37% |
| model:gliner-urchade-ru | eligible | Dates & times | 15/650 | 2.31% | 2.31% | 2.31% |
| model:gliner-urchade-ru | eligible | Organizations | 250/277 | 90.25% | 92.06% | 90.25% |
| model:gliner-urchade-ru | eligible | Network identifiers | 630/1103 | 57.12% | 57.93% | 57.12% |
| model:gliner2-fastino | eligible | Documents & identifiers | 496/655 | 75.73% | 80.00% | 75.73% |
| model:gliner2-fastino | eligible | People's names | 3469/3798 | 91.34% | 95.29% | 91.34% |
| model:gliner2-fastino | eligible | Phone numbers & email | 578/588 | 98.30% | 99.15% | 98.13% |
| model:gliner2-fastino | eligible | Addresses & locations | 1186/1637 | 72.45% | 88.58% | 71.41% |
| model:gliner2-fastino | eligible | Dates & times | 6/650 | 0.92% | 0.92% | 0.92% |
| model:gliner2-fastino | eligible | Organizations | 222/277 | 80.14% | 85.20% | 80.14% |
| model:gliner2-fastino | eligible | Network identifiers | 507/1103 | 45.97% | 59.11% | 45.87% |
| model:gliner2-fastino-ru | eligible | Documents & identifiers | 543/655 | 82.90% | 87.48% | 82.90% |
| model:gliner2-fastino-ru | eligible | People's names | 2345/3798 | 61.74% | 67.48% | 61.61% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 580/588 | 98.64% | 99.32% | 98.47% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 1150/1637 | 70.25% | 86.74% | 69.58% |
| model:gliner2-fastino-ru | eligible | Dates & times | 10/650 | 1.54% | 1.54% | 1.54% |
| model:gliner2-fastino-ru | eligible | Organizations | 217/277 | 78.34% | 82.67% | 78.34% |
| model:gliner2-fastino-ru | eligible | Network identifiers | 510/1103 | 46.24% | 59.47% | 46.15% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 351/655 | 53.59% | 55.11% | 53.59% |
| model:gliner2-hivetrace-omni | eligible | People's names | 2662/3798 | 70.09% | 75.41% | 70.09% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 575/588 | 97.79% | 98.30% | 97.62% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 896/1637 | 54.73% | 79.29% | 54.73% |
| model:gliner2-hivetrace-omni | eligible | Dates & times | 5/650 | 0.77% | 0.92% | 0.77% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 210/277 | 75.81% | 81.23% | 75.81% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 448/1103 | 40.62% | 43.06% | 40.62% |
| model:gliner2-hivetrace-omni-ru | eligible | Documents & identifiers | 526/655 | 80.31% | 83.05% | 80.31% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 2095/3798 | 55.16% | 60.69% | 55.16% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 572/588 | 97.28% | 97.79% | 97.11% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 853/1637 | 52.11% | 78.44% | 52.05% |
| model:gliner2-hivetrace-omni-ru | eligible | Dates & times | 10/650 | 1.54% | 1.85% | 1.54% |
| model:gliner2-hivetrace-omni-ru | eligible | Organizations | 206/277 | 74.37% | 79.06% | 74.37% |
| model:gliner2-hivetrace-omni-ru | eligible | Network identifiers | 448/1103 | 40.62% | 43.79% | 40.62% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 440/655 | 67.18% | 71.45% | 67.18% |
| model:gliner2-hivetrace-uni | eligible | People's names | 2624/3798 | 69.09% | 70.77% | 69.06% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 529/588 | 89.97% | 90.65% | 89.80% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 826/1637 | 50.46% | 67.87% | 50.46% |
| model:gliner2-hivetrace-uni | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 153/277 | 55.23% | 58.84% | 55.23% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 144/1103 | 13.06% | 13.33% | 13.06% |
| model:gliner2-hivetrace-uni-ru | eligible | Documents & identifiers | 317/655 | 48.40% | 51.30% | 48.40% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 782/3798 | 20.59% | 21.04% | 20.56% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 117/588 | 19.90% | 19.90% | 19.73% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 350/1637 | 21.38% | 26.82% | 21.38% |
| model:gliner2-hivetrace-uni-ru | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:gliner2-hivetrace-uni-ru | eligible | Organizations | 92/277 | 33.21% | 36.10% | 33.21% |
| model:gliner2-hivetrace-uni-ru | eligible | Network identifiers | 4/1103 | 0.36% | 0.54% | 0.36% |
| model:gliner2-large | eligible | Documents & identifiers | 385/655 | 58.78% | 60.92% | 58.78% |
| model:gliner2-large | eligible | People's names | 1878/3798 | 49.45% | 52.79% | 49.45% |
| model:gliner2-large | eligible | Phone numbers & email | 568/588 | 96.60% | 97.45% | 96.43% |
| model:gliner2-large | eligible | Addresses & locations | 784/1637 | 47.89% | 67.81% | 47.83% |
| model:gliner2-large | eligible | Dates & times | 39/650 | 6.00% | 6.46% | 6.00% |
| model:gliner2-large | eligible | Organizations | 198/277 | 71.48% | 76.17% | 71.48% |
| model:gliner2-large | eligible | Network identifiers | 412/1103 | 37.35% | 40.44% | 37.35% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 290/655 | 44.27% | 47.18% | 44.27% |
| model:gliner2-vladlinv | eligible | People's names | 3077/3798 | 81.02% | 83.57% | 80.73% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 381/588 | 64.80% | 64.97% | 64.63% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 162/1637 | 9.90% | 10.51% | 9.90% |
| model:gliner2-vladlinv | eligible | Dates & times | 53/650 | 8.15% | 10.15% | 8.15% |
| model:gliner2-vladlinv | eligible | Organizations | 2/277 | 0.72% | 0.72% | 0.72% |
| model:gliner2-vladlinv | eligible | Network identifiers | 76/1103 | 6.89% | 7.62% | 6.89% |
| model:gliner2-vladlinv-ru | eligible | Documents & identifiers | 357/655 | 54.50% | 56.64% | 54.50% |
| model:gliner2-vladlinv-ru | eligible | People's names | 2090/3798 | 55.03% | 56.85% | 54.98% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 382/588 | 64.97% | 65.14% | 64.80% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 142/1637 | 8.67% | 9.59% | 8.67% |
| model:gliner2-vladlinv-ru | eligible | Dates & times | 51/650 | 7.85% | 9.08% | 7.85% |
| model:gliner2-vladlinv-ru | eligible | Organizations | 0/277 | 0.00% | 0.00% | 0.00% |
| model:gliner2-vladlinv-ru | eligible | Network identifiers | 59/1103 | 5.35% | 5.89% | 5.35% |
| model:gliner25-fastino | eligible | Documents & identifiers | 22/655 | 3.36% | 3.66% | 3.36% |
| model:gliner25-fastino | eligible | People's names | 2936/3798 | 77.30% | 82.04% | 77.28% |
| model:gliner25-fastino | eligible | Phone numbers & email | 527/588 | 89.63% | 90.31% | 89.46% |
| model:gliner25-fastino | eligible | Addresses & locations | 970/1637 | 59.25% | 67.99% | 59.07% |
| model:gliner25-fastino | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:gliner25-fastino | eligible | Organizations | 82/277 | 29.60% | 32.85% | 29.60% |
| model:gliner25-fastino | eligible | Network identifiers | 778/1103 | 70.53% | 72.26% | 70.17% |
| model:gliner25-fastino-ru | eligible | Documents & identifiers | 262/655 | 40.00% | 40.92% | 40.00% |
| model:gliner25-fastino-ru | eligible | People's names | 2358/3798 | 62.09% | 63.69% | 62.06% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 477/588 | 81.12% | 81.80% | 80.95% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 888/1637 | 54.25% | 67.56% | 54.06% |
| model:gliner25-fastino-ru | eligible | Dates & times | 2/650 | 0.31% | 0.31% | 0.31% |
| model:gliner25-fastino-ru | eligible | Organizations | 51/277 | 18.41% | 20.94% | 18.41% |
| model:gliner25-fastino-ru | eligible | Network identifiers | 564/1103 | 51.13% | 52.77% | 50.95% |
| model:gravitee-small | eligible | Documents & identifiers | 170/655 | 25.95% | 35.57% | 21.98% |
| model:gravitee-small | eligible | People's names | 609/3798 | 16.03% | 19.06% | 11.66% |
| model:gravitee-small | eligible | Phone numbers & email | 386/588 | 65.65% | 83.50% | 61.22% |
| model:gravitee-small | eligible | Addresses & locations | 355/1637 | 21.69% | 31.77% | 17.78% |
| model:gravitee-small | eligible | Dates & times | 288/650 | 44.31% | 58.31% | 42.31% |
| model:gravitee-small | eligible | Organizations | 21/277 | 7.58% | 9.75% | 6.14% |
| model:gravitee-small | eligible | Network identifiers | 332/1103 | 30.10% | 68.54% | 28.01% |
| model:kalyan-ettin | eligible | Documents & identifiers | 95/655 | 14.50% | 32.67% | 2.90% |
| model:kalyan-ettin | eligible | People's names | 1942/3798 | 51.13% | 71.09% | 30.09% |
| model:kalyan-ettin | eligible | Phone numbers & email | 302/588 | 51.36% | 76.70% | 46.77% |
| model:kalyan-ettin | eligible | Addresses & locations | 519/1637 | 31.70% | 56.57% | 17.65% |
| model:kalyan-ettin | eligible | Dates & times | 362/650 | 55.69% | 77.38% | 51.54% |
| model:kalyan-ettin | eligible | Organizations | 67/277 | 24.19% | 37.55% | 11.91% |
| model:kalyan-ettin | eligible | Network identifiers | 418/1103 | 37.90% | 79.51% | 33.54% |
| model:mmbert32k | eligible | Documents & identifiers | 328/655 | 50.08% | 92.06% | 13.74% |
| model:mmbert32k | eligible | People's names | 2540/3798 | 66.88% | 83.68% | 32.99% |
| model:mmbert32k | eligible | Phone numbers & email | 308/588 | 52.38% | 98.98% | 34.01% |
| model:mmbert32k | eligible | Addresses & locations | 501/1637 | 30.60% | 68.23% | 16.25% |
| model:mmbert32k | eligible | Dates & times | 417/650 | 64.15% | 94.00% | 48.31% |
| model:mmbert32k | eligible | Organizations | 78/277 | 28.16% | 53.07% | 7.58% |
| model:mmbert32k | eligible | Network identifiers | 219/1103 | 19.85% | 95.83% | 6.26% |
| model:natasha | eligible | Documents & identifiers | 25/655 | 3.82% | 5.80% | 3.36% |
| model:natasha | eligible | People's names | 3413/3798 | 89.86% | 90.86% | 88.78% |
| model:natasha | eligible | Phone numbers & email | 0/588 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Addresses & locations | 659/1637 | 40.26% | 66.28% | 40.26% |
| model:natasha | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Organizations | 196/277 | 70.76% | 72.92% | 70.76% |
| model:natasha | eligible | Network identifiers | 1/1103 | 0.09% | 0.18% | 0.09% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/655 | 0.00% | 0.15% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 2471/3798 | 65.06% | 96.00% | 60.32% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/588 | 0.00% | 15.48% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 674/1637 | 41.17% | 80.57% | 33.41% |
| model:ner-ru-gherman | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Organizations | 3/277 | 1.08% | 10.47% | 1.08% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/1103 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 64/655 | 9.77% | 13.89% | 7.02% |
| model:ner-ru-yqelz | eligible | People's names | 2825/3798 | 74.38% | 76.49% | 70.54% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 0/588 | 0.00% | 4.59% | 0.00% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 746/1637 | 45.57% | 67.68% | 43.56% |
| model:ner-ru-yqelz | eligible | Dates & times | 48/650 | 7.38% | 13.08% | 6.62% |
| model:ner-ru-yqelz | eligible | Organizations | 182/277 | 65.70% | 70.40% | 61.01% |
| model:ner-ru-yqelz | eligible | Network identifiers | 44/1103 | 3.99% | 10.97% | 3.17% |
| model:nuner-zero | eligible | Documents & identifiers | 452/655 | 69.01% | 72.67% | 39.69% |
| model:nuner-zero | eligible | People's names | 3429/3798 | 90.28% | 93.81% | 62.82% |
| model:nuner-zero | eligible | Phone numbers & email | 571/588 | 97.11% | 98.30% | 70.75% |
| model:nuner-zero | eligible | Addresses & locations | 914/1637 | 55.83% | 76.05% | 31.46% |
| model:nuner-zero | eligible | Dates & times | 7/650 | 1.08% | 1.23% | 1.08% |
| model:nuner-zero | eligible | Organizations | 224/277 | 80.87% | 84.12% | 36.10% |
| model:nuner-zero | eligible | Network identifiers | 1040/1103 | 94.29% | 97.55% | 93.74% |
| model:nym-base | eligible | Documents & identifiers | 452/655 | 69.01% | 82.14% | 67.02% |
| model:nym-base | eligible | People's names | 2790/3798 | 73.46% | 99.29% | 96.45% |
| model:nym-base | eligible | Phone numbers & email | 551/588 | 93.71% | 97.45% | 93.03% |
| model:nym-base | eligible | Addresses & locations | 1067/1637 | 65.18% | 92.91% | 64.94% |
| model:nym-base | eligible | Dates & times | 572/650 | 88.00% | 94.31% | 86.15% |
| model:nym-base | eligible | Organizations | 183/277 | 66.06% | 72.56% | 66.43% |
| model:nym-base | eligible | Network identifiers | 541/1103 | 49.05% | 64.82% | 35.45% |
| model:nym-small | eligible | Documents & identifiers | 441/655 | 67.33% | 82.14% | 63.82% |
| model:nym-small | eligible | People's names | 2983/3798 | 78.54% | 97.02% | 95.08% |
| model:nym-small | eligible | Phone numbers & email | 553/588 | 94.05% | 98.64% | 92.69% |
| model:nym-small | eligible | Addresses & locations | 969/1637 | 59.19% | 88.76% | 58.28% |
| model:nym-small | eligible | Dates & times | 557/650 | 85.69% | 92.00% | 82.62% |
| model:nym-small | eligible | Organizations | 177/277 | 63.90% | 69.68% | 60.29% |
| model:nym-small | eligible | Network identifiers | 529/1103 | 47.96% | 68.63% | 33.73% |
| model:openai-base | eligible | Documents & identifiers | 524/655 | 80.00% | 85.50% | 80.00% |
| model:openai-base | eligible | People's names | 2881/3798 | 75.86% | 78.12% | 72.54% |
| model:openai-base | eligible | Phone numbers & email | 564/588 | 95.92% | 97.45% | 94.56% |
| model:openai-base | eligible | Addresses & locations | 881/1637 | 53.82% | 58.58% | 51.80% |
| model:openai-base | eligible | Dates & times | 407/650 | 62.62% | 69.54% | 61.85% |
| model:openai-base | eligible | Organizations | 58/277 | 20.94% | 24.19% | 17.33% |
| model:openai-base | eligible | Network identifiers | 800/1103 | 72.53% | 81.60% | 70.63% |
| model:openmed-multilingual | eligible | Documents & identifiers | 412/655 | 62.90% | 88.24% | 60.15% |
| model:openmed-multilingual | eligible | People's names | 1768/3798 | 46.55% | 69.14% | 43.36% |
| model:openmed-multilingual | eligible | Phone numbers & email | 529/588 | 89.97% | 97.11% | 88.95% |
| model:openmed-multilingual | eligible | Addresses & locations | 588/1637 | 35.92% | 72.21% | 28.10% |
| model:openmed-multilingual | eligible | Dates & times | 357/650 | 54.92% | 79.38% | 50.62% |
| model:openmed-multilingual | eligible | Organizations | 54/277 | 19.49% | 35.74% | 13.00% |
| model:openmed-multilingual | eligible | Network identifiers | 768/1103 | 69.63% | 96.55% | 61.83% |
| model:openmed-nemotron | eligible | Documents & identifiers | 132/655 | 20.15% | 41.98% | 10.99% |
| model:openmed-nemotron | eligible | People's names | 2037/3798 | 53.63% | 79.41% | 47.68% |
| model:openmed-nemotron | eligible | Phone numbers & email | 443/588 | 75.34% | 89.29% | 68.88% |
| model:openmed-nemotron | eligible | Addresses & locations | 680/1637 | 41.54% | 64.45% | 30.79% |
| model:openmed-nemotron | eligible | Dates & times | 352/650 | 54.15% | 70.46% | 50.00% |
| model:openmed-nemotron | eligible | Organizations | 61/277 | 22.02% | 38.27% | 10.83% |
| model:openmed-nemotron | eligible | Network identifiers | 549/1103 | 49.77% | 82.41% | 42.88% |
| model:opf-kz-ru | eligible | Documents & identifiers | 554/655 | 84.58% | 92.82% | 83.05% |
| model:opf-kz-ru | eligible | People's names | 2251/3798 | 59.27% | 63.85% | 50.71% |
| model:opf-kz-ru | eligible | Phone numbers & email | 559/588 | 95.07% | 98.81% | 94.05% |
| model:opf-kz-ru | eligible | Addresses & locations | 499/1637 | 30.48% | 46.37% | 27.79% |
| model:opf-kz-ru | eligible | Dates & times | 429/650 | 66.00% | 77.54% | 59.85% |
| model:opf-kz-ru | eligible | Organizations | 28/277 | 10.11% | 13.36% | 7.94% |
| model:opf-kz-ru | eligible | Network identifiers | 844/1103 | 76.52% | 97.10% | 62.83% |
| model:opf-ru | eligible | Documents & identifiers | 318/655 | 48.55% | 76.34% | 41.98% |
| model:opf-ru | eligible | People's names | 3055/3798 | 80.44% | 88.84% | 72.49% |
| model:opf-ru | eligible | Phone numbers & email | 500/588 | 85.03% | 97.45% | 81.29% |
| model:opf-ru | eligible | Addresses & locations | 607/1637 | 37.08% | 70.37% | 29.20% |
| model:opf-ru | eligible | Dates & times | 164/650 | 25.23% | 40.92% | 20.77% |
| model:opf-ru | eligible | Organizations | 49/277 | 17.69% | 33.57% | 7.58% |
| model:opf-ru | eligible | Network identifiers | 68/1103 | 6.17% | 64.01% | 1.63% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 384/655 | 58.63% | 80.00% | 52.82% |
| model:opf-ru-v2 | eligible | People's names | 2927/3798 | 77.07% | 81.02% | 70.12% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 516/588 | 87.76% | 93.88% | 85.03% |
| model:opf-ru-v2 | eligible | Addresses & locations | 618/1637 | 37.75% | 48.32% | 34.82% |
| model:opf-ru-v2 | eligible | Dates & times | 4/650 | 0.62% | 3.08% | 0.31% |
| model:opf-ru-v2 | eligible | Organizations | 57/277 | 20.58% | 28.88% | 16.25% |
| model:opf-ru-v2 | eligible | Network identifiers | 410/1103 | 37.17% | 73.16% | 32.64% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 373/655 | 56.95% | 72.67% | 47.48% |
| model:pii-shield-onnx | eligible | People's names | 2705/3798 | 71.22% | 78.04% | 63.80% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 544/588 | 92.52% | 98.47% | 87.93% |
| model:pii-shield-onnx | eligible | Addresses & locations | 701/1637 | 42.82% | 70.74% | 36.96% |
| model:pii-shield-onnx | eligible | Dates & times | 253/650 | 38.92% | 80.77% | 32.46% |
| model:pii-shield-onnx | eligible | Organizations | 26/277 | 9.39% | 19.49% | 5.42% |
| model:pii-shield-onnx | eligible | Network identifiers | 469/1103 | 42.52% | 89.57% | 31.55% |
| model:pplx | eligible | Documents & identifiers | 565/655 | 86.26% | 92.06% | 86.26% |
| model:pplx | eligible | People's names | 3763/3798 | 99.08% | 99.37% | 97.95% |
| model:pplx | eligible | Phone numbers & email | 585/588 | 99.49% | 99.66% | 99.32% |
| model:pplx | eligible | Addresses & locations | 1014/1637 | 61.94% | 67.75% | 61.51% |
| model:pplx | eligible | Dates & times | 473/650 | 72.77% | 74.92% | 72.62% |
| model:pplx | eligible | Organizations | 24/277 | 8.66% | 10.11% | 8.30% |
| model:pplx | eligible | Network identifiers | 1025/1103 | 92.93% | 94.02% | 91.93% |
| model:ru-legal-ner | eligible | Documents & identifiers | 338/655 | 51.60% | 79.85% | 40.92% |
| model:ru-legal-ner | eligible | People's names | 3404/3798 | 89.63% | 91.86% | 85.04% |
| model:ru-legal-ner | eligible | Phone numbers & email | 457/588 | 77.72% | 97.96% | 72.11% |
| model:ru-legal-ner | eligible | Addresses & locations | 652/1637 | 39.83% | 66.22% | 33.48% |
| model:ru-legal-ner | eligible | Dates & times | 375/650 | 57.69% | 79.08% | 56.46% |
| model:ru-legal-ner | eligible | Organizations | 159/277 | 57.40% | 71.12% | 45.85% |
| model:ru-legal-ner | eligible | Network identifiers | 32/1103 | 2.90% | 54.49% | 1.81% |
| model:ru-legal-ner+cpu | eligible | Documents & identifiers | 338/655 | 51.60% | 79.85% | 40.92% |
| model:ru-legal-ner+cpu | eligible | People's names | 3404/3798 | 89.63% | 91.86% | 85.04% |
| model:ru-legal-ner+cpu | eligible | Phone numbers & email | 457/588 | 77.72% | 97.96% | 72.11% |
| model:ru-legal-ner+cpu | eligible | Addresses & locations | 652/1637 | 39.83% | 66.22% | 33.48% |
| model:ru-legal-ner+cpu | eligible | Dates & times | 375/650 | 57.69% | 79.08% | 56.46% |
| model:ru-legal-ner+cpu | eligible | Organizations | 159/277 | 57.40% | 71.12% | 45.85% |
| model:ru-legal-ner+cpu | eligible | Network identifiers | 32/1103 | 2.90% | 54.49% | 1.81% |
| model:ru-pii-ner | eligible | Documents & identifiers | 486/655 | 74.20% | 82.90% | 74.20% |
| model:ru-pii-ner | eligible | People's names | 3744/3798 | 98.58% | 99.32% | 98.31% |
| model:ru-pii-ner | eligible | Phone numbers & email | 459/588 | 78.06% | 78.57% | 77.72% |
| model:ru-pii-ner | eligible | Addresses & locations | 416/1637 | 25.41% | 27.55% | 25.41% |
| model:ru-pii-ner | eligible | Dates & times | 371/650 | 57.08% | 62.46% | 56.92% |
| model:ru-pii-ner | eligible | Organizations | 4/277 | 1.44% | 1.44% | 1.44% |
| model:ru-pii-ner | eligible | Network identifiers | 262/1103 | 23.75% | 24.75% | 23.75% |
| model:rules-ru | eligible | Documents & identifiers | 26/655 | 3.97% | 4.27% | 3.97% |
| model:rules-ru | eligible | People's names | 0/3798 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 449/588 | 76.36% | 77.04% | 75.00% |
| model:rules-ru | eligible | Addresses & locations | 7/1637 | 0.43% | 0.43% | 0.43% |
| model:rules-ru | eligible | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Organizations | 2/277 | 0.72% | 1.44% | 0.72% |
| model:rules-ru | eligible | Network identifiers | 531/1103 | 48.14% | 70.17% | 48.05% |
| model:spacy-alrosait | train | Documents & identifiers | 1/655 | 0.15% | 0.15% | 0.15% |
| model:spacy-alrosait | train | People's names | 3339/3798 | 87.91% | 87.99% | 87.89% |
| model:spacy-alrosait | train | Phone numbers & email | 1/588 | 0.17% | 0.17% | 0.17% |
| model:spacy-alrosait | train | Addresses & locations | 1288/1637 | 78.68% | 80.51% | 78.62% |
| model:spacy-alrosait | train | Dates & times | 0/650 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | train | Organizations | 3/277 | 1.08% | 1.08% | 1.08% |
| model:spacy-alrosait | train | Network identifiers | 0/1103 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 21/655 | 3.21% | 4.12% | 3.21% |
| model:spacy-ru-lg | eligible | People's names | 3486/3798 | 91.79% | 92.86% | 89.73% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 27/588 | 4.59% | 4.59% | 4.59% |
| model:spacy-ru-lg | eligible | Addresses & locations | 689/1637 | 42.09% | 73.18% | 42.03% |
| model:spacy-ru-lg | eligible | Dates & times | 2/650 | 0.31% | 0.31% | 0.31% |
| model:spacy-ru-lg | eligible | Organizations | 203/277 | 73.29% | 76.53% | 73.29% |
| model:spacy-ru-lg | eligible | Network identifiers | 7/1103 | 0.63% | 0.82% | 0.63% |
| model:stanza-ru | eligible | Documents & identifiers | 163/655 | 24.89% | 37.40% | 24.89% |
| model:stanza-ru | eligible | People's names | 3737/3798 | 98.39% | 98.66% | 98.31% |
| model:stanza-ru | eligible | Phone numbers & email | 24/588 | 4.08% | 4.08% | 4.08% |
| model:stanza-ru | eligible | Addresses & locations | 879/1637 | 53.70% | 78.99% | 53.15% |
| model:stanza-ru | eligible | Dates & times | 8/650 | 1.23% | 2.15% | 1.23% |
| model:stanza-ru | eligible | Organizations | 213/277 | 76.90% | 85.20% | 76.90% |
| model:stanza-ru | eligible | Network identifiers | 11/1103 | 1.00% | 16.05% | 1.00% |
| model:traciora | eligible | Documents & identifiers | 266/655 | 40.61% | 60.76% | 33.74% |
| model:traciora | eligible | People's names | 3174/3798 | 83.57% | 87.15% | 79.09% |
| model:traciora | eligible | Phone numbers & email | 494/588 | 84.01% | 90.82% | 80.78% |
| model:traciora | eligible | Addresses & locations | 917/1637 | 56.02% | 65.12% | 50.40% |
| model:traciora | eligible | Dates & times | 6/650 | 0.92% | 2.62% | 0.62% |
| model:traciora | eligible | Organizations | 65/277 | 23.47% | 31.05% | 15.88% |
| model:traciora | eligible | Network identifiers | 231/1103 | 20.94% | 42.34% | 17.86% |
