# multiconer-ru - ru / pii (1500 rows, 1208 spans, 420 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.200 (80.0% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ner-ru-yqelz | **42** | 3.5% [2.4%, 4.6%] | 93.5% | 0.637 [0.618, 0.656] | 0.475 | 0.966 | 0.390 | 0.696 | 0.437 | 397/420 | 8519 | 0 | 2 | 559M |  |
| gliner2-fastino | **95** | 7.9% [6.4%, 9.5%] | 73.8% | 0.646 [0.628, 0.666] | 0.526 | 0.838 | 0.421 | 0.654 | 0.335 | 293/420 | 4127 | 3 | 2 | 307M |  |
| gliner2-fastino-ru | **97** | 8.0% [6.5%, 9.8%] | 72.8% | 0.662 [0.642, 0.683] | 0.556 | 0.818 | 0.440 | 0.675 | 0.167 | 286/420 | 3792 | 2 | 5 | 307M |  |
| gliner2-hivetrace-omni | **120** | 9.9% [8.4%, 11.7%] | 73.9% | 0.656 [0.636, 0.675] | 0.552 | 0.809 | 0.465 | 0.663 | 0.352 | 305/420 | 4323 | 0 | 3 | 307M |  |
| gliner2-hivetrace-omni-ru | **136** | 11.3% [9.5%, 13.1%] | 72.7% | 0.642 [0.620, 0.660] | 0.539 | 0.792 | 0.461 | 0.649 | 0.148 | 308/420 | 4412 | 0 | 2 | 307M |  |
| gliner25-fastino | **238** | 19.7% [17.4%, 21.9%] | 60.9% | 0.628 [0.606, 0.650] | 0.559 | 0.716 | 0.423 | 0.640 | 0.325 | 287/420 | 3882 | 8 | 1 | 287M |  |
| gliner25-fastino-ru | **259** | 21.4% [19.1%, 23.9%] | 59.2% | 0.628 [0.605, 0.649] | 0.594 | 0.666 | 0.437 | 0.652 | 0.201 | 255/420 | 3077 | 5 | 4 | 287M |  |
| gliner2-large | **311** | 25.7% [23.3%, 28.5%] | 55.0% | 0.539 [0.517, 0.560] | 0.493 | 0.594 | 0.359 | 0.578 | 0.288 | 318/420 | 4208 | 3 | 3 | 486M |  |
| gliner-urchade | **322** | 26.7% [24.3%, 29.3%] | 66.3% | 0.621 [0.598, 0.644] | 0.560 | 0.698 | 0.487 | 0.654 | 0.265 | 162/420 | 2785 | 0 | 3 | 289M |  |
| gliner-pii-edge | **341** | 28.2% [26.0%, 30.9%] | 43.4% | 0.487 [0.463, 0.505] | 0.424 | 0.571 | 0.237 | 0.520 | 0.132 | 315/420 | 4824 | 0 | 14 | 45M |  |
| spacy-ru-lg | **388** | 32.1% [29.5%, 34.8%] | 50.2% | 0.624 [0.600, 0.647] | 0.656 | 0.595 | 0.431 | 0.654 | 0.439 | 134/420 | 1693 | 0 | 1 | - |  |
| gliner-multi-v21 | **410** | 33.9% [31.6%, 36.7%] | 48.8% | 0.591 [0.568, 0.614] | 0.593 | 0.590 | 0.400 | 0.607 | 0.283 | 150/420 | 1976 | 0 | 2 | 289M |  |
| nuner-zero | **467** | 38.7% [35.7%, 41.3%] | 43.6% | 0.507 [0.484, 0.531] | 0.519 | 0.496 | 0.296 | 0.565 | 0.227 | 191/420 | 2340 | 0 | 4 | 449M |  |
| gliner-multi-v21-ru | **494** | 40.9% [38.1%, 43.6%] | 42.7% | 0.552 [0.526, 0.578] | 0.604 | 0.508 | 0.380 | 0.585 | 0.185 | 123/420 | 1624 | 0 | 6 | 289M |  |
| gliner-nvidia | **496** | 41.1% [38.2%, 43.9%] | 44.0% | 0.526 [0.501, 0.553] | 0.549 | 0.505 | 0.343 | 0.573 | 0.214 | 192/420 | 2454 | 0 | 4 | 445M |  |
| gliner-stream-pii | **508** | 42.1% [39.2%, 44.8%] | 32.5% | 0.457 [0.433, 0.483] | 0.488 | 0.430 | 0.229 | 0.525 | 0.153 | 278/420 | 2810 | 0 | 18 | 677M |  |
| gliner2-hivetrace-uni | **532** | 44.0% [41.4%, 46.9%] | 43.0% | 0.542 [0.515, 0.569] | 0.668 | 0.456 | 0.416 | 0.598 | 0.402 | 182/420 | 1837 | 1 | 6 | 147M |  |
| gliner-urchade-ru | **546** | 45.2% [42.3%, 48.2%] | 48.8% | 0.554 [0.527, 0.580] | 0.597 | 0.517 | 0.422 | 0.588 | 0.096 | 115/420 | 1627 | 0 | 4 | 289M |  |
| mmbert32k | **561** | 46.4% [43.5%, 49.5%] | 28.0% | 0.470 [0.446, 0.496] | 0.566 | 0.403 | 0.221 | 0.480 | 0.240 | 177/420 | 1687 | 0 | 2 | 308M |  |
| gliner2-hivetrace-uni-ru | **567** | 46.9% [44.0%, 49.8%] | 39.6% | 0.507 [0.479, 0.535] | 0.647 | 0.417 | 0.383 | 0.573 | 0.124 | 172/420 | 1822 | 0 | 7 | 147M |  |
| ru-legal-ner | **617** | 51.1% [48.2%, 54.1%] | 27.4% | 0.399 [0.375, 0.421] | 0.413 | 0.385 | 0.165 | 0.451 | 0.228 | 156/420 | 2651 | 0 | 1 | 29M |  |
| gliner-nvidia-ru | **620** | 51.3% [48.3%, 54.2%] | 34.6% | 0.474 [0.447, 0.500] | 0.620 | 0.383 | 0.347 | 0.535 | 0.112 | 145/420 | 1565 | 0 | 22 | 445M |  |
| nym-base | **644** | 53.3% [50.3%, 56.3%] | 32.5% | 0.459 [0.434, 0.486] | 0.500 | 0.425 | 0.189 | 0.463 | 0.255 | 120/420 | 1383 | 0 | 2 | 308M |  |
| gravitee-small | **646** | 53.5% [50.4%, 56.4%] | 32.3% | 0.348 [0.326, 0.368] | 0.301 | 0.412 | 0.089 | 0.429 | 0.178 | 248/420 | 5106 | 0 | 2 | 29M |  |
| davlan-xlmr | **700** | 57.9% [54.8%, 60.9%] | 29.2% | 0.497 [0.465, 0.530] | 0.708 | 0.383 | 0.334 | 0.516 | 0.343 | 40/420 | 519 | 0 | 1 | 277M |  |
| gliner-pii-base | **722** | 59.8% [56.8%, 62.6%] | 26.2% | 0.392 [0.365, 0.419] | 0.562 | 0.300 | 0.270 | 0.452 | 0.207 | 134/420 | 1324 | 0 | 2 | 166M |  |
| gliner2-vladlinv | **732** | 60.6% [57.6%, 63.3%] | 32.0% | 0.442 [0.413, 0.470] | 0.660 | 0.332 | 0.345 | 0.488 | 0.278 | 81/420 | 883 | 1 | 1 | 287M |  |
| gliner2-vladlinv-ru | **735** | 60.8% [57.8%, 63.7%] | 32.2% | 0.444 [0.415, 0.475] | 0.665 | 0.334 | 0.346 | 0.488 | 0.267 | 77/420 | 856 | 1 | 2 | 287M |  |
| davlan-mbert | **761** | 63.0% [60.1%, 65.9%] | 24.2% | 0.427 [0.395, 0.460] | 0.694 | 0.308 | 0.292 | 0.480 | 0.282 | 31/420 | 487 | 0 | 1 | 177M |  |
| fef2-secret-ru | **770** | 63.7% [61.2%, 66.5%] | 24.4% | 0.422 [0.392, 0.453] | 0.682 | 0.306 | 0.279 | 0.465 | 0.304 | 50/420 | 648 | 0 | 1 | 177M |  |
| ru-pii-ner | **789** | 65.3% [62.4%, 68.4%] | 25.5% | 0.394 [0.365, 0.422] | 0.556 | 0.305 | 0.249 | 0.425 | 0.216 | 76/420 | 886 | 0 | 32 | 358M |  |
| ner-ru-gherman | **836** | 69.2% [66.4%, 71.8%] | 10.2% | 0.341 [0.315, 0.366] | 0.655 | 0.231 | 0.123 | 0.401 | 0.059 | 35/420 | 367 | 0 | 1 | 177M |  |
| bardsai-eu | **845** | 70.0% [67.0%, 72.8%] | 22.0% | 0.368 [0.334, 0.399] | 0.522 | 0.284 | 0.252 | 0.377 | 0.106 | 42/420 | 875 | 0 | 398 | - |  |
| nym-small | **847** | 70.1% [67.3%, 72.7%] | 20.0% | 0.332 [0.305, 0.362] | 0.431 | 0.269 | 0.126 | 0.342 | 0.212 | 101/420 | 1218 | 0 | 358 | - |  |
| kalyan-ettin | **886** | 73.3% [70.7%, 75.8%] | 9.6% | 0.233 [0.210, 0.258] | 0.421 | 0.161 | 0.101 | 0.301 | 0.125 | 141/420 | 1238 | 0 | 2 | 68M |  |
| traciora | **897** | 74.3% [71.7%, 76.7%] | 13.7% | 0.313 [0.285, 0.341] | 0.506 | 0.226 | 0.116 | 0.351 | 0.177 | 87/420 | 1198 | 0 | 210 | 1.4B |  |
| openmed-nemotron | **901** | 74.6% [72.0%, 77.1%] | 10.8% | 0.258 [0.233, 0.283] | 0.350 | 0.204 | 0.081 | 0.294 | 0.120 | 132/420 | 1904 | 0 | 15 | 1.4B |  |
| pii-shield-onnx | **932** | 77.2% [74.8%, 79.6%] | 11.2% | 0.269 [0.241, 0.297] | 0.454 | 0.192 | 0.116 | 0.276 | 0.166 | 141/420 | 1176 | 0 | 789 | - |  |
| openmed-multilingual | **941** | 77.9% [75.5%, 80.1%] | 7.3% | 0.205 [0.182, 0.227] | 0.354 | 0.144 | 0.069 | 0.244 | 0.119 | 200/420 | 1652 | 0 | 26 | 1.4B |  |
| opf-ru | **962** | 79.6% [77.3%, 81.9%] | 6.1% | 0.200 [0.178, 0.223] | 0.492 | 0.125 | 0.072 | 0.278 | 0.101 | 98/420 | 744 | 0 | 31 | 1.4B |  |
| pplx | **975** | 80.7% [78.6%, 82.9%] | 11.7% | 0.240 [0.211, 0.269] | 0.542 | 0.154 | 0.143 | 0.281 | 0.193 | 51/420 | 576 | 0 | 54 | 596M |  |
| stanza-ru | **1087** | 90.0% [88.3%, 91.6%] | 7.1% | 0.133 [0.107, 0.159] | 0.506 | 0.077 | 0.109 | 0.167 | 0.068 | 68/420 | 699 | 0 | 15 | - |  |
| apararti | **1101** | 91.1% [89.4%, 92.9%] | 4.7% | 0.114 [0.091, 0.139] | 0.259 | 0.073 | 0.024 | 0.136 | 0.070 | 68/420 | 843 | 0 | 56 | 1.4B |  |
| openai-base | **1122** | 92.9% [91.4%, 94.3%] | 4.2% | 0.116 [0.091, 0.141] | 0.410 | 0.067 | 0.033 | 0.124 | 0.077 | 23/420 | 321 | 0 | 66 | 1.4B |  |
| opf-ru-v2 | **1126** | 93.2% [91.6%, 94.6%] | 3.1% | 0.098 [0.076, 0.122] | 0.537 | 0.054 | 0.039 | 0.120 | 0.067 | 25/420 | 229 | 0 | 208 | 1.4B |  |
| opf-kz-ru | **1159** | 95.9% [94.7%, 97.1%] | 2.2% | 0.055 [0.038, 0.073] | 0.247 | 0.031 | 0.018 | 0.069 | 0.033 | 34/420 | 392 | 0 | 49 | 1.4B |  |
| natasha | **1198** | 99.2% [98.6%, 99.7%] | 0.7% | 0.013 [0.005, 0.022] | 0.911 | 0.006 | 0.015 | 0.016 | 0.010 | 1/420 | 4 | 0 | 0 | - |  |
| spacy-alrosait | **1200** | 99.3% [98.9%, 99.8%] | 0.2% | 0.010 [0.003, 0.018] | 0.474 | 0.005 | 0.002 | 0.013 | 0.002 | 5/420 | 22 | 0 | 1 | - |  |
| rules-ru | **1202** | 99.5% [99.1%, 99.8%] | 0.2% | 0.005 [0.002, 0.009] | 1.000 | 0.003 | 0.005 | 0.010 | 0.000 | 0/420 | 0 | 0 | 0 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: gliner2-fastino ≈ gliner2-fastino-ru; gliner2-hivetrace-omni ≈ gliner2-hivetrace-omni-ru; gliner25-fastino ≈ gliner25-fastino-ru; gliner2-large ≈ gliner-urchade; gliner-urchade ≈ gliner-pii-edge; spacy-ru-lg ≈ gliner-multi-v21; nuner-zero ≈ gliner-multi-v21-ru; gliner-multi-v21-ru ≈ gliner-nvidia; gliner-nvidia ≈ gliner-stream-pii; gliner-stream-pii ≈ gliner2-hivetrace-uni; gliner2-hivetrace-uni ≈ gliner-urchade-ru; gliner-urchade-ru ≈ mmbert32k; mmbert32k ≈ gliner2-hivetrace-uni-ru; ru-legal-ner ≈ gliner-nvidia-ru; gliner-nvidia-ru ≈ nym-base; nym-base ≈ gravitee-small; gravitee-small ≈ davlan-xlmr; davlan-xlmr ≈ gliner-pii-base; gliner-pii-base ≈ gliner2-vladlinv; gliner2-vladlinv ≈ gliner2-vladlinv-ru; gliner2-vladlinv-ru ≈ davlan-mbert; davlan-mbert ≈ fef2-secret-ru; fef2-secret-ru ≈ ru-pii-ner; ner-ru-gherman ≈ bardsai-eu; bardsai-eu ≈ nym-small; nym-small ≈ kalyan-ettin; kalyan-ettin ≈ traciora; traciora ≈ openmed-nemotron; openmed-nemotron ≈ pii-shield-onnx; pii-shield-onnx ≈ openmed-multilingual; openmed-multilingual ≈ opf-ru; opf-ru ≈ pplx; stanza-ru ≈ apararti; openai-base ≈ opf-ru-v2; natasha ≈ spacy-alrosait; spacy-alrosait ≈ rules-ru

## Missed by group

| model | PERSON | ADDRESS | ORG |
|---|---|---|---|
| spans in gold | 305 | 379 | 524 |
| ner-ru-yqelz | 3 (1.0%) | 18 (4.7%) | 21 (4.0%) |
| gliner2-fastino | 6 (2.0%) | 37 (9.8%) | 52 (9.9%) |
| gliner2-fastino-ru | 5 (1.6%) | 32 (8.4%) | 60 (11.5%) |
| gliner2-hivetrace-omni | 22 (7.2%) | 55 (14.5%) | 43 (8.2%) |
| gliner2-hivetrace-omni-ru | 29 (9.5%) | 54 (14.2%) | 53 (10.1%) |
| gliner25-fastino | 16 (5.2%) | 70 (18.5%) | 152 (29.0%) |
| gliner25-fastino-ru | 10 (3.3%) | 64 (16.9%) | 185 (35.3%) |
| gliner2-large | 69 (22.6%) | 106 (28.0%) | 136 (26.0%) |
| gliner-urchade | 38 (12.5%) | 122 (32.2%) | 162 (30.9%) |
| gliner-pii-edge | 55 (18.0%) | 99 (26.1%) | 187 (35.7%) |
| spacy-ru-lg | 40 (13.1%) | 159 (42.0%) | 189 (36.1%) |
| gliner-multi-v21 | 37 (12.1%) | 112 (29.6%) | 261 (49.8%) |
| nuner-zero | 63 (20.7%) | 94 (24.8%) | 310 (59.2%) |
| gliner-multi-v21-ru | 52 (17.0%) | 124 (32.7%) | 318 (60.7%) |
| gliner-nvidia | 96 (31.5%) | 151 (39.8%) | 249 (47.5%) |
| gliner-stream-pii | 110 (36.1%) | 200 (52.8%) | 198 (37.8%) |
| gliner2-hivetrace-uni | 65 (21.3%) | 257 (67.8%) | 210 (40.1%) |
| gliner-urchade-ru | 177 (58.0%) | 120 (31.7%) | 249 (47.5%) |
| mmbert32k | 63 (20.7%) | 170 (44.9%) | 328 (62.6%) |
| gliner2-hivetrace-uni-ru | 124 (40.7%) | 216 (57.0%) | 227 (43.3%) |
| ru-legal-ner | 80 (26.2%) | 236 (62.3%) | 301 (57.4%) |
| gliner-nvidia-ru | 130 (42.6%) | 188 (49.6%) | 302 (57.6%) |
| nym-base | 138 (45.2%) | 204 (53.8%) | 302 (57.6%) |
| gravitee-small | 124 (40.7%) | 207 (54.6%) | 315 (60.1%) |
| davlan-xlmr | 151 (49.5%) | 223 (58.8%) | 326 (62.2%) |
| gliner-pii-base | 182 (59.7%) | 211 (55.7%) | 329 (62.8%) |
| gliner2-vladlinv | 44 (14.4%) | 217 (57.3%) | 471 (89.9%) |
| gliner2-vladlinv-ru | 46 (15.1%) | 214 (56.5%) | 475 (90.6%) |
| davlan-mbert | 164 (53.8%) | 233 (61.5%) | 364 (69.5%) |
| fef2-secret-ru | 130 (42.6%) | 245 (64.6%) | 395 (75.4%) |
| ru-pii-ner | 84 (27.5%) | 228 (60.2%) | 477 (91.0%) |
| ner-ru-gherman | 140 (45.9%) | 222 (58.6%) | 474 (90.5%) |
| bardsai-eu | 216 (70.8%) | 243 (64.1%) | 386 (73.7%) |
| nym-small | 220 (72.1%) | 273 (72.0%) | 354 (67.6%) |
| kalyan-ettin | 196 (64.3%) | 281 (74.1%) | 409 (78.1%) |
| traciora | 159 (52.1%) | 290 (76.5%) | 448 (85.5%) |
| openmed-nemotron | 207 (67.9%) | 293 (77.3%) | 401 (76.5%) |
| pii-shield-onnx | 209 (68.5%) | 287 (75.7%) | 436 (83.2%) |
| openmed-multilingual | 239 (78.4%) | 293 (77.3%) | 409 (78.1%) |
| opf-ru | 195 (63.9%) | 309 (81.5%) | 458 (87.4%) |
| pplx | 160 (52.5%) | 337 (88.9%) | 478 (91.2%) |
| stanza-ru | 284 (93.1%) | 365 (96.3%) | 438 (83.6%) |
| apararti | 266 (87.2%) | 339 (89.4%) | 496 (94.7%) |
| openai-base | 260 (85.2%) | 355 (93.7%) | 507 (96.8%) |
| opf-ru-v2 | 255 (83.6%) | 361 (95.3%) | 510 (97.3%) |
| opf-kz-ru | 284 (93.1%) | 365 (96.3%) | 510 (97.3%) |
| natasha | 303 (99.3%) | 378 (99.7%) | 517 (98.7%) |
| spacy-alrosait | 302 (99.0%) | 377 (99.5%) | 521 (99.4%) |
| rules-ru | 304 (99.7%) | 379 (100.0%) | 519 (99.0%) |

## Char recall by gold type

| type | group | ner-ru-yqelz | gliner2-fastino | gliner2-fastino-ru | gliner2-hivetrace-omni | gliner2-hivetrace-omni-ru | gliner25-fastino | gliner25-fastino-ru | gliner2-large | gliner-urchade | gliner-pii-edge | spacy-ru-lg | gliner-multi-v21 | nuner-zero | gliner-multi-v21-ru | gliner-nvidia | gliner-stream-pii | gliner2-hivetrace-uni | gliner-urchade-ru | mmbert32k | gliner2-hivetrace-uni-ru | ru-legal-ner | gliner-nvidia-ru | nym-base | gravitee-small | davlan-xlmr | gliner-pii-base | gliner2-vladlinv | gliner2-vladlinv-ru | davlan-mbert | fef2-secret-ru | ru-pii-ner | ner-ru-gherman | bardsai-eu | nym-small | kalyan-ettin | traciora | openmed-nemotron | pii-shield-onnx | openmed-multilingual | opf-ru | pplx | stanza-ru | apararti | openai-base | opf-ru-v2 | opf-kz-ru | natasha | spacy-alrosait | rules-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CORP | ORG | 0.977 | 0.898 | 0.871 | 0.885 | 0.871 | 0.777 | 0.759 | 0.783 | 0.738 | 0.515 | 0.667 | 0.582 | 0.406 | 0.518 | 0.612 | 0.536 | 0.632 | 0.607 | 0.286 | 0.580 | 0.304 | 0.551 | 0.461 | 0.435 | 0.318 | 0.406 | 0.072 | 0.065 | 0.194 | 0.124 | 0.082 | 0.023 | 0.276 | 0.390 | 0.167 | 0.081 | 0.199 | 0.149 | 0.138 | 0.081 | 0.040 | 0.105 | 0.039 | 0.024 | 0.013 | 0.023 | 0.011 | 0.001 | 0.009 |
| GRP | ORG | 0.955 | 0.712 | 0.667 | 0.726 | 0.718 | 0.523 | 0.363 | 0.401 | 0.601 | 0.467 | 0.436 | 0.353 | 0.216 | 0.196 | 0.386 | 0.398 | 0.330 | 0.427 | 0.176 | 0.321 | 0.272 | 0.203 | 0.323 | 0.273 | 0.345 | 0.159 | 0.052 | 0.048 | 0.276 | 0.234 | 0.033 | 0.082 | 0.256 | 0.236 | 0.076 | 0.127 | 0.172 | 0.081 | 0.143 | 0.045 | 0.040 | 0.120 | 0.032 | 0.016 | 0.020 | 0.008 | 0.006 | 0.004 | 0.002 |
| LOC | ADDRESS | 0.960 | 0.846 | 0.853 | 0.793 | 0.789 | 0.750 | 0.734 | 0.658 | 0.662 | 0.673 | 0.529 | 0.659 | 0.662 | 0.636 | 0.524 | 0.408 | 0.258 | 0.664 | 0.485 | 0.345 | 0.311 | 0.421 | 0.416 | 0.402 | 0.377 | 0.378 | 0.358 | 0.383 | 0.352 | 0.318 | 0.397 | 0.319 | 0.341 | 0.253 | 0.197 | 0.230 | 0.194 | 0.277 | 0.176 | 0.140 | 0.096 | 0.030 | 0.103 | 0.081 | 0.038 | 0.035 | 0.003 | 0.004 | 0.000 |
| PER | PERSON | 0.977 | 0.926 | 0.913 | 0.864 | 0.818 | 0.855 | 0.871 | 0.608 | 0.813 | 0.628 | 0.787 | 0.793 | 0.711 | 0.727 | 0.541 | 0.410 | 0.669 | 0.401 | 0.664 | 0.476 | 0.649 | 0.424 | 0.521 | 0.565 | 0.482 | 0.302 | 0.818 | 0.811 | 0.387 | 0.513 | 0.689 | 0.465 | 0.263 | 0.233 | 0.217 | 0.445 | 0.254 | 0.263 | 0.118 | 0.234 | 0.428 | 0.053 | 0.115 | 0.144 | 0.140 | 0.058 | 0.006 | 0.011 | 0.001 |

## char F1 by domain

| domain | n | ner-ru-yqelz | gliner2-fastino | gliner2-fastino-ru | gliner2-hivetrace-omni | gliner2-hivetrace-omni-ru | gliner25-fastino | gliner25-fastino-ru | gliner2-large | gliner-urchade | gliner-pii-edge | spacy-ru-lg | gliner-multi-v21 | nuner-zero | gliner-multi-v21-ru | gliner-nvidia | gliner-stream-pii | gliner2-hivetrace-uni | gliner-urchade-ru | mmbert32k | gliner2-hivetrace-uni-ru | ru-legal-ner | gliner-nvidia-ru | nym-base | gravitee-small | davlan-xlmr | gliner-pii-base | gliner2-vladlinv | gliner2-vladlinv-ru | davlan-mbert | fef2-secret-ru | ru-pii-ner | ner-ru-gherman | bardsai-eu | nym-small | kalyan-ettin | traciora | openmed-nemotron | pii-shield-onnx | openmed-multilingual | opf-ru | pplx | stanza-ru | apararti | openai-base | opf-ru-v2 | opf-kz-ru | natasha | spacy-alrosait | rules-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ru-lowner | 700 | 0.585 | 0.576 | 0.590 | 0.591 | 0.574 | 0.582 | 0.597 | 0.510 | 0.568 | 0.413 | 0.630 | 0.578 | 0.475 | 0.547 | 0.497 | 0.420 | 0.554 | 0.486 | 0.480 | 0.500 | 0.374 | 0.480 | 0.478 | 0.213 | 0.578 | 0.425 | 0.407 | 0.404 | 0.512 | 0.499 | 0.362 | 0.394 | 0.455 | 0.363 | 0.225 | 0.231 | 0.190 | 0.254 | 0.154 | 0.187 | 0.244 | 0.171 | 0.104 | 0.069 | 0.116 | 0.051 | 0.022 | 0.010 | 0.002 |
| ru-msq | 104 | 0.779 | 0.852 | 0.853 | 0.832 | 0.815 | 0.823 | 0.811 | 0.710 | 0.751 | 0.731 | 0.612 | 0.727 | 0.725 | 0.676 | 0.530 | 0.483 | 0.542 | 0.716 | 0.561 | 0.515 | 0.567 | 0.481 | 0.392 | 0.568 | 0.500 | 0.436 | 0.714 | 0.739 | 0.346 | 0.427 | 0.658 | 0.377 | 0.367 | 0.160 | 0.246 | 0.540 | 0.232 | 0.462 | 0.258 | 0.323 | 0.315 | 0.000 | 0.217 | 0.214 | 0.111 | 0.102 | 0.000 | 0.000 | 0.000 |
| ru-orcas | 696 | 0.664 | 0.704 | 0.722 | 0.704 | 0.692 | 0.651 | 0.631 | 0.548 | 0.672 | 0.547 | 0.619 | 0.585 | 0.506 | 0.535 | 0.557 | 0.497 | 0.530 | 0.604 | 0.442 | 0.513 | 0.407 | 0.466 | 0.441 | 0.463 | 0.394 | 0.343 | 0.418 | 0.420 | 0.336 | 0.324 | 0.375 | 0.270 | 0.227 | 0.314 | 0.240 | 0.354 | 0.343 | 0.249 | 0.253 | 0.188 | 0.221 | 0.119 | 0.106 | 0.140 | 0.078 | 0.049 | 0.007 | 0.013 | 0.009 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| ner-ru-yqelz | 42 (3.5%) | 41 (3.4%) | 41 (3.4%) | 41 (3.4%) |
| gliner2-fastino | 95 (7.9%) | 67 (5.5%) | 48 (4.0%) | 31 (2.6%) |
| gliner2-fastino-ru | 97 (8.0%) | 59 (4.9%) | 45 (3.7%) | 29 (2.4%) |
| gliner2-hivetrace-omni | 120 (9.9%) | 48 (4.0%) | 36 (3.0%) | 26 (2.2%) |
| gliner2-hivetrace-omni-ru | 136 (11.3%) | 52 (4.3%) | 33 (2.7%) | 22 (1.8%) |
| gliner25-fastino | 238 (19.7%) | 199 (16.5%) | 185 (15.3%) | 170 (14.1%) |
| gliner25-fastino-ru | 259 (21.4%) | 230 (19.0%) | 214 (17.7%) | 202 (16.7%) |
| gliner2-large | 311 (25.7%) | 178 (14.7%) | 117 (9.7%) | 80 (6.6%) |
| gliner-urchade | 322 (26.7%) | 144 (11.9%) | 103 (8.5%) | 67 (5.5%) |
| gliner-pii-edge | 341 (28.2%) | 50 (4.1%) | 17 (1.4%) | 2 (0.2%) |
| gliner-multi-v21 | 410 (33.9%) | 221 (18.3%) | 134 (11.1%) | 60 (5.0%) |
| nuner-zero | 467 (38.7%) | 334 (27.6%) | 241 (20.0%) | 162 (13.4%) |
| gliner-multi-v21-ru | 494 (40.9%) | 296 (24.5%) | 190 (15.7%) | 90 (7.5%) |
| gliner-nvidia | 496 (41.1%) | 322 (26.7%) | 235 (19.5%) | 124 (10.3%) |
| gliner-stream-pii | 508 (42.1%) | 271 (22.4%) | 168 (13.9%) | 88 (7.3%) |
| gliner2-hivetrace-uni | 532 (44.0%) | 321 (26.6%) | 219 (18.1%) | 125 (10.3%) |
| gliner-urchade-ru | 546 (45.2%) | 272 (22.5%) | 183 (15.1%) | 95 (7.9%) |
| mmbert32k | 561 (46.4%) | 419 (34.7%) | 409 (33.9%) | 408 (33.8%) |
| gliner2-hivetrace-uni-ru | 567 (46.9%) | 295 (24.4%) | 200 (16.6%) | 120 (9.9%) |
| ru-legal-ner | 617 (51.1%) | 462 (38.2%) | 434 (35.9%) | 427 (35.3%) |
| gliner-nvidia-ru | 620 (51.3%) | 464 (38.4%) | 345 (28.6%) | 225 (18.6%) |
| nym-base | 644 (53.3%) | 613 (50.7%) | 613 (50.7%) | 613 (50.7%) |
| gravitee-small | 646 (53.5%) | 558 (46.2%) | 556 (46.0%) | 556 (46.0%) |
| davlan-xlmr | 700 (57.9%) | 692 (57.3%) | 692 (57.3%) | 692 (57.3%) |
| gliner-pii-base | 722 (59.8%) | 144 (11.9%) | 34 (2.8%) | 4 (0.3%) |
| gliner2-vladlinv | 732 (60.6%) | 708 (58.6%) | 697 (57.7%) | 683 (56.5%) |
| gliner2-vladlinv-ru | 735 (60.8%) | 712 (58.9%) | 700 (57.9%) | 688 (57.0%) |
| davlan-mbert | 761 (63.0%) | 761 (63.0%) | 761 (63.0%) | 761 (63.0%) |
| fef2-secret-ru | 770 (63.7%) | 747 (61.8%) | 746 (61.8%) | 746 (61.8%) |
| ner-ru-gherman | 836 (69.2%) | 821 (68.0%) | 820 (67.9%) | 820 (67.9%) |
| bardsai-eu | 845 (70.0%) | 836 (69.2%) | 836 (69.2%) | 836 (69.2%) |
| nym-small | 847 (70.1%) | 816 (67.5%) | 816 (67.5%) | 816 (67.5%) |
| kalyan-ettin | 886 (73.3%) | 710 (58.8%) | 670 (55.5%) | 661 (54.7%) |
| traciora | 897 (74.3%) | 895 (74.1%) | 894 (74.0%) | 894 (74.0%) |
| openmed-nemotron | 901 (74.6%) | 826 (68.4%) | 822 (68.0%) | 822 (68.0%) |
| pii-shield-onnx | 932 (77.2%) | 865 (71.6%) | 859 (71.1%) | 858 (71.0%) |
| openmed-multilingual | 941 (77.9%) | 807 (66.8%) | 803 (66.5%) | 803 (66.5%) |
| opf-ru | 962 (79.6%) | 951 (78.7%) | 951 (78.7%) | 951 (78.7%) |
| apararti | 1101 (91.1%) | 1097 (90.8%) | 1097 (90.8%) | 1097 (90.8%) |
| openai-base | 1122 (92.9%) | 1120 (92.7%) | 1120 (92.7%) | 1120 (92.7%) |
| opf-ru-v2 | 1126 (93.2%) | 1126 (93.2%) | 1126 (93.2%) | 1126 (93.2%) |
| opf-kz-ru | 1159 (95.9%) | 1158 (95.9%) | 1158 (95.9%) | 1158 (95.9%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
