# synth-jira-comments: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/synth-jira-comments.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Passwords, keys & tokens | 67/344 | 19.48% | 24.71% | 19.48% |
| composition:fastino | eligible | Logins & usernames | 216/221 | 97.74% | 97.74% | 97.74% |
| composition:fastino | eligible | People's names | 547/566 | 96.64% | 98.23% | 96.64% |
| composition:fastino | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| composition:fastino | eligible | Network identifiers | 1025/1132 | 90.55% | 91.43% | 90.55% |
| composition:pplx | eligible | Passwords, keys & tokens | 340/344 | 98.84% | 100.00% | 98.84% |
| composition:pplx | eligible | Logins & usernames | 221/221 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | People's names | 566/566 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Network identifiers | 1125/1132 | 99.38% | 99.82% | 99.29% |
| composition:pplx+fastino | eligible | Passwords, keys & tokens | 340/344 | 98.84% | 100.00% | 98.84% |
| composition:pplx+fastino | eligible | Logins & usernames | 221/221 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | People's names | 566/566 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Network identifiers | 1129/1132 | 99.73% | 99.82% | 99.73% |
| composition:pplx+fastino+bardsai | eligible | Passwords, keys & tokens | 340/344 | 98.84% | 100.00% | 98.84% |
| composition:pplx+fastino+bardsai | eligible | Logins & usernames | 221/221 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | People's names | 566/566 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 1129/1132 | 99.73% | 99.82% | 99.73% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Passwords, keys & tokens | 340/344 | 98.84% | 100.00% | 98.84% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Logins & usernames | 221/221 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 566/566 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 1129/1132 | 99.73% | 100.00% | 99.73% |
| composition:pplx+fastino+mmbert | eligible | Passwords, keys & tokens | 340/344 | 98.84% | 100.00% | 98.84% |
| composition:pplx+fastino+mmbert | eligible | Logins & usernames | 221/221 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | People's names | 566/566 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 1129/1132 | 99.73% | 100.00% | 99.73% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Passwords, keys & tokens | 308/344 | 89.53% | 96.80% | 87.79% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Logins & usernames | 106/221 | 47.96% | 55.20% | 41.18% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 543/566 | 95.94% | 99.12% | 93.29% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 1079/1132 | 95.32% | 96.29% | 95.32% |
| model:apararti | eligible | Passwords, keys & tokens | 333/344 | 96.80% | 99.42% | 93.60% |
| model:apararti | eligible | Logins & usernames | 72/221 | 32.58% | 40.72% | 20.81% |
| model:apararti | eligible | People's names | 492/566 | 86.93% | 93.46% | 82.86% |
| model:apararti | eligible | Phone numbers & email | 434/442 | 98.19% | 99.77% | 93.67% |
| model:apararti | eligible | Network identifiers | 389/1132 | 34.36% | 55.65% | 29.95% |
| model:bardsai-eu | eligible | Passwords, keys & tokens | 249/344 | 72.38% | 86.92% | 58.43% |
| model:bardsai-eu | eligible | Logins & usernames | 155/221 | 70.14% | 83.71% | 57.47% |
| model:bardsai-eu | eligible | People's names | 556/566 | 98.23% | 100.00% | 90.81% |
| model:bardsai-eu | eligible | Phone numbers & email | 233/442 | 52.71% | 99.77% | 50.68% |
| model:bardsai-eu | eligible | Network identifiers | 19/1132 | 1.68% | 13.96% | 0.97% |
| model:davlan-mbert | eligible | Passwords, keys & tokens | 0/344 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Logins & usernames | 0/221 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | People's names | 541/566 | 95.58% | 99.29% | 80.74% |
| model:davlan-mbert | eligible | Phone numbers & email | 0/442 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Network identifiers | 0/1132 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Passwords, keys & tokens | 0/344 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Logins & usernames | 6/221 | 2.71% | 4.52% | 0.45% |
| model:davlan-xlmr | eligible | People's names | 562/566 | 99.29% | 100.00% | 87.28% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/442 | 0.00% | 2.94% | 0.00% |
| model:davlan-xlmr | eligible | Network identifiers | 0/1132 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Passwords, keys & tokens | 171/344 | 49.71% | 59.59% | 47.09% |
| model:fef2-secret-ru | eligible | Logins & usernames | 72/221 | 32.58% | 38.46% | 24.43% |
| model:fef2-secret-ru | eligible | People's names | 363/566 | 64.13% | 68.73% | 55.48% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 209/442 | 47.29% | 50.23% | 44.57% |
| model:fef2-secret-ru | eligible | Network identifiers | 0/1132 | 0.00% | 0.27% | 0.00% |
| model:gliner-multi-v21 | eligible | Passwords, keys & tokens | 28/344 | 8.14% | 10.17% | 8.14% |
| model:gliner-multi-v21 | eligible | Logins & usernames | 149/221 | 67.42% | 71.04% | 67.42% |
| model:gliner-multi-v21 | eligible | People's names | 551/566 | 97.35% | 97.53% | 97.35% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 176/442 | 39.82% | 65.61% | 39.82% |
| model:gliner-multi-v21 | eligible | Network identifiers | 126/1132 | 11.13% | 15.90% | 11.13% |
| model:gliner-multi-v21-ru | eligible | Passwords, keys & tokens | 43/344 | 12.50% | 15.12% | 12.50% |
| model:gliner-multi-v21-ru | eligible | Logins & usernames | 140/221 | 63.35% | 64.71% | 63.35% |
| model:gliner-multi-v21-ru | eligible | People's names | 470/566 | 83.04% | 83.04% | 83.04% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 173/442 | 39.14% | 71.49% | 39.14% |
| model:gliner-multi-v21-ru | eligible | Network identifiers | 252/1132 | 22.26% | 25.53% | 22.26% |
| model:gliner-nvidia | eligible | Passwords, keys & tokens | 291/344 | 84.59% | 85.17% | 84.59% |
| model:gliner-nvidia | eligible | Logins & usernames | 66/221 | 29.86% | 32.13% | 29.86% |
| model:gliner-nvidia | eligible | People's names | 337/566 | 59.54% | 80.21% | 55.83% |
| model:gliner-nvidia | eligible | Phone numbers & email | 431/442 | 97.51% | 99.55% | 97.51% |
| model:gliner-nvidia | eligible | Network identifiers | 1078/1132 | 95.23% | 95.23% | 95.23% |
| model:gliner-nvidia-ru | eligible | Passwords, keys & tokens | 89/344 | 25.87% | 26.16% | 25.87% |
| model:gliner-nvidia-ru | eligible | Logins & usernames | 15/221 | 6.79% | 17.19% | 6.79% |
| model:gliner-nvidia-ru | eligible | People's names | 310/566 | 54.77% | 79.68% | 38.52% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 437/442 | 98.87% | 98.87% | 98.87% |
| model:gliner-nvidia-ru | eligible | Network identifiers | 649/1132 | 57.33% | 57.33% | 57.33% |
| model:gliner-pii-base | eligible | Passwords, keys & tokens | 165/344 | 47.97% | 50.87% | 47.97% |
| model:gliner-pii-base | eligible | Logins & usernames | 69/221 | 31.22% | 31.22% | 31.22% |
| model:gliner-pii-base | eligible | People's names | 90/566 | 15.90% | 16.78% | 15.90% |
| model:gliner-pii-base | eligible | Phone numbers & email | 358/442 | 81.00% | 84.39% | 81.00% |
| model:gliner-pii-base | eligible | Network identifiers | 557/1132 | 49.20% | 50.09% | 49.20% |
| model:gliner-pii-edge | eligible | Passwords, keys & tokens | 294/344 | 85.47% | 96.51% | 85.47% |
| model:gliner-pii-edge | eligible | Logins & usernames | 161/221 | 72.85% | 78.73% | 72.85% |
| model:gliner-pii-edge | eligible | People's names | 186/566 | 32.86% | 52.47% | 28.62% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 401/442 | 90.72% | 91.63% | 90.72% |
| model:gliner-pii-edge | eligible | Network identifiers | 772/1132 | 68.20% | 69.70% | 68.20% |
| model:gliner-stream-pii | eligible | Passwords, keys & tokens | 191/344 | 55.52% | 61.92% | 55.52% |
| model:gliner-stream-pii | eligible | Logins & usernames | 140/221 | 63.35% | 73.76% | 63.35% |
| model:gliner-stream-pii | eligible | People's names | 188/566 | 33.22% | 33.75% | 33.22% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 369/442 | 83.48% | 93.89% | 83.48% |
| model:gliner-stream-pii | eligible | Network identifiers | 595/1132 | 52.56% | 57.77% | 52.56% |
| model:gliner-urchade | eligible | Passwords, keys & tokens | 77/344 | 22.38% | 24.42% | 22.38% |
| model:gliner-urchade | eligible | Logins & usernames | 65/221 | 29.41% | 29.41% | 29.41% |
| model:gliner-urchade | eligible | People's names | 566/566 | 100.00% | 100.00% | 100.00% |
| model:gliner-urchade | eligible | Phone numbers & email | 358/442 | 81.00% | 89.14% | 81.00% |
| model:gliner-urchade | eligible | Network identifiers | 750/1132 | 66.25% | 66.25% | 66.25% |
| model:gliner-urchade-ru | eligible | Passwords, keys & tokens | 33/344 | 9.59% | 11.05% | 9.59% |
| model:gliner-urchade-ru | eligible | Logins & usernames | 35/221 | 15.84% | 15.84% | 15.84% |
| model:gliner-urchade-ru | eligible | People's names | 13/566 | 2.30% | 2.30% | 2.30% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 288/442 | 65.16% | 68.78% | 65.16% |
| model:gliner-urchade-ru | eligible | Network identifiers | 545/1132 | 48.14% | 48.14% | 48.14% |
| model:gliner2-fastino | eligible | Passwords, keys & tokens | 67/344 | 19.48% | 24.71% | 19.48% |
| model:gliner2-fastino | eligible | Logins & usernames | 216/221 | 97.74% | 97.74% | 97.74% |
| model:gliner2-fastino | eligible | People's names | 547/566 | 96.64% | 98.23% | 96.64% |
| model:gliner2-fastino | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| model:gliner2-fastino | eligible | Network identifiers | 1025/1132 | 90.55% | 91.43% | 90.55% |
| model:gliner2-fastino-ru | eligible | Passwords, keys & tokens | 44/344 | 12.79% | 16.57% | 12.79% |
| model:gliner2-fastino-ru | eligible | Logins & usernames | 127/221 | 57.47% | 57.47% | 57.47% |
| model:gliner2-fastino-ru | eligible | People's names | 548/566 | 96.82% | 98.76% | 96.82% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| model:gliner2-fastino-ru | eligible | Network identifiers | 1107/1132 | 97.79% | 97.79% | 97.79% |
| model:gliner2-hivetrace-omni | eligible | Passwords, keys & tokens | 196/344 | 56.98% | 61.05% | 56.98% |
| model:gliner2-hivetrace-omni | eligible | Logins & usernames | 92/221 | 41.63% | 41.63% | 41.63% |
| model:gliner2-hivetrace-omni | eligible | People's names | 565/566 | 99.82% | 100.00% | 99.82% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 1103/1132 | 97.44% | 97.88% | 97.44% |
| model:gliner2-hivetrace-omni-ru | eligible | Passwords, keys & tokens | 86/344 | 25.00% | 29.65% | 25.00% |
| model:gliner2-hivetrace-omni-ru | eligible | Logins & usernames | 38/221 | 17.19% | 17.19% | 17.19% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 564/566 | 99.65% | 100.00% | 99.65% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| model:gliner2-hivetrace-omni-ru | eligible | Network identifiers | 946/1132 | 83.57% | 83.57% | 83.57% |
| model:gliner2-hivetrace-uni | eligible | Passwords, keys & tokens | 3/344 | 0.87% | 1.16% | 0.87% |
| model:gliner2-hivetrace-uni | eligible | Logins & usernames | 43/221 | 19.46% | 20.36% | 19.46% |
| model:gliner2-hivetrace-uni | eligible | People's names | 492/566 | 86.93% | 91.34% | 86.75% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 423/442 | 95.70% | 95.70% | 95.70% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 0/1132 | 0.00% | 0.00% | 0.00% |
| model:gliner2-hivetrace-uni-ru | eligible | Passwords, keys & tokens | 87/344 | 25.29% | 27.33% | 25.29% |
| model:gliner2-hivetrace-uni-ru | eligible | Logins & usernames | 38/221 | 17.19% | 17.19% | 17.19% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 367/566 | 64.84% | 66.25% | 64.84% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 169/442 | 38.24% | 38.24% | 38.24% |
| model:gliner2-hivetrace-uni-ru | eligible | Network identifiers | 0/1132 | 0.00% | 0.62% | 0.00% |
| model:gliner2-large | eligible | Passwords, keys & tokens | 47/344 | 13.66% | 16.57% | 13.66% |
| model:gliner2-large | eligible | Logins & usernames | 80/221 | 36.20% | 36.20% | 36.20% |
| model:gliner2-large | eligible | People's names | 320/566 | 56.54% | 68.73% | 56.54% |
| model:gliner2-large | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| model:gliner2-large | eligible | Network identifiers | 1024/1132 | 90.46% | 90.46% | 90.46% |
| model:gliner2-vladlinv | eligible | Passwords, keys & tokens | 122/344 | 35.47% | 37.50% | 35.47% |
| model:gliner2-vladlinv | eligible | Logins & usernames | 8/221 | 3.62% | 4.07% | 3.62% |
| model:gliner2-vladlinv | eligible | People's names | 550/566 | 97.17% | 98.59% | 97.17% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 384/442 | 86.88% | 86.88% | 86.88% |
| model:gliner2-vladlinv | eligible | Network identifiers | 0/1132 | 0.00% | 0.00% | 0.00% |
| model:gliner2-vladlinv-ru | eligible | Passwords, keys & tokens | 155/344 | 45.06% | 47.67% | 45.06% |
| model:gliner2-vladlinv-ru | eligible | Logins & usernames | 8/221 | 3.62% | 4.07% | 3.62% |
| model:gliner2-vladlinv-ru | eligible | People's names | 550/566 | 97.17% | 98.59% | 97.17% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 368/442 | 83.26% | 83.26% | 83.26% |
| model:gliner2-vladlinv-ru | eligible | Network identifiers | 0/1132 | 0.00% | 0.00% | 0.00% |
| model:gliner25-fastino | eligible | Passwords, keys & tokens | 123/344 | 35.76% | 40.70% | 35.76% |
| model:gliner25-fastino | eligible | Logins & usernames | 72/221 | 32.58% | 32.58% | 32.58% |
| model:gliner25-fastino | eligible | People's names | 559/566 | 98.76% | 99.47% | 98.76% |
| model:gliner25-fastino | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| model:gliner25-fastino | eligible | Network identifiers | 998/1132 | 88.16% | 88.16% | 88.16% |
| model:gliner25-fastino-ru | eligible | Passwords, keys & tokens | 60/344 | 17.44% | 20.93% | 17.44% |
| model:gliner25-fastino-ru | eligible | Logins & usernames | 55/221 | 24.89% | 24.89% | 24.89% |
| model:gliner25-fastino-ru | eligible | People's names | 559/566 | 98.76% | 99.82% | 98.76% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| model:gliner25-fastino-ru | eligible | Network identifiers | 822/1132 | 72.61% | 72.61% | 72.61% |
| model:gravitee-small | eligible | Passwords, keys & tokens | 131/344 | 38.08% | 59.30% | 23.26% |
| model:gravitee-small | eligible | Logins & usernames | 19/221 | 8.60% | 17.65% | 4.52% |
| model:gravitee-small | eligible | People's names | 418/566 | 73.85% | 80.04% | 59.72% |
| model:gravitee-small | eligible | Phone numbers & email | 353/442 | 79.86% | 98.42% | 77.83% |
| model:gravitee-small | eligible | Network identifiers | 560/1132 | 49.47% | 50.00% | 49.47% |
| model:kalyan-ettin | eligible | Passwords, keys & tokens | 161/344 | 46.80% | 79.36% | 13.08% |
| model:kalyan-ettin | eligible | Logins & usernames | 213/221 | 96.38% | 100.00% | 94.12% |
| model:kalyan-ettin | eligible | People's names | 150/566 | 26.50% | 97.88% | 22.44% |
| model:kalyan-ettin | eligible | Phone numbers & email | 366/442 | 82.81% | 98.64% | 76.92% |
| model:kalyan-ettin | eligible | Network identifiers | 450/1132 | 39.75% | 51.86% | 37.37% |
| model:mmbert32k | eligible | Passwords, keys & tokens | 111/344 | 32.27% | 85.47% | 0.58% |
| model:mmbert32k | eligible | Logins & usernames | 114/221 | 51.58% | 79.64% | 20.36% |
| model:mmbert32k | eligible | People's names | 429/566 | 75.80% | 99.12% | 53.71% |
| model:mmbert32k | eligible | Phone numbers & email | 194/442 | 43.89% | 100.00% | 26.47% |
| model:mmbert32k | eligible | Network identifiers | 431/1132 | 38.07% | 81.45% | 17.93% |
| model:natasha | eligible | Passwords, keys & tokens | 0/344 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Logins & usernames | 0/221 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | People's names | 328/566 | 57.95% | 63.07% | 56.89% |
| model:natasha | eligible | Phone numbers & email | 0/442 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Network identifiers | 0/1132 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Passwords, keys & tokens | 0/344 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Logins & usernames | 38/221 | 17.19% | 38.01% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 23/566 | 4.06% | 100.00% | 3.36% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/442 | 0.00% | 18.33% | 0.00% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/1132 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Passwords, keys & tokens | 19/344 | 5.52% | 8.14% | 0.00% |
| model:ner-ru-yqelz | eligible | Logins & usernames | 0/221 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | People's names | 563/566 | 99.47% | 100.00% | 97.88% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 1/442 | 0.23% | 2.49% | 0.00% |
| model:ner-ru-yqelz | eligible | Network identifiers | 5/1132 | 0.44% | 5.39% | 0.09% |
| model:nuner-zero | eligible | Passwords, keys & tokens | 117/344 | 34.01% | 43.60% | 31.98% |
| model:nuner-zero | eligible | Logins & usernames | 47/221 | 21.27% | 24.89% | 20.81% |
| model:nuner-zero | eligible | People's names | 416/566 | 73.50% | 77.92% | 0.00% |
| model:nuner-zero | eligible | Phone numbers & email | 425/442 | 96.15% | 100.00% | 60.86% |
| model:nuner-zero | eligible | Network identifiers | 1132/1132 | 100.00% | 100.00% | 100.00% |
| model:nym-base | eligible | Passwords, keys & tokens | 265/344 | 77.03% | 99.13% | 48.55% |
| model:nym-base | eligible | Logins & usernames | 136/221 | 61.54% | 70.14% | 47.06% |
| model:nym-base | eligible | People's names | 11/566 | 1.94% | 100.00% | 99.29% |
| model:nym-base | eligible | Phone numbers & email | 413/442 | 93.44% | 99.55% | 93.44% |
| model:nym-base | eligible | Network identifiers | 196/1132 | 17.31% | 30.21% | 11.13% |
| model:openai-base | eligible | Passwords, keys & tokens | 324/344 | 94.19% | 95.93% | 91.57% |
| model:openai-base | eligible | Logins & usernames | 126/221 | 57.01% | 66.52% | 46.15% |
| model:openai-base | eligible | People's names | 515/566 | 90.99% | 93.11% | 89.40% |
| model:openai-base | eligible | Phone numbers & email | 432/442 | 97.74% | 98.42% | 96.61% |
| model:openai-base | eligible | Network identifiers | 247/1132 | 21.82% | 32.42% | 21.47% |
| model:openmed-multilingual | eligible | Passwords, keys & tokens | 297/344 | 86.34% | 99.13% | 65.70% |
| model:openmed-multilingual | eligible | Logins & usernames | 95/221 | 42.99% | 52.04% | 32.13% |
| model:openmed-multilingual | eligible | People's names | 36/566 | 6.36% | 60.78% | 23.50% |
| model:openmed-multilingual | eligible | Phone numbers & email | 426/442 | 96.38% | 100.00% | 94.80% |
| model:openmed-multilingual | eligible | Network identifiers | 549/1132 | 48.50% | 50.00% | 48.50% |
| model:openmed-nemotron | eligible | Passwords, keys & tokens | 251/344 | 72.97% | 89.83% | 36.63% |
| model:openmed-nemotron | eligible | Logins & usernames | 149/221 | 67.42% | 76.02% | 52.49% |
| model:openmed-nemotron | eligible | People's names | 84/566 | 14.84% | 96.11% | 62.72% |
| model:openmed-nemotron | eligible | Phone numbers & email | 419/442 | 94.80% | 97.29% | 88.91% |
| model:openmed-nemotron | eligible | Network identifiers | 512/1132 | 45.23% | 49.47% | 43.55% |
| model:opf-kz-ru | eligible | Passwords, keys & tokens | 332/344 | 96.51% | 98.55% | 93.60% |
| model:opf-kz-ru | eligible | Logins & usernames | 135/221 | 61.09% | 73.76% | 42.99% |
| model:opf-kz-ru | eligible | People's names | 519/566 | 91.70% | 94.17% | 86.75% |
| model:opf-kz-ru | eligible | Phone numbers & email | 439/442 | 99.32% | 99.55% | 96.38% |
| model:opf-kz-ru | eligible | Network identifiers | 405/1132 | 35.78% | 52.21% | 31.54% |
| model:opf-ru | eligible | Passwords, keys & tokens | 315/344 | 91.57% | 99.13% | 85.47% |
| model:opf-ru | eligible | Logins & usernames | 183/221 | 82.81% | 89.14% | 72.85% |
| model:opf-ru | eligible | People's names | 455/566 | 80.39% | 94.52% | 73.67% |
| model:opf-ru | eligible | Phone numbers & email | 415/442 | 93.89% | 98.64% | 89.37% |
| model:opf-ru | eligible | Network identifiers | 30/1132 | 2.65% | 30.12% | 1.68% |
| model:opf-ru-v2 | eligible | Passwords, keys & tokens | 296/344 | 86.05% | 94.48% | 81.69% |
| model:opf-ru-v2 | eligible | Logins & usernames | 58/221 | 26.24% | 36.65% | 14.93% |
| model:opf-ru-v2 | eligible | People's names | 512/566 | 90.46% | 95.05% | 85.69% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 409/442 | 92.53% | 99.77% | 91.86% |
| model:opf-ru-v2 | eligible | Network identifiers | 485/1132 | 42.84% | 47.88% | 42.40% |
| model:pplx | eligible | Passwords, keys & tokens | 340/344 | 98.84% | 100.00% | 98.84% |
| model:pplx | eligible | Logins & usernames | 221/221 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | People's names | 566/566 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Network identifiers | 1125/1132 | 99.38% | 99.82% | 99.29% |
| model:ru-legal-ner | eligible | Passwords, keys & tokens | 205/344 | 59.59% | 93.90% | 6.69% |
| model:ru-legal-ner | eligible | Logins & usernames | 137/221 | 61.99% | 79.19% | 35.29% |
| model:ru-legal-ner | eligible | People's names | 401/566 | 70.85% | 77.74% | 55.48% |
| model:ru-legal-ner | eligible | Phone numbers & email | 338/442 | 76.47% | 96.61% | 68.10% |
| model:ru-legal-ner | eligible | Network identifiers | 94/1132 | 8.30% | 65.64% | 6.01% |
| model:ru-pii-ner | eligible | Passwords, keys & tokens | 16/344 | 4.65% | 6.40% | 4.07% |
| model:ru-pii-ner | eligible | Logins & usernames | 178/221 | 80.54% | 80.54% | 80.54% |
| model:ru-pii-ner | eligible | People's names | 563/566 | 99.47% | 99.65% | 99.47% |
| model:ru-pii-ner | eligible | Phone numbers & email | 392/442 | 88.69% | 88.91% | 88.01% |
| model:ru-pii-ner | eligible | Network identifiers | 36/1132 | 3.18% | 3.18% | 3.09% |
| model:rules-ru | eligible | Passwords, keys & tokens | 317/344 | 92.15% | 92.15% | 92.15% |
| model:rules-ru | eligible | Logins & usernames | 7/221 | 3.17% | 3.17% | 3.17% |
| model:rules-ru | eligible | People's names | 0/566 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 442/442 | 100.00% | 100.00% | 100.00% |
| model:rules-ru | eligible | Network identifiers | 1132/1132 | 100.00% | 100.00% | 100.00% |
| model:spacy-alrosait | eligible | Passwords, keys & tokens | 0/344 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Logins & usernames | 0/221 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 382/566 | 67.49% | 67.67% | 67.49% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/442 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Network identifiers | 0/1132 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Passwords, keys & tokens | 1/344 | 0.29% | 0.29% | 0.29% |
| model:spacy-ru-lg | eligible | Logins & usernames | 5/221 | 2.26% | 2.26% | 2.26% |
| model:spacy-ru-lg | eligible | People's names | 149/566 | 26.33% | 46.29% | 25.44% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 1/442 | 0.23% | 0.23% | 0.23% |
| model:spacy-ru-lg | eligible | Network identifiers | 2/1132 | 0.18% | 0.18% | 0.18% |
| model:stanza-ru | eligible | Passwords, keys & tokens | 14/344 | 4.07% | 23.55% | 0.29% |
| model:stanza-ru | eligible | Logins & usernames | 0/221 | 0.00% | 0.00% | 0.00% |
| model:stanza-ru | eligible | People's names | 566/566 | 100.00% | 100.00% | 100.00% |
| model:stanza-ru | eligible | Phone numbers & email | 35/442 | 7.92% | 7.92% | 7.92% |
| model:stanza-ru | eligible | Network identifiers | 3/1132 | 0.27% | 2.74% | 0.27% |
| model:traciora | eligible | Passwords, keys & tokens | 301/344 | 87.50% | 95.06% | 82.27% |
| model:traciora | eligible | Logins & usernames | 108/221 | 48.87% | 64.25% | 20.81% |
| model:traciora | eligible | People's names | 457/566 | 80.74% | 89.22% | 76.15% |
| model:traciora | eligible | Phone numbers & email | 431/442 | 97.51% | 99.10% | 93.89% |
| model:traciora | eligible | Network identifiers | 236/1132 | 20.85% | 28.53% | 20.05% |
