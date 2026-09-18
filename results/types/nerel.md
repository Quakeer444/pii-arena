# nerel: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/nerel.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | People's names | 8254/9496 | 86.92% | 87.68% | 85.84% |
| composition:fastino | eligible | Addresses & locations | 7583/8861 | 85.58% | 88.23% | 85.52% |
| composition:fastino | eligible | Organizations | 5139/6012 | 85.48% | 94.33% | 85.18% |
| composition:pplx | eligible | People's names | 2841/9496 | 29.92% | 30.31% | 29.22% |
| composition:pplx | eligible | Addresses & locations | 169/8861 | 1.91% | 2.10% | 1.85% |
| composition:pplx | eligible | Organizations | 16/6012 | 0.27% | 0.38% | 0.25% |
| composition:pplx+fastino | eligible | People's names | 8471/9496 | 89.21% | 89.74% | 88.07% |
| composition:pplx+fastino | eligible | Addresses & locations | 7591/8861 | 85.67% | 88.30% | 85.61% |
| composition:pplx+fastino | eligible | Organizations | 5139/6012 | 85.48% | 94.33% | 85.18% |
| composition:pplx+fastino+bardsai | eligible | People's names | 9407/9496 | 99.06% | 99.26% | 96.76% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 7962/8861 | 89.85% | 92.37% | 88.60% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 5407/6012 | 89.94% | 97.29% | 89.24% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 9430/9496 | 99.30% | 99.51% | 97.42% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 7989/8861 | 90.16% | 92.75% | 88.66% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 5414/6012 | 90.05% | 97.44% | 89.44% |
| composition:pplx+fastino+mmbert | eligible | People's names | 9033/9496 | 95.12% | 96.24% | 89.15% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 7689/8861 | 86.77% | 89.91% | 85.88% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 5170/6012 | 85.99% | 95.31% | 85.55% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 3432/9496 | 36.14% | 44.23% | 32.62% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 435/8861 | 4.91% | 5.68% | 4.00% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 136/6012 | 2.26% | 4.29% | 1.78% |
| model:apararti | eligible | People's names | 3406/9496 | 35.87% | 40.72% | 28.64% |
| model:apararti | eligible | Addresses & locations | 983/8861 | 11.09% | 12.71% | 8.37% |
| model:apararti | eligible | Organizations | 361/6012 | 6.00% | 9.71% | 3.93% |
| model:bardsai-eu | eligible | People's names | 9297/9496 | 97.90% | 98.46% | 93.66% |
| model:bardsai-eu | eligible | Addresses & locations | 7184/8861 | 81.07% | 84.61% | 76.12% |
| model:bardsai-eu | eligible | Organizations | 4366/6012 | 72.62% | 85.31% | 69.73% |
| model:davlan-mbert | eligible | People's names | 9233/9496 | 97.23% | 98.04% | 92.85% |
| model:davlan-mbert | eligible | Addresses & locations | 7008/8861 | 79.09% | 82.72% | 76.88% |
| model:davlan-mbert | eligible | Organizations | 4122/6012 | 68.56% | 83.00% | 66.28% |
| model:davlan-xlmr | eligible | People's names | 9251/9496 | 97.42% | 98.09% | 93.42% |
| model:davlan-xlmr | eligible | Addresses & locations | 6991/8861 | 78.90% | 82.24% | 76.05% |
| model:davlan-xlmr | eligible | Organizations | 4252/6012 | 70.73% | 83.95% | 67.98% |
| model:fef2-secret-ru | eligible | People's names | 9243/9496 | 97.34% | 97.87% | 95.63% |
| model:fef2-secret-ru | eligible | Addresses & locations | 7040/8861 | 79.45% | 82.95% | 78.98% |
| model:fef2-secret-ru | eligible | Organizations | 3967/6012 | 65.98% | 84.21% | 64.67% |
| model:gliner-multi-v21 | eligible | People's names | 7535/9496 | 79.35% | 79.96% | 78.26% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 6261/8861 | 70.66% | 72.77% | 70.61% |
| model:gliner-multi-v21 | eligible | Organizations | 3815/6012 | 63.46% | 76.36% | 63.36% |
| model:gliner-multi-v21-ru | eligible | People's names | 6839/9496 | 72.02% | 72.75% | 71.17% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 6229/8861 | 70.30% | 72.40% | 70.25% |
| model:gliner-multi-v21-ru | eligible | Organizations | 3572/6012 | 59.41% | 73.37% | 59.31% |
| model:gliner-nvidia | eligible | People's names | 5326/9496 | 56.09% | 71.52% | 54.95% |
| model:gliner-nvidia | eligible | Addresses & locations | 5924/8861 | 66.85% | 69.35% | 66.84% |
| model:gliner-nvidia | eligible | Organizations | 2596/6012 | 43.18% | 57.34% | 43.15% |
| model:gliner-nvidia+ov100 | eligible | People's names | 5269/9496 | 55.49% | 70.48% | 54.48% |
| model:gliner-nvidia+ov100 | eligible | Addresses & locations | 5745/8861 | 64.83% | 67.42% | 64.78% |
| model:gliner-nvidia+ov100 | eligible | Organizations | 2441/6012 | 40.60% | 54.39% | 40.49% |
| model:gliner-nvidia+sent300 | eligible | People's names | 6154/9496 | 64.81% | 81.72% | 63.22% |
| model:gliner-nvidia+sent300 | eligible | Addresses & locations | 6604/8861 | 74.53% | 77.32% | 74.53% |
| model:gliner-nvidia+sent300 | eligible | Organizations | 3361/6012 | 55.90% | 70.51% | 55.81% |
| model:gliner-nvidia-ru | eligible | People's names | 5273/9496 | 55.53% | 69.89% | 43.59% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 5532/8861 | 62.43% | 64.72% | 62.41% |
| model:gliner-nvidia-ru | eligible | Organizations | 1796/6012 | 29.87% | 43.70% | 29.87% |
| model:gliner-pii-base | eligible | People's names | 6839/9496 | 72.02% | 74.65% | 71.14% |
| model:gliner-pii-base | eligible | Addresses & locations | 4775/8861 | 53.89% | 56.48% | 53.89% |
| model:gliner-pii-base | eligible | Organizations | 3221/6012 | 53.58% | 66.60% | 53.56% |
| model:gliner-pii-edge | eligible | People's names | 7112/9496 | 74.89% | 80.53% | 74.14% |
| model:gliner-pii-edge | eligible | Addresses & locations | 5847/8861 | 65.99% | 71.26% | 65.94% |
| model:gliner-pii-edge | eligible | Organizations | 2871/6012 | 47.75% | 66.88% | 47.60% |
| model:gliner-stream-pii | eligible | People's names | 5400/9496 | 56.87% | 61.50% | 56.08% |
| model:gliner-stream-pii | eligible | Addresses & locations | 4393/8861 | 49.58% | 52.69% | 49.57% |
| model:gliner-stream-pii | eligible | Organizations | 2233/6012 | 37.14% | 50.02% | 37.04% |
| model:gliner-urchade | eligible | People's names | 7495/9496 | 78.93% | 79.53% | 77.95% |
| model:gliner-urchade | eligible | Addresses & locations | 6764/8861 | 76.33% | 78.19% | 76.30% |
| model:gliner-urchade | eligible | Organizations | 4108/6012 | 68.33% | 78.79% | 68.31% |
| model:gliner-urchade-ru | eligible | People's names | 343/9496 | 3.61% | 3.72% | 3.60% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 6355/8861 | 71.72% | 73.15% | 71.68% |
| model:gliner-urchade-ru | eligible | Organizations | 3882/6012 | 64.57% | 74.82% | 64.55% |
| model:gliner2-fastino | eligible | People's names | 8254/9496 | 86.92% | 87.68% | 85.84% |
| model:gliner2-fastino | eligible | Addresses & locations | 7583/8861 | 85.58% | 88.23% | 85.52% |
| model:gliner2-fastino | eligible | Organizations | 5139/6012 | 85.48% | 94.33% | 85.18% |
| model:gliner2-fastino-ru | eligible | People's names | 8188/9496 | 86.23% | 87.74% | 85.08% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 7382/8861 | 83.31% | 86.31% | 83.24% |
| model:gliner2-fastino-ru | eligible | Organizations | 5110/6012 | 85.00% | 93.91% | 84.65% |
| model:gliner2-hivetrace-omni | eligible | People's names | 6714/9496 | 70.70% | 71.89% | 70.07% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 6021/8861 | 67.95% | 70.26% | 67.92% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 3602/6012 | 59.91% | 71.07% | 59.86% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 6406/9496 | 67.46% | 68.78% | 66.87% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 5719/8861 | 64.54% | 66.73% | 64.51% |
| model:gliner2-hivetrace-omni-ru | eligible | Organizations | 3493/6012 | 58.10% | 69.03% | 58.05% |
| model:gliner2-hivetrace-uni | eligible | People's names | 5383/9496 | 56.69% | 58.24% | 56.27% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 4049/8861 | 45.69% | 47.41% | 45.69% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 1706/6012 | 28.38% | 39.94% | 28.38% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 2213/9496 | 23.30% | 23.92% | 23.27% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 956/8861 | 10.79% | 11.24% | 10.79% |
| model:gliner2-hivetrace-uni-ru | eligible | Organizations | 1151/6012 | 19.15% | 21.21% | 19.15% |
| model:gliner2-large | eligible | People's names | 6716/9496 | 70.72% | 74.53% | 70.10% |
| model:gliner2-large | eligible | Addresses & locations | 5343/8861 | 60.30% | 62.14% | 60.30% |
| model:gliner2-large | eligible | Organizations | 4158/6012 | 69.16% | 76.33% | 69.05% |
| model:gliner2-vladlinv | eligible | People's names | 8261/9496 | 86.99% | 89.48% | 85.76% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 433/8861 | 4.89% | 5.28% | 4.89% |
| model:gliner2-vladlinv | eligible | Organizations | 69/6012 | 1.15% | 2.41% | 1.15% |
| model:gliner2-vladlinv-ru | eligible | People's names | 8259/9496 | 86.97% | 89.64% | 85.89% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 458/8861 | 5.17% | 5.65% | 5.16% |
| model:gliner2-vladlinv-ru | eligible | Organizations | 58/6012 | 0.96% | 2.20% | 0.96% |
| model:gliner25-fastino | eligible | People's names | 7601/9496 | 80.04% | 81.15% | 79.14% |
| model:gliner25-fastino | eligible | Addresses & locations | 6306/8861 | 71.17% | 73.58% | 71.12% |
| model:gliner25-fastino | eligible | Organizations | 4148/6012 | 69.00% | 78.29% | 68.93% |
| model:gliner25-fastino+nochunk | eligible | People's names | 5612/9496 | 59.10% | 60.08% | 58.35% |
| model:gliner25-fastino+nochunk | eligible | Addresses & locations | 5805/8861 | 65.51% | 67.78% | 65.49% |
| model:gliner25-fastino+nochunk | eligible | Organizations | 3451/6012 | 57.40% | 67.08% | 57.39% |
| model:gliner25-fastino+ov100 | eligible | People's names | 7523/9496 | 79.22% | 80.31% | 78.23% |
| model:gliner25-fastino+ov100 | eligible | Addresses & locations | 6264/8861 | 70.69% | 73.15% | 70.51% |
| model:gliner25-fastino+ov100 | eligible | Organizations | 4075/6012 | 67.78% | 77.38% | 67.56% |
| model:gliner25-fastino+sent300 | eligible | People's names | 8391/9496 | 88.36% | 89.84% | 87.45% |
| model:gliner25-fastino+sent300 | eligible | Addresses & locations | 6608/8861 | 74.57% | 77.15% | 74.53% |
| model:gliner25-fastino+sent300 | eligible | Organizations | 4456/6012 | 74.12% | 83.55% | 74.00% |
| model:gliner25-fastino-ru | eligible | People's names | 7550/9496 | 79.51% | 80.59% | 78.60% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 6227/8861 | 70.27% | 72.68% | 70.23% |
| model:gliner25-fastino-ru | eligible | Organizations | 4085/6012 | 67.95% | 77.58% | 67.88% |
| model:gliner25-fastino-ru+nochunk | eligible | People's names | 5531/9496 | 58.25% | 59.32% | 57.50% |
| model:gliner25-fastino-ru+nochunk | eligible | Addresses & locations | 5822/8861 | 65.70% | 67.89% | 65.67% |
| model:gliner25-fastino-ru+nochunk | eligible | Organizations | 3429/6012 | 57.04% | 66.90% | 57.02% |
| model:gravitee-small | eligible | People's names | 359/9496 | 3.78% | 5.32% | 2.40% |
| model:gravitee-small | eligible | Addresses & locations | 191/8861 | 2.16% | 2.45% | 1.30% |
| model:gravitee-small | eligible | Organizations | 123/6012 | 2.05% | 3.28% | 1.73% |
| model:kalyan-ettin | eligible | People's names | 2997/9496 | 31.56% | 70.07% | 19.87% |
| model:kalyan-ettin | eligible | Addresses & locations | 3719/8861 | 41.97% | 49.17% | 13.87% |
| model:kalyan-ettin | eligible | Organizations | 488/6012 | 8.12% | 21.79% | 2.98% |
| model:mmbert32k | eligible | People's names | 5865/9496 | 61.76% | 86.04% | 16.07% |
| model:mmbert32k | eligible | Addresses & locations | 1759/8861 | 19.85% | 25.89% | 3.94% |
| model:mmbert32k | eligible | Organizations | 676/6012 | 11.24% | 23.92% | 2.96% |
| model:mmbert32k+nochunk | eligible | People's names | 2935/9496 | 30.91% | 64.01% | 5.12% |
| model:mmbert32k+nochunk | eligible | Addresses & locations | 983/8861 | 11.09% | 15.45% | 1.57% |
| model:mmbert32k+nochunk | eligible | Organizations | 406/6012 | 6.75% | 15.59% | 1.56% |
| model:natasha | eligible | People's names | 9044/9496 | 95.24% | 95.75% | 94.03% |
| model:natasha | eligible | Addresses & locations | 6996/8861 | 78.95% | 82.20% | 78.78% |
| model:natasha | eligible | Organizations | 3790/6012 | 63.04% | 81.40% | 62.04% |
| model:ner-ru-gherman | eligible | People's names | 3486/9496 | 36.71% | 97.22% | 33.98% |
| model:ner-ru-gherman | eligible | Addresses & locations | 6129/8861 | 69.17% | 77.44% | 56.43% |
| model:ner-ru-gherman | eligible | Organizations | 120/6012 | 2.00% | 25.12% | 1.13% |
| model:ner-ru-yqelz | eligible | People's names | 6147/9496 | 64.73% | 66.91% | 59.59% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 7135/8861 | 80.52% | 83.44% | 77.08% |
| model:ner-ru-yqelz | eligible | Organizations | 3603/6012 | 59.93% | 71.52% | 55.22% |
| model:nuner-zero | eligible | People's names | 7823/9496 | 82.38% | 84.33% | 26.60% |
| model:nuner-zero | eligible | Addresses & locations | 5739/8861 | 64.77% | 68.30% | 58.28% |
| model:nuner-zero | eligible | Organizations | 4377/6012 | 72.80% | 85.89% | 39.25% |
| model:nym-base | eligible | People's names | 7862/9496 | 82.79% | 97.43% | 95.53% |
| model:nym-base | eligible | Addresses & locations | 7635/8861 | 86.16% | 90.07% | 84.90% |
| model:nym-base | eligible | Organizations | 3754/6012 | 62.44% | 80.71% | 65.44% |
| model:nym-base+ov100 | eligible | People's names | 8185/9496 | 86.19% | 98.10% | 96.36% |
| model:nym-base+ov100 | eligible | Addresses & locations | 7767/8861 | 87.65% | 91.58% | 86.67% |
| model:nym-base+ov100 | eligible | Organizations | 3899/6012 | 64.85% | 82.82% | 68.26% |
| model:nym-base+sent300 | eligible | People's names | 7344/9496 | 77.34% | 95.33% | 92.82% |
| model:nym-base+sent300 | eligible | Addresses & locations | 7330/8861 | 82.72% | 86.59% | 81.18% |
| model:nym-base+sent300 | eligible | Organizations | 3474/6012 | 57.78% | 75.42% | 59.68% |
| model:openai-base | eligible | People's names | 1840/9496 | 19.38% | 20.65% | 17.68% |
| model:openai-base | eligible | Addresses & locations | 241/8861 | 2.72% | 3.08% | 2.39% |
| model:openai-base | eligible | Organizations | 84/6012 | 1.40% | 2.15% | 1.20% |
| model:openmed-multilingual | eligible | People's names | 1645/9496 | 17.32% | 48.39% | 20.65% |
| model:openmed-multilingual | eligible | Addresses & locations | 2552/8861 | 28.80% | 34.69% | 20.47% |
| model:openmed-multilingual | eligible | Organizations | 416/6012 | 6.92% | 17.43% | 3.98% |
| model:openmed-nemotron | eligible | People's names | 2129/9496 | 22.42% | 58.98% | 24.78% |
| model:openmed-nemotron | eligible | Addresses & locations | 3204/8861 | 36.16% | 42.05% | 22.76% |
| model:openmed-nemotron | eligible | Organizations | 766/6012 | 12.74% | 30.67% | 7.09% |
| model:opf-kz-ru | eligible | People's names | 1856/9496 | 19.55% | 24.08% | 14.35% |
| model:opf-kz-ru | eligible | Addresses & locations | 353/8861 | 3.98% | 4.91% | 2.87% |
| model:opf-kz-ru | eligible | Organizations | 82/6012 | 1.36% | 2.56% | 0.96% |
| model:opf-ru | eligible | People's names | 5617/9496 | 59.15% | 70.65% | 47.97% |
| model:opf-ru | eligible | Addresses & locations | 1211/8861 | 13.67% | 17.94% | 9.12% |
| model:opf-ru | eligible | Organizations | 380/6012 | 6.32% | 14.85% | 3.88% |
| model:opf-ru-v2 | eligible | People's names | 3384/9496 | 35.64% | 39.50% | 29.67% |
| model:opf-ru-v2 | eligible | Addresses & locations | 449/8861 | 5.07% | 6.13% | 3.70% |
| model:opf-ru-v2 | eligible | Organizations | 233/6012 | 3.88% | 6.65% | 2.91% |
| model:opf-ru-v2+ov100 | eligible | People's names | 3409/9496 | 35.90% | 39.60% | 29.98% |
| model:opf-ru-v2+ov100 | eligible | Addresses & locations | 446/8861 | 5.03% | 6.11% | 3.68% |
| model:opf-ru-v2+ov100 | eligible | Organizations | 242/6012 | 4.03% | 7.07% | 2.98% |
| model:opf-ru-v2+sent300 | eligible | People's names | 3959/9496 | 41.69% | 45.23% | 35.77% |
| model:opf-ru-v2+sent300 | eligible | Addresses & locations | 611/8861 | 6.90% | 8.28% | 5.47% |
| model:opf-ru-v2+sent300 | eligible | Organizations | 335/6012 | 5.57% | 9.36% | 4.19% |
| model:pplx | eligible | People's names | 2841/9496 | 29.92% | 30.31% | 29.22% |
| model:pplx | eligible | Addresses & locations | 169/8861 | 1.91% | 2.10% | 1.85% |
| model:pplx | eligible | Organizations | 16/6012 | 0.27% | 0.38% | 0.25% |
| model:pplx+ov100 | eligible | People's names | 3462/9496 | 36.46% | 37.07% | 35.68% |
| model:pplx+ov100 | eligible | Addresses & locations | 237/8861 | 2.67% | 2.89% | 2.56% |
| model:pplx+ov100 | eligible | Organizations | 23/6012 | 0.38% | 0.68% | 0.32% |
| model:pplx+sent300 | eligible | People's names | 5857/9496 | 61.68% | 63.75% | 58.61% |
| model:pplx+sent300 | eligible | Addresses & locations | 816/8861 | 9.21% | 9.87% | 8.52% |
| model:pplx+sent300 | eligible | Organizations | 84/6012 | 1.40% | 2.54% | 1.31% |
| model:ru-legal-ner | eligible | People's names | 8233/9496 | 86.70% | 89.63% | 81.28% |
| model:ru-legal-ner | eligible | Addresses & locations | 2534/8861 | 28.60% | 34.33% | 24.99% |
| model:ru-legal-ner | eligible | Organizations | 1498/6012 | 24.92% | 39.57% | 21.42% |
| model:ru-legal-ner+ov100 | eligible | People's names | 8137/9496 | 85.69% | 88.95% | 79.98% |
| model:ru-legal-ner+ov100 | eligible | Addresses & locations | 2431/8861 | 27.43% | 33.05% | 23.32% |
| model:ru-legal-ner+ov100 | eligible | Organizations | 1467/6012 | 24.40% | 38.56% | 21.04% |
| model:ru-legal-ner+sent300 | eligible | People's names | 8658/9496 | 91.18% | 92.91% | 88.16% |
| model:ru-legal-ner+sent300 | eligible | Addresses & locations | 3050/8861 | 34.42% | 40.77% | 31.22% |
| model:ru-legal-ner+sent300 | eligible | Organizations | 1783/6012 | 29.66% | 46.62% | 26.50% |
| model:ru-pii-ner | eligible | People's names | 7332/9496 | 77.21% | 78.38% | 77.00% |
| model:ru-pii-ner | eligible | Addresses & locations | 650/8861 | 7.34% | 7.58% | 7.34% |
| model:ru-pii-ner | eligible | Organizations | 20/6012 | 0.33% | 0.77% | 0.33% |
| model:rules-ru | eligible | People's names | 0/9496 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Addresses & locations | 6/8861 | 0.07% | 0.08% | 0.07% |
| model:rules-ru | eligible | Organizations | 23/6012 | 0.38% | 0.48% | 0.38% |
| model:spacy-alrosait | eligible | People's names | 6021/9496 | 63.41% | 67.23% | 62.79% |
| model:spacy-alrosait | eligible | Addresses & locations | 4642/8861 | 52.39% | 56.71% | 52.38% |
| model:spacy-alrosait | eligible | Organizations | 277/6012 | 4.61% | 18.75% | 4.61% |
| model:spacy-ru-lg | eligible | People's names | 9114/9496 | 95.98% | 96.82% | 94.90% |
| model:spacy-ru-lg | eligible | Addresses & locations | 7052/8861 | 79.58% | 82.97% | 79.42% |
| model:spacy-ru-lg | eligible | Organizations | 3841/6012 | 63.89% | 82.58% | 62.82% |
| model:stanza-ru | eligible | People's names | 9287/9496 | 97.80% | 98.42% | 96.77% |
| model:stanza-ru | eligible | Addresses & locations | 7302/8861 | 82.41% | 85.37% | 82.00% |
| model:stanza-ru | eligible | Organizations | 4210/6012 | 70.03% | 81.77% | 69.89% |
| model:traciora | eligible | People's names | 4190/9496 | 44.12% | 49.79% | 36.91% |
| model:traciora | eligible | Addresses & locations | 1255/8861 | 14.16% | 16.31% | 10.52% |
| model:traciora | eligible | Organizations | 585/6012 | 9.73% | 15.97% | 7.42% |
