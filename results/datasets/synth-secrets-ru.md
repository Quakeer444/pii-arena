# synth-secrets-ru - ru / secrets (600 rows, 581 spans, 300 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.100 (90.0% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pplx | **0** | 0.0% [0.0%, 0.0%] | 97.6% | 0.328 [0.295, 0.365] | 0.197 | 0.983 | 0.133 | 0.213 | 0.269 | 285/300 | 54077 | 0 | 80 | 596M |  |
| opf-ru | **1** | 0.2% [0.0%, 0.6%] | 79.7% | 0.395 [0.356, 0.435] | 0.255 | 0.877 | 0.130 | 0.232 | 0.347 | 285/300 | 37681 | 0 | 44 | 1.4B |  |
| pii-shield-onnx | **2** | 0.3% [0.0%, 0.9%] | 97.4% | 0.241 [0.213, 0.271] | 0.137 | 0.995 | 0.070 | 0.177 | 0.238 | 292/300 | 85073 | 0 | 313 | - |  |
| opf-kz-ru | **4** | 0.7% [0.2%, 1.4%] | 94.1% | 0.314 [0.280, 0.354] | 0.187 | 0.981 | 0.073 | 0.156 | 0.253 | 278/300 | 59343 | 0 | 58 | 1.4B |  |
| apararti | **4** | 0.7% [0.0%, 1.7%] | 91.7% | 0.300 [0.267, 0.340] | 0.178 | 0.974 | 0.091 | 0.168 | 0.251 | 282/300 | 63103 | 0 | 60 | 1.4B |  |
| openai-base | **12** | 2.1% [0.9%, 3.6%] | 91.7% | 0.304 [0.268, 0.345] | 0.180 | 0.972 | 0.090 | 0.160 | 0.248 | 252/300 | 62394 | 0 | 68 | 1.4B |  |
| opf-ru-v2 | **15** | 2.6% [1.4%, 3.9%] | 80.9% | 0.381 [0.344, 0.420] | 0.241 | 0.910 | 0.133 | 0.234 | 0.350 | 277/300 | 40118 | 0 | 509 | 1.4B |  |
| traciora | **17** | 2.9% [1.6%, 4.3%] | 77.3% | 0.392 [0.356, 0.432] | 0.248 | 0.933 | 0.095 | 0.191 | 0.274 | 268/300 | 39261 | 0 | 261 | 1.4B |  |
| openmed-multilingual | **20** | 3.4% [2.1%, 5.1%] | 72.1% | 0.334 [0.299, 0.374] | 0.207 | 0.871 | 0.091 | 0.170 | 0.256 | 286/300 | 47615 | 0 | 37 | 1.4B |  |
| nym-base | **21** | 3.6% [2.2%, 5.3%] | 68.2% | 0.346 [0.312, 0.383] | 0.222 | 0.785 | 0.149 | 0.234 | 0.143 | 274/300 | 41531 | 0 | 8 | 308M |  |
| nym-small | **32** | 5.5% [3.6%, 7.5%] | 60.9% | 0.350 [0.315, 0.386] | 0.226 | 0.778 | 0.127 | 0.220 | 0.094 | 284/300 | 39428 | 0 | 197 | - |  |
| ru-legal-ner | **52** | 9.0% [6.5%, 11.6%] | 35.6% | 0.369 [0.335, 0.405] | 0.241 | 0.789 | 0.047 | 0.174 | 0.000 | 282/300 | 35118 | 0 | 7 | 29M |  |
| bardsai-eu | **55** | 9.5% [7.3%, 12.0%] | 70.2% | 0.400 [0.361, 0.439] | 0.264 | 0.821 | 0.226 | 0.337 | 0.000 | 266/300 | 34172 | 0 | 652 | - |  |
| gliner-pii-edge | **86** | 14.8% [11.9%, 17.9%] | 71.3% | 0.391 [0.353, 0.430] | 0.267 | 0.730 | 0.294 | 0.373 | 0.114 | 285/300 | 32286 | 0 | 70 | 45M |  |
| kalyan-ettin | **86** | 14.8% [11.7%, 17.9%] | 44.2% | 0.381 [0.346, 0.418] | 0.257 | 0.738 | 0.096 | 0.222 | 0.281 | 296/300 | 32592 | 0 | 28 | 68M |  |
| openmed-nemotron | **86** | 14.8% [12.0%, 18.0%] | 53.5% | 0.345 [0.310, 0.383] | 0.219 | 0.813 | 0.070 | 0.170 | 0.265 | 299/300 | 41446 | 0 | 38 | 1.4B |  |
| rules-ru | **105** | 18.1% [15.1%, 21.5%] | 81.4% | 0.518 [0.477, 0.559] | 0.360 | 0.922 | 0.264 | 0.286 | 0.517 | 246/300 | 20258 | 0 | 1 | - |  |
| mmbert32k | **136** | 23.4% [20.2%, 27.1%] | 22.0% | 0.256 [0.229, 0.284] | 0.165 | 0.567 | 0.018 | 0.079 | 0.000 | 300/300 | 41071 | 0 | 12 | 308M |  |
| fef2-secret-ru | **150** | 25.8% [22.4%, 29.8%] | 56.1% | 0.571 [0.528, 0.614] | 0.531 | 0.617 | 0.379 | 0.580 | 0.092 | 130/300 | 6320 | 0 | 7 | 177M |  |
| nuner-zero | **198** | 34.1% [29.7%, 38.1%] | 52.2% | 0.491 [0.449, 0.536] | 0.531 | 0.456 | 0.340 | 0.500 | 0.088 | 185/300 | 6224 | 0 | 16 | 449M |  |
| gliner2-fastino | **204** | 35.1% [30.8%, 39.6%] | 59.6% | 0.475 [0.430, 0.522] | 0.566 | 0.409 | 0.497 | 0.550 | 0.083 | 158/300 | 5383 | 0 | 8 | 307M |  |
| gliner-nvidia | **210** | 36.1% [31.8%, 40.1%] | 61.6% | 0.461 [0.419, 0.502] | 0.395 | 0.553 | 0.364 | 0.442 | 0.083 | 233/300 | 14528 | 0 | 16 | 445M |  |
| gliner25-fastino | **232** | 39.9% [35.4%, 44.2%] | 56.8% | 0.266 [0.233, 0.305] | 0.190 | 0.444 | 0.167 | 0.194 | 0.064 | 260/300 | 29524 | 0 | 4 | 287M |  |
| stanza-ru | **238** | 41.0% [37.0%, 45.2%] | 28.4% | 0.303 [0.270, 0.338] | 0.237 | 0.420 | 0.075 | 0.201 | 0.000 | 270/300 | 17951 | 0 | 58 | - |  |
| gliner25-fastino-ru | **265** | 45.6% [41.2%, 50.1%] | 52.0% | 0.335 [0.296, 0.375] | 0.277 | 0.422 | 0.200 | 0.223 | 0.151 | 227/300 | 17560 | 0 | 8 | 287M |  |
| gliner2-hivetrace-omni | **271** | 46.6% [42.6%, 51.1%] | 53.0% | 0.400 [0.357, 0.443] | 0.408 | 0.392 | 0.325 | 0.340 | 0.171 | 227/300 | 9215 | 0 | 11 | 307M |  |
| gliner2-fastino-ru | **284** | 48.9% [44.3%, 53.2%] | 46.5% | 0.394 [0.352, 0.442] | 0.609 | 0.291 | 0.430 | 0.492 | 0.125 | 146/300 | 3414 | 0 | 11 | 307M |  |
| gliner-stream-pii | **305** | 52.5% [48.3%, 56.9%] | 40.6% | 0.370 [0.327, 0.422] | 0.489 | 0.298 | 0.247 | 0.298 | 0.039 | 229/300 | 5158 | 0 | 7 | 677M |  |
| gliner-nvidia-ru | **331** | 57.0% [52.2%, 61.2%] | 42.3% | 0.424 [0.373, 0.477] | 0.611 | 0.325 | 0.405 | 0.464 | 0.163 | 138/300 | 4254 | 0 | 42 | 445M |  |
| gravitee-small | **334** | 57.5% [52.7%, 62.3%] | 23.4% | 0.187 [0.159, 0.213] | 0.170 | 0.207 | 0.083 | 0.169 | 0.159 | 299/300 | 13289 | 0 | 6 | 29M |  |
| gliner2-hivetrace-omni-ru | **338** | 58.2% [54.0%, 62.2%] | 41.7% | 0.290 [0.251, 0.328] | 0.299 | 0.281 | 0.210 | 0.223 | 0.154 | 250/300 | 9835 | 0 | 9 | 307M |  |
| gliner2-vladlinv-ru | **376** | 64.7% [59.9%, 69.4%] | 33.2% | 0.203 [0.166, 0.240] | 0.223 | 0.186 | 0.253 | 0.273 | 0.124 | 125/300 | 10241 | 0 | 7 | 287M |  |
| gliner-urchade | **378** | 65.1% [60.5%, 69.3%] | 32.0% | 0.307 [0.262, 0.357] | 0.628 | 0.203 | 0.341 | 0.404 | 0.088 | 105/300 | 1969 | 0 | 8 | 289M |  |
| gliner2-vladlinv | **403** | 69.4% [65.0%, 73.7%] | 28.1% | 0.211 [0.173, 0.254] | 0.353 | 0.150 | 0.297 | 0.328 | 0.118 | 87/300 | 4146 | 0 | 4 | 287M |  |
| gliner2-large | **426** | 73.3% [69.7%, 77.4%] | 23.8% | 0.216 [0.175, 0.258] | 0.374 | 0.152 | 0.189 | 0.234 | 0.196 | 220/300 | 4169 | 0 | 20 | 486M |  |
| gliner-pii-base | **445** | 76.6% [73.1%, 80.3%] | 21.5% | 0.213 [0.171, 0.260] | 0.512 | 0.135 | 0.288 | 0.316 | 0.119 | 93/300 | 2317 | 0 | 4 | 166M |  |
| gliner-multi-v21-ru | **453** | 78.0% [74.4%, 81.6%] | 16.2% | 0.123 [0.097, 0.151] | 0.354 | 0.074 | 0.148 | 0.254 | 0.118 | 108/300 | 1812 | 0 | 14 | 289M |  |
| gliner-urchade-ru | **457** | 78.7% [75.1%, 82.4%] | 20.5% | 0.193 [0.148, 0.235] | 0.610 | 0.114 | 0.253 | 0.291 | 0.127 | 67/300 | 1097 | 0 | 10 | 289M |  |
| gliner-multi-v21 | **465** | 80.0% [76.7%, 83.4%] | 14.5% | 0.103 [0.082, 0.126] | 0.317 | 0.061 | 0.153 | 0.232 | 0.057 | 117/300 | 1899 | 0 | 4 | 289M |  |
| ru-pii-ner | **477** | 82.1% [79.0%, 85.0%] | 12.9% | 0.136 [0.107, 0.164] | 0.225 | 0.098 | 0.116 | 0.189 | 0.000 | 181/300 | 6106 | 0 | 91 | 358M |  |
| gliner2-hivetrace-uni-ru | **491** | 84.5% [81.5%, 87.6%] | 11.7% | 0.136 [0.103, 0.168] | 0.336 | 0.085 | 0.153 | 0.203 | 0.029 | 134/300 | 3695 | 0 | 8 | 147M |  |
| ner-ru-yqelz | **527** | 90.7% [88.4%, 92.9%] | 5.2% | 0.076 [0.053, 0.100] | 0.070 | 0.082 | 0.023 | 0.041 | 0.000 | 279/300 | 16828 | 0 | 9 | 559M |  |
| gliner2-hivetrace-uni | **575** | 99.0% [98.1%, 99.7%] | 1.0% | 0.010 [0.002, 0.022] | 0.361 | 0.005 | 0.020 | 0.020 | 0.000 | 17/300 | 258 | 0 | 8 | 147M |  |
| spacy-ru-lg | **577** | 99.3% [98.6%, 99.8%] | 0.7% | 0.008 [0.001, 0.020] | 0.086 | 0.004 | 0.012 | 0.012 | 0.000 | 32/300 | 329 | 0 | 4 | - |  |
| natasha | **580** | 99.8% [99.5%, 100.0%] | 0.2% | 0.002 [0.000, 0.006] | 0.018 | 0.001 | 0.003 | 0.003 | 0.000 | 75/300 | 764 | 0 | 4 | - |  |
| davlan-mbert | **581** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 10/300 | 59 | 0 | 7 | 177M |  |
| davlan-xlmr | **581** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/300 | 0 | 0 | 6 | 277M |  |
| ner-ru-gherman | **581** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/300 | 0 | 0 | 7 | 177M |  |
| spacy-alrosait | **581** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/300 | 0 | 0 | 4 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: pplx ≈ opf-ru; opf-ru ≈ pii-shield-onnx; pii-shield-onnx ≈ opf-kz-ru; opf-kz-ru ≈ apararti; openai-base ≈ opf-ru-v2; opf-ru-v2 ≈ traciora; traciora ≈ openmed-multilingual; openmed-multilingual ≈ nym-base; ru-legal-ner ≈ bardsai-eu; gliner-pii-edge ≈ kalyan-ettin; kalyan-ettin ≈ openmed-nemotron; openmed-nemotron ≈ rules-ru; mmbert32k ≈ fef2-secret-ru; nuner-zero ≈ gliner2-fastino; gliner2-fastino ≈ gliner-nvidia; gliner-nvidia ≈ gliner25-fastino; gliner25-fastino ≈ stanza-ru; stanza-ru ≈ gliner25-fastino-ru; gliner25-fastino-ru ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ gliner2-fastino-ru; gliner2-fastino-ru ≈ gliner-stream-pii; gliner-stream-pii ≈ gliner-nvidia-ru; gliner-nvidia-ru ≈ gravitee-small; gravitee-small ≈ gliner2-hivetrace-omni-ru; gliner2-vladlinv-ru ≈ gliner-urchade; gliner-urchade ≈ gliner2-vladlinv; gliner2-vladlinv ≈ gliner2-large; gliner2-large ≈ gliner-pii-base; gliner-pii-base ≈ gliner-multi-v21-ru; gliner-multi-v21-ru ≈ gliner-urchade-ru; gliner-urchade-ru ≈ gliner-multi-v21; gliner-multi-v21 ≈ ru-pii-ner; ru-pii-ner ≈ gliner2-hivetrace-uni-ru; gliner2-hivetrace-uni ≈ spacy-ru-lg; spacy-ru-lg ≈ natasha; natasha ≈ davlan-mbert; davlan-mbert ≈ davlan-xlmr; davlan-xlmr ≈ ner-ru-gherman; ner-ru-gherman ≈ spacy-alrosait

## Missed by group

| model | SECRET |
|---|---|
| spans in gold | 581 |
| pplx | 0 (0.0%) |
| opf-ru | 1 (0.2%) |
| pii-shield-onnx | 2 (0.3%) |
| opf-kz-ru | 4 (0.7%) |
| apararti | 4 (0.7%) |
| openai-base | 12 (2.1%) |
| opf-ru-v2 | 15 (2.6%) |
| traciora | 17 (2.9%) |
| openmed-multilingual | 20 (3.4%) |
| nym-base | 21 (3.6%) |
| nym-small | 32 (5.5%) |
| ru-legal-ner | 52 (9.0%) |
| bardsai-eu | 55 (9.5%) |
| gliner-pii-edge | 86 (14.8%) |
| kalyan-ettin | 86 (14.8%) |
| openmed-nemotron | 86 (14.8%) |
| rules-ru | 105 (18.1%) |
| mmbert32k | 136 (23.4%) |
| fef2-secret-ru | 150 (25.8%) |
| nuner-zero | 198 (34.1%) |
| gliner2-fastino | 204 (35.1%) |
| gliner-nvidia | 210 (36.1%) |
| gliner25-fastino | 232 (39.9%) |
| stanza-ru | 238 (41.0%) |
| gliner25-fastino-ru | 265 (45.6%) |
| gliner2-hivetrace-omni | 271 (46.6%) |
| gliner2-fastino-ru | 284 (48.9%) |
| gliner-stream-pii | 305 (52.5%) |
| gliner-nvidia-ru | 331 (57.0%) |
| gravitee-small | 334 (57.5%) |
| gliner2-hivetrace-omni-ru | 338 (58.2%) |
| gliner2-vladlinv-ru | 376 (64.7%) |
| gliner-urchade | 378 (65.1%) |
| gliner2-vladlinv | 403 (69.4%) |
| gliner2-large | 426 (73.3%) |
| gliner-pii-base | 445 (76.6%) |
| gliner-multi-v21-ru | 453 (78.0%) |
| gliner-urchade-ru | 457 (78.7%) |
| gliner-multi-v21 | 465 (80.0%) |
| ru-pii-ner | 477 (82.1%) |
| gliner2-hivetrace-uni-ru | 491 (84.5%) |
| ner-ru-yqelz | 527 (90.7%) |
| gliner2-hivetrace-uni | 575 (99.0%) |
| spacy-ru-lg | 577 (99.3%) |
| natasha | 580 (99.8%) |
| davlan-mbert | 581 (100.0%) |
| davlan-xlmr | 581 (100.0%) |
| ner-ru-gherman | 581 (100.0%) |
| spacy-alrosait | 581 (100.0%) |

## Char recall by gold type

| type | group | pplx | opf-ru | pii-shield-onnx | opf-kz-ru | apararti | openai-base | opf-ru-v2 | traciora | openmed-multilingual | nym-base | nym-small | ru-legal-ner | bardsai-eu | gliner-pii-edge | kalyan-ettin | openmed-nemotron | rules-ru | mmbert32k | fef2-secret-ru | nuner-zero | gliner2-fastino | gliner-nvidia | gliner25-fastino | stanza-ru | gliner25-fastino-ru | gliner2-hivetrace-omni | gliner2-fastino-ru | gliner-stream-pii | gliner-nvidia-ru | gravitee-small | gliner2-hivetrace-omni-ru | gliner2-vladlinv-ru | gliner-urchade | gliner2-vladlinv | gliner2-large | gliner-pii-base | gliner-multi-v21-ru | gliner-urchade-ru | gliner-multi-v21 | ru-pii-ner | gliner2-hivetrace-uni-ru | ner-ru-yqelz | gliner2-hivetrace-uni | spacy-ru-lg | natasha | davlan-mbert | davlan-xlmr | ner-ru-gherman | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| password | SECRET | 1.000 | 0.978 | 0.979 | 0.987 | 0.978 | 0.968 | 0.911 | 0.902 | 0.953 | 0.865 | 0.827 | 0.633 | 0.660 | 0.830 | 0.647 | 0.616 | 0.551 | 0.553 | 0.758 | 0.756 | 0.888 | 0.702 | 0.701 | 0.353 | 0.551 | 0.620 | 0.848 | 0.480 | 0.510 | 0.580 | 0.582 | 0.608 | 0.610 | 0.561 | 0.444 | 0.388 | 0.480 | 0.488 | 0.450 | 0.251 | 0.221 | 0.017 | 0.019 | 0.013 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| secret | SECRET | 0.982 | 0.870 | 0.996 | 0.981 | 0.974 | 0.972 | 0.910 | 0.935 | 0.865 | 0.780 | 0.774 | 0.800 | 0.832 | 0.723 | 0.744 | 0.826 | 0.947 | 0.568 | 0.608 | 0.436 | 0.377 | 0.543 | 0.427 | 0.425 | 0.413 | 0.377 | 0.254 | 0.286 | 0.313 | 0.182 | 0.261 | 0.158 | 0.176 | 0.123 | 0.132 | 0.118 | 0.047 | 0.089 | 0.035 | 0.087 | 0.076 | 0.087 | 0.004 | 0.004 | 0.001 | 0.000 | 0.000 | 0.000 | 0.000 |

## char F1 by domain

| domain | n | pplx | opf-ru | pii-shield-onnx | opf-kz-ru | apararti | openai-base | opf-ru-v2 | traciora | openmed-multilingual | nym-base | nym-small | ru-legal-ner | bardsai-eu | gliner-pii-edge | kalyan-ettin | openmed-nemotron | rules-ru | mmbert32k | fef2-secret-ru | nuner-zero | gliner2-fastino | gliner-nvidia | gliner25-fastino | stanza-ru | gliner25-fastino-ru | gliner2-hivetrace-omni | gliner2-fastino-ru | gliner-stream-pii | gliner-nvidia-ru | gravitee-small | gliner2-hivetrace-omni-ru | gliner2-vladlinv-ru | gliner-urchade | gliner2-vladlinv | gliner2-large | gliner-pii-base | gliner-multi-v21-ru | gliner-urchade-ru | gliner-multi-v21 | ru-pii-ner | gliner2-hivetrace-uni-ru | ner-ru-yqelz | gliner2-hivetrace-uni | spacy-ru-lg | natasha | davlan-mbert | davlan-xlmr | ner-ru-gherman | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| chat | 120 | 0.642 | 0.613 | 0.533 | 0.628 | 0.630 | 0.669 | 0.625 | 0.623 | 0.601 | 0.598 | 0.575 | 0.580 | 0.586 | 0.581 | 0.469 | 0.492 | 0.844 | 0.433 | 0.719 | 0.699 | 0.613 | 0.706 | 0.589 | 0.367 | 0.608 | 0.578 | 0.552 | 0.511 | 0.666 | 0.227 | 0.471 | 0.530 | 0.519 | 0.479 | 0.330 | 0.156 | 0.164 | 0.343 | 0.122 | 0.179 | 0.224 | 0.106 | 0.000 | 0.040 | 0.010 | 0.000 | 0.000 | 0.000 | 0.000 |
| comment | 120 | 0.449 | 0.471 | 0.411 | 0.430 | 0.440 | 0.459 | 0.499 | 0.453 | 0.500 | 0.426 | 0.383 | 0.428 | 0.459 | 0.447 | 0.440 | 0.486 | 0.652 | 0.308 | 0.618 | 0.407 | 0.426 | 0.592 | 0.524 | 0.346 | 0.515 | 0.423 | 0.342 | 0.431 | 0.454 | 0.105 | 0.237 | 0.152 | 0.250 | 0.103 | 0.290 | 0.159 | 0.058 | 0.126 | 0.057 | 0.117 | 0.123 | 0.147 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| env | 120 | 0.357 | 0.349 | 0.230 | 0.392 | 0.407 | 0.493 | 0.381 | 0.372 | 0.356 | 0.299 | 0.329 | 0.382 | 0.346 | 0.337 | 0.404 | 0.297 | 0.659 | 0.331 | 0.379 | 0.304 | 0.271 | 0.172 | 0.337 | 0.175 | 0.282 | 0.241 | 0.186 | 0.297 | 0.027 | 0.258 | 0.205 | 0.227 | 0.172 | 0.245 | 0.038 | 0.203 | 0.089 | 0.150 | 0.069 | 0.127 | 0.103 | 0.084 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| log | 120 | 0.139 | 0.208 | 0.091 | 0.118 | 0.108 | 0.101 | 0.168 | 0.192 | 0.142 | 0.183 | 0.186 | 0.197 | 0.234 | 0.246 | 0.227 | 0.181 | 0.231 | 0.109 | 0.739 | 0.565 | 0.618 | 0.300 | 0.112 | 0.404 | 0.181 | 0.351 | 0.512 | 0.182 | 0.197 | 0.189 | 0.248 | 0.050 | 0.124 | 0.058 | 0.059 | 0.342 | 0.079 | 0.073 | 0.071 | 0.078 | 0.045 | 0.014 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| wiki | 120 | 0.515 | 0.561 | 0.493 | 0.584 | 0.547 | 0.590 | 0.595 | 0.581 | 0.588 | 0.485 | 0.480 | 0.489 | 0.537 | 0.480 | 0.478 | 0.540 | 0.687 | 0.346 | 0.608 | 0.524 | 0.460 | 0.561 | 0.302 | 0.369 | 0.338 | 0.438 | 0.388 | 0.416 | 0.504 | 0.108 | 0.342 | 0.290 | 0.386 | 0.228 | 0.311 | 0.198 | 0.197 | 0.236 | 0.174 | 0.174 | 0.153 | 0.105 | 0.040 | 0.003 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| opf-ru | 1 (0.2%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| pii-shield-onnx | 2 (0.3%) | 2 (0.3%) | 2 (0.3%) | 2 (0.3%) |
| opf-kz-ru | 4 (0.7%) | 4 (0.7%) | 4 (0.7%) | 4 (0.7%) |
| apararti | 4 (0.7%) | 4 (0.7%) | 4 (0.7%) | 4 (0.7%) |
| openai-base | 12 (2.1%) | 12 (2.1%) | 12 (2.1%) | 12 (2.1%) |
| opf-ru-v2 | 15 (2.6%) | 14 (2.4%) | 14 (2.4%) | 14 (2.4%) |
| traciora | 17 (2.9%) | 15 (2.6%) | 13 (2.2%) | 13 (2.2%) |
| openmed-multilingual | 20 (3.4%) | 13 (2.2%) | 13 (2.2%) | 13 (2.2%) |
| nym-base | 21 (3.6%) | 18 (3.1%) | 18 (3.1%) | 18 (3.1%) |
| nym-small | 32 (5.5%) | 27 (4.6%) | 27 (4.6%) | 27 (4.6%) |
| ru-legal-ner | 52 (9.0%) | 11 (1.9%) | 11 (1.9%) | 11 (1.9%) |
| bardsai-eu | 55 (9.5%) | 15 (2.6%) | 4 (0.7%) | 4 (0.7%) |
| gliner-pii-edge | 86 (14.8%) | 2 (0.3%) | 0 (0.0%) | 0 (0.0%) |
| kalyan-ettin | 86 (14.8%) | 40 (6.9%) | 35 (6.0%) | 35 (6.0%) |
| openmed-nemotron | 86 (14.8%) | 48 (8.3%) | 47 (8.1%) | 47 (8.1%) |
| mmbert32k | 136 (23.4%) | 1 (0.2%) | 1 (0.2%) | 0 (0.0%) |
| fef2-secret-ru | 150 (25.8%) | 146 (25.1%) | 146 (25.1%) | 146 (25.1%) |
| nuner-zero | 198 (34.1%) | 77 (13.3%) | 50 (8.6%) | 32 (5.5%) |
| gliner2-fastino | 204 (35.1%) | 111 (19.1%) | 79 (13.6%) | 46 (7.9%) |
| gliner-nvidia | 210 (36.1%) | 182 (31.3%) | 172 (29.6%) | 149 (25.6%) |
| gliner25-fastino | 232 (39.9%) | 135 (23.2%) | 92 (15.8%) | 60 (10.3%) |
| gliner25-fastino-ru | 265 (45.6%) | 141 (24.3%) | 95 (16.4%) | 44 (7.6%) |
| gliner2-hivetrace-omni | 271 (46.6%) | 150 (25.8%) | 93 (16.0%) | 50 (8.6%) |
| gliner2-fastino-ru | 284 (48.9%) | 134 (23.1%) | 84 (14.5%) | 48 (8.3%) |
| gliner-stream-pii | 305 (52.5%) | 255 (43.9%) | 209 (36.0%) | 150 (25.8%) |
| gliner-nvidia-ru | 331 (57.0%) | 289 (49.7%) | 268 (46.1%) | 235 (40.4%) |
| gravitee-small | 334 (57.5%) | 329 (56.6%) | 329 (56.6%) | 329 (56.6%) |
| gliner2-hivetrace-omni-ru | 338 (58.2%) | 156 (26.9%) | 108 (18.6%) | 53 (9.1%) |
| gliner2-vladlinv-ru | 376 (64.7%) | 345 (59.4%) | 322 (55.4%) | 292 (50.3%) |
| gliner-urchade | 378 (65.1%) | 260 (44.8%) | 185 (31.8%) | 104 (17.9%) |
| gliner2-vladlinv | 403 (69.4%) | 366 (63.0%) | 352 (60.6%) | 336 (57.8%) |
| gliner2-large | 426 (73.3%) | 377 (64.9%) | 349 (60.1%) | 302 (52.0%) |
| gliner-pii-base | 445 (76.6%) | 58 (10.0%) | 9 (1.5%) | 0 (0.0%) |
| gliner-multi-v21-ru | 453 (78.0%) | 301 (51.8%) | 196 (33.7%) | 103 (17.7%) |
| gliner-urchade-ru | 457 (78.7%) | 303 (52.2%) | 217 (37.3%) | 153 (26.3%) |
| gliner-multi-v21 | 465 (80.0%) | 270 (46.5%) | 162 (27.9%) | 69 (11.9%) |
| gliner2-hivetrace-uni-ru | 491 (84.5%) | 348 (59.9%) | 256 (44.1%) | 129 (22.2%) |
| ner-ru-yqelz | 527 (90.7%) | 523 (90.0%) | 523 (90.0%) | 523 (90.0%) |
| gliner2-hivetrace-uni | 575 (99.0%) | 504 (86.7%) | 371 (63.9%) | 172 (29.6%) |
| davlan-mbert | 581 (100.0%) | 581 (100.0%) | 581 (100.0%) | 581 (100.0%) |
| ner-ru-gherman | 581 (100.0%) | 581 (100.0%) | 581 (100.0%) | 581 (100.0%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
