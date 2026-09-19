# synth-env-configs - en / secrets (400 rows, 392 spans, 200 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.097 (90.3% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pplx | **0** | 0.0% [0.0%, 0.0%] | 98.2% | 0.418 [0.384, 0.449] | 0.265 | 0.996 | 0.204 | 0.290 | 0.262 | 193/200 | 25405 | 0 | 70 | 596M |  |
| pii-shield-onnx | **0** | 0.0% [0.0%, 0.0%] | 99.2% | 0.214 [0.193, 0.234] | 0.120 | 0.999 | 0.025 | 0.108 | 0.208 | 200/200 | 66629 | 0 | 318 | - |  |
| opf-kz-ru | **1** | 0.3% [0.0%, 0.9%] | 83.2% | 0.463 [0.427, 0.497] | 0.307 | 0.940 | 0.166 | 0.395 | 0.310 | 184/200 | 19843 | 0 | 25 | 1.4B |  |
| traciora | **2** | 0.5% [0.0%, 1.3%] | 67.1% | 0.466 [0.425, 0.501] | 0.315 | 0.893 | 0.171 | 0.365 | 0.280 | 181/200 | 18482 | 0 | 272 | 1.4B |  |
| opf-ru | **2** | 0.5% [0.0%, 1.3%] | 67.3% | 0.375 [0.338, 0.408] | 0.254 | 0.714 | 0.152 | 0.369 | 0.326 | 196/200 | 20060 | 0 | 46 | 1.4B |  |
| apararti | **3** | 0.8% [0.0%, 1.8%] | 78.3% | 0.472 [0.434, 0.507] | 0.320 | 0.900 | 0.243 | 0.438 | 0.348 | 182/200 | 18490 | 0 | 63 | 1.4B |  |
| openmed-multilingual | **4** | 1.0% [0.2%, 2.2%] | 64.3% | 0.391 [0.352, 0.426] | 0.265 | 0.743 | 0.159 | 0.350 | 0.296 | 197/200 | 19804 | 0 | 39 | 1.4B |  |
| opf-ru-v2 | **8** | 2.0% [0.8%, 3.5%] | 66.6% | 0.440 [0.401, 0.478] | 0.299 | 0.833 | 0.230 | 0.438 | 0.379 | 186/200 | 18049 | 0 | 456 | 1.4B |  |
| nym-small | **11** | 2.8% [1.3%, 4.4%] | 51.5% | 0.292 [0.260, 0.322] | 0.193 | 0.597 | 0.099 | 0.212 | 0.087 | 195/200 | 24490 | 0 | 169 | - |  |
| nym-base | **12** | 3.1% [1.4%, 5.1%] | 56.4% | 0.314 [0.280, 0.347] | 0.214 | 0.588 | 0.148 | 0.296 | 0.141 | 183/200 | 21531 | 0 | 7 | 308M |  |
| rules-ru | **16** | 4.1% [2.2%, 6.2%] | 95.7% | 0.650 [0.619, 0.679] | 0.486 | 0.981 | 0.390 | 0.391 | 0.650 | 192/200 | 10104 | 0 | 1 | - |  |
| openai-base | **19** | 4.8% [2.8%, 7.2%] | 77.3% | 0.549 [0.504, 0.587] | 0.401 | 0.873 | 0.348 | 0.607 | 0.424 | 123/200 | 12337 | 0 | 71 | 1.4B |  |
| kalyan-ettin | **30** | 7.7% [5.2%, 10.3%] | 46.7% | 0.435 [0.394, 0.473] | 0.323 | 0.666 | 0.182 | 0.437 | 0.306 | 169/200 | 13790 | 0 | 26 | 68M |  |
| openmed-nemotron | **34** | 8.7% [6.2%, 11.4%] | 54.1% | 0.354 [0.319, 0.387] | 0.239 | 0.680 | 0.100 | 0.321 | 0.249 | 197/200 | 19764 | 0 | 35 | 1.4B |  |
| fef2-secret-ru | **35** | 8.9% [6.5%, 11.7%] | 57.4% | 0.441 [0.400, 0.476] | 0.334 | 0.646 | 0.289 | 0.551 | 0.071 | 139/200 | 12239 | 0 | 9 | 177M |  |
| bardsai-eu | **40** | 10.2% [7.3%, 13.6%] | 56.9% | 0.348 [0.311, 0.381] | 0.238 | 0.650 | 0.258 | 0.438 | 0.000 | 173/200 | 20237 | 0 | 734 | - |  |
| mmbert32k | **51** | 13.0% [9.7%, 16.5%] | 25.3% | 0.337 [0.306, 0.366] | 0.230 | 0.627 | 0.044 | 0.190 | 0.000 | 192/200 | 20253 | 0 | 11 | 308M |  |
| ru-legal-ner | **54** | 13.8% [10.7%, 17.4%] | 28.6% | 0.359 [0.323, 0.392] | 0.250 | 0.640 | 0.052 | 0.240 | 0.000 | 181/200 | 18746 | 0 | 8 | 29M |  |
| gravitee-small | **91** | 23.2% [19.2%, 27.3%] | 40.6% | 0.333 [0.294, 0.369] | 0.286 | 0.398 | 0.200 | 0.464 | 0.278 | 178/200 | 9393 | 0 | 6 | 29M |  |
| gliner-pii-edge | **123** | 31.4% [27.4%, 35.6%] | 63.0% | 0.321 [0.281, 0.356] | 0.234 | 0.510 | 0.344 | 0.375 | 0.132 | 181/200 | 16897 | 0 | 68 | 45M |  |
| gliner2-hivetrace-omni | **180** | 45.9% [41.7%, 50.5%] | 54.1% | 0.347 [0.305, 0.384] | 0.355 | 0.340 | 0.291 | 0.291 | 0.083 | 184/200 | 6536 | 0 | 12 | 307M |  |
| gliner2-fastino | **181** | 46.2% [41.9%, 51.4%] | 48.7% | 0.287 [0.247, 0.326] | 0.261 | 0.320 | 0.181 | 0.209 | 0.057 | 196/200 | 9978 | 0 | 9 | 307M |  |
| gliner25-fastino | **195** | 49.7% [45.5%, 55.1%] | 49.5% | 0.271 [0.233, 0.306] | 0.233 | 0.323 | 0.177 | 0.180 | 0.064 | 191/200 | 10930 | 2 | 4 | 287M |  |
| stanza-ru | **201** | 51.3% [45.9%, 56.7%] | 18.6% | 0.150 [0.125, 0.178] | 0.106 | 0.258 | 0.008 | 0.124 | 0.000 | 187/200 | 19609 | 0 | 63 | - |  |
| gliner-stream-pii | **203** | 51.8% [47.1%, 56.4%] | 42.3% | 0.338 [0.294, 0.381] | 0.433 | 0.277 | 0.298 | 0.342 | 0.033 | 177/200 | 3436 | 0 | 7 | 677M |  |
| gliner-nvidia | **215** | 54.8% [50.4%, 59.4%] | 44.1% | 0.335 [0.289, 0.384] | 0.377 | 0.302 | 0.272 | 0.352 | 0.071 | 149/200 | 5733 | 0 | 9 | 445M |  |
| nuner-zero | **231** | 58.9% [53.8%, 64.1%] | 37.5% | 0.203 [0.167, 0.238] | 0.194 | 0.214 | 0.134 | 0.183 | 0.054 | 195/200 | 8136 | 0 | 8 | 449M |  |
| gliner2-vladlinv | **266** | 67.9% [63.5%, 73.1%] | 30.4% | 0.291 [0.238, 0.340] | 0.797 | 0.178 | 0.391 | 0.414 | 0.053 | 37/200 | 394 | 0 | 4 | 287M |  |
| gliner-urchade | **283** | 72.2% [68.0%, 76.3%] | 27.8% | 0.175 [0.138, 0.212] | 0.236 | 0.139 | 0.184 | 0.184 | 0.038 | 177/200 | 4657 | 0 | 6 | 289M |  |
| gliner-multi-v21 | **301** | 76.8% [72.6%, 80.8%] | 20.7% | 0.146 [0.113, 0.182] | 0.220 | 0.110 | 0.108 | 0.153 | 0.028 | 130/200 | 3866 | 0 | 5 | 289M |  |
| gliner-pii-base | **311** | 79.3% [75.3%, 83.4%] | 18.1% | 0.186 [0.139, 0.231] | 0.346 | 0.127 | 0.229 | 0.261 | 0.084 | 72/200 | 2835 | 0 | 5 | 166M |  |
| ner-ru-yqelz | **331** | 84.4% [81.0%, 87.7%] | 1.5% | 0.067 [0.050, 0.085] | 0.075 | 0.061 | 0.005 | 0.098 | 0.000 | 181/200 | 7426 | 0 | 10 | 559M |  |
| ru-pii-ner | **344** | 87.8% [84.1%, 91.0%] | 10.2% | 0.075 [0.051, 0.101] | 0.140 | 0.052 | 0.074 | 0.126 | 0.000 | 114/200 | 3751 | 0 | 110 | 358M |  |
| gliner2-large | **363** | 92.6% [89.8%, 95.1%] | 7.4% | 0.029 [0.017, 0.046] | 0.040 | 0.022 | 0.029 | 0.044 | 0.028 | 187/200 | 4809 | 0 | 21 | 486M |  |
| spacy-ru-lg | **387** | 98.7% [97.5%, 99.7%] | 1.3% | 0.019 [0.002, 0.040] | 0.242 | 0.010 | 0.023 | 0.023 | 0.000 | 20/200 | 356 | 0 | 6 | - |  |
| gliner2-hivetrace-uni | **390** | 99.5% [98.6%, 100.0%] | 0.5% | 0.005 [0.000, 0.016] | 0.259 | 0.003 | 0.010 | 0.010 | 0.000 | 6/200 | 121 | 0 | 5 | 147M |  |
| natasha | **391** | 99.7% [99.2%, 100.0%] | 0.0% | 0.002 [0.000, 0.008] | 0.010 | 0.001 | 0.000 | 0.003 | 0.000 | 102/200 | 1247 | 0 | 3 | - |  |
| ner-ru-gherman | **391** | 99.7% [99.2%, 100.0%] | 0.3% | 0.002 [0.000, 0.007] | 0.113 | 0.001 | 0.005 | 0.005 | 0.000 | 7/200 | 109 | 0 | 8 | 177M |  |
| davlan-mbert | **392** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 7/200 | 65 | 0 | 8 | 177M |  |
| davlan-xlmr | **392** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/200 | 0 | 0 | 7 | 277M |  |
| spacy-alrosait | **392** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/200 | 0 | 0 | 6 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: pplx ≈ pii-shield-onnx; pii-shield-onnx ≈ opf-kz-ru; opf-kz-ru ≈ traciora; traciora ≈ opf-ru; opf-ru ≈ apararti; apararti ≈ openmed-multilingual; openmed-multilingual ≈ opf-ru-v2; opf-ru-v2 ≈ nym-small; nym-small ≈ nym-base; nym-base ≈ rules-ru; rules-ru ≈ openai-base; openai-base ≈ kalyan-ettin; kalyan-ettin ≈ openmed-nemotron; openmed-nemotron ≈ fef2-secret-ru; fef2-secret-ru ≈ bardsai-eu; bardsai-eu ≈ mmbert32k; mmbert32k ≈ ru-legal-ner; gliner2-hivetrace-omni ≈ gliner2-fastino; gliner2-fastino ≈ gliner25-fastino; gliner25-fastino ≈ stanza-ru; stanza-ru ≈ gliner-stream-pii; gliner-stream-pii ≈ gliner-nvidia; gliner-nvidia ≈ nuner-zero; gliner2-vladlinv ≈ gliner-urchade; gliner-urchade ≈ gliner-multi-v21; gliner-multi-v21 ≈ gliner-pii-base; gliner-pii-base ≈ ner-ru-yqelz; ner-ru-yqelz ≈ ru-pii-ner; spacy-ru-lg ≈ gliner2-hivetrace-uni; gliner2-hivetrace-uni ≈ natasha; natasha ≈ ner-ru-gherman; ner-ru-gherman ≈ davlan-mbert; davlan-mbert ≈ davlan-xlmr; davlan-xlmr ≈ spacy-alrosait

## Missed by group

| model | SECRET |
|---|---|
| spans in gold | 392 |
| pplx | 0 (0.0%) |
| pii-shield-onnx | 0 (0.0%) |
| opf-kz-ru | 1 (0.3%) |
| traciora | 2 (0.5%) |
| opf-ru | 2 (0.5%) |
| apararti | 3 (0.8%) |
| openmed-multilingual | 4 (1.0%) |
| opf-ru-v2 | 8 (2.0%) |
| nym-small | 11 (2.8%) |
| nym-base | 12 (3.1%) |
| rules-ru | 16 (4.1%) |
| openai-base | 19 (4.8%) |
| kalyan-ettin | 30 (7.7%) |
| openmed-nemotron | 34 (8.7%) |
| fef2-secret-ru | 35 (8.9%) |
| bardsai-eu | 40 (10.2%) |
| mmbert32k | 51 (13.0%) |
| ru-legal-ner | 54 (13.8%) |
| gravitee-small | 91 (23.2%) |
| gliner-pii-edge | 123 (31.4%) |
| gliner2-hivetrace-omni | 180 (45.9%) |
| gliner2-fastino | 181 (46.2%) |
| gliner25-fastino | 195 (49.7%) |
| stanza-ru | 201 (51.3%) |
| gliner-stream-pii | 203 (51.8%) |
| gliner-nvidia | 215 (54.8%) |
| nuner-zero | 231 (58.9%) |
| gliner2-vladlinv | 266 (67.9%) |
| gliner-urchade | 283 (72.2%) |
| gliner-multi-v21 | 301 (76.8%) |
| gliner-pii-base | 311 (79.3%) |
| ner-ru-yqelz | 331 (84.4%) |
| ru-pii-ner | 344 (87.8%) |
| gliner2-large | 363 (92.6%) |
| spacy-ru-lg | 387 (98.7%) |
| gliner2-hivetrace-uni | 390 (99.5%) |
| natasha | 391 (99.7%) |
| ner-ru-gherman | 391 (99.7%) |
| davlan-mbert | 392 (100.0%) |
| davlan-xlmr | 392 (100.0%) |
| spacy-alrosait | 392 (100.0%) |

## Char recall by gold type

| type | group | pplx | pii-shield-onnx | opf-kz-ru | traciora | opf-ru | apararti | openmed-multilingual | opf-ru-v2 | nym-small | nym-base | rules-ru | openai-base | kalyan-ettin | openmed-nemotron | fef2-secret-ru | bardsai-eu | mmbert32k | ru-legal-ner | gravitee-small | gliner-pii-edge | gliner2-hivetrace-omni | gliner2-fastino | gliner25-fastino | stanza-ru | gliner-stream-pii | gliner-nvidia | nuner-zero | gliner2-vladlinv | gliner-urchade | gliner-multi-v21 | gliner-pii-base | ner-ru-yqelz | ru-pii-ner | gliner2-large | spacy-ru-lg | gliner2-hivetrace-uni | natasha | ner-ru-gherman | davlan-mbert | davlan-xlmr | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| password | SECRET | 1.000 | 0.994 | 1.000 | 0.978 | 1.000 | 1.000 | 1.000 | 0.954 | 0.936 | 0.967 | 0.839 | 0.966 | 0.936 | 0.882 | 0.954 | 0.592 | 0.587 | 0.385 | 0.994 | 0.941 | 1.000 | 1.000 | 0.954 | 0.059 | 0.744 | 0.984 | 1.000 | 0.432 | 0.967 | 0.598 | 0.470 | 0.000 | 0.265 | 0.402 | 0.016 | 0.016 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| secret | SECRET | 0.996 | 0.999 | 0.938 | 0.890 | 0.704 | 0.896 | 0.734 | 0.829 | 0.585 | 0.575 | 0.986 | 0.870 | 0.656 | 0.673 | 0.635 | 0.652 | 0.628 | 0.649 | 0.377 | 0.494 | 0.316 | 0.295 | 0.301 | 0.265 | 0.260 | 0.278 | 0.186 | 0.169 | 0.109 | 0.092 | 0.115 | 0.063 | 0.044 | 0.009 | 0.009 | 0.002 | 0.001 | 0.001 | 0.000 | 0.000 | 0.000 |

## char F1 by domain

| domain | n | pplx | pii-shield-onnx | opf-kz-ru | traciora | opf-ru | apararti | openmed-multilingual | opf-ru-v2 | nym-small | nym-base | rules-ru | openai-base | kalyan-ettin | openmed-nemotron | fef2-secret-ru | bardsai-eu | mmbert32k | ru-legal-ner | gravitee-small | gliner-pii-edge | gliner2-hivetrace-omni | gliner2-fastino | gliner25-fastino | stanza-ru | gliner-stream-pii | gliner-nvidia | nuner-zero | gliner2-vladlinv | gliner-urchade | gliner-multi-v21 | gliner-pii-base | ner-ru-yqelz | ru-pii-ner | gliner2-large | spacy-ru-lg | gliner2-hivetrace-uni | natasha | ner-ru-gherman | davlan-mbert | davlan-xlmr | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| compose | 80 | 0.403 | 0.184 | 0.420 | 0.466 | 0.378 | 0.446 | 0.397 | 0.436 | 0.291 | 0.336 | 0.563 | 0.559 | 0.450 | 0.362 | 0.427 | 0.334 | 0.308 | 0.369 | 0.358 | 0.313 | 0.386 | 0.330 | 0.340 | 0.177 | 0.330 | 0.292 | 0.217 | 0.296 | 0.222 | 0.218 | 0.165 | 0.047 | 0.082 | 0.049 | 0.000 | 0.019 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| env | 80 | 0.351 | 0.211 | 0.398 | 0.401 | 0.305 | 0.394 | 0.314 | 0.360 | 0.232 | 0.260 | 0.620 | 0.479 | 0.389 | 0.251 | 0.379 | 0.284 | 0.279 | 0.308 | 0.289 | 0.280 | 0.321 | 0.333 | 0.277 | 0.143 | 0.247 | 0.082 | 0.211 | 0.195 | 0.105 | 0.082 | 0.111 | 0.067 | 0.067 | 0.019 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| j2 | 80 | 0.647 | 0.240 | 0.638 | 0.650 | 0.510 | 0.675 | 0.527 | 0.651 | 0.449 | 0.476 | 0.823 | 0.775 | 0.582 | 0.387 | 0.580 | 0.503 | 0.537 | 0.531 | 0.404 | 0.446 | 0.369 | 0.182 | 0.179 | 0.185 | 0.416 | 0.326 | 0.146 | 0.429 | 0.146 | 0.054 | 0.125 | 0.130 | 0.127 | 0.018 | 0.000 | 0.006 | 0.012 | 0.010 | 0.000 | 0.000 | 0.000 |
| json | 80 | 0.402 | 0.231 | 0.466 | 0.451 | 0.361 | 0.455 | 0.408 | 0.420 | 0.287 | 0.281 | 0.665 | 0.498 | 0.417 | 0.417 | 0.435 | 0.349 | 0.304 | 0.335 | 0.335 | 0.304 | 0.347 | 0.320 | 0.255 | 0.122 | 0.358 | 0.388 | 0.217 | 0.347 | 0.166 | 0.164 | 0.218 | 0.074 | 0.051 | 0.026 | 0.027 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| yaml | 80 | 0.386 | 0.215 | 0.454 | 0.426 | 0.364 | 0.456 | 0.361 | 0.409 | 0.272 | 0.293 | 0.639 | 0.502 | 0.388 | 0.378 | 0.430 | 0.338 | 0.330 | 0.335 | 0.296 | 0.305 | 0.315 | 0.312 | 0.313 | 0.070 | 0.334 | 0.492 | 0.226 | 0.149 | 0.221 | 0.228 | 0.274 | 0.022 | 0.048 | 0.030 | 0.064 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| pii-shield-onnx | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| opf-kz-ru | 1 (0.3%) | 1 (0.3%) | 1 (0.3%) | 1 (0.3%) |
| traciora | 2 (0.5%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| opf-ru | 2 (0.5%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| apararti | 3 (0.8%) | 3 (0.8%) | 3 (0.8%) | 3 (0.8%) |
| openmed-multilingual | 4 (1.0%) | 1 (0.3%) | 1 (0.3%) | 1 (0.3%) |
| opf-ru-v2 | 8 (2.0%) | 6 (1.5%) | 6 (1.5%) | 6 (1.5%) |
| nym-small | 11 (2.8%) | 9 (2.3%) | 9 (2.3%) | 9 (2.3%) |
| nym-base | 12 (3.1%) | 9 (2.3%) | 9 (2.3%) | 9 (2.3%) |
| openai-base | 19 (4.8%) | 19 (4.8%) | 19 (4.8%) | 19 (4.8%) |
| kalyan-ettin | 30 (7.7%) | 11 (2.8%) | 11 (2.8%) | 11 (2.8%) |
| openmed-nemotron | 34 (8.7%) | 22 (5.6%) | 22 (5.6%) | 22 (5.6%) |
| fef2-secret-ru | 35 (8.9%) | 35 (8.9%) | 35 (8.9%) | 35 (8.9%) |
| bardsai-eu | 40 (10.2%) | 6 (1.5%) | 4 (1.0%) | 4 (1.0%) |
| mmbert32k | 51 (13.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| ru-legal-ner | 54 (13.8%) | 18 (4.6%) | 15 (3.8%) | 15 (3.8%) |
| gravitee-small | 91 (23.2%) | 86 (21.9%) | 86 (21.9%) | 86 (21.9%) |
| gliner-pii-edge | 123 (31.4%) | 21 (5.4%) | 1 (0.3%) | 0 (0.0%) |
| gliner2-hivetrace-omni | 180 (45.9%) | 140 (35.7%) | 122 (31.1%) | 102 (26.0%) |
| gliner2-fastino | 181 (46.2%) | 143 (36.5%) | 115 (29.3%) | 90 (23.0%) |
| gliner25-fastino | 195 (49.7%) | 153 (39.0%) | 133 (33.9%) | 102 (26.0%) |
| gliner-stream-pii | 203 (51.8%) | 168 (42.9%) | 140 (35.7%) | 98 (25.0%) |
| gliner-nvidia | 215 (54.8%) | 203 (51.8%) | 192 (49.0%) | 170 (43.4%) |
| nuner-zero | 231 (58.9%) | 168 (42.9%) | 137 (34.9%) | 106 (27.0%) |
| gliner2-vladlinv | 266 (67.9%) | 253 (64.5%) | 247 (63.0%) | 243 (62.0%) |
| gliner-urchade | 283 (72.2%) | 217 (55.4%) | 178 (45.4%) | 123 (31.4%) |
| gliner-multi-v21 | 301 (76.8%) | 132 (33.7%) | 62 (15.8%) | 25 (6.4%) |
| gliner-pii-base | 311 (79.3%) | 122 (31.1%) | 31 (7.9%) | 0 (0.0%) |
| ner-ru-yqelz | 331 (84.4%) | 327 (83.4%) | 327 (83.4%) | 327 (83.4%) |
| gliner2-large | 363 (92.6%) | 345 (88.0%) | 331 (84.4%) | 310 (79.1%) |
| gliner2-hivetrace-uni | 390 (99.5%) | 343 (87.5%) | 286 (73.0%) | 178 (45.4%) |
| ner-ru-gherman | 391 (99.7%) | 391 (99.7%) | 391 (99.7%) | 391 (99.7%) |
| davlan-mbert | 392 (100.0%) | 392 (100.0%) | 392 (100.0%) | 392 (100.0%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
