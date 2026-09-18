# secrets-issues - en / secrets (500 rows, 288 spans, 250 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.031 (96.9% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pplx+cpu-int8 | **0** | 0.0% [0.0%, 0.0%] | 81.2% | 0.208 [0.124, 0.307] | 0.117 | 0.969 | 0.007 | 0.054 | 0.203 | 233/250 | 109560 | 0 | 717 | 596M |  |
| pii-shield-onnx | **1** | 0.3% [0.0%, 1.1%] | 83.7% | 0.124 [0.071, 0.191] | 0.066 | 0.980 | 0.003 | 0.034 | 0.121 | 245/250 | 222713 | 0 | 3881 | - |  |
| nym-base+ov100 | **2** | 0.7% [0.0%, 1.8%] | 70.5% | 0.350 [0.223, 0.479] | 0.215 | 0.941 | 0.036 | 0.082 | 0.038 | 206/250 | 38709 | 0 | 25 | 308M |  |
| nym-base+sent300 | **3** | 1.0% [0.0%, 2.4%] | 71.5% | 0.327 [0.207, 0.453] | 0.198 | 0.943 | 0.030 | 0.069 | 0.117 | 216/250 | 46867 | 0 | 22 | 308M |  |
| nym-base | **4** | 1.4% [0.3%, 2.9%] | 69.4% | 0.350 [0.224, 0.480] | 0.215 | 0.938 | 0.034 | 0.082 | 0.030 | 208/250 | 39137 | 0 | 22 | 308M |  |
| opf-ru | **5** | 1.7% [0.3%, 3.9%] | 72.9% | 0.372 [0.237, 0.501] | 0.232 | 0.943 | 0.024 | 0.121 | 0.353 | 223/250 | 34083 | 0 | 357 | 1.4B |  |
| nym-base+cpu-int8 | **5** | 1.7% [0.3%, 3.8%] | 69.4% | 0.343 [0.218, 0.470] | 0.210 | 0.938 | 0.037 | 0.077 | 0.070 | 209/250 | 41883 | 0 | 348 | 308M |  |
| apararti | **6** | 2.1% [0.4%, 4.2%] | 74.7% | 0.344 [0.216, 0.470] | 0.211 | 0.944 | 0.048 | 0.161 | 0.320 | 185/250 | 38838 | 0 | 202 | 1.4B |  |
| nym-small | **6** | 2.1% [0.4%, 4.0%] | 67.0% | 0.331 [0.209, 0.461] | 0.201 | 0.938 | 0.046 | 0.077 | 0.127 | 211/250 | 44036 | 0 | 1850 | - |  |
| traciora | **9** | 3.1% [1.4%, 5.6%] | 71.9% | 0.416 [0.269, 0.556] | 0.267 | 0.940 | 0.068 | 0.186 | 0.323 | 148/250 | 21743 | 0 | 859 | 1.4B |  |
| opf-kz-ru | **9** | 3.1% [0.7%, 6.1%] | 76.4% | 0.327 [0.203, 0.453] | 0.198 | 0.936 | 0.034 | 0.145 | 0.287 | 185/250 | 42126 | 0 | 204 | 1.4B |  |
| pplx+sent300 | **9** | 3.1% [1.1%, 5.4%] | 73.6% | 0.289 [0.176, 0.406] | 0.171 | 0.941 | 0.025 | 0.106 | 0.247 | 203/250 | 62225 | 0 | 430 | 596M |  |
| opf-ru-v2+sent300 | **10** | 3.5% [1.4%, 6.0%] | 71.9% | 0.411 [0.267, 0.547] | 0.264 | 0.932 | 0.047 | 0.204 | 0.368 | 149/250 | 21992 | 0 | 31 | 1.4B |  |
| pplx+ov100 | **11** | 3.8% [1.7%, 6.3%] | 75.7% | 0.303 [0.187, 0.423] | 0.180 | 0.947 | 0.025 | 0.124 | 0.284 | 195/250 | 56902 | 0 | 310 | 596M |  |
| pplx | **12** | 4.2% [1.7%, 7.0%] | 75.0% | 0.288 [0.183, 0.409] | 0.173 | 0.878 | 0.034 | 0.128 | 0.266 | 191/250 | 57544 | 0 | 251 | 596M |  |
| bardsai-eu | **13** | 4.5% [1.9%, 7.8%] | 72.6% | 0.361 [0.230, 0.494] | 0.223 | 0.939 | 0.057 | 0.140 | 0.000 | 198/250 | 34779 | 0 | 1862 | - |  |
| opf-ru-v2 | **14** | 4.9% [2.2%, 8.3%] | 71.2% | 0.418 [0.268, 0.555] | 0.270 | 0.922 | 0.055 | 0.232 | 0.392 | 138/250 | 20573 | 0 | 1112 | 1.4B |  |
| opf-ru-v2+ov100 | **15** | 5.2% [2.7%, 8.2%] | 71.2% | 0.409 [0.263, 0.551] | 0.262 | 0.929 | 0.057 | 0.221 | 0.364 | 134/250 | 20789 | 0 | 25 | 1.4B |  |
| mmbert32k+cpu-int8 | **16** | 5.6% [2.6%, 8.9%] | 55.9% | 0.300 [0.182, 0.422] | 0.180 | 0.913 | 0.018 | 0.032 | 0.000 | 245/250 | 55672 | 0 | 320 | 308M |  |
| openmed-nemotron | **17** | 5.9% [3.2%, 8.9%] | 68.4% | 0.269 [0.164, 0.384] | 0.157 | 0.935 | 0.030 | 0.076 | 0.197 | 237/250 | 68471 | 0 | 310 | 1.4B |  |
| openmed-multilingual | **20** | 6.9% [3.8%, 10.4%] | 66.0% | 0.284 [0.170, 0.402] | 0.168 | 0.919 | 0.026 | 0.077 | 0.226 | 234/250 | 60068 | 0 | 310 | 1.4B |  |
| openai-base | **21** | 7.3% [3.9%, 11.6%] | 71.2% | 0.402 [0.256, 0.534] | 0.258 | 0.915 | 0.065 | 0.250 | 0.369 | 129/250 | 23834 | 0 | 554 | 1.4B |  |
| kalyan-ettin | **34** | 11.8% [8.3%, 15.7%] | 60.4% | 0.344 [0.212, 0.473] | 0.213 | 0.891 | 0.036 | 0.079 | 0.269 | 220/250 | 38351 | 0 | 45 | 68M |  |
| gliner-pii-edge | **37** | 12.8% [8.7%, 17.4%] | 64.9% | 0.352 [0.213, 0.480] | 0.220 | 0.877 | 0.040 | 0.078 | 0.352 | 248/250 | 46265 | 0 | 691 | 45M |  |
| ru-legal-ner+ov100 | **38** | 13.2% [9.0%, 18.0%] | 56.6% | 0.132 [0.110, 0.159] | 0.079 | 0.391 | 0.023 | 0.041 | 0.000 | 235/250 | 59579 | 0 | 25 | 29M |  |
| ru-legal-ner | **45** | 15.6% [10.9%, 20.9%] | 53.5% | 0.129 [0.108, 0.157] | 0.079 | 0.356 | 0.023 | 0.044 | 0.000 | 231/250 | 54009 | 0 | 22 | 29M |  |
| ru-legal-ner+cpu-int8 | **46** | 16.0% [11.3%, 21.4%] | 53.5% | 0.128 [0.106, 0.155] | 0.078 | 0.356 | 0.021 | 0.043 | 0.000 | 228/250 | 54965 | 0 | 34 | 29M |  |
| mmbert32k+nochunk | **47** | 16.3% [11.4%, 20.9%] | 46.5% | 0.337 [0.211, 0.465] | 0.214 | 0.794 | 0.025 | 0.047 | 0.000 | 239/250 | 42190 | 0 | 96 | 308M |  |
| ru-legal-ner+sent300 | **50** | 17.4% [12.4%, 22.8%] | 54.2% | 0.125 [0.104, 0.151] | 0.075 | 0.362 | 0.022 | 0.042 | 0.000 | 240/250 | 60833 | 0 | 23 | 29M |  |
| credsweeper-noml | **52** | 18.1% [12.5%, 24.7%] | 60.1% | 0.477 [0.300, 0.648] | 0.356 | 0.722 | 0.144 | 0.348 | 0.477 | 102/250 | 10572 | 0 | 37 | - |  |
| mmbert32k | **53** | 18.4% [13.4%, 23.0%] | 44.4% | 0.298 [0.161, 0.430] | 0.182 | 0.815 | 0.016 | 0.032 | 0.000 | 240/250 | 56920 | 0 | 32 | 308M |  |
| credsweeper | **76** | 26.4% [20.2%, 33.2%] | 55.9% | 0.490 [0.299, 0.661] | 0.379 | 0.693 | 0.184 | 0.411 | 0.490 | 59/250 | 7870 | 0 | 219 | - |  |
| nuner-zero | **85** | 29.5% [23.7%, 36.1%] | 49.3% | 0.308 [0.227, 0.399] | 0.264 | 0.369 | 0.038 | 0.158 | 0.308 | 171/250 | 14718 | 0 | 36 | 449M |  |
| rules-ru | **93** | 32.3% [25.7%, 39.3%] | 49.0% | 0.246 [0.129, 0.384] | 0.152 | 0.649 | 0.044 | 0.117 | 0.242 | 228/250 | 59328 | 0 | 2 | - |  |
| gliner2-fastino | **100** | 34.7% [29.1%, 40.8%] | 42.7% | 0.352 [0.192, 0.499] | 0.236 | 0.691 | 0.027 | 0.076 | 0.352 | 219/250 | 33191 | 0 | 24 | 307M |  |
| gliner-nvidia+ov100 | **101** | 35.1% [29.3%, 41.1%] | 45.8% | 0.463 [0.269, 0.611] | 0.330 | 0.779 | 0.066 | 0.176 | 0.463 | 203/250 | 19686 | 0 | 57 | 445M |  |
| gliner-urchade | **110** | 38.2% [32.4%, 44.4%] | 43.8% | 0.288 [0.206, 0.384] | 0.256 | 0.329 | 0.069 | 0.142 | 0.288 | 193/250 | 15823 | 0 | 23 | 289M |  |
| gliner-nvidia+sent300 | **114** | 39.6% [33.7%, 45.9%] | 42.4% | 0.401 [0.213, 0.556] | 0.273 | 0.752 | 0.050 | 0.127 | 0.401 | 215/250 | 25915 | 0 | 73 | 445M |  |
| gliner-stream-pii | **121** | 42.0% [35.7%, 48.5%] | 41.0% | 0.501 [0.244, 0.662] | 0.399 | 0.671 | 0.079 | 0.133 | 0.501 | 224/250 | 16134 | 0 | 33 | 677M |  |
| gliner-nvidia | **121** | 42.0% [35.6%, 48.5%] | 40.6% | 0.449 [0.238, 0.605] | 0.323 | 0.734 | 0.061 | 0.163 | 0.449 | 187/250 | 18606 | 0 | 38 | 445M |  |
| betterleaks | **123** | 42.7% [35.6%, 49.2%] | 44.8% | 0.541 [0.311, 0.696] | 0.432 | 0.726 | 0.269 | 0.529 | 0.541 | 32/250 | 5812 | 0 | 1 | - |  |
| gitleaks | **130** | 45.1% [37.9%, 51.4%] | 45.5% | 0.538 [0.313, 0.698] | 0.428 | 0.727 | 0.303 | 0.569 | 0.538 | 16/250 | 4720 | 0 | 1 | - |  |
| gliner25-fastino+ov100 | **132** | 45.8% [39.8%, 52.5%] | 36.5% | 0.128 [0.101, 0.159] | 0.091 | 0.215 | 0.023 | 0.050 | 0.128 | 228/250 | 32491 | 0 | 16 | 287M |  |
| fef2-secret-ru | **140** | 48.6% [42.1%, 55.6%] | 33.0% | 0.544 [0.304, 0.723] | 0.507 | 0.587 | 0.088 | 0.320 | 0.010 | 72/250 | 2582 | 0 | 24 | 177M |  |
| fef2-secret-ru+cpu-int8 | **145** | 50.3% [43.5%, 57.1%] | 30.9% | 0.563 [0.315, 0.743] | 0.550 | 0.576 | 0.096 | 0.348 | 0.008 | 52/250 | 1440 | 0 | 724 | 177M |  |
| gliner25-fastino+sent300 | **155** | 53.8% [47.9%, 60.1%] | 27.4% | 0.188 [0.086, 0.315] | 0.125 | 0.386 | 0.011 | 0.035 | 0.188 | 244/250 | 42553 | 0 | 17 | 287M |  |
| deepsecrets | **160** | 55.6% [49.1%, 61.9%] | 34.7% | 0.228 [0.158, 0.327] | 0.254 | 0.207 | 0.199 | 0.499 | 0.228 | 18/250 | 3955 | 0 | 96 | - |  |
| gliner25-fastino | **170** | 59.0% [52.8%, 65.3%] | 24.3% | 0.140 [0.085, 0.218] | 0.100 | 0.232 | 0.011 | 0.040 | 0.140 | 218/250 | 31445 | 0 | 17 | 287M |  |
| stanza-ru | **179** | 62.2% [56.1%, 67.6%] | 19.8% | 0.179 [0.060, 0.304] | 0.104 | 0.632 | 0.003 | 0.017 | 0.000 | 248/250 | 101263 | 0 | 188 | - |  |
| gliner2-hivetrace-omni | **187** | 64.9% [58.9%, 71.2%] | 20.8% | 0.284 [0.124, 0.506] | 0.317 | 0.257 | 0.056 | 0.145 | 0.284 | 137/250 | 7409 | 0 | 18 | 307M |  |
| ner-ru-yqelz | **189** | 65.6% [59.9%, 71.9%] | 25.3% | 0.107 [0.062, 0.176] | 0.073 | 0.204 | 0.017 | 0.023 | 0.000 | 248/250 | 50664 | 0 | 30 | 559M |  |
| gliner25-fastino+nochunk | **189** | 65.6% [59.4%, 71.7%] | 19.1% | 0.103 [0.072, 0.142] | 0.090 | 0.120 | 0.018 | 0.055 | 0.103 | 203/250 | 16264 | 0 | 114 | 287M |  |
| gliner2-large | **195** | 67.7% [61.9%, 73.5%] | 13.5% | 0.090 [0.063, 0.130] | 0.101 | 0.082 | 0.018 | 0.077 | 0.090 | 176/250 | 13433 | 0 | 58 | 486M |  |
| noseyparker | **201** | 69.8% [63.7%, 75.7%] | 23.3% | 0.421 [0.164, 0.634] | 0.371 | 0.488 | 0.017 | 0.369 | 0.421 | 17/250 | 4814 | 0 | 10 | - |  |
| titus | **202** | 70.1% [64.1%, 75.6%] | 24.3% | 0.420 [0.168, 0.630] | 0.367 | 0.493 | 0.021 | 0.366 | 0.420 | 22/250 | 5193 | 0 | 1 | - |  |
| gliner-multi-v21 | **203** | 70.5% [64.2%, 76.1%] | 11.8% | 0.095 [0.063, 0.137] | 0.107 | 0.085 | 0.023 | 0.072 | 0.095 | 175/250 | 12079 | 0 | 22 | 289M |  |
| detect-secrets | **213** | 74.0% [67.9%, 79.5%] | 24.3% | 0.371 [0.132, 0.574] | 0.306 | 0.472 | 0.000 | 0.253 | 0.371 | 42/250 | 10625 | 0 | 90 | - |  |
| gravitee-small | **214** | 74.3% [68.9%, 79.2%] | 12.2% | 0.077 [0.053, 0.109] | 0.064 | 0.098 | 0.013 | 0.048 | 0.075 | 199/250 | 21182 | 0 | 12 | 29M |  |
| gravitee-small+cpu-int8 | **217** | 75.3% [70.4%, 80.3%] | 11.5% | 0.079 [0.055, 0.111] | 0.067 | 0.094 | 0.014 | 0.048 | 0.075 | 193/250 | 18792 | 0 | 65 | 29M |  |
| kingfisher | **242** | 84.0% [79.4%, 88.2%] | 13.9% | 0.441 [0.154, 0.643] | 0.392 | 0.503 | 0.060 | 0.250 | 0.441 | 10/250 | 4920 | 0 | 11 | - |  |
| gliner-pii-edge+cpu-int8 | **243** | 84.4% [79.8%, 88.8%] | 11.1% | 0.262 [0.069, 0.527] | 0.420 | 0.190 | 0.078 | 0.121 | 0.262 | 77/250 | 3202 | 0 | 847 | 45M |  |
| trufflehog | **244** | 84.7% [80.5%, 88.8%] | 12.5% | 0.164 [0.095, 0.269] | 0.258 | 0.120 | 0.064 | 0.235 | 0.164 | 8/250 | 2189 | 0 | 48 | - |  |
| gliner-pii-base | **246** | 85.4% [80.6%, 90.0%] | 9.4% | 0.168 [0.053, 0.328] | 0.333 | 0.113 | 0.035 | 0.093 | 0.168 | 127/250 | 4214 | 0 | 18 | 166M |  |
| gliner2-hivetrace-uni | **248** | 86.1% [81.3%, 90.3%] | 8.0% | 0.074 [0.040, 0.134] | 0.223 | 0.044 | 0.042 | 0.112 | 0.074 | 97/250 | 2640 | 0 | 33 | 147M |  |
| ru-pii-ner | **253** | 87.8% [83.9%, 91.9%] | 7.3% | 0.242 [0.036, 0.501] | 0.276 | 0.215 | 0.029 | 0.060 | 0.000 | 119/250 | 7336 | 0 | 272 | 358M |  |
| gliner2-vladlinv | **260** | 90.3% [86.6%, 94.0%] | 6.6% | 0.158 [0.036, 0.339] | 0.494 | 0.094 | 0.061 | 0.123 | 0.158 | 11/250 | 217 | 0 | 19 | 287M |  |
| spacy-ru-lg | **274** | 95.1% [92.1%, 97.7%] | 3.5% | 0.439 [0.015, 0.643] | 0.416 | 0.465 | 0.005 | 0.022 | 0.000 | 143/250 | 14601 | 0 | 24 | - |  |
| davlan-mbert+cpu-int8 | **284** | 98.6% [97.2%, 99.7%] | 0.0% | 0.002 [0.000, 0.006] | 0.009 | 0.001 | 0.000 | 0.009 | 0.000 | 107/250 | 3081 | 0 | 781 | 177M |  |
| natasha | **285** | 99.0% [97.1%, 100.0%] | 0.7% | 0.193 [0.000, 0.496] | 0.373 | 0.130 | 0.004 | 0.006 | 0.000 | 95/250 | 3622 | 0 | 12 | - |  |
| davlan-mbert | **285** | 99.0% [97.2%, 100.0%] | 0.0% | 0.002 [0.000, 0.006] | 0.006 | 0.001 | 0.000 | 0.006 | 0.000 | 144/250 | 4079 | 0 | 23 | 177M |  |
| davlan-xlmr+cpu-int8 | **287** | 99.7% [98.9%, 100.0%] | 0.0% | 0.001 [0.000, 0.002] | 0.009 | 0.000 | 0.000 | 0.005 | 0.000 | 35/250 | 657 | 0 | 765 | 277M |  |
| davlan-xlmr | **287** | 99.7% [98.9%, 100.0%] | 0.0% | 0.000 [0.000, 0.001] | 0.001 | 0.000 | 0.000 | 0.002 | 0.000 | 132/250 | 2869 | 0 | 22 | 277M |  |
| gliner-multi-v21+cpu-int8 | **288** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/250 | 0 | 0 | 807 | 289M |  |
| gliner-nvidia+cpu-int8 | **288** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/250 | 0 | 0 | 1337 | 445M |  |
| gliner-urchade+cpu-int8 | **288** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/250 | 0 | 0 | 878 | 289M |  |
| ner-ru-gherman+cpu-int8 | **288** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 24/250 | 609 | 0 | 609 | 177M |  |
| ner-ru-gherman | **288** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 33/250 | 624 | 0 | 23 | 177M |  |
| spacy-alrosait | **288** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/250 | 0 | 0 | 24 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: pplx+cpu-int8 ≈ pii-shield-onnx; pii-shield-onnx ≈ nym-base+ov100; nym-base+ov100 ≈ nym-base+sent300; nym-base+sent300 ≈ nym-base; nym-base ≈ opf-ru; opf-ru ≈ nym-base+cpu-int8; nym-base+cpu-int8 ≈ apararti; apararti ≈ nym-small; nym-small ≈ traciora; traciora ≈ opf-kz-ru; opf-kz-ru ≈ pplx+sent300; pplx+sent300 ≈ opf-ru-v2+sent300; opf-ru-v2+sent300 ≈ pplx+ov100; pplx+ov100 ≈ pplx; pplx ≈ bardsai-eu; bardsai-eu ≈ opf-ru-v2; opf-ru-v2 ≈ opf-ru-v2+ov100; opf-ru-v2+ov100 ≈ mmbert32k+cpu-int8; mmbert32k+cpu-int8 ≈ openmed-nemotron; openmed-nemotron ≈ openmed-multilingual; openmed-multilingual ≈ openai-base; openai-base ≈ kalyan-ettin; kalyan-ettin ≈ gliner-pii-edge; gliner-pii-edge ≈ ru-legal-ner+ov100; ru-legal-ner+ov100 ≈ ru-legal-ner; ru-legal-ner ≈ ru-legal-ner+cpu-int8; ru-legal-ner+cpu-int8 ≈ mmbert32k+nochunk; mmbert32k+nochunk ≈ ru-legal-ner+sent300; ru-legal-ner+sent300 ≈ credsweeper-noml; credsweeper-noml ≈ mmbert32k; credsweeper ≈ nuner-zero; nuner-zero ≈ rules-ru; rules-ru ≈ gliner2-fastino; gliner2-fastino ≈ gliner-nvidia+ov100; gliner-nvidia+ov100 ≈ gliner-urchade; gliner-urchade ≈ gliner-nvidia+sent300; gliner-nvidia+sent300 ≈ gliner-stream-pii; gliner-stream-pii ≈ gliner-nvidia; gliner-nvidia ≈ betterleaks; betterleaks ≈ gitleaks; gitleaks ≈ gliner25-fastino+ov100; gliner25-fastino+ov100 ≈ fef2-secret-ru; fef2-secret-ru ≈ fef2-secret-ru+cpu-int8; fef2-secret-ru+cpu-int8 ≈ gliner25-fastino+sent300; gliner25-fastino+sent300 ≈ deepsecrets; deepsecrets ≈ gliner25-fastino; gliner25-fastino ≈ stanza-ru; stanza-ru ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ ner-ru-yqelz; ner-ru-yqelz ≈ gliner25-fastino+nochunk; gliner25-fastino+nochunk ≈ gliner2-large; gliner2-large ≈ noseyparker; noseyparker ≈ titus; titus ≈ gliner-multi-v21; gliner-multi-v21 ≈ detect-secrets; detect-secrets ≈ gravitee-small; gravitee-small ≈ gravitee-small+cpu-int8; kingfisher ≈ gliner-pii-edge+cpu-int8; gliner-pii-edge+cpu-int8 ≈ trufflehog; trufflehog ≈ gliner-pii-base; gliner-pii-base ≈ gliner2-hivetrace-uni; gliner2-hivetrace-uni ≈ ru-pii-ner; ru-pii-ner ≈ gliner2-vladlinv; gliner2-vladlinv ≈ spacy-ru-lg; davlan-mbert+cpu-int8 ≈ natasha; natasha ≈ davlan-mbert; davlan-mbert ≈ davlan-xlmr+cpu-int8; davlan-xlmr+cpu-int8 ≈ davlan-xlmr; davlan-xlmr ≈ gliner-multi-v21+cpu-int8; gliner-multi-v21+cpu-int8 ≈ gliner-nvidia+cpu-int8; gliner-nvidia+cpu-int8 ≈ gliner-urchade+cpu-int8; gliner-urchade+cpu-int8 ≈ ner-ru-gherman+cpu-int8; ner-ru-gherman+cpu-int8 ≈ ner-ru-gherman; ner-ru-gherman ≈ spacy-alrosait

Legacy runs on this set: betterleaks, credsweeper, credsweeper-noml, deepsecrets, detect-secrets, kingfisher, noseyparker, titus, trufflehog. Their meta carries no `protocol` and no `bench_sha256`, so the version of the text they were taken from is confirmed only by the row and character counts, not by a fingerprint.

detect-secrets, trufflehog mark a whole line at a time (`granularity` in the meta line), so their char P / R / F1 and entity exact are not comparable with the rest; their missed count is.

## Missed by group

| model | SECRET |
|---|---|
| spans in gold | 288 |
| pplx+cpu-int8 | 0 (0.0%) |
| pii-shield-onnx | 1 (0.3%) |
| nym-base+ov100 | 2 (0.7%) |
| nym-base+sent300 | 3 (1.0%) |
| nym-base | 4 (1.4%) |
| opf-ru | 5 (1.7%) |
| nym-base+cpu-int8 | 5 (1.7%) |
| apararti | 6 (2.1%) |
| nym-small | 6 (2.1%) |
| traciora | 9 (3.1%) |
| opf-kz-ru | 9 (3.1%) |
| pplx+sent300 | 9 (3.1%) |
| opf-ru-v2+sent300 | 10 (3.5%) |
| pplx+ov100 | 11 (3.8%) |
| pplx | 12 (4.2%) |
| bardsai-eu | 13 (4.5%) |
| opf-ru-v2 | 14 (4.9%) |
| opf-ru-v2+ov100 | 15 (5.2%) |
| mmbert32k+cpu-int8 | 16 (5.6%) |
| openmed-nemotron | 17 (5.9%) |
| openmed-multilingual | 20 (6.9%) |
| openai-base | 21 (7.3%) |
| kalyan-ettin | 34 (11.8%) |
| gliner-pii-edge | 37 (12.8%) |
| ru-legal-ner+ov100 | 38 (13.2%) |
| ru-legal-ner | 45 (15.6%) |
| ru-legal-ner+cpu-int8 | 46 (16.0%) |
| mmbert32k+nochunk | 47 (16.3%) |
| ru-legal-ner+sent300 | 50 (17.4%) |
| credsweeper-noml | 52 (18.1%) |
| mmbert32k | 53 (18.4%) |
| credsweeper | 76 (26.4%) |
| nuner-zero | 85 (29.5%) |
| rules-ru | 93 (32.3%) |
| gliner2-fastino | 100 (34.7%) |
| gliner-nvidia+ov100 | 101 (35.1%) |
| gliner-urchade | 110 (38.2%) |
| gliner-nvidia+sent300 | 114 (39.6%) |
| gliner-stream-pii | 121 (42.0%) |
| gliner-nvidia | 121 (42.0%) |
| betterleaks | 123 (42.7%) |
| gitleaks | 130 (45.1%) |
| gliner25-fastino+ov100 | 132 (45.8%) |
| fef2-secret-ru | 140 (48.6%) |
| fef2-secret-ru+cpu-int8 | 145 (50.3%) |
| gliner25-fastino+sent300 | 155 (53.8%) |
| deepsecrets | 160 (55.6%) |
| gliner25-fastino | 170 (59.0%) |
| stanza-ru | 179 (62.2%) |
| gliner2-hivetrace-omni | 187 (64.9%) |
| ner-ru-yqelz | 189 (65.6%) |
| gliner25-fastino+nochunk | 189 (65.6%) |
| gliner2-large | 195 (67.7%) |
| noseyparker | 201 (69.8%) |
| titus | 202 (70.1%) |
| gliner-multi-v21 | 203 (70.5%) |
| detect-secrets | 213 (74.0%) |
| gravitee-small | 214 (74.3%) |
| gravitee-small+cpu-int8 | 217 (75.3%) |
| kingfisher | 242 (84.0%) |
| gliner-pii-edge+cpu-int8 | 243 (84.4%) |
| trufflehog | 244 (84.7%) |
| gliner-pii-base | 246 (85.4%) |
| gliner2-hivetrace-uni | 248 (86.1%) |
| ru-pii-ner | 253 (87.8%) |
| gliner2-vladlinv | 260 (90.3%) |
| spacy-ru-lg | 274 (95.1%) |
| davlan-mbert+cpu-int8 | 284 (98.6%) |
| natasha | 285 (99.0%) |
| davlan-mbert | 285 (99.0%) |
| davlan-xlmr+cpu-int8 | 287 (99.7%) |
| davlan-xlmr | 287 (99.7%) |
| gliner-multi-v21+cpu-int8 | 288 (100.0%) |
| gliner-nvidia+cpu-int8 | 288 (100.0%) |
| gliner-urchade+cpu-int8 | 288 (100.0%) |
| ner-ru-gherman+cpu-int8 | 288 (100.0%) |
| ner-ru-gherman | 288 (100.0%) |
| spacy-alrosait | 288 (100.0%) |

## Char recall by gold type

| type | group | pplx+cpu-int8 | pii-shield-onnx | nym-base+ov100 | nym-base+sent300 | nym-base | opf-ru | nym-base+cpu-int8 | apararti | nym-small | traciora | opf-kz-ru | pplx+sent300 | opf-ru-v2+sent300 | pplx+ov100 | pplx | bardsai-eu | opf-ru-v2 | opf-ru-v2+ov100 | mmbert32k+cpu-int8 | openmed-nemotron | openmed-multilingual | openai-base | kalyan-ettin | gliner-pii-edge | ru-legal-ner+ov100 | ru-legal-ner | ru-legal-ner+cpu-int8 | mmbert32k+nochunk | ru-legal-ner+sent300 | credsweeper-noml | mmbert32k | credsweeper | nuner-zero | rules-ru | gliner2-fastino | gliner-nvidia+ov100 | gliner-urchade | gliner-nvidia+sent300 | gliner-stream-pii | gliner-nvidia | betterleaks | gitleaks | gliner25-fastino+ov100 | fef2-secret-ru | fef2-secret-ru+cpu-int8 | gliner25-fastino+sent300 | deepsecrets | gliner25-fastino | stanza-ru | gliner2-hivetrace-omni | ner-ru-yqelz | gliner25-fastino+nochunk | gliner2-large | noseyparker | titus | gliner-multi-v21 | detect-secrets | gravitee-small | gravitee-small+cpu-int8 | kingfisher | gliner-pii-edge+cpu-int8 | trufflehog | gliner-pii-base | gliner2-hivetrace-uni | ru-pii-ner | gliner2-vladlinv | spacy-ru-lg | davlan-mbert+cpu-int8 | natasha | davlan-mbert | davlan-xlmr+cpu-int8 | davlan-xlmr | gliner-multi-v21+cpu-int8 | gliner-nvidia+cpu-int8 | gliner-urchade+cpu-int8 | ner-ru-gherman+cpu-int8 | ner-ru-gherman | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SECRET | SECRET | 0.969 | 0.980 | 0.941 | 0.943 | 0.938 | 0.943 | 0.938 | 0.944 | 0.938 | 0.940 | 0.936 | 0.941 | 0.932 | 0.947 | 0.878 | 0.939 | 0.922 | 0.929 | 0.913 | 0.935 | 0.919 | 0.915 | 0.891 | 0.877 | 0.391 | 0.356 | 0.356 | 0.794 | 0.362 | 0.722 | 0.815 | 0.693 | 0.369 | 0.649 | 0.691 | 0.779 | 0.329 | 0.752 | 0.671 | 0.734 | 0.726 | 0.727 | 0.215 | 0.587 | 0.576 | 0.386 | 0.207 | 0.232 | 0.632 | 0.257 | 0.204 | 0.120 | 0.082 | 0.488 | 0.493 | 0.085 | 0.472 | 0.098 | 0.094 | 0.503 | 0.190 | 0.120 | 0.113 | 0.044 | 0.215 | 0.094 | 0.465 | 0.001 | 0.130 | 0.001 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## char F1 by domain

| domain | n | pplx+cpu-int8 | pii-shield-onnx | nym-base+ov100 | nym-base+sent300 | nym-base | opf-ru | nym-base+cpu-int8 | apararti | nym-small | traciora | opf-kz-ru | pplx+sent300 | opf-ru-v2+sent300 | pplx+ov100 | pplx | bardsai-eu | opf-ru-v2 | opf-ru-v2+ov100 | mmbert32k+cpu-int8 | openmed-nemotron | openmed-multilingual | openai-base | kalyan-ettin | gliner-pii-edge | ru-legal-ner+ov100 | ru-legal-ner | ru-legal-ner+cpu-int8 | mmbert32k+nochunk | ru-legal-ner+sent300 | credsweeper-noml | mmbert32k | credsweeper | nuner-zero | rules-ru | gliner2-fastino | gliner-nvidia+ov100 | gliner-urchade | gliner-nvidia+sent300 | gliner-stream-pii | gliner-nvidia | betterleaks | gitleaks | gliner25-fastino+ov100 | fef2-secret-ru | fef2-secret-ru+cpu-int8 | gliner25-fastino+sent300 | deepsecrets | gliner25-fastino | stanza-ru | gliner2-hivetrace-omni | ner-ru-yqelz | gliner25-fastino+nochunk | gliner2-large | noseyparker | titus | gliner-multi-v21 | detect-secrets | gravitee-small | gravitee-small+cpu-int8 | kingfisher | gliner-pii-edge+cpu-int8 | trufflehog | gliner-pii-base | gliner2-hivetrace-uni | ru-pii-ner | gliner2-vladlinv | spacy-ru-lg | davlan-mbert+cpu-int8 | natasha | davlan-mbert | davlan-xlmr+cpu-int8 | davlan-xlmr | gliner-multi-v21+cpu-int8 | gliner-nvidia+cpu-int8 | gliner-urchade+cpu-int8 | ner-ru-gherman+cpu-int8 | ner-ru-gherman | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| issue | 500 | 0.208 | 0.124 | 0.350 | 0.327 | 0.350 | 0.372 | 0.343 | 0.344 | 0.331 | 0.416 | 0.327 | 0.289 | 0.411 | 0.303 | 0.288 | 0.361 | 0.418 | 0.409 | 0.300 | 0.269 | 0.284 | 0.402 | 0.344 | 0.352 | 0.132 | 0.129 | 0.128 | 0.337 | 0.125 | 0.477 | 0.298 | 0.490 | 0.308 | 0.246 | 0.352 | 0.463 | 0.288 | 0.401 | 0.501 | 0.449 | 0.541 | 0.538 | 0.128 | 0.544 | 0.563 | 0.188 | 0.228 | 0.140 | 0.179 | 0.284 | 0.107 | 0.103 | 0.090 | 0.421 | 0.420 | 0.095 | 0.371 | 0.077 | 0.079 | 0.441 | 0.262 | 0.164 | 0.168 | 0.074 | 0.242 | 0.158 | 0.439 | 0.002 | 0.193 | 0.002 | 0.001 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| pii-shield-onnx | 1 (0.3%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| nym-base+ov100 | 2 (0.7%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| nym-base+sent300 | 3 (1.0%) | 2 (0.7%) | 2 (0.7%) | 2 (0.7%) |
| nym-base | 4 (1.4%) | 1 (0.3%) | 1 (0.3%) | 1 (0.3%) |
| opf-ru | 5 (1.7%) | 5 (1.7%) | 5 (1.7%) | 5 (1.7%) |
| nym-base+cpu-int8 | 5 (1.7%) | 1 (0.3%) | 1 (0.3%) | 1 (0.3%) |
| apararti | 6 (2.1%) | 6 (2.1%) | 6 (2.1%) | 6 (2.1%) |
| nym-small | 6 (2.1%) | 5 (1.7%) | 5 (1.7%) | 5 (1.7%) |
| traciora | 9 (3.1%) | 7 (2.4%) | 6 (2.1%) | 6 (2.1%) |
| opf-kz-ru | 9 (3.1%) | 9 (3.1%) | 9 (3.1%) | 9 (3.1%) |
| opf-ru-v2+sent300 | 10 (3.5%) | 8 (2.8%) | 8 (2.8%) | 8 (2.8%) |
| bardsai-eu | 13 (4.5%) | 9 (3.1%) | 9 (3.1%) | 9 (3.1%) |
| opf-ru-v2 | 14 (4.9%) | 12 (4.2%) | 12 (4.2%) | 12 (4.2%) |
| opf-ru-v2+ov100 | 15 (5.2%) | 12 (4.2%) | 12 (4.2%) | 12 (4.2%) |
| mmbert32k+cpu-int8 | 16 (5.6%) | 3 (1.0%) | 1 (0.3%) | 1 (0.3%) |
| openmed-nemotron | 17 (5.9%) | 13 (4.5%) | 13 (4.5%) | 13 (4.5%) |
| openmed-multilingual | 20 (6.9%) | 19 (6.6%) | 19 (6.6%) | 19 (6.6%) |
| openai-base | 21 (7.3%) | 21 (7.3%) | 21 (7.3%) | 21 (7.3%) |
| kalyan-ettin | 34 (11.8%) | 18 (6.2%) | 18 (6.2%) | 18 (6.2%) |
| gliner-pii-edge | 37 (12.8%) | 1 (0.3%) | 0 (0.0%) | 0 (0.0%) |
| ru-legal-ner+ov100 | 38 (13.2%) | 25 (8.7%) | 25 (8.7%) | 25 (8.7%) |
| ru-legal-ner | 45 (15.6%) | 31 (10.8%) | 31 (10.8%) | 31 (10.8%) |
| ru-legal-ner+cpu-int8 | 46 (16.0%) | 29 (10.1%) | 29 (10.1%) | 29 (10.1%) |
| mmbert32k+nochunk | 47 (16.3%) | 16 (5.6%) | 14 (4.9%) | 14 (4.9%) |
| ru-legal-ner+sent300 | 50 (17.4%) | 30 (10.4%) | 30 (10.4%) | 30 (10.4%) |
| mmbert32k | 53 (18.4%) | 7 (2.4%) | 6 (2.1%) | 6 (2.1%) |
| nuner-zero | 85 (29.5%) | 45 (15.6%) | 37 (12.8%) | 24 (8.3%) |
| gliner2-fastino | 100 (34.7%) | 77 (26.7%) | 69 (24.0%) | 60 (20.8%) |
| gliner-nvidia+ov100 | 101 (35.1%) | 90 (31.2%) | 81 (28.1%) | 64 (22.2%) |
| gliner-urchade | 110 (38.2%) | 66 (22.9%) | 45 (15.6%) | 26 (9.0%) |
| gliner-nvidia+sent300 | 114 (39.6%) | 100 (34.7%) | 92 (31.9%) | 78 (27.1%) |
| gliner-stream-pii | 121 (42.0%) | 95 (33.0%) | 78 (27.1%) | 58 (20.1%) |
| gliner-nvidia | 121 (42.0%) | 105 (36.5%) | 95 (33.0%) | 82 (28.5%) |
| gliner25-fastino+ov100 | 132 (45.8%) | 90 (31.2%) | 58 (20.1%) | 34 (11.8%) |
| fef2-secret-ru | 140 (48.6%) | 138 (47.9%) | 138 (47.9%) | 138 (47.9%) |
| fef2-secret-ru+cpu-int8 | 145 (50.3%) | 143 (49.7%) | 143 (49.7%) | 143 (49.7%) |
| gliner25-fastino+sent300 | 155 (53.8%) | 109 (37.8%) | 101 (35.1%) | 82 (28.5%) |
| gliner25-fastino | 170 (59.0%) | 126 (43.8%) | 105 (36.5%) | 80 (27.8%) |
| gliner2-hivetrace-omni | 187 (64.9%) | 125 (43.4%) | 98 (34.0%) | 81 (28.1%) |
| ner-ru-yqelz | 189 (65.6%) | 188 (65.3%) | 188 (65.3%) | 188 (65.3%) |
| gliner25-fastino+nochunk | 189 (65.6%) | 160 (55.6%) | 135 (46.9%) | 120 (41.7%) |
| gliner2-large | 195 (67.7%) | 176 (61.1%) | 164 (56.9%) | 151 (52.4%) |
| gliner-multi-v21 | 203 (70.5%) | 93 (32.3%) | 65 (22.6%) | 35 (12.2%) |
| gravitee-small | 214 (74.3%) | 213 (74.0%) | 213 (74.0%) | 213 (74.0%) |
| gravitee-small+cpu-int8 | 217 (75.3%) | 213 (74.0%) | 213 (74.0%) | 213 (74.0%) |
| gliner-pii-edge+cpu-int8 | 243 (84.4%) | 102 (35.4%) | 27 (9.4%) | 1 (0.3%) |
| gliner-pii-base | 246 (85.4%) | 80 (27.8%) | 1 (0.3%) | 0 (0.0%) |
| gliner2-hivetrace-uni | 248 (86.1%) | 172 (59.7%) | 135 (46.9%) | 99 (34.4%) |
| gliner2-vladlinv | 260 (90.3%) | 256 (88.9%) | 251 (87.2%) | 250 (86.8%) |
| davlan-mbert+cpu-int8 | 284 (98.6%) | 284 (98.6%) | 284 (98.6%) | 284 (98.6%) |
| davlan-mbert | 285 (99.0%) | 285 (99.0%) | 285 (99.0%) | 285 (99.0%) |
| davlan-xlmr+cpu-int8 | 287 (99.7%) | 287 (99.7%) | 287 (99.7%) | 287 (99.7%) |
| davlan-xlmr | 287 (99.7%) | 287 (99.7%) | 287 (99.7%) | 287 (99.7%) |
| gliner-multi-v21+cpu-int8 | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) |
| gliner-nvidia+cpu-int8 | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) | 283 (98.3%) |
| gliner-urchade+cpu-int8 | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) | 286 (99.3%) |
| ner-ru-gherman+cpu-int8 | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) |
| ner-ru-gherman | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) | 288 (100.0%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
