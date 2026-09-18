# synth-wiki-tables: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/synth-wiki-tables.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Logins & usernames | 1592/1597 | 99.69% | 99.69% | 99.69% |
| composition:fastino | eligible | People's names | 1593/1597 | 99.75% | 99.87% | 99.75% |
| composition:fastino | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| composition:fastino | eligible | Organizations | 104/300 | 34.67% | 87.67% | 34.67% |
| composition:fastino | eligible | Network identifiers | 1872/3212 | 58.28% | 58.28% | 58.28% |
| composition:fastino | eligible | Customer & employee IDs | 1268/1597 | 79.40% | 89.67% | 79.40% |
| composition:pplx | eligible | Logins & usernames | 1597/1597 | 100.00% | 100.00% | 99.69% |
| composition:pplx | eligible | People's names | 1597/1597 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| composition:pplx | eligible | Organizations | 26/300 | 8.67% | 33.00% | 8.67% |
| composition:pplx | eligible | Network identifiers | 2564/3212 | 79.83% | 83.44% | 79.83% |
| composition:pplx | eligible | Customer & employee IDs | 1064/1597 | 66.62% | 99.94% | 65.18% |
| composition:pplx+fastino | eligible | Logins & usernames | 1597/1597 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | People's names | 1597/1597 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino | eligible | Organizations | 113/300 | 37.67% | 99.33% | 37.67% |
| composition:pplx+fastino | eligible | Network identifiers | 3088/3212 | 96.14% | 97.35% | 96.14% |
| composition:pplx+fastino | eligible | Customer & employee IDs | 1268/1597 | 79.40% | 100.00% | 79.40% |
| composition:pplx+fastino+bardsai | eligible | Logins & usernames | 1597/1597 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | People's names | 1597/1597 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 154/300 | 51.33% | 100.00% | 47.00% |
| composition:pplx+fastino+bardsai | eligible | Network identifiers | 3089/3212 | 96.17% | 97.60% | 96.14% |
| composition:pplx+fastino+bardsai | eligible | Customer & employee IDs | 1268/1597 | 79.40% | 100.00% | 79.40% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Logins & usernames | 1597/1597 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 1597/1597 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 168/300 | 56.00% | 100.00% | 51.67% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Network identifiers | 3092/3212 | 96.26% | 98.91% | 96.26% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Customer & employee IDs | 1268/1597 | 79.40% | 100.00% | 79.40% |
| composition:pplx+fastino+mmbert | eligible | Logins & usernames | 1597/1597 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | People's names | 1597/1597 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 127/300 | 42.33% | 100.00% | 42.33% |
| composition:pplx+fastino+mmbert | eligible | Network identifiers | 3088/3212 | 96.14% | 98.85% | 96.14% |
| composition:pplx+fastino+mmbert | eligible | Customer & employee IDs | 1268/1597 | 79.40% | 100.00% | 79.40% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Logins & usernames | 1127/1597 | 70.57% | 78.15% | 62.74% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 1553/1597 | 97.24% | 99.69% | 93.99% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Phone numbers & email | 4736/4791 | 98.85% | 99.56% | 98.08% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 60/300 | 20.00% | 60.67% | 19.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Network identifiers | 1641/3212 | 51.09% | 56.16% | 51.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Customer & employee IDs | 944/1597 | 59.11% | 92.61% | 40.83% |
| model:apararti | eligible | Logins & usernames | 1305/1597 | 81.72% | 84.72% | 73.20% |
| model:apararti | eligible | People's names | 1518/1597 | 95.05% | 99.06% | 90.61% |
| model:apararti | eligible | Phone numbers & email | 4778/4791 | 99.73% | 99.92% | 99.44% |
| model:apararti | eligible | Organizations | 84/300 | 28.00% | 64.00% | 27.00% |
| model:apararti | eligible | Network identifiers | 1930/3212 | 60.09% | 75.03% | 56.91% |
| model:apararti | eligible | Customer & employee IDs | 1120/1597 | 70.13% | 96.99% | 61.43% |
| model:bardsai-eu | eligible | Logins & usernames | 1459/1597 | 91.36% | 94.80% | 83.84% |
| model:bardsai-eu | eligible | People's names | 1596/1597 | 99.94% | 100.00% | 98.43% |
| model:bardsai-eu | eligible | Phone numbers & email | 1842/4791 | 38.45% | 99.14% | 35.73% |
| model:bardsai-eu | eligible | Organizations | 96/300 | 32.00% | 88.33% | 27.33% |
| model:bardsai-eu | eligible | Network identifiers | 274/3212 | 8.53% | 52.40% | 7.72% |
| model:bardsai-eu | eligible | Customer & employee IDs | 704/1597 | 44.08% | 56.79% | 37.38% |
| model:davlan-mbert | eligible | Logins & usernames | 3/1597 | 0.19% | 0.25% | 0.00% |
| model:davlan-mbert | eligible | People's names | 1590/1597 | 99.56% | 99.94% | 78.33% |
| model:davlan-mbert | eligible | Phone numbers & email | 0/4791 | 0.00% | 0.21% | 0.00% |
| model:davlan-mbert | eligible | Organizations | 193/300 | 64.33% | 91.67% | 62.00% |
| model:davlan-mbert | eligible | Network identifiers | 0/3212 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | Customer & employee IDs | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Logins & usernames | 99/1597 | 6.20% | 12.65% | 2.13% |
| model:davlan-xlmr | eligible | People's names | 1597/1597 | 100.00% | 100.00% | 83.09% |
| model:davlan-xlmr | eligible | Phone numbers & email | 0/4791 | 0.00% | 11.00% | 0.00% |
| model:davlan-xlmr | eligible | Organizations | 246/300 | 82.00% | 100.00% | 77.00% |
| model:davlan-xlmr | eligible | Network identifiers | 0/3212 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | Customer & employee IDs | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | Logins & usernames | 654/1597 | 40.95% | 48.15% | 30.93% |
| model:fef2-secret-ru | eligible | People's names | 953/1597 | 59.67% | 99.94% | 48.28% |
| model:fef2-secret-ru | eligible | Phone numbers & email | 1530/4791 | 31.93% | 48.99% | 31.27% |
| model:fef2-secret-ru | eligible | Organizations | 50/300 | 16.67% | 87.67% | 11.33% |
| model:fef2-secret-ru | eligible | Network identifiers | 0/3212 | 0.00% | 2.15% | 0.00% |
| model:fef2-secret-ru | eligible | Customer & employee IDs | 65/1597 | 4.07% | 5.70% | 2.63% |
| model:gliner-multi-v21 | eligible | Logins & usernames | 362/1597 | 22.67% | 22.73% | 22.67% |
| model:gliner-multi-v21 | eligible | People's names | 1593/1597 | 99.75% | 99.75% | 99.75% |
| model:gliner-multi-v21 | eligible | Phone numbers & email | 91/4791 | 1.90% | 11.00% | 1.90% |
| model:gliner-multi-v21 | eligible | Organizations | 78/300 | 26.00% | 54.00% | 26.00% |
| model:gliner-multi-v21 | eligible | Network identifiers | 185/3212 | 5.76% | 6.66% | 5.76% |
| model:gliner-multi-v21 | eligible | Customer & employee IDs | 66/1597 | 4.13% | 4.13% | 4.13% |
| model:gliner-multi-v21-ru | eligible | Logins & usernames | 170/1597 | 10.64% | 10.64% | 10.64% |
| model:gliner-multi-v21-ru | eligible | People's names | 987/1597 | 61.80% | 61.87% | 61.80% |
| model:gliner-multi-v21-ru | eligible | Phone numbers & email | 52/4791 | 1.09% | 4.63% | 1.09% |
| model:gliner-multi-v21-ru | eligible | Organizations | 80/300 | 26.67% | 53.33% | 26.67% |
| model:gliner-multi-v21-ru | eligible | Network identifiers | 253/3212 | 7.88% | 8.00% | 7.88% |
| model:gliner-multi-v21-ru | eligible | Customer & employee IDs | 26/1597 | 1.63% | 1.63% | 1.63% |
| model:gliner-nvidia | eligible | Logins & usernames | 833/1597 | 52.16% | 52.35% | 52.16% |
| model:gliner-nvidia | eligible | People's names | 753/1597 | 47.15% | 81.65% | 45.21% |
| model:gliner-nvidia | eligible | Phone numbers & email | 2789/4791 | 58.21% | 66.85% | 58.21% |
| model:gliner-nvidia | eligible | Organizations | 152/300 | 50.67% | 79.33% | 50.67% |
| model:gliner-nvidia | eligible | Network identifiers | 1911/3212 | 59.50% | 59.50% | 59.50% |
| model:gliner-nvidia | eligible | Customer & employee IDs | 567/1597 | 35.50% | 36.32% | 35.50% |
| model:gliner-nvidia-ru | eligible | Logins & usernames | 377/1597 | 23.61% | 27.30% | 23.61% |
| model:gliner-nvidia-ru | eligible | People's names | 558/1597 | 34.94% | 60.80% | 23.92% |
| model:gliner-nvidia-ru | eligible | Phone numbers & email | 2848/4791 | 59.44% | 63.51% | 59.44% |
| model:gliner-nvidia-ru | eligible | Organizations | 116/300 | 38.67% | 57.33% | 38.67% |
| model:gliner-nvidia-ru | eligible | Network identifiers | 1281/3212 | 39.88% | 39.88% | 39.88% |
| model:gliner-nvidia-ru | eligible | Customer & employee IDs | 202/1597 | 12.65% | 23.23% | 12.65% |
| model:gliner-pii-base | eligible | Logins & usernames | 209/1597 | 13.09% | 13.09% | 13.09% |
| model:gliner-pii-base | eligible | People's names | 85/1597 | 5.32% | 5.70% | 5.32% |
| model:gliner-pii-base | eligible | Phone numbers & email | 2199/4791 | 45.90% | 45.98% | 45.90% |
| model:gliner-pii-base | eligible | Organizations | 3/300 | 1.00% | 45.00% | 1.00% |
| model:gliner-pii-base | eligible | Network identifiers | 732/3212 | 22.79% | 22.88% | 22.79% |
| model:gliner-pii-base | eligible | Customer & employee IDs | 944/1597 | 59.11% | 59.11% | 59.11% |
| model:gliner-pii-edge | eligible | Logins & usernames | 1282/1597 | 80.28% | 80.71% | 80.28% |
| model:gliner-pii-edge | eligible | People's names | 770/1597 | 48.22% | 81.03% | 47.03% |
| model:gliner-pii-edge | eligible | Phone numbers & email | 3361/4791 | 70.15% | 95.97% | 70.15% |
| model:gliner-pii-edge | eligible | Organizations | 56/300 | 18.67% | 90.00% | 18.67% |
| model:gliner-pii-edge | eligible | Network identifiers | 754/3212 | 23.47% | 43.56% | 23.10% |
| model:gliner-pii-edge | eligible | Customer & employee IDs | 1009/1597 | 63.18% | 80.96% | 63.18% |
| model:gliner-stream-pii | eligible | Logins & usernames | 477/1597 | 29.87% | 33.06% | 29.87% |
| model:gliner-stream-pii | eligible | People's names | 485/1597 | 30.37% | 31.62% | 30.37% |
| model:gliner-stream-pii | eligible | Phone numbers & email | 3942/4791 | 82.28% | 86.47% | 82.28% |
| model:gliner-stream-pii | eligible | Organizations | 162/300 | 54.00% | 54.00% | 54.00% |
| model:gliner-stream-pii | eligible | Network identifiers | 1112/3212 | 34.62% | 39.32% | 34.62% |
| model:gliner-stream-pii | eligible | Customer & employee IDs | 855/1597 | 53.54% | 54.85% | 53.54% |
| model:gliner-urchade | eligible | Logins & usernames | 1212/1597 | 75.89% | 75.89% | 75.89% |
| model:gliner-urchade | eligible | People's names | 1597/1597 | 100.00% | 100.00% | 100.00% |
| model:gliner-urchade | eligible | Phone numbers & email | 3854/4791 | 80.44% | 85.60% | 80.44% |
| model:gliner-urchade | eligible | Organizations | 250/300 | 83.33% | 96.67% | 83.33% |
| model:gliner-urchade | eligible | Network identifiers | 585/3212 | 18.21% | 18.31% | 18.21% |
| model:gliner-urchade | eligible | Customer & employee IDs | 649/1597 | 40.64% | 40.64% | 40.64% |
| model:gliner-urchade-ru | eligible | Logins & usernames | 1369/1597 | 85.72% | 85.72% | 85.72% |
| model:gliner-urchade-ru | eligible | People's names | 1/1597 | 0.06% | 0.06% | 0.06% |
| model:gliner-urchade-ru | eligible | Phone numbers & email | 4154/4791 | 86.70% | 89.65% | 86.70% |
| model:gliner-urchade-ru | eligible | Organizations | 224/300 | 74.67% | 86.33% | 74.67% |
| model:gliner-urchade-ru | eligible | Network identifiers | 524/3212 | 16.31% | 16.31% | 16.31% |
| model:gliner-urchade-ru | eligible | Customer & employee IDs | 589/1597 | 36.88% | 61.49% | 36.88% |
| model:gliner2-fastino | eligible | Logins & usernames | 1592/1597 | 99.69% | 99.69% | 99.69% |
| model:gliner2-fastino | eligible | People's names | 1593/1597 | 99.75% | 99.87% | 99.75% |
| model:gliner2-fastino | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| model:gliner2-fastino | eligible | Organizations | 104/300 | 34.67% | 87.67% | 34.67% |
| model:gliner2-fastino | eligible | Network identifiers | 1872/3212 | 58.28% | 58.28% | 58.28% |
| model:gliner2-fastino | eligible | Customer & employee IDs | 1268/1597 | 79.40% | 89.67% | 79.40% |
| model:gliner2-fastino-ru | eligible | Logins & usernames | 1597/1597 | 100.00% | 100.00% | 100.00% |
| model:gliner2-fastino-ru | eligible | People's names | 1582/1597 | 99.06% | 99.50% | 99.06% |
| model:gliner2-fastino-ru | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| model:gliner2-fastino-ru | eligible | Organizations | 103/300 | 34.33% | 84.00% | 34.33% |
| model:gliner2-fastino-ru | eligible | Network identifiers | 2010/3212 | 62.58% | 62.58% | 62.58% |
| model:gliner2-fastino-ru | eligible | Customer & employee IDs | 1091/1597 | 68.32% | 99.94% | 68.32% |
| model:gliner2-hivetrace-omni | eligible | Logins & usernames | 1157/1597 | 72.45% | 72.45% | 72.45% |
| model:gliner2-hivetrace-omni | eligible | People's names | 1597/1597 | 100.00% | 100.00% | 100.00% |
| model:gliner2-hivetrace-omni | eligible | Phone numbers & email | 4731/4791 | 98.75% | 98.75% | 98.75% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 239/300 | 79.67% | 90.33% | 79.67% |
| model:gliner2-hivetrace-omni | eligible | Network identifiers | 1397/3212 | 43.49% | 43.65% | 43.49% |
| model:gliner2-hivetrace-omni | eligible | Customer & employee IDs | 1303/1597 | 81.59% | 81.65% | 81.59% |
| model:gliner2-hivetrace-omni-ru | eligible | Logins & usernames | 839/1597 | 52.54% | 52.54% | 52.54% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 1595/1597 | 99.87% | 99.87% | 99.87% |
| model:gliner2-hivetrace-omni-ru | eligible | Phone numbers & email | 4749/4791 | 99.12% | 99.12% | 99.12% |
| model:gliner2-hivetrace-omni-ru | eligible | Organizations | 226/300 | 75.33% | 85.33% | 75.33% |
| model:gliner2-hivetrace-omni-ru | eligible | Network identifiers | 1758/3212 | 54.73% | 54.83% | 54.73% |
| model:gliner2-hivetrace-omni-ru | eligible | Customer & employee IDs | 1429/1597 | 89.48% | 93.43% | 89.48% |
| model:gliner2-hivetrace-uni | eligible | Logins & usernames | 533/1597 | 33.38% | 33.38% | 33.38% |
| model:gliner2-hivetrace-uni | eligible | People's names | 1408/1597 | 88.17% | 89.86% | 88.17% |
| model:gliner2-hivetrace-uni | eligible | Phone numbers & email | 3176/4791 | 66.29% | 66.29% | 66.29% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 62/300 | 20.67% | 46.33% | 20.67% |
| model:gliner2-hivetrace-uni | eligible | Network identifiers | 0/3212 | 0.00% | 0.44% | 0.00% |
| model:gliner2-hivetrace-uni | eligible | Customer & employee IDs | 168/1597 | 10.52% | 10.58% | 10.52% |
| model:gliner2-hivetrace-uni-ru | eligible | Logins & usernames | 130/1597 | 8.14% | 8.14% | 8.14% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 194/1597 | 12.15% | 12.15% | 12.15% |
| model:gliner2-hivetrace-uni-ru | eligible | Phone numbers & email | 226/4791 | 4.72% | 4.72% | 4.72% |
| model:gliner2-hivetrace-uni-ru | eligible | Organizations | 8/300 | 2.67% | 11.33% | 2.67% |
| model:gliner2-hivetrace-uni-ru | eligible | Network identifiers | 0/3212 | 0.00% | 0.09% | 0.00% |
| model:gliner2-hivetrace-uni-ru | eligible | Customer & employee IDs | 193/1597 | 12.09% | 12.59% | 12.09% |
| model:gliner2-large | eligible | Logins & usernames | 540/1597 | 33.81% | 33.81% | 33.81% |
| model:gliner2-large | eligible | People's names | 1439/1597 | 90.11% | 96.74% | 90.11% |
| model:gliner2-large | eligible | Phone numbers & email | 4117/4791 | 85.93% | 85.93% | 85.93% |
| model:gliner2-large | eligible | Organizations | 20/300 | 6.67% | 28.67% | 6.67% |
| model:gliner2-large | eligible | Network identifiers | 2235/3212 | 69.58% | 69.58% | 69.58% |
| model:gliner2-large | eligible | Customer & employee IDs | 1369/1597 | 85.72% | 85.72% | 85.72% |
| model:gliner2-vladlinv | eligible | Logins & usernames | 1592/1597 | 99.69% | 99.69% | 99.69% |
| model:gliner2-vladlinv | eligible | People's names | 1594/1597 | 99.81% | 99.87% | 99.81% |
| model:gliner2-vladlinv | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| model:gliner2-vladlinv | eligible | Organizations | 6/300 | 2.00% | 24.67% | 2.00% |
| model:gliner2-vladlinv | eligible | Network identifiers | 0/3212 | 0.00% | 0.00% | 0.00% |
| model:gliner2-vladlinv | eligible | Customer & employee IDs | 1065/1597 | 66.69% | 98.06% | 66.69% |
| model:gliner2-vladlinv-ru | eligible | Logins & usernames | 1594/1597 | 99.81% | 99.81% | 99.81% |
| model:gliner2-vladlinv-ru | eligible | People's names | 1596/1597 | 99.94% | 99.94% | 99.94% |
| model:gliner2-vladlinv-ru | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| model:gliner2-vladlinv-ru | eligible | Organizations | 0/300 | 0.00% | 23.00% | 0.00% |
| model:gliner2-vladlinv-ru | eligible | Network identifiers | 0/3212 | 0.00% | 0.00% | 0.00% |
| model:gliner2-vladlinv-ru | eligible | Customer & employee IDs | 1063/1597 | 66.56% | 99.87% | 66.56% |
| model:gliner25-fastino | eligible | Logins & usernames | 1009/1597 | 63.18% | 63.18% | 63.18% |
| model:gliner25-fastino | eligible | People's names | 1589/1597 | 99.50% | 100.00% | 99.50% |
| model:gliner25-fastino | eligible | Phone numbers & email | 4754/4791 | 99.23% | 99.23% | 99.23% |
| model:gliner25-fastino | eligible | Organizations | 36/300 | 12.00% | 74.00% | 12.00% |
| model:gliner25-fastino | eligible | Network identifiers | 871/3212 | 27.12% | 27.12% | 27.12% |
| model:gliner25-fastino | eligible | Customer & employee IDs | 92/1597 | 5.76% | 5.82% | 5.76% |
| model:gliner25-fastino-ru | eligible | Logins & usernames | 1159/1597 | 72.57% | 72.57% | 72.57% |
| model:gliner25-fastino-ru | eligible | People's names | 1586/1597 | 99.31% | 99.94% | 99.31% |
| model:gliner25-fastino-ru | eligible | Phone numbers & email | 4646/4791 | 96.97% | 96.97% | 96.97% |
| model:gliner25-fastino-ru | eligible | Organizations | 12/300 | 4.00% | 57.00% | 4.00% |
| model:gliner25-fastino-ru | eligible | Network identifiers | 1164/3212 | 36.24% | 36.24% | 36.24% |
| model:gliner25-fastino-ru | eligible | Customer & employee IDs | 369/1597 | 23.11% | 23.17% | 23.11% |
| model:gravitee-small | eligible | Logins & usernames | 63/1597 | 3.94% | 8.83% | 2.13% |
| model:gravitee-small | eligible | People's names | 1192/1597 | 74.64% | 80.21% | 58.67% |
| model:gravitee-small | eligible | Phone numbers & email | 2673/4791 | 55.79% | 64.48% | 54.21% |
| model:gravitee-small | eligible | Organizations | 0/300 | 0.00% | 1.67% | 0.00% |
| model:gravitee-small | eligible | Network identifiers | 874/3212 | 27.21% | 41.81% | 26.21% |
| model:gravitee-small | eligible | Customer & employee IDs | 41/1597 | 2.57% | 4.51% | 1.13% |
| model:kalyan-ettin | eligible | Logins & usernames | 1346/1597 | 84.28% | 98.62% | 70.44% |
| model:kalyan-ettin | eligible | People's names | 349/1597 | 21.85% | 98.31% | 5.45% |
| model:kalyan-ettin | eligible | Phone numbers & email | 1811/4791 | 37.80% | 88.62% | 22.54% |
| model:kalyan-ettin | eligible | Organizations | 15/300 | 5.00% | 62.33% | 1.00% |
| model:kalyan-ettin | eligible | Network identifiers | 654/3212 | 20.36% | 62.83% | 15.47% |
| model:kalyan-ettin | eligible | Customer & employee IDs | 208/1597 | 13.02% | 18.22% | 0.00% |
| model:mmbert32k | eligible | Logins & usernames | 466/1597 | 29.18% | 53.41% | 2.38% |
| model:mmbert32k | eligible | People's names | 1062/1597 | 66.50% | 98.87% | 30.56% |
| model:mmbert32k | eligible | Phone numbers & email | 1133/4791 | 23.65% | 92.05% | 12.52% |
| model:mmbert32k | eligible | Organizations | 58/300 | 19.33% | 80.33% | 14.00% |
| model:mmbert32k | eligible | Network identifiers | 402/3212 | 12.52% | 86.15% | 1.84% |
| model:mmbert32k | eligible | Customer & employee IDs | 613/1597 | 38.38% | 96.49% | 6.07% |
| model:natasha | eligible | Logins & usernames | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | People's names | 1111/1597 | 69.57% | 82.22% | 67.75% |
| model:natasha | eligible | Phone numbers & email | 0/4791 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Organizations | 177/300 | 59.00% | 91.67% | 59.00% |
| model:natasha | eligible | Network identifiers | 0/3212 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | Customer & employee IDs | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Logins & usernames | 490/1597 | 30.68% | 70.07% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 19/1597 | 1.19% | 100.00% | 0.88% |
| model:ner-ru-gherman | eligible | Phone numbers & email | 0/4791 | 0.00% | 45.13% | 0.00% |
| model:ner-ru-gherman | eligible | Organizations | 0/300 | 0.00% | 81.33% | 0.00% |
| model:ner-ru-gherman | eligible | Network identifiers | 0/3212 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | Customer & employee IDs | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | Logins & usernames | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-yqelz | eligible | People's names | 1596/1597 | 99.94% | 100.00% | 98.62% |
| model:ner-ru-yqelz | eligible | Phone numbers & email | 0/4791 | 0.00% | 1.13% | 0.00% |
| model:ner-ru-yqelz | eligible | Organizations | 275/300 | 91.67% | 99.67% | 88.00% |
| model:ner-ru-yqelz | eligible | Network identifiers | 17/3212 | 0.53% | 13.67% | 0.28% |
| model:ner-ru-yqelz | eligible | Customer & employee IDs | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:nuner-zero | eligible | Logins & usernames | 442/1597 | 27.68% | 30.62% | 27.61% |
| model:nuner-zero | eligible | People's names | 1595/1597 | 99.87% | 99.94% | 0.00% |
| model:nuner-zero | eligible | Phone numbers & email | 2231/4791 | 46.57% | 75.70% | 39.76% |
| model:nuner-zero | eligible | Organizations | 32/300 | 10.67% | 58.33% | 0.00% |
| model:nuner-zero | eligible | Network identifiers | 2800/3212 | 87.17% | 94.02% | 86.67% |
| model:nuner-zero | eligible | Customer & employee IDs | 1286/1597 | 80.53% | 88.92% | 66.56% |
| model:nym-base | eligible | Logins & usernames | 1578/1597 | 98.81% | 99.69% | 97.81% |
| model:nym-base | eligible | People's names | 0/1597 | 0.00% | 100.00% | 99.44% |
| model:nym-base | eligible | Phone numbers & email | 4613/4791 | 96.28% | 99.75% | 94.18% |
| model:nym-base | eligible | Organizations | 296/300 | 98.67% | 100.00% | 97.67% |
| model:nym-base | eligible | Network identifiers | 1425/3212 | 44.36% | 72.95% | 42.15% |
| model:nym-base | eligible | Customer & employee IDs | 1065/1597 | 66.69% | 99.31% | 66.62% |
| model:openai-base | eligible | Logins & usernames | 1514/1597 | 94.80% | 95.55% | 91.73% |
| model:openai-base | eligible | People's names | 1541/1597 | 96.49% | 98.37% | 95.62% |
| model:openai-base | eligible | Phone numbers & email | 4784/4791 | 99.85% | 99.96% | 99.67% |
| model:openai-base | eligible | Organizations | 65/300 | 21.67% | 43.67% | 21.00% |
| model:openai-base | eligible | Network identifiers | 1501/3212 | 46.73% | 63.95% | 44.71% |
| model:openai-base | eligible | Customer & employee IDs | 1187/1597 | 74.33% | 82.97% | 69.32% |
| model:openmed-multilingual | eligible | Logins & usernames | 1261/1597 | 78.96% | 83.78% | 72.70% |
| model:openmed-multilingual | eligible | People's names | 103/1597 | 6.45% | 63.43% | 12.59% |
| model:openmed-multilingual | eligible | Phone numbers & email | 3331/4791 | 69.53% | 98.56% | 68.42% |
| model:openmed-multilingual | eligible | Organizations | 0/300 | 0.00% | 23.67% | 0.00% |
| model:openmed-multilingual | eligible | Network identifiers | 2336/3212 | 72.73% | 78.67% | 72.17% |
| model:openmed-multilingual | eligible | Customer & employee IDs | 1062/1597 | 66.50% | 88.10% | 66.31% |
| model:openmed-nemotron | eligible | Logins & usernames | 1401/1597 | 87.73% | 92.49% | 77.96% |
| model:openmed-nemotron | eligible | People's names | 261/1597 | 16.34% | 98.75% | 59.36% |
| model:openmed-nemotron | eligible | Phone numbers & email | 4345/4791 | 90.69% | 97.02% | 83.24% |
| model:openmed-nemotron | eligible | Organizations | 24/300 | 8.00% | 50.33% | 2.67% |
| model:openmed-nemotron | eligible | Network identifiers | 2143/3212 | 66.72% | 76.12% | 62.45% |
| model:openmed-nemotron | eligible | Customer & employee IDs | 407/1597 | 25.49% | 70.19% | 10.52% |
| model:opf-kz-ru | eligible | Logins & usernames | 1176/1597 | 73.64% | 77.83% | 62.55% |
| model:opf-kz-ru | eligible | People's names | 1349/1597 | 84.47% | 90.92% | 75.83% |
| model:opf-kz-ru | eligible | Phone numbers & email | 4776/4791 | 99.69% | 99.96% | 99.39% |
| model:opf-kz-ru | eligible | Organizations | 35/300 | 11.67% | 30.00% | 9.33% |
| model:opf-kz-ru | eligible | Network identifiers | 1936/3212 | 60.27% | 80.01% | 57.75% |
| model:opf-kz-ru | eligible | Customer & employee IDs | 1121/1597 | 70.19% | 91.17% | 64.56% |
| model:opf-ru | eligible | Logins & usernames | 1400/1597 | 87.66% | 91.92% | 78.77% |
| model:opf-ru | eligible | People's names | 1414/1597 | 88.54% | 99.75% | 75.95% |
| model:opf-ru | eligible | Phone numbers & email | 3556/4791 | 74.22% | 99.52% | 72.36% |
| model:opf-ru | eligible | Organizations | 58/300 | 19.33% | 76.67% | 15.33% |
| model:opf-ru | eligible | Network identifiers | 21/3212 | 0.65% | 37.52% | 0.47% |
| model:opf-ru | eligible | Customer & employee IDs | 68/1597 | 4.26% | 37.82% | 0.50% |
| model:opf-ru-v2 | eligible | Logins & usernames | 684/1597 | 42.83% | 53.98% | 22.60% |
| model:opf-ru-v2 | eligible | People's names | 1529/1597 | 95.74% | 98.81% | 90.23% |
| model:opf-ru-v2 | eligible | Phone numbers & email | 4654/4791 | 97.14% | 99.33% | 95.41% |
| model:opf-ru-v2 | eligible | Organizations | 69/300 | 23.00% | 61.00% | 22.00% |
| model:opf-ru-v2 | eligible | Network identifiers | 706/3212 | 21.98% | 27.46% | 21.61% |
| model:opf-ru-v2 | eligible | Customer & employee IDs | 647/1597 | 40.51% | 85.28% | 16.28% |
| model:pplx | eligible | Logins & usernames | 1597/1597 | 100.00% | 100.00% | 99.69% |
| model:pplx | eligible | People's names | 1597/1597 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| model:pplx | eligible | Organizations | 26/300 | 8.67% | 33.00% | 8.67% |
| model:pplx | eligible | Network identifiers | 2564/3212 | 79.83% | 83.44% | 79.83% |
| model:pplx | eligible | Customer & employee IDs | 1064/1597 | 66.62% | 99.94% | 65.18% |
| model:ru-legal-ner | eligible | Logins & usernames | 1526/1597 | 95.55% | 99.87% | 83.41% |
| model:ru-legal-ner | eligible | People's names | 1570/1597 | 98.31% | 99.31% | 85.10% |
| model:ru-legal-ner | eligible | Phone numbers & email | 4347/4791 | 90.73% | 99.85% | 82.11% |
| model:ru-legal-ner | eligible | Organizations | 236/300 | 78.67% | 84.00% | 73.33% |
| model:ru-legal-ner | eligible | Network identifiers | 193/3212 | 6.01% | 86.71% | 4.36% |
| model:ru-legal-ner | eligible | Customer & employee IDs | 437/1597 | 27.36% | 82.40% | 20.41% |
| model:ru-pii-ner | eligible | Logins & usernames | 1530/1597 | 95.80% | 95.80% | 95.80% |
| model:ru-pii-ner | eligible | People's names | 1597/1597 | 100.00% | 100.00% | 100.00% |
| model:ru-pii-ner | eligible | Phone numbers & email | 4476/4791 | 93.43% | 93.74% | 92.11% |
| model:ru-pii-ner | eligible | Organizations | 34/300 | 11.33% | 32.33% | 11.33% |
| model:ru-pii-ner | eligible | Network identifiers | 30/3212 | 0.93% | 0.97% | 0.93% |
| model:ru-pii-ner | eligible | Customer & employee IDs | 1063/1597 | 66.56% | 99.12% | 55.23% |
| model:rules-ru | eligible | Logins & usernames | 894/1597 | 55.98% | 55.98% | 55.98% |
| model:rules-ru | eligible | People's names | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Phone numbers & email | 4791/4791 | 100.00% | 100.00% | 100.00% |
| model:rules-ru | eligible | Organizations | 230/300 | 76.67% | 76.67% | 76.67% |
| model:rules-ru | eligible | Network identifiers | 3212/3212 | 100.00% | 100.00% | 100.00% |
| model:rules-ru | eligible | Customer & employee IDs | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Logins & usernames | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 1539/1597 | 96.37% | 97.56% | 96.37% |
| model:spacy-alrosait | eligible | Phone numbers & email | 0/4791 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Organizations | 0/300 | 0.00% | 18.67% | 0.00% |
| model:spacy-alrosait | eligible | Network identifiers | 0/3212 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Customer & employee IDs | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Logins & usernames | 1/1597 | 0.06% | 0.06% | 0.06% |
| model:spacy-ru-lg | eligible | People's names | 285/1597 | 17.85% | 48.97% | 16.53% |
| model:spacy-ru-lg | eligible | Phone numbers & email | 11/4791 | 0.23% | 0.40% | 0.23% |
| model:spacy-ru-lg | eligible | Organizations | 104/300 | 34.67% | 76.67% | 34.67% |
| model:spacy-ru-lg | eligible | Network identifiers | 43/3212 | 1.34% | 1.53% | 1.34% |
| model:spacy-ru-lg | eligible | Customer & employee IDs | 2/1597 | 0.13% | 0.13% | 0.13% |
| model:stanza-ru | eligible | Logins & usernames | 0/1597 | 0.00% | 0.00% | 0.00% |
| model:stanza-ru | eligible | People's names | 1592/1597 | 99.69% | 100.00% | 99.69% |
| model:stanza-ru | eligible | Phone numbers & email | 1/4791 | 0.02% | 0.02% | 0.02% |
| model:stanza-ru | eligible | Organizations | 199/300 | 66.33% | 100.00% | 66.33% |
| model:stanza-ru | eligible | Network identifiers | 1/3212 | 0.03% | 0.03% | 0.03% |
| model:stanza-ru | eligible | Customer & employee IDs | 0/1597 | 0.00% | 11.90% | 0.00% |
| model:traciora | eligible | Logins & usernames | 1304/1597 | 81.65% | 89.17% | 60.61% |
| model:traciora | eligible | People's names | 1502/1597 | 94.05% | 96.74% | 91.11% |
| model:traciora | eligible | Phone numbers & email | 4623/4791 | 96.49% | 98.64% | 90.77% |
| model:traciora | eligible | Organizations | 83/300 | 27.67% | 87.67% | 26.00% |
| model:traciora | eligible | Network identifiers | 467/3212 | 14.54% | 27.90% | 13.85% |
| model:traciora | eligible | Customer & employee IDs | 575/1597 | 36.01% | 79.52% | 11.65% |
