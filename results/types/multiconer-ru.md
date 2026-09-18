# multiconer-ru: category results

Exact counts from the frozen predictions at threshold 0.5. `train` marks a known training-source overlap and is excluded from pooled charts. All configurations are listed for inspection, not ranked across different supported scopes. `model:` is a single detector configuration; `composition:` is a fixed union or vote.

[Dataset outcomes](../by-dataset.md) · [Historical metrics and uncertainty](../datasets/multiconer-ru.md) · [Metric contract](../../docs/metrics.md)

| Configuration | Status | Category | Hidden / gold | Hidden % | Detected % | Raw hiding % |
|---|---|---|---:|---:|---:|---:|
| composition:fastino | eligible | People's names | 211/305 | 69.18% | 98.03% | 68.20% |
| composition:fastino | eligible | Addresses & locations | 284/379 | 74.93% | 90.24% | 74.41% |
| composition:fastino | eligible | Organizations | 396/524 | 75.57% | 90.08% | 74.81% |
| composition:pplx | eligible | People's names | 88/305 | 28.85% | 47.54% | 20.33% |
| composition:pplx | eligible | Addresses & locations | 32/379 | 8.44% | 11.08% | 5.80% |
| composition:pplx | eligible | Organizations | 21/524 | 4.01% | 8.78% | 2.67% |
| composition:pplx+fastino | eligible | People's names | 240/305 | 78.69% | 98.36% | 77.70% |
| composition:pplx+fastino | eligible | Addresses & locations | 287/379 | 75.73% | 90.77% | 75.20% |
| composition:pplx+fastino | eligible | Organizations | 399/524 | 76.15% | 91.03% | 75.00% |
| composition:pplx+fastino+bardsai | eligible | People's names | 242/305 | 79.34% | 98.36% | 77.70% |
| composition:pplx+fastino+bardsai | eligible | Addresses & locations | 291/379 | 76.78% | 91.29% | 76.25% |
| composition:pplx+fastino+bardsai | eligible | Organizations | 401/524 | 76.53% | 91.60% | 75.38% |
| composition:pplx+fastino+bardsai+mmbert | eligible | People's names | 244/305 | 80.00% | 99.02% | 79.34% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Addresses & locations | 294/379 | 77.57% | 92.61% | 76.52% |
| composition:pplx+fastino+bardsai+mmbert | eligible | Organizations | 404/524 | 77.10% | 92.94% | 75.57% |
| composition:pplx+fastino+mmbert | eligible | People's names | 244/305 | 80.00% | 99.02% | 79.34% |
| composition:pplx+fastino+mmbert | eligible | Addresses & locations | 291/379 | 76.78% | 92.61% | 75.46% |
| composition:pplx+fastino+mmbert | eligible | Organizations | 402/524 | 76.72% | 92.56% | 75.19% |
| composition:vote2(pplx,opf2,nvidia) | eligible | People's names | 41/305 | 13.44% | 37.38% | 10.16% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Addresses & locations | 28/379 | 7.39% | 9.50% | 4.49% |
| composition:vote2(pplx,opf2,nvidia) | eligible | Organizations | 14/524 | 2.67% | 6.68% | 2.29% |
| model:apararti | eligible | People's names | 14/305 | 4.59% | 12.79% | 2.95% |
| model:apararti | eligible | Addresses & locations | 28/379 | 7.39% | 10.55% | 6.07% |
| model:apararti | eligible | Organizations | 15/524 | 2.86% | 5.34% | 2.48% |
| model:bardsai-eu | eligible | People's names | 44/305 | 14.43% | 29.18% | 11.15% |
| model:bardsai-eu | eligible | Addresses & locations | 112/379 | 29.55% | 35.88% | 23.75% |
| model:bardsai-eu | eligible | Organizations | 110/524 | 20.99% | 26.34% | 19.66% |
| model:davlan-mbert | eligible | People's names | 69/305 | 22.62% | 46.23% | 18.36% |
| model:davlan-mbert | eligible | Addresses & locations | 110/379 | 29.02% | 38.52% | 25.33% |
| model:davlan-mbert | eligible | Organizations | 113/524 | 21.56% | 30.53% | 20.23% |
| model:davlan-xlmr | eligible | People's names | 90/305 | 29.51% | 50.49% | 27.54% |
| model:davlan-xlmr | eligible | Addresses & locations | 112/379 | 29.55% | 41.16% | 24.01% |
| model:davlan-xlmr | eligible | Organizations | 151/524 | 28.82% | 37.79% | 26.15% |
| model:fef2-secret-ru | eligible | People's names | 100/305 | 32.79% | 57.38% | 25.90% |
| model:fef2-secret-ru | eligible | Addresses & locations | 102/379 | 26.91% | 35.36% | 20.58% |
| model:fef2-secret-ru | eligible | Organizations | 93/524 | 17.75% | 24.62% | 15.65% |
| model:gliner-multi-v21 | eligible | People's names | 168/305 | 55.08% | 87.87% | 54.75% |
| model:gliner-multi-v21 | eligible | Addresses & locations | 215/379 | 56.73% | 70.45% | 56.20% |
| model:gliner-multi-v21 | eligible | Organizations | 207/524 | 39.50% | 50.19% | 39.31% |
| model:gliner-multi-v21-ru | eligible | People's names | 153/305 | 50.16% | 82.95% | 49.84% |
| model:gliner-multi-v21-ru | eligible | Addresses & locations | 202/379 | 53.30% | 67.28% | 53.03% |
| model:gliner-multi-v21-ru | eligible | Organizations | 161/524 | 30.73% | 39.31% | 30.73% |
| model:gliner-nvidia | eligible | People's names | 109/305 | 35.74% | 68.52% | 34.10% |
| model:gliner-nvidia | eligible | Addresses & locations | 198/379 | 52.24% | 60.16% | 52.24% |
| model:gliner-nvidia | eligible | Organizations | 225/524 | 42.94% | 52.48% | 42.56% |
| model:gliner-nvidia-ru | eligible | People's names | 72/305 | 23.61% | 57.38% | 21.64% |
| model:gliner-nvidia-ru | eligible | Addresses & locations | 160/379 | 42.22% | 50.40% | 42.22% |
| model:gliner-nvidia-ru | eligible | Organizations | 186/524 | 35.50% | 42.37% | 35.31% |
| model:gliner-pii-base | eligible | People's names | 43/305 | 14.10% | 40.33% | 13.44% |
| model:gliner-pii-base | eligible | Addresses & locations | 128/379 | 33.77% | 44.33% | 33.77% |
| model:gliner-pii-base | eligible | Organizations | 146/524 | 27.86% | 37.21% | 27.67% |
| model:gliner-pii-edge | eligible | People's names | 99/305 | 32.46% | 81.97% | 30.82% |
| model:gliner-pii-edge | eligible | Addresses & locations | 217/379 | 57.26% | 73.88% | 56.46% |
| model:gliner-pii-edge | eligible | Organizations | 208/524 | 39.69% | 64.31% | 39.50% |
| model:gliner-stream-pii | eligible | People's names | 60/305 | 19.67% | 63.93% | 17.05% |
| model:gliner-stream-pii | eligible | Addresses & locations | 130/379 | 34.30% | 47.23% | 34.04% |
| model:gliner-stream-pii | eligible | Organizations | 202/524 | 38.55% | 62.21% | 38.36% |
| model:gliner-urchade | eligible | People's names | 230/305 | 75.41% | 87.54% | 75.41% |
| model:gliner-urchade | eligible | Addresses & locations | 240/379 | 63.32% | 67.81% | 63.32% |
| model:gliner-urchade | eligible | Organizations | 331/524 | 63.17% | 69.08% | 63.17% |
| model:gliner-urchade-ru | eligible | People's names | 100/305 | 32.79% | 41.97% | 32.79% |
| model:gliner-urchade-ru | eligible | Addresses & locations | 242/379 | 63.85% | 68.34% | 63.85% |
| model:gliner-urchade-ru | eligible | Organizations | 247/524 | 47.14% | 52.48% | 47.14% |
| model:gliner2-fastino | eligible | People's names | 211/305 | 69.18% | 98.03% | 68.20% |
| model:gliner2-fastino | eligible | Addresses & locations | 284/379 | 74.93% | 90.24% | 74.41% |
| model:gliner2-fastino | eligible | Organizations | 396/524 | 75.57% | 90.08% | 74.81% |
| model:gliner2-fastino-ru | eligible | People's names | 204/305 | 66.89% | 98.36% | 65.90% |
| model:gliner2-fastino-ru | eligible | Addresses & locations | 287/379 | 75.73% | 91.56% | 75.20% |
| model:gliner2-fastino-ru | eligible | Organizations | 389/524 | 74.24% | 88.55% | 73.66% |
| model:gliner2-hivetrace-omni | eligible | People's names | 213/305 | 69.84% | 92.79% | 69.84% |
| model:gliner2-hivetrace-omni | eligible | Addresses & locations | 269/379 | 70.98% | 85.49% | 70.98% |
| model:gliner2-hivetrace-omni | eligible | Organizations | 411/524 | 78.44% | 91.79% | 78.24% |
| model:gliner2-hivetrace-omni-ru | eligible | People's names | 198/305 | 64.92% | 90.49% | 64.92% |
| model:gliner2-hivetrace-omni-ru | eligible | Addresses & locations | 273/379 | 72.03% | 85.75% | 72.03% |
| model:gliner2-hivetrace-omni-ru | eligible | Organizations | 407/524 | 77.67% | 89.89% | 77.48% |
| model:gliner2-hivetrace-uni | eligible | People's names | 161/305 | 52.79% | 78.69% | 52.79% |
| model:gliner2-hivetrace-uni | eligible | Addresses & locations | 99/379 | 26.12% | 32.19% | 26.12% |
| model:gliner2-hivetrace-uni | eligible | Organizations | 260/524 | 49.62% | 59.92% | 49.62% |
| model:gliner2-hivetrace-uni-ru | eligible | People's names | 100/305 | 32.79% | 59.34% | 32.79% |
| model:gliner2-hivetrace-uni-ru | eligible | Addresses & locations | 130/379 | 34.30% | 43.01% | 34.30% |
| model:gliner2-hivetrace-uni-ru | eligible | Organizations | 248/524 | 47.33% | 56.68% | 47.14% |
| model:gliner2-large | eligible | People's names | 132/305 | 43.28% | 77.38% | 42.95% |
| model:gliner2-large | eligible | Addresses & locations | 218/379 | 57.52% | 72.03% | 57.52% |
| model:gliner2-large | eligible | Organizations | 314/524 | 59.92% | 74.05% | 59.54% |
| model:gliner2-vladlinv | eligible | People's names | 204/305 | 66.89% | 85.57% | 65.90% |
| model:gliner2-vladlinv | eligible | Addresses & locations | 141/379 | 37.20% | 42.74% | 37.20% |
| model:gliner2-vladlinv | eligible | Organizations | 42/524 | 8.02% | 10.11% | 7.82% |
| model:gliner2-vladlinv-ru | eligible | People's names | 207/305 | 67.87% | 84.92% | 67.21% |
| model:gliner2-vladlinv-ru | eligible | Addresses & locations | 143/379 | 37.73% | 43.54% | 37.73% |
| model:gliner2-vladlinv-ru | eligible | Organizations | 39/524 | 7.44% | 9.35% | 7.25% |
| model:gliner25-fastino | eligible | People's names | 191/305 | 62.62% | 94.75% | 61.64% |
| model:gliner25-fastino | eligible | Addresses & locations | 247/379 | 65.17% | 81.53% | 64.64% |
| model:gliner25-fastino | eligible | Organizations | 298/524 | 56.87% | 70.99% | 56.68% |
| model:gliner25-fastino-ru | eligible | People's names | 192/305 | 62.95% | 96.72% | 61.97% |
| model:gliner25-fastino-ru | eligible | Addresses & locations | 255/379 | 67.28% | 83.11% | 67.02% |
| model:gliner25-fastino-ru | eligible | Organizations | 268/524 | 51.15% | 64.69% | 51.15% |
| model:gravitee-small | eligible | People's names | 115/305 | 37.70% | 59.34% | 29.18% |
| model:gravitee-small | eligible | Addresses & locations | 131/379 | 34.56% | 45.38% | 29.02% |
| model:gravitee-small | eligible | Organizations | 144/524 | 27.48% | 39.89% | 24.43% |
| model:kalyan-ettin | eligible | People's names | 7/305 | 2.30% | 35.74% | 0.33% |
| model:kalyan-ettin | eligible | Addresses & locations | 63/379 | 16.62% | 25.86% | 3.69% |
| model:kalyan-ettin | eligible | Organizations | 46/524 | 8.78% | 21.95% | 3.63% |
| model:mmbert32k | eligible | People's names | 123/305 | 40.33% | 79.34% | 19.34% |
| model:mmbert32k | eligible | Addresses & locations | 140/379 | 36.94% | 55.15% | 19.79% |
| model:mmbert32k | eligible | Organizations | 75/524 | 14.31% | 37.40% | 7.63% |
| model:natasha | eligible | People's names | 2/305 | 0.66% | 0.66% | 0.66% |
| model:natasha | eligible | Addresses & locations | 1/379 | 0.26% | 0.26% | 0.26% |
| model:natasha | eligible | Organizations | 6/524 | 1.15% | 1.34% | 1.15% |
| model:ner-ru-gherman | eligible | People's names | 13/305 | 4.26% | 54.10% | 3.28% |
| model:ner-ru-gherman | eligible | Addresses & locations | 107/379 | 28.23% | 41.42% | 23.48% |
| model:ner-ru-gherman | eligible | Organizations | 3/524 | 0.57% | 9.54% | 0.38% |
| model:ner-ru-yqelz | eligible | People's names | 286/305 | 93.77% | 99.02% | 90.49% |
| model:ner-ru-yqelz | eligible | Addresses & locations | 354/379 | 93.40% | 95.25% | 90.50% |
| model:ner-ru-yqelz | eligible | Organizations | 490/524 | 93.51% | 95.99% | 91.41% |
| model:nuner-zero | eligible | People's names | 151/305 | 49.51% | 79.34% | 7.21% |
| model:nuner-zero | eligible | Addresses & locations | 226/379 | 59.63% | 75.20% | 54.88% |
| model:nuner-zero | eligible | Organizations | 150/524 | 28.63% | 40.84% | 13.93% |
| model:nym-base | eligible | People's names | 94/305 | 30.82% | 54.75% | 32.46% |
| model:nym-base | eligible | Addresses & locations | 136/379 | 35.88% | 46.17% | 31.66% |
| model:nym-base | eligible | Organizations | 162/524 | 30.92% | 42.37% | 29.77% |
| model:nym-small | eligible | People's names | 44/305 | 14.43% | 27.87% | 14.43% |
| model:nym-small | eligible | Addresses & locations | 83/379 | 21.90% | 27.97% | 19.26% |
| model:nym-small | eligible | Organizations | 115/524 | 21.95% | 32.44% | 19.66% |
| model:openai-base | eligible | People's names | 18/305 | 5.90% | 14.75% | 4.92% |
| model:openai-base | eligible | Addresses & locations | 20/379 | 5.28% | 6.33% | 5.01% |
| model:openai-base | eligible | Organizations | 13/524 | 2.48% | 3.24% | 2.10% |
| model:openmed-multilingual | eligible | People's names | 7/305 | 2.30% | 21.64% | 1.31% |
| model:openmed-multilingual | eligible | Addresses & locations | 48/379 | 12.66% | 22.69% | 7.12% |
| model:openmed-multilingual | eligible | Organizations | 33/524 | 6.30% | 21.95% | 3.24% |
| model:openmed-nemotron | eligible | People's names | 14/305 | 4.59% | 32.13% | 1.97% |
| model:openmed-nemotron | eligible | Addresses & locations | 61/379 | 16.09% | 22.69% | 6.33% |
| model:openmed-nemotron | eligible | Organizations | 55/524 | 10.50% | 23.47% | 4.20% |
| model:opf-kz-ru | eligible | People's names | 2/305 | 0.66% | 6.89% | 0.00% |
| model:opf-kz-ru | eligible | Addresses & locations | 14/379 | 3.69% | 3.69% | 2.90% |
| model:opf-kz-ru | eligible | Organizations | 10/524 | 1.91% | 2.67% | 1.53% |
| model:opf-ru | eligible | People's names | 11/305 | 3.61% | 36.07% | 2.30% |
| model:opf-ru | eligible | Addresses & locations | 29/379 | 7.65% | 18.47% | 3.96% |
| model:opf-ru | eligible | Organizations | 34/524 | 6.49% | 12.60% | 4.96% |
| model:opf-ru-v2 | eligible | People's names | 16/305 | 5.25% | 16.39% | 3.28% |
| model:opf-ru-v2 | eligible | Addresses & locations | 13/379 | 3.43% | 4.75% | 1.32% |
| model:opf-ru-v2 | eligible | Organizations | 8/524 | 1.53% | 2.67% | 1.15% |
| model:pii-shield-onnx | eligible | People's names | 38/305 | 12.46% | 31.48% | 9.51% |
| model:pii-shield-onnx | eligible | Addresses & locations | 63/379 | 16.62% | 24.27% | 11.35% |
| model:pii-shield-onnx | eligible | Organizations | 34/524 | 6.49% | 16.79% | 4.77% |
| model:pplx | eligible | People's names | 88/305 | 28.85% | 47.54% | 20.33% |
| model:pplx | eligible | Addresses & locations | 32/379 | 8.44% | 11.08% | 5.80% |
| model:pplx | eligible | Organizations | 21/524 | 4.01% | 8.78% | 2.67% |
| model:ru-legal-ner | eligible | People's names | 110/305 | 36.07% | 73.77% | 25.25% |
| model:ru-legal-ner | eligible | Addresses & locations | 86/379 | 22.69% | 37.73% | 10.82% |
| model:ru-legal-ner | eligible | Organizations | 135/524 | 25.76% | 42.56% | 18.70% |
| model:ru-pii-ner | eligible | People's names | 155/305 | 50.82% | 72.46% | 49.84% |
| model:ru-pii-ner | eligible | Addresses & locations | 119/379 | 31.40% | 39.84% | 30.61% |
| model:ru-pii-ner | eligible | Organizations | 34/524 | 6.49% | 8.97% | 6.49% |
| model:rules-ru | eligible | People's names | 0/305 | 0.00% | 0.33% | 0.00% |
| model:rules-ru | eligible | Addresses & locations | 0/379 | 0.00% | 0.00% | 0.00% |
| model:rules-ru | eligible | Organizations | 3/524 | 0.57% | 0.95% | 0.57% |
| model:spacy-alrosait | eligible | People's names | 0/305 | 0.00% | 0.98% | 0.00% |
| model:spacy-alrosait | eligible | Addresses & locations | 2/379 | 0.53% | 0.53% | 0.53% |
| model:spacy-alrosait | eligible | Organizations | 0/524 | 0.00% | 0.57% | 0.00% |
| model:spacy-ru-lg | eligible | People's names | 167/305 | 54.75% | 86.89% | 54.75% |
| model:spacy-ru-lg | eligible | Addresses & locations | 170/379 | 44.85% | 58.05% | 44.59% |
| model:spacy-ru-lg | eligible | Organizations | 269/524 | 51.34% | 63.93% | 51.15% |
| model:stanza-ru | eligible | People's names | 11/305 | 3.61% | 6.89% | 3.61% |
| model:stanza-ru | eligible | Addresses & locations | 10/379 | 2.64% | 3.69% | 2.64% |
| model:stanza-ru | eligible | Organizations | 65/524 | 12.40% | 16.41% | 12.40% |
| model:traciora | eligible | People's names | 68/305 | 22.30% | 47.87% | 15.08% |
| model:traciora | eligible | Addresses & locations | 59/379 | 15.57% | 23.48% | 9.76% |
| model:traciora | eligible | Organizations | 39/524 | 7.44% | 14.50% | 5.15% |
