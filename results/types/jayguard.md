# jayguard: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/jayguard.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | People's names | 584/806 | 72.46% | 87.34% | 72.33% |
| composition:fastino | eligible | Addresses & locations | 343/389 | 88.17% | 93.83% | 87.92% |
| composition:pplx | eligible | People's names | 559/806 | 69.35% | 83.25% | 67.87% |
| composition:pplx | eligible | Addresses & locations | 301/389 | 77.38% | 84.06% | 74.04% |
| composition:pplx+fastino | eligible | People's names | 603/806 | 74.81% | 89.58% | 74.81% |
| composition:pplx+fastino | eligible | Addresses & locations | 371/389 | 95.37% | 98.20% | 95.37% |
| composition:pplx+fastino+bardsai | eligible | People's names | 604/806 | 74.94% | 89.70% | 74.94% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 375/389 | 96.40% | 99.23% | 96.40% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 605/806 | 75.06% | 89.95% | 75.06% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 376/389 | 96.66% | 99.23% | 96.66% |
| composition:pplx+fastino+mmbert | eligible | People's names | 604/806 | 74.94% | 89.83% | 74.94% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 374/389 | 96.14% | 99.23% | 95.63% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 492/806 | 61.04% | 75.56% | 58.68% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 277/389 | 71.21% | 82.78% | 68.64% |
| model:apararti | eligible | People's names | 350/806 | 43.42% | 57.44% | 38.71% |
| model:apararti | eligible | Addresses & locations | 230/389 | 59.13% | 70.44% | 57.33% |
| model:bardsai-eu | eligible | People's names | 544/806 | 67.49% | 82.38% | 64.02% |
| model:bardsai-eu | eligible | Addresses & locations | 280/389 | 71.98% | 83.80% | 70.18% |
| model:betterleaks | eligible | People's names | 0/806 | 0.00% | 0.00% | 0.00% |
| model:betterleaks | eligible | Addresses & locations | 0/389 | 0.00% | 0.00% | 0.00% |
| model:davlan-mbert | eligible | People's names | 496/806 | 61.54% | 76.67% | 58.31% |
| model:davlan-mbert | eligible | Addresses & locations | 164/389 | 42.16% | 72.75% | 39.85% |
| model:davlan-xlmr | eligible | People's names | 548/806 | 67.99% | 82.26% | 65.14% |
| model:davlan-xlmr | eligible | Addresses & locations | 255/389 | 65.55% | 84.32% | 61.18% |
| model:fef2-secret-ru | eligible | People's names | 527/806 | 65.38% | 80.77% | 62.66% |
| model:fef2-secret-ru | eligible | Addresses & locations | 124/389 | 31.88% | 77.38% | 27.76% |
| model:gitleaks | eligible | People's names | 0/806 | 0.00% | 0.00% | 0.00% |
| model:gitleaks | eligible | Addresses & locations | 0/389 | 0.00% | 0.00% | 0.00% |
| model:gliner-multi-v21 | eligible | People's names | 568/806 | 70.47% | 84.99% | 70.47% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 307/389 | 78.92% | 90.49% | 78.15% |
| model:gliner-multi-v21-ru | eligible | People's names | 520/806 | 64.52% | 78.29% | 64.52% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 308/389 | 79.18% | 91.77% | 78.15% |
| model:gliner-nvidia | eligible | People's names | 428/806 | 53.10% | 68.61% | 50.62% |
| model:gliner-nvidia | eligible | Addresses & locations | 302/389 | 77.63% | 89.46% | 77.63% |
| model:gliner-nvidia+ov100 | eligible | People's names | 436/806 | 54.09% | 69.23% | 51.61% |
| model:gliner-nvidia+ov100 | eligible | Addresses & locations | 302/389 | 77.63% | 89.46% | 77.63% |
| model:gliner-nvidia+sent300 | eligible | People's names | 447/806 | 55.46% | 71.09% | 52.98% |
| model:gliner-nvidia+sent300 | eligible | Addresses & locations | 302/389 | 77.63% | 89.46% | 77.63% |
| model:gliner-nvidia-ru | eligible | People's names | 375/806 | 46.53% | 62.28% | 39.70% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 296/389 | 76.09% | 89.46% | 76.09% |
| model:gliner-pii-base | eligible | People's names | 457/806 | 56.70% | 70.47% | 56.58% |
| model:gliner-pii-base | eligible | Addresses & locations | 65/389 | 16.71% | 48.07% | 16.71% |
| model:gliner-pii-edge | eligible | People's names | 453/806 | 56.20% | 72.08% | 56.08% |
| model:gliner-pii-edge | eligible | Addresses & locations | 108/389 | 27.76% | 69.41% | 25.45% |
| model:gliner-stream-pii | eligible | People's names | 389/806 | 48.26% | 61.17% | 47.52% |
| model:gliner-stream-pii | eligible | Addresses & locations | 149/389 | 38.30% | 62.21% | 38.30% |
| model:gliner-urchade | eligible | People's names | 567/806 | 70.35% | 84.99% | 70.35% |
| model:gliner-urchade | eligible | Addresses & locations | 346/389 | 88.95% | 90.75% | 88.95% |
| model:gliner-urchade-ru | eligible | People's names | 56/806 | 6.95% | 7.69% | 6.95% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 345/389 | 88.69% | 89.72% | 88.69% |
| model:gliner2-fastino | eligible | People's names | 584/806 | 72.46% | 87.34% | 72.33% |
| model:gliner2-fastino | eligible | Addresses & locations | 343/389 | 88.17% | 93.83% | 87.92% |
| model:gliner2-fastino-ru | eligible | People's names | 580/806 | 71.96% | 86.48% | 71.84% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 339/389 | 87.15% | 92.29% | 86.89% |
| model:gliner2-hivetrace-omni | eligible | People's names | 551/806 | 68.36% | 82.51% | 68.36% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 330/389 | 84.83% | 93.83% | 84.83% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 535/806 | 66.38% | 80.65% | 66.38% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 316/389 | 81.23% | 93.32% | 81.23% |
| model:gliner2-hivetrace-uni | eligible | People's names | 478/806 | 59.31% | 72.70% | 59.31% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 224/389 | 57.58% | 68.89% | 57.58% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 184/806 | 22.83% | 28.91% | 22.83% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 32/389 | 8.23% | 16.20% | 8.23% |
| model:gliner2-large | eligible | People's names | 448/806 | 55.58% | 67.12% | 55.58% |
| model:gliner2-large | eligible | Addresses & locations | 252/389 | 64.78% | 86.38% | 64.52% |
| model:gliner2-vladlinv | eligible | People's names | 569/806 | 70.60% | 85.24% | 70.35% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 202/389 | 51.93% | 53.21% | 51.67% |
| model:gliner2-vladlinv-ru | eligible | People's names | 567/806 | 70.35% | 84.86% | 70.10% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 205/389 | 52.70% | 53.98% | 52.44% |
| model:gliner25-fastino | eligible | People's names | 569/806 | 70.60% | 84.86% | 70.60% |
| model:gliner25-fastino | eligible | Addresses & locations | 321/389 | 82.52% | 89.72% | 82.52% |
| model:gliner25-fastino+nochunk | eligible | People's names | 571/806 | 70.84% | 85.36% | 70.84% |
| model:gliner25-fastino+nochunk | eligible | Addresses & locations | 321/389 | 82.52% | 89.72% | 82.52% |
| model:gliner25-fastino+ov100 | eligible | People's names | 572/806 | 70.97% | 85.11% | 70.97% |
| model:gliner25-fastino+ov100 | eligible | Addresses & locations | 321/389 | 82.52% | 89.72% | 82.52% |
| model:gliner25-fastino+sent300 | eligible | People's names | 575/806 | 71.34% | 85.86% | 71.34% |
| model:gliner25-fastino+sent300 | eligible | Addresses & locations | 321/389 | 82.52% | 89.72% | 82.52% |
| model:gliner25-fastino-ru | eligible | People's names | 565/806 | 70.10% | 84.37% | 70.10% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 309/389 | 79.43% | 88.69% | 79.43% |
| model:gliner25-fastino-ru+nochunk | eligible | People's names | 563/806 | 69.85% | 84.24% | 69.73% |
| model:gliner25-fastino-ru+nochunk | eligible | Addresses & locations | 309/389 | 79.43% | 88.69% | 79.43% |
| model:gravitee-small | eligible | People's names | 87/806 | 10.79% | 13.40% | 7.69% |
| model:gravitee-small | eligible | Addresses & locations | 176/389 | 45.24% | 63.24% | 37.53% |
| model:kalyan-ettin | eligible | People's names | 281/806 | 34.86% | 55.46% | 19.35% |
| model:kalyan-ettin | eligible | Addresses & locations | 68/389 | 17.48% | 46.27% | 5.40% |
| model:mmbert32k | eligible | People's names | 495/806 | 61.41% | 78.91% | 32.01% |
| model:mmbert32k | eligible | Addresses & locations | 88/389 | 22.62% | 80.46% | 8.74% |
| model:mmbert32k+nochunk | eligible | People's names | 460/806 | 57.07% | 73.70% | 27.79% |
| model:mmbert32k+nochunk | eligible | Addresses & locations | 88/389 | 22.62% | 80.46% | 8.74% |
| model:natasha | eligible | People's names | 470/806 | 58.31% | 72.21% | 58.19% |
| model:natasha | eligible | Addresses & locations | 60/389 | 15.42% | 38.05% | 15.42% |
| model:ner-ru-gherman | eligible | People's names | 383/806 | 47.52% | 79.53% | 44.29% |
| model:ner-ru-gherman | eligible | Addresses & locations | 61/389 | 15.68% | 77.89% | 13.37% |
| model:ner-ru-yqelz | eligible | People's names | 547/806 | 67.87% | 82.38% | 65.76% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 174/389 | 44.73% | 83.03% | 40.62% |
| model:nuner-zero | eligible | People's names | 561/806 | 69.60% | 84.12% | 49.75% |
| model:nuner-zero | eligible | Addresses & locations | 288/389 | 74.04% | 85.86% | 21.34% |
| model:nym-base | eligible | People's names | 431/806 | 53.47% | 83.87% | 66.87% |
| model:nym-base | eligible | Addresses & locations | 242/389 | 62.21% | 93.32% | 66.07% |
| model:nym-base+ov100 | eligible | People's names | 432/806 | 53.60% | 83.75% | 67.12% |
| model:nym-base+ov100 | eligible | Addresses & locations | 242/389 | 62.21% | 93.32% | 66.07% |
| model:nym-base+sent300 | eligible | People's names | 431/806 | 53.47% | 83.62% | 66.50% |
| model:nym-base+sent300 | eligible | Addresses & locations | 242/389 | 62.21% | 93.32% | 66.07% |
| model:openai-base | eligible | People's names | 324/806 | 40.20% | 50.62% | 37.47% |
| model:openai-base | eligible | Addresses & locations | 226/389 | 58.10% | 64.01% | 56.56% |
| model:openmed-multilingual | eligible | People's names | 233/806 | 28.91% | 50.87% | 26.18% |
| model:openmed-multilingual | eligible | Addresses & locations | 110/389 | 28.28% | 75.06% | 21.85% |
| model:openmed-nemotron | eligible | People's names | 320/806 | 39.70% | 64.89% | 34.12% |
| model:openmed-nemotron | eligible | Addresses & locations | 144/389 | 37.02% | 64.78% | 32.13% |
| model:opf-kz-ru | eligible | People's names | 238/806 | 29.53% | 41.44% | 25.06% |
| model:opf-kz-ru | eligible | Addresses & locations | 81/389 | 20.82% | 50.39% | 18.25% |
| model:opf-ru | eligible | People's names | 462/806 | 57.32% | 74.32% | 51.99% |
| model:opf-ru | eligible | Addresses & locations | 124/389 | 31.88% | 70.95% | 23.39% |
| model:opf-ru-v2 | eligible | People's names | 342/806 | 42.43% | 54.96% | 37.72% |
| model:opf-ru-v2 | eligible | Addresses & locations | 191/389 | 49.10% | 62.21% | 47.56% |
| model:opf-ru-v2+ov100 | eligible | People's names | 350/806 | 43.42% | 56.45% | 39.08% |
| model:opf-ru-v2+ov100 | eligible | Addresses & locations | 194/389 | 49.87% | 62.72% | 48.07% |
| model:opf-ru-v2+sent300 | eligible | People's names | 351/806 | 43.55% | 56.82% | 39.83% |
| model:opf-ru-v2+sent300 | eligible | Addresses & locations | 194/389 | 49.87% | 62.72% | 48.07% |
| model:pii-shield-onnx | eligible | People's names | 416/806 | 51.61% | 66.87% | 45.29% |
| model:pii-shield-onnx | eligible | Addresses & locations | 154/389 | 39.59% | 71.21% | 36.50% |
| model:pplx | eligible | People's names | 559/806 | 69.35% | 83.25% | 67.87% |
| model:pplx | eligible | Addresses & locations | 301/389 | 77.38% | 84.06% | 74.04% |
| model:pplx+ov100 | eligible | People's names | 563/806 | 69.85% | 83.87% | 68.49% |
| model:pplx+ov100 | eligible | Addresses & locations | 301/389 | 77.38% | 84.06% | 74.04% |
| model:pplx+sent300 | eligible | People's names | 571/806 | 70.84% | 84.99% | 68.98% |
| model:pplx+sent300 | eligible | Addresses & locations | 301/389 | 77.38% | 84.06% | 74.04% |
| model:ru-legal-ner | eligible | People's names | 505/806 | 62.66% | 77.42% | 57.44% |
| model:ru-legal-ner | eligible | Addresses & locations | 200/389 | 51.41% | 78.66% | 45.50% |
| model:ru-legal-ner+ov100 | eligible | People's names | 510/806 | 63.28% | 78.16% | 58.31% |
| model:ru-legal-ner+ov100 | eligible | Addresses & locations | 200/389 | 51.41% | 78.66% | 45.50% |
| model:ru-legal-ner+sent300 | eligible | People's names | 537/806 | 66.63% | 81.02% | 63.28% |
| model:ru-legal-ner+sent300 | eligible | Addresses & locations | 200/389 | 51.41% | 78.66% | 45.50% |
| model:ru-pii-ner | eligible | People's names | 579/806 | 71.84% | 86.72% | 71.84% |
| model:ru-pii-ner | eligible | Addresses & locations | 231/389 | 59.38% | 63.24% | 57.84% |
| model:rules-ru | eligible | People's names | 1/806 | 0.12% | 0.12% | 0.12% |
| model:rules-ru | eligible | Addresses & locations | 0/389 | 0.00% | 0.00% | 0.00% |
| model:spacy-alrosait | eligible | People's names | 359/806 | 44.54% | 57.57% | 44.54% |
| model:spacy-alrosait | eligible | Addresses & locations | 217/389 | 55.78% | 64.27% | 55.78% |
| model:spacy-ru-lg | eligible | People's names | 546/806 | 67.74% | 82.75% | 67.62% |
| model:spacy-ru-lg | eligible | Addresses & locations | 82/389 | 21.08% | 71.98% | 21.08% |
| model:stanza-ru | eligible | People's names | 500/806 | 62.03% | 76.30% | 62.03% |
| model:stanza-ru | eligible | Addresses & locations | 116/389 | 29.82% | 69.15% | 29.31% |
| model:traciora | eligible | People's names | 433/806 | 53.72% | 66.87% | 47.64% |
| model:traciora | eligible | Addresses & locations | 209/389 | 53.73% | 65.55% | 51.16% |
