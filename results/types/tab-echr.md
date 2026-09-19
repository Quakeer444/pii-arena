# tab-echr: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/tab-echr.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | Documents & identifiers | 311/334 | 93.11% | 93.41% | 92.51% |
| composition:fastino | eligible | People's names | 676/1030 | 65.63% | 98.93% | 65.63% |
| composition:fastino | eligible | Addresses & locations | 454/516 | 87.98% | 99.61% | 87.98% |
| composition:fastino | eligible | Organizations | 1673/1950 | 85.79% | 98.72% | 85.69% |
| composition:pplx | eligible | Documents & identifiers | 288/334 | 86.23% | 86.23% | 85.93% |
| composition:pplx | eligible | People's names | 599/1030 | 58.16% | 94.85% | 58.06% |
| composition:pplx | eligible | Addresses & locations | 164/516 | 31.78% | 33.91% | 31.59% |
| composition:pplx | eligible | Organizations | 35/1950 | 1.79% | 3.90% | 1.79% |
| composition:pplx+fastino | eligible | Documents & identifiers | 312/334 | 93.41% | 93.71% | 93.11% |
| composition:pplx+fastino | eligible | People's names | 794/1030 | 77.09% | 99.51% | 76.99% |
| composition:pplx+fastino | eligible | Addresses & locations | 474/516 | 91.86% | 99.61% | 91.86% |
| composition:pplx+fastino | eligible | Organizations | 1675/1950 | 85.90% | 98.72% | 85.79% |
| composition:pplx+fastino+bardsai | eligible | Documents & identifiers | 312/334 | 93.41% | 93.71% | 93.11% |
| composition:pplx+fastino+bardsai | eligible | People's names | 838/1030 | 81.36% | 99.61% | 80.58% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 480/516 | 93.02% | 99.61% | 93.02% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 1738/1950 | 89.13% | 98.97% | 88.97% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Documents & identifiers | 316/334 | 94.61% | 96.71% | 93.41% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 842/1030 | 81.75% | 99.61% | 82.23% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 480/516 | 93.02% | 99.61% | 93.02% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 1738/1950 | 89.13% | 98.97% | 88.97% |
| composition:pplx+fastino+mmbert | eligible | Documents & identifiers | 316/334 | 94.61% | 96.71% | 93.41% |
| composition:pplx+fastino+mmbert | eligible | People's names | 799/1030 | 77.57% | 99.51% | 77.48% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 474/516 | 91.86% | 99.61% | 91.86% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 1676/1950 | 85.95% | 98.72% | 85.85% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Documents & identifiers | 150/334 | 44.91% | 48.50% | 44.61% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 524/1030 | 50.87% | 92.52% | 50.78% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 144/516 | 27.91% | 33.53% | 27.71% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 40/1950 | 2.05% | 4.92% | 2.00% |
| model:apararti | eligible | Documents & identifiers | 116/334 | 34.73% | 42.22% | 32.93% |
| model:apararti | eligible | People's names | 834/1030 | 80.97% | 84.17% | 79.90% |
| model:apararti | eligible | Addresses & locations | 24/516 | 4.65% | 5.43% | 3.68% |
| model:apararti | eligible | Organizations | 36/1950 | 1.85% | 3.54% | 1.59% |
| model:bardsai-eu | eligible | Documents & identifiers | 79/334 | 23.65% | 36.83% | 21.56% |
| model:bardsai-eu | eligible | People's names | 522/1030 | 50.68% | 96.70% | 45.83% |
| model:bardsai-eu | eligible | Addresses & locations | 455/516 | 88.18% | 96.51% | 87.02% |
| model:bardsai-eu | eligible | Organizations | 1451/1950 | 74.41% | 87.08% | 72.87% |
| model:davlan-mbert | eligible | Documents & identifiers | 0/334 | 0.00% | 0.30% | 0.00% |
| model:davlan-mbert | eligible | People's names | 141/1030 | 13.69% | 97.57% | 13.69% |
| model:davlan-mbert | eligible | Addresses & locations | 442/516 | 85.66% | 98.45% | 85.27% |
| model:davlan-mbert | eligible | Organizations | 1478/1950 | 75.79% | 93.44% | 75.44% |
| model:davlan-mbert+cpu-int8 | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert+cpu-int8 | eligible | People's names | 140/1030 | 13.59% | 97.28% | 13.50% |
| model:davlan-mbert+cpu-int8 | eligible | Addresses & locations | 439/516 | 85.08% | 97.67% | 84.69% |
| model:davlan-mbert+cpu-int8 | eligible | Organizations | 1508/1950 | 77.33% | 93.95% | 76.56% |
| model:davlan-xlmr | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr | eligible | People's names | 155/1030 | 15.05% | 98.16% | 14.95% |
| model:davlan-xlmr | eligible | Addresses & locations | 439/516 | 85.08% | 98.06% | 84.50% |
| model:davlan-xlmr | eligible | Organizations | 1497/1950 | 76.77% | 92.26% | 75.08% |
| model:davlan-xlmr+cpu-int8 | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:davlan-xlmr+cpu-int8 | eligible | People's names | 138/1030 | 13.40% | 94.27% | 7.86% |
| model:davlan-xlmr+cpu-int8 | eligible | Addresses & locations | 402/516 | 77.91% | 93.22% | 66.67% |
| model:davlan-xlmr+cpu-int8 | eligible | Organizations | 847/1950 | 43.44% | 80.00% | 33.59% |
| model:fef2-secret-ru | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru | eligible | People's names | 4/1030 | 0.39% | 22.52% | 0.39% |
| model:fef2-secret-ru | eligible | Addresses & locations | 47/516 | 9.11% | 12.21% | 6.78% |
| model:fef2-secret-ru | eligible | Organizations | 28/1950 | 1.44% | 2.72% | 1.38% |
| model:fef2-secret-ru+cpu-int8 | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:fef2-secret-ru+cpu-int8 | eligible | People's names | 10/1030 | 0.97% | 28.35% | 0.58% |
| model:fef2-secret-ru+cpu-int8 | eligible | Addresses & locations | 41/516 | 7.95% | 10.27% | 6.01% |
| model:fef2-secret-ru+cpu-int8 | eligible | Organizations | 28/1950 | 1.44% | 2.56% | 1.28% |
| model:gliner-multi-v21 | eligible | Documents & identifiers | 165/334 | 49.40% | 50.30% | 49.40% |
| model:gliner-multi-v21 | eligible | People's names | 990/1030 | 96.12% | 96.80% | 96.12% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 448/516 | 86.82% | 96.12% | 86.82% |
| model:gliner-multi-v21 | eligible | Organizations | 1600/1950 | 82.05% | 92.00% | 82.05% |
| model:gliner-multi-v21+cpu-int8 | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | People's names | 0/1030 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Addresses & locations | 0/516 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21+cpu-int8 | eligible | Organizations | 0/1950 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia | eligible | Documents & identifiers | 159/334 | 47.60% | 47.60% | 47.60% |
| model:gliner-nvidia | eligible | People's names | 278/1030 | 26.99% | 77.57% | 26.89% |
| model:gliner-nvidia | eligible | Addresses & locations | 419/516 | 81.20% | 91.86% | 81.20% |
| model:gliner-nvidia | eligible | Organizations | 1372/1950 | 70.36% | 75.95% | 70.36% |
| model:gliner-nvidia+cpu-int8 | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | People's names | 0/1030 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Addresses & locations | 0/516 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+cpu-int8 | eligible | Organizations | 0/1950 | 0.00% | 0.00% | 0.00% |
| model:gliner-nvidia+ov100 | eligible | Documents & identifiers | 160/334 | 47.90% | 48.20% | 47.90% |
| model:gliner-nvidia+ov100 | eligible | People's names | 279/1030 | 27.09% | 77.96% | 27.09% |
| model:gliner-nvidia+ov100 | eligible | Addresses & locations | 419/516 | 81.20% | 92.25% | 80.81% |
| model:gliner-nvidia+ov100 | eligible | Organizations | 1322/1950 | 67.79% | 74.21% | 67.64% |
| model:gliner-nvidia+sent300 | eligible | Documents & identifiers | 158/334 | 47.31% | 47.31% | 47.31% |
| model:gliner-nvidia+sent300 | eligible | People's names | 339/1030 | 32.91% | 84.95% | 32.14% |
| model:gliner-nvidia+sent300 | eligible | Addresses & locations | 433/516 | 83.91% | 94.77% | 83.91% |
| model:gliner-nvidia+sent300 | eligible | Organizations | 1582/1950 | 81.13% | 85.69% | 81.13% |
| model:gliner-pii-base | eligible | Documents & identifiers | 88/334 | 26.35% | 26.35% | 26.35% |
| model:gliner-pii-base | eligible | People's names | 898/1030 | 87.18% | 88.16% | 87.18% |
| model:gliner-pii-base | eligible | Addresses & locations | 441/516 | 85.47% | 90.31% | 85.47% |
| model:gliner-pii-base | eligible | Organizations | 1547/1950 | 79.33% | 88.62% | 79.33% |
| model:gliner-pii-base+cpu-int8 | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | People's names | 0/1030 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-base+cpu-int8 | eligible | Addresses & locations | 1/516 | 0.19% | 0.19% | 0.19% |
| model:gliner-pii-base+cpu-int8 | eligible | Organizations | 89/1950 | 4.56% | 4.77% | 4.56% |
| model:gliner-pii-edge | eligible | Documents & identifiers | 4/334 | 1.20% | 1.20% | 1.20% |
| model:gliner-pii-edge | eligible | People's names | 966/1030 | 93.79% | 96.41% | 93.79% |
| model:gliner-pii-edge | eligible | Addresses & locations | 457/516 | 88.57% | 97.67% | 88.37% |
| model:gliner-pii-edge | eligible | Organizations | 1557/1950 | 79.85% | 92.26% | 79.85% |
| model:gliner-pii-edge+cpu-int8 | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:gliner-pii-edge+cpu-int8 | eligible | People's names | 50/1030 | 4.85% | 5.15% | 4.85% |
| model:gliner-pii-edge+cpu-int8 | eligible | Addresses & locations | 54/516 | 10.47% | 11.63% | 10.47% |
| model:gliner-pii-edge+cpu-int8 | eligible | Organizations | 22/1950 | 1.13% | 1.69% | 1.13% |
| model:gliner-stream-pii | eligible | Documents & identifiers | 58/334 | 17.37% | 47.01% | 8.08% |
| model:gliner-stream-pii | eligible | People's names | 695/1030 | 67.48% | 75.15% | 67.48% |
| model:gliner-stream-pii | eligible | Addresses & locations | 429/516 | 83.14% | 93.80% | 83.14% |
| model:gliner-stream-pii | eligible | Organizations | 1428/1950 | 73.23% | 85.79% | 73.13% |
| model:gliner-urchade | eligible | Documents & identifiers | 2/334 | 0.60% | 0.60% | 0.60% |
| model:gliner-urchade | eligible | People's names | 969/1030 | 94.08% | 94.76% | 94.08% |
| model:gliner-urchade | eligible | Addresses & locations | 429/516 | 83.14% | 84.50% | 83.14% |
| model:gliner-urchade | eligible | Organizations | 1544/1950 | 79.18% | 84.00% | 79.18% |
| model:gliner-urchade+cpu-int8 | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | People's names | 0/1030 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Addresses & locations | 0/516 | 0.00% | 0.00% | 0.00% |
| model:gliner-urchade+cpu-int8 | eligible | Organizations | 0/1950 | 0.00% | 0.00% | 0.00% |
| model:gliner2-fastino | eligible | Documents & identifiers | 311/334 | 93.11% | 93.41% | 92.51% |
| model:gliner2-fastino | eligible | People's names | 676/1030 | 65.63% | 98.93% | 65.63% |
| model:gliner2-fastino | eligible | Addresses & locations | 454/516 | 87.98% | 99.61% | 87.98% |
| model:gliner2-fastino | eligible | Organizations | 1673/1950 | 85.79% | 98.72% | 85.69% |
| model:gliner2-hivetrace-omni | eligible | Documents & identifiers | 297/334 | 88.92% | 88.92% | 88.62% |
| model:gliner2-hivetrace-omni | eligible | People's names | 540/1030 | 52.43% | 95.34% | 52.43% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 447/516 | 86.63% | 94.57% | 86.63% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 1452/1950 | 74.46% | 84.87% | 74.36% |
| model:gliner2-hivetrace-uni | eligible | Documents & identifiers | 15/334 | 4.49% | 4.49% | 4.49% |
| model:gliner2-hivetrace-uni | eligible | People's names | 379/1030 | 36.80% | 62.33% | 36.80% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 35/516 | 6.78% | 7.56% | 6.78% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 515/1950 | 26.41% | 29.69% | 26.41% |
| model:gliner2-large | eligible | Documents & identifiers | 206/334 | 61.68% | 61.68% | 61.38% |
| model:gliner2-large | eligible | People's names | 887/1030 | 86.12% | 96.41% | 86.12% |
| model:gliner2-large | eligible | Addresses & locations | 449/516 | 87.02% | 98.84% | 87.02% |
| model:gliner2-large | eligible | Organizations | 1653/1950 | 84.77% | 96.41% | 84.67% |
| model:gliner2-vladlinv | eligible | Documents & identifiers | 5/334 | 1.50% | 1.50% | 1.50% |
| model:gliner2-vladlinv | eligible | People's names | 548/1030 | 53.20% | 95.44% | 53.11% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 162/516 | 31.40% | 33.14% | 31.40% |
| model:gliner2-vladlinv | eligible | Organizations | 18/1950 | 0.92% | 1.49% | 0.92% |
| model:gliner25-fastino | eligible | Documents & identifiers | 298/334 | 89.22% | 89.82% | 89.22% |
| model:gliner25-fastino | eligible | People's names | 933/1030 | 90.58% | 98.25% | 90.49% |
| model:gliner25-fastino | eligible | Addresses & locations | 450/516 | 87.21% | 98.45% | 87.21% |
| model:gliner25-fastino | eligible | Organizations | 1645/1950 | 84.36% | 95.23% | 84.31% |
| model:gliner25-fastino+nochunk | eligible | Documents & identifiers | 133/334 | 39.82% | 40.42% | 39.82% |
| model:gliner25-fastino+nochunk | eligible | People's names | 638/1030 | 61.94% | 63.59% | 61.94% |
| model:gliner25-fastino+nochunk | eligible | Addresses & locations | 391/516 | 75.78% | 87.40% | 75.78% |
| model:gliner25-fastino+nochunk | eligible | Organizations | 990/1950 | 50.77% | 60.21% | 50.77% |
| model:gliner25-fastino+ov100 | eligible | Documents & identifiers | 295/334 | 88.32% | 90.12% | 88.32% |
| model:gliner25-fastino+ov100 | eligible | People's names | 954/1030 | 92.62% | 97.18% | 92.62% |
| model:gliner25-fastino+ov100 | eligible | Addresses & locations | 449/516 | 87.02% | 98.06% | 86.63% |
| model:gliner25-fastino+ov100 | eligible | Organizations | 1660/1950 | 85.13% | 95.59% | 85.08% |
| model:gliner25-fastino+sent300 | eligible | Documents & identifiers | 307/334 | 91.92% | 92.51% | 91.92% |
| model:gliner25-fastino+sent300 | eligible | People's names | 842/1030 | 81.75% | 98.93% | 77.38% |
| model:gliner25-fastino+sent300 | eligible | Addresses & locations | 454/516 | 87.98% | 99.22% | 87.98% |
| model:gliner25-fastino+sent300 | eligible | Organizations | 1656/1950 | 84.92% | 96.00% | 84.92% |
| model:gravitee-small | eligible | Documents & identifiers | 20/334 | 5.99% | 10.78% | 5.39% |
| model:gravitee-small | eligible | People's names | 735/1030 | 71.36% | 88.16% | 58.16% |
| model:gravitee-small | eligible | Addresses & locations | 349/516 | 67.64% | 75.97% | 64.73% |
| model:gravitee-small | eligible | Organizations | 464/1950 | 23.79% | 42.41% | 22.92% |
| model:gravitee-small+cpu-int8 | eligible | Documents & identifiers | 26/334 | 7.78% | 12.57% | 6.89% |
| model:gravitee-small+cpu-int8 | eligible | People's names | 723/1030 | 70.19% | 88.16% | 56.02% |
| model:gravitee-small+cpu-int8 | eligible | Addresses & locations | 327/516 | 63.37% | 70.74% | 60.85% |
| model:gravitee-small+cpu-int8 | eligible | Organizations | 462/1950 | 23.69% | 41.95% | 22.72% |
| model:kalyan-ettin | eligible | Documents & identifiers | 13/334 | 3.89% | 26.95% | 0.90% |
| model:kalyan-ettin | eligible | People's names | 27/1030 | 2.62% | 90.00% | 6.60% |
| model:kalyan-ettin | eligible | Addresses & locations | 308/516 | 59.69% | 71.71% | 54.26% |
| model:kalyan-ettin | eligible | Organizations | 122/1950 | 6.26% | 31.54% | 5.13% |
| model:kalyan-ettin+cpu-int8 | eligible | Documents & identifiers | 7/334 | 2.10% | 12.28% | 0.30% |
| model:kalyan-ettin+cpu-int8 | eligible | People's names | 21/1030 | 2.04% | 62.04% | 2.72% |
| model:kalyan-ettin+cpu-int8 | eligible | Addresses & locations | 210/516 | 40.70% | 52.71% | 27.13% |
| model:kalyan-ettin+cpu-int8 | eligible | Organizations | 61/1950 | 3.13% | 19.13% | 2.26% |
| model:mmbert32k | eligible | Documents & identifiers | 185/334 | 55.39% | 94.01% | 12.87% |
| model:mmbert32k | eligible | People's names | 149/1030 | 14.47% | 92.14% | 14.56% |
| model:mmbert32k | eligible | Addresses & locations | 138/516 | 26.74% | 34.50% | 22.29% |
| model:mmbert32k | eligible | Organizations | 85/1950 | 4.36% | 19.18% | 2.82% |
| model:mmbert32k+cpu-int8 | eligible | Documents & identifiers | 36/334 | 10.78% | 80.84% | 0.60% |
| model:mmbert32k+cpu-int8 | eligible | People's names | 45/1030 | 4.37% | 63.50% | 3.98% |
| model:mmbert32k+cpu-int8 | eligible | Addresses & locations | 100/516 | 19.38% | 28.49% | 11.24% |
| model:mmbert32k+cpu-int8 | eligible | Organizations | 46/1950 | 2.36% | 14.26% | 0.56% |
| model:mmbert32k+nochunk | eligible | Documents & identifiers | 145/334 | 43.41% | 89.52% | 11.98% |
| model:mmbert32k+nochunk | eligible | People's names | 75/1030 | 7.28% | 84.76% | 7.18% |
| model:mmbert32k+nochunk | eligible | Addresses & locations | 74/516 | 14.34% | 22.29% | 6.98% |
| model:mmbert32k+nochunk | eligible | Organizations | 40/1950 | 2.05% | 8.97% | 0.36% |
| model:natasha | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:natasha | eligible | People's names | 337/1030 | 32.72% | 33.40% | 32.72% |
| model:natasha | eligible | Addresses & locations | 113/516 | 21.90% | 28.68% | 21.90% |
| model:natasha | eligible | Organizations | 99/1950 | 5.08% | 5.38% | 5.08% |
| model:ner-ru-gherman | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman | eligible | People's names | 29/1030 | 2.82% | 89.81% | 2.72% |
| model:ner-ru-gherman | eligible | Addresses & locations | 406/516 | 78.68% | 94.77% | 76.74% |
| model:ner-ru-gherman | eligible | Organizations | 147/1950 | 7.54% | 37.59% | 4.72% |
| model:ner-ru-gherman+cpu-int8 | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman+cpu-int8 | eligible | People's names | 29/1030 | 2.82% | 89.42% | 2.72% |
| model:ner-ru-gherman+cpu-int8 | eligible | Addresses & locations | 408/516 | 79.07% | 94.19% | 77.52% |
| model:ner-ru-gherman+cpu-int8 | eligible | Organizations | 92/1950 | 4.72% | 36.97% | 4.36% |
| model:ner-ru-gherman-onnx | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:ner-ru-gherman-onnx | eligible | People's names | 29/1030 | 2.82% | 89.81% | 2.72% |
| model:ner-ru-gherman-onnx | eligible | Addresses & locations | 406/516 | 78.68% | 94.96% | 76.74% |
| model:ner-ru-gherman-onnx | eligible | Organizations | 116/1950 | 5.95% | 37.33% | 4.56% |
| model:ner-ru-yqelz | eligible | Documents & identifiers | 0/334 | 0.00% | 0.90% | 0.00% |
| model:ner-ru-yqelz | eligible | People's names | 476/1030 | 46.21% | 74.85% | 18.54% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 433/516 | 83.91% | 94.57% | 82.56% |
| model:ner-ru-yqelz | eligible | Organizations | 1215/1950 | 62.31% | 83.08% | 59.54% |
| model:nuner-zero | eligible | Documents & identifiers | 271/334 | 81.14% | 85.03% | 79.64% |
| model:nuner-zero | eligible | People's names | 866/1030 | 84.08% | 96.80% | 9.13% |
| model:nuner-zero | eligible | Addresses & locations | 451/516 | 87.40% | 98.45% | 75.19% |
| model:nuner-zero | eligible | Organizations | 1652/1950 | 84.72% | 97.08% | 13.59% |
| model:nym-base | eligible | Documents & identifiers | 257/334 | 76.95% | 81.44% | 49.10% |
| model:nym-base | eligible | People's names | 363/1030 | 35.24% | 95.83% | 56.60% |
| model:nym-base | eligible | Addresses & locations | 438/516 | 84.88% | 96.32% | 85.66% |
| model:nym-base | eligible | Organizations | 617/1950 | 31.64% | 59.33% | 38.15% |
| model:nym-base+cpu-int8 | eligible | Documents & identifiers | 243/334 | 72.75% | 83.53% | 42.22% |
| model:nym-base+cpu-int8 | eligible | People's names | 336/1030 | 32.62% | 95.44% | 53.50% |
| model:nym-base+cpu-int8 | eligible | Addresses & locations | 428/516 | 82.95% | 95.35% | 84.11% |
| model:nym-base+cpu-int8 | eligible | Organizations | 582/1950 | 29.85% | 57.03% | 35.08% |
| model:nym-base+ov100 | eligible | Documents & identifiers | 262/334 | 78.44% | 81.74% | 53.59% |
| model:nym-base+ov100 | eligible | People's names | 400/1030 | 38.83% | 95.92% | 65.05% |
| model:nym-base+ov100 | eligible | Addresses & locations | 441/516 | 85.47% | 97.09% | 87.02% |
| model:nym-base+ov100 | eligible | Organizations | 665/1950 | 34.10% | 60.82% | 39.33% |
| model:nym-base+sent300 | eligible | Documents & identifiers | 234/334 | 70.06% | 79.04% | 65.57% |
| model:nym-base+sent300 | eligible | People's names | 296/1030 | 28.74% | 94.56% | 50.10% |
| model:nym-base+sent300 | eligible | Addresses & locations | 429/516 | 83.14% | 95.16% | 84.30% |
| model:nym-base+sent300 | eligible | Organizations | 547/1950 | 28.05% | 56.26% | 36.67% |
| model:nym-small | eligible | Documents & identifiers | 199/334 | 59.58% | 75.15% | 20.06% |
| model:nym-small | eligible | People's names | 433/1030 | 42.04% | 96.41% | 55.53% |
| model:nym-small | eligible | Addresses & locations | 435/516 | 84.30% | 96.71% | 85.27% |
| model:nym-small | eligible | Organizations | 628/1950 | 32.21% | 62.10% | 43.38% |
| model:openai-base | eligible | Documents & identifiers | 94/334 | 28.14% | 28.44% | 27.84% |
| model:openai-base | eligible | People's names | 733/1030 | 71.17% | 73.50% | 70.78% |
| model:openai-base | eligible | Addresses & locations | 12/516 | 2.33% | 2.33% | 1.94% |
| model:openai-base | eligible | Organizations | 12/1950 | 0.62% | 1.13% | 0.62% |
| model:openai-base-onnx | eligible | Documents & identifiers | 94/334 | 28.14% | 28.44% | 27.84% |
| model:openai-base-onnx | eligible | People's names | 738/1030 | 71.65% | 73.59% | 71.36% |
| model:openai-base-onnx | eligible | Addresses & locations | 11/516 | 2.13% | 2.33% | 1.94% |
| model:openai-base-onnx | eligible | Organizations | 13/1950 | 0.67% | 1.13% | 0.62% |
| model:openmed-multilingual | eligible | Documents & identifiers | 166/334 | 49.70% | 80.84% | 38.02% |
| model:openmed-multilingual | eligible | People's names | 144/1030 | 13.98% | 92.43% | 45.53% |
| model:openmed-multilingual | eligible | Addresses & locations | 393/516 | 76.16% | 88.57% | 75.00% |
| model:openmed-multilingual | eligible | Organizations | 222/1950 | 11.38% | 40.10% | 10.77% |
| model:openmed-nemotron | eligible | Documents & identifiers | 17/334 | 5.09% | 23.65% | 2.10% |
| model:openmed-nemotron | eligible | People's names | 48/1030 | 4.66% | 91.84% | 21.07% |
| model:openmed-nemotron | eligible | Addresses & locations | 356/516 | 68.99% | 80.62% | 65.31% |
| model:openmed-nemotron | eligible | Organizations | 152/1950 | 7.79% | 33.33% | 7.38% |
| model:opf-kz-ru | eligible | Documents & identifiers | 143/334 | 42.81% | 52.10% | 42.22% |
| model:opf-kz-ru | eligible | People's names | 721/1030 | 70.00% | 76.41% | 69.03% |
| model:opf-kz-ru | eligible | Addresses & locations | 10/516 | 1.94% | 2.33% | 1.74% |
| model:opf-kz-ru | eligible | Organizations | 19/1950 | 0.97% | 2.72% | 0.51% |
| model:opf-ru | eligible | Documents & identifiers | 35/334 | 10.48% | 27.25% | 5.39% |
| model:opf-ru | eligible | People's names | 649/1030 | 63.01% | 78.74% | 61.36% |
| model:opf-ru | eligible | Addresses & locations | 28/516 | 5.43% | 7.36% | 3.49% |
| model:opf-ru | eligible | Organizations | 39/1950 | 2.00% | 4.92% | 1.28% |
| model:opf-ru-v2 | eligible | Documents & identifiers | 1/334 | 0.30% | 4.49% | 0.00% |
| model:opf-ru-v2 | eligible | People's names | 716/1030 | 69.51% | 74.66% | 68.54% |
| model:opf-ru-v2 | eligible | Addresses & locations | 7/516 | 1.36% | 1.94% | 1.16% |
| model:opf-ru-v2 | eligible | Organizations | 11/1950 | 0.56% | 1.85% | 0.46% |
| model:opf-ru-v2+ov100 | eligible | Documents & identifiers | 3/334 | 0.90% | 5.99% | 0.30% |
| model:opf-ru-v2+ov100 | eligible | People's names | 730/1030 | 70.87% | 76.99% | 69.42% |
| model:opf-ru-v2+ov100 | eligible | Addresses & locations | 10/516 | 1.94% | 1.94% | 1.94% |
| model:opf-ru-v2+ov100 | eligible | Organizations | 14/1950 | 0.72% | 2.51% | 0.62% |
| model:opf-ru-v2+sent300 | eligible | Documents & identifiers | 3/334 | 0.90% | 7.19% | 0.30% |
| model:opf-ru-v2+sent300 | eligible | People's names | 701/1030 | 68.06% | 76.80% | 67.18% |
| model:opf-ru-v2+sent300 | eligible | Addresses & locations | 5/516 | 0.97% | 1.55% | 0.97% |
| model:opf-ru-v2+sent300 | eligible | Organizations | 21/1950 | 1.08% | 2.56% | 0.82% |
| model:pii-shield-onnx | eligible | Documents & identifiers | 94/334 | 28.14% | 63.77% | 12.57% |
| model:pii-shield-onnx | eligible | People's names | 53/1030 | 5.15% | 36.50% | 3.30% |
| model:pii-shield-onnx | eligible | Addresses & locations | 254/516 | 49.22% | 60.08% | 37.98% |
| model:pii-shield-onnx | eligible | Organizations | 74/1950 | 3.79% | 14.00% | 2.41% |
| model:pplx | eligible | Documents & identifiers | 288/334 | 86.23% | 86.23% | 85.93% |
| model:pplx | eligible | People's names | 599/1030 | 58.16% | 94.85% | 58.06% |
| model:pplx | eligible | Addresses & locations | 164/516 | 31.78% | 33.91% | 31.59% |
| model:pplx | eligible | Organizations | 35/1950 | 1.79% | 3.90% | 1.79% |
| model:pplx+cpu-int8 | eligible | Documents & identifiers | 327/334 | 97.90% | 98.20% | 97.60% |
| model:pplx+cpu-int8 | eligible | People's names | 903/1030 | 87.67% | 98.93% | 87.48% |
| model:pplx+cpu-int8 | eligible | Addresses & locations | 377/516 | 73.06% | 74.61% | 73.06% |
| model:pplx+cpu-int8 | eligible | Organizations | 228/1950 | 11.69% | 23.74% | 11.69% |
| model:pplx+ov100 | eligible | Documents & identifiers | 294/334 | 88.02% | 88.02% | 87.72% |
| model:pplx+ov100 | eligible | People's names | 581/1030 | 56.41% | 96.31% | 56.31% |
| model:pplx+ov100 | eligible | Addresses & locations | 213/516 | 41.28% | 45.16% | 41.09% |
| model:pplx+ov100 | eligible | Organizations | 48/1950 | 2.46% | 8.97% | 2.46% |
| model:pplx+sent300 | eligible | Documents & identifiers | 236/334 | 70.66% | 71.26% | 70.66% |
| model:pplx+sent300 | eligible | People's names | 487/1030 | 47.28% | 94.85% | 45.24% |
| model:pplx+sent300 | eligible | Addresses & locations | 287/516 | 55.62% | 64.92% | 55.62% |
| model:pplx+sent300 | eligible | Organizations | 78/1950 | 4.00% | 13.54% | 4.00% |
| model:ru-legal-ner | eligible | Documents & identifiers | 124/334 | 37.13% | 53.59% | 37.13% |
| model:ru-legal-ner | eligible | People's names | 60/1030 | 5.83% | 40.49% | 3.69% |
| model:ru-legal-ner | eligible | Addresses & locations | 30/516 | 5.81% | 7.36% | 1.74% |
| model:ru-legal-ner | eligible | Organizations | 13/1950 | 0.67% | 5.95% | 0.10% |
| model:ru-legal-ner+cpu-int8 | eligible | Documents & identifiers | 128/334 | 38.32% | 53.59% | 37.13% |
| model:ru-legal-ner+cpu-int8 | eligible | People's names | 60/1030 | 5.83% | 41.26% | 3.98% |
| model:ru-legal-ner+cpu-int8 | eligible | Addresses & locations | 35/516 | 6.78% | 7.95% | 1.94% |
| model:ru-legal-ner+cpu-int8 | eligible | Organizations | 10/1950 | 0.51% | 6.05% | 0.10% |
| model:ru-legal-ner+ov100 | eligible | Documents & identifiers | 136/334 | 40.72% | 56.89% | 37.72% |
| model:ru-legal-ner+ov100 | eligible | People's names | 66/1030 | 6.41% | 40.78% | 4.56% |
| model:ru-legal-ner+ov100 | eligible | Addresses & locations | 24/516 | 4.65% | 6.59% | 0.97% |
| model:ru-legal-ner+ov100 | eligible | Organizations | 16/1950 | 0.82% | 4.67% | 0.00% |
| model:ru-legal-ner+sent300 | eligible | Documents & identifiers | 96/334 | 28.74% | 57.19% | 26.65% |
| model:ru-legal-ner+sent300 | eligible | People's names | 104/1030 | 10.10% | 49.13% | 8.06% |
| model:ru-legal-ner+sent300 | eligible | Addresses & locations | 61/516 | 11.82% | 17.44% | 6.40% |
| model:ru-legal-ner+sent300 | eligible | Organizations | 35/1950 | 1.79% | 11.23% | 0.72% |
| model:ru-pii-ner | eligible | Documents & identifiers | 48/334 | 14.37% | 14.67% | 14.37% |
| model:ru-pii-ner | eligible | People's names | 371/1030 | 36.02% | 89.22% | 35.92% |
| model:ru-pii-ner | eligible | Addresses & locations | 152/516 | 29.46% | 29.65% | 29.46% |
| model:ru-pii-ner | eligible | Organizations | 32/1950 | 1.64% | 2.10% | 1.64% |
| model:rules-ru | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | People's names | 0/1030 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Addresses & locations | 0/516 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Organizations | 0/1950 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 0/1030 | 0.00% | 0.10% | 0.00% |
| model:spacy-alrosait | eligible | Addresses & locations | 0/516 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | Organizations | 0/1950 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | Documents & identifiers | 0/334 | 0.00% | 0.00% | 0.00% |
| model:spacy-ru-lg | eligible | People's names | 569/1030 | 55.24% | 55.44% | 55.15% |
| model:spacy-ru-lg | eligible | Addresses & locations | 71/516 | 13.76% | 20.54% | 13.76% |
| model:spacy-ru-lg | eligible | Organizations | 331/1950 | 16.97% | 17.49% | 16.97% |
| model:stanza-ru | eligible | Documents & identifiers | 2/334 | 0.60% | 1.50% | 0.60% |
| model:stanza-ru | eligible | People's names | 920/1030 | 89.32% | 93.50% | 88.93% |
| model:stanza-ru | eligible | Addresses & locations | 395/516 | 76.55% | 86.43% | 76.55% |
| model:stanza-ru | eligible | Organizations | 1642/1950 | 84.21% | 92.46% | 83.95% |
| model:traciora | eligible | Documents & identifiers | 1/334 | 0.30% | 2.10% | 0.00% |
| model:traciora | eligible | People's names | 611/1030 | 59.32% | 69.51% | 58.06% |
| model:traciora | eligible | Addresses & locations | 23/516 | 4.46% | 6.01% | 3.49% |
| model:traciora | eligible | Organizations | 14/1950 | 0.72% | 1.85% | 0.62% |
