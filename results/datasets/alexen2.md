# alexen2 - ru / pii (911 rows, 1261 spans, 40 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.522 (47.8% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gliner2-vladlinv-ru | **0** | 0.0% [0.0%, 0.0%] | 26.3% | 0.975 [0.974, 0.976] | 1.000 | 0.952 | 0.263 | 1.000 | 0.975 | 0/40 | 0 | 0 | 1 | 287M |  |
| gliner2-vladlinv | **0** | 0.0% [0.0%, 0.0%] | 26.3% | 0.975 [0.974, 0.976] | 0.999 | 0.952 | 0.263 | 0.999 | 0.975 | 0/40 | 0 | 0 | 1 | 287M |  |
| ru-pii-ner | **0** | 0.0% [0.0%, 0.0%] | 26.3% | 0.972 [0.969, 0.974] | 0.992 | 0.952 | 0.261 | 0.993 | 0.653 | 9/40 | 107 | 0 | 26 | 358M |  |
| gliner2-fastino | **3** | 0.2% [0.0%, 0.6%] | 27.8% | 0.969 [0.966, 0.972] | 0.989 | 0.949 | 0.275 | 0.990 | 0.969 | 14/40 | 130 | 0 | 2 | 307M |  |
| gliner2-fastino-ru | **4** | 0.3% [0.0%, 0.6%] | 27.4% | 0.972 [0.969, 0.974] | 0.996 | 0.948 | 0.273 | 0.995 | 0.972 | 7/40 | 67 | 0 | 1 | 307M |  |
| gliner2-hivetrace-omni | **5** | 0.4% [0.1%, 0.8%] | 27.7% | 0.969 [0.966, 0.972] | 0.990 | 0.950 | 0.274 | 0.987 | 0.969 | 14/40 | 140 | 0 | 2 | 307M |  |
| gliner2-hivetrace-omni-ru | **5** | 0.4% [0.1%, 0.8%] | 27.7% | 0.969 [0.966, 0.972] | 0.989 | 0.950 | 0.274 | 0.986 | 0.969 | 15/40 | 139 | 0 | 2 | 307M |  |
| gliner25-fastino | **5** | 0.4% [0.1%, 0.8%] | 27.0% | 0.963 [0.959, 0.967] | 0.984 | 0.944 | 0.267 | 0.986 | 0.962 | 22/40 | 247 | 0 | 1 | 287M |  |
| gliner-urchade | **7** | 0.6% [0.2%, 1.0%] | 28.0% | 0.970 [0.966, 0.973] | 0.992 | 0.948 | 0.276 | 0.991 | 0.970 | 10/40 | 110 | 0 | 3 | 289M |  |
| gliner25-fastino-ru | **8** | 0.6% [0.2%, 1.1%] | 27.1% | 0.968 [0.965, 0.971] | 0.992 | 0.946 | 0.270 | 0.991 | 0.968 | 14/40 | 145 | 0 | 1 | 287M |  |
| nuner-zero | **10** | 0.8% [0.3%, 1.3%] | 27.9% | 0.947 [0.941, 0.953] | 0.944 | 0.950 | 0.257 | 0.976 | 0.947 | 15/40 | 175 | 0 | 4 | 449M |  |
| nym-base | **15** | 1.2% [0.6%, 1.8%] | 11.8% | 0.932 [0.926, 0.937] | 0.986 | 0.884 | 0.099 | 0.982 | 0.562 | 17/40 | 201 | 0 | 2 | 308M |  |
| gliner-nvidia | **18** | 1.4% [0.8%, 2.1%] | 26.5% | 0.957 [0.953, 0.962] | 0.986 | 0.931 | 0.264 | 0.983 | 0.957 | 10/40 | 98 | 0 | 3 | 445M |  |
| mmbert32k | **21** | 1.7% [1.0%, 2.4%] | 22.6% | 0.954 [0.950, 0.958] | 0.989 | 0.922 | 0.209 | 0.981 | 0.925 | 14/40 | 126 | 0 | 2 | 308M |  |
| gliner-nvidia-ru | **25** | 2.0% [1.3%, 2.8%] | 23.5% | 0.949 [0.943, 0.954] | 0.991 | 0.909 | 0.235 | 0.981 | 0.948 | 16/40 | 134 | 0 | 3 | 445M |  |
| nym-small | **38** | 3.0% [2.1%, 4.0%] | 10.2% | 0.943 [0.938, 0.947] | 0.981 | 0.907 | 0.086 | 0.965 | 0.586 | 17/40 | 194 | 0 | 73 | - |  |
| traciora | **41** | 3.3% [2.3%, 4.3%] | 25.9% | 0.941 [0.935, 0.947] | 0.956 | 0.926 | 0.231 | 0.976 | 0.916 | 16/40 | 191 | 0 | 6 | 1.4B |  |
| opf-ru | **54** | 4.3% [3.2%, 5.4%] | 23.5% | 0.942 [0.935, 0.948] | 0.986 | 0.901 | 0.226 | 0.970 | 0.929 | 19/40 | 178 | 0 | 15 | 1.4B |  |
| pii-shield-onnx | **63** | 5.0% [3.9%, 6.2%] | 22.8% | 0.946 [0.941, 0.951] | 0.988 | 0.907 | 0.227 | 0.966 | 0.940 | 14/40 | 146 | 0 | 522 | - |  |
| pplx | **66** | 5.2% [4.0%, 6.5%] | 55.6% | 0.905 [0.896, 0.915] | 0.876 | 0.937 | 0.435 | 0.964 | 0.882 | 7/40 | 90 | 0 | 39 | 596M |  |
| gliner-pii-base | **69** | 5.5% [4.1%, 6.8%] | 24.4% | 0.945 [0.938, 0.952] | 0.984 | 0.908 | 0.245 | 0.959 | 0.945 | 16/40 | 165 | 0 | 2 | 166M |  |
| ru-legal-ner | **74** | 5.9% [4.7%, 7.2%] | 23.8% | 0.917 [0.910, 0.924] | 0.985 | 0.858 | 0.225 | 0.962 | 0.862 | 11/40 | 106 | 0 | 1 | 29M |  |
| gliner2-large | **82** | 6.5% [5.1%, 7.9%] | 21.7% | 0.923 [0.915, 0.931] | 0.968 | 0.882 | 0.207 | 0.938 | 0.917 | 10/40 | 102 | 0 | 3 | 486M |  |
| openmed-nemotron | **84** | 6.7% [5.3%, 8.1%] | 11.2% | 0.886 [0.877, 0.895] | 0.912 | 0.862 | 0.080 | 0.917 | 0.780 | 18/40 | 250 | 0 | 15 | 1.4B |  |
| bardsai-eu | **89** | 7.1% [5.6%, 8.6%] | 26.3% | 0.912 [0.904, 0.919] | 0.983 | 0.851 | 0.266 | 0.951 | 0.515 | 13/40 | 178 | 0 | 252 | - |  |
| gliner-pii-edge | **90** | 7.1% [5.7%, 8.5%] | 22.0% | 0.904 [0.895, 0.914] | 0.935 | 0.876 | 0.187 | 0.922 | 0.904 | 27/40 | 283 | 0 | 2 | 45M |  |
| apararti | **93** | 7.4% [5.9%, 8.8%] | 22.0% | 0.937 [0.931, 0.944] | 0.977 | 0.900 | 0.215 | 0.955 | 0.922 | 13/40 | 174 | 0 | 8 | 1.4B |  |
| opf-kz-ru | **96** | 7.6% [6.1%, 9.1%] | 21.9% | 0.922 [0.915, 0.930] | 0.944 | 0.901 | 0.199 | 0.943 | 0.898 | 17/40 | 209 | 0 | 7 | 1.4B |  |
| opf-ru-v2 | **100** | 7.9% [6.5%, 9.5%] | 23.3% | 0.938 [0.931, 0.945] | 0.981 | 0.899 | 0.223 | 0.953 | 0.934 | 11/40 | 159 | 0 | 17 | 1.4B |  |
| kalyan-ettin | **106** | 8.4% [6.9%, 10.0%] | 14.2% | 0.874 [0.863, 0.884] | 0.960 | 0.802 | 0.110 | 0.936 | 0.822 | 20/40 | 193 | 0 | 2 | 68M |  |
| openmed-multilingual | **145** | 11.5% [9.7%, 13.2%] | 7.1% | 0.895 [0.886, 0.905] | 0.985 | 0.820 | 0.059 | 0.923 | 0.843 | 20/40 | 144 | 0 | 13 | 1.4B |  |
| openai-base | **153** | 12.1% [10.4%, 14.1%] | 20.9% | 0.917 [0.909, 0.925] | 0.970 | 0.870 | 0.195 | 0.930 | 0.904 | 10/40 | 134 | 0 | 12 | 1.4B |  |
| gliner-multi-v21 | **157** | 12.5% [10.8%, 14.1%] | 27.0% | 0.855 [0.842, 0.869] | 0.989 | 0.753 | 0.284 | 0.927 | 0.833 | 10/40 | 95 | 0 | 2 | 289M |  |
| gliner2-hivetrace-uni | **160** | 12.7% [10.9%, 14.5%] | 21.8% | 0.894 [0.882, 0.906] | 0.992 | 0.813 | 0.231 | 0.924 | 0.892 | 7/40 | 70 | 0 | 5 | 147M |  |
| gravitee-small | **178** | 14.1% [12.1%, 16.0%] | 18.7% | 0.712 [0.698, 0.725] | 0.634 | 0.810 | 0.044 | 0.786 | 0.602 | 24/40 | 630 | 0 | 2 | 29M |  |
| gliner-stream-pii | **190** | 15.1% [13.3%, 17.0%] | 22.1% | 0.873 [0.861, 0.884] | 0.973 | 0.791 | 0.231 | 0.897 | 0.873 | 38/40 | 326 | 0 | 5 | 677M |  |
| gliner-multi-v21-ru | **201** | 15.9% [14.2%, 17.7%] | 26.7% | 0.831 [0.817, 0.845] | 0.991 | 0.715 | 0.288 | 0.906 | 0.808 | 6/40 | 54 | 0 | 1 | 289M |  |
| fef2-secret-ru | **335** | 26.6% [24.4%, 28.8%] | 22.2% | 0.814 [0.799, 0.827] | 0.984 | 0.693 | 0.243 | 0.839 | 0.410 | 16/40 | 137 | 0 | 1 | 177M |  |
| gliner-urchade-ru | **353** | 28.0% [25.5%, 30.0%] | 9.0% | 0.825 [0.812, 0.840] | 0.996 | 0.704 | 0.101 | 0.835 | 0.825 | 3/40 | 31 | 0 | 2 | 289M |  |
| ner-ru-yqelz | **555** | 44.0% [42.0%, 46.1%] | 26.1% | 0.587 [0.570, 0.604] | 0.868 | 0.443 | 0.283 | 0.669 | 0.482 | 20/40 | 289 | 0 | 2 | 559M |  |
| rules-ru | **571** | 45.3% [43.1%, 47.3%] | 4.7% | 0.733 [0.719, 0.747] | 1.000 | 0.578 | 0.060 | 0.707 | 0.733 | 0/40 | 0 | 0 | 0 | - |  |
| ner-ru-gherman | **603** | 47.8% [45.4%, 50.3%] | 4.8% | 0.577 [0.558, 0.596] | 0.980 | 0.409 | 0.051 | 0.678 | 0.000 | 15/40 | 148 | 0 | 1 | 177M |  |
| stanza-ru | **616** | 48.9% [46.8%, 51.0%] | 21.3% | 0.600 [0.580, 0.620] | 0.884 | 0.453 | 0.263 | 0.641 | 0.473 | 18/40 | 232 | 0 | 7 | - |  |
| spacy-ru-lg | **672** | 53.3% [51.2%, 55.6%] | 22.5% | 0.566 [0.545, 0.586] | 0.967 | 0.401 | 0.301 | 0.625 | 0.491 | 15/40 | 163 | 0 | 1 | - |  |
| davlan-xlmr | **686** | 54.4% [52.3%, 56.5%] | 22.4% | 0.555 [0.536, 0.574] | 0.978 | 0.388 | 0.305 | 0.622 | 0.527 | 12/40 | 171 | 0 | 1 | 277M |  |
| davlan-mbert | **695** | 55.1% [53.2%, 57.3%] | 20.9% | 0.552 [0.533, 0.571] | 0.976 | 0.385 | 0.284 | 0.611 | 0.508 | 13/40 | 156 | 0 | 1 | 177M |  |
| natasha | **730** | 57.9% [56.0%, 60.0%] | 21.3% | 0.520 [0.500, 0.538] | 0.927 | 0.361 | 0.280 | 0.578 | 0.498 | 15/40 | 207 | 0 | 0 | - |  |
| spacy-alrosait | **779** | 61.8% [60.0%, 63.7%] | 18.3% | 0.504 [0.484, 0.521] | 0.968 | 0.340 | 0.261 | 0.549 | 0.000 | 13/40 | 183 | 0 | 1 | - |  |
| gliner2-hivetrace-uni-ru | **1056** | 83.7% [81.8%, 85.8%] | 5.2% | 0.239 [0.212, 0.266] | 0.979 | 0.136 | 0.088 | 0.277 | 0.229 | 0/40 | 0 | 0 | 6 | 147M |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: gliner2-vladlinv-ru ≈ gliner2-vladlinv; gliner2-vladlinv ≈ ru-pii-ner; ru-pii-ner ≈ gliner2-fastino; gliner2-fastino ≈ gliner2-fastino-ru; gliner2-fastino-ru ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ gliner2-hivetrace-omni-ru; gliner2-hivetrace-omni-ru ≈ gliner25-fastino; gliner25-fastino ≈ gliner-urchade; gliner-urchade ≈ gliner25-fastino-ru; gliner25-fastino-ru ≈ nuner-zero; nuner-zero ≈ nym-base; nym-base ≈ gliner-nvidia; gliner-nvidia ≈ mmbert32k; mmbert32k ≈ gliner-nvidia-ru; gliner-nvidia-ru ≈ nym-small; nym-small ≈ traciora; traciora ≈ opf-ru; opf-ru ≈ pii-shield-onnx; pii-shield-onnx ≈ pplx; pplx ≈ gliner-pii-base; gliner-pii-base ≈ ru-legal-ner; ru-legal-ner ≈ gliner2-large; gliner2-large ≈ openmed-nemotron; openmed-nemotron ≈ bardsai-eu; bardsai-eu ≈ gliner-pii-edge; gliner-pii-edge ≈ apararti; apararti ≈ opf-kz-ru; opf-kz-ru ≈ opf-ru-v2; opf-ru-v2 ≈ kalyan-ettin; openmed-multilingual ≈ openai-base; openai-base ≈ gliner-multi-v21; gliner-multi-v21 ≈ gliner2-hivetrace-uni; gliner2-hivetrace-uni ≈ gravitee-small; gravitee-small ≈ gliner-stream-pii; gliner-stream-pii ≈ gliner-multi-v21-ru; fef2-secret-ru ≈ gliner-urchade-ru; ner-ru-yqelz ≈ rules-ru; rules-ru ≈ ner-ru-gherman; ner-ru-gherman ≈ stanza-ru; spacy-ru-lg ≈ davlan-xlmr; davlan-xlmr ≈ davlan-mbert

## Missed by group

| model | PERSON | CONTACT |
|---|---|---|
| spans in gold | 571 | 690 |
| gliner2-vladlinv-ru | 0 (0.0%) | 0 (0.0%) |
| gliner2-vladlinv | 0 (0.0%) | 0 (0.0%) |
| ru-pii-ner | 0 (0.0%) | 0 (0.0%) |
| gliner2-fastino | 3 (0.5%) | 0 (0.0%) |
| gliner2-fastino-ru | 3 (0.5%) | 1 (0.1%) |
| gliner2-hivetrace-omni | 4 (0.7%) | 1 (0.1%) |
| gliner2-hivetrace-omni-ru | 4 (0.7%) | 1 (0.1%) |
| gliner25-fastino | 5 (0.9%) | 0 (0.0%) |
| gliner-urchade | 3 (0.5%) | 4 (0.6%) |
| gliner25-fastino-ru | 8 (1.4%) | 0 (0.0%) |
| nuner-zero | 10 (1.8%) | 0 (0.0%) |
| nym-base | 14 (2.5%) | 1 (0.1%) |
| gliner-nvidia | 18 (3.2%) | 0 (0.0%) |
| mmbert32k | 21 (3.7%) | 0 (0.0%) |
| gliner-nvidia-ru | 25 (4.4%) | 0 (0.0%) |
| nym-small | 37 (6.5%) | 1 (0.1%) |
| traciora | 40 (7.0%) | 1 (0.1%) |
| opf-ru | 40 (7.0%) | 14 (2.0%) |
| pii-shield-onnx | 63 (11.0%) | 0 (0.0%) |
| pplx | 66 (11.6%) | 0 (0.0%) |
| gliner-pii-base | 59 (10.3%) | 10 (1.4%) |
| ru-legal-ner | 57 (10.0%) | 17 (2.5%) |
| gliner2-large | 79 (13.8%) | 3 (0.4%) |
| openmed-nemotron | 61 (10.7%) | 23 (3.3%) |
| bardsai-eu | 63 (11.0%) | 26 (3.8%) |
| gliner-pii-edge | 80 (14.0%) | 10 (1.4%) |
| apararti | 86 (15.1%) | 7 (1.0%) |
| opf-kz-ru | 88 (15.4%) | 8 (1.2%) |
| opf-ru-v2 | 82 (14.4%) | 18 (2.6%) |
| kalyan-ettin | 62 (10.9%) | 44 (6.4%) |
| openmed-multilingual | 143 (25.0%) | 2 (0.3%) |
| openai-base | 139 (24.3%) | 14 (2.0%) |
| gliner-multi-v21 | 5 (0.9%) | 152 (22.0%) |
| gliner2-hivetrace-uni | 74 (13.0%) | 86 (12.5%) |
| gravitee-small | 134 (23.5%) | 44 (6.4%) |
| gliner-stream-pii | 33 (5.8%) | 157 (22.8%) |
| gliner-multi-v21-ru | 8 (1.4%) | 193 (28.0%) |
| fef2-secret-ru | 22 (3.9%) | 313 (45.4%) |
| gliner-urchade-ru | 345 (60.4%) | 8 (1.2%) |
| ner-ru-yqelz | 1 (0.2%) | 554 (80.3%) |
| rules-ru | 571 (100.0%) | 0 (0.0%) |
| ner-ru-gherman | 39 (6.8%) | 564 (81.7%) |
| stanza-ru | 30 (5.3%) | 586 (84.9%) |
| spacy-ru-lg | 17 (3.0%) | 655 (94.9%) |
| davlan-xlmr | 21 (3.7%) | 665 (96.4%) |
| davlan-mbert | 34 (6.0%) | 661 (95.8%) |
| natasha | 40 (7.0%) | 690 (100.0%) |
| spacy-alrosait | 89 (15.6%) | 690 (100.0%) |
| gliner2-hivetrace-uni-ru | 429 (75.1%) | 627 (90.9%) |

## Char recall by gold type

| type | group | gliner2-vladlinv-ru | gliner2-vladlinv | ru-pii-ner | gliner2-fastino | gliner2-fastino-ru | gliner2-hivetrace-omni | gliner2-hivetrace-omni-ru | gliner25-fastino | gliner-urchade | gliner25-fastino-ru | nuner-zero | nym-base | gliner-nvidia | mmbert32k | gliner-nvidia-ru | nym-small | traciora | opf-ru | pii-shield-onnx | pplx | gliner-pii-base | ru-legal-ner | gliner2-large | openmed-nemotron | bardsai-eu | gliner-pii-edge | apararti | opf-kz-ru | opf-ru-v2 | kalyan-ettin | openmed-multilingual | openai-base | gliner-multi-v21 | gliner2-hivetrace-uni | gravitee-small | gliner-stream-pii | gliner-multi-v21-ru | fef2-secret-ru | gliner-urchade-ru | ner-ru-yqelz | rules-ru | ner-ru-gherman | stanza-ru | spacy-ru-lg | davlan-xlmr | davlan-mbert | natasha | spacy-alrosait | gliner2-hivetrace-uni-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EMAIL | CONTACT | 0.953 | 0.953 | 0.953 | 0.942 | 0.943 | 0.946 | 0.946 | 0.930 | 0.941 | 0.939 | 0.953 | 0.807 | 0.953 | 0.939 | 0.951 | 0.925 | 0.943 | 0.892 | 0.945 | 0.981 | 0.950 | 0.741 | 0.943 | 0.932 | 0.738 | 0.905 | 0.921 | 0.918 | 0.884 | 0.944 | 0.939 | 0.909 | 0.303 | 0.709 | 0.820 | 0.722 | 0.177 | 0.920 | 0.942 | 0.049 | 0.953 | 0.253 | 0.294 | 0.118 | 0.063 | 0.071 | 0.000 | 0.000 | 0.029 |
| PER | PERSON | 0.959 | 0.959 | 0.959 | 0.961 | 0.958 | 0.960 | 0.960 | 0.955 | 0.962 | 0.955 | 0.955 | 0.897 | 0.905 | 0.920 | 0.852 | 0.868 | 0.906 | 0.876 | 0.851 | 0.874 | 0.868 | 0.904 | 0.791 | 0.815 | 0.910 | 0.801 | 0.850 | 0.855 | 0.878 | 0.769 | 0.651 | 0.783 | 0.960 | 0.839 | 0.758 | 0.904 | 0.958 | 0.940 | 0.338 | 0.965 | 0.000 | 0.859 | 0.940 | 0.939 | 0.947 | 0.935 | 0.928 | 0.874 | 0.230 |
| PHONE | CONTACT | 0.941 | 0.941 | 0.941 | 0.941 | 0.941 | 0.941 | 0.941 | 0.941 | 0.939 | 0.941 | 0.941 | 0.941 | 0.941 | 0.909 | 0.941 | 0.939 | 0.936 | 0.939 | 0.941 | 0.973 | 0.919 | 0.913 | 0.936 | 0.856 | 0.883 | 0.941 | 0.941 | 0.941 | 0.940 | 0.710 | 0.917 | 0.941 | 0.920 | 0.879 | 0.866 | 0.717 | 0.919 | 0.176 | 0.932 | 0.167 | 0.941 | 0.000 | 0.002 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.121 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| gliner2-vladlinv-ru | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| gliner2-vladlinv | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| gliner2-fastino | 3 (0.2%) | 2 (0.2%) | 2 (0.2%) | 1 (0.1%) |
| gliner2-fastino-ru | 4 (0.3%) | 4 (0.3%) | 4 (0.3%) | 2 (0.2%) |
| gliner2-hivetrace-omni | 5 (0.4%) | 4 (0.3%) | 3 (0.2%) | 0 (0.0%) |
| gliner2-hivetrace-omni-ru | 5 (0.4%) | 4 (0.3%) | 4 (0.3%) | 2 (0.2%) |
| gliner25-fastino | 5 (0.4%) | 4 (0.3%) | 4 (0.3%) | 4 (0.3%) |
| gliner-urchade | 7 (0.6%) | 4 (0.3%) | 2 (0.2%) | 0 (0.0%) |
| gliner25-fastino-ru | 8 (0.6%) | 8 (0.6%) | 8 (0.6%) | 8 (0.6%) |
| nuner-zero | 10 (0.8%) | 8 (0.6%) | 6 (0.5%) | 5 (0.4%) |
| nym-base | 15 (1.2%) | 14 (1.1%) | 14 (1.1%) | 14 (1.1%) |
| gliner-nvidia | 18 (1.4%) | 9 (0.7%) | 4 (0.3%) | 1 (0.1%) |
| mmbert32k | 21 (1.7%) | 13 (1.0%) | 13 (1.0%) | 13 (1.0%) |
| gliner-nvidia-ru | 25 (2.0%) | 11 (0.9%) | 6 (0.5%) | 4 (0.3%) |
| nym-small | 38 (3.0%) | 32 (2.5%) | 32 (2.5%) | 32 (2.5%) |
| traciora | 41 (3.3%) | 41 (3.3%) | 41 (3.3%) | 41 (3.3%) |
| opf-ru | 54 (4.3%) | 50 (4.0%) | 50 (4.0%) | 50 (4.0%) |
| pii-shield-onnx | 63 (5.0%) | 52 (4.1%) | 52 (4.1%) | 52 (4.1%) |
| gliner-pii-base | 69 (5.5%) | 26 (2.1%) | 5 (0.4%) | 0 (0.0%) |
| ru-legal-ner | 74 (5.9%) | 52 (4.1%) | 51 (4.0%) | 51 (4.0%) |
| gliner2-large | 82 (6.5%) | 56 (4.4%) | 47 (3.7%) | 32 (2.5%) |
| openmed-nemotron | 84 (6.7%) | 61 (4.8%) | 59 (4.7%) | 58 (4.6%) |
| bardsai-eu | 89 (7.1%) | 76 (6.0%) | 75 (5.9%) | 75 (5.9%) |
| gliner-pii-edge | 90 (7.1%) | 17 (1.3%) | 2 (0.2%) | 1 (0.1%) |
| apararti | 93 (7.4%) | 92 (7.3%) | 92 (7.3%) | 92 (7.3%) |
| opf-kz-ru | 96 (7.6%) | 95 (7.5%) | 95 (7.5%) | 95 (7.5%) |
| opf-ru-v2 | 100 (7.9%) | 100 (7.9%) | 100 (7.9%) | 100 (7.9%) |
| kalyan-ettin | 106 (8.4%) | 45 (3.6%) | 35 (2.8%) | 32 (2.5%) |
| openmed-multilingual | 145 (11.5%) | 107 (8.5%) | 102 (8.1%) | 101 (8.0%) |
| openai-base | 153 (12.1%) | 153 (12.1%) | 153 (12.1%) | 153 (12.1%) |
| gliner-multi-v21 | 157 (12.5%) | 35 (2.8%) | 6 (0.5%) | 0 (0.0%) |
| gliner2-hivetrace-uni | 160 (12.7%) | 70 (5.6%) | 50 (4.0%) | 28 (2.2%) |
| gravitee-small | 178 (14.1%) | 119 (9.4%) | 119 (9.4%) | 119 (9.4%) |
| gliner-stream-pii | 190 (15.1%) | 143 (11.3%) | 125 (9.9%) | 101 (8.0%) |
| gliner-multi-v21-ru | 201 (15.9%) | 55 (4.4%) | 13 (1.0%) | 0 (0.0%) |
| fef2-secret-ru | 335 (26.6%) | 333 (26.4%) | 332 (26.3%) | 332 (26.3%) |
| gliner-urchade-ru | 353 (28.0%) | 270 (21.4%) | 194 (15.4%) | 105 (8.3%) |
| ner-ru-yqelz | 555 (44.0%) | 542 (43.0%) | 542 (43.0%) | 542 (43.0%) |
| ner-ru-gherman | 603 (47.8%) | 603 (47.8%) | 603 (47.8%) | 603 (47.8%) |
| davlan-xlmr | 686 (54.4%) | 686 (54.4%) | 686 (54.4%) | 686 (54.4%) |
| davlan-mbert | 695 (55.1%) | 695 (55.1%) | 695 (55.1%) | 695 (55.1%) |
| gliner2-hivetrace-uni-ru | 1056 (83.7%) | 506 (40.1%) | 233 (18.5%) | 49 (3.9%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
