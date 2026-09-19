# synth-secrets-en - en / secrets (600 rows, 581 spans, 300 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.101 (89.9% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pplx | **1** | 0.2% [0.0%, 0.5%] | 97.4% | 0.330 [0.297, 0.367] | 0.198 | 0.981 | 0.135 | 0.215 | 0.268 | 275/300 | 53318 | 0 | 75 | 596M |  |
| pii-shield-onnx | **2** | 0.3% [0.0%, 0.9%] | 97.8% | 0.241 [0.214, 0.272] | 0.137 | 0.995 | 0.068 | 0.173 | 0.239 | 289/300 | 85054 | 0 | 295 | - |  |
| openmed-multilingual | **5** | 0.9% [0.2%, 1.7%] | 82.4% | 0.335 [0.300, 0.374] | 0.205 | 0.917 | 0.096 | 0.160 | 0.264 | 300/300 | 50927 | 0 | 24 | 1.4B |  |
| opf-ru | **10** | 1.7% [0.7%, 3.1%] | 77.5% | 0.404 [0.365, 0.446] | 0.264 | 0.859 | 0.136 | 0.244 | 0.354 | 273/300 | 35382 | 0 | 45 | 1.4B |  |
| opf-kz-ru | **10** | 1.7% [0.6%, 3.1%] | 91.4% | 0.319 [0.284, 0.361] | 0.191 | 0.974 | 0.070 | 0.157 | 0.248 | 274/300 | 57799 | 0 | 62 | 1.4B |  |
| apararti | **17** | 2.9% [1.6%, 4.6%] | 88.0% | 0.304 [0.269, 0.345] | 0.181 | 0.958 | 0.092 | 0.167 | 0.246 | 274/300 | 61360 | 0 | 62 | 1.4B |  |
| opf-ru-v2 | **23** | 4.0% [2.3%, 5.6%] | 78.7% | 0.378 [0.340, 0.418] | 0.241 | 0.881 | 0.134 | 0.234 | 0.349 | 274/300 | 39111 | 0 | 535 | 1.4B |  |
| traciora | **32** | 5.5% [3.4%, 7.8%] | 70.6% | 0.396 [0.359, 0.436] | 0.254 | 0.896 | 0.095 | 0.196 | 0.274 | 265/300 | 37195 | 0 | 272 | 1.4B |  |
| nym-base | **35** | 6.0% [4.1%, 8.1%] | 62.5% | 0.354 [0.318, 0.393] | 0.230 | 0.768 | 0.148 | 0.243 | 0.162 | 267/300 | 38844 | 0 | 7 | 308M |  |
| nym-small | **39** | 6.7% [4.6%, 8.9%] | 57.3% | 0.352 [0.317, 0.388] | 0.230 | 0.750 | 0.136 | 0.242 | 0.118 | 274/300 | 37462 | 0 | 191 | - |  |
| bardsai-eu | **41** | 7.1% [5.3%, 9.1%] | 73.5% | 0.398 [0.360, 0.437] | 0.263 | 0.819 | 0.234 | 0.347 | 0.000 | 259/300 | 33980 | 0 | 673 | - |  |
| openai-base | **41** | 7.1% [4.7%, 9.6%] | 84.5% | 0.300 [0.264, 0.343] | 0.179 | 0.923 | 0.083 | 0.157 | 0.244 | 240/300 | 60039 | 0 | 70 | 1.4B |  |
| ru-legal-ner | **63** | 10.8% [8.4%, 13.4%] | 33.6% | 0.368 [0.333, 0.404] | 0.244 | 0.750 | 0.047 | 0.176 | 0.000 | 279/300 | 33030 | 0 | 7 | 29M |  |
| openmed-nemotron | **75** | 12.9% [10.4%, 15.6%] | 57.1% | 0.353 [0.319, 0.392] | 0.224 | 0.827 | 0.081 | 0.176 | 0.270 | 299/300 | 41047 | 0 | 37 | 1.4B |  |
| kalyan-ettin | **84** | 14.5% [11.4%, 17.6%] | 48.0% | 0.379 [0.342, 0.414] | 0.258 | 0.714 | 0.102 | 0.227 | 0.294 | 294/300 | 31184 | 0 | 25 | 68M |  |
| gliner-pii-edge | **95** | 16.4% [13.3%, 19.6%] | 70.6% | 0.400 [0.359, 0.440] | 0.279 | 0.710 | 0.317 | 0.392 | 0.121 | 268/300 | 29567 | 0 | 63 | 45M |  |
| rules-ru | **103** | 17.7% [14.8%, 21.2%] | 81.8% | 0.519 [0.478, 0.561] | 0.361 | 0.925 | 0.265 | 0.287 | 0.518 | 246/300 | 20258 | 0 | 1 | - |  |
| mmbert32k | **126** | 21.7% [18.3%, 25.2%] | 20.8% | 0.255 [0.227, 0.283] | 0.166 | 0.556 | 0.018 | 0.081 | 0.000 | 300/300 | 40065 | 0 | 11 | 308M |  |
| fef2-secret-ru | **168** | 28.9% [25.0%, 32.7%] | 53.2% | 0.574 [0.533, 0.621] | 0.552 | 0.599 | 0.394 | 0.599 | 0.088 | 88/300 | 5343 | 0 | 8 | 177M |  |
| gravitee-small | **169** | 29.1% [25.0%, 33.2%] | 46.3% | 0.356 [0.323, 0.389] | 0.297 | 0.442 | 0.183 | 0.311 | 0.340 | 257/300 | 13479 | 0 | 5 | 29M |  |
| gliner2-fastino | **206** | 35.5% [31.2%, 39.6%] | 58.0% | 0.466 [0.424, 0.508] | 0.555 | 0.402 | 0.482 | 0.542 | 0.084 | 159/300 | 5573 | 0 | 8 | 307M |  |
| nuner-zero | **207** | 35.6% [31.2%, 39.8%] | 53.2% | 0.483 [0.439, 0.528] | 0.553 | 0.430 | 0.364 | 0.524 | 0.079 | 139/300 | 4862 | 0 | 15 | 449M |  |
| gliner-nvidia | **207** | 35.6% [31.7%, 39.5%] | 62.0% | 0.473 [0.430, 0.515] | 0.413 | 0.554 | 0.386 | 0.468 | 0.098 | 211/300 | 13626 | 0 | 14 | 445M |  |
| gliner25-fastino | **251** | 43.2% [38.7%, 47.9%] | 54.0% | 0.261 [0.223, 0.299] | 0.191 | 0.412 | 0.172 | 0.193 | 0.073 | 240/300 | 27811 | 0 | 6 | 287M |  |
| gliner2-hivetrace-omni | **264** | 45.4% [41.0%, 49.5%] | 54.2% | 0.422 [0.380, 0.468] | 0.447 | 0.400 | 0.352 | 0.364 | 0.158 | 216/300 | 7895 | 0 | 10 | 307M |  |
| gliner-stream-pii | **299** | 51.5% [47.3%, 55.4%] | 41.3% | 0.390 [0.345, 0.440] | 0.504 | 0.318 | 0.239 | 0.295 | 0.041 | 237/300 | 5019 | 0 | 7 | 677M |  |
| stanza-ru | **319** | 54.9% [50.8%, 59.0%] | 20.7% | 0.227 [0.198, 0.259] | 0.177 | 0.315 | 0.041 | 0.140 | 0.000 | 271/300 | 19057 | 0 | 58 | - |  |
| gliner-pii-base | **380** | 65.4% [61.5%, 69.4%] | 31.2% | 0.319 [0.274, 0.367] | 0.576 | 0.221 | 0.372 | 0.418 | 0.166 | 121/300 | 3188 | 0 | 5 | 166M |  |
| gliner-urchade | **403** | 69.4% [65.4%, 73.2%] | 27.9% | 0.258 [0.215, 0.305] | 0.624 | 0.162 | 0.319 | 0.370 | 0.068 | 104/300 | 1594 | 0 | 8 | 289M |  |
| gliner2-vladlinv | **424** | 73.0% [68.8%, 77.1%] | 25.1% | 0.189 [0.151, 0.228] | 0.334 | 0.132 | 0.279 | 0.301 | 0.112 | 84/300 | 3980 | 0 | 8 | 287M |  |
| gliner-multi-v21 | **435** | 74.9% [71.3%, 78.7%] | 18.2% | 0.131 [0.107, 0.156] | 0.350 | 0.081 | 0.179 | 0.268 | 0.070 | 138/300 | 2365 | 0 | 7 | 289M |  |
| gliner2-large | **468** | 80.6% [77.2%, 84.0%] | 17.7% | 0.141 [0.107, 0.177] | 0.340 | 0.089 | 0.162 | 0.195 | 0.117 | 176/300 | 2549 | 0 | 20 | 486M |  |
| ru-pii-ner | **496** | 85.4% [82.3%, 88.3%] | 10.7% | 0.111 [0.084, 0.138] | 0.198 | 0.077 | 0.095 | 0.162 | 0.000 | 174/300 | 5603 | 0 | 94 | 358M |  |
| ner-ru-yqelz | **515** | 88.6% [86.3%, 90.9%] | 5.7% | 0.080 [0.058, 0.103] | 0.073 | 0.087 | 0.025 | 0.051 | 0.000 | 274/300 | 17072 | 0 | 9 | 559M |  |
| gliner2-hivetrace-uni | **576** | 99.1% [98.3%, 99.8%] | 0.9% | 0.006 [0.001, 0.013] | 0.444 | 0.003 | 0.017 | 0.017 | 0.000 | 10/300 | 105 | 0 | 7 | 147M |  |
| davlan-mbert | **581** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2/300 | 13 | 0 | 7 | 177M |  |
| davlan-xlmr | **581** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/300 | 0 | 0 | 6 | 277M |  |
| natasha | **581** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 32/300 | 425 | 0 | 4 | - |  |
| ner-ru-gherman | **581** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1/300 | 18 | 0 | 7 | 177M |  |
| spacy-alrosait | **581** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/300 | 0 | 0 | 4 | - |  |
| spacy-ru-lg | **581** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 29/300 | 945 | 0 | 5 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: pplx ≈ pii-shield-onnx; pii-shield-onnx ≈ openmed-multilingual; openmed-multilingual ≈ opf-ru; opf-ru ≈ opf-kz-ru; apararti ≈ opf-ru-v2; opf-ru-v2 ≈ traciora; traciora ≈ nym-base; nym-base ≈ nym-small; nym-small ≈ bardsai-eu; bardsai-eu ≈ openai-base; ru-legal-ner ≈ openmed-nemotron; openmed-nemotron ≈ kalyan-ettin; kalyan-ettin ≈ gliner-pii-edge; gliner-pii-edge ≈ rules-ru; rules-ru ≈ mmbert32k; fef2-secret-ru ≈ gravitee-small; gliner2-fastino ≈ nuner-zero; nuner-zero ≈ gliner-nvidia; gliner25-fastino ≈ gliner2-hivetrace-omni; gliner-stream-pii ≈ stanza-ru; gliner-pii-base ≈ gliner-urchade; gliner-urchade ≈ gliner2-vladlinv; gliner2-vladlinv ≈ gliner-multi-v21; ru-pii-ner ≈ ner-ru-yqelz; davlan-mbert ≈ davlan-xlmr; davlan-xlmr ≈ natasha; natasha ≈ ner-ru-gherman; ner-ru-gherman ≈ spacy-alrosait; spacy-alrosait ≈ spacy-ru-lg

## Missed by group

| model | SECRET |
|---|---|
| spans in gold | 581 |
| pplx | 1 (0.2%) |
| pii-shield-onnx | 2 (0.3%) |
| openmed-multilingual | 5 (0.9%) |
| opf-ru | 10 (1.7%) |
| opf-kz-ru | 10 (1.7%) |
| apararti | 17 (2.9%) |
| opf-ru-v2 | 23 (4.0%) |
| traciora | 32 (5.5%) |
| nym-base | 35 (6.0%) |
| nym-small | 39 (6.7%) |
| bardsai-eu | 41 (7.1%) |
| openai-base | 41 (7.1%) |
| ru-legal-ner | 63 (10.8%) |
| openmed-nemotron | 75 (12.9%) |
| kalyan-ettin | 84 (14.5%) |
| gliner-pii-edge | 95 (16.4%) |
| rules-ru | 103 (17.7%) |
| mmbert32k | 126 (21.7%) |
| fef2-secret-ru | 168 (28.9%) |
| gravitee-small | 169 (29.1%) |
| gliner2-fastino | 206 (35.5%) |
| nuner-zero | 207 (35.6%) |
| gliner-nvidia | 207 (35.6%) |
| gliner25-fastino | 251 (43.2%) |
| gliner2-hivetrace-omni | 264 (45.4%) |
| gliner-stream-pii | 299 (51.5%) |
| stanza-ru | 319 (54.9%) |
| gliner-pii-base | 380 (65.4%) |
| gliner-urchade | 403 (69.4%) |
| gliner2-vladlinv | 424 (73.0%) |
| gliner-multi-v21 | 435 (74.9%) |
| gliner2-large | 468 (80.6%) |
| ru-pii-ner | 496 (85.4%) |
| ner-ru-yqelz | 515 (88.6%) |
| gliner2-hivetrace-uni | 576 (99.1%) |
| davlan-mbert | 581 (100.0%) |
| davlan-xlmr | 581 (100.0%) |
| natasha | 581 (100.0%) |
| ner-ru-gherman | 581 (100.0%) |
| spacy-alrosait | 581 (100.0%) |
| spacy-ru-lg | 581 (100.0%) |

## Char recall by gold type

| type | group | pplx | pii-shield-onnx | openmed-multilingual | opf-ru | opf-kz-ru | apararti | opf-ru-v2 | traciora | nym-base | nym-small | bardsai-eu | openai-base | ru-legal-ner | openmed-nemotron | kalyan-ettin | gliner-pii-edge | rules-ru | mmbert32k | fef2-secret-ru | gravitee-small | gliner2-fastino | nuner-zero | gliner-nvidia | gliner25-fastino | gliner2-hivetrace-omni | gliner-stream-pii | stanza-ru | gliner-pii-base | gliner-urchade | gliner2-vladlinv | gliner-multi-v21 | gliner2-large | ru-pii-ner | ner-ru-yqelz | gliner2-hivetrace-uni | davlan-mbert | davlan-xlmr | natasha | ner-ru-gherman | spacy-alrosait | spacy-ru-lg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| password | SECRET | 1.000 | 0.978 | 0.961 | 0.970 | 0.969 | 0.943 | 0.907 | 0.860 | 0.784 | 0.783 | 0.750 | 0.929 | 0.592 | 0.619 | 0.724 | 0.834 | 0.551 | 0.491 | 0.742 | 0.737 | 0.897 | 0.792 | 0.703 | 0.698 | 0.621 | 0.492 | 0.285 | 0.487 | 0.617 | 0.522 | 0.560 | 0.452 | 0.191 | 0.036 | 0.019 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| secret | SECRET | 0.980 | 0.997 | 0.914 | 0.852 | 0.975 | 0.959 | 0.879 | 0.898 | 0.767 | 0.748 | 0.823 | 0.923 | 0.761 | 0.841 | 0.714 | 0.702 | 0.950 | 0.560 | 0.589 | 0.423 | 0.369 | 0.405 | 0.544 | 0.393 | 0.386 | 0.306 | 0.317 | 0.203 | 0.132 | 0.105 | 0.049 | 0.065 | 0.069 | 0.091 | 0.002 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## char F1 by domain

| domain | n | pplx | pii-shield-onnx | openmed-multilingual | opf-ru | opf-kz-ru | apararti | opf-ru-v2 | traciora | nym-base | nym-small | bardsai-eu | openai-base | ru-legal-ner | openmed-nemotron | kalyan-ettin | gliner-pii-edge | rules-ru | mmbert32k | fef2-secret-ru | gravitee-small | gliner2-fastino | nuner-zero | gliner-nvidia | gliner25-fastino | gliner2-hivetrace-omni | gliner-stream-pii | stanza-ru | gliner-pii-base | gliner-urchade | gliner2-vladlinv | gliner-multi-v21 | gliner2-large | ru-pii-ner | ner-ru-yqelz | gliner2-hivetrace-uni | davlan-mbert | davlan-xlmr | natasha | ner-ru-gherman | spacy-alrosait | spacy-ru-lg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| chat | 120 | 0.646 | 0.537 | 0.559 | 0.639 | 0.661 | 0.657 | 0.643 | 0.650 | 0.584 | 0.573 | 0.584 | 0.691 | 0.553 | 0.527 | 0.457 | 0.598 | 0.848 | 0.438 | 0.734 | 0.538 | 0.515 | 0.600 | 0.689 | 0.591 | 0.634 | 0.546 | 0.371 | 0.373 | 0.413 | 0.443 | 0.196 | 0.328 | 0.163 | 0.114 | 0.004 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| comment | 120 | 0.468 | 0.413 | 0.487 | 0.498 | 0.466 | 0.466 | 0.503 | 0.493 | 0.455 | 0.368 | 0.463 | 0.468 | 0.446 | 0.489 | 0.448 | 0.486 | 0.652 | 0.310 | 0.660 | 0.469 | 0.456 | 0.468 | 0.615 | 0.489 | 0.477 | 0.435 | 0.126 | 0.380 | 0.162 | 0.075 | 0.113 | 0.149 | 0.098 | 0.140 | 0.015 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| env | 120 | 0.359 | 0.233 | 0.352 | 0.345 | 0.393 | 0.407 | 0.380 | 0.372 | 0.312 | 0.331 | 0.335 | 0.497 | 0.376 | 0.297 | 0.414 | 0.353 | 0.659 | 0.321 | 0.376 | 0.282 | 0.285 | 0.303 | 0.204 | 0.337 | 0.256 | 0.301 | 0.171 | 0.224 | 0.160 | 0.191 | 0.085 | 0.029 | 0.115 | 0.086 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| log | 120 | 0.139 | 0.091 | 0.142 | 0.210 | 0.117 | 0.108 | 0.169 | 0.192 | 0.183 | 0.186 | 0.234 | 0.101 | 0.197 | 0.181 | 0.229 | 0.247 | 0.231 | 0.109 | 0.742 | 0.198 | 0.618 | 0.593 | 0.301 | 0.113 | 0.351 | 0.185 | 0.404 | 0.335 | 0.131 | 0.063 | 0.073 | 0.073 | 0.062 | 0.016 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| wiki | 120 | 0.518 | 0.485 | 0.574 | 0.614 | 0.612 | 0.592 | 0.590 | 0.592 | 0.523 | 0.522 | 0.538 | 0.620 | 0.524 | 0.567 | 0.469 | 0.477 | 0.687 | 0.357 | 0.590 | 0.438 | 0.471 | 0.509 | 0.602 | 0.338 | 0.442 | 0.456 | 0.192 | 0.301 | 0.361 | 0.227 | 0.179 | 0.138 | 0.113 | 0.120 | 0.011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| pii-shield-onnx | 2 (0.3%) | 2 (0.3%) | 2 (0.3%) | 2 (0.3%) |
| openmed-multilingual | 5 (0.9%) | 3 (0.5%) | 3 (0.5%) | 3 (0.5%) |
| opf-ru | 10 (1.7%) | 6 (1.0%) | 6 (1.0%) | 6 (1.0%) |
| opf-kz-ru | 10 (1.7%) | 10 (1.7%) | 10 (1.7%) | 10 (1.7%) |
| apararti | 17 (2.9%) | 14 (2.4%) | 14 (2.4%) | 14 (2.4%) |
| opf-ru-v2 | 23 (4.0%) | 22 (3.8%) | 22 (3.8%) | 22 (3.8%) |
| traciora | 32 (5.5%) | 26 (4.5%) | 24 (4.1%) | 24 (4.1%) |
| nym-base | 35 (6.0%) | 32 (5.5%) | 32 (5.5%) | 32 (5.5%) |
| nym-small | 39 (6.7%) | 36 (6.2%) | 36 (6.2%) | 36 (6.2%) |
| bardsai-eu | 41 (7.1%) | 14 (2.4%) | 2 (0.3%) | 2 (0.3%) |
| openai-base | 41 (7.1%) | 40 (6.9%) | 40 (6.9%) | 40 (6.9%) |
| ru-legal-ner | 63 (10.8%) | 20 (3.4%) | 14 (2.4%) | 14 (2.4%) |
| openmed-nemotron | 75 (12.9%) | 45 (7.7%) | 44 (7.6%) | 44 (7.6%) |
| kalyan-ettin | 84 (14.5%) | 34 (5.9%) | 31 (5.3%) | 31 (5.3%) |
| gliner-pii-edge | 95 (16.4%) | 9 (1.5%) | 0 (0.0%) | 0 (0.0%) |
| mmbert32k | 126 (21.7%) | 1 (0.2%) | 1 (0.2%) | 0 (0.0%) |
| fef2-secret-ru | 168 (28.9%) | 166 (28.6%) | 166 (28.6%) | 166 (28.6%) |
| gravitee-small | 169 (29.1%) | 162 (27.9%) | 162 (27.9%) | 162 (27.9%) |
| gliner2-fastino | 206 (35.5%) | 118 (20.3%) | 88 (15.1%) | 48 (8.3%) |
| nuner-zero | 207 (35.6%) | 87 (15.0%) | 51 (8.8%) | 32 (5.5%) |
| gliner-nvidia | 207 (35.6%) | 189 (32.5%) | 171 (29.4%) | 148 (25.5%) |
| gliner25-fastino | 251 (43.2%) | 140 (24.1%) | 101 (17.4%) | 61 (10.5%) |
| gliner2-hivetrace-omni | 264 (45.4%) | 144 (24.8%) | 96 (16.5%) | 52 (9.0%) |
| gliner-stream-pii | 299 (51.5%) | 243 (41.8%) | 209 (36.0%) | 156 (26.9%) |
| gliner-pii-base | 380 (65.4%) | 49 (8.4%) | 10 (1.7%) | 0 (0.0%) |
| gliner-urchade | 403 (69.4%) | 281 (48.4%) | 201 (34.6%) | 111 (19.1%) |
| gliner2-vladlinv | 424 (73.0%) | 392 (67.5%) | 371 (63.9%) | 356 (61.3%) |
| gliner-multi-v21 | 435 (74.9%) | 257 (44.2%) | 160 (27.5%) | 62 (10.7%) |
| gliner2-large | 468 (80.6%) | 426 (73.3%) | 376 (64.7%) | 324 (55.8%) |
| ner-ru-yqelz | 515 (88.6%) | 506 (87.1%) | 506 (87.1%) | 506 (87.1%) |
| gliner2-hivetrace-uni | 576 (99.1%) | 492 (84.7%) | 391 (67.3%) | 183 (31.5%) |
| davlan-mbert | 581 (100.0%) | 581 (100.0%) | 581 (100.0%) | 581 (100.0%) |
| ner-ru-gherman | 581 (100.0%) | 581 (100.0%) | 581 (100.0%) | 581 (100.0%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
