# corrupt-secrets-issues - en / secrets (500 rows, 288 spans, 250 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.031 (96.9% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| opf-ru | **7** | 2.4% [0.7%, 4.6%] | 70.8% | 0.340 [0.210, 0.474] | 0.208 | 0.919 | 0.019 | 0.090 | 0.316 | 230/250 | 50933 | 0 | 170 | 1.4B |  |
| apararti | **8** | 2.8% [0.7%, 5.4%] | 72.9% | 0.335 [0.208, 0.463] | 0.204 | 0.933 | 0.042 | 0.137 | 0.306 | 205/250 | 46142 | 0 | 212 | 1.4B |  |
| nym-base+homoglyph | **11** | 3.8% [1.5%, 6.9%] | 63.2% | 0.357 [0.228, 0.487] | 0.221 | 0.923 | 0.035 | 0.085 | 0.082 | 203/250 | 37216 | 0 | 25 | 308M |  |
| nym-base | **11** | 3.8% [1.5%, 6.9%] | 63.2% | 0.356 [0.228, 0.486] | 0.221 | 0.922 | 0.035 | 0.085 | 0.082 | 208/250 | 37384 | 0 | 26 | 308M |  |
| pplx | **12** | 4.2% [1.7%, 7.3%] | 75.7% | 0.306 [0.187, 0.427] | 0.183 | 0.943 | 0.034 | 0.122 | 0.283 | 202/250 | 59676 | 0 | 294 | 596M |  |
| pplx+homoglyph | **12** | 4.2% [1.7%, 7.3%] | 75.7% | 0.304 [0.186, 0.426] | 0.182 | 0.943 | 0.034 | 0.121 | 0.281 | 202/250 | 60755 | 0 | 193 | 596M |  |
| opf-kz-ru | **13** | 4.5% [2.1%, 7.6%] | 73.3% | 0.319 [0.194, 0.445] | 0.193 | 0.917 | 0.025 | 0.122 | 0.281 | 211/250 | 48591 | 0 | 212 | 1.4B |  |
| traciora | **16** | 5.6% [2.9%, 8.6%] | 69.4% | 0.404 [0.261, 0.543] | 0.259 | 0.925 | 0.056 | 0.150 | 0.303 | 174/250 | 26886 | 0 | 186 | 1.4B |  |
| bardsai-eu | **16** | 5.6% [2.7%, 8.8%] | 70.8% | 0.360 [0.227, 0.491] | 0.223 | 0.930 | 0.058 | 0.145 | 0.000 | 193/250 | 33853 | 0 | 883 | - |  |
| opf-ru-v2 | **20** | 6.9% [3.9%, 10.7%] | 70.1% | 0.414 [0.263, 0.556] | 0.269 | 0.905 | 0.059 | 0.214 | 0.379 | 152/250 | 22019 | 0 | 902 | 1.4B |  |
| opf-ru-v2+homoglyph | **21** | 7.3% [4.1%, 11.0%] | 70.1% | 0.417 [0.264, 0.556] | 0.271 | 0.905 | 0.062 | 0.221 | 0.383 | 142/250 | 21077 | 0 | 23 | 1.4B |  |
| openmed-nemotron | **28** | 9.7% [6.1%, 13.9%] | 62.2% | 0.273 [0.163, 0.391] | 0.161 | 0.918 | 0.022 | 0.068 | 0.197 | 241/250 | 70229 | 0 | 124 | 1.4B |  |
| openai-base | **30** | 10.4% [6.3%, 15.4%] | 68.1% | 0.408 [0.258, 0.546] | 0.264 | 0.890 | 0.071 | 0.236 | 0.379 | 138/250 | 26022 | 0 | 225 | 1.4B |  |
| openmed-multilingual | **30** | 10.4% [6.0%, 15.4%] | 53.8% | 0.291 [0.172, 0.413] | 0.174 | 0.886 | 0.019 | 0.070 | 0.233 | 234/250 | 56678 | 0 | 114 | 1.4B |  |
| kalyan-ettin | **38** | 13.2% [9.1%, 17.4%] | 53.5% | 0.345 [0.208, 0.475] | 0.215 | 0.873 | 0.029 | 0.079 | 0.258 | 229/250 | 38362 | 0 | 56 | 68M |  |
| gliner-pii-edge | **39** | 13.5% [8.9%, 18.0%] | 52.8% | 0.332 [0.194, 0.464] | 0.206 | 0.854 | 0.032 | 0.072 | 0.332 | 249/250 | 53427 | 0 | 560 | 45M |  |
| mmbert32k | **48** | 16.7% [12.4%, 21.0%] | 35.1% | 0.305 [0.170, 0.434] | 0.188 | 0.808 | 0.013 | 0.033 | 0.000 | 238/250 | 52212 | 0 | 33 | 308M |  |
| ru-legal-ner | **65** | 22.6% [16.8%, 28.3%] | 41.7% | 0.137 [0.104, 0.186] | 0.084 | 0.384 | 0.017 | 0.038 | 0.000 | 241/250 | 69454 | 0 | 24 | 29M |  |
| ru-legal-ner+homoglyph | **66** | 22.9% [17.1%, 28.7%] | 41.3% | 0.144 [0.109, 0.196] | 0.089 | 0.383 | 0.019 | 0.041 | 0.000 | 235/250 | 59189 | 0 | 22 | 29M |  |
| nuner-zero | **85** | 29.5% [23.8%, 35.7%] | 41.0% | 0.442 [0.246, 0.604] | 0.359 | 0.573 | 0.031 | 0.154 | 0.442 | 177/250 | 13185 | 0 | 54 | 449M |  |
| gliner2-fastino | **102** | 35.4% [29.5%, 41.8%] | 35.8% | 0.332 [0.170, 0.480] | 0.223 | 0.650 | 0.025 | 0.074 | 0.332 | 219/250 | 34030 | 0 | 34 | 307M |  |
| rules-ru | **116** | 40.3% [33.6%, 47.1%] | 41.0% | 0.196 [0.114, 0.328] | 0.128 | 0.415 | 0.048 | 0.120 | 0.191 | 204/250 | 43447 | 0 | 2 | - |  |
| gliner-stream-pii | **127** | 44.1% [37.9%, 50.4%] | 27.8% | 0.453 [0.208, 0.624] | 0.383 | 0.554 | 0.056 | 0.133 | 0.453 | 217/250 | 14094 | 0 | 121 | 677M |  |
| gliner-urchade | **129** | 44.8% [38.4%, 51.5%] | 34.4% | 0.246 [0.171, 0.343] | 0.219 | 0.281 | 0.055 | 0.126 | 0.246 | 206/250 | 16900 | 0 | 28 | 289M |  |
| fef2-secret-ru | **141** | 49.0% [41.6%, 55.8%] | 33.3% | 0.546 [0.313, 0.730] | 0.509 | 0.590 | 0.103 | 0.334 | 0.013 | 69/250 | 2517 | 0 | 14 | 177M |  |
| gliner-nvidia | **151** | 52.4% [46.3%, 59.2%] | 29.9% | 0.418 [0.194, 0.580] | 0.302 | 0.674 | 0.046 | 0.132 | 0.418 | 199/250 | 19389 | 0 | 53 | 445M |  |
| gliner-nvidia+homoglyph | **151** | 52.4% [46.3%, 59.2%] | 29.9% | 0.417 [0.194, 0.581] | 0.302 | 0.674 | 0.046 | 0.131 | 0.417 | 198/250 | 19423 | 0 | 31 | 445M |  |
| stanza-ru | **152** | 52.8% [46.6%, 58.4%] | 20.8% | 0.144 [0.048, 0.249] | 0.081 | 0.643 | 0.001 | 0.017 | 0.000 | 248/250 | 122621 | 0 | 195 | - |  |
| gliner25-fastino | **166** | 57.6% [51.6%, 64.0%] | 23.3% | 0.129 [0.078, 0.203] | 0.092 | 0.217 | 0.012 | 0.039 | 0.129 | 226/250 | 33315 | 0 | 22 | 287M |  |
| ner-ru-yqelz | **191** | 66.3% [60.3%, 72.4%] | 19.8% | 0.102 [0.059, 0.171] | 0.070 | 0.190 | 0.013 | 0.023 | 0.000 | 244/250 | 44646 | 0 | 35 | 559M |  |
| gliner2-hivetrace-omni | **201** | 69.8% [64.0%, 75.6%] | 16.3% | 0.248 [0.092, 0.474] | 0.283 | 0.220 | 0.044 | 0.124 | 0.248 | 153/250 | 7700 | 0 | 31 | 307M |  |
| gliner2-large | **202** | 70.1% [64.5%, 76.2%] | 11.5% | 0.086 [0.056, 0.128] | 0.098 | 0.077 | 0.014 | 0.073 | 0.086 | 171/250 | 12025 | 0 | 68 | 486M |  |
| gravitee-small | **210** | 72.9% [67.5%, 78.0%] | 11.1% | 0.078 [0.054, 0.106] | 0.063 | 0.101 | 0.010 | 0.048 | 0.075 | 215/250 | 23248 | 0 | 13 | 29M |  |
| ru-pii-ner | **212** | 73.6% [68.0%, 78.6%] | 19.4% | 0.250 [0.090, 0.456] | 0.218 | 0.292 | 0.039 | 0.092 | 0.000 | 129/250 | 10301 | 0 | 312 | 358M |  |
| gliner-multi-v21 | **212** | 73.6% [67.4%, 79.5%] | 8.3% | 0.074 [0.048, 0.107] | 0.086 | 0.064 | 0.015 | 0.066 | 0.074 | 175/250 | 11083 | 0 | 25 | 289M |  |
| gliner2-hivetrace-uni | **245** | 85.1% [80.3%, 89.6%] | 5.2% | 0.055 [0.032, 0.096] | 0.183 | 0.032 | 0.031 | 0.123 | 0.055 | 97/250 | 2619 | 0 | 36 | 147M |  |
| gliner-pii-base | **249** | 86.5% [81.8%, 90.7%] | 7.6% | 0.155 [0.042, 0.317] | 0.337 | 0.101 | 0.031 | 0.093 | 0.155 | 104/250 | 3330 | 0 | 21 | 166M |  |
| gliner2-vladlinv+homoglyph | **260** | 90.3% [86.9%, 93.7%] | 4.2% | 0.047 [0.023, 0.082] | 0.217 | 0.026 | 0.043 | 0.121 | 0.047 | 11/250 | 249 | 0 | 16 | 287M |  |
| gliner2-vladlinv | **260** | 90.3% [86.9%, 93.7%] | 4.2% | 0.046 [0.023, 0.081] | 0.211 | 0.026 | 0.043 | 0.120 | 0.046 | 12/250 | 380 | 0 | 29 | 287M |  |
| spacy-ru-lg | **272** | 94.4% [91.2%, 97.3%] | 2.8% | 0.384 [0.017, 0.583] | 0.328 | 0.463 | 0.002 | 0.017 | 0.000 | 162/250 | 18789 | 0 | 28 | - |  |
| natasha | **281** | 97.6% [94.8%, 99.6%] | 0.0% | 0.180 [0.001, 0.464] | 0.303 | 0.128 | 0.000 | 0.012 | 0.000 | 106/250 | 4805 | 0 | 14 | - |  |
| davlan-mbert | **285** | 99.0% [97.7%, 100.0%] | 0.0% | 0.001 [0.000, 0.004] | 0.003 | 0.001 | 0.000 | 0.004 | 0.000 | 168/250 | 5451 | 0 | 25 | 177M |  |
| davlan-xlmr | **288** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 114/250 | 2652 | 0 | 23 | 277M |  |
| ner-ru-gherman+homoglyph | **288** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 40/250 | 684 | 0 | 25 | 177M |  |
| ner-ru-gherman | **288** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 38/250 | 565 | 0 | 26 | 177M |  |
| spacy-alrosait | **288** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12/250 | 132 | 0 | 27 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: opf-ru ≈ apararti; apararti ≈ nym-base+homoglyph; nym-base+homoglyph ≈ nym-base; nym-base ≈ pplx; pplx ≈ pplx+homoglyph; pplx+homoglyph ≈ opf-kz-ru; opf-kz-ru ≈ traciora; traciora ≈ bardsai-eu; bardsai-eu ≈ opf-ru-v2; opf-ru-v2 ≈ opf-ru-v2+homoglyph; opf-ru-v2+homoglyph ≈ openmed-nemotron; openmed-nemotron ≈ openai-base; openai-base ≈ openmed-multilingual; openmed-multilingual ≈ kalyan-ettin; kalyan-ettin ≈ gliner-pii-edge; gliner-pii-edge ≈ mmbert32k; mmbert32k ≈ ru-legal-ner; ru-legal-ner ≈ ru-legal-ner+homoglyph; ru-legal-ner+homoglyph ≈ nuner-zero; nuner-zero ≈ gliner2-fastino; gliner2-fastino ≈ rules-ru; rules-ru ≈ gliner-stream-pii; gliner-stream-pii ≈ gliner-urchade; gliner-urchade ≈ fef2-secret-ru; fef2-secret-ru ≈ gliner-nvidia; gliner-nvidia ≈ gliner-nvidia+homoglyph; gliner-nvidia+homoglyph ≈ stanza-ru; stanza-ru ≈ gliner25-fastino; gliner25-fastino ≈ ner-ru-yqelz; ner-ru-yqelz ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ gliner2-large; gliner2-large ≈ gravitee-small; gravitee-small ≈ ru-pii-ner; ru-pii-ner ≈ gliner-multi-v21; gliner2-hivetrace-uni ≈ gliner-pii-base; gliner-pii-base ≈ gliner2-vladlinv+homoglyph; gliner2-vladlinv+homoglyph ≈ gliner2-vladlinv; gliner2-vladlinv ≈ spacy-ru-lg; spacy-ru-lg ≈ natasha; natasha ≈ davlan-mbert; davlan-mbert ≈ davlan-xlmr; davlan-xlmr ≈ ner-ru-gherman+homoglyph; ner-ru-gherman+homoglyph ≈ ner-ru-gherman; ner-ru-gherman ≈ spacy-alrosait

## Missed by group

| model | SECRET |
|---|---|
| spans in gold | 288 |
| opf-ru | 7 (2.4%) |
| apararti | 8 (2.8%) |
| nym-base+homoglyph | 11 (3.8%) |
| nym-base | 11 (3.8%) |
| pplx | 12 (4.2%) |
| pplx+homoglyph | 12 (4.2%) |
| opf-kz-ru | 13 (4.5%) |
| traciora | 16 (5.6%) |
| bardsai-eu | 16 (5.6%) |
| opf-ru-v2 | 20 (6.9%) |
| opf-ru-v2+homoglyph | 21 (7.3%) |
| openmed-nemotron | 28 (9.7%) |
| openai-base | 30 (10.4%) |
| openmed-multilingual | 30 (10.4%) |
| kalyan-ettin | 38 (13.2%) |
| gliner-pii-edge | 39 (13.5%) |
| mmbert32k | 48 (16.7%) |
| ru-legal-ner | 65 (22.6%) |
| ru-legal-ner+homoglyph | 66 (22.9%) |
| nuner-zero | 85 (29.5%) |
| gliner2-fastino | 102 (35.4%) |
| rules-ru | 116 (40.3%) |
| gliner-stream-pii | 127 (44.1%) |
| gliner-urchade | 129 (44.8%) |
| fef2-secret-ru | 141 (49.0%) |
| gliner-nvidia | 151 (52.4%) |
| gliner-nvidia+homoglyph | 151 (52.4%) |
| stanza-ru | 152 (52.8%) |
| gliner25-fastino | 166 (57.6%) |
| ner-ru-yqelz | 191 (66.3%) |
| gliner2-hivetrace-omni | 201 (69.8%) |
| gliner2-large | 202 (70.1%) |
| gravitee-small | 210 (72.9%) |
| ru-pii-ner | 212 (73.6%) |
| gliner-multi-v21 | 212 (73.6%) |
| gliner2-hivetrace-uni | 245 (85.1%) |
| gliner-pii-base | 249 (86.5%) |
| gliner2-vladlinv+homoglyph | 260 (90.3%) |
| gliner2-vladlinv | 260 (90.3%) |
| spacy-ru-lg | 272 (94.4%) |
| natasha | 281 (97.6%) |
| davlan-mbert | 285 (99.0%) |
| davlan-xlmr | 288 (100.0%) |
| ner-ru-gherman+homoglyph | 288 (100.0%) |
| ner-ru-gherman | 288 (100.0%) |
| spacy-alrosait | 288 (100.0%) |

## Char recall by gold type

| type | group | opf-ru | apararti | nym-base+homoglyph | nym-base | pplx | pplx+homoglyph | opf-kz-ru | traciora | bardsai-eu | opf-ru-v2 | opf-ru-v2+homoglyph | openmed-nemotron | openai-base | openmed-multilingual | kalyan-ettin | gliner-pii-edge | mmbert32k | ru-legal-ner | ru-legal-ner+homoglyph | nuner-zero | gliner2-fastino | rules-ru | gliner-stream-pii | gliner-urchade | fef2-secret-ru | gliner-nvidia | gliner-nvidia+homoglyph | stanza-ru | gliner25-fastino | ner-ru-yqelz | gliner2-hivetrace-omni | gliner2-large | gravitee-small | ru-pii-ner | gliner-multi-v21 | gliner2-hivetrace-uni | gliner-pii-base | gliner2-vladlinv+homoglyph | gliner2-vladlinv | spacy-ru-lg | natasha | davlan-mbert | davlan-xlmr | ner-ru-gherman+homoglyph | ner-ru-gherman | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SECRET | SECRET | 0.919 | 0.933 | 0.923 | 0.922 | 0.943 | 0.943 | 0.917 | 0.925 | 0.930 | 0.905 | 0.905 | 0.918 | 0.890 | 0.886 | 0.873 | 0.854 | 0.808 | 0.384 | 0.383 | 0.573 | 0.650 | 0.415 | 0.554 | 0.281 | 0.590 | 0.674 | 0.674 | 0.643 | 0.217 | 0.190 | 0.220 | 0.077 | 0.101 | 0.292 | 0.064 | 0.032 | 0.101 | 0.026 | 0.026 | 0.463 | 0.128 | 0.001 | 0.000 | 0.000 | 0.000 | 0.000 |

## char F1 by domain

| domain | n | opf-ru | apararti | nym-base+homoglyph | nym-base | pplx | pplx+homoglyph | opf-kz-ru | traciora | bardsai-eu | opf-ru-v2 | opf-ru-v2+homoglyph | openmed-nemotron | openai-base | openmed-multilingual | kalyan-ettin | gliner-pii-edge | mmbert32k | ru-legal-ner | ru-legal-ner+homoglyph | nuner-zero | gliner2-fastino | rules-ru | gliner-stream-pii | gliner-urchade | fef2-secret-ru | gliner-nvidia | gliner-nvidia+homoglyph | stanza-ru | gliner25-fastino | ner-ru-yqelz | gliner2-hivetrace-omni | gliner2-large | gravitee-small | ru-pii-ner | gliner-multi-v21 | gliner2-hivetrace-uni | gliner-pii-base | gliner2-vladlinv+homoglyph | gliner2-vladlinv | spacy-ru-lg | natasha | davlan-mbert | davlan-xlmr | ner-ru-gherman+homoglyph | ner-ru-gherman | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| issue | 500 | 0.340 | 0.335 | 0.357 | 0.356 | 0.306 | 0.304 | 0.319 | 0.404 | 0.360 | 0.414 | 0.417 | 0.273 | 0.408 | 0.291 | 0.345 | 0.332 | 0.305 | 0.137 | 0.144 | 0.442 | 0.332 | 0.196 | 0.453 | 0.246 | 0.546 | 0.418 | 0.417 | 0.144 | 0.129 | 0.102 | 0.248 | 0.086 | 0.078 | 0.250 | 0.074 | 0.055 | 0.155 | 0.047 | 0.046 | 0.384 | 0.180 | 0.001 | 0.000 | 0.000 | 0.000 | 0.000 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| opf-ru | 7 (2.4%) | 7 (2.4%) | 7 (2.4%) | 7 (2.4%) |
| apararti | 8 (2.8%) | 8 (2.8%) | 8 (2.8%) | 8 (2.8%) |
| nym-base+homoglyph | 11 (3.8%) | 11 (3.8%) | 11 (3.8%) | 11 (3.8%) |
| nym-base | 11 (3.8%) | 11 (3.8%) | 11 (3.8%) | 11 (3.8%) |
| opf-kz-ru | 13 (4.5%) | 11 (3.8%) | 11 (3.8%) | 11 (3.8%) |
| traciora | 16 (5.6%) | 11 (3.8%) | 11 (3.8%) | 11 (3.8%) |
| bardsai-eu | 16 (5.6%) | 12 (4.2%) | 11 (3.8%) | 11 (3.8%) |
| opf-ru-v2 | 20 (6.9%) | 19 (6.6%) | 19 (6.6%) | 19 (6.6%) |
| opf-ru-v2+homoglyph | 21 (7.3%) | 19 (6.6%) | 19 (6.6%) | 19 (6.6%) |
| openmed-nemotron | 28 (9.7%) | 20 (6.9%) | 20 (6.9%) | 20 (6.9%) |
| openai-base | 30 (10.4%) | 30 (10.4%) | 30 (10.4%) | 30 (10.4%) |
| openmed-multilingual | 30 (10.4%) | 29 (10.1%) | 29 (10.1%) | 29 (10.1%) |
| kalyan-ettin | 38 (13.2%) | 24 (8.3%) | 24 (8.3%) | 24 (8.3%) |
| gliner-pii-edge | 39 (13.5%) | 1 (0.3%) | 0 (0.0%) | 0 (0.0%) |
| mmbert32k | 48 (16.7%) | 5 (1.7%) | 4 (1.4%) | 4 (1.4%) |
| ru-legal-ner | 65 (22.6%) | 43 (14.9%) | 41 (14.2%) | 41 (14.2%) |
| ru-legal-ner+homoglyph | 66 (22.9%) | 43 (14.9%) | 40 (13.9%) | 40 (13.9%) |
| nuner-zero | 85 (29.5%) | 46 (16.0%) | 38 (13.2%) | 26 (9.0%) |
| gliner2-fastino | 102 (35.4%) | 67 (23.3%) | 56 (19.4%) | 50 (17.4%) |
| gliner-stream-pii | 127 (44.1%) | 98 (34.0%) | 79 (27.4%) | 56 (19.4%) |
| gliner-urchade | 129 (44.8%) | 83 (28.8%) | 37 (12.8%) | 22 (7.6%) |
| fef2-secret-ru | 141 (49.0%) | 135 (46.9%) | 135 (46.9%) | 135 (46.9%) |
| gliner-nvidia | 151 (52.4%) | 118 (41.0%) | 98 (34.0%) | 78 (27.1%) |
| gliner-nvidia+homoglyph | 151 (52.4%) | 118 (41.0%) | 98 (34.0%) | 78 (27.1%) |
| gliner25-fastino | 166 (57.6%) | 117 (40.6%) | 89 (30.9%) | 71 (24.7%) |
| ner-ru-yqelz | 191 (66.3%) | 190 (66.0%) | 190 (66.0%) | 190 (66.0%) |
| gliner2-hivetrace-omni | 201 (69.8%) | 125 (43.4%) | 101 (35.1%) | 83 (28.8%) |
| gliner2-large | 202 (70.1%) | 179 (62.2%) | 165 (57.3%) | 145 (50.3%) |
| gravitee-small | 210 (72.9%) | 207 (71.9%) | 207 (71.9%) | 207 (71.9%) |
| gliner-multi-v21 | 212 (73.6%) | 98 (34.0%) | 59 (20.5%) | 34 (11.8%) |
| gliner2-hivetrace-uni | 245 (85.1%) | 165 (57.3%) | 116 (40.3%) | 83 (28.8%) |
| gliner-pii-base | 249 (86.5%) | 56 (19.4%) | 1 (0.3%) | 0 (0.0%) |
| gliner2-vladlinv+homoglyph | 260 (90.3%) | 256 (88.9%) | 251 (87.2%) | 249 (86.5%) |
| gliner2-vladlinv | 260 (90.3%) | 256 (88.9%) | 251 (87.2%) | 249 (86.5%) |
| davlan-mbert | 285 (99.0%) | 285 (99.0%) | 285 (99.0%) | 285 (99.0%) |
| davlan-xlmr | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) |
| ner-ru-gherman+homoglyph | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) |
| ner-ru-gherman | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
