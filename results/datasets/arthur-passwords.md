# arthur-passwords - en / secrets (516 rows, 280 spans, 236 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.035 (96.5% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gliner-pii-base | **0** | 0.0% [0.0%, 0.0%] | 100.0% | 0.730 [0.683, 0.774] | 0.574 | 1.000 | 0.790 | 0.790 | 0.730 | 110/236 | 2063 | 0 | 3 | 166M |  |
| pplx | **0** | 0.0% [0.0%, 0.0%] | 100.0% | 0.295 [0.273, 0.318] | 0.173 | 1.000 | 0.337 | 0.352 | 0.262 | 227/236 | 7898 | 0 | 50 | 596M |  |
| openmed-multilingual | **0** | 0.0% [0.0%, 0.0%] | 100.0% | 0.235 [0.216, 0.256] | 0.133 | 1.000 | 0.281 | 0.285 | 0.234 | 236/236 | 11042 | 0 | 28 | 1.4B |  |
| gliner-pii-edge | **1** | 0.4% [0.0%, 1.1%] | 99.6% | 0.606 [0.562, 0.650] | 0.435 | 0.996 | 0.716 | 0.718 | 0.606 | 99/236 | 2293 | 0 | 15 | 45M |  |
| gliner25-fastino | **3** | 1.1% [0.0%, 2.4%] | 98.9% | 0.579 [0.534, 0.625] | 0.409 | 0.989 | 0.662 | 0.664 | 0.579 | 126/236 | 3232 | 0 | 2 | 287M |  |
| opf-ru | **3** | 1.1% [0.0%, 2.5%] | 98.9% | 0.370 [0.343, 0.396] | 0.228 | 0.989 | 0.330 | 0.341 | 0.332 | 214/236 | 5878 | 0 | 39 | 1.4B |  |
| gliner2-hivetrace-omni | **4** | 1.4% [0.3%, 3.0%] | 98.6% | 0.622 [0.580, 0.662] | 0.455 | 0.986 | 0.672 | 0.675 | 0.622 | 171/236 | 3026 | 0 | 2 | 307M |  |
| apararti | **4** | 1.4% [0.3%, 2.9%] | 98.6% | 0.324 [0.300, 0.347] | 0.194 | 0.986 | 0.353 | 0.373 | 0.263 | 213/236 | 6803 | 0 | 63 | 1.4B |  |
| gliner-nvidia | **6** | 2.1% [0.7%, 4.0%] | 97.9% | 0.745 [0.701, 0.787] | 0.601 | 0.979 | 0.764 | 0.766 | 0.745 | 121/236 | 1835 | 0 | 7 | 445M |  |
| pii-shield-onnx | **6** | 2.1% [0.7%, 4.0%] | 97.9% | 0.350 [0.324, 0.377] | 0.213 | 0.979 | 0.405 | 0.408 | 0.343 | 212/236 | 5899 | 0 | 1253 | - |  |
| nym-base | **6** | 2.1% [0.7%, 4.0%] | 97.9% | 0.309 [0.286, 0.332] | 0.184 | 0.979 | 0.315 | 0.322 | 0.273 | 228/236 | 7200 | 0 | 2 | 308M |  |
| nuner-zero | **7** | 2.5% [0.8%, 4.5%] | 97.5% | 0.680 [0.636, 0.726] | 0.522 | 0.975 | 0.743 | 0.743 | 0.680 | 100/236 | 2017 | 0 | 7 | 449M |  |
| opf-kz-ru | **7** | 2.5% [0.7%, 4.5%] | 97.5% | 0.315 [0.291, 0.339] | 0.188 | 0.975 | 0.318 | 0.367 | 0.250 | 211/236 | 6813 | 0 | 59 | 1.4B |  |
| gliner2-vladlinv | **11** | 3.9% [1.8%, 6.4%] | 96.1% | 0.513 [0.478, 0.548] | 0.350 | 0.961 | 0.555 | 0.555 | 0.513 | 126/236 | 3088 | 0 | 3 | 287M |  |
| bardsai-eu | **14** | 5.0% [2.6%, 7.9%] | 95.0% | 0.330 [0.303, 0.357] | 0.200 | 0.950 | 0.326 | 0.330 | 0.000 | 208/236 | 6476 | 0 | 508 | - |  |
| gliner-multi-v21 | **15** | 5.4% [2.9%, 8.0%] | 94.6% | 0.612 [0.572, 0.651] | 0.452 | 0.946 | 0.641 | 0.641 | 0.612 | 139/236 | 2445 | 0 | 4 | 289M |  |
| opf-ru-v2 | **16** | 5.7% [3.2%, 8.4%] | 94.3% | 0.384 [0.355, 0.412] | 0.241 | 0.943 | 0.398 | 0.411 | 0.300 | 188/236 | 5163 | 0 | 261 | 1.4B |  |
| traciora | **18** | 6.4% [3.6%, 9.7%] | 93.6% | 0.382 [0.351, 0.410] | 0.240 | 0.936 | 0.377 | 0.399 | 0.255 | 195/236 | 5119 | 0 | 52 | 1.4B |  |
| openai-base | **20** | 7.1% [4.1%, 10.4%] | 92.9% | 0.329 [0.303, 0.353] | 0.200 | 0.929 | 0.350 | 0.379 | 0.256 | 203/236 | 6158 | 0 | 72 | 1.4B |  |
| gliner-urchade | **27** | 9.6% [6.3%, 13.3%] | 90.4% | 0.783 [0.747, 0.820] | 0.691 | 0.904 | 0.783 | 0.783 | 0.783 | 83/236 | 1019 | 0 | 3 | 289M |  |
| kalyan-ettin | **33** | 11.8% [8.0%, 15.7%] | 88.2% | 0.285 [0.261, 0.306] | 0.170 | 0.882 | 0.284 | 0.289 | 0.232 | 222/236 | 7174 | 0 | 3 | 68M |  |
| gliner2-large | **39** | 13.9% [9.7%, 17.8%] | 86.1% | 0.716 [0.678, 0.754] | 0.612 | 0.861 | 0.725 | 0.725 | 0.716 | 90/236 | 1245 | 0 | 4 | 486M |  |
| openmed-nemotron | **39** | 13.9% [10.1%, 18.5%] | 86.1% | 0.270 [0.247, 0.294] | 0.160 | 0.861 | 0.292 | 0.298 | 0.188 | 226/236 | 7363 | 0 | 29 | 1.4B |  |
| gliner2-fastino | **49** | 17.5% [13.1%, 22.0%] | 82.5% | 0.750 [0.712, 0.791] | 0.687 | 0.825 | 0.748 | 0.748 | 0.750 | 55/236 | 773 | 0 | 3 | 307M |  |
| mmbert32k | **50** | 17.9% [13.4%, 22.6%] | 82.1% | 0.271 [0.246, 0.295] | 0.162 | 0.821 | 0.210 | 0.211 | 0.000 | 231/236 | 7294 | 0 | 4 | 308M |  |
| ru-legal-ner | **56** | 20.0% [15.7%, 24.4%] | 80.0% | 0.355 [0.325, 0.384] | 0.228 | 0.800 | 0.331 | 0.340 | 0.000 | 199/236 | 4617 | 0 | 2 | 29M |  |
| gliner-stream-pii | **82** | 29.3% [23.9%, 35.0%] | 70.7% | 0.590 [0.546, 0.638] | 0.506 | 0.707 | 0.596 | 0.599 | 0.590 | 109/236 | 1533 | 0 | 35 | 677M |  |
| gravitee-small | **88** | 31.4% [26.1%, 36.8%] | 68.6% | 0.234 [0.211, 0.259] | 0.141 | 0.686 | 0.269 | 0.277 | 0.227 | 213/236 | 7037 | 0 | 3 | 29M |  |
| fef2-secret-ru | **112** | 40.0% [34.1%, 45.5%] | 60.0% | 0.465 [0.424, 0.509] | 0.380 | 0.600 | 0.461 | 0.479 | 0.413 | 85/236 | 1682 | 0 | 3 | 177M |  |
| ru-pii-ner | **121** | 43.2% [37.8%, 48.7%] | 56.8% | 0.277 [0.245, 0.309] | 0.183 | 0.568 | 0.283 | 0.286 | 0.000 | 189/236 | 4835 | 0 | 62 | 358M |  |
| stanza-ru | **193** | 68.9% [63.6%, 74.4%] | 31.1% | 0.074 [0.061, 0.089] | 0.042 | 0.311 | 0.047 | 0.099 | 0.000 | 235/236 | 12002 | 0 | 31 | - |  |
| gliner2-hivetrace-uni | **238** | 85.0% [80.9%, 89.0%] | 15.0% | 0.198 [0.148, 0.245] | 0.290 | 0.150 | 0.205 | 0.205 | 0.198 | 40/236 | 663 | 0 | 6 | 147M |  |
| rules-ru | **255** | 91.1% [87.9%, 94.3%] | 8.9% | 0.066 [0.043, 0.090] | 0.052 | 0.089 | 0.015 | 0.093 | 0.066 | 93/236 | 2272 | 0 | 0 | - |  |
| ner-ru-yqelz | **269** | 96.1% [93.4%, 98.2%] | 3.9% | 0.020 [0.009, 0.034] | 0.014 | 0.039 | 0.021 | 0.021 | 0.000 | 213/236 | 4533 | 0 | 3 | 559M |  |
| ner-ru-gherman | **277** | 98.9% [97.6%, 100.0%] | 1.1% | 0.010 [0.000, 0.024] | 0.010 | 0.011 | 0.008 | 0.008 | 0.000 | 140/236 | 1839 | 0 | 2 | 177M |  |
| spacy-ru-lg | **277** | 98.9% [97.7%, 100.0%] | 1.1% | 0.010 [0.000, 0.021] | 0.009 | 0.011 | 0.000 | 0.012 | 0.000 | 84/236 | 2208 | 0 | 3 | - |  |
| davlan-mbert | **278** | 99.3% [98.2%, 100.0%] | 0.7% | 0.006 [0.000, 0.016] | 0.005 | 0.007 | 0.005 | 0.005 | 0.000 | 156/236 | 2473 | 0 | 2 | 177M |  |
| davlan-xlmr | **280** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 176/236 | 2711 | 0 | 3 | 277M |  |
| natasha | **280** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 43/236 | 461 | 0 | 1 | - |  |
| spacy-alrosait | **280** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1/236 | 20 | 0 | 3 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: gliner-pii-base ≈ pplx; pplx ≈ openmed-multilingual; openmed-multilingual ≈ gliner-pii-edge; gliner-pii-edge ≈ gliner25-fastino; gliner25-fastino ≈ opf-ru; opf-ru ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ apararti; apararti ≈ gliner-nvidia; gliner-nvidia ≈ pii-shield-onnx; pii-shield-onnx ≈ nym-base; nym-base ≈ nuner-zero; nuner-zero ≈ opf-kz-ru; opf-kz-ru ≈ gliner2-vladlinv; gliner2-vladlinv ≈ bardsai-eu; bardsai-eu ≈ gliner-multi-v21; gliner-multi-v21 ≈ opf-ru-v2; opf-ru-v2 ≈ traciora; traciora ≈ openai-base; openai-base ≈ gliner-urchade; gliner-urchade ≈ kalyan-ettin; kalyan-ettin ≈ gliner2-large; gliner2-large ≈ openmed-nemotron; openmed-nemotron ≈ gliner2-fastino; gliner2-fastino ≈ mmbert32k; mmbert32k ≈ ru-legal-ner; gliner-stream-pii ≈ gravitee-small; fef2-secret-ru ≈ ru-pii-ner; ner-ru-gherman ≈ spacy-ru-lg; spacy-ru-lg ≈ davlan-mbert; davlan-mbert ≈ davlan-xlmr; davlan-xlmr ≈ natasha; natasha ≈ spacy-alrosait

## Missed by group

| model | SECRET |
|---|---|
| spans in gold | 280 |
| gliner-pii-base | 0 (0.0%) |
| pplx | 0 (0.0%) |
| openmed-multilingual | 0 (0.0%) |
| gliner-pii-edge | 1 (0.4%) |
| gliner25-fastino | 3 (1.1%) |
| opf-ru | 3 (1.1%) |
| gliner2-hivetrace-omni | 4 (1.4%) |
| apararti | 4 (1.4%) |
| gliner-nvidia | 6 (2.1%) |
| pii-shield-onnx | 6 (2.1%) |
| nym-base | 6 (2.1%) |
| nuner-zero | 7 (2.5%) |
| opf-kz-ru | 7 (2.5%) |
| gliner2-vladlinv | 11 (3.9%) |
| bardsai-eu | 14 (5.0%) |
| gliner-multi-v21 | 15 (5.4%) |
| opf-ru-v2 | 16 (5.7%) |
| traciora | 18 (6.4%) |
| openai-base | 20 (7.1%) |
| gliner-urchade | 27 (9.6%) |
| kalyan-ettin | 33 (11.8%) |
| gliner2-large | 39 (13.9%) |
| openmed-nemotron | 39 (13.9%) |
| gliner2-fastino | 49 (17.5%) |
| mmbert32k | 50 (17.9%) |
| ru-legal-ner | 56 (20.0%) |
| gliner-stream-pii | 82 (29.3%) |
| gravitee-small | 88 (31.4%) |
| fef2-secret-ru | 112 (40.0%) |
| ru-pii-ner | 121 (43.2%) |
| stanza-ru | 193 (68.9%) |
| gliner2-hivetrace-uni | 238 (85.0%) |
| rules-ru | 255 (91.1%) |
| ner-ru-yqelz | 269 (96.1%) |
| ner-ru-gherman | 277 (98.9%) |
| spacy-ru-lg | 277 (98.9%) |
| davlan-mbert | 278 (99.3%) |
| davlan-xlmr | 280 (100.0%) |
| natasha | 280 (100.0%) |
| spacy-alrosait | 280 (100.0%) |

## Char recall by gold type

| type | group | gliner-pii-base | pplx | openmed-multilingual | gliner-pii-edge | gliner25-fastino | opf-ru | gliner2-hivetrace-omni | apararti | gliner-nvidia | pii-shield-onnx | nym-base | nuner-zero | opf-kz-ru | gliner2-vladlinv | bardsai-eu | gliner-multi-v21 | opf-ru-v2 | traciora | openai-base | gliner-urchade | kalyan-ettin | gliner2-large | openmed-nemotron | gliner2-fastino | mmbert32k | ru-legal-ner | gliner-stream-pii | gravitee-small | fef2-secret-ru | ru-pii-ner | stanza-ru | gliner2-hivetrace-uni | rules-ru | ner-ru-yqelz | ner-ru-gherman | spacy-ru-lg | davlan-mbert | davlan-xlmr | natasha | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PASSWORD | SECRET | 1.000 | 1.000 | 1.000 | 0.996 | 0.989 | 0.989 | 0.986 | 0.986 | 0.979 | 0.979 | 0.979 | 0.975 | 0.975 | 0.961 | 0.950 | 0.946 | 0.943 | 0.936 | 0.929 | 0.904 | 0.882 | 0.861 | 0.861 | 0.825 | 0.821 | 0.800 | 0.707 | 0.686 | 0.600 | 0.568 | 0.311 | 0.150 | 0.089 | 0.039 | 0.011 | 0.011 | 0.007 | 0.000 | 0.000 | 0.000 |

## char F1 by domain

| domain | n | gliner-pii-base | pplx | openmed-multilingual | gliner-pii-edge | gliner25-fastino | opf-ru | gliner2-hivetrace-omni | apararti | gliner-nvidia | pii-shield-onnx | nym-base | nuner-zero | opf-kz-ru | gliner2-vladlinv | bardsai-eu | gliner-multi-v21 | opf-ru-v2 | traciora | openai-base | gliner-urchade | kalyan-ettin | gliner2-large | openmed-nemotron | gliner2-fastino | mmbert32k | ru-legal-ner | gliner-stream-pii | gravitee-small | fef2-secret-ru | ru-pii-ner | stanza-ru | gliner2-hivetrace-uni | rules-ru | ner-ru-yqelz | ner-ru-gherman | spacy-ru-lg | davlan-mbert | davlan-xlmr | natasha | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| easy | 289 | 0.715 | 0.281 | 0.226 | 0.632 | 0.717 | 0.356 | 0.644 | 0.318 | 0.769 | 0.340 | 0.301 | 0.827 | 0.306 | 0.573 | 0.324 | 0.658 | 0.396 | 0.392 | 0.337 | 0.975 | 0.300 | 0.941 | 0.291 | 0.977 | 0.273 | 0.350 | 0.730 | 0.308 | 0.656 | 0.283 | 0.074 | 0.041 | 0.122 | 0.007 | 0.007 | 0.006 | 0.000 | 0.000 | 0.000 | 0.000 |
| hard | 227 | 0.746 | 0.312 | 0.244 | 0.581 | 0.481 | 0.387 | 0.600 | 0.330 | 0.720 | 0.361 | 0.319 | 0.570 | 0.326 | 0.459 | 0.337 | 0.567 | 0.371 | 0.371 | 0.319 | 0.625 | 0.267 | 0.532 | 0.246 | 0.547 | 0.269 | 0.360 | 0.426 | 0.141 | 0.199 | 0.269 | 0.075 | 0.332 | 0.000 | 0.036 | 0.014 | 0.014 | 0.014 | 0.000 | 0.000 | 0.000 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| gliner-pii-base | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| openmed-multilingual | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| gliner-pii-edge | 1 (0.4%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| gliner25-fastino | 3 (1.1%) | 2 (0.7%) | 2 (0.7%) | 2 (0.7%) |
| opf-ru | 3 (1.1%) | 2 (0.7%) | 2 (0.7%) | 2 (0.7%) |
| gliner2-hivetrace-omni | 4 (1.4%) | 2 (0.7%) | 2 (0.7%) | 1 (0.4%) |
| apararti | 4 (1.4%) | 4 (1.4%) | 4 (1.4%) | 4 (1.4%) |
| gliner-nvidia | 6 (2.1%) | 6 (2.1%) | 5 (1.8%) | 3 (1.1%) |
| pii-shield-onnx | 6 (2.1%) | 3 (1.1%) | 3 (1.1%) | 3 (1.1%) |
| nym-base | 6 (2.1%) | 4 (1.4%) | 4 (1.4%) | 4 (1.4%) |
| nuner-zero | 7 (2.5%) | 7 (2.5%) | 5 (1.8%) | 4 (1.4%) |
| opf-kz-ru | 7 (2.5%) | 6 (2.1%) | 6 (2.1%) | 6 (2.1%) |
| gliner2-vladlinv | 11 (3.9%) | 10 (3.6%) | 9 (3.2%) | 9 (3.2%) |
| bardsai-eu | 14 (5.0%) | 3 (1.1%) | 3 (1.1%) | 3 (1.1%) |
| gliner-multi-v21 | 15 (5.4%) | 7 (2.5%) | 6 (2.1%) | 5 (1.8%) |
| opf-ru-v2 | 16 (5.7%) | 13 (4.6%) | 13 (4.6%) | 13 (4.6%) |
| traciora | 18 (6.4%) | 15 (5.4%) | 15 (5.4%) | 15 (5.4%) |
| openai-base | 20 (7.1%) | 20 (7.1%) | 20 (7.1%) | 20 (7.1%) |
| gliner-urchade | 27 (9.6%) | 17 (6.1%) | 15 (5.4%) | 10 (3.6%) |
| kalyan-ettin | 33 (11.8%) | 16 (5.7%) | 16 (5.7%) | 16 (5.7%) |
| gliner2-large | 39 (13.9%) | 36 (12.9%) | 30 (10.7%) | 27 (9.6%) |
| openmed-nemotron | 39 (13.9%) | 24 (8.6%) | 23 (8.2%) | 23 (8.2%) |
| gliner2-fastino | 49 (17.5%) | 37 (13.2%) | 32 (11.4%) | 29 (10.4%) |
| mmbert32k | 50 (17.9%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| ru-legal-ner | 56 (20.0%) | 24 (8.6%) | 22 (7.9%) | 22 (7.9%) |
| gliner-stream-pii | 82 (29.3%) | 60 (21.4%) | 42 (15.0%) | 24 (8.6%) |
| gravitee-small | 88 (31.4%) | 85 (30.4%) | 85 (30.4%) | 85 (30.4%) |
| fef2-secret-ru | 112 (40.0%) | 110 (39.3%) | 110 (39.3%) | 110 (39.3%) |
| gliner2-hivetrace-uni | 238 (85.0%) | 144 (51.4%) | 83 (29.6%) | 26 (9.3%) |
| ner-ru-yqelz | 269 (96.1%) | 267 (95.4%) | 267 (95.4%) | 267 (95.4%) |
| ner-ru-gherman | 277 (98.9%) | 277 (98.9%) | 277 (98.9%) | 277 (98.9%) |
| davlan-mbert | 278 (99.3%) | 278 (99.3%) | 278 (99.3%) | 278 (99.3%) |
| davlan-xlmr | 280 (100.0%) | 280 (100.0%) | 280 (100.0%) | 280 (100.0%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
