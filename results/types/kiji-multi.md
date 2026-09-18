# kiji-multi: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/kiji-multi.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 235/255 | 92.16% | 95.29% | 92.16% |
| composition:fastino | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 98.18% |
| composition:fastino | eligible | Bank accounts & cards | 212/215 | 98.60% | 100.00% | 98.60% |
| composition:fastino | eligible | Documents & identifiers | 816/877 | 93.04% | 93.04% | 93.04% |
| composition:fastino | eligible | People's names | 1756/1866 | 94.11% | 95.77% | 94.11% |
| composition:fastino | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| composition:fastino | eligible | Addresses & locations | 3501/3612 | 96.93% | 98.01% | 96.93% |
| composition:fastino | eligible | Dates & times | 131/144 | 90.97% | 90.97% | 90.97% |
| composition:fastino | eligible | Organizations | 147/149 | 98.66% | 98.66% | 98.66% |
| composition:fastino | eligible | Network identifiers | 53/133 | 39.85% | 39.85% | 39.85% |
| composition:pplx | eligible | Passwords, keys & tokens | 244/255 | 95.69% | 96.47% | 95.69% |
| composition:pplx | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 98.18% |
| composition:pplx | eligible | Bank accounts & cards | 211/215 | 98.14% | 99.07% | 98.14% |
| composition:pplx | eligible | Documents & identifiers | 874/877 | 99.66% | 99.66% | 99.66% |
| composition:pplx | eligible | People's names | 1836/1866 | 98.39% | 98.55% | 98.29% |
| composition:pplx | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 99.61% |
| composition:pplx | eligible | Addresses & locations | 3477/3612 | 96.26% | 96.37% | 96.23% |
| composition:pplx | eligible | Dates & times | 144/144 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Organizations | 7/149 | 4.70% | 6.04% | 4.70% |
| composition:pplx | eligible | Network identifiers | 127/133 | 95.49% | 95.49% | 95.49% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 246/255 | 96.47% | 97.25% | 96.47% |
| composition:pplx+fastino | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Bank accounts & cards | 213/215 | 99.07% | 100.00% | 99.07% |
| composition:pplx+fastino | eligible | Documents & identifiers | 875/877 | 99.77% | 99.77% | 99.77% |
| composition:pplx+fastino | eligible | People's names | 1847/1866 | 98.98% | 99.20% | 98.87% |
| composition:pplx+fastino | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Addresses & locations | 3601/3612 | 99.70% | 99.83% | 99.70% |
| composition:pplx+fastino | eligible | Dates & times | 144/144 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Organizations | 149/149 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Network identifiers | 131/133 | 98.50% | 98.50% | 98.50% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 246/255 | 96.47% | 97.25% | 96.47% |
| composition:pplx+fastino+bardsai | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Bank accounts & cards | 213/215 | 99.07% | 100.00% | 99.07% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 875/877 | 99.77% | 99.77% | 99.77% |
| composition:pplx+fastino+bardsai | eligible | People's names | 1850/1866 | 99.14% | 99.36% | 99.14% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 3608/3612 | 99.89% | 99.94% | 99.86% |
| composition:pplx+fastino+bardsai | eligible | Dates & times | 144/144 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 149/149 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 131/133 | 98.50% | 100.00% | 98.50% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 246/255 | 96.47% | 97.25% | 96.47% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Bank accounts & cards | 213/215 | 99.07% | 100.00% | 99.07% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 875/877 | 99.77% | 99.77% | 99.77% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 1852/1866 | 99.25% | 99.41% | 99.25% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 3608/3612 | 99.89% | 99.94% | 99.86% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Dates & times | 144/144 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 149/149 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 132/133 | 99.25% | 100.00% | 99.25% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 246/255 | 96.47% | 97.25% | 96.47% |
| composition:pplx+fastino+mmbert | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Bank accounts & cards | 213/215 | 99.07% | 100.00% | 99.07% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 875/877 | 99.77% | 99.77% | 99.77% |
| composition:pplx+fastino+mmbert | eligible | People's names | 1850/1866 | 99.14% | 99.30% | 99.14% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 3604/3612 | 99.78% | 99.92% | 99.78% |
| composition:pplx+fastino+mmbert | eligible | Dates & times | 144/144 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 149/149 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 132/133 | 99.25% | 100.00% | 99.25% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 245/255 | 96.08% | 96.47% | 95.69% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Logins & usernames | 53/55 | 96.36% | 96.36% | 94.55% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Bank accounts & cards | 204/215 | 94.88% | 97.67% | 95.81% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 839/877 | 95.67% | 98.63% | 92.59% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 1823/1866 | 97.70% | 98.18% | 97.59% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 258/259 | 99.61% | 99.61% | 99.61% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 3350/3612 | 92.75% | 93.66% | 92.17% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Dates & times | 125/144 | 86.81% | 91.67% | 86.81% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 19/149 | 12.75% | 17.45% | 10.74% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 112/133 | 84.21% | 92.48% | 84.21% |
| model:apararti | eligible | Passwords, keys & tokens | 231/255 | 90.59% | 94.90% | 80.39% |
| model:apararti | eligible | Logins & usernames | 43/55 | 78.18% | 78.18% | 69.09% |
| model:apararti | eligible | Bank accounts & cards | 196/215 | 91.16% | 97.67% | 94.42% |
| model:apararti | eligible | Documents & identifiers | 854/877 | 97.38% | 99.32% | 96.81% |
| model:apararti | eligible | People's names | 1413/1866 | 75.72% | 76.85% | 74.71% |
| model:apararti | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 99.61% |
| model:apararti | eligible | Addresses & locations | 2518/3612 | 69.71% | 70.99% | 66.81% |
| model:apararti | eligible | Dates & times | 141/144 | 97.92% | 100.00% | 97.22% |
| model:apararti | eligible | Organizations | 11/149 | 7.38% | 10.74% | 5.37% |
| model:apararti | eligible | Network identifiers | 81/133 | 60.90% | 74.44% | 55.64% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 147/255 | 57.65% | 74.51% | 42.75% |
| model:bardsai-eu | eligible | Logins & usernames | 49/55 | 89.09% | 90.91% | 85.45% |
| model:bardsai-eu | eligible | Bank accounts & cards | 153/215 | 71.16% | 89.77% | 55.81% |
| model:bardsai-eu | eligible | Documents & identifiers | 808/877 | 92.13% | 96.01% | 87.57% |
| model:bardsai-eu | eligible | People's names | 1838/1866 | 98.50% | 98.87% | 98.39% |
| model:bardsai-eu | eligible | Phone numbers & email | 177/259 | 68.34% | 100.00% | 54.05% |
| model:bardsai-eu | eligible | Addresses & locations | 3433/3612 | 95.04% | 95.18% | 93.80% |
| model:bardsai-eu | eligible | Dates & times | 121/144 | 84.03% | 84.03% | 84.03% |
| model:bardsai-eu | eligible | Organizations | 148/149 | 99.33% | 99.33% | 99.33% |
| model:bardsai-eu | eligible | Network identifiers | 7/133 | 5.26% | 83.46% | 0.75% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 1.18% | 0.00% |
| model:davlan-mbert | eligible | Logins & usernames | 7/55 | 12.73% | 12.73% | 3.64% |
| model:davlan-mbert | eligible | Bank accounts & cards | 1/215 | 0.47% | 0.47% | 0.00% |
| model:davlan-mbert | eligible | Documents & identifiers | 1/877 | 0.11% | 0.23% | 0.00% |
| model:davlan-mbert | eligible | People's names | 1810/1866 | 97.00% | 97.64% | 96.68% |
| model:davlan-mbert | eligible | Phone numbers & email | 2/259 | 0.77% | 1.16% | 0.39% |
| model:davlan-mbert | eligible | Addresses & locations | 2253/3612 | 62.38% | 63.54% | 61.85% |
| model:davlan-mbert | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Organizations | 139/149 | 93.29% | 98.66% | 93.29% |
| model:davlan-mbert | eligible | Network identifiers | 2/133 | 1.50% | 27.07% | 0.75% |
| model:davlan-mbert+cpu-int8 | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 0.78% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Logins & usernames | 1/55 | 1.82% | 1.82% | 1.82% |
| model:davlan-mbert+cpu-int8 | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Documents & identifiers | 0/877 | 0.00% | 0.11% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | People's names | 1791/1866 | 95.98% | 96.62% | 95.55% |
| model:davlan-mbert+cpu-int8 | eligible | Phone numbers & email | 0/259 | 0.00% | 0.39% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Addresses & locations | 2257/3612 | 62.49% | 63.79% | 61.71% |
| model:davlan-mbert+cpu-int8 | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | Organizations | 135/149 | 90.60% | 97.32% | 89.26% |
| model:davlan-mbert+cpu-int8 | eligible | Network identifiers | 0/133 | 0.00% | 9.77% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 0.78% | 0.00% |
| model:davlan-xlmr | eligible | Logins & usernames | 16/55 | 29.09% | 30.91% | 9.09% |
| model:davlan-xlmr | eligible | Bank accounts & cards | 1/215 | 0.47% | 0.93% | 0.47% |
| model:davlan-xlmr | eligible | Documents & identifiers | 0/877 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 1835/1866 | 98.34% | 98.87% | 98.12% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/259 | 0.00% | 5.79% | 0.00% |
| model:davlan-xlmr | eligible | Addresses & locations | 2362/3612 | 65.39% | 66.53% | 64.37% |
| model:davlan-xlmr | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Organizations | 145/149 | 97.32% | 99.33% | 97.32% |
| model:davlan-xlmr | eligible | Network identifiers | 0/133 | 0.00% | 20.30% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 1.96% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Logins & usernames | 10/55 | 18.18% | 20.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.47% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Documents & identifiers | 2/877 | 0.23% | 0.46% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | People's names | 1740/1866 | 93.25% | 94.05% | 89.23% |
| model:davlan-xlmr+cpu-int8 | eligible | Phone numbers & email | 0/259 | 0.00% | 5.02% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Addresses & locations | 2021/3612 | 55.95% | 59.91% | 50.33% |
| model:davlan-xlmr+cpu-int8 | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | Organizations | 119/149 | 79.87% | 91.95% | 63.09% |
| model:davlan-xlmr+cpu-int8 | eligible | Network identifiers | 0/133 | 0.00% | 8.27% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 53/255 | 20.78% | 27.06% | 19.61% |
| model:fef2-secret-ru | eligible | Logins & usernames | 5/55 | 9.09% | 9.09% | 9.09% |
| model:fef2-secret-ru | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 14/877 | 1.60% | 2.62% | 1.48% |
| model:fef2-secret-ru | eligible | People's names | 150/1866 | 8.04% | 8.25% | 6.59% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 69/259 | 26.64% | 38.22% | 24.71% |
| model:fef2-secret-ru | eligible | Addresses & locations | 56/3612 | 1.55% | 1.97% | 1.11% |
| model:fef2-secret-ru | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Organizations | 6/149 | 4.03% | 4.70% | 4.03% |
| model:fef2-secret-ru | eligible | Network identifiers | 1/133 | 0.75% | 1.50% | 0.75% |
| model:fef2-secret-ru+cpu-int8 | eligible | Passwords, keys & tokens | 36/255 | 14.12% | 21.57% | 12.94% |
| model:fef2-secret-ru+cpu-int8 | eligible | Logins & usernames | 3/55 | 5.45% | 5.45% | 5.45% |
| model:fef2-secret-ru+cpu-int8 | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru+cpu-int8 | eligible | Documents & identifiers | 5/877 | 0.57% | 1.03% | 0.34% |
| model:fef2-secret-ru+cpu-int8 | eligible | People's names | 167/1866 | 8.95% | 9.11% | 7.18% |
| model:fef2-secret-ru+cpu-int8 | eligible | Phone numbers & email | 26/259 | 10.04% | 30.89% | 8.49% |
| model:fef2-secret-ru+cpu-int8 | eligible | Addresses & locations | 31/3612 | 0.86% | 1.02% | 0.61% |
| model:fef2-secret-ru+cpu-int8 | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru+cpu-int8 | eligible | Organizations | 3/149 | 2.01% | 2.01% | 2.01% |
| model:fef2-secret-ru+cpu-int8 | eligible | Network identifiers | 0/133 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 144/255 | 56.47% | 59.22% | 56.47% |
| model:gliner-multi-v21 | eligible | Logins & usernames | 25/55 | 45.45% | 45.45% | 45.45% |
| model:gliner-multi-v21 | eligible | Bank accounts & cards | 130/215 | 60.47% | 62.79% | 60.00% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 174/877 | 19.84% | 19.95% | 19.84% |
| model:gliner-multi-v21 | eligible | People's names | 1632/1866 | 87.46% | 87.83% | 87.46% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 116/259 | 44.79% | 63.71% | 44.79% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 2897/3612 | 80.20% | 81.06% | 80.20% |
| model:gliner-multi-v21 | eligible | Dates & times | 114/144 | 79.17% | 81.94% | 79.17% |
| model:gliner-multi-v21 | eligible | Organizations | 115/149 | 77.18% | 79.87% | 77.18% |
| model:gliner-multi-v21 | eligible | Network identifiers | 1/133 | 0.75% | 15.04% | 0.75% |
| model:gliner-multi-v21+cpu-int8 | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Logins & usernames | 0/55 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Documents & identifiers | 0/877 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | People's names | 0/1866 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Phone numbers & email | 0/259 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Addresses & locations | 0/3612 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Organizations | 0/149 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Network identifiers | 0/133 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 236/255 | 92.55% | 93.73% | 92.55% |
| model:gliner-nvidia | eligible | Logins & usernames | 52/55 | 94.55% | 96.36% | 94.55% |
| model:gliner-nvidia | eligible | Bank accounts & cards | 192/215 | 89.30% | 94.42% | 89.30% |
| model:gliner-nvidia | eligible | Documents & identifiers | 747/877 | 85.18% | 85.52% | 85.18% |
| model:gliner-nvidia | eligible | People's names | 1811/1866 | 97.05% | 98.02% | 96.89% |
| model:gliner-nvidia | eligible | Phone numbers & email | 167/259 | 64.48% | 98.46% | 64.48% |
| model:gliner-nvidia | eligible | Addresses & locations | 3278/3612 | 90.75% | 92.03% | 90.75% |
| model:gliner-nvidia | eligible | Dates & times | 125/144 | 86.81% | 91.67% | 86.81% |
| model:gliner-nvidia | eligible | Organizations | 135/149 | 90.60% | 95.30% | 90.60% |
| model:gliner-nvidia | eligible | Network identifiers | 114/133 | 85.71% | 94.74% | 85.71% |
| model:gliner-nvidia+cpu-int8 | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Logins & usernames | 0/55 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Documents & identifiers | 0/877 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | People's names | 0/1866 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Phone numbers & email | 0/259 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Addresses & locations | 0/3612 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Organizations | 0/149 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Network identifiers | 0/133 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 140/255 | 54.90% | 58.04% | 54.90% |
| model:gliner-pii-base | eligible | Logins & usernames | 48/55 | 87.27% | 87.27% | 87.27% |
| model:gliner-pii-base | eligible | Bank accounts & cards | 164/215 | 76.28% | 79.53% | 76.28% |
| model:gliner-pii-base | eligible | Documents & identifiers | 531/877 | 60.55% | 60.89% | 60.55% |
| model:gliner-pii-base | eligible | People's names | 198/1866 | 10.61% | 10.66% | 10.61% |
| model:gliner-pii-base | eligible | Phone numbers & email | 248/259 | 95.75% | 96.91% | 95.75% |
| model:gliner-pii-base | eligible | Addresses & locations | 2164/3612 | 59.91% | 60.55% | 59.91% |
| model:gliner-pii-base | eligible | Dates & times | 49/144 | 34.03% | 35.42% | 34.03% |
| model:gliner-pii-base | eligible | Organizations | 115/149 | 77.18% | 82.55% | 77.18% |
| model:gliner-pii-base | eligible | Network identifiers | 64/133 | 48.12% | 53.38% | 48.12% |
| model:gliner-pii-base+cpu-int8 | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Logins & usernames | 0/55 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Documents & identifiers | 2/877 | 0.23% | 0.23% | 0.23% |
| model:gliner-pii-base+cpu-int8 | eligible | People's names | 0/1866 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Phone numbers & email | 1/259 | 0.39% | 0.39% | 0.39% |
| model:gliner-pii-base+cpu-int8 | eligible | Addresses & locations | 0/3612 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Organizations | 0/149 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Network identifiers | 0/133 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 186/255 | 72.94% | 84.31% | 72.94% |
| model:gliner-pii-edge | eligible | Logins & usernames | 53/55 | 96.36% | 96.36% | 96.36% |
| model:gliner-pii-edge | eligible | Bank accounts & cards | 169/215 | 78.60% | 81.40% | 78.60% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 711/877 | 81.07% | 81.30% | 81.07% |
| model:gliner-pii-edge | eligible | People's names | 963/1866 | 51.61% | 51.82% | 51.61% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 249/259 | 96.14% | 96.91% | 96.14% |
| model:gliner-pii-edge | eligible | Addresses & locations | 1444/3612 | 39.98% | 40.48% | 39.98% |
| model:gliner-pii-edge | eligible | Dates & times | 37/144 | 25.69% | 25.69% | 25.69% |
| model:gliner-pii-edge | eligible | Organizations | 134/149 | 89.93% | 95.97% | 89.93% |
| model:gliner-pii-edge | eligible | Network identifiers | 109/133 | 81.95% | 92.48% | 81.95% |
| model:gliner-pii-edge+cpu-int8 | eligible | Passwords, keys & tokens | 28/255 | 10.98% | 12.55% | 10.98% |
| model:gliner-pii-edge+cpu-int8 | eligible | Logins & usernames | 18/55 | 32.73% | 32.73% | 32.73% |
| model:gliner-pii-edge+cpu-int8 | eligible | Bank accounts & cards | 49/215 | 22.79% | 26.05% | 22.79% |
| model:gliner-pii-edge+cpu-int8 | eligible | Documents & identifiers | 354/877 | 40.36% | 43.10% | 40.36% |
| model:gliner-pii-edge+cpu-int8 | eligible | People's names | 219/1866 | 11.74% | 11.84% | 11.74% |
| model:gliner-pii-edge+cpu-int8 | eligible | Phone numbers & email | 26/259 | 10.04% | 24.32% | 10.04% |
| model:gliner-pii-edge+cpu-int8 | eligible | Addresses & locations | 565/3612 | 15.64% | 15.97% | 15.64% |
| model:gliner-pii-edge+cpu-int8 | eligible | Dates & times | 29/144 | 20.14% | 20.14% | 20.14% |
| model:gliner-pii-edge+cpu-int8 | eligible | Organizations | 27/149 | 18.12% | 18.79% | 18.12% |
| model:gliner-pii-edge+cpu-int8 | eligible | Network identifiers | 7/133 | 5.26% | 13.53% | 5.26% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 192/255 | 75.29% | 82.35% | 75.29% |
| model:gliner-stream-pii | eligible | Logins & usernames | 45/55 | 81.82% | 83.64% | 81.82% |
| model:gliner-stream-pii | eligible | Bank accounts & cards | 86/215 | 40.00% | 95.35% | 40.00% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 642/877 | 73.20% | 81.76% | 73.20% |
| model:gliner-stream-pii | eligible | People's names | 1461/1866 | 78.30% | 80.76% | 78.19% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 196/259 | 75.68% | 87.26% | 75.68% |
| model:gliner-stream-pii | eligible | Addresses & locations | 3065/3612 | 84.86% | 86.60% | 84.86% |
| model:gliner-stream-pii | eligible | Dates & times | 106/144 | 73.61% | 73.61% | 73.61% |
| model:gliner-stream-pii | eligible | Organizations | 112/149 | 75.17% | 79.87% | 75.17% |
| model:gliner-stream-pii | eligible | Network identifiers | 48/133 | 36.09% | 37.59% | 36.09% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 234/255 | 91.76% | 94.90% | 91.76% |
| model:gliner-urchade | eligible | Logins & usernames | 52/55 | 94.55% | 96.36% | 94.55% |
| model:gliner-urchade | eligible | Bank accounts & cards | 194/215 | 90.23% | 94.88% | 90.23% |
| model:gliner-urchade | eligible | Documents & identifiers | 788/877 | 89.85% | 90.19% | 89.85% |
| model:gliner-urchade | eligible | People's names | 177/1866 | 9.49% | 9.59% | 9.49% |
| model:gliner-urchade | eligible | Phone numbers & email | 249/259 | 96.14% | 99.23% | 96.14% |
| model:gliner-urchade | eligible | Addresses & locations | 3025/3612 | 83.75% | 84.22% | 83.75% |
| model:gliner-urchade | eligible | Dates & times | 119/144 | 82.64% | 87.50% | 82.64% |
| model:gliner-urchade | eligible | Organizations | 141/149 | 94.63% | 96.64% | 94.63% |
| model:gliner-urchade | eligible | Network identifiers | 117/133 | 87.97% | 95.49% | 87.97% |
| model:gliner-urchade+cpu-int8 | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Logins & usernames | 0/55 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Documents & identifiers | 0/877 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | People's names | 0/1866 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Phone numbers & email | 0/259 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Addresses & locations | 0/3612 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Organizations | 0/149 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Network identifiers | 0/133 | 0.00% | 0.00% | 0.00% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 235/255 | 92.16% | 95.29% | 92.16% |
| model:gliner2-fastino | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 98.18% |
| model:gliner2-fastino | eligible | Bank accounts & cards | 212/215 | 98.60% | 100.00% | 98.60% |
| model:gliner2-fastino | eligible | Documents & identifiers | 816/877 | 93.04% | 93.04% | 93.04% |
| model:gliner2-fastino | eligible | People's names | 1756/1866 | 94.11% | 95.77% | 94.11% |
| model:gliner2-fastino | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| model:gliner2-fastino | eligible | Addresses & locations | 3501/3612 | 96.93% | 98.01% | 96.93% |
| model:gliner2-fastino | eligible | Dates & times | 131/144 | 90.97% | 90.97% | 90.97% |
| model:gliner2-fastino | eligible | Organizations | 147/149 | 98.66% | 98.66% | 98.66% |
| model:gliner2-fastino | eligible | Network identifiers | 53/133 | 39.85% | 39.85% | 39.85% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 231/255 | 90.59% | 96.08% | 90.59% |
| model:gliner2-hivetrace-omni | eligible | Logins & usernames | 54/55 | 98.18% | 98.18% | 98.18% |
| model:gliner2-hivetrace-omni | eligible | Bank accounts & cards | 212/215 | 98.60% | 100.00% | 98.60% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 756/877 | 86.20% | 86.20% | 86.20% |
| model:gliner2-hivetrace-omni | eligible | People's names | 1771/1866 | 94.91% | 97.11% | 94.91% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 3440/3612 | 95.24% | 96.15% | 95.24% |
| model:gliner2-hivetrace-omni | eligible | Dates & times | 130/144 | 90.28% | 90.28% | 90.28% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 134/149 | 89.93% | 90.60% | 89.93% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 46/133 | 34.59% | 34.59% | 34.59% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 178/255 | 69.80% | 76.08% | 69.80% |
| model:gliner2-hivetrace-uni | eligible | Logins & usernames | 52/55 | 94.55% | 96.36% | 94.55% |
| model:gliner2-hivetrace-uni | eligible | Bank accounts & cards | 73/215 | 33.95% | 34.42% | 33.95% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 822/877 | 93.73% | 94.07% | 93.73% |
| model:gliner2-hivetrace-uni | eligible | People's names | 663/1866 | 35.53% | 35.69% | 35.53% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 2837/3612 | 78.54% | 79.84% | 78.54% |
| model:gliner2-hivetrace-uni | eligible | Dates & times | 127/144 | 88.19% | 88.19% | 88.19% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 120/149 | 80.54% | 83.89% | 80.54% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 2/133 | 1.50% | 1.50% | 1.50% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 192/255 | 75.29% | 86.27% | 75.29% |
| model:gliner2-large | eligible | Logins & usernames | 48/55 | 87.27% | 87.27% | 87.27% |
| model:gliner2-large | eligible | Bank accounts & cards | 186/215 | 86.51% | 98.60% | 85.58% |
| model:gliner2-large | eligible | Documents & identifiers | 760/877 | 86.66% | 86.66% | 86.66% |
| model:gliner2-large | eligible | People's names | 1417/1866 | 75.94% | 76.58% | 75.94% |
| model:gliner2-large | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| model:gliner2-large | eligible | Addresses & locations | 2791/3612 | 77.27% | 78.38% | 77.27% |
| model:gliner2-large | eligible | Dates & times | 123/144 | 85.42% | 85.42% | 85.42% |
| model:gliner2-large | eligible | Organizations | 145/149 | 97.32% | 97.32% | 97.32% |
| model:gliner2-large | eligible | Network identifiers | 43/133 | 32.33% | 32.33% | 32.33% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 199/255 | 78.04% | 83.53% | 78.04% |
| model:gliner2-vladlinv | eligible | Logins & usernames | 48/55 | 87.27% | 94.55% | 85.45% |
| model:gliner2-vladlinv | eligible | Bank accounts & cards | 192/215 | 89.30% | 90.70% | 89.30% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 580/877 | 66.13% | 66.13% | 66.13% |
| model:gliner2-vladlinv | eligible | People's names | 1717/1866 | 92.02% | 92.28% | 92.02% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 256/259 | 98.84% | 98.84% | 98.84% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 843/3612 | 23.34% | 23.37% | 23.34% |
| model:gliner2-vladlinv | eligible | Dates & times | 142/144 | 98.61% | 98.61% | 98.61% |
| model:gliner2-vladlinv | eligible | Organizations | 0/149 | 0.00% | 0.67% | 0.00% |
| model:gliner2-vladlinv | eligible | Network identifiers | 4/133 | 3.01% | 3.01% | 3.01% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 139/255 | 54.51% | 55.69% | 54.51% |
| model:gliner25-fastino | eligible | Logins & usernames | 4/55 | 7.27% | 9.09% | 5.45% |
| model:gliner25-fastino | eligible | Bank accounts & cards | 153/215 | 71.16% | 71.63% | 71.16% |
| model:gliner25-fastino | eligible | Documents & identifiers | 269/877 | 30.67% | 30.79% | 30.67% |
| model:gliner25-fastino | eligible | People's names | 989/1866 | 53.00% | 53.97% | 52.89% |
| model:gliner25-fastino | eligible | Phone numbers & email | 258/259 | 99.61% | 99.61% | 99.61% |
| model:gliner25-fastino | eligible | Addresses & locations | 3185/3612 | 88.18% | 89.51% | 88.18% |
| model:gliner25-fastino | eligible | Dates & times | 121/144 | 84.03% | 84.03% | 84.03% |
| model:gliner25-fastino | eligible | Organizations | 112/149 | 75.17% | 76.51% | 75.17% |
| model:gliner25-fastino | eligible | Network identifiers | 13/133 | 9.77% | 9.77% | 9.77% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 110/255 | 43.14% | 47.06% | 41.57% |
| model:gravitee-small | eligible | Logins & usernames | 11/55 | 20.00% | 23.64% | 7.27% |
| model:gravitee-small | eligible | Bank accounts & cards | 200/215 | 93.02% | 94.42% | 90.70% |
| model:gravitee-small | eligible | Documents & identifiers | 536/877 | 61.12% | 62.60% | 59.41% |
| model:gravitee-small | eligible | People's names | 1695/1866 | 90.84% | 91.10% | 89.82% |
| model:gravitee-small | eligible | Phone numbers & email | 252/259 | 97.30% | 98.07% | 96.91% |
| model:gravitee-small | eligible | Addresses & locations | 2299/3612 | 63.65% | 65.97% | 57.34% |
| model:gravitee-small | eligible | Dates & times | 139/144 | 96.53% | 98.61% | 96.53% |
| model:gravitee-small | eligible | Organizations | 119/149 | 79.87% | 83.89% | 75.84% |
| model:gravitee-small | eligible | Network identifiers | 95/133 | 71.43% | 79.70% | 68.42% |
| model:gravitee-small+cpu-int8 | eligible | Passwords, keys & tokens | 105/255 | 41.18% | 45.49% | 38.82% |
| model:gravitee-small+cpu-int8 | eligible | Logins & usernames | 13/55 | 23.64% | 29.09% | 9.09% |
| model:gravitee-small+cpu-int8 | eligible | Bank accounts & cards | 201/215 | 93.49% | 94.88% | 91.63% |
| model:gravitee-small+cpu-int8 | eligible | Documents & identifiers | 530/877 | 60.43% | 62.37% | 58.72% |
| model:gravitee-small+cpu-int8 | eligible | People's names | 1669/1866 | 89.44% | 89.98% | 88.48% |
| model:gravitee-small+cpu-int8 | eligible | Phone numbers & email | 248/259 | 95.75% | 97.68% | 94.98% |
| model:gravitee-small+cpu-int8 | eligible | Addresses & locations | 2270/3612 | 62.85% | 65.45% | 55.84% |
| model:gravitee-small+cpu-int8 | eligible | Dates & times | 139/144 | 96.53% | 97.22% | 96.53% |
| model:gravitee-small+cpu-int8 | eligible | Organizations | 114/149 | 76.51% | 82.55% | 74.50% |
| model:gravitee-small+cpu-int8 | eligible | Network identifiers | 89/133 | 66.92% | 77.44% | 60.90% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 123/255 | 48.24% | 67.84% | 26.27% |
| model:kalyan-ettin | eligible | Logins & usernames | 37/55 | 67.27% | 67.27% | 43.64% |
| model:kalyan-ettin | eligible | Bank accounts & cards | 85/215 | 39.53% | 69.77% | 20.47% |
| model:kalyan-ettin | eligible | Documents & identifiers | 173/877 | 19.73% | 36.94% | 9.35% |
| model:kalyan-ettin | eligible | People's names | 1594/1866 | 85.42% | 87.35% | 81.19% |
| model:kalyan-ettin | eligible | Phone numbers & email | 192/259 | 74.13% | 96.14% | 75.68% |
| model:kalyan-ettin | eligible | Addresses & locations | 3029/3612 | 83.86% | 87.04% | 74.81% |
| model:kalyan-ettin | eligible | Dates & times | 114/144 | 79.17% | 98.61% | 77.08% |
| model:kalyan-ettin | eligible | Organizations | 72/149 | 48.32% | 71.81% | 36.24% |
| model:kalyan-ettin | eligible | Network identifiers | 9/133 | 6.77% | 69.92% | 3.76% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 103/255 | 40.39% | 75.29% | 2.35% |
| model:mmbert32k | eligible | Logins & usernames | 35/55 | 63.64% | 67.27% | 10.91% |
| model:mmbert32k | eligible | Bank accounts & cards | 90/215 | 41.86% | 97.21% | 26.05% |
| model:mmbert32k | eligible | Documents & identifiers | 605/877 | 68.99% | 96.01% | 12.43% |
| model:mmbert32k | eligible | People's names | 1676/1866 | 89.82% | 90.46% | 89.23% |
| model:mmbert32k | eligible | Phone numbers & email | 162/259 | 62.55% | 100.00% | 57.14% |
| model:mmbert32k | eligible | Addresses & locations | 2824/3612 | 78.18% | 82.17% | 72.09% |
| model:mmbert32k | eligible | Dates & times | 117/144 | 81.25% | 100.00% | 79.86% |
| model:mmbert32k | eligible | Organizations | 71/149 | 47.65% | 80.54% | 46.31% |
| model:mmbert32k | eligible | Network identifiers | 37/133 | 27.82% | 97.74% | 22.56% |
| model:mmbert32k+cpu-int8 | eligible | Passwords, keys & tokens | 83/255 | 32.55% | 66.67% | 0.00% |
| model:mmbert32k+cpu-int8 | eligible | Logins & usernames | 16/55 | 29.09% | 30.91% | 1.82% |
| model:mmbert32k+cpu-int8 | eligible | Bank accounts & cards | 82/215 | 38.14% | 97.67% | 0.93% |
| model:mmbert32k+cpu-int8 | eligible | Documents & identifiers | 518/877 | 59.06% | 93.96% | 1.94% |
| model:mmbert32k+cpu-int8 | eligible | People's names | 909/1866 | 48.71% | 51.29% | 45.82% |
| model:mmbert32k+cpu-int8 | eligible | Phone numbers & email | 39/259 | 15.06% | 81.08% | 3.47% |
| model:mmbert32k+cpu-int8 | eligible | Addresses & locations | 2137/3612 | 59.16% | 66.92% | 39.29% |
| model:mmbert32k+cpu-int8 | eligible | Dates & times | 22/144 | 15.28% | 87.50% | 0.69% |
| model:mmbert32k+cpu-int8 | eligible | Organizations | 36/149 | 24.16% | 46.98% | 15.44% |
| model:mmbert32k+cpu-int8 | eligible | Network identifiers | 8/133 | 6.02% | 71.43% | 3.01% |
| model:natasha | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 0.39% | 0.00% |
| model:natasha | eligible | Logins & usernames | 0/55 | 0.00% | 1.82% | 0.00% |
| model:natasha | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Documents & identifiers | 1/877 | 0.11% | 0.11% | 0.11% |
| model:natasha | eligible | People's names | 392/1866 | 21.01% | 21.01% | 21.01% |
| model:natasha | eligible | Phone numbers & email | 0/259 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Addresses & locations | 326/3612 | 9.03% | 9.05% | 9.00% |
| model:natasha | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Organizations | 6/149 | 4.03% | 4.03% | 4.03% |
| model:natasha | eligible | Network identifiers | 0/133 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 5.10% | 0.00% |
| model:ner-ru-gherman | eligible | Logins & usernames | 14/55 | 25.45% | 27.27% | 0.00% |
| model:ner-ru-gherman | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/877 | 0.00% | 0.11% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 1777/1866 | 95.23% | 96.36% | 94.64% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/259 | 0.00% | 24.32% | 0.00% |
| model:ner-ru-gherman | eligible | Addresses & locations | 2389/3612 | 66.14% | 74.36% | 56.59% |
| model:ner-ru-gherman | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Organizations | 1/149 | 0.67% | 9.40% | 0.67% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/133 | 0.00% | 7.52% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 4.31% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Logins & usernames | 8/55 | 14.55% | 16.36% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Documents & identifiers | 0/877 | 0.00% | 0.11% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | People's names | 1763/1866 | 94.48% | 95.82% | 93.84% |
| model:ner-ru-gherman+cpu-int8 | eligible | Phone numbers & email | 0/259 | 0.00% | 15.44% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Addresses & locations | 2168/3612 | 60.02% | 66.31% | 52.27% |
| model:ner-ru-gherman+cpu-int8 | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Organizations | 0/149 | 0.00% | 7.38% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | Network identifiers | 0/133 | 0.00% | 7.52% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 4.71% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Logins & usernames | 12/55 | 21.82% | 23.64% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Documents & identifiers | 0/877 | 0.00% | 0.11% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | People's names | 1776/1866 | 95.18% | 96.20% | 94.53% |
| model:ner-ru-gherman-onnx | eligible | Phone numbers & email | 0/259 | 0.00% | 25.48% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Addresses & locations | 2368/3612 | 65.56% | 73.78% | 56.40% |
| model:ner-ru-gherman-onnx | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | Organizations | 1/149 | 0.67% | 9.40% | 0.67% |
| model:ner-ru-gherman-onnx | eligible | Network identifiers | 0/133 | 0.00% | 7.52% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 19/255 | 7.45% | 9.80% | 3.14% |
| model:ner-ru-yqelz | eligible | Logins & usernames | 1/55 | 1.82% | 1.82% | 0.00% |
| model:ner-ru-yqelz | eligible | Bank accounts & cards | 57/215 | 26.51% | 54.88% | 8.37% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 42/877 | 4.79% | 6.39% | 3.31% |
| model:ner-ru-yqelz | eligible | People's names | 1461/1866 | 78.30% | 78.78% | 75.78% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 2/259 | 0.77% | 6.56% | 0.77% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 2108/3612 | 58.36% | 59.69% | 54.40% |
| model:ner-ru-yqelz | eligible | Dates & times | 0/144 | 0.00% | 0.69% | 0.00% |
| model:ner-ru-yqelz | eligible | Organizations | 72/149 | 48.32% | 58.39% | 39.60% |
| model:ner-ru-yqelz | eligible | Network identifiers | 2/133 | 1.50% | 13.53% | 1.50% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 234/255 | 91.76% | 95.29% | 91.37% |
| model:nuner-zero | eligible | Logins & usernames | 53/55 | 96.36% | 98.18% | 96.36% |
| model:nuner-zero | eligible | Bank accounts & cards | 196/215 | 91.16% | 94.42% | 35.35% |
| model:nuner-zero | eligible | Documents & identifiers | 637/877 | 72.63% | 73.20% | 69.90% |
| model:nuner-zero | eligible | People's names | 595/1866 | 31.89% | 32.42% | 30.60% |
| model:nuner-zero | eligible | Phone numbers & email | 252/259 | 97.30% | 99.61% | 56.76% |
| model:nuner-zero | eligible | Addresses & locations | 3242/3612 | 89.76% | 91.03% | 78.43% |
| model:nuner-zero | eligible | Dates & times | 128/144 | 88.89% | 96.53% | 74.31% |
| model:nuner-zero | eligible | Organizations | 138/149 | 92.62% | 95.97% | 46.98% |
| model:nuner-zero | eligible | Network identifiers | 126/133 | 94.74% | 100.00% | 94.74% |
| model:nym-base | eligible | Passwords, keys & tokens | 210/255 | 82.35% | 89.41% | 70.98% |
| model:nym-base | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 98.18% |
| model:nym-base | eligible | Bank accounts & cards | 200/215 | 93.02% | 94.88% | 92.56% |
| model:nym-base | eligible | Documents & identifiers | 804/877 | 91.68% | 94.87% | 87.12% |
| model:nym-base | eligible | People's names | 1828/1866 | 97.96% | 98.61% | 98.07% |
| model:nym-base | eligible | Phone numbers & email | 238/259 | 91.89% | 100.00% | 91.12% |
| model:nym-base | eligible | Addresses & locations | 3552/3612 | 98.34% | 98.73% | 98.39% |
| model:nym-base | eligible | Dates & times | 130/144 | 90.28% | 90.97% | 86.11% |
| model:nym-base | eligible | Organizations | 134/149 | 89.93% | 94.63% | 91.28% |
| model:nym-base | eligible | Network identifiers | 105/133 | 78.95% | 90.98% | 78.95% |
| model:nym-base+cpu-int8 | eligible | Passwords, keys & tokens | 195/255 | 76.47% | 85.88% | 60.78% |
| model:nym-base+cpu-int8 | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 100.00% |
| model:nym-base+cpu-int8 | eligible | Bank accounts & cards | 201/215 | 93.49% | 95.81% | 88.37% |
| model:nym-base+cpu-int8 | eligible | Documents & identifiers | 798/877 | 90.99% | 95.32% | 84.95% |
| model:nym-base+cpu-int8 | eligible | People's names | 1804/1866 | 96.68% | 97.32% | 96.73% |
| model:nym-base+cpu-int8 | eligible | Phone numbers & email | 233/259 | 89.96% | 100.00% | 89.19% |
| model:nym-base+cpu-int8 | eligible | Addresses & locations | 3495/3612 | 96.76% | 97.51% | 96.62% |
| model:nym-base+cpu-int8 | eligible | Dates & times | 127/144 | 88.19% | 90.97% | 86.81% |
| model:nym-base+cpu-int8 | eligible | Organizations | 129/149 | 86.58% | 92.62% | 87.92% |
| model:nym-base+cpu-int8 | eligible | Network identifiers | 103/133 | 77.44% | 93.98% | 76.69% |
| model:nym-small | eligible | Passwords, keys & tokens | 195/255 | 76.47% | 83.92% | 66.27% |
| model:nym-small | eligible | Logins & usernames | 53/55 | 96.36% | 98.18% | 94.55% |
| model:nym-small | eligible | Bank accounts & cards | 206/215 | 95.81% | 97.21% | 93.49% |
| model:nym-small | eligible | Documents & identifiers | 811/877 | 92.47% | 95.78% | 89.62% |
| model:nym-small | eligible | People's names | 1817/1866 | 97.37% | 98.18% | 97.80% |
| model:nym-small | eligible | Phone numbers & email | 253/259 | 97.68% | 100.00% | 96.91% |
| model:nym-small | eligible | Addresses & locations | 3530/3612 | 97.73% | 98.39% | 97.70% |
| model:nym-small | eligible | Dates & times | 131/144 | 90.97% | 92.36% | 87.50% |
| model:nym-small | eligible | Organizations | 135/149 | 90.60% | 94.63% | 91.28% |
| model:nym-small | eligible | Network identifiers | 104/133 | 78.20% | 93.98% | 78.20% |
| model:openai-base | eligible | Passwords, keys & tokens | 202/255 | 79.22% | 84.71% | 74.12% |
| model:openai-base | eligible | Logins & usernames | 45/55 | 81.82% | 83.64% | 76.36% |
| model:openai-base | eligible | Bank accounts & cards | 205/215 | 95.35% | 98.14% | 95.81% |
| model:openai-base | eligible | Documents & identifiers | 830/877 | 94.64% | 96.24% | 93.84% |
| model:openai-base | eligible | People's names | 1628/1866 | 87.25% | 88.00% | 87.19% |
| model:openai-base | eligible | Phone numbers & email | 257/259 | 99.23% | 99.61% | 99.61% |
| model:openai-base | eligible | Addresses & locations | 2433/3612 | 67.36% | 68.02% | 66.17% |
| model:openai-base | eligible | Dates & times | 141/144 | 97.92% | 98.61% | 97.92% |
| model:openai-base | eligible | Organizations | 11/149 | 7.38% | 12.08% | 6.71% |
| model:openai-base | eligible | Network identifiers | 47/133 | 35.34% | 40.60% | 32.33% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 200/255 | 78.43% | 82.75% | 61.18% |
| model:openmed-multilingual | eligible | Logins & usernames | 50/55 | 90.91% | 92.73% | 80.00% |
| model:openmed-multilingual | eligible | Bank accounts & cards | 149/215 | 69.30% | 71.16% | 60.47% |
| model:openmed-multilingual | eligible | Documents & identifiers | 599/877 | 68.30% | 75.48% | 58.38% |
| model:openmed-multilingual | eligible | People's names | 1671/1866 | 89.55% | 91.26% | 89.44% |
| model:openmed-multilingual | eligible | Phone numbers & email | 252/259 | 97.30% | 99.61% | 96.91% |
| model:openmed-multilingual | eligible | Addresses & locations | 2901/3612 | 80.32% | 83.53% | 78.46% |
| model:openmed-multilingual | eligible | Dates & times | 125/144 | 86.81% | 95.14% | 87.50% |
| model:openmed-multilingual | eligible | Organizations | 13/149 | 8.72% | 21.48% | 6.71% |
| model:openmed-multilingual | eligible | Network identifiers | 54/133 | 40.60% | 58.65% | 38.35% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 157/255 | 61.57% | 76.47% | 30.98% |
| model:openmed-nemotron | eligible | Logins & usernames | 40/55 | 72.73% | 76.36% | 63.64% |
| model:openmed-nemotron | eligible | Bank accounts & cards | 98/215 | 45.58% | 74.42% | 31.63% |
| model:openmed-nemotron | eligible | Documents & identifiers | 187/877 | 21.32% | 35.01% | 12.09% |
| model:openmed-nemotron | eligible | People's names | 1576/1866 | 84.46% | 87.41% | 82.58% |
| model:openmed-nemotron | eligible | Phone numbers & email | 223/259 | 86.10% | 97.68% | 84.17% |
| model:openmed-nemotron | eligible | Addresses & locations | 2620/3612 | 72.54% | 75.61% | 64.78% |
| model:openmed-nemotron | eligible | Dates & times | 127/144 | 88.19% | 93.75% | 84.72% |
| model:openmed-nemotron | eligible | Organizations | 91/149 | 61.07% | 71.14% | 51.68% |
| model:openmed-nemotron | eligible | Network identifiers | 101/133 | 75.94% | 87.22% | 73.68% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 213/255 | 83.53% | 92.55% | 74.12% |
| model:opf-kz-ru | eligible | Logins & usernames | 39/55 | 70.91% | 70.91% | 67.27% |
| model:opf-kz-ru | eligible | Bank accounts & cards | 204/215 | 94.88% | 99.07% | 97.67% |
| model:opf-kz-ru | eligible | Documents & identifiers | 848/877 | 96.69% | 98.75% | 96.01% |
| model:opf-kz-ru | eligible | People's names | 1417/1866 | 75.94% | 76.85% | 74.92% |
| model:opf-kz-ru | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| model:opf-kz-ru | eligible | Addresses & locations | 2533/3612 | 70.13% | 70.93% | 67.94% |
| model:opf-kz-ru | eligible | Dates & times | 138/144 | 95.83% | 99.31% | 96.53% |
| model:opf-kz-ru | eligible | Organizations | 8/149 | 5.37% | 6.71% | 4.70% |
| model:opf-kz-ru | eligible | Network identifiers | 96/133 | 72.18% | 78.95% | 70.68% |
| model:opf-ru | eligible | Passwords, keys & tokens | 218/255 | 85.49% | 91.76% | 74.51% |
| model:opf-ru | eligible | Logins & usernames | 49/55 | 89.09% | 92.73% | 81.82% |
| model:opf-ru | eligible | Bank accounts & cards | 117/215 | 54.42% | 98.14% | 46.51% |
| model:opf-ru | eligible | Documents & identifiers | 619/877 | 70.58% | 89.40% | 49.83% |
| model:opf-ru | eligible | People's names | 1599/1866 | 85.69% | 86.55% | 84.99% |
| model:opf-ru | eligible | Phone numbers & email | 256/259 | 98.84% | 99.61% | 98.84% |
| model:opf-ru | eligible | Addresses & locations | 2051/3612 | 56.78% | 62.49% | 49.42% |
| model:opf-ru | eligible | Dates & times | 113/144 | 78.47% | 89.58% | 76.39% |
| model:opf-ru | eligible | Organizations | 19/149 | 12.75% | 22.82% | 8.05% |
| model:opf-ru | eligible | Network identifiers | 6/133 | 4.51% | 54.89% | 4.51% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 204/255 | 80.00% | 92.16% | 64.71% |
| model:opf-ru-v2 | eligible | Logins & usernames | 34/55 | 61.82% | 61.82% | 50.91% |
| model:opf-ru-v2 | eligible | Bank accounts & cards | 165/215 | 76.74% | 94.88% | 74.42% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 655/877 | 74.69% | 90.88% | 55.87% |
| model:opf-ru-v2 | eligible | People's names | 1262/1866 | 67.63% | 68.17% | 66.77% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 251/259 | 96.91% | 98.84% | 98.46% |
| model:opf-ru-v2 | eligible | Addresses & locations | 1968/3612 | 54.49% | 55.79% | 49.92% |
| model:opf-ru-v2 | eligible | Dates & times | 0/144 | 0.00% | 1.39% | 0.00% |
| model:opf-ru-v2 | eligible | Organizations | 16/149 | 10.74% | 14.77% | 8.72% |
| model:opf-ru-v2 | eligible | Network identifiers | 1/133 | 0.75% | 7.52% | 0.75% |
| model:pii-shield-onnx | eligible | Passwords, keys & tokens | 174/255 | 68.24% | 81.18% | 63.14% |
| model:pii-shield-onnx | eligible | Logins & usernames | 37/55 | 67.27% | 69.09% | 50.91% |
| model:pii-shield-onnx | eligible | Bank accounts & cards | 181/215 | 84.19% | 88.84% | 67.44% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 665/877 | 75.83% | 85.40% | 55.42% |
| model:pii-shield-onnx | eligible | People's names | 851/1866 | 45.61% | 47.64% | 31.89% |
| model:pii-shield-onnx | eligible | Phone numbers & email | 215/259 | 83.01% | 98.46% | 81.47% |
| model:pii-shield-onnx | eligible | Addresses & locations | 2348/3612 | 65.01% | 68.47% | 48.95% |
| model:pii-shield-onnx | eligible | Dates & times | 40/144 | 27.78% | 73.61% | 26.39% |
| model:pii-shield-onnx | eligible | Organizations | 102/149 | 68.46% | 79.87% | 42.95% |
| model:pii-shield-onnx | eligible | Network identifiers | 114/133 | 85.71% | 96.99% | 84.96% |
| model:pplx | eligible | Passwords, keys & tokens | 244/255 | 95.69% | 96.47% | 95.69% |
| model:pplx | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 98.18% |
| model:pplx | eligible | Bank accounts & cards | 211/215 | 98.14% | 99.07% | 98.14% |
| model:pplx | eligible | Documents & identifiers | 874/877 | 99.66% | 99.66% | 99.66% |
| model:pplx | eligible | People's names | 1836/1866 | 98.39% | 98.55% | 98.29% |
| model:pplx | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 99.61% |
| model:pplx | eligible | Addresses & locations | 3477/3612 | 96.26% | 96.37% | 96.23% |
| model:pplx | eligible | Dates & times | 144/144 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Organizations | 7/149 | 4.70% | 6.04% | 4.70% |
| model:pplx | eligible | Network identifiers | 127/133 | 95.49% | 95.49% | 95.49% |
| model:pplx+cpu-int8 | eligible | Passwords, keys & tokens | 245/255 | 96.08% | 96.86% | 95.69% |
| model:pplx+cpu-int8 | eligible | Logins & usernames | 55/55 | 100.00% | 100.00% | 98.18% |
| model:pplx+cpu-int8 | eligible | Bank accounts & cards | 214/215 | 99.53% | 99.53% | 98.60% |
| model:pplx+cpu-int8 | eligible | Documents & identifiers | 876/877 | 99.89% | 99.89% | 99.89% |
| model:pplx+cpu-int8 | eligible | People's names | 1854/1866 | 99.36% | 99.46% | 99.30% |
| model:pplx+cpu-int8 | eligible | Phone numbers & email | 259/259 | 100.00% | 100.00% | 100.00% |
| model:pplx+cpu-int8 | eligible | Addresses & locations | 3595/3612 | 99.53% | 99.58% | 99.50% |
| model:pplx+cpu-int8 | eligible | Dates & times | 144/144 | 100.00% | 100.00% | 100.00% |
| model:pplx+cpu-int8 | eligible | Organizations | 102/149 | 68.46% | 73.83% | 68.46% |
| model:pplx+cpu-int8 | eligible | Network identifiers | 130/133 | 97.74% | 98.50% | 97.74% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 79/255 | 30.98% | 65.88% | 5.49% |
| model:ru-legal-ner | eligible | Logins & usernames | 41/55 | 74.55% | 80.00% | 41.82% |
| model:ru-legal-ner | eligible | Bank accounts & cards | 97/215 | 45.12% | 78.60% | 10.23% |
| model:ru-legal-ner | eligible | Documents & identifiers | 456/877 | 52.00% | 74.34% | 24.29% |
| model:ru-legal-ner | eligible | People's names | 621/1866 | 33.28% | 33.87% | 27.01% |
| model:ru-legal-ner | eligible | Phone numbers & email | 147/259 | 56.76% | 93.82% | 53.67% |
| model:ru-legal-ner | eligible | Addresses & locations | 1735/3612 | 48.03% | 52.77% | 37.24% |
| model:ru-legal-ner | eligible | Dates & times | 67/144 | 46.53% | 82.64% | 44.44% |
| model:ru-legal-ner | eligible | Organizations | 33/149 | 22.15% | 36.91% | 10.74% |
| model:ru-legal-ner | eligible | Network identifiers | 1/133 | 0.75% | 71.43% | 0.75% |
| model:ru-legal-ner+cpu-int8 | eligible | Passwords, keys & tokens | 78/255 | 30.59% | 62.75% | 5.10% |
| model:ru-legal-ner+cpu-int8 | eligible | Logins & usernames | 42/55 | 76.36% | 81.82% | 36.36% |
| model:ru-legal-ner+cpu-int8 | eligible | Bank accounts & cards | 95/215 | 44.19% | 75.35% | 10.23% |
| model:ru-legal-ner+cpu-int8 | eligible | Documents & identifiers | 450/877 | 51.31% | 72.18% | 24.06% |
| model:ru-legal-ner+cpu-int8 | eligible | People's names | 636/1866 | 34.08% | 35.10% | 26.58% |
| model:ru-legal-ner+cpu-int8 | eligible | Phone numbers & email | 143/259 | 55.21% | 94.59% | 51.35% |
| model:ru-legal-ner+cpu-int8 | eligible | Addresses & locations | 1732/3612 | 47.95% | 52.82% | 37.13% |
| model:ru-legal-ner+cpu-int8 | eligible | Dates & times | 63/144 | 43.75% | 81.25% | 42.36% |
| model:ru-legal-ner+cpu-int8 | eligible | Organizations | 41/149 | 27.52% | 41.61% | 12.75% |
| model:ru-legal-ner+cpu-int8 | eligible | Network identifiers | 1/133 | 0.75% | 72.93% | 0.75% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 139/255 | 54.51% | 60.00% | 51.37% |
| model:ru-pii-ner | eligible | Logins & usernames | 39/55 | 70.91% | 70.91% | 69.09% |
| model:ru-pii-ner | eligible | Bank accounts & cards | 180/215 | 83.72% | 95.35% | 82.33% |
| model:ru-pii-ner | eligible | Documents & identifiers | 784/877 | 89.40% | 89.85% | 89.40% |
| model:ru-pii-ner | eligible | People's names | 1456/1866 | 78.03% | 78.30% | 77.97% |
| model:ru-pii-ner | eligible | Phone numbers & email | 248/259 | 95.75% | 97.30% | 95.75% |
| model:ru-pii-ner | eligible | Addresses & locations | 1062/3612 | 29.40% | 29.60% | 29.35% |
| model:ru-pii-ner | eligible | Dates & times | 140/144 | 97.22% | 97.22% | 97.22% |
| model:ru-pii-ner | eligible | Organizations | 10/149 | 6.71% | 9.40% | 6.71% |
| model:ru-pii-ner | eligible | Network identifiers | 18/133 | 13.53% | 17.29% | 13.53% |
| model:rules-ru | eligible | Passwords, keys & tokens | 40/255 | 15.69% | 15.69% | 15.69% |
| model:rules-ru | eligible | Logins & usernames | 6/55 | 10.91% | 10.91% | 10.91% |
| model:rules-ru | eligible | Bank accounts & cards | 51/215 | 23.72% | 24.65% | 10.23% |
| model:rules-ru | eligible | Documents & identifiers | 11/877 | 1.25% | 1.60% | 1.14% |
| model:rules-ru | eligible | People's names | 9/1866 | 0.48% | 0.48% | 0.48% |
| model:rules-ru | eligible | Phone numbers & email | 229/259 | 88.42% | 88.42% | 88.42% |
| model:rules-ru | eligible | Addresses & locations | 5/3612 | 0.14% | 0.14% | 0.11% |
| model:rules-ru | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Organizations | 20/149 | 13.42% | 15.44% | 13.42% |
| model:rules-ru | eligible | Network identifiers | 132/133 | 99.25% | 99.25% | 99.25% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/255 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Logins & usernames | 0/55 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Bank accounts & cards | 0/215 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/877 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 0/1866 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Phone numbers & email | 1/259 | 0.39% | 0.39% | 0.39% |
| model:spacy-alrosait | eligible | Addresses & locations | 7/3612 | 0.19% | 0.19% | 0.19% |
| model:spacy-alrosait | eligible | Dates & times | 0/144 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Organizations | 0/149 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Network identifiers | 0/133 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 21/255 | 8.24% | 8.24% | 8.24% |
| model:spacy-ru-lg | eligible | Logins & usernames | 4/55 | 7.27% | 7.27% | 7.27% |
| model:spacy-ru-lg | eligible | Bank accounts & cards | 6/215 | 2.79% | 2.79% | 2.79% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 36/877 | 4.10% | 4.22% | 4.10% |
| model:spacy-ru-lg | eligible | People's names | 684/1866 | 36.66% | 36.66% | 36.66% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 4/259 | 1.54% | 2.32% | 1.54% |
| model:spacy-ru-lg | eligible | Addresses & locations | 633/3612 | 17.52% | 17.58% | 17.52% |
| model:spacy-ru-lg | eligible | Dates & times | 4/144 | 2.78% | 5.56% | 2.78% |
| model:spacy-ru-lg | eligible | Organizations | 32/149 | 21.48% | 22.15% | 21.48% |
| model:spacy-ru-lg | eligible | Network identifiers | 5/133 | 3.76% | 3.76% | 3.76% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 36/255 | 14.12% | 19.22% | 13.33% |
| model:stanza-ru | eligible | Logins & usernames | 5/55 | 9.09% | 9.09% | 9.09% |
| model:stanza-ru | eligible | Bank accounts & cards | 10/215 | 4.65% | 20.00% | 4.65% |
| model:stanza-ru | eligible | Documents & identifiers | 61/877 | 6.96% | 10.38% | 6.73% |
| model:stanza-ru | eligible | People's names | 1626/1866 | 87.14% | 87.14% | 87.14% |
| model:stanza-ru | eligible | Phone numbers & email | 7/259 | 2.70% | 2.70% | 2.70% |
| model:stanza-ru | eligible | Addresses & locations | 1526/3612 | 42.25% | 43.63% | 41.94% |
| model:stanza-ru | eligible | Dates & times | 1/144 | 0.69% | 2.08% | 0.69% |
| model:stanza-ru | eligible | Organizations | 94/149 | 63.09% | 69.13% | 63.09% |
| model:stanza-ru | eligible | Network identifiers | 2/133 | 1.50% | 1.50% | 1.50% |
| model:traciora | eligible | Passwords, keys & tokens | 182/255 | 71.37% | 81.57% | 52.55% |
| model:traciora | eligible | Logins & usernames | 34/55 | 61.82% | 65.45% | 52.73% |
| model:traciora | eligible | Bank accounts & cards | 191/215 | 88.84% | 93.95% | 86.05% |
| model:traciora | eligible | Documents & identifiers | 485/877 | 55.30% | 69.21% | 29.99% |
| model:traciora | eligible | People's names | 1406/1866 | 75.35% | 76.58% | 74.49% |
| model:traciora | eligible | Phone numbers & email | 251/259 | 96.91% | 99.23% | 96.53% |
| model:traciora | eligible | Addresses & locations | 2332/3612 | 64.56% | 66.11% | 59.86% |
| model:traciora | eligible | Dates & times | 0/144 | 0.00% | 12.50% | 0.00% |
| model:traciora | eligible | Organizations | 23/149 | 15.44% | 20.81% | 11.41% |
| model:traciora | eligible | Network identifiers | 2/133 | 1.50% | 13.53% | 1.50% |
