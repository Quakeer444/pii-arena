# factrueval: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/factrueval.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | People's names | 2204/3369 | 65.42% | 65.75% | 65.39% |
| composition:fastino | eligible | Addresses & locations | 2324/2396 | 96.99% | 97.75% | 96.66% |
| composition:fastino | eligible | Organizations | 1997/2201 | 90.73% | 93.00% | 90.55% |
| composition:pplx | eligible | People's names | 989/3369 | 29.36% | 29.36% | 28.94% |
| composition:pplx | eligible | Addresses & locations | 10/2396 | 0.42% | 0.42% | 0.42% |
| composition:pplx | eligible | Organizations | 3/2201 | 0.14% | 0.14% | 0.14% |
| composition:pplx+fastino | eligible | People's names | 2439/3369 | 72.40% | 72.60% | 72.31% |
| composition:pplx+fastino | eligible | Addresses & locations | 2324/2396 | 96.99% | 97.75% | 96.66% |
| composition:pplx+fastino | eligible | Organizations | 1997/2201 | 90.73% | 93.00% | 90.55% |
| composition:pplx+fastino+bardsai | eligible | People's names | 3342/3369 | 99.20% | 99.23% | 98.34% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 2359/2396 | 98.46% | 98.83% | 97.87% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 2098/2201 | 95.32% | 96.96% | 94.64% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 3353/3369 | 99.53% | 99.55% | 98.49% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 2359/2396 | 98.46% | 98.83% | 97.95% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 2099/2201 | 95.37% | 97.05% | 94.68% |
| composition:pplx+fastino+mmbert | eligible | People's names | 3068/3369 | 91.07% | 91.63% | 78.09% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 2330/2396 | 97.25% | 98.08% | 96.79% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 2014/2201 | 91.50% | 94.05% | 90.91% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 1901/3369 | 56.43% | 56.69% | 53.07% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 79/2396 | 3.30% | 3.67% | 2.42% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 70/2201 | 3.18% | 4.04% | 2.27% |
| model:apararti | eligible | People's names | 1700/3369 | 50.46% | 50.70% | 42.45% |
| model:apararti | eligible | Addresses & locations | 192/2396 | 8.01% | 8.60% | 5.63% |
| model:apararti | eligible | Organizations | 162/2201 | 7.36% | 9.09% | 5.45% |
| model:bardsai-eu | eligible | People's names | 3307/3369 | 98.16% | 98.19% | 96.11% |
| model:bardsai-eu | eligible | Addresses & locations | 2182/2396 | 91.07% | 92.15% | 87.23% |
| model:bardsai-eu | eligible | Organizations | 1916/2201 | 87.05% | 90.14% | 84.51% |
| model:davlan-mbert | eligible | People's names | 3323/3369 | 98.63% | 98.69% | 95.90% |
| model:davlan-mbert | eligible | Addresses & locations | 2286/2396 | 95.41% | 96.45% | 93.49% |
| model:davlan-mbert | eligible | Organizations | 1876/2201 | 85.23% | 89.32% | 82.74% |
| model:davlan-xlmr | eligible | People's names | 3311/3369 | 98.28% | 98.31% | 95.07% |
| model:davlan-xlmr | eligible | Addresses & locations | 2317/2396 | 96.70% | 97.62% | 93.70% |
| model:davlan-xlmr | eligible | Organizations | 1918/2201 | 87.14% | 90.78% | 85.28% |
| model:fef2-secret-ru | eligible | People's names | 3305/3369 | 98.10% | 98.16% | 97.77% |
| model:fef2-secret-ru | eligible | Addresses & locations | 2343/2396 | 97.79% | 98.50% | 96.91% |
| model:fef2-secret-ru | eligible | Organizations | 1946/2201 | 88.41% | 92.09% | 87.60% |
| model:gliner-multi-v21 | eligible | People's names | 2454/3369 | 72.84% | 72.90% | 72.81% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 1855/2396 | 77.42% | 78.09% | 77.25% |
| model:gliner-multi-v21 | eligible | Organizations | 1697/2201 | 77.10% | 79.42% | 76.97% |
| model:gliner-multi-v21-ru | eligible | People's names | 2520/3369 | 74.80% | 74.86% | 74.77% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 1597/2396 | 66.65% | 67.32% | 66.53% |
| model:gliner-multi-v21-ru | eligible | Organizations | 1669/2201 | 75.83% | 77.96% | 75.78% |
| model:gliner-nvidia | eligible | People's names | 2935/3369 | 87.12% | 87.86% | 87.09% |
| model:gliner-nvidia | eligible | Addresses & locations | 1674/2396 | 69.87% | 70.58% | 69.74% |
| model:gliner-nvidia | eligible | Organizations | 1266/2201 | 57.52% | 59.52% | 57.38% |
| model:gliner-nvidia+ov100 | eligible | People's names | 2960/3369 | 87.86% | 88.51% | 87.74% |
| model:gliner-nvidia+ov100 | eligible | Addresses & locations | 1681/2396 | 70.16% | 70.87% | 69.82% |
| model:gliner-nvidia+ov100 | eligible | Organizations | 1237/2201 | 56.20% | 58.52% | 56.02% |
| model:gliner-nvidia+sent300 | eligible | People's names | 3004/3369 | 89.17% | 89.91% | 89.11% |
| model:gliner-nvidia+sent300 | eligible | Addresses & locations | 1941/2396 | 81.01% | 81.76% | 80.80% |
| model:gliner-nvidia+sent300 | eligible | Organizations | 1496/2201 | 67.97% | 70.10% | 67.92% |
| model:gliner-nvidia-ru | eligible | People's names | 2382/3369 | 70.70% | 71.21% | 70.67% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 823/2396 | 34.35% | 34.89% | 34.35% |
| model:gliner-nvidia-ru | eligible | Organizations | 980/2201 | 44.53% | 45.71% | 44.48% |
| model:gliner-pii-base | eligible | People's names | 317/3369 | 9.41% | 9.50% | 9.41% |
| model:gliner-pii-base | eligible | Addresses & locations | 1477/2396 | 61.64% | 62.35% | 61.60% |
| model:gliner-pii-base | eligible | Organizations | 1448/2201 | 65.79% | 69.56% | 65.61% |
| model:gliner-pii-edge | eligible | People's names | 2726/3369 | 80.91% | 81.09% | 80.91% |
| model:gliner-pii-edge | eligible | Addresses & locations | 2099/2396 | 87.60% | 89.98% | 87.56% |
| model:gliner-pii-edge | eligible | Organizations | 1670/2201 | 75.87% | 84.10% | 75.69% |
| model:gliner-stream-pii | eligible | People's names | 731/3369 | 21.70% | 21.96% | 21.70% |
| model:gliner-stream-pii | eligible | Addresses & locations | 1481/2396 | 61.81% | 63.27% | 61.73% |
| model:gliner-stream-pii | eligible | Organizations | 1065/2201 | 48.39% | 52.89% | 48.30% |
| model:gliner-urchade | eligible | People's names | 120/3369 | 3.56% | 3.62% | 3.56% |
| model:gliner-urchade | eligible | Addresses & locations | 1367/2396 | 57.05% | 57.55% | 57.05% |
| model:gliner-urchade | eligible | Organizations | 1705/2201 | 77.46% | 78.69% | 77.37% |
| model:gliner-urchade-ru | eligible | People's names | 97/3369 | 2.88% | 2.88% | 2.88% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 1198/2396 | 50.00% | 50.50% | 50.00% |
| model:gliner-urchade-ru | eligible | Organizations | 1663/2201 | 75.56% | 76.56% | 75.47% |
| model:gliner2-fastino | eligible | People's names | 2204/3369 | 65.42% | 65.75% | 65.39% |
| model:gliner2-fastino | eligible | Addresses & locations | 2324/2396 | 96.99% | 97.75% | 96.66% |
| model:gliner2-fastino | eligible | Organizations | 1997/2201 | 90.73% | 93.00% | 90.55% |
| model:gliner2-fastino-ru | eligible | People's names | 2681/3369 | 79.58% | 79.64% | 79.55% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 2247/2396 | 93.78% | 94.41% | 93.49% |
| model:gliner2-fastino-ru | eligible | Organizations | 2007/2201 | 91.19% | 93.18% | 91.05% |
| model:gliner2-hivetrace-omni | eligible | People's names | 2385/3369 | 70.79% | 71.42% | 70.76% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 1553/2396 | 64.82% | 65.28% | 64.77% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 1623/2201 | 73.74% | 75.74% | 73.60% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 2282/3369 | 67.74% | 67.85% | 67.74% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 1517/2396 | 63.31% | 63.77% | 63.27% |
| model:gliner2-hivetrace-omni-ru | eligible | Organizations | 1617/2201 | 73.47% | 75.60% | 73.38% |
| model:gliner2-hivetrace-uni | eligible | People's names | 469/3369 | 13.92% | 13.92% | 13.92% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 157/2396 | 6.55% | 6.72% | 6.55% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 490/2201 | 22.26% | 22.90% | 22.26% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 1861/3369 | 55.24% | 55.39% | 55.24% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 242/2396 | 10.10% | 10.31% | 10.10% |
| model:gliner2-hivetrace-uni-ru | eligible | Organizations | 935/2201 | 42.48% | 43.39% | 42.44% |
| model:gliner2-large | eligible | People's names | 2247/3369 | 66.70% | 66.79% | 66.67% |
| model:gliner2-large | eligible | Addresses & locations | 1811/2396 | 75.58% | 76.09% | 75.46% |
| model:gliner2-large | eligible | Organizations | 1566/2201 | 71.15% | 73.92% | 71.10% |
| model:gliner2-vladlinv | eligible | People's names | 2564/3369 | 76.11% | 76.19% | 76.08% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 77/2396 | 3.21% | 3.34% | 3.21% |
| model:gliner2-vladlinv | eligible | Organizations | 21/2201 | 0.95% | 1.14% | 0.95% |
| model:gliner2-vladlinv-ru | eligible | People's names | 2425/3369 | 71.98% | 72.01% | 71.92% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 67/2396 | 2.80% | 2.88% | 2.80% |
| model:gliner2-vladlinv-ru | eligible | Organizations | 17/2201 | 0.77% | 0.86% | 0.77% |
| model:gliner25-fastino | eligible | People's names | 432/3369 | 12.82% | 12.85% | 12.82% |
| model:gliner25-fastino | eligible | Addresses & locations | 2193/2396 | 91.53% | 92.40% | 91.36% |
| model:gliner25-fastino | eligible | Organizations | 1833/2201 | 83.28% | 84.92% | 83.19% |
| model:gliner25-fastino+nochunk | eligible | People's names | 216/3369 | 6.41% | 6.44% | 6.41% |
| model:gliner25-fastino+nochunk | eligible | Addresses & locations | 1708/2396 | 71.29% | 72.33% | 71.24% |
| model:gliner25-fastino+nochunk | eligible | Organizations | 1549/2201 | 70.38% | 72.33% | 70.38% |
| model:gliner25-fastino+ov100 | eligible | People's names | 425/3369 | 12.62% | 12.67% | 12.50% |
| model:gliner25-fastino+ov100 | eligible | Addresses & locations | 2186/2396 | 91.24% | 92.03% | 91.11% |
| model:gliner25-fastino+ov100 | eligible | Organizations | 1836/2201 | 83.42% | 84.92% | 83.19% |
| model:gliner25-fastino+sent300 | eligible | People's names | 613/3369 | 18.20% | 18.28% | 18.20% |
| model:gliner25-fastino+sent300 | eligible | Addresses & locations | 2218/2396 | 92.57% | 93.49% | 92.49% |
| model:gliner25-fastino+sent300 | eligible | Organizations | 1878/2201 | 85.32% | 86.69% | 85.28% |
| model:gliner25-fastino-ru | eligible | People's names | 2643/3369 | 78.45% | 78.48% | 78.42% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 1754/2396 | 73.21% | 74.04% | 73.21% |
| model:gliner25-fastino-ru | eligible | Organizations | 1780/2201 | 80.87% | 82.37% | 80.78% |
| model:gliner25-fastino-ru+nochunk | eligible | People's names | 1188/3369 | 35.26% | 35.26% | 35.23% |
| model:gliner25-fastino-ru+nochunk | eligible | Addresses & locations | 1338/2396 | 55.84% | 56.89% | 55.80% |
| model:gliner25-fastino-ru+nochunk | eligible | Organizations | 1516/2201 | 68.88% | 70.51% | 68.88% |
| model:gravitee-small | eligible | People's names | 177/3369 | 5.25% | 5.28% | 3.53% |
| model:gravitee-small | eligible | Addresses & locations | 65/2396 | 2.71% | 2.80% | 1.63% |
| model:gravitee-small | eligible | Organizations | 54/2201 | 2.45% | 3.59% | 1.77% |
| model:kalyan-ettin | eligible | People's names | 1858/3369 | 55.15% | 55.86% | 26.48% |
| model:kalyan-ettin | eligible | Addresses & locations | 1120/2396 | 46.74% | 49.58% | 15.44% |
| model:kalyan-ettin | eligible | Organizations | 272/2201 | 12.36% | 20.17% | 4.77% |
| model:mmbert32k | eligible | People's names | 2570/3369 | 76.28% | 77.29% | 31.08% |
| model:mmbert32k | eligible | Addresses & locations | 391/2396 | 16.32% | 17.53% | 3.26% |
| model:mmbert32k | eligible | Organizations | 400/2201 | 18.17% | 28.31% | 5.59% |
| model:mmbert32k+nochunk | eligible | People's names | 1531/3369 | 45.44% | 46.54% | 10.75% |
| model:mmbert32k+nochunk | eligible | Addresses & locations | 203/2396 | 8.47% | 9.43% | 1.21% |
| model:mmbert32k+nochunk | eligible | Organizations | 218/2201 | 9.90% | 16.67% | 1.77% |
| model:natasha | eligible | People's names | 3262/3369 | 96.82% | 96.85% | 96.76% |
| model:natasha | eligible | Addresses & locations | 2332/2396 | 97.33% | 97.91% | 96.74% |
| model:natasha | eligible | Organizations | 1925/2201 | 87.46% | 91.19% | 86.92% |
| model:ner-ru-gherman | eligible | People's names | 3199/3369 | 94.95% | 95.61% | 90.71% |
| model:ner-ru-gherman | eligible | Addresses & locations | 2019/2396 | 84.27% | 87.10% | 75.29% |
| model:ner-ru-gherman | eligible | Organizations | 74/2201 | 3.36% | 9.40% | 2.73% |
| model:ner-ru-yqelz | eligible | People's names | 2755/3369 | 81.78% | 81.83% | 79.25% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 2034/2396 | 84.89% | 85.43% | 82.60% |
| model:ner-ru-yqelz | eligible | Organizations | 1486/2201 | 67.51% | 71.06% | 62.70% |
| model:nuner-zero | eligible | People's names | 224/3369 | 6.65% | 6.74% | 6.53% |
| model:nuner-zero | eligible | Addresses & locations | 2139/2396 | 89.27% | 90.11% | 83.56% |
| model:nuner-zero | eligible | Organizations | 1904/2201 | 86.51% | 89.96% | 61.24% |
| model:nym-base | eligible | People's names | 3180/3369 | 94.39% | 94.45% | 93.53% |
| model:nym-base | eligible | Addresses & locations | 2067/2396 | 86.27% | 87.35% | 85.52% |
| model:nym-base | eligible | Organizations | 1702/2201 | 77.33% | 81.24% | 75.97% |
| model:nym-base+ov100 | eligible | People's names | 3204/3369 | 95.10% | 95.16% | 94.39% |
| model:nym-base+ov100 | eligible | Addresses & locations | 2070/2396 | 86.39% | 87.77% | 85.48% |
| model:nym-base+ov100 | eligible | Organizations | 1738/2201 | 78.96% | 82.60% | 77.56% |
| model:nym-base+sent300 | eligible | People's names | 3152/3369 | 93.56% | 93.68% | 92.58% |
| model:nym-base+sent300 | eligible | Addresses & locations | 1996/2396 | 83.31% | 84.47% | 82.43% |
| model:nym-base+sent300 | eligible | Organizations | 1623/2201 | 73.74% | 78.06% | 71.83% |
| model:nym-small | eligible | People's names | 3158/3369 | 93.74% | 93.83% | 92.79% |
| model:nym-small | eligible | Addresses & locations | 2004/2396 | 83.64% | 85.06% | 83.01% |
| model:nym-small | eligible | Organizations | 1585/2201 | 72.01% | 76.19% | 69.65% |
| model:openai-base | eligible | People's names | 1033/3369 | 30.66% | 30.72% | 28.67% |
| model:openai-base | eligible | Addresses & locations | 38/2396 | 1.59% | 1.67% | 1.04% |
| model:openai-base | eligible | Organizations | 46/2201 | 2.09% | 2.41% | 1.95% |
| model:openmed-multilingual | eligible | People's names | 1645/3369 | 48.83% | 49.66% | 34.08% |
| model:openmed-multilingual | eligible | Addresses & locations | 672/2396 | 28.05% | 30.05% | 20.08% |
| model:openmed-multilingual | eligible | Organizations | 214/2201 | 9.72% | 15.45% | 6.18% |
| model:openmed-nemotron | eligible | People's names | 1855/3369 | 55.06% | 55.89% | 35.86% |
| model:openmed-nemotron | eligible | Addresses & locations | 975/2396 | 40.69% | 43.41% | 30.05% |
| model:openmed-nemotron | eligible | Organizations | 369/2201 | 16.77% | 25.72% | 9.59% |
| model:opf-kz-ru | eligible | People's names | 1089/3369 | 32.32% | 32.56% | 25.68% |
| model:opf-kz-ru | eligible | Addresses & locations | 58/2396 | 2.42% | 2.63% | 1.42% |
| model:opf-kz-ru | eligible | Organizations | 50/2201 | 2.27% | 2.86% | 1.14% |
| model:opf-ru | eligible | People's names | 2355/3369 | 69.90% | 70.41% | 59.60% |
| model:opf-ru | eligible | Addresses & locations | 357/2396 | 14.90% | 16.74% | 10.56% |
| model:opf-ru | eligible | Organizations | 184/2201 | 8.36% | 12.40% | 5.77% |
| model:opf-ru-v2 | eligible | People's names | 1666/3369 | 49.45% | 49.57% | 44.11% |
| model:opf-ru-v2 | eligible | Addresses & locations | 93/2396 | 3.88% | 4.42% | 2.80% |
| model:opf-ru-v2 | eligible | Organizations | 100/2201 | 4.54% | 5.91% | 3.00% |
| model:opf-ru-v2+ov100 | eligible | People's names | 1717/3369 | 50.96% | 51.08% | 46.01% |
| model:opf-ru-v2+ov100 | eligible | Addresses & locations | 113/2396 | 4.72% | 5.05% | 3.51% |
| model:opf-ru-v2+ov100 | eligible | Organizations | 104/2201 | 4.73% | 6.00% | 3.54% |
| model:opf-ru-v2+sent300 | eligible | People's names | 1841/3369 | 54.65% | 54.85% | 49.75% |
| model:opf-ru-v2+sent300 | eligible | Addresses & locations | 129/2396 | 5.38% | 6.05% | 4.26% |
| model:opf-ru-v2+sent300 | eligible | Organizations | 129/2201 | 5.86% | 7.41% | 4.73% |
| model:pii-shield-onnx | eligible | People's names | 1976/3369 | 58.65% | 59.07% | 48.41% |
| model:pii-shield-onnx | eligible | Addresses & locations | 1060/2396 | 44.24% | 45.74% | 39.32% |
| model:pii-shield-onnx | eligible | Organizations | 141/2201 | 6.41% | 11.86% | 4.23% |
| model:pplx | eligible | People's names | 989/3369 | 29.36% | 29.36% | 28.94% |
| model:pplx | eligible | Addresses & locations | 10/2396 | 0.42% | 0.42% | 0.42% |
| model:pplx | eligible | Organizations | 3/2201 | 0.14% | 0.14% | 0.14% |
| model:pplx+ov100 | eligible | People's names | 1315/3369 | 39.03% | 39.03% | 38.47% |
| model:pplx+ov100 | eligible | Addresses & locations | 27/2396 | 1.13% | 1.13% | 1.04% |
| model:pplx+ov100 | eligible | Organizations | 6/2201 | 0.27% | 0.41% | 0.23% |
| model:pplx+sent300 | eligible | People's names | 2049/3369 | 60.82% | 60.82% | 58.65% |
| model:pplx+sent300 | eligible | Addresses & locations | 90/2396 | 3.76% | 3.84% | 3.51% |
| model:pplx+sent300 | eligible | Organizations | 44/2201 | 2.00% | 2.23% | 1.95% |
| model:ru-legal-ner | eligible | People's names | 3021/3369 | 89.67% | 89.76% | 86.32% |
| model:ru-legal-ner | eligible | Addresses & locations | 451/2396 | 18.82% | 20.53% | 16.07% |
| model:ru-legal-ner | eligible | Organizations | 783/2201 | 35.57% | 43.57% | 31.12% |
| model:ru-legal-ner+ov100 | eligible | People's names | 3009/3369 | 89.31% | 89.43% | 85.90% |
| model:ru-legal-ner+ov100 | eligible | Addresses & locations | 466/2396 | 19.45% | 21.37% | 15.78% |
| model:ru-legal-ner+ov100 | eligible | Organizations | 757/2201 | 34.39% | 42.48% | 29.94% |
| model:ru-legal-ner+sent300 | eligible | People's names | 3117/3369 | 92.52% | 92.55% | 90.62% |
| model:ru-legal-ner+sent300 | eligible | Addresses & locations | 547/2396 | 22.83% | 24.87% | 20.45% |
| model:ru-legal-ner+sent300 | eligible | Organizations | 891/2201 | 40.48% | 49.70% | 36.48% |
| model:ru-pii-ner | eligible | People's names | 2325/3369 | 69.01% | 69.04% | 68.95% |
| model:ru-pii-ner | eligible | Addresses & locations | 30/2396 | 1.25% | 1.38% | 1.25% |
| model:ru-pii-ner | eligible | Organizations | 18/2201 | 0.82% | 0.82% | 0.82% |
| model:rules-ru | eligible | People's names | 0/3369 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Addresses & locations | 2/2396 | 0.08% | 0.08% | 0.08% |
| model:rules-ru | eligible | Organizations | 42/2201 | 1.91% | 1.91% | 1.91% |
| model:spacy-alrosait | eligible | People's names | 2468/3369 | 73.26% | 73.49% | 73.26% |
| model:spacy-alrosait | eligible | Addresses & locations | 1481/2396 | 61.81% | 63.48% | 61.77% |
| model:spacy-alrosait | eligible | Organizations | 110/2201 | 5.00% | 8.54% | 5.00% |
| model:spacy-ru-lg | eligible | People's names | 3265/3369 | 96.91% | 97.03% | 96.88% |
| model:spacy-ru-lg | eligible | Addresses & locations | 2315/2396 | 96.62% | 97.45% | 96.08% |
| model:spacy-ru-lg | eligible | Organizations | 1904/2201 | 86.51% | 90.64% | 86.01% |
| model:stanza-ru | eligible | People's names | 3337/3369 | 99.05% | 99.11% | 98.96% |
| model:stanza-ru | eligible | Addresses & locations | 2357/2396 | 98.37% | 98.96% | 97.87% |
| model:stanza-ru | eligible | Organizations | 1918/2201 | 87.14% | 90.64% | 86.87% |
| model:traciora | eligible | People's names | 1925/3369 | 57.14% | 57.29% | 49.36% |
| model:traciora | eligible | Addresses & locations | 310/2396 | 12.94% | 13.81% | 9.60% |
| model:traciora | eligible | Organizations | 236/2201 | 10.72% | 13.27% | 7.63% |
