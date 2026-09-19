# tonicai - en / pii (1500 rows, 2417 spans, 440 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.083 (91.7% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gliner2-fastino | **108** | 4.5% [3.5%, 5.4%] | 92.2% | 0.885 [0.874, 0.896] | 0.822 | 0.958 | 0.817 | 0.863 | 0.864 | 154/440 | 1172 | 4 | 2 | 307M |  |
| gliner2-large | **136** | 5.6% [4.7%, 6.7%] | 91.6% | 0.844 [0.831, 0.857] | 0.762 | 0.946 | 0.729 | 0.827 | 0.817 | 275/440 | 2372 | 2 | 5 | 486M |  |
| gliner-nvidia | **171** | 7.1% [5.9%, 8.3%] | 88.7% | 0.915 [0.906, 0.924] | 0.911 | 0.920 | 0.856 | 0.917 | 0.875 | 92/440 | 608 | 0 | 4 | 445M |  |
| gliner2-hivetrace-omni | **171** | 7.1% [6.0%, 8.2%] | 89.3% | 0.891 [0.882, 0.901] | 0.850 | 0.936 | 0.835 | 0.881 | 0.869 | 102/440 | 875 | 4 | 8 | 307M |  |
| gliner-pii-edge | **276** | 11.4% [9.9%, 13.1%] | 80.5% | 0.836 [0.823, 0.847] | 0.809 | 0.864 | 0.652 | 0.814 | 0.764 | 178/440 | 1201 | 0 | 8 | 45M |  |
| gravitee-small | **333** | 13.8% [12.4%, 15.3%] | 82.3% | 0.788 [0.775, 0.801] | 0.718 | 0.874 | 0.600 | 0.777 | 0.713 | 170/440 | 1555 | 0 | 2 | 29M |  |
| gliner-multi-v21 | **432** | 17.9% [16.2%, 19.7%] | 66.2% | 0.761 [0.746, 0.776] | 0.792 | 0.733 | 0.519 | 0.811 | 0.424 | 110/440 | 1021 | 0 | 2 | 289M |  |
| pplx | **502** | 20.8% [18.9%, 22.5%] | 75.5% | 0.848 [0.836, 0.860] | 0.881 | 0.817 | 0.672 | 0.831 | 0.753 | 41/440 | 317 | 0 | 44 | 596M |  |
| gliner2-vladlinv | **570** | 23.6% [21.8%, 25.5%] | 74.3% | 0.859 [0.845, 0.872] | 0.958 | 0.778 | 0.711 | 0.851 | 0.677 | 22/440 | 175 | 0 | 1 | 287M |  |
| gliner-stream-pii | **626** | 25.9% [24.1%, 27.7%] | 59.6% | 0.670 [0.654, 0.686] | 0.732 | 0.617 | 0.523 | 0.707 | 0.385 | 316/440 | 2251 | 0 | 5 | 677M |  |
| gliner25-fastino | **629** | 26.0% [24.1%, 28.1%] | 72.4% | 0.791 [0.775, 0.807] | 0.772 | 0.811 | 0.694 | 0.754 | 0.768 | 114/440 | 1114 | 1 | 1 | 287M |  |
| mmbert32k | **632** | 26.1% [24.4%, 28.1%] | 62.1% | 0.830 [0.818, 0.842] | 0.926 | 0.753 | 0.472 | 0.806 | 0.694 | 32/440 | 169 | 0 | 2 | 308M |  |
| kalyan-ettin | **658** | 27.2% [25.3%, 29.2%] | 69.0% | 0.816 [0.802, 0.829] | 0.844 | 0.790 | 0.646 | 0.748 | 0.693 | 91/440 | 538 | 0 | 2 | 68M |  |
| nuner-zero | **689** | 28.5% [25.8%, 31.2%] | 67.5% | 0.794 [0.778, 0.810] | 0.761 | 0.831 | 0.599 | 0.716 | 0.732 | 231/440 | 2208 | 0 | 4 | 449M |  |
| openmed-nemotron | **701** | 29.0% [27.1%, 31.1%] | 67.3% | 0.818 [0.805, 0.832] | 0.870 | 0.772 | 0.690 | 0.762 | 0.755 | 61/440 | 317 | 0 | 26 | 1.4B |  |
| bardsai-eu | **738** | 30.5% [28.3%, 32.9%] | 53.6% | 0.732 [0.715, 0.749] | 0.863 | 0.636 | 0.462 | 0.781 | 0.201 | 13/440 | 106 | 0 | 193 | - |  |
| gliner2-hivetrace-uni | **755** | 31.2% [29.1%, 33.3%] | 67.4% | 0.814 [0.799, 0.830] | 0.903 | 0.741 | 0.740 | 0.771 | 0.759 | 76/440 | 517 | 0 | 7 | 147M |  |
| openai-base | **761** | 31.5% [29.3%, 33.8%] | 65.4% | 0.841 [0.827, 0.854] | 0.949 | 0.755 | 0.642 | 0.795 | 0.763 | 14/440 | 124 | 0 | 70 | 1.4B |  |
| openmed-multilingual | **762** | 31.5% [29.5%, 33.7%] | 63.4% | 0.815 [0.801, 0.828] | 0.869 | 0.768 | 0.644 | 0.721 | 0.707 | 124/440 | 574 | 0 | 24 | 1.4B |  |
| nym-small | **852** | 35.3% [33.0%, 37.7%] | 62.0% | 0.849 [0.835, 0.860] | 0.945 | 0.770 | 0.691 | 0.761 | 0.518 | 18/440 | 118 | 0 | 16 | - |  |
| ner-ru-yqelz | **855** | 35.4% [33.4%, 37.5%] | 57.3% | 0.514 [0.493, 0.533] | 0.599 | 0.450 | 0.459 | 0.672 | 0.412 | 192/440 | 2207 | 0 | 2 | 559M |  |
| opf-ru | **891** | 36.9% [34.7%, 39.0%] | 59.5% | 0.816 [0.802, 0.831] | 0.944 | 0.719 | 0.626 | 0.747 | 0.739 | 22/440 | 112 | 0 | 41 | 1.4B |  |
| apararti | **901** | 37.3% [35.1%, 39.6%] | 59.3% | 0.815 [0.799, 0.830] | 0.926 | 0.727 | 0.594 | 0.743 | 0.732 | 22/440 | 150 | 0 | 63 | 1.4B |  |
| davlan-xlmr | **963** | 39.8% [37.2%, 42.9%] | 55.7% | 0.549 [0.521, 0.577] | 0.878 | 0.400 | 0.558 | 0.726 | 0.455 | 10/440 | 71 | 0 | 2 | 277M |  |
| nym-base | **1003** | 41.5% [39.1%, 43.9%] | 55.4% | 0.816 [0.802, 0.830] | 0.937 | 0.723 | 0.648 | 0.713 | 0.524 | 20/440 | 166 | 0 | 2 | 308M |  |
| opf-kz-ru | **1049** | 43.4% [41.2%, 45.9%] | 53.4% | 0.794 [0.778, 0.809] | 0.941 | 0.686 | 0.550 | 0.704 | 0.720 | 13/440 | 88 | 0 | 60 | 1.4B |  |
| traciora | **1159** | 48.0% [45.6%, 50.3%] | 49.0% | 0.783 [0.767, 0.800] | 0.947 | 0.668 | 0.512 | 0.673 | 0.700 | 13/440 | 98 | 0 | 138 | 1.4B |  |
| ru-pii-ner | **1178** | 48.7% [46.4%, 50.9%] | 48.9% | 0.737 [0.720, 0.755] | 0.864 | 0.642 | 0.501 | 0.642 | 0.461 | 38/440 | 368 | 0 | 53 | 358M |  |
| ner-ru-gherman | **1212** | 50.1% [47.6%, 52.9%] | 38.8% | 0.493 [0.468, 0.514] | 0.928 | 0.336 | 0.494 | 0.648 | 0.000 | 5/440 | 33 | 0 | 2 | 177M |  |
| stanza-ru | **1329** | 55.0% [51.8%, 58.5%] | 44.6% | 0.275 [0.258, 0.292] | 0.215 | 0.382 | 0.208 | 0.470 | 0.035 | 114/440 | 1411 | 0 | 28 | - |  |
| davlan-mbert | **1337** | 55.3% [52.1%, 58.9%] | 39.5% | 0.477 [0.444, 0.503] | 0.838 | 0.333 | 0.436 | 0.589 | 0.321 | 5/440 | 23 | 0 | 2 | 177M |  |
| gliner-pii-base | **1395** | 57.7% [55.7%, 59.8%] | 39.3% | 0.560 [0.535, 0.584] | 0.745 | 0.448 | 0.483 | 0.530 | 0.505 | 121/440 | 963 | 0 | 2 | 166M |  |
| gliner-urchade | **1397** | 57.8% [55.3%, 60.0%] | 37.7% | 0.670 [0.650, 0.690] | 0.705 | 0.639 | 0.395 | 0.519 | 0.508 | 123/440 | 1229 | 0 | 5 | 289M |  |
| opf-ru-v2 | **1412** | 58.4% [56.2%, 60.5%] | 38.4% | 0.748 [0.729, 0.766] | 0.971 | 0.608 | 0.422 | 0.582 | 0.674 | 2/440 | 8 | 0 | 500 | 1.4B |  |
| ru-legal-ner | **1647** | 68.1% [65.8%, 70.4%] | 25.2% | 0.554 [0.534, 0.575] | 0.576 | 0.534 | 0.176 | 0.382 | 0.437 | 156/440 | 1573 | 0 | 2 | 29M |  |
| pii-shield-onnx | **1744** | 72.2% [70.2%, 74.1%] | 25.7% | 0.652 [0.628, 0.676] | 0.861 | 0.525 | 0.317 | 0.401 | 0.573 | 40/440 | 234 | 0 | 38 | - |  |
| rules-ru | **1954** | 80.8% [79.0%, 82.6%] | 15.6% | 0.651 [0.623, 0.679] | 0.998 | 0.483 | 0.254 | 0.322 | 0.568 | 0/440 | 0 | 0 | 0 | - |  |
| fef2-secret-ru | **2073** | 85.8% [84.1%, 87.2%] | 10.9% | 0.484 [0.453, 0.517] | 0.939 | 0.326 | 0.145 | 0.247 | 0.017 | 2/440 | 24 | 0 | 2 | 177M |  |
| spacy-ru-lg | **2076** | 85.9% [83.9%, 87.8%] | 14.1% | 0.154 [0.131, 0.177] | 0.309 | 0.102 | 0.098 | 0.239 | 0.040 | 11/440 | 269 | 0 | 2 | - |  |
| natasha | **2103** | 87.0% [85.2%, 88.8%] | 11.3% | 0.186 [0.158, 0.213] | 0.780 | 0.105 | 0.111 | 0.228 | 0.058 | 1/440 | 2 | 0 | 1 | - |  |
| spacy-alrosait | **2416** | 100.0% [99.9%, 100.0%] | 0.0% | 0.000 [0.000, 0.001] | 0.556 | 0.000 | 0.000 | 0.001 | 0.000 | 0/440 | 0 | 0 | 2 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: gliner-nvidia ≈ gliner2-hivetrace-omni; gliner2-vladlinv ≈ gliner-stream-pii; gliner-stream-pii ≈ gliner25-fastino; gliner25-fastino ≈ mmbert32k; mmbert32k ≈ kalyan-ettin; kalyan-ettin ≈ nuner-zero; nuner-zero ≈ openmed-nemotron; openmed-nemotron ≈ bardsai-eu; bardsai-eu ≈ gliner2-hivetrace-uni; gliner2-hivetrace-uni ≈ openai-base; openai-base ≈ openmed-multilingual; nym-small ≈ ner-ru-yqelz; ner-ru-yqelz ≈ opf-ru; opf-ru ≈ apararti; apararti ≈ davlan-xlmr; davlan-xlmr ≈ nym-base; nym-base ≈ opf-kz-ru; traciora ≈ ru-pii-ner; ru-pii-ner ≈ ner-ru-gherman; stanza-ru ≈ davlan-mbert; davlan-mbert ≈ gliner-pii-base; gliner-pii-base ≈ gliner-urchade; gliner-urchade ≈ opf-ru-v2; fef2-secret-ru ≈ spacy-ru-lg; spacy-ru-lg ≈ natasha

## Missed by group

| model | PERSON | CONTACT | ACCOUNT | ORG |
|---|---|---|---|---|
| spans in gold | 1530 | 365 | 96 | 426 |
| gliner2-fastino | 30 (2.0%) | 0 (0.0%) | 13 (13.5%) | 65 (15.3%) |
| gliner2-large | 49 (3.2%) | 1 (0.3%) | 20 (20.8%) | 66 (15.5%) |
| gliner-nvidia | 29 (1.9%) | 0 (0.0%) | 22 (22.9%) | 120 (28.2%) |
| gliner2-hivetrace-omni | 58 (3.8%) | 1 (0.3%) | 22 (22.9%) | 90 (21.1%) |
| gliner-pii-edge | 148 (9.7%) | 7 (1.9%) | 6 (6.2%) | 115 (27.0%) |
| gravitee-small | 60 (3.9%) | 0 (0.0%) | 16 (16.7%) | 257 (60.3%) |
| gliner-multi-v21 | 261 (17.1%) | 41 (11.2%) | 36 (37.5%) | 94 (22.1%) |
| pplx | 155 (10.1%) | 0 (0.0%) | 0 (0.0%) | 347 (81.5%) |
| gliner2-vladlinv | 145 (9.5%) | 5 (1.4%) | 41 (42.7%) | 379 (89.0%) |
| gliner-stream-pii | 316 (20.7%) | 29 (7.9%) | 11 (11.5%) | 270 (63.4%) |
| gliner25-fastino | 449 (29.3%) | 0 (0.0%) | 72 (75.0%) | 108 (25.4%) |
| mmbert32k | 332 (21.7%) | 1 (0.3%) | 16 (16.7%) | 283 (66.4%) |
| kalyan-ettin | 333 (21.8%) | 0 (0.0%) | 32 (33.3%) | 293 (68.8%) |
| nuner-zero | 628 (41.0%) | 0 (0.0%) | 0 (0.0%) | 61 (14.3%) |
| openmed-nemotron | 329 (21.5%) | 0 (0.0%) | 27 (28.1%) | 345 (81.0%) |
| bardsai-eu | 414 (27.1%) | 2 (0.5%) | 69 (71.9%) | 253 (59.4%) |
| gliner2-hivetrace-uni | 417 (27.3%) | 0 (0.0%) | 76 (79.2%) | 262 (61.5%) |
| openai-base | 355 (23.2%) | 0 (0.0%) | 4 (4.2%) | 402 (94.4%) |
| openmed-multilingual | 414 (27.1%) | 0 (0.0%) | 9 (9.4%) | 339 (79.6%) |
| nym-small | 551 (36.0%) | 1 (0.3%) | 11 (11.5%) | 289 (67.8%) |
| ner-ru-yqelz | 470 (30.7%) | 201 (55.1%) | 94 (97.9%) | 90 (21.1%) |
| opf-ru | 484 (31.6%) | 0 (0.0%) | 13 (13.5%) | 394 (92.5%) |
| apararti | 495 (32.4%) | 0 (0.0%) | 1 (1.0%) | 405 (95.1%) |
| davlan-xlmr | 375 (24.5%) | 265 (72.6%) | 93 (96.9%) | 230 (54.0%) |
| nym-base | 683 (44.6%) | 0 (0.0%) | 22 (22.9%) | 298 (70.0%) |
| opf-kz-ru | 628 (41.0%) | 0 (0.0%) | 11 (11.5%) | 410 (96.2%) |
| traciora | 745 (48.7%) | 0 (0.0%) | 11 (11.5%) | 403 (94.6%) |
| ru-pii-ner | 711 (46.5%) | 8 (2.2%) | 44 (45.8%) | 415 (97.4%) |
| ner-ru-gherman | 608 (39.7%) | 142 (38.9%) | 66 (68.8%) | 396 (93.0%) |
| stanza-ru | 722 (47.2%) | 274 (75.1%) | 70 (72.9%) | 263 (61.7%) |
| davlan-mbert | 750 (49.0%) | 244 (66.8%) | 81 (84.4%) | 262 (61.5%) |
| gliner-pii-base | 1035 (67.6%) | 177 (48.5%) | 67 (69.8%) | 116 (27.2%) |
| gliner-urchade | 1278 (83.5%) | 10 (2.7%) | 0 (0.0%) | 109 (25.6%) |
| opf-ru-v2 | 985 (64.4%) | 0 (0.0%) | 15 (15.6%) | 412 (96.7%) |
| ru-legal-ner | 1263 (82.5%) | 1 (0.3%) | 42 (43.8%) | 341 (80.0%) |
| pii-shield-onnx | 1305 (85.3%) | 1 (0.3%) | 44 (45.8%) | 394 (92.5%) |
| rules-ru | 1530 (100.0%) | 1 (0.3%) | 1 (1.0%) | 422 (99.1%) |
| fef2-secret-ru | 1501 (98.1%) | 63 (17.3%) | 92 (95.8%) | 417 (97.9%) |
| spacy-ru-lg | 1239 (81.0%) | 358 (98.1%) | 96 (100.0%) | 383 (89.9%) |
| natasha | 1302 (85.1%) | 365 (100.0%) | 48 (50.0%) | 388 (91.1%) |
| spacy-alrosait | 1529 (99.9%) | 365 (100.0%) | 96 (100.0%) | 426 (100.0%) |

## Char recall by gold type

| type | group | gliner2-fastino | gliner2-large | gliner-nvidia | gliner2-hivetrace-omni | gliner-pii-edge | gravitee-small | gliner-multi-v21 | pplx | gliner2-vladlinv | gliner-stream-pii | gliner25-fastino | mmbert32k | kalyan-ettin | nuner-zero | openmed-nemotron | bardsai-eu | gliner2-hivetrace-uni | openai-base | openmed-multilingual | nym-small | ner-ru-yqelz | opf-ru | apararti | davlan-xlmr | nym-base | opf-kz-ru | traciora | ru-pii-ner | ner-ru-gherman | stanza-ru | davlan-mbert | gliner-pii-base | gliner-urchade | opf-ru-v2 | ru-legal-ner | pii-shield-onnx | rules-ru | fef2-secret-ru | spacy-ru-lg | natasha | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EMAIL_ADDRESS | CONTACT | 0.999 | 0.992 | 0.972 | 0.997 | 0.892 | 1.000 | 0.639 | 1.000 | 0.984 | 0.564 | 0.999 | 0.907 | 0.999 | 0.997 | 0.994 | 0.677 | 0.995 | 1.000 | 0.990 | 0.994 | 0.153 | 0.996 | 1.000 | 0.111 | 0.976 | 0.999 | 1.000 | 0.967 | 0.220 | 0.254 | 0.176 | 0.436 | 0.898 | 0.998 | 0.949 | 0.996 | 0.997 | 0.736 | 0.016 | 0.000 | 0.000 |
| NAME_FAMILY | PERSON | 0.974 | 0.959 | 0.995 | 0.987 | 0.740 | 0.990 | 0.907 | 0.907 | 0.903 | 0.710 | 0.365 | 0.919 | 0.897 | 0.199 | 0.839 | 0.825 | 0.083 | 0.786 | 0.775 | 0.743 | 0.876 | 0.751 | 0.755 | 0.812 | 0.823 | 0.708 | 0.692 | 0.643 | 0.530 | 0.516 | 0.523 | 0.548 | 0.163 | 0.622 | 0.337 | 0.456 | 0.000 | 0.038 | 0.200 | 0.163 | 0.000 |
| NAME_GIVEN | PERSON | 0.983 | 0.969 | 0.979 | 0.961 | 0.928 | 0.959 | 0.829 | 0.902 | 0.915 | 0.804 | 0.747 | 0.787 | 0.800 | 0.634 | 0.802 | 0.746 | 0.805 | 0.774 | 0.761 | 0.671 | 0.688 | 0.693 | 0.679 | 0.776 | 0.566 | 0.587 | 0.508 | 0.553 | 0.634 | 0.542 | 0.526 | 0.316 | 0.173 | 0.343 | 0.176 | 0.125 | 0.000 | 0.018 | 0.203 | 0.159 | 0.001 |
| ORGANIZATION | ORG | 0.887 | 0.885 | 0.782 | 0.833 | 0.732 | 0.442 | 0.844 | 0.163 | 0.095 | 0.356 | 0.812 | 0.333 | 0.322 | 0.913 | 0.214 | 0.465 | 0.406 | 0.053 | 0.218 | 0.384 | 0.841 | 0.066 | 0.052 | 0.508 | 0.369 | 0.035 | 0.056 | 0.031 | 0.060 | 0.444 | 0.414 | 0.755 | 0.813 | 0.043 | 0.214 | 0.077 | 0.011 | 0.039 | 0.155 | 0.134 | 0.000 |
| USERNAME | ACCOUNT | 0.765 | 0.706 | 0.639 | 0.679 | 0.826 | 0.719 | 0.517 | 0.881 | 0.526 | 0.717 | 0.217 | 0.583 | 0.549 | 0.869 | 0.602 | 0.204 | 0.174 | 0.868 | 0.774 | 0.784 | 0.013 | 0.718 | 0.897 | 0.023 | 0.654 | 0.781 | 0.800 | 0.527 | 0.313 | 0.237 | 0.149 | 0.270 | 0.925 | 0.732 | 0.432 | 0.488 | 0.872 | 0.021 | 0.000 | 0.415 | 0.000 |

## char F1 by domain

| domain | n | gliner2-fastino | gliner2-large | gliner-nvidia | gliner2-hivetrace-omni | gliner-pii-edge | gravitee-small | gliner-multi-v21 | pplx | gliner2-vladlinv | gliner-stream-pii | gliner25-fastino | mmbert32k | kalyan-ettin | nuner-zero | openmed-nemotron | bardsai-eu | gliner2-hivetrace-uni | openai-base | openmed-multilingual | nym-small | ner-ru-yqelz | opf-ru | apararti | davlan-xlmr | nym-base | opf-kz-ru | traciora | ru-pii-ner | ner-ru-gherman | stanza-ru | davlan-mbert | gliner-pii-base | gliner-urchade | opf-ru-v2 | ru-legal-ner | pii-shield-onnx | rules-ru | fef2-secret-ru | spacy-ru-lg | natasha | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| email | 194 | 0.887 | 0.874 | 0.931 | 0.895 | 0.844 | 0.753 | 0.787 | 0.785 | 0.787 | 0.739 | 0.782 | 0.806 | 0.805 | 0.711 | 0.788 | 0.829 | 0.779 | 0.781 | 0.814 | 0.869 | 0.680 | 0.742 | 0.735 | 0.841 | 0.830 | 0.706 | 0.662 | 0.723 | 0.737 | 0.271 | 0.786 | 0.700 | 0.495 | 0.608 | 0.334 | 0.408 | 0.280 | 0.245 | 0.333 | 0.383 | 0.000 |
| slack | 1306 | 0.884 | 0.833 | 0.909 | 0.889 | 0.832 | 0.802 | 0.750 | 0.875 | 0.885 | 0.644 | 0.795 | 0.840 | 0.821 | 0.822 | 0.831 | 0.679 | 0.828 | 0.864 | 0.815 | 0.839 | 0.436 | 0.845 | 0.845 | 0.361 | 0.810 | 0.827 | 0.826 | 0.742 | 0.358 | 0.282 | 0.264 | 0.496 | 0.728 | 0.797 | 0.608 | 0.741 | 0.758 | 0.561 | 0.055 | 0.082 | 0.001 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| gliner2-fastino | 108 (4.5%) | 70 (2.9%) | 61 (2.5%) | 55 (2.3%) |
| gliner2-large | 136 (5.6%) | 81 (3.4%) | 68 (2.8%) | 55 (2.3%) |
| gliner-nvidia | 171 (7.1%) | 118 (4.9%) | 88 (3.6%) | 70 (2.9%) |
| gliner2-hivetrace-omni | 171 (7.1%) | 102 (4.2%) | 84 (3.5%) | 63 (2.6%) |
| gliner-pii-edge | 276 (11.4%) | 70 (2.9%) | 40 (1.7%) | 33 (1.4%) |
| gravitee-small | 333 (13.8%) | 301 (12.5%) | 301 (12.5%) | 301 (12.5%) |
| gliner-multi-v21 | 432 (17.9%) | 103 (4.3%) | 79 (3.3%) | 55 (2.3%) |
| gliner2-vladlinv | 570 (23.6%) | 544 (22.5%) | 531 (22.0%) | 512 (21.2%) |
| gliner-stream-pii | 626 (25.9%) | 419 (17.3%) | 337 (13.9%) | 242 (10.0%) |
| gliner25-fastino | 629 (26.0%) | 526 (21.8%) | 486 (20.1%) | 433 (17.9%) |
| mmbert32k | 632 (26.1%) | 456 (18.9%) | 440 (18.2%) | 438 (18.1%) |
| kalyan-ettin | 658 (27.2%) | 510 (21.1%) | 494 (20.4%) | 492 (20.4%) |
| nuner-zero | 689 (28.5%) | 439 (18.2%) | 335 (13.9%) | 221 (9.1%) |
| openmed-nemotron | 701 (29.0%) | 606 (25.1%) | 602 (24.9%) | 602 (24.9%) |
| bardsai-eu | 738 (30.5%) | 700 (29.0%) | 693 (28.7%) | 693 (28.7%) |
| gliner2-hivetrace-uni | 755 (31.2%) | 528 (21.8%) | 367 (15.2%) | 220 (9.1%) |
| openai-base | 761 (31.5%) | 759 (31.4%) | 759 (31.4%) | 759 (31.4%) |
| openmed-multilingual | 762 (31.5%) | 715 (29.6%) | 714 (29.5%) | 714 (29.5%) |
| nym-small | 852 (35.3%) | 830 (34.3%) | 829 (34.3%) | 829 (34.3%) |
| ner-ru-yqelz | 855 (35.4%) | 800 (33.1%) | 799 (33.1%) | 799 (33.1%) |
| opf-ru | 891 (36.9%) | 876 (36.2%) | 876 (36.2%) | 876 (36.2%) |
| apararti | 901 (37.3%) | 898 (37.2%) | 898 (37.2%) | 898 (37.2%) |
| davlan-xlmr | 963 (39.8%) | 942 (39.0%) | 942 (39.0%) | 942 (39.0%) |
| nym-base | 1003 (41.5%) | 960 (39.7%) | 960 (39.7%) | 960 (39.7%) |
| opf-kz-ru | 1049 (43.4%) | 1047 (43.3%) | 1047 (43.3%) | 1047 (43.3%) |
| traciora | 1159 (48.0%) | 1150 (47.6%) | 1150 (47.6%) | 1150 (47.6%) |
| ner-ru-gherman | 1212 (50.1%) | 1199 (49.6%) | 1199 (49.6%) | 1199 (49.6%) |
| davlan-mbert | 1337 (55.3%) | 1328 (54.9%) | 1328 (54.9%) | 1328 (54.9%) |
| gliner-pii-base | 1395 (57.7%) | 311 (12.9%) | 86 (3.6%) | 39 (1.6%) |
| gliner-urchade | 1397 (57.8%) | 1212 (50.1%) | 1110 (45.9%) | 952 (39.4%) |
| opf-ru-v2 | 1412 (58.4%) | 1409 (58.3%) | 1409 (58.3%) | 1409 (58.3%) |
| ru-legal-ner | 1647 (68.1%) | 1383 (57.2%) | 1352 (55.9%) | 1345 (55.6%) |
| pii-shield-onnx | 1744 (72.2%) | 1621 (67.1%) | 1607 (66.5%) | 1606 (66.4%) |
| fef2-secret-ru | 2073 (85.8%) | 2073 (85.8%) | 2073 (85.8%) | 2073 (85.8%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
