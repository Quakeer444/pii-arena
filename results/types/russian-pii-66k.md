# russian-pii-66k: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/russian-pii-66k.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 184/194 | 94.85% | 98.45% | 93.81% |
| composition:fastino | eligible | Logins & usernames | 305/311 | 98.07% | 98.07% | 98.07% |
| composition:fastino | eligible | Bank accounts & cards | 424/448 | 94.64% | 94.64% | 94.64% |
| composition:fastino | eligible | Documents & identifiers | 746/784 | 95.15% | 95.15% | 95.15% |
| composition:fastino | eligible | People's names | 1099/1151 | 95.48% | 95.48% | 95.48% |
| composition:fastino | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| composition:fastino | eligible | Addresses & locations | 659/901 | 73.14% | 86.68% | 73.14% |
| composition:fastino | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Logins & usernames | 310/311 | 99.68% | 99.68% | 99.68% |
| composition:pplx | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Documents & identifiers | 784/784 | 100.00% | 100.00% | 99.87% |
| composition:pplx | eligible | People's names | 1147/1151 | 99.65% | 99.65% | 99.30% |
| composition:pplx | eligible | Phone numbers & email | 792/793 | 99.87% | 100.00% | 99.37% |
| composition:pplx | eligible | Addresses & locations | 808/901 | 89.68% | 99.33% | 89.46% |
| composition:pplx | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 98.65% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Logins & usernames | 311/311 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Documents & identifiers | 784/784 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | People's names | 1149/1151 | 99.83% | 99.83% | 99.65% |
| composition:pplx+fastino | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Addresses & locations | 857/901 | 95.12% | 100.00% | 95.01% |
| composition:pplx+fastino | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Logins & usernames | 311/311 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 784/784 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | People's names | 1151/1151 | 100.00% | 100.00% | 99.91% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 863/901 | 95.78% | 100.00% | 95.78% |
| composition:pplx+fastino+bardsai | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Logins & usernames | 311/311 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 784/784 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 1151/1151 | 100.00% | 100.00% | 99.91% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 866/901 | 96.12% | 100.00% | 95.89% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Logins & usernames | 311/311 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 784/784 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | People's names | 1151/1151 | 100.00% | 100.00% | 99.91% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 860/901 | 95.45% | 100.00% | 95.12% |
| composition:pplx+fastino+mmbert | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 100.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Logins & usernames | 309/311 | 99.36% | 99.36% | 99.04% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 97.54% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 782/784 | 99.74% | 100.00% | 100.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 1149/1151 | 99.83% | 99.83% | 99.74% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 713/901 | 79.13% | 98.67% | 78.69% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 98.65% |
| model:apararti | eligible | Passwords, keys & tokens | 190/194 | 97.94% | 99.48% | 97.42% |
| model:apararti | eligible | Logins & usernames | 231/311 | 74.28% | 74.28% | 65.59% |
| model:apararti | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 99.33% |
| model:apararti | eligible | Documents & identifiers | 747/784 | 95.28% | 100.00% | 97.19% |
| model:apararti | eligible | People's names | 979/1151 | 85.06% | 85.06% | 81.06% |
| model:apararti | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 99.87% |
| model:apararti | eligible | Addresses & locations | 643/901 | 71.37% | 80.36% | 69.81% |
| model:apararti | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 166/194 | 85.57% | 95.88% | 79.38% |
| model:bardsai-eu | eligible | Logins & usernames | 281/311 | 90.35% | 90.35% | 82.64% |
| model:bardsai-eu | eligible | Bank accounts & cards | 421/448 | 93.97% | 93.97% | 56.70% |
| model:bardsai-eu | eligible | Documents & identifiers | 670/784 | 85.46% | 96.17% | 78.95% |
| model:bardsai-eu | eligible | People's names | 1146/1151 | 99.57% | 99.57% | 98.96% |
| model:bardsai-eu | eligible | Phone numbers & email | 427/793 | 53.85% | 99.87% | 49.31% |
| model:bardsai-eu | eligible | Addresses & locations | 592/901 | 65.70% | 93.12% | 62.49% |
| model:bardsai-eu | eligible | Dates & times | 217/223 | 97.31% | 99.10% | 97.31% |
| model:betterleaks | eligible | Passwords, keys & tokens | 0/194 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Logins & usernames | 0/311 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Bank accounts & cards | 0/448 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Documents & identifiers | 0/784 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | People's names | 0/1151 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Phone numbers & email | 0/793 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Addresses & locations | 0/901 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 1/194 | 0.52% | 0.52% | 0.00% |
| model:davlan-mbert | eligible | Logins & usernames | 8/311 | 2.57% | 2.57% | 0.64% |
| model:davlan-mbert | eligible | Bank accounts & cards | 0/448 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 0/784 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | People's names | 1142/1151 | 99.22% | 99.22% | 98.52% |
| model:davlan-mbert | eligible | Phone numbers & email | 0/793 | 0.00% | 0.63% | 0.00% |
| model:davlan-mbert | eligible | Addresses & locations | 351/901 | 38.96% | 65.15% | 38.51% |
| model:davlan-mbert | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/194 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Logins & usernames | 43/311 | 13.83% | 13.83% | 5.79% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 0/448 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Documents & identifiers | 0/784 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 1146/1151 | 99.57% | 99.57% | 98.87% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/793 | 0.00% | 0.50% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 515/901 | 57.16% | 75.47% | 51.05% |
| model:davlan-xlmr | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 192/194 | 98.97% | 100.00% | 98.97% |
| model:fef2-secret-ru | eligible | Logins & usernames | 265/311 | 85.21% | 85.21% | 80.06% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 391/448 | 87.28% | 87.28% | 49.11% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 600/784 | 76.53% | 90.31% | 73.72% |
| model:fef2-secret-ru | eligible | People's names | 1128/1151 | 98.00% | 98.00% | 97.57% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 480/793 | 60.53% | 77.18% | 58.39% |
| model:fef2-secret-ru | eligible | Addresses & locations | 176/901 | 19.53% | 66.81% | 16.32% |
| model:fef2-secret-ru | eligible | Dates & times | 4/223 | 1.79% | 5.38% | 1.79% |
| model:gitleaks | eligible | Passwords, keys & tokens | 0/194 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Logins & usernames | 0/311 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Bank accounts & cards | 0/448 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Documents & identifiers | 0/784 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | People's names | 0/1151 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Phone numbers & email | 0/793 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Addresses & locations | 0/901 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 19/194 | 9.79% | 15.98% | 9.79% |
| model:gliner-multi-v21 | eligible | Logins & usernames | 272/311 | 87.46% | 87.46% | 87.46% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 57/448 | 12.72% | 12.72% | 12.72% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 170/784 | 21.68% | 21.68% | 21.68% |
| model:gliner-multi-v21 | eligible | People's names | 1132/1151 | 98.35% | 98.35% | 98.35% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 269/793 | 33.92% | 70.24% | 30.90% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 493/901 | 54.72% | 76.91% | 54.72% |
| model:gliner-multi-v21 | eligible | Dates & times | 221/223 | 99.10% | 99.10% | 99.10% |
| model:gliner-multi-v21-ru | eligible | Passwords, keys & tokens | 51/194 | 26.29% | 28.87% | 25.77% |
| model:gliner-multi-v21-ru | eligible | Logins & usernames | 277/311 | 89.07% | 89.07% | 89.07% |
| model:gliner-multi-v21-ru | eligible | Bank accounts & cards | 138/448 | 30.80% | 30.80% | 30.80% |
| model:gliner-multi-v21-ru | eligible | Documents & identifiers | 279/784 | 35.59% | 35.59% | 35.59% |
| model:gliner-multi-v21-ru | eligible | People's names | 1139/1151 | 98.96% | 98.96% | 98.96% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 282/793 | 35.56% | 73.27% | 31.53% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 534/901 | 59.27% | 83.68% | 59.27% |
| model:gliner-multi-v21-ru | eligible | Dates & times | 216/223 | 96.86% | 96.86% | 96.86% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 100.00% |
| model:gliner-nvidia | eligible | Logins & usernames | 309/311 | 99.36% | 99.36% | 99.36% |
| model:gliner-nvidia | eligible | Bank accounts & cards | 387/448 | 86.38% | 86.38% | 86.38% |
| model:gliner-nvidia | eligible | Documents & identifiers | 720/784 | 91.84% | 91.96% | 91.84% |
| model:gliner-nvidia | eligible | People's names | 1146/1151 | 99.57% | 99.57% | 99.57% |
| model:gliner-nvidia | eligible | Phone numbers & email | 792/793 | 99.87% | 99.87% | 99.87% |
| model:gliner-nvidia | eligible | Addresses & locations | 606/901 | 67.26% | 93.67% | 67.26% |
| model:gliner-nvidia | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:gliner-nvidia-ru | eligible | Passwords, keys & tokens | 193/194 | 99.48% | 99.48% | 99.48% |
| model:gliner-nvidia-ru | eligible | Logins & usernames | 276/311 | 88.75% | 88.75% | 88.75% |
| model:gliner-nvidia-ru | eligible | Bank accounts & cards | 429/448 | 95.76% | 95.76% | 95.76% |
| model:gliner-nvidia-ru | eligible | Documents & identifiers | 763/784 | 97.32% | 97.32% | 97.32% |
| model:gliner-nvidia-ru | eligible | People's names | 1143/1151 | 99.30% | 99.30% | 99.30% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 788/793 | 99.37% | 99.37% | 99.37% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 603/901 | 66.93% | 91.23% | 66.93% |
| model:gliner-nvidia-ru | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 102/194 | 52.58% | 58.25% | 52.06% |
| model:gliner-pii-base | eligible | Logins & usernames | 270/311 | 86.82% | 86.82% | 86.82% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 93/448 | 20.76% | 20.76% | 20.76% |
| model:gliner-pii-base | eligible | Documents & identifiers | 34/784 | 4.34% | 4.34% | 4.34% |
| model:gliner-pii-base | eligible | People's names | 381/1151 | 33.10% | 33.10% | 33.10% |
| model:gliner-pii-base | eligible | Phone numbers & email | 752/793 | 94.83% | 94.83% | 94.83% |
| model:gliner-pii-base | eligible | Addresses & locations | 151/901 | 16.76% | 33.63% | 16.76% |
| model:gliner-pii-base | eligible | Dates & times | 100/223 | 44.84% | 44.84% | 44.84% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 143/194 | 73.71% | 87.63% | 73.20% |
| model:gliner-pii-edge | eligible | Logins & usernames | 306/311 | 98.39% | 98.39% | 98.39% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 408/784 | 52.04% | 54.34% | 51.91% |
| model:gliner-pii-edge | eligible | People's names | 1035/1151 | 89.92% | 89.92% | 89.92% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 768/793 | 96.85% | 97.10% | 96.85% |
| model:gliner-pii-edge | eligible | Addresses & locations | 257/901 | 28.52% | 49.28% | 28.52% |
| model:gliner-pii-edge | eligible | Dates & times | 187/223 | 83.86% | 83.86% | 83.86% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 153/194 | 78.87% | 88.66% | 78.87% |
| model:gliner-stream-pii | eligible | Logins & usernames | 279/311 | 89.71% | 89.71% | 89.71% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 376/448 | 83.93% | 83.93% | 83.93% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 112/784 | 14.29% | 57.53% | 14.29% |
| model:gliner-stream-pii | eligible | People's names | 1036/1151 | 90.01% | 90.01% | 90.01% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 600/793 | 75.66% | 93.69% | 75.66% |
| model:gliner-stream-pii | eligible | Addresses & locations | 329/901 | 36.51% | 57.05% | 36.07% |
| model:gliner-stream-pii | eligible | Dates & times | 219/223 | 98.21% | 98.21% | 98.21% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 187/194 | 96.39% | 98.45% | 96.39% |
| model:gliner-urchade | eligible | Logins & usernames | 289/311 | 92.93% | 92.93% | 92.93% |
| model:gliner-urchade | eligible | Bank accounts & cards | 425/448 | 94.87% | 94.87% | 94.87% |
| model:gliner-urchade | eligible | Documents & identifiers | 606/784 | 77.30% | 77.30% | 77.30% |
| model:gliner-urchade | eligible | People's names | 100/1151 | 8.69% | 8.69% | 8.69% |
| model:gliner-urchade | eligible | Phone numbers & email | 792/793 | 99.87% | 100.00% | 99.87% |
| model:gliner-urchade | eligible | Addresses & locations | 759/901 | 84.24% | 89.68% | 84.24% |
| model:gliner-urchade | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:gliner-urchade-ru | eligible | Passwords, keys & tokens | 190/194 | 97.94% | 99.48% | 97.94% |
| model:gliner-urchade-ru | eligible | Logins & usernames | 212/311 | 68.17% | 68.17% | 68.17% |
| model:gliner-urchade-ru | eligible | Bank accounts & cards | 382/448 | 85.27% | 85.27% | 85.27% |
| model:gliner-urchade-ru | eligible | Documents & identifiers | 582/784 | 74.23% | 74.23% | 74.23% |
| model:gliner-urchade-ru | eligible | People's names | 121/1151 | 10.51% | 10.51% | 10.51% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 765/901 | 84.91% | 89.12% | 84.91% |
| model:gliner-urchade-ru | eligible | Dates & times | 222/223 | 99.55% | 99.55% | 99.55% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 184/194 | 94.85% | 98.45% | 93.81% |
| model:gliner2-fastino | eligible | Logins & usernames | 305/311 | 98.07% | 98.07% | 98.07% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 424/448 | 94.64% | 94.64% | 94.64% |
| model:gliner2-fastino | eligible | Documents & identifiers | 746/784 | 95.15% | 95.15% | 95.15% |
| model:gliner2-fastino | eligible | People's names | 1099/1151 | 95.48% | 95.48% | 95.48% |
| model:gliner2-fastino | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| model:gliner2-fastino | eligible | Addresses & locations | 659/901 | 73.14% | 86.68% | 73.14% |
| model:gliner2-fastino | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:gliner2-fastino-ru | eligible | Passwords, keys & tokens | 187/194 | 96.39% | 98.45% | 94.85% |
| model:gliner2-fastino-ru | eligible | Logins & usernames | 299/311 | 96.14% | 96.14% | 96.14% |
| model:gliner2-fastino-ru | eligible | Bank accounts & cards | 410/448 | 91.52% | 91.52% | 91.52% |
| model:gliner2-fastino-ru | eligible | Documents & identifiers | 761/784 | 97.07% | 97.19% | 97.07% |
| model:gliner2-fastino-ru | eligible | People's names | 1120/1151 | 97.31% | 97.31% | 97.31% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 631/901 | 70.03% | 84.24% | 70.03% |
| model:gliner2-fastino-ru | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 190/194 | 97.94% | 98.97% | 97.94% |
| model:gliner2-hivetrace-omni | eligible | Logins & usernames | 246/311 | 79.10% | 79.10% | 79.10% |
| model:gliner2-hivetrace-omni | eligible | Bank accounts & cards | 445/448 | 99.33% | 99.33% | 99.33% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 600/784 | 76.53% | 76.66% | 76.53% |
| model:gliner2-hivetrace-omni | eligible | People's names | 1117/1151 | 97.05% | 97.05% | 97.05% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 792/793 | 99.87% | 99.87% | 99.87% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 560/901 | 62.15% | 96.78% | 62.15% |
| model:gliner2-hivetrace-omni | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:gliner2-hivetrace-omni-ru | eligible | Passwords, keys & tokens | 190/194 | 97.94% | 98.97% | 97.94% |
| model:gliner2-hivetrace-omni-ru | eligible | Logins & usernames | 288/311 | 92.60% | 92.60% | 92.60% |
| model:gliner2-hivetrace-omni-ru | eligible | Bank accounts & cards | 433/448 | 96.65% | 96.65% | 96.65% |
| model:gliner2-hivetrace-omni-ru | eligible | Documents & identifiers | 570/784 | 72.70% | 72.83% | 72.70% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 1140/1151 | 99.04% | 99.04% | 99.04% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 788/793 | 99.37% | 99.37% | 99.37% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 573/901 | 63.60% | 97.34% | 63.60% |
| model:gliner2-hivetrace-omni-ru | eligible | Dates & times | 222/223 | 99.55% | 99.55% | 99.55% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 80/194 | 41.24% | 41.75% | 41.24% |
| model:gliner2-hivetrace-uni | eligible | Logins & usernames | 234/311 | 75.24% | 75.24% | 75.24% |
| model:gliner2-hivetrace-uni | eligible | Bank accounts & cards | 418/448 | 93.30% | 93.30% | 93.30% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 689/784 | 87.88% | 91.07% | 87.76% |
| model:gliner2-hivetrace-uni | eligible | People's names | 253/1151 | 21.98% | 21.98% | 21.98% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 784/793 | 98.87% | 98.87% | 98.87% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 328/901 | 36.40% | 61.38% | 36.40% |
| model:gliner2-hivetrace-uni | eligible | Dates & times | 222/223 | 99.55% | 99.55% | 99.55% |
| model:gliner2-hivetrace-uni-ru | eligible | Passwords, keys & tokens | 9/194 | 4.64% | 4.64% | 4.64% |
| model:gliner2-hivetrace-uni-ru | eligible | Logins & usernames | 190/311 | 61.09% | 61.09% | 61.09% |
| model:gliner2-hivetrace-uni-ru | eligible | Bank accounts & cards | 32/448 | 7.14% | 7.14% | 7.14% |
| model:gliner2-hivetrace-uni-ru | eligible | Documents & identifiers | 319/784 | 40.69% | 41.45% | 40.69% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 792/1151 | 68.81% | 68.81% | 68.81% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 6/793 | 0.76% | 0.76% | 0.76% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 91/901 | 10.10% | 17.87% | 10.10% |
| model:gliner2-hivetrace-uni-ru | eligible | Dates & times | 189/223 | 84.75% | 84.75% | 84.75% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 157/194 | 80.93% | 93.30% | 80.93% |
| model:gliner2-large | eligible | Logins & usernames | 259/311 | 83.28% | 83.28% | 83.28% |
| model:gliner2-large | eligible | Bank accounts & cards | 418/448 | 93.30% | 93.30% | 93.30% |
| model:gliner2-large | eligible | Documents & identifiers | 584/784 | 74.49% | 74.62% | 74.49% |
| model:gliner2-large | eligible | People's names | 743/1151 | 64.55% | 64.55% | 64.55% |
| model:gliner2-large | eligible | Phone numbers & email | 790/793 | 99.62% | 99.62% | 99.62% |
| model:gliner2-large | eligible | Addresses & locations | 486/901 | 53.94% | 58.38% | 53.94% |
| model:gliner2-large | eligible | Dates & times | 222/223 | 99.55% | 99.55% | 99.55% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 189/194 | 97.42% | 98.45% | 97.42% |
| model:gliner2-vladlinv | eligible | Logins & usernames | 226/311 | 72.67% | 72.67% | 72.67% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 257/448 | 57.37% | 57.37% | 57.37% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 489/784 | 62.37% | 62.37% | 62.37% |
| model:gliner2-vladlinv | eligible | People's names | 1091/1151 | 94.79% | 94.79% | 94.79% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 786/793 | 99.12% | 99.12% | 99.12% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 93/901 | 10.32% | 10.54% | 10.32% |
| model:gliner2-vladlinv | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:gliner2-vladlinv-ru | eligible | Passwords, keys & tokens | 169/194 | 87.11% | 87.63% | 87.11% |
| model:gliner2-vladlinv-ru | eligible | Logins & usernames | 222/311 | 71.38% | 71.38% | 71.38% |
| model:gliner2-vladlinv-ru | eligible | Bank accounts & cards | 292/448 | 65.18% | 65.18% | 65.18% |
| model:gliner2-vladlinv-ru | eligible | Documents & identifiers | 657/784 | 83.80% | 83.80% | 83.80% |
| model:gliner2-vladlinv-ru | eligible | People's names | 1102/1151 | 95.74% | 95.74% | 95.74% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 787/793 | 99.24% | 99.24% | 99.24% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 342/901 | 37.96% | 38.40% | 37.96% |
| model:gliner2-vladlinv-ru | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 177/194 | 91.24% | 96.91% | 89.18% |
| model:gliner25-fastino | eligible | Logins & usernames | 73/311 | 23.47% | 23.47% | 23.47% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 168/448 | 37.50% | 37.50% | 37.50% |
| model:gliner25-fastino | eligible | Documents & identifiers | 252/784 | 32.14% | 32.14% | 32.14% |
| model:gliner25-fastino | eligible | People's names | 1001/1151 | 86.97% | 86.97% | 86.97% |
| model:gliner25-fastino | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| model:gliner25-fastino | eligible | Addresses & locations | 438/901 | 48.61% | 59.93% | 48.61% |
| model:gliner25-fastino | eligible | Dates & times | 168/223 | 75.34% | 75.34% | 75.34% |
| model:gliner25-fastino-ru | eligible | Passwords, keys & tokens | 158/194 | 81.44% | 85.05% | 80.93% |
| model:gliner25-fastino-ru | eligible | Logins & usernames | 136/311 | 43.73% | 43.73% | 43.73% |
| model:gliner25-fastino-ru | eligible | Bank accounts & cards | 284/448 | 63.39% | 63.39% | 63.39% |
| model:gliner25-fastino-ru | eligible | Documents & identifiers | 382/784 | 48.72% | 48.85% | 48.72% |
| model:gliner25-fastino-ru | eligible | People's names | 1105/1151 | 96.00% | 96.00% | 96.00% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 607/901 | 67.37% | 78.80% | 67.37% |
| model:gliner25-fastino-ru | eligible | Dates & times | 162/223 | 72.65% | 72.65% | 72.65% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 41/194 | 21.13% | 35.57% | 14.43% |
| model:gravitee-small | eligible | Logins & usernames | 29/311 | 9.32% | 9.32% | 3.86% |
| model:gravitee-small | eligible | Bank accounts & cards | 309/448 | 68.97% | 68.97% | 29.24% |
| model:gravitee-small | eligible | Documents & identifiers | 488/784 | 62.24% | 72.70% | 57.78% |
| model:gravitee-small | eligible | People's names | 603/1151 | 52.39% | 52.39% | 42.83% |
| model:gravitee-small | eligible | Phone numbers & email | 644/793 | 81.21% | 97.35% | 72.38% |
| model:gravitee-small | eligible | Addresses & locations | 688/901 | 76.36% | 85.35% | 73.36% |
| model:gravitee-small | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 133/194 | 68.56% | 91.75% | 34.02% |
| model:kalyan-ettin | eligible | Logins & usernames | 269/311 | 86.50% | 86.50% | 52.41% |
| model:kalyan-ettin | eligible | Bank accounts & cards | 373/448 | 83.26% | 83.26% | 20.31% |
| model:kalyan-ettin | eligible | Documents & identifiers | 170/784 | 21.68% | 53.95% | 9.82% |
| model:kalyan-ettin | eligible | People's names | 1049/1151 | 91.14% | 91.14% | 60.12% |
| model:kalyan-ettin | eligible | Phone numbers & email | 543/793 | 68.47% | 96.85% | 66.20% |
| model:kalyan-ettin | eligible | Addresses & locations | 212/901 | 23.53% | 45.39% | 15.65% |
| model:kalyan-ettin | eligible | Dates & times | 220/223 | 98.65% | 100.00% | 98.65% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 112/194 | 57.73% | 91.75% | 18.56% |
| model:mmbert32k | eligible | Logins & usernames | 269/311 | 86.50% | 86.50% | 41.48% |
| model:mmbert32k | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 57.81% |
| model:mmbert32k | eligible | Documents & identifiers | 424/784 | 54.08% | 99.36% | 29.46% |
| model:mmbert32k | eligible | People's names | 1119/1151 | 97.22% | 97.22% | 84.19% |
| model:mmbert32k | eligible | Phone numbers & email | 539/793 | 67.97% | 100.00% | 58.01% |
| model:mmbert32k | eligible | Addresses & locations | 516/901 | 57.27% | 96.45% | 46.61% |
| model:mmbert32k | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 96.86% |
| model:natasha | eligible | Passwords, keys & tokens | 4/194 | 2.06% | 6.19% | 1.55% |
| model:natasha | eligible | Logins & usernames | 0/311 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Bank accounts & cards | 0/448 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 3/784 | 0.38% | 0.38% | 0.38% |
| model:natasha | eligible | People's names | 1123/1151 | 97.57% | 97.57% | 97.57% |
| model:natasha | eligible | Phone numbers & email | 0/793 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Addresses & locations | 2/901 | 0.22% | 34.30% | 0.22% |
| model:natasha | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/194 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Logins & usernames | 88/311 | 28.30% | 28.30% | 16.72% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 0/448 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/784 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 1118/1151 | 97.13% | 97.13% | 96.61% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/793 | 0.00% | 13.62% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 185/901 | 20.53% | 78.80% | 20.31% |
| model:ner-ru-gherman | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 3/194 | 1.55% | 2.58% | 0.00% |
| model:ner-ru-yqelz | eligible | Logins & usernames | 67/311 | 21.54% | 21.54% | 8.68% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 101/448 | 22.54% | 22.54% | 0.00% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 5/784 | 0.64% | 2.17% | 0.13% |
| model:ner-ru-yqelz | eligible | People's names | 1137/1151 | 98.78% | 98.78% | 98.18% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 41/793 | 5.17% | 21.06% | 2.40% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 206/901 | 22.86% | 50.72% | 16.43% |
| model:ner-ru-yqelz | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 187/194 | 96.39% | 99.48% | 96.39% |
| model:nuner-zero | eligible | Logins & usernames | 306/311 | 98.39% | 98.39% | 98.39% |
| model:nuner-zero | eligible | Bank accounts & cards | 444/448 | 99.11% | 99.11% | 99.11% |
| model:nuner-zero | eligible | Documents & identifiers | 559/784 | 71.30% | 75.64% | 26.79% |
| model:nuner-zero | eligible | People's names | 853/1151 | 74.11% | 74.11% | 74.11% |
| model:nuner-zero | eligible | Phone numbers & email | 788/793 | 99.37% | 99.50% | 58.39% |
| model:nuner-zero | eligible | Addresses & locations | 587/901 | 65.15% | 84.24% | 35.96% |
| model:nuner-zero | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:nym-base | eligible | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 100.00% |
| model:nym-base | eligible | Logins & usernames | 311/311 | 100.00% | 100.00% | 99.68% |
| model:nym-base | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| model:nym-base | eligible | Documents & identifiers | 779/784 | 99.36% | 100.00% | 99.23% |
| model:nym-base | eligible | People's names | 1149/1151 | 99.83% | 99.83% | 99.65% |
| model:nym-base | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| model:nym-base | eligible | Addresses & locations | 882/901 | 97.89% | 99.89% | 98.56% |
| model:nym-base | eligible | Dates & times | 222/223 | 99.55% | 100.00% | 99.55% |
| model:nym-small | eligible | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 100.00% |
| model:nym-small | eligible | Logins & usernames | 309/311 | 99.36% | 99.36% | 99.36% |
| model:nym-small | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| model:nym-small | eligible | Documents & identifiers | 781/784 | 99.62% | 100.00% | 99.11% |
| model:nym-small | eligible | People's names | 1146/1151 | 99.57% | 99.57% | 99.39% |
| model:nym-small | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| model:nym-small | eligible | Addresses & locations | 885/901 | 98.22% | 99.45% | 98.45% |
| model:nym-small | eligible | Dates & times | 221/223 | 99.10% | 99.10% | 99.10% |
| model:openai-base | eligible | Passwords, keys & tokens | 189/194 | 97.42% | 98.97% | 97.42% |
| model:openai-base | eligible | Logins & usernames | 252/311 | 81.03% | 81.03% | 76.21% |
| model:openai-base | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 99.55% |
| model:openai-base | eligible | Documents & identifiers | 741/784 | 94.52% | 99.87% | 97.19% |
| model:openai-base | eligible | People's names | 989/1151 | 85.93% | 85.93% | 84.01% |
| model:openai-base | eligible | Phone numbers & email | 792/793 | 99.87% | 100.00% | 99.87% |
| model:openai-base | eligible | Addresses & locations | 682/901 | 75.69% | 83.24% | 75.25% |
| model:openai-base | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 192/194 | 98.97% | 99.48% | 96.91% |
| model:openmed-multilingual | eligible | Logins & usernames | 258/311 | 82.96% | 82.96% | 66.24% |
| model:openmed-multilingual | eligible | Bank accounts & cards | 436/448 | 97.32% | 97.32% | 89.96% |
| model:openmed-multilingual | eligible | Documents & identifiers | 731/784 | 93.24% | 99.74% | 94.01% |
| model:openmed-multilingual | eligible | People's names | 920/1151 | 79.93% | 79.93% | 66.72% |
| model:openmed-multilingual | eligible | Phone numbers & email | 761/793 | 95.96% | 100.00% | 95.21% |
| model:openmed-multilingual | eligible | Addresses & locations | 332/901 | 36.85% | 69.48% | 32.96% |
| model:openmed-multilingual | eligible | Dates & times | 222/223 | 99.55% | 100.00% | 96.86% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 161/194 | 82.99% | 96.91% | 67.53% |
| model:openmed-nemotron | eligible | Logins & usernames | 253/311 | 81.35% | 81.35% | 58.20% |
| model:openmed-nemotron | eligible | Bank accounts & cards | 242/448 | 54.02% | 54.02% | 8.26% |
| model:openmed-nemotron | eligible | Documents & identifiers | 210/784 | 26.79% | 63.27% | 11.73% |
| model:openmed-nemotron | eligible | People's names | 1002/1151 | 87.05% | 87.05% | 71.68% |
| model:openmed-nemotron | eligible | Phone numbers & email | 758/793 | 95.59% | 99.37% | 93.95% |
| model:openmed-nemotron | eligible | Addresses & locations | 349/901 | 38.73% | 71.14% | 35.85% |
| model:openmed-nemotron | eligible | Dates & times | 222/223 | 99.55% | 100.00% | 99.55% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 180/194 | 92.78% | 97.42% | 89.69% |
| model:opf-kz-ru | eligible | Logins & usernames | 186/311 | 59.81% | 59.81% | 52.09% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| model:opf-kz-ru | eligible | Documents & identifiers | 716/784 | 91.33% | 100.00% | 96.81% |
| model:opf-kz-ru | eligible | People's names | 926/1151 | 80.45% | 80.45% | 74.02% |
| model:opf-kz-ru | eligible | Phone numbers & email | 792/793 | 99.87% | 100.00% | 99.75% |
| model:opf-kz-ru | eligible | Addresses & locations | 357/901 | 39.62% | 67.70% | 37.51% |
| model:opf-kz-ru | eligible | Dates & times | 222/223 | 99.55% | 100.00% | 98.21% |
| model:opf-ru | train | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 99.48% |
| model:opf-ru | train | Logins & usernames | 311/311 | 100.00% | 100.00% | 100.00% |
| model:opf-ru | train | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| model:opf-ru | train | Documents & identifiers | 782/784 | 99.74% | 100.00% | 100.00% |
| model:opf-ru | train | People's names | 1149/1151 | 99.83% | 99.83% | 99.48% |
| model:opf-ru | train | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| model:opf-ru | train | Addresses & locations | 900/901 | 99.89% | 99.89% | 99.56% |
| model:opf-ru | train | Dates & times | 223/223 | 100.00% | 100.00% | 100.00% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 190/194 | 97.94% | 99.48% | 91.24% |
| model:opf-ru-v2 | eligible | Logins & usernames | 197/311 | 63.34% | 63.34% | 39.23% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 77.46% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 778/784 | 99.23% | 100.00% | 99.87% |
| model:opf-ru-v2 | eligible | People's names | 1061/1151 | 92.18% | 92.18% | 89.66% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 788/793 | 99.37% | 100.00% | 99.50% |
| model:opf-ru-v2 | eligible | Addresses & locations | 646/901 | 71.70% | 79.36% | 69.26% |
| model:opf-ru-v2 | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 182/194 | 93.81% | 97.42% | 91.24% |
| model:pii-shield-onnx | eligible | Logins & usernames | 248/311 | 79.74% | 79.74% | 63.34% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 95.76% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 664/784 | 84.69% | 98.47% | 86.61% |
| model:pii-shield-onnx | eligible | People's names | 783/1151 | 68.03% | 68.03% | 58.64% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 784/793 | 98.87% | 99.50% | 98.99% |
| model:pii-shield-onnx | eligible | Addresses & locations | 460/901 | 51.05% | 73.58% | 46.61% |
| model:pii-shield-onnx | eligible | Dates & times | 221/223 | 99.10% | 100.00% | 98.65% |
| model:pplx | eligible | Passwords, keys & tokens | 194/194 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Logins & usernames | 310/311 | 99.68% | 99.68% | 99.68% |
| model:pplx | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Documents & identifiers | 784/784 | 100.00% | 100.00% | 99.87% |
| model:pplx | eligible | People's names | 1147/1151 | 99.65% | 99.65% | 99.30% |
| model:pplx | eligible | Phone numbers & email | 792/793 | 99.87% | 100.00% | 99.37% |
| model:pplx | eligible | Addresses & locations | 808/901 | 89.68% | 99.33% | 89.46% |
| model:pplx | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 98.65% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 67/194 | 34.54% | 77.32% | 4.12% |
| model:ru-legal-ner | eligible | Logins & usernames | 257/311 | 82.64% | 82.64% | 31.19% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 446/448 | 99.55% | 99.55% | 37.95% |
| model:ru-legal-ner | eligible | Documents & identifiers | 726/784 | 92.60% | 99.36% | 91.07% |
| model:ru-legal-ner | eligible | People's names | 1104/1151 | 95.92% | 95.92% | 94.18% |
| model:ru-legal-ner | eligible | Phone numbers & email | 764/793 | 96.34% | 98.74% | 95.08% |
| model:ru-legal-ner | eligible | Addresses & locations | 692/901 | 76.80% | 89.90% | 69.26% |
| model:ru-legal-ner | eligible | Dates & times | 111/223 | 49.78% | 84.75% | 49.33% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 186/194 | 95.88% | 97.94% | 95.88% |
| model:ru-pii-ner | eligible | Logins & usernames | 305/311 | 98.07% | 98.07% | 98.07% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 448/448 | 100.00% | 100.00% | 99.33% |
| model:ru-pii-ner | eligible | Documents & identifiers | 780/784 | 99.49% | 99.49% | 98.60% |
| model:ru-pii-ner | eligible | People's names | 1138/1151 | 98.87% | 98.87% | 98.78% |
| model:ru-pii-ner | eligible | Phone numbers & email | 781/793 | 98.49% | 98.49% | 98.49% |
| model:ru-pii-ner | eligible | Addresses & locations | 763/901 | 84.68% | 84.91% | 84.68% |
| model:ru-pii-ner | eligible | Dates & times | 223/223 | 100.00% | 100.00% | 99.55% |
| model:rules-ru | eligible | Passwords, keys & tokens | 14/194 | 7.22% | 12.89% | 7.22% |
| model:rules-ru | eligible | Logins & usernames | 1/311 | 0.32% | 0.32% | 0.32% |
| model:rules-ru | eligible | Bank accounts & cards | 208/448 | 46.43% | 46.43% | 33.48% |
| model:rules-ru | eligible | Documents & identifiers | 600/784 | 76.53% | 76.53% | 76.53% |
| model:rules-ru | eligible | People's names | 0/1151 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 793/793 | 100.00% | 100.00% | 100.00% |
| model:rules-ru | eligible | Addresses & locations | 0/901 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 1/194 | 0.52% | 0.52% | 0.52% |
| model:spacy-alrosait | eligible | Logins & usernames | 0/311 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 0/448 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/784 | 0.00% | 0.77% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 1082/1151 | 94.01% | 94.01% | 94.01% |
| model:spacy-alrosait | eligible | Phone numbers & email | 4/793 | 0.50% | 0.63% | 0.50% |
| model:spacy-alrosait | eligible | Addresses & locations | 649/901 | 72.03% | 76.03% | 72.03% |
| model:spacy-alrosait | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 12/194 | 6.19% | 6.19% | 6.19% |
| model:spacy-ru-lg | eligible | Logins & usernames | 25/311 | 8.04% | 8.04% | 8.04% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 214/448 | 47.77% | 47.77% | 47.77% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 1/784 | 0.13% | 0.51% | 0.13% |
| model:spacy-ru-lg | eligible | People's names | 1142/1151 | 99.22% | 99.22% | 99.22% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 13/793 | 1.64% | 1.64% | 1.64% |
| model:spacy-ru-lg | eligible | Addresses & locations | 1/901 | 0.11% | 45.28% | 0.00% |
| model:spacy-ru-lg | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 117/194 | 60.31% | 83.51% | 55.15% |
| model:stanza-ru | eligible | Logins & usernames | 74/311 | 23.79% | 23.79% | 18.97% |
| model:stanza-ru | eligible | Bank accounts & cards | 250/448 | 55.80% | 55.80% | 55.80% |
| model:stanza-ru | eligible | Documents & identifiers | 140/784 | 17.86% | 19.26% | 17.86% |
| model:stanza-ru | eligible | People's names | 1149/1151 | 99.83% | 99.83% | 99.83% |
| model:stanza-ru | eligible | Phone numbers & email | 71/793 | 8.95% | 8.95% | 8.95% |
| model:stanza-ru | eligible | Addresses & locations | 79/901 | 8.77% | 58.27% | 8.77% |
| model:stanza-ru | eligible | Dates & times | 0/223 | 0.00% | 0.00% | 0.00% |
| model:traciora | eligible | Passwords, keys & tokens | 188/194 | 96.91% | 98.45% | 95.36% |
| model:traciora | eligible | Logins & usernames | 239/311 | 76.85% | 76.85% | 54.98% |
| model:traciora | eligible | Bank accounts & cards | 444/448 | 99.11% | 99.11% | 87.05% |
| model:traciora | eligible | Documents & identifiers | 766/784 | 97.70% | 99.74% | 98.34% |
| model:traciora | eligible | People's names | 1068/1151 | 92.79% | 92.79% | 90.62% |
| model:traciora | eligible | Phone numbers & email | 777/793 | 97.98% | 99.87% | 97.98% |
| model:traciora | eligible | Addresses & locations | 650/901 | 72.14% | 78.02% | 69.48% |
| model:traciora | eligible | Dates & times | 12/223 | 5.38% | 31.84% | 2.69% |
