# redact-ru: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/redact-ru.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| composition:fastino | eligible | Bank accounts & cards | 40/65 | 61.54% | 69.23% | 61.54% |
| composition:fastino | eligible | Documents & identifiers | 375/473 | 79.28% | 84.57% | 79.07% |
| composition:fastino | eligible | People's names | 3457/3854 | 89.70% | 91.90% | 89.70% |
| composition:fastino | eligible | Phone numbers & email | 1138/1199 | 94.91% | 97.83% | 94.91% |
| composition:fastino | eligible | Addresses & locations | 438/835 | 52.46% | 95.81% | 51.98% |
| composition:fastino | eligible | Dates & times | 323/324 | 99.69% | 100.00% | 99.69% |
| composition:fastino | eligible | Organizations | 193/366 | 52.73% | 93.44% | 52.73% |
| composition:fastino | eligible | Network identifiers | 46/54 | 85.19% | 88.89% | 85.19% |
| composition:fastino | eligible | Customer & employee IDs | 587/1160 | 50.60% | 52.84% | 50.60% |
| composition:fastino | eligible | Other sensitive attributes | 478/889 | 53.77% | 68.28% | 53.77% |
| composition:pplx | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| composition:pplx | eligible | Bank accounts & cards | 33/65 | 50.77% | 95.38% | 49.23% |
| composition:pplx | eligible | Documents & identifiers | 436/473 | 92.18% | 99.79% | 92.18% |
| composition:pplx | eligible | People's names | 3799/3854 | 98.57% | 99.87% | 97.33% |
| composition:pplx | eligible | Phone numbers & email | 1163/1199 | 97.00% | 99.42% | 96.91% |
| composition:pplx | eligible | Addresses & locations | 672/835 | 80.48% | 85.15% | 80.00% |
| composition:pplx | eligible | Dates & times | 314/324 | 96.91% | 100.00% | 96.60% |
| composition:pplx | eligible | Organizations | 30/366 | 8.20% | 9.56% | 8.20% |
| composition:pplx | eligible | Network identifiers | 50/54 | 92.59% | 98.15% | 92.59% |
| composition:pplx | eligible | Customer & employee IDs | 1105/1160 | 95.26% | 97.84% | 95.17% |
| composition:pplx | eligible | Other sensitive attributes | 431/889 | 48.48% | 56.81% | 48.03% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 43/65 | 66.15% | 98.46% | 64.62% |
| composition:pplx+fastino | eligible | Documents & identifiers | 442/473 | 93.45% | 99.79% | 93.45% |
| composition:pplx+fastino | eligible | People's names | 3826/3854 | 99.27% | 99.90% | 98.29% |
| composition:pplx+fastino | eligible | Phone numbers & email | 1169/1199 | 97.50% | 99.92% | 97.41% |
| composition:pplx+fastino | eligible | Addresses & locations | 788/835 | 94.37% | 99.16% | 94.13% |
| composition:pplx+fastino | eligible | Dates & times | 323/324 | 99.69% | 100.00% | 99.69% |
| composition:pplx+fastino | eligible | Organizations | 197/366 | 53.83% | 94.54% | 53.83% |
| composition:pplx+fastino | eligible | Network identifiers | 50/54 | 92.59% | 100.00% | 92.59% |
| composition:pplx+fastino | eligible | Customer & employee IDs | 1110/1160 | 95.69% | 98.10% | 95.69% |
| composition:pplx+fastino | eligible | Other sensitive attributes | 590/889 | 66.37% | 79.30% | 66.14% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 51/65 | 78.46% | 100.00% | 76.92% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 453/473 | 95.77% | 100.00% | 95.77% |
| composition:pplx+fastino+bardsai | eligible | People's names | 3847/3854 | 99.82% | 100.00% | 99.20% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 1172/1199 | 97.75% | 99.92% | 97.66% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 795/835 | 95.21% | 99.52% | 94.97% |
| composition:pplx+fastino+bardsai | eligible | Dates & times | 323/324 | 99.69% | 100.00% | 99.69% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 276/366 | 75.41% | 98.63% | 75.14% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 50/54 | 92.59% | 100.00% | 92.59% |
| composition:pplx+fastino+bardsai | eligible | Customer & employee IDs | 1128/1160 | 97.24% | 99.83% | 97.07% |
| composition:pplx+fastino+bardsai | eligible | Other sensitive attributes | 604/889 | 67.94% | 81.21% | 67.27% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 51/65 | 78.46% | 100.00% | 78.46% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 453/473 | 95.77% | 100.00% | 95.77% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 3847/3854 | 99.82% | 100.00% | 99.20% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 1172/1199 | 97.75% | 100.00% | 97.66% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 796/835 | 95.33% | 99.76% | 95.21% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Dates & times | 323/324 | 99.69% | 100.00% | 99.69% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 276/366 | 75.41% | 98.91% | 75.96% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 51/54 | 94.44% | 100.00% | 94.44% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Customer & employee IDs | 1132/1160 | 97.59% | 100.00% | 97.24% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Other sensitive attributes | 636/889 | 71.54% | 86.39% | 67.49% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 43/65 | 66.15% | 100.00% | 66.15% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 443/473 | 93.66% | 100.00% | 93.66% |
| composition:pplx+fastino+mmbert | eligible | People's names | 3832/3854 | 99.43% | 99.92% | 98.42% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 1169/1199 | 97.50% | 100.00% | 97.41% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 789/835 | 94.49% | 99.40% | 94.37% |
| composition:pplx+fastino+mmbert | eligible | Dates & times | 323/324 | 99.69% | 100.00% | 99.69% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 197/366 | 53.83% | 98.36% | 54.10% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 51/54 | 94.44% | 100.00% | 94.44% |
| composition:pplx+fastino+mmbert | eligible | Customer & employee IDs | 1113/1160 | 95.95% | 99.74% | 95.78% |
| composition:pplx+fastino+mmbert | eligible | Other sensitive attributes | 623/889 | 70.08% | 85.04% | 66.37% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Bank accounts & cards | 14/65 | 21.54% | 67.69% | 18.46% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 411/473 | 86.89% | 96.62% | 85.84% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 3714/3854 | 96.37% | 99.22% | 94.89% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 1156/1199 | 96.41% | 99.25% | 96.25% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 636/835 | 76.17% | 84.79% | 75.81% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Dates & times | 289/324 | 89.20% | 99.69% | 88.89% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 49/366 | 13.39% | 23.50% | 12.57% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 49/54 | 90.74% | 98.15% | 90.74% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Customer & employee IDs | 783/1160 | 67.50% | 81.90% | 64.05% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Other sensitive attributes | 308/889 | 34.65% | 44.77% | 33.18% |
| model:apararti | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:apararti | eligible | Bank accounts & cards | 40/65 | 61.54% | 83.08% | 58.46% |
| model:apararti | eligible | Documents & identifiers | 393/473 | 83.09% | 97.89% | 82.24% |
| model:apararti | eligible | People's names | 3382/3854 | 87.75% | 90.17% | 82.56% |
| model:apararti | eligible | Phone numbers & email | 1146/1199 | 95.58% | 98.58% | 95.33% |
| model:apararti | eligible | Addresses & locations | 615/835 | 73.65% | 78.20% | 72.22% |
| model:apararti | eligible | Dates & times | 304/324 | 93.83% | 99.07% | 93.83% |
| model:apararti | eligible | Organizations | 55/366 | 15.03% | 29.23% | 12.84% |
| model:apararti | eligible | Network identifiers | 43/54 | 79.63% | 96.30% | 70.37% |
| model:apararti | eligible | Customer & employee IDs | 963/1160 | 83.02% | 92.84% | 75.26% |
| model:apararti | eligible | Other sensitive attributes | 208/889 | 23.40% | 31.50% | 18.67% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 6/11 | 54.55% | 90.91% | 45.45% |
| model:bardsai-eu | eligible | Bank accounts & cards | 24/65 | 36.92% | 46.15% | 30.77% |
| model:bardsai-eu | eligible | Documents & identifiers | 386/473 | 81.61% | 91.97% | 74.84% |
| model:bardsai-eu | eligible | People's names | 3781/3854 | 98.11% | 98.68% | 93.18% |
| model:bardsai-eu | eligible | Phone numbers & email | 673/1199 | 56.13% | 98.67% | 45.54% |
| model:bardsai-eu | eligible | Addresses & locations | 563/835 | 67.43% | 98.20% | 62.28% |
| model:bardsai-eu | eligible | Dates & times | 309/324 | 95.37% | 97.84% | 95.37% |
| model:bardsai-eu | eligible | Organizations | 226/366 | 61.75% | 91.80% | 58.20% |
| model:bardsai-eu | eligible | Network identifiers | 44/54 | 81.48% | 96.30% | 62.96% |
| model:bardsai-eu | eligible | Customer & employee IDs | 823/1160 | 70.95% | 92.84% | 58.02% |
| model:bardsai-eu | eligible | Other sensitive attributes | 349/889 | 39.26% | 49.61% | 34.53% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/11 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Bank accounts & cards | 0/65 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 0/473 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | People's names | 3711/3854 | 96.29% | 98.70% | 88.53% |
| model:davlan-mbert | eligible | Phone numbers & email | 7/1199 | 0.58% | 13.34% | 0.33% |
| model:davlan-mbert | eligible | Addresses & locations | 426/835 | 51.02% | 97.96% | 49.34% |
| model:davlan-mbert | eligible | Dates & times | 0/324 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Organizations | 248/366 | 67.76% | 90.44% | 65.03% |
| model:davlan-mbert | eligible | Network identifiers | 0/54 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Customer & employee IDs | 42/1160 | 3.62% | 8.45% | 0.09% |
| model:davlan-mbert | eligible | Other sensitive attributes | 91/889 | 10.24% | 18.00% | 8.89% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/11 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 0/65 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 0/473 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 3794/3854 | 98.44% | 98.75% | 93.20% |
| model:davlan-xlmr | eligible | Phone numbers & email | 1/1199 | 0.08% | 22.60% | 0.08% |
| model:davlan-xlmr | eligible | Addresses & locations | 431/835 | 51.62% | 97.84% | 50.06% |
| model:davlan-xlmr | eligible | Dates & times | 0/324 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Organizations | 262/366 | 71.58% | 92.62% | 69.40% |
| model:davlan-xlmr | eligible | Network identifiers | 0/54 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Customer & employee IDs | 38/1160 | 3.28% | 10.43% | 0.26% |
| model:davlan-xlmr | eligible | Other sensitive attributes | 91/889 | 10.24% | 17.21% | 9.11% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 5/11 | 45.45% | 90.91% | 45.45% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 3/65 | 4.62% | 7.69% | 3.08% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 33/473 | 6.98% | 12.90% | 5.07% |
| model:fef2-secret-ru | eligible | People's names | 3092/3854 | 80.23% | 93.18% | 78.05% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 617/1199 | 51.46% | 56.88% | 50.29% |
| model:fef2-secret-ru | eligible | Addresses & locations | 372/835 | 44.55% | 91.50% | 43.59% |
| model:fef2-secret-ru | eligible | Dates & times | 1/324 | 0.31% | 0.62% | 0.31% |
| model:fef2-secret-ru | eligible | Organizations | 225/366 | 61.48% | 84.97% | 59.84% |
| model:fef2-secret-ru | eligible | Network identifiers | 1/54 | 1.85% | 1.85% | 0.00% |
| model:fef2-secret-ru | eligible | Customer & employee IDs | 585/1160 | 50.43% | 61.81% | 44.66% |
| model:fef2-secret-ru | eligible | Other sensitive attributes | 76/889 | 8.55% | 17.10% | 7.20% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 2/11 | 18.18% | 45.45% | 18.18% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 2/65 | 3.08% | 4.62% | 3.08% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 40/473 | 8.46% | 9.73% | 8.46% |
| model:gliner-multi-v21 | eligible | People's names | 3547/3854 | 92.03% | 92.73% | 91.80% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 292/1199 | 24.35% | 44.95% | 24.27% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 402/835 | 48.14% | 94.25% | 48.14% |
| model:gliner-multi-v21 | eligible | Dates & times | 255/324 | 78.70% | 79.32% | 78.70% |
| model:gliner-multi-v21 | eligible | Organizations | 214/366 | 58.47% | 92.62% | 58.20% |
| model:gliner-multi-v21 | eligible | Network identifiers | 42/54 | 77.78% | 79.63% | 77.78% |
| model:gliner-multi-v21 | eligible | Customer & employee IDs | 151/1160 | 13.02% | 19.91% | 13.02% |
| model:gliner-multi-v21 | eligible | Other sensitive attributes | 303/889 | 34.08% | 47.02% | 34.08% |
| model:gliner-multi-v21-ru | eligible | Passwords, keys & tokens | 2/11 | 18.18% | 45.45% | 18.18% |
| model:gliner-multi-v21-ru | eligible | Bank accounts & cards | 0/65 | 0.00% | 4.62% | 0.00% |
| model:gliner-multi-v21-ru | eligible | Documents & identifiers | 60/473 | 12.68% | 13.74% | 12.68% |
| model:gliner-multi-v21-ru | eligible | People's names | 766/3854 | 19.88% | 20.03% | 19.82% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 181/1199 | 15.10% | 24.94% | 15.01% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 418/835 | 50.06% | 96.53% | 49.94% |
| model:gliner-multi-v21-ru | eligible | Dates & times | 227/324 | 70.06% | 70.37% | 70.06% |
| model:gliner-multi-v21-ru | eligible | Organizations | 213/366 | 58.20% | 89.07% | 57.92% |
| model:gliner-multi-v21-ru | eligible | Network identifiers | 43/54 | 79.63% | 81.48% | 79.63% |
| model:gliner-multi-v21-ru | eligible | Customer & employee IDs | 73/1160 | 6.29% | 8.10% | 6.29% |
| model:gliner-multi-v21-ru | eligible | Other sensitive attributes | 228/889 | 25.65% | 35.88% | 25.65% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:gliner-nvidia | eligible | Bank accounts & cards | 12/65 | 18.46% | 50.77% | 18.46% |
| model:gliner-nvidia | eligible | Documents & identifiers | 327/473 | 69.13% | 74.42% | 69.13% |
| model:gliner-nvidia | eligible | People's names | 2408/3854 | 62.48% | 96.99% | 62.43% |
| model:gliner-nvidia | eligible | Phone numbers & email | 1031/1199 | 85.99% | 98.75% | 85.99% |
| model:gliner-nvidia | eligible | Addresses & locations | 417/835 | 49.94% | 91.50% | 49.94% |
| model:gliner-nvidia | eligible | Dates & times | 290/324 | 89.51% | 99.69% | 89.51% |
| model:gliner-nvidia | eligible | Organizations | 251/366 | 68.58% | 83.88% | 68.31% |
| model:gliner-nvidia | eligible | Network identifiers | 52/54 | 96.30% | 98.15% | 96.30% |
| model:gliner-nvidia | eligible | Customer & employee IDs | 659/1160 | 56.81% | 61.90% | 56.81% |
| model:gliner-nvidia | eligible | Other sensitive attributes | 409/889 | 46.01% | 62.54% | 46.01% |
| model:gliner-nvidia+ov100 | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:gliner-nvidia+ov100 | eligible | Bank accounts & cards | 13/65 | 20.00% | 43.08% | 20.00% |
| model:gliner-nvidia+ov100 | eligible | Documents & identifiers | 335/473 | 70.82% | 76.32% | 70.61% |
| model:gliner-nvidia+ov100 | eligible | People's names | 2407/3854 | 62.45% | 96.99% | 62.43% |
| model:gliner-nvidia+ov100 | eligible | Phone numbers & email | 1049/1199 | 87.49% | 98.83% | 87.49% |
| model:gliner-nvidia+ov100 | eligible | Addresses & locations | 415/835 | 49.70% | 91.26% | 49.58% |
| model:gliner-nvidia+ov100 | eligible | Dates & times | 290/324 | 89.51% | 99.07% | 89.51% |
| model:gliner-nvidia+ov100 | eligible | Organizations | 253/366 | 69.13% | 85.25% | 68.85% |
| model:gliner-nvidia+ov100 | eligible | Network identifiers | 50/54 | 92.59% | 92.59% | 92.59% |
| model:gliner-nvidia+ov100 | eligible | Customer & employee IDs | 632/1160 | 54.48% | 60.26% | 54.40% |
| model:gliner-nvidia+ov100 | eligible | Other sensitive attributes | 406/889 | 45.67% | 62.43% | 45.44% |
| model:gliner-nvidia+sent300 | eligible | Passwords, keys & tokens | 7/11 | 63.64% | 100.00% | 63.64% |
| model:gliner-nvidia+sent300 | eligible | Bank accounts & cards | 15/65 | 23.08% | 53.85% | 23.08% |
| model:gliner-nvidia+sent300 | eligible | Documents & identifiers | 361/473 | 76.32% | 81.61% | 76.32% |
| model:gliner-nvidia+sent300 | eligible | People's names | 2437/3854 | 63.23% | 98.11% | 63.23% |
| model:gliner-nvidia+sent300 | eligible | Phone numbers & email | 1043/1199 | 86.99% | 99.00% | 86.91% |
| model:gliner-nvidia+sent300 | eligible | Addresses & locations | 433/835 | 51.86% | 95.21% | 51.62% |
| model:gliner-nvidia+sent300 | eligible | Dates & times | 293/324 | 90.43% | 99.07% | 90.43% |
| model:gliner-nvidia+sent300 | eligible | Organizations | 275/366 | 75.14% | 89.89% | 74.86% |
| model:gliner-nvidia+sent300 | eligible | Network identifiers | 51/54 | 94.44% | 94.44% | 94.44% |
| model:gliner-nvidia+sent300 | eligible | Customer & employee IDs | 720/1160 | 62.07% | 67.93% | 62.07% |
| model:gliner-nvidia+sent300 | eligible | Other sensitive attributes | 447/889 | 50.28% | 67.49% | 50.28% |
| model:gliner-nvidia-ru | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:gliner-nvidia-ru | eligible | Bank accounts & cards | 18/65 | 27.69% | 73.85% | 27.69% |
| model:gliner-nvidia-ru | eligible | Documents & identifiers | 277/473 | 58.56% | 67.65% | 58.56% |
| model:gliner-nvidia-ru | eligible | People's names | 1711/3854 | 44.40% | 75.06% | 44.11% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 989/1199 | 82.49% | 96.08% | 82.49% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 401/835 | 48.02% | 89.34% | 48.02% |
| model:gliner-nvidia-ru | eligible | Dates & times | 288/324 | 88.89% | 98.77% | 88.89% |
| model:gliner-nvidia-ru | eligible | Organizations | 146/366 | 39.89% | 62.02% | 39.89% |
| model:gliner-nvidia-ru | eligible | Network identifiers | 38/54 | 70.37% | 70.37% | 70.37% |
| model:gliner-nvidia-ru | eligible | Customer & employee IDs | 402/1160 | 34.66% | 38.45% | 34.66% |
| model:gliner-nvidia-ru | eligible | Other sensitive attributes | 343/889 | 38.58% | 51.52% | 38.58% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 2/11 | 18.18% | 54.55% | 18.18% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 2/65 | 3.08% | 6.15% | 3.08% |
| model:gliner-pii-base | eligible | Documents & identifiers | 145/473 | 30.66% | 34.67% | 30.66% |
| model:gliner-pii-base | eligible | People's names | 403/3854 | 10.46% | 16.11% | 10.46% |
| model:gliner-pii-base | eligible | Phone numbers & email | 1022/1199 | 85.24% | 87.41% | 85.24% |
| model:gliner-pii-base | eligible | Addresses & locations | 273/835 | 32.69% | 63.59% | 32.69% |
| model:gliner-pii-base | eligible | Dates & times | 47/324 | 14.51% | 14.51% | 14.51% |
| model:gliner-pii-base | eligible | Organizations | 121/366 | 33.06% | 78.96% | 33.06% |
| model:gliner-pii-base | eligible | Network identifiers | 44/54 | 81.48% | 81.48% | 81.48% |
| model:gliner-pii-base | eligible | Customer & employee IDs | 342/1160 | 29.48% | 30.26% | 29.22% |
| model:gliner-pii-base | eligible | Other sensitive attributes | 129/889 | 14.51% | 21.71% | 14.29% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 5/11 | 45.45% | 90.91% | 45.45% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 17/65 | 26.15% | 35.38% | 24.62% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 245/473 | 51.80% | 59.62% | 51.80% |
| model:gliner-pii-edge | eligible | People's names | 2527/3854 | 65.57% | 70.29% | 64.87% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 1044/1199 | 87.07% | 92.74% | 87.07% |
| model:gliner-pii-edge | eligible | Addresses & locations | 302/835 | 36.17% | 63.71% | 36.17% |
| model:gliner-pii-edge | eligible | Dates & times | 72/324 | 22.22% | 23.77% | 22.22% |
| model:gliner-pii-edge | eligible | Organizations | 101/366 | 27.60% | 70.22% | 27.60% |
| model:gliner-pii-edge | eligible | Network identifiers | 49/54 | 90.74% | 94.44% | 90.74% |
| model:gliner-pii-edge | eligible | Customer & employee IDs | 576/1160 | 49.66% | 57.67% | 49.66% |
| model:gliner-pii-edge | eligible | Other sensitive attributes | 266/889 | 29.92% | 58.16% | 29.13% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 5/11 | 45.45% | 63.64% | 45.45% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 10/65 | 15.38% | 80.00% | 15.38% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 49/473 | 10.36% | 43.55% | 10.36% |
| model:gliner-stream-pii | eligible | People's names | 1057/3854 | 27.43% | 41.75% | 27.22% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 663/1199 | 55.30% | 59.63% | 55.30% |
| model:gliner-stream-pii | eligible | Addresses & locations | 162/835 | 19.40% | 38.68% | 19.40% |
| model:gliner-stream-pii | eligible | Dates & times | 222/324 | 68.52% | 82.72% | 68.52% |
| model:gliner-stream-pii | eligible | Organizations | 74/366 | 20.22% | 24.04% | 20.22% |
| model:gliner-stream-pii | eligible | Network identifiers | 45/54 | 83.33% | 83.33% | 83.33% |
| model:gliner-stream-pii | eligible | Customer & employee IDs | 330/1160 | 28.45% | 34.91% | 28.45% |
| model:gliner-stream-pii | eligible | Other sensitive attributes | 167/889 | 18.79% | 36.11% | 18.79% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 7/11 | 63.64% | 100.00% | 63.64% |
| model:gliner-urchade | eligible | Bank accounts & cards | 28/65 | 43.08% | 50.77% | 43.08% |
| model:gliner-urchade | eligible | Documents & identifiers | 299/473 | 63.21% | 67.44% | 63.21% |
| model:gliner-urchade | eligible | People's names | 3713/3854 | 96.34% | 96.76% | 96.34% |
| model:gliner-urchade | eligible | Phone numbers & email | 1142/1199 | 95.25% | 98.33% | 95.16% |
| model:gliner-urchade | eligible | Addresses & locations | 475/835 | 56.89% | 93.17% | 56.89% |
| model:gliner-urchade | eligible | Dates & times | 301/324 | 92.90% | 95.99% | 92.90% |
| model:gliner-urchade | eligible | Organizations | 327/366 | 89.34% | 93.99% | 89.34% |
| model:gliner-urchade | eligible | Network identifiers | 50/54 | 92.59% | 92.59% | 92.59% |
| model:gliner-urchade | eligible | Customer & employee IDs | 613/1160 | 52.84% | 54.05% | 52.84% |
| model:gliner-urchade | eligible | Other sensitive attributes | 480/889 | 53.99% | 73.23% | 53.99% |
| model:gliner-urchade-ru | eligible | Passwords, keys & tokens | 6/11 | 54.55% | 90.91% | 54.55% |
| model:gliner-urchade-ru | eligible | Bank accounts & cards | 26/65 | 40.00% | 46.15% | 40.00% |
| model:gliner-urchade-ru | eligible | Documents & identifiers | 328/473 | 69.34% | 72.94% | 69.34% |
| model:gliner-urchade-ru | eligible | People's names | 245/3854 | 6.36% | 6.77% | 6.36% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 998/1199 | 83.24% | 86.32% | 83.24% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 483/835 | 57.84% | 93.77% | 57.84% |
| model:gliner-urchade-ru | eligible | Dates & times | 304/324 | 93.83% | 95.68% | 93.83% |
| model:gliner-urchade-ru | eligible | Organizations | 327/366 | 89.34% | 93.99% | 89.34% |
| model:gliner-urchade-ru | eligible | Network identifiers | 50/54 | 92.59% | 92.59% | 92.59% |
| model:gliner-urchade-ru | eligible | Customer & employee IDs | 268/1160 | 23.10% | 25.00% | 23.10% |
| model:gliner-urchade-ru | eligible | Other sensitive attributes | 422/889 | 47.47% | 62.54% | 47.47% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 40/65 | 61.54% | 69.23% | 61.54% |
| model:gliner2-fastino | eligible | Documents & identifiers | 375/473 | 79.28% | 84.57% | 79.07% |
| model:gliner2-fastino | eligible | People's names | 3457/3854 | 89.70% | 91.90% | 89.70% |
| model:gliner2-fastino | eligible | Phone numbers & email | 1138/1199 | 94.91% | 97.83% | 94.91% |
| model:gliner2-fastino | eligible | Addresses & locations | 438/835 | 52.46% | 95.81% | 51.98% |
| model:gliner2-fastino | eligible | Dates & times | 323/324 | 99.69% | 100.00% | 99.69% |
| model:gliner2-fastino | eligible | Organizations | 193/366 | 52.73% | 93.44% | 52.73% |
| model:gliner2-fastino | eligible | Network identifiers | 46/54 | 85.19% | 88.89% | 85.19% |
| model:gliner2-fastino | eligible | Customer & employee IDs | 587/1160 | 50.60% | 52.84% | 50.60% |
| model:gliner2-fastino | eligible | Other sensitive attributes | 478/889 | 53.77% | 68.28% | 53.77% |
| model:gliner2-fastino-ru | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:gliner2-fastino-ru | eligible | Bank accounts & cards | 37/65 | 56.92% | 61.54% | 56.92% |
| model:gliner2-fastino-ru | eligible | Documents & identifiers | 399/473 | 84.36% | 90.06% | 84.14% |
| model:gliner2-fastino-ru | eligible | People's names | 2568/3854 | 66.63% | 68.03% | 66.63% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 1138/1199 | 94.91% | 97.50% | 94.91% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 440/835 | 52.69% | 95.93% | 52.34% |
| model:gliner2-fastino-ru | eligible | Dates & times | 323/324 | 99.69% | 100.00% | 99.69% |
| model:gliner2-fastino-ru | eligible | Organizations | 205/366 | 56.01% | 93.72% | 56.01% |
| model:gliner2-fastino-ru | eligible | Network identifiers | 46/54 | 85.19% | 88.89% | 85.19% |
| model:gliner2-fastino-ru | eligible | Customer & employee IDs | 422/1160 | 36.38% | 38.53% | 36.38% |
| model:gliner2-fastino-ru | eligible | Other sensitive attributes | 456/889 | 51.29% | 63.44% | 51.29% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:gliner2-hivetrace-omni | eligible | Bank accounts & cards | 44/65 | 67.69% | 73.85% | 67.69% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 297/473 | 62.79% | 66.60% | 62.79% |
| model:gliner2-hivetrace-omni | eligible | People's names | 3539/3854 | 91.83% | 92.86% | 91.83% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 1138/1199 | 94.91% | 97.58% | 94.91% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 382/835 | 45.75% | 90.42% | 45.75% |
| model:gliner2-hivetrace-omni | eligible | Dates & times | 309/324 | 95.37% | 97.53% | 95.37% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 297/366 | 81.15% | 88.25% | 81.15% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 46/54 | 85.19% | 85.19% | 85.19% |
| model:gliner2-hivetrace-omni | eligible | Customer & employee IDs | 679/1160 | 58.53% | 60.60% | 58.53% |
| model:gliner2-hivetrace-omni | eligible | Other sensitive attributes | 441/889 | 49.61% | 59.84% | 49.61% |
| model:gliner2-hivetrace-omni-ru | eligible | Passwords, keys & tokens | 7/11 | 63.64% | 72.73% | 63.64% |
| model:gliner2-hivetrace-omni-ru | eligible | Bank accounts & cards | 42/65 | 64.62% | 70.77% | 64.62% |
| model:gliner2-hivetrace-omni-ru | eligible | Documents & identifiers | 296/473 | 62.58% | 67.65% | 62.58% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 3120/3854 | 80.95% | 84.33% | 80.95% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 1138/1199 | 94.91% | 97.50% | 94.91% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 383/835 | 45.87% | 90.18% | 45.87% |
| model:gliner2-hivetrace-omni-ru | eligible | Dates & times | 309/324 | 95.37% | 96.30% | 95.37% |
| model:gliner2-hivetrace-omni-ru | eligible | Organizations | 296/366 | 80.87% | 88.52% | 80.87% |
| model:gliner2-hivetrace-omni-ru | eligible | Network identifiers | 47/54 | 87.04% | 87.04% | 87.04% |
| model:gliner2-hivetrace-omni-ru | eligible | Customer & employee IDs | 465/1160 | 40.09% | 41.29% | 40.09% |
| model:gliner2-hivetrace-omni-ru | eligible | Other sensitive attributes | 421/889 | 47.36% | 58.16% | 47.36% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 4/11 | 36.36% | 63.64% | 36.36% |
| model:gliner2-hivetrace-uni | eligible | Bank accounts & cards | 24/65 | 36.92% | 63.08% | 36.92% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 395/473 | 83.51% | 93.66% | 83.51% |
| model:gliner2-hivetrace-uni | eligible | People's names | 3470/3854 | 90.04% | 90.69% | 90.04% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 1134/1199 | 94.58% | 97.58% | 94.50% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 406/835 | 48.62% | 91.98% | 48.62% |
| model:gliner2-hivetrace-uni | eligible | Dates & times | 280/324 | 86.42% | 88.27% | 86.42% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 156/366 | 42.62% | 51.64% | 42.62% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 35/54 | 64.81% | 66.67% | 64.81% |
| model:gliner2-hivetrace-uni | eligible | Customer & employee IDs | 707/1160 | 60.95% | 63.79% | 60.95% |
| model:gliner2-hivetrace-uni | eligible | Other sensitive attributes | 73/889 | 8.21% | 14.62% | 8.21% |
| model:gliner2-hivetrace-uni-ru | eligible | Passwords, keys & tokens | 0/11 | 0.00% | 9.09% | 0.00% |
| model:gliner2-hivetrace-uni-ru | eligible | Bank accounts & cards | 6/65 | 9.23% | 9.23% | 9.23% |
| model:gliner2-hivetrace-uni-ru | eligible | Documents & identifiers | 139/473 | 29.39% | 33.40% | 29.39% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 499/3854 | 12.95% | 13.03% | 12.95% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 31/1199 | 2.59% | 2.75% | 2.59% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 166/835 | 19.88% | 45.87% | 19.88% |
| model:gliner2-hivetrace-uni-ru | eligible | Dates & times | 161/324 | 49.69% | 49.69% | 49.69% |
| model:gliner2-hivetrace-uni-ru | eligible | Organizations | 123/366 | 33.61% | 38.80% | 33.61% |
| model:gliner2-hivetrace-uni-ru | eligible | Network identifiers | 2/54 | 3.70% | 3.70% | 3.70% |
| model:gliner2-hivetrace-uni-ru | eligible | Customer & employee IDs | 398/1160 | 34.31% | 35.17% | 34.31% |
| model:gliner2-hivetrace-uni-ru | eligible | Other sensitive attributes | 14/889 | 1.57% | 3.04% | 1.57% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 5/11 | 45.45% | 100.00% | 45.45% |
| model:gliner2-large | eligible | Bank accounts & cards | 24/65 | 36.92% | 66.15% | 36.92% |
| model:gliner2-large | eligible | Documents & identifiers | 246/473 | 52.01% | 60.47% | 51.80% |
| model:gliner2-large | eligible | People's names | 2253/3854 | 58.46% | 63.49% | 58.41% |
| model:gliner2-large | eligible | Phone numbers & email | 1126/1199 | 93.91% | 97.83% | 93.91% |
| model:gliner2-large | eligible | Addresses & locations | 306/835 | 36.65% | 75.69% | 36.65% |
| model:gliner2-large | eligible | Dates & times | 303/324 | 93.52% | 94.44% | 93.52% |
| model:gliner2-large | eligible | Organizations | 208/366 | 56.83% | 69.95% | 56.83% |
| model:gliner2-large | eligible | Network identifiers | 47/54 | 87.04% | 87.04% | 87.04% |
| model:gliner2-large | eligible | Customer & employee IDs | 447/1160 | 38.53% | 40.52% | 38.53% |
| model:gliner2-large | eligible | Other sensitive attributes | 419/889 | 47.13% | 56.02% | 47.02% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 4/11 | 36.36% | 36.36% | 36.36% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 5/65 | 7.69% | 13.85% | 7.69% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 114/473 | 24.10% | 27.91% | 23.89% |
| model:gliner2-vladlinv | eligible | People's names | 2536/3854 | 65.80% | 67.67% | 65.78% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 1027/1199 | 85.65% | 87.49% | 85.65% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 377/835 | 45.15% | 47.66% | 45.15% |
| model:gliner2-vladlinv | eligible | Dates & times | 293/324 | 90.43% | 99.07% | 90.43% |
| model:gliner2-vladlinv | eligible | Organizations | 13/366 | 3.55% | 4.10% | 3.55% |
| model:gliner2-vladlinv | eligible | Network identifiers | 14/54 | 25.93% | 25.93% | 25.93% |
| model:gliner2-vladlinv | eligible | Customer & employee IDs | 174/1160 | 15.00% | 15.52% | 15.00% |
| model:gliner2-vladlinv | eligible | Other sensitive attributes | 25/889 | 2.81% | 4.16% | 2.81% |
| model:gliner2-vladlinv-ru | eligible | Passwords, keys & tokens | 6/11 | 54.55% | 54.55% | 54.55% |
| model:gliner2-vladlinv-ru | eligible | Bank accounts & cards | 12/65 | 18.46% | 38.46% | 18.46% |
| model:gliner2-vladlinv-ru | eligible | Documents & identifiers | 208/473 | 43.97% | 51.37% | 43.97% |
| model:gliner2-vladlinv-ru | eligible | People's names | 2228/3854 | 57.81% | 59.44% | 57.76% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 1027/1199 | 85.65% | 87.49% | 85.65% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 408/835 | 48.86% | 51.26% | 48.86% |
| model:gliner2-vladlinv-ru | eligible | Dates & times | 289/324 | 89.20% | 97.84% | 89.20% |
| model:gliner2-vladlinv-ru | eligible | Organizations | 13/366 | 3.55% | 3.83% | 3.55% |
| model:gliner2-vladlinv-ru | eligible | Network identifiers | 14/54 | 25.93% | 25.93% | 25.93% |
| model:gliner2-vladlinv-ru | eligible | Customer & employee IDs | 227/1160 | 19.57% | 21.03% | 19.57% |
| model:gliner2-vladlinv-ru | eligible | Other sensitive attributes | 38/889 | 4.27% | 6.30% | 4.27% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 5/11 | 45.45% | 45.45% | 45.45% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 6/65 | 9.23% | 12.31% | 9.23% |
| model:gliner25-fastino | eligible | Documents & identifiers | 163/473 | 34.46% | 38.27% | 34.46% |
| model:gliner25-fastino | eligible | People's names | 3615/3854 | 93.80% | 94.40% | 93.80% |
| model:gliner25-fastino | eligible | Phone numbers & email | 1143/1199 | 95.33% | 98.00% | 95.33% |
| model:gliner25-fastino | eligible | Addresses & locations | 647/835 | 77.49% | 93.17% | 77.13% |
| model:gliner25-fastino | eligible | Dates & times | 80/324 | 24.69% | 24.69% | 24.69% |
| model:gliner25-fastino | eligible | Organizations | 175/366 | 47.81% | 86.89% | 47.81% |
| model:gliner25-fastino | eligible | Network identifiers | 46/54 | 85.19% | 87.04% | 85.19% |
| model:gliner25-fastino | eligible | Customer & employee IDs | 167/1160 | 14.40% | 15.17% | 14.40% |
| model:gliner25-fastino | eligible | Other sensitive attributes | 292/889 | 32.85% | 43.31% | 32.85% |
| model:gliner25-fastino+nochunk | eligible | Passwords, keys & tokens | 6/11 | 54.55% | 54.55% | 54.55% |
| model:gliner25-fastino+nochunk | eligible | Bank accounts & cards | 19/65 | 29.23% | 32.31% | 29.23% |
| model:gliner25-fastino+nochunk | eligible | Documents & identifiers | 180/473 | 38.05% | 40.59% | 38.05% |
| model:gliner25-fastino+nochunk | eligible | People's names | 3138/3854 | 81.42% | 82.62% | 81.42% |
| model:gliner25-fastino+nochunk | eligible | Phone numbers & email | 1138/1199 | 94.91% | 97.25% | 94.91% |
| model:gliner25-fastino+nochunk | eligible | Addresses & locations | 657/835 | 78.68% | 90.18% | 78.32% |
| model:gliner25-fastino+nochunk | eligible | Dates & times | 86/324 | 26.54% | 26.85% | 26.54% |
| model:gliner25-fastino+nochunk | eligible | Organizations | 196/366 | 53.55% | 82.24% | 53.55% |
| model:gliner25-fastino+nochunk | eligible | Network identifiers | 48/54 | 88.89% | 92.59% | 88.89% |
| model:gliner25-fastino+nochunk | eligible | Customer & employee IDs | 226/1160 | 19.48% | 20.09% | 19.48% |
| model:gliner25-fastino+nochunk | eligible | Other sensitive attributes | 285/889 | 32.06% | 40.49% | 32.06% |
| model:gliner25-fastino+ov100 | eligible | Passwords, keys & tokens | 4/11 | 36.36% | 36.36% | 36.36% |
| model:gliner25-fastino+ov100 | eligible | Bank accounts & cards | 7/65 | 10.77% | 13.85% | 10.77% |
| model:gliner25-fastino+ov100 | eligible | Documents & identifiers | 172/473 | 36.36% | 39.32% | 36.15% |
| model:gliner25-fastino+ov100 | eligible | People's names | 3618/3854 | 93.88% | 94.40% | 93.80% |
| model:gliner25-fastino+ov100 | eligible | Phone numbers & email | 1151/1199 | 96.00% | 98.75% | 96.00% |
| model:gliner25-fastino+ov100 | eligible | Addresses & locations | 661/835 | 79.16% | 94.13% | 78.68% |
| model:gliner25-fastino+ov100 | eligible | Dates & times | 89/324 | 27.47% | 28.09% | 26.85% |
| model:gliner25-fastino+ov100 | eligible | Organizations | 180/366 | 49.18% | 86.89% | 49.18% |
| model:gliner25-fastino+ov100 | eligible | Network identifiers | 44/54 | 81.48% | 83.33% | 81.48% |
| model:gliner25-fastino+ov100 | eligible | Customer & employee IDs | 163/1160 | 14.05% | 14.83% | 14.05% |
| model:gliner25-fastino+ov100 | eligible | Other sensitive attributes | 297/889 | 33.41% | 43.87% | 33.30% |
| model:gliner25-fastino+sent300 | eligible | Passwords, keys & tokens | 4/11 | 36.36% | 36.36% | 36.36% |
| model:gliner25-fastino+sent300 | eligible | Bank accounts & cards | 1/65 | 1.54% | 4.62% | 1.54% |
| model:gliner25-fastino+sent300 | eligible | Documents & identifiers | 120/473 | 25.37% | 30.44% | 25.37% |
| model:gliner25-fastino+sent300 | eligible | People's names | 3645/3854 | 94.58% | 95.43% | 94.55% |
| model:gliner25-fastino+sent300 | eligible | Phone numbers & email | 1124/1199 | 93.74% | 96.66% | 93.74% |
| model:gliner25-fastino+sent300 | eligible | Addresses & locations | 555/835 | 66.47% | 93.65% | 65.99% |
| model:gliner25-fastino+sent300 | eligible | Dates & times | 88/324 | 27.16% | 27.16% | 27.16% |
| model:gliner25-fastino+sent300 | eligible | Organizations | 165/366 | 45.08% | 89.07% | 45.08% |
| model:gliner25-fastino+sent300 | eligible | Network identifiers | 42/54 | 77.78% | 77.78% | 77.78% |
| model:gliner25-fastino+sent300 | eligible | Customer & employee IDs | 142/1160 | 12.24% | 13.10% | 12.24% |
| model:gliner25-fastino+sent300 | eligible | Other sensitive attributes | 278/889 | 31.27% | 40.49% | 31.27% |
| model:gliner25-fastino-ru | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 72.73% | 72.73% |
| model:gliner25-fastino-ru | eligible | Bank accounts & cards | 37/65 | 56.92% | 61.54% | 56.92% |
| model:gliner25-fastino-ru | eligible | Documents & identifiers | 201/473 | 42.49% | 46.30% | 42.49% |
| model:gliner25-fastino-ru | eligible | People's names | 3004/3854 | 77.94% | 78.26% | 77.94% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 1155/1199 | 96.33% | 98.67% | 96.33% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 616/835 | 73.77% | 91.86% | 73.41% |
| model:gliner25-fastino-ru | eligible | Dates & times | 163/324 | 50.31% | 50.31% | 50.31% |
| model:gliner25-fastino-ru | eligible | Organizations | 175/366 | 47.81% | 85.25% | 47.81% |
| model:gliner25-fastino-ru | eligible | Network identifiers | 47/54 | 87.04% | 88.89% | 87.04% |
| model:gliner25-fastino-ru | eligible | Customer & employee IDs | 214/1160 | 18.45% | 20.17% | 18.45% |
| model:gliner25-fastino-ru | eligible | Other sensitive attributes | 298/889 | 33.52% | 42.97% | 33.52% |
| model:gliner25-fastino-ru+nochunk | eligible | Passwords, keys & tokens | 7/11 | 63.64% | 63.64% | 63.64% |
| model:gliner25-fastino-ru+nochunk | eligible | Bank accounts & cards | 43/65 | 66.15% | 72.31% | 66.15% |
| model:gliner25-fastino-ru+nochunk | eligible | Documents & identifiers | 220/473 | 46.51% | 50.11% | 46.51% |
| model:gliner25-fastino-ru+nochunk | eligible | People's names | 2392/3854 | 62.07% | 62.40% | 62.07% |
| model:gliner25-fastino-ru+nochunk | eligible | Phone numbers & email | 1137/1199 | 94.83% | 96.58% | 94.83% |
| model:gliner25-fastino-ru+nochunk | eligible | Addresses & locations | 667/835 | 79.88% | 92.46% | 79.52% |
| model:gliner25-fastino-ru+nochunk | eligible | Dates & times | 193/324 | 59.57% | 59.88% | 59.57% |
| model:gliner25-fastino-ru+nochunk | eligible | Organizations | 184/366 | 50.27% | 76.23% | 50.27% |
| model:gliner25-fastino-ru+nochunk | eligible | Network identifiers | 47/54 | 87.04% | 92.59% | 87.04% |
| model:gliner25-fastino-ru+nochunk | eligible | Customer & employee IDs | 265/1160 | 22.84% | 23.88% | 22.84% |
| model:gliner25-fastino-ru+nochunk | eligible | Other sensitive attributes | 322/889 | 36.22% | 45.78% | 36.22% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 1/11 | 9.09% | 45.45% | 9.09% |
| model:gravitee-small | eligible | Bank accounts & cards | 7/65 | 10.77% | 49.23% | 6.15% |
| model:gravitee-small | eligible | Documents & identifiers | 145/473 | 30.66% | 41.44% | 28.54% |
| model:gravitee-small | eligible | People's names | 1679/3854 | 43.57% | 47.66% | 36.38% |
| model:gravitee-small | eligible | Phone numbers & email | 828/1199 | 69.06% | 88.99% | 66.47% |
| model:gravitee-small | eligible | Addresses & locations | 425/835 | 50.90% | 66.11% | 44.79% |
| model:gravitee-small | eligible | Dates & times | 281/324 | 86.73% | 95.06% | 86.42% |
| model:gravitee-small | eligible | Organizations | 59/366 | 16.12% | 22.68% | 15.03% |
| model:gravitee-small | eligible | Network identifiers | 44/54 | 81.48% | 88.89% | 81.48% |
| model:gravitee-small | eligible | Customer & employee IDs | 70/1160 | 6.03% | 11.21% | 2.76% |
| model:gravitee-small | eligible | Other sensitive attributes | 142/889 | 15.97% | 21.03% | 12.60% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 6/11 | 54.55% | 81.82% | 18.18% |
| model:kalyan-ettin | eligible | Bank accounts & cards | 12/65 | 18.46% | 35.38% | 15.38% |
| model:kalyan-ettin | eligible | Documents & identifiers | 74/473 | 15.64% | 31.29% | 4.86% |
| model:kalyan-ettin | eligible | People's names | 2257/3854 | 58.56% | 84.33% | 34.95% |
| model:kalyan-ettin | eligible | Phone numbers & email | 752/1199 | 62.72% | 94.50% | 64.55% |
| model:kalyan-ettin | eligible | Addresses & locations | 317/835 | 37.96% | 88.14% | 19.52% |
| model:kalyan-ettin | eligible | Dates & times | 243/324 | 75.00% | 94.14% | 75.00% |
| model:kalyan-ettin | eligible | Organizations | 39/366 | 10.66% | 32.51% | 7.10% |
| model:kalyan-ettin | eligible | Network identifiers | 47/54 | 87.04% | 98.15% | 79.63% |
| model:kalyan-ettin | eligible | Customer & employee IDs | 286/1160 | 24.66% | 56.29% | 11.47% |
| model:kalyan-ettin | eligible | Other sensitive attributes | 109/889 | 12.26% | 20.58% | 6.52% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 4/11 | 36.36% | 72.73% | 9.09% |
| model:mmbert32k | eligible | Bank accounts & cards | 12/65 | 18.46% | 76.92% | 9.23% |
| model:mmbert32k | eligible | Documents & identifiers | 321/473 | 67.86% | 97.89% | 16.28% |
| model:mmbert32k | eligible | People's names | 2364/3854 | 61.34% | 78.75% | 45.90% |
| model:mmbert32k | eligible | Phone numbers & email | 199/1199 | 16.60% | 99.08% | 10.59% |
| model:mmbert32k | eligible | Addresses & locations | 108/835 | 12.93% | 62.87% | 6.47% |
| model:mmbert32k | eligible | Dates & times | 283/324 | 87.35% | 99.38% | 82.72% |
| model:mmbert32k | eligible | Organizations | 49/366 | 13.39% | 60.11% | 6.83% |
| model:mmbert32k | eligible | Network identifiers | 36/54 | 66.67% | 98.15% | 9.26% |
| model:mmbert32k | eligible | Customer & employee IDs | 284/1160 | 24.48% | 94.14% | 4.57% |
| model:mmbert32k | eligible | Other sensitive attributes | 119/889 | 13.39% | 29.58% | 2.36% |
| model:mmbert32k+nochunk | eligible | Passwords, keys & tokens | 4/11 | 36.36% | 72.73% | 0.00% |
| model:mmbert32k+nochunk | eligible | Bank accounts & cards | 10/65 | 15.38% | 64.62% | 9.23% |
| model:mmbert32k+nochunk | eligible | Documents & identifiers | 273/473 | 57.72% | 94.50% | 9.51% |
| model:mmbert32k+nochunk | eligible | People's names | 1280/3854 | 33.21% | 52.52% | 18.73% |
| model:mmbert32k+nochunk | eligible | Phone numbers & email | 79/1199 | 6.59% | 94.16% | 3.50% |
| model:mmbert32k+nochunk | eligible | Addresses & locations | 55/835 | 6.59% | 52.10% | 4.07% |
| model:mmbert32k+nochunk | eligible | Dates & times | 240/324 | 74.07% | 96.60% | 61.11% |
| model:mmbert32k+nochunk | eligible | Organizations | 23/366 | 6.28% | 45.08% | 2.46% |
| model:mmbert32k+nochunk | eligible | Network identifiers | 13/54 | 24.07% | 100.00% | 5.56% |
| model:mmbert32k+nochunk | eligible | Customer & employee IDs | 216/1160 | 18.62% | 89.31% | 2.16% |
| model:mmbert32k+nochunk | eligible | Other sensitive attributes | 103/889 | 11.59% | 27.45% | 1.91% |
| model:natasha | eligible | Passwords, keys & tokens | 0/11 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Bank accounts & cards | 0/65 | 0.00% | 4.62% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 3/473 | 0.63% | 0.63% | 0.63% |
| model:natasha | eligible | People's names | 3005/3854 | 77.97% | 79.87% | 77.14% |
| model:natasha | eligible | Phone numbers & email | 1/1199 | 0.08% | 1.58% | 0.08% |
| model:natasha | eligible | Addresses & locations | 392/835 | 46.95% | 93.53% | 46.83% |
| model:natasha | eligible | Dates & times | 0/324 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Organizations | 232/366 | 63.39% | 86.34% | 63.39% |
| model:natasha | eligible | Network identifiers | 0/54 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Customer & employee IDs | 165/1160 | 14.22% | 14.57% | 14.05% |
| model:natasha | eligible | Other sensitive attributes | 92/889 | 10.35% | 18.22% | 9.79% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 1/11 | 9.09% | 9.09% | 0.00% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 0/65 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/473 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 2472/3854 | 64.14% | 99.30% | 57.81% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/1199 | 0.00% | 47.29% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 406/835 | 48.62% | 97.49% | 43.11% |
| model:ner-ru-gherman | eligible | Dates & times | 0/324 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Organizations | 6/366 | 1.64% | 18.85% | 0.00% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/54 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Customer & employee IDs | 66/1160 | 5.69% | 13.53% | 0.00% |
| model:ner-ru-gherman | eligible | Other sensitive attributes | 82/889 | 9.22% | 16.31% | 1.35% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 1/11 | 9.09% | 9.09% | 9.09% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 6/65 | 9.23% | 21.54% | 9.23% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 4/473 | 0.85% | 3.59% | 0.21% |
| model:ner-ru-yqelz | eligible | People's names | 3399/3854 | 88.19% | 89.65% | 81.58% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 5/1199 | 0.42% | 12.84% | 0.42% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 426/835 | 51.02% | 96.77% | 49.34% |
| model:ner-ru-yqelz | eligible | Dates & times | 3/324 | 0.93% | 2.47% | 0.93% |
| model:ner-ru-yqelz | eligible | Organizations | 187/366 | 51.09% | 72.13% | 45.36% |
| model:ner-ru-yqelz | eligible | Network identifiers | 0/54 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Customer & employee IDs | 26/1160 | 2.24% | 5.52% | 0.26% |
| model:ner-ru-yqelz | eligible | Other sensitive attributes | 190/889 | 21.37% | 39.26% | 15.64% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 6/11 | 54.55% | 90.91% | 54.55% |
| model:nuner-zero | eligible | Bank accounts & cards | 8/65 | 12.31% | 24.62% | 10.77% |
| model:nuner-zero | eligible | Documents & identifiers | 309/473 | 65.33% | 72.09% | 34.25% |
| model:nuner-zero | eligible | People's names | 3124/3854 | 81.06% | 83.32% | 53.04% |
| model:nuner-zero | eligible | Phone numbers & email | 1141/1199 | 95.16% | 99.08% | 56.55% |
| model:nuner-zero | eligible | Addresses & locations | 536/835 | 64.19% | 93.29% | 44.43% |
| model:nuner-zero | eligible | Dates & times | 291/324 | 89.81% | 96.60% | 80.86% |
| model:nuner-zero | eligible | Organizations | 242/366 | 66.12% | 90.44% | 16.12% |
| model:nuner-zero | eligible | Network identifiers | 51/54 | 94.44% | 96.30% | 94.44% |
| model:nuner-zero | eligible | Customer & employee IDs | 663/1160 | 57.16% | 63.79% | 56.64% |
| model:nuner-zero | eligible | Other sensitive attributes | 446/889 | 50.17% | 67.83% | 23.85% |
| model:nym-base | eligible | Passwords, keys & tokens | 7/11 | 63.64% | 100.00% | 63.64% |
| model:nym-base | eligible | Bank accounts & cards | 15/65 | 23.08% | 61.54% | 18.46% |
| model:nym-base | eligible | Documents & identifiers | 401/473 | 84.78% | 97.89% | 82.45% |
| model:nym-base | eligible | People's names | 2534/3854 | 65.75% | 97.95% | 91.52% |
| model:nym-base | eligible | Phone numbers & email | 993/1199 | 82.82% | 96.33% | 80.73% |
| model:nym-base | eligible | Addresses & locations | 405/835 | 48.50% | 93.77% | 46.47% |
| model:nym-base | eligible | Dates & times | 287/324 | 88.58% | 99.69% | 86.11% |
| model:nym-base | eligible | Organizations | 275/366 | 75.14% | 81.42% | 72.95% |
| model:nym-base | eligible | Network identifiers | 21/54 | 38.89% | 61.11% | 27.78% |
| model:nym-base | eligible | Customer & employee IDs | 375/1160 | 32.33% | 42.76% | 24.74% |
| model:nym-base | eligible | Other sensitive attributes | 280/889 | 31.50% | 44.88% | 27.78% |
| model:nym-base+ov100 | eligible | Passwords, keys & tokens | 7/11 | 63.64% | 100.00% | 63.64% |
| model:nym-base+ov100 | eligible | Bank accounts & cards | 15/65 | 23.08% | 53.85% | 21.54% |
| model:nym-base+ov100 | eligible | Documents & identifiers | 403/473 | 85.20% | 97.89% | 83.51% |
| model:nym-base+ov100 | eligible | People's names | 2554/3854 | 66.27% | 97.92% | 92.03% |
| model:nym-base+ov100 | eligible | Phone numbers & email | 987/1199 | 82.32% | 96.41% | 80.23% |
| model:nym-base+ov100 | eligible | Addresses & locations | 416/835 | 49.82% | 94.37% | 47.43% |
| model:nym-base+ov100 | eligible | Dates & times | 286/324 | 88.27% | 99.69% | 87.04% |
| model:nym-base+ov100 | eligible | Organizations | 272/366 | 74.32% | 81.15% | 71.58% |
| model:nym-base+ov100 | eligible | Network identifiers | 21/54 | 38.89% | 64.81% | 18.52% |
| model:nym-base+ov100 | eligible | Customer & employee IDs | 366/1160 | 31.55% | 43.19% | 24.57% |
| model:nym-base+ov100 | eligible | Other sensitive attributes | 289/889 | 32.51% | 45.78% | 27.67% |
| model:nym-base+sent300 | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 63.64% |
| model:nym-base+sent300 | eligible | Bank accounts & cards | 15/65 | 23.08% | 66.15% | 21.54% |
| model:nym-base+sent300 | eligible | Documents & identifiers | 402/473 | 84.99% | 97.89% | 83.09% |
| model:nym-base+sent300 | eligible | People's names | 2524/3854 | 65.49% | 98.50% | 92.24% |
| model:nym-base+sent300 | eligible | Phone numbers & email | 1004/1199 | 83.74% | 97.16% | 82.57% |
| model:nym-base+sent300 | eligible | Addresses & locations | 418/835 | 50.06% | 96.29% | 48.38% |
| model:nym-base+sent300 | eligible | Dates & times | 289/324 | 89.20% | 99.69% | 88.89% |
| model:nym-base+sent300 | eligible | Organizations | 293/366 | 80.05% | 87.43% | 77.87% |
| model:nym-base+sent300 | eligible | Network identifiers | 43/54 | 79.63% | 96.30% | 68.52% |
| model:nym-base+sent300 | eligible | Customer & employee IDs | 386/1160 | 33.28% | 44.91% | 25.17% |
| model:nym-base+sent300 | eligible | Other sensitive attributes | 282/889 | 31.72% | 45.89% | 27.90% |
| model:nym-small | eligible | Passwords, keys & tokens | 7/11 | 63.64% | 90.91% | 63.64% |
| model:nym-small | eligible | Bank accounts & cards | 16/65 | 24.62% | 75.38% | 20.00% |
| model:nym-small | eligible | Documents & identifiers | 412/473 | 87.10% | 98.10% | 85.62% |
| model:nym-small | eligible | People's names | 2461/3854 | 63.86% | 95.12% | 90.97% |
| model:nym-small | eligible | Phone numbers & email | 1028/1199 | 85.74% | 94.16% | 84.82% |
| model:nym-small | eligible | Addresses & locations | 413/835 | 49.46% | 95.57% | 48.14% |
| model:nym-small | eligible | Dates & times | 271/324 | 83.64% | 93.83% | 80.56% |
| model:nym-small | eligible | Organizations | 270/366 | 73.77% | 83.33% | 74.86% |
| model:nym-small | eligible | Network identifiers | 28/54 | 51.85% | 62.96% | 38.89% |
| model:nym-small | eligible | Customer & employee IDs | 372/1160 | 32.07% | 43.28% | 24.14% |
| model:nym-small | eligible | Other sensitive attributes | 251/889 | 28.23% | 42.63% | 22.27% |
| model:openai-base | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:openai-base | eligible | Bank accounts & cards | 34/65 | 52.31% | 63.08% | 49.23% |
| model:openai-base | eligible | Documents & identifiers | 394/473 | 83.30% | 90.91% | 82.66% |
| model:openai-base | eligible | People's names | 3546/3854 | 92.01% | 93.07% | 90.11% |
| model:openai-base | eligible | Phone numbers & email | 1138/1199 | 94.91% | 97.41% | 94.66% |
| model:openai-base | eligible | Addresses & locations | 611/835 | 73.17% | 76.41% | 71.98% |
| model:openai-base | eligible | Dates & times | 306/324 | 94.44% | 99.69% | 94.14% |
| model:openai-base | eligible | Organizations | 53/366 | 14.48% | 23.77% | 13.93% |
| model:openai-base | eligible | Network identifiers | 34/54 | 62.96% | 74.07% | 57.41% |
| model:openai-base | eligible | Customer & employee IDs | 845/1160 | 72.84% | 81.29% | 68.36% |
| model:openai-base | eligible | Other sensitive attributes | 133/889 | 14.96% | 19.91% | 13.39% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 54.55% |
| model:openmed-multilingual | eligible | Bank accounts & cards | 15/65 | 23.08% | 49.23% | 16.92% |
| model:openmed-multilingual | eligible | Documents & identifiers | 356/473 | 75.26% | 88.37% | 70.82% |
| model:openmed-multilingual | eligible | People's names | 2199/3854 | 57.06% | 84.09% | 58.87% |
| model:openmed-multilingual | eligible | Phone numbers & email | 1065/1199 | 88.82% | 98.50% | 88.24% |
| model:openmed-multilingual | eligible | Addresses & locations | 246/835 | 29.46% | 79.88% | 24.91% |
| model:openmed-multilingual | eligible | Dates & times | 279/324 | 86.11% | 96.91% | 84.88% |
| model:openmed-multilingual | eligible | Organizations | 50/366 | 13.66% | 36.61% | 8.74% |
| model:openmed-multilingual | eligible | Network identifiers | 48/54 | 88.89% | 100.00% | 81.48% |
| model:openmed-multilingual | eligible | Customer & employee IDs | 470/1160 | 40.52% | 68.19% | 30.78% |
| model:openmed-multilingual | eligible | Other sensitive attributes | 178/889 | 20.02% | 39.48% | 13.84% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 36.36% |
| model:openmed-nemotron | eligible | Bank accounts & cards | 11/65 | 16.92% | 46.15% | 13.85% |
| model:openmed-nemotron | eligible | Documents & identifiers | 116/473 | 24.52% | 36.58% | 9.09% |
| model:openmed-nemotron | eligible | People's names | 2333/3854 | 60.53% | 90.50% | 59.94% |
| model:openmed-nemotron | eligible | Phone numbers & email | 992/1199 | 82.74% | 96.58% | 80.73% |
| model:openmed-nemotron | eligible | Addresses & locations | 318/835 | 38.08% | 83.35% | 31.74% |
| model:openmed-nemotron | eligible | Dates & times | 278/324 | 85.80% | 92.59% | 83.64% |
| model:openmed-nemotron | eligible | Organizations | 52/366 | 14.21% | 45.36% | 9.02% |
| model:openmed-nemotron | eligible | Network identifiers | 39/54 | 72.22% | 87.04% | 70.37% |
| model:openmed-nemotron | eligible | Customer & employee IDs | 314/1160 | 27.07% | 46.03% | 16.64% |
| model:openmed-nemotron | eligible | Other sensitive attributes | 158/889 | 17.77% | 28.91% | 10.46% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 43/65 | 66.15% | 87.69% | 63.08% |
| model:opf-kz-ru | eligible | Documents & identifiers | 419/473 | 88.58% | 97.89% | 89.22% |
| model:opf-kz-ru | eligible | People's names | 3185/3854 | 82.64% | 85.60% | 78.05% |
| model:opf-kz-ru | eligible | Phone numbers & email | 1142/1199 | 95.25% | 98.17% | 94.58% |
| model:opf-kz-ru | eligible | Addresses & locations | 373/835 | 44.67% | 71.50% | 42.63% |
| model:opf-kz-ru | eligible | Dates & times | 308/324 | 95.06% | 98.46% | 92.59% |
| model:opf-kz-ru | eligible | Organizations | 38/366 | 10.38% | 17.21% | 8.74% |
| model:opf-kz-ru | eligible | Network identifiers | 32/54 | 59.26% | 90.74% | 44.44% |
| model:opf-kz-ru | eligible | Customer & employee IDs | 969/1160 | 83.53% | 91.81% | 75.52% |
| model:opf-kz-ru | eligible | Other sensitive attributes | 151/889 | 16.99% | 24.30% | 12.26% |
| model:opf-ru | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:opf-ru | eligible | Bank accounts & cards | 10/65 | 15.38% | 55.38% | 10.77% |
| model:opf-ru | eligible | Documents & identifiers | 322/473 | 68.08% | 92.60% | 59.62% |
| model:opf-ru | eligible | People's names | 3457/3854 | 89.70% | 95.82% | 78.72% |
| model:opf-ru | eligible | Phone numbers & email | 1095/1199 | 91.33% | 97.25% | 90.58% |
| model:opf-ru | eligible | Addresses & locations | 191/835 | 22.87% | 68.98% | 19.64% |
| model:opf-ru | eligible | Dates & times | 272/324 | 83.95% | 95.37% | 83.64% |
| model:opf-ru | eligible | Organizations | 30/366 | 8.20% | 31.97% | 7.10% |
| model:opf-ru | eligible | Network identifiers | 5/54 | 9.26% | 57.41% | 0.00% |
| model:opf-ru | eligible | Customer & employee IDs | 343/1160 | 29.57% | 73.97% | 16.55% |
| model:opf-ru | eligible | Other sensitive attributes | 94/889 | 10.57% | 21.37% | 4.16% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 11/65 | 16.92% | 43.08% | 10.77% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 340/473 | 71.88% | 91.75% | 68.71% |
| model:opf-ru-v2 | eligible | People's names | 3383/3854 | 87.78% | 90.11% | 83.19% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 1103/1199 | 91.99% | 96.58% | 91.83% |
| model:opf-ru-v2 | eligible | Addresses & locations | 543/835 | 65.03% | 71.26% | 62.75% |
| model:opf-ru-v2 | eligible | Dates & times | 0/324 | 0.00% | 4.32% | 0.00% |
| model:opf-ru-v2 | eligible | Organizations | 49/366 | 13.39% | 26.23% | 11.20% |
| model:opf-ru-v2 | eligible | Network identifiers | 44/54 | 81.48% | 92.59% | 77.78% |
| model:opf-ru-v2 | eligible | Customer & employee IDs | 309/1160 | 26.64% | 59.31% | 17.67% |
| model:opf-ru-v2 | eligible | Other sensitive attributes | 64/889 | 7.20% | 13.50% | 3.26% |
| model:opf-ru-v2+ov100 | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:opf-ru-v2+ov100 | eligible | Bank accounts & cards | 10/65 | 15.38% | 38.46% | 10.77% |
| model:opf-ru-v2+ov100 | eligible | Documents & identifiers | 337/473 | 71.25% | 91.97% | 70.82% |
| model:opf-ru-v2+ov100 | eligible | People's names | 3428/3854 | 88.95% | 90.87% | 84.15% |
| model:opf-ru-v2+ov100 | eligible | Phone numbers & email | 1107/1199 | 92.33% | 96.83% | 91.66% |
| model:opf-ru-v2+ov100 | eligible | Addresses & locations | 550/835 | 65.87% | 71.74% | 62.99% |
| model:opf-ru-v2+ov100 | eligible | Dates & times | 0/324 | 0.00% | 4.63% | 0.00% |
| model:opf-ru-v2+ov100 | eligible | Organizations | 43/366 | 11.75% | 26.78% | 10.11% |
| model:opf-ru-v2+ov100 | eligible | Network identifiers | 44/54 | 81.48% | 94.44% | 75.93% |
| model:opf-ru-v2+ov100 | eligible | Customer & employee IDs | 320/1160 | 27.59% | 59.48% | 18.45% |
| model:opf-ru-v2+ov100 | eligible | Other sensitive attributes | 69/889 | 7.76% | 15.64% | 4.05% |
| model:opf-ru-v2+sent300 | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:opf-ru-v2+sent300 | eligible | Bank accounts & cards | 10/65 | 15.38% | 52.31% | 15.38% |
| model:opf-ru-v2+sent300 | eligible | Documents & identifiers | 349/473 | 73.78% | 93.23% | 72.30% |
| model:opf-ru-v2+sent300 | eligible | People's names | 3459/3854 | 89.75% | 91.52% | 85.47% |
| model:opf-ru-v2+sent300 | eligible | Phone numbers & email | 1115/1199 | 92.99% | 97.00% | 92.33% |
| model:opf-ru-v2+sent300 | eligible | Addresses & locations | 507/835 | 60.72% | 71.62% | 57.49% |
| model:opf-ru-v2+sent300 | eligible | Dates & times | 2/324 | 0.62% | 2.16% | 0.31% |
| model:opf-ru-v2+sent300 | eligible | Organizations | 44/366 | 12.02% | 28.96% | 11.20% |
| model:opf-ru-v2+sent300 | eligible | Network identifiers | 47/54 | 87.04% | 96.30% | 83.33% |
| model:opf-ru-v2+sent300 | eligible | Customer & employee IDs | 329/1160 | 28.36% | 59.48% | 19.31% |
| model:opf-ru-v2+sent300 | eligible | Other sensitive attributes | 74/889 | 8.32% | 15.52% | 4.72% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 7/11 | 63.64% | 100.00% | 45.45% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 5/65 | 7.69% | 16.92% | 4.62% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 269/473 | 56.87% | 67.23% | 47.36% |
| model:pii-shield-onnx | eligible | People's names | 2352/3854 | 61.03% | 71.46% | 53.32% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 1127/1199 | 93.99% | 98.83% | 91.41% |
| model:pii-shield-onnx | eligible | Addresses & locations | 332/835 | 39.76% | 79.88% | 37.37% |
| model:pii-shield-onnx | eligible | Dates & times | 208/324 | 64.20% | 87.35% | 63.58% |
| model:pii-shield-onnx | eligible | Organizations | 37/366 | 10.11% | 20.49% | 8.74% |
| model:pii-shield-onnx | eligible | Network identifiers | 27/54 | 50.00% | 77.78% | 38.89% |
| model:pii-shield-onnx | eligible | Customer & employee IDs | 645/1160 | 55.60% | 78.79% | 42.84% |
| model:pii-shield-onnx | eligible | Other sensitive attributes | 115/889 | 12.94% | 23.62% | 7.65% |
| model:pplx | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:pplx | eligible | Bank accounts & cards | 33/65 | 50.77% | 95.38% | 49.23% |
| model:pplx | eligible | Documents & identifiers | 436/473 | 92.18% | 99.79% | 92.18% |
| model:pplx | eligible | People's names | 3799/3854 | 98.57% | 99.87% | 97.33% |
| model:pplx | eligible | Phone numbers & email | 1163/1199 | 97.00% | 99.42% | 96.91% |
| model:pplx | eligible | Addresses & locations | 672/835 | 80.48% | 85.15% | 80.00% |
| model:pplx | eligible | Dates & times | 314/324 | 96.91% | 100.00% | 96.60% |
| model:pplx | eligible | Organizations | 30/366 | 8.20% | 9.56% | 8.20% |
| model:pplx | eligible | Network identifiers | 50/54 | 92.59% | 98.15% | 92.59% |
| model:pplx | eligible | Customer & employee IDs | 1105/1160 | 95.26% | 97.84% | 95.17% |
| model:pplx | eligible | Other sensitive attributes | 431/889 | 48.48% | 56.81% | 48.03% |
| model:pplx+ov100 | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:pplx+ov100 | eligible | Bank accounts & cards | 33/65 | 50.77% | 92.31% | 49.23% |
| model:pplx+ov100 | eligible | Documents & identifiers | 435/473 | 91.97% | 99.37% | 91.97% |
| model:pplx+ov100 | eligible | People's names | 3799/3854 | 98.57% | 99.90% | 97.33% |
| model:pplx+ov100 | eligible | Phone numbers & email | 1167/1199 | 97.33% | 99.75% | 97.25% |
| model:pplx+ov100 | eligible | Addresses & locations | 678/835 | 81.20% | 86.59% | 80.72% |
| model:pplx+ov100 | eligible | Dates & times | 309/324 | 95.37% | 100.00% | 95.37% |
| model:pplx+ov100 | eligible | Organizations | 34/366 | 9.29% | 10.38% | 9.29% |
| model:pplx+ov100 | eligible | Network identifiers | 49/54 | 90.74% | 100.00% | 90.74% |
| model:pplx+ov100 | eligible | Customer & employee IDs | 1097/1160 | 94.57% | 97.93% | 94.40% |
| model:pplx+ov100 | eligible | Other sensitive attributes | 444/889 | 49.94% | 58.72% | 49.27% |
| model:pplx+sent300 | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 72.73% |
| model:pplx+sent300 | eligible | Bank accounts & cards | 30/65 | 46.15% | 87.69% | 44.62% |
| model:pplx+sent300 | eligible | Documents & identifiers | 424/473 | 89.64% | 99.37% | 89.64% |
| model:pplx+sent300 | eligible | People's names | 3777/3854 | 98.00% | 99.84% | 96.37% |
| model:pplx+sent300 | eligible | Phone numbers & email | 1139/1199 | 95.00% | 99.50% | 94.91% |
| model:pplx+sent300 | eligible | Addresses & locations | 635/835 | 76.05% | 91.62% | 73.41% |
| model:pplx+sent300 | eligible | Dates & times | 295/324 | 91.05% | 100.00% | 91.05% |
| model:pplx+sent300 | eligible | Organizations | 34/366 | 9.29% | 15.30% | 9.02% |
| model:pplx+sent300 | eligible | Network identifiers | 49/54 | 90.74% | 100.00% | 90.74% |
| model:pplx+sent300 | eligible | Customer & employee IDs | 1057/1160 | 91.12% | 97.24% | 90.78% |
| model:pplx+sent300 | eligible | Other sensitive attributes | 334/889 | 37.57% | 45.33% | 37.23% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 5/11 | 45.45% | 100.00% | 18.18% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 11/65 | 16.92% | 72.31% | 12.31% |
| model:ru-legal-ner | eligible | Documents & identifiers | 355/473 | 75.05% | 93.02% | 62.37% |
| model:ru-legal-ner | eligible | People's names | 3044/3854 | 78.98% | 84.46% | 75.06% |
| model:ru-legal-ner | eligible | Phone numbers & email | 609/1199 | 50.79% | 97.08% | 49.79% |
| model:ru-legal-ner | eligible | Addresses & locations | 456/835 | 54.61% | 69.10% | 51.14% |
| model:ru-legal-ner | eligible | Dates & times | 292/324 | 90.12% | 97.84% | 90.12% |
| model:ru-legal-ner | eligible | Organizations | 226/366 | 61.75% | 77.05% | 57.65% |
| model:ru-legal-ner | eligible | Network identifiers | 7/54 | 12.96% | 46.30% | 3.70% |
| model:ru-legal-ner | eligible | Customer & employee IDs | 260/1160 | 22.41% | 67.67% | 9.91% |
| model:ru-legal-ner | eligible | Other sensitive attributes | 118/889 | 13.27% | 26.66% | 6.30% |
| model:ru-legal-ner+ov100 | eligible | Passwords, keys & tokens | 4/11 | 36.36% | 100.00% | 18.18% |
| model:ru-legal-ner+ov100 | eligible | Bank accounts & cards | 10/65 | 15.38% | 67.69% | 6.15% |
| model:ru-legal-ner+ov100 | eligible | Documents & identifiers | 359/473 | 75.90% | 93.45% | 67.44% |
| model:ru-legal-ner+ov100 | eligible | People's names | 3112/3854 | 80.75% | 86.07% | 76.93% |
| model:ru-legal-ner+ov100 | eligible | Phone numbers & email | 621/1199 | 51.79% | 97.08% | 50.46% |
| model:ru-legal-ner+ov100 | eligible | Addresses & locations | 455/835 | 54.49% | 68.98% | 50.18% |
| model:ru-legal-ner+ov100 | eligible | Dates & times | 298/324 | 91.98% | 97.84% | 91.67% |
| model:ru-legal-ner+ov100 | eligible | Organizations | 222/366 | 60.66% | 76.23% | 57.10% |
| model:ru-legal-ner+ov100 | eligible | Network identifiers | 7/54 | 12.96% | 53.70% | 3.70% |
| model:ru-legal-ner+ov100 | eligible | Customer & employee IDs | 276/1160 | 23.79% | 71.38% | 10.95% |
| model:ru-legal-ner+ov100 | eligible | Other sensitive attributes | 129/889 | 14.51% | 28.57% | 8.21% |
| model:ru-legal-ner+sent300 | eligible | Passwords, keys & tokens | 5/11 | 45.45% | 100.00% | 27.27% |
| model:ru-legal-ner+sent300 | eligible | Bank accounts & cards | 13/65 | 20.00% | 80.00% | 13.85% |
| model:ru-legal-ner+sent300 | eligible | Documents & identifiers | 355/473 | 75.05% | 92.39% | 65.33% |
| model:ru-legal-ner+sent300 | eligible | People's names | 3242/3854 | 84.12% | 88.45% | 79.89% |
| model:ru-legal-ner+sent300 | eligible | Phone numbers & email | 654/1199 | 54.55% | 98.50% | 53.63% |
| model:ru-legal-ner+sent300 | eligible | Addresses & locations | 421/835 | 50.42% | 70.30% | 47.07% |
| model:ru-legal-ner+sent300 | eligible | Dates & times | 301/324 | 92.90% | 98.77% | 92.90% |
| model:ru-legal-ner+sent300 | eligible | Organizations | 233/366 | 63.66% | 77.05% | 60.66% |
| model:ru-legal-ner+sent300 | eligible | Network identifiers | 9/54 | 16.67% | 51.85% | 0.00% |
| model:ru-legal-ner+sent300 | eligible | Customer & employee IDs | 291/1160 | 25.09% | 67.33% | 11.90% |
| model:ru-legal-ner+sent300 | eligible | Other sensitive attributes | 140/889 | 15.75% | 31.95% | 7.76% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 6/11 | 54.55% | 63.64% | 54.55% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 31/65 | 47.69% | 83.08% | 47.69% |
| model:ru-pii-ner | eligible | Documents & identifiers | 352/473 | 74.42% | 83.51% | 74.21% |
| model:ru-pii-ner | eligible | People's names | 3790/3854 | 98.34% | 98.57% | 96.24% |
| model:ru-pii-ner | eligible | Phone numbers & email | 1047/1199 | 87.32% | 89.49% | 87.24% |
| model:ru-pii-ner | eligible | Addresses & locations | 444/835 | 53.17% | 56.05% | 52.93% |
| model:ru-pii-ner | eligible | Dates & times | 293/324 | 90.43% | 98.77% | 90.43% |
| model:ru-pii-ner | eligible | Organizations | 17/366 | 4.64% | 4.64% | 4.64% |
| model:ru-pii-ner | eligible | Network identifiers | 26/54 | 48.15% | 50.00% | 48.15% |
| model:ru-pii-ner | eligible | Customer & employee IDs | 892/1160 | 76.90% | 81.72% | 72.33% |
| model:ru-pii-ner | eligible | Other sensitive attributes | 43/889 | 4.84% | 7.20% | 3.15% |
| model:rules-ru | eligible | Passwords, keys & tokens | 2/11 | 18.18% | 18.18% | 18.18% |
| model:rules-ru | eligible | Bank accounts & cards | 2/65 | 3.08% | 3.08% | 3.08% |
| model:rules-ru | eligible | Documents & identifiers | 126/473 | 26.64% | 26.64% | 26.64% |
| model:rules-ru | eligible | People's names | 25/3854 | 0.65% | 0.75% | 0.65% |
| model:rules-ru | eligible | Phone numbers & email | 1127/1199 | 93.99% | 96.16% | 93.99% |
| model:rules-ru | eligible | Addresses & locations | 0/835 | 0.00% | 0.12% | 0.00% |
| model:rules-ru | eligible | Dates & times | 0/324 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Organizations | 166/366 | 45.36% | 46.99% | 45.36% |
| model:rules-ru | eligible | Network identifiers | 41/54 | 75.93% | 85.19% | 75.93% |
| model:rules-ru | eligible | Customer & employee IDs | 168/1160 | 14.48% | 15.86% | 14.48% |
| model:rules-ru | eligible | Other sensitive attributes | 6/889 | 0.67% | 1.57% | 0.67% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/11 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 1/65 | 1.54% | 1.54% | 1.54% |
| model:spacy-alrosait | eligible | Documents & identifiers | 1/473 | 0.21% | 0.63% | 0.21% |
| model:spacy-alrosait | eligible | People's names | 3284/3854 | 85.21% | 86.07% | 85.21% |
| model:spacy-alrosait | eligible | Phone numbers & email | 1/1199 | 0.08% | 1.25% | 0.08% |
| model:spacy-alrosait | eligible | Addresses & locations | 535/835 | 64.07% | 84.67% | 63.35% |
| model:spacy-alrosait | eligible | Dates & times | 0/324 | 0.00% | 0.62% | 0.00% |
| model:spacy-alrosait | eligible | Organizations | 2/366 | 0.55% | 12.84% | 0.55% |
| model:spacy-alrosait | eligible | Network identifiers | 0/54 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Customer & employee IDs | 1/1160 | 0.09% | 0.09% | 0.09% |
| model:spacy-alrosait | eligible | Other sensitive attributes | 57/889 | 6.41% | 9.90% | 6.41% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 0/11 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 0/65 | 0.00% | 4.62% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 16/473 | 3.38% | 3.81% | 3.38% |
| model:spacy-ru-lg | eligible | People's names | 2996/3854 | 77.74% | 81.91% | 71.59% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 37/1199 | 3.09% | 4.50% | 3.09% |
| model:spacy-ru-lg | eligible | Addresses & locations | 399/835 | 47.78% | 94.25% | 47.43% |
| model:spacy-ru-lg | eligible | Dates & times | 4/324 | 1.23% | 1.23% | 1.23% |
| model:spacy-ru-lg | eligible | Organizations | 274/366 | 74.86% | 87.43% | 74.04% |
| model:spacy-ru-lg | eligible | Network identifiers | 2/54 | 3.70% | 3.70% | 3.70% |
| model:spacy-ru-lg | eligible | Customer & employee IDs | 69/1160 | 5.95% | 6.38% | 5.95% |
| model:spacy-ru-lg | eligible | Other sensitive attributes | 91/889 | 10.24% | 17.89% | 10.12% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 1/11 | 9.09% | 45.45% | 9.09% |
| model:stanza-ru | eligible | Bank accounts & cards | 2/65 | 3.08% | 10.77% | 3.08% |
| model:stanza-ru | eligible | Documents & identifiers | 28/473 | 5.92% | 6.98% | 5.92% |
| model:stanza-ru | eligible | People's names | 3756/3854 | 97.46% | 98.08% | 97.12% |
| model:stanza-ru | eligible | Phone numbers & email | 93/1199 | 7.76% | 9.26% | 7.76% |
| model:stanza-ru | eligible | Addresses & locations | 397/835 | 47.54% | 95.09% | 47.54% |
| model:stanza-ru | eligible | Dates & times | 6/324 | 1.85% | 1.85% | 1.85% |
| model:stanza-ru | eligible | Organizations | 259/366 | 70.77% | 88.80% | 70.77% |
| model:stanza-ru | eligible | Network identifiers | 0/54 | 0.00% | 0.00% | 0.00% |
| model:stanza-ru | eligible | Customer & employee IDs | 120/1160 | 10.34% | 45.43% | 9.66% |
| model:stanza-ru | eligible | Other sensitive attributes | 150/889 | 16.87% | 28.57% | 16.76% |
| model:traciora | eligible | Passwords, keys & tokens | 8/11 | 72.73% | 100.00% | 54.55% |
| model:traciora | eligible | Bank accounts & cards | 6/65 | 9.23% | 23.08% | 10.77% |
| model:traciora | eligible | Documents & identifiers | 255/473 | 53.91% | 74.84% | 38.48% |
| model:traciora | eligible | People's names | 3312/3854 | 85.94% | 88.66% | 80.88% |
| model:traciora | eligible | Phone numbers & email | 1103/1199 | 91.99% | 98.33% | 91.33% |
| model:traciora | eligible | Addresses & locations | 596/835 | 71.38% | 74.25% | 69.70% |
| model:traciora | eligible | Dates & times | 0/324 | 0.00% | 8.33% | 0.00% |
| model:traciora | eligible | Organizations | 42/366 | 11.48% | 29.78% | 10.11% |
| model:traciora | eligible | Network identifiers | 29/54 | 53.70% | 77.78% | 53.70% |
| model:traciora | eligible | Customer & employee IDs | 350/1160 | 30.17% | 48.45% | 17.41% |
| model:traciora | eligible | Other sensitive attributes | 79/889 | 8.89% | 15.97% | 4.27% |
