# alrosait - ru / pii (1500 rows, 1862 spans, 340 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.158 (84.2% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| spacy-alrosait | **1** | 0.1% [0.0%, 0.2%] | 99.8% | 0.999 [0.997, 0.999] | 0.998 | 0.999 | 0.995 | 0.998 | 0.587 | 3/340 | 51 | 0 | 3 | - | train |
| gliner25-fastino | **8** | 0.4% [0.2%, 0.7%] | 87.1% | 0.889 [0.878, 0.899] | 0.841 | 0.942 | 0.704 | 0.829 | 0.885 | 282/340 | 6070 | 0 | 3 | 287M |  |
| gliner-multi-v21 | **9** | 0.5% [0.2%, 0.8%] | 71.6% | 0.831 [0.820, 0.843] | 0.797 | 0.869 | 0.507 | 0.779 | 0.829 | 275/340 | 6096 | 0 | 4 | 289M |  |
| pplx | **10** | 0.5% [0.3%, 0.9%] | 96.7% | 0.938 [0.930, 0.945] | 0.889 | 0.992 | 0.767 | 0.892 | 0.932 | 122/340 | 2286 | 0 | 52 | 596M |  |
| nym-base | **12** | 0.6% [0.3%, 1.1%] | 18.2% | 0.910 [0.903, 0.917] | 0.922 | 0.899 | 0.094 | 0.912 | 0.092 | 168/340 | 2465 | 0 | 2 | 308M |  |
| nuner-zero | **12** | 0.6% [0.3%, 1.1%] | 77.9% | 0.873 [0.862, 0.883] | 0.818 | 0.936 | 0.557 | 0.787 | 0.860 | 254/340 | 5735 | 0 | 9 | 449M |  |
| gliner-multi-v21-ru | **15** | 0.8% [0.4%, 1.3%] | 70.9% | 0.865 [0.854, 0.875] | 0.858 | 0.871 | 0.541 | 0.843 | 0.863 | 199/340 | 3834 | 0 | 11 | 289M |  |
| gliner25-fastino-ru | **18** | 1.0% [0.5%, 1.4%] | 86.6% | 0.923 [0.915, 0.932] | 0.908 | 0.939 | 0.773 | 0.909 | 0.921 | 181/340 | 3418 | 0 | 8 | 287M |  |
| ner-ru-yqelz | **20** | 1.1% [0.6%, 1.6%] | 55.0% | 0.779 [0.768, 0.790] | 0.896 | 0.689 | 0.456 | 0.898 | 0.445 | 171/340 | 2440 | 0 | 4 | 559M |  |
| opf-ru | **22** | 1.2% [0.7%, 1.7%] | 45.6% | 0.838 [0.830, 0.847] | 0.876 | 0.804 | 0.306 | 0.871 | 0.791 | 210/340 | 3049 | 0 | 20 | 1.4B |  |
| mmbert32k | **33** | 1.8% [1.1%, 2.4%] | 44.0% | 0.843 [0.834, 0.852] | 0.924 | 0.775 | 0.299 | 0.912 | 0.387 | 134/340 | 1840 | 0 | 3 | 308M |  |
| davlan-xlmr | **35** | 1.9% [1.2%, 2.6%] | 56.1% | 0.883 [0.875, 0.891] | 0.940 | 0.832 | 0.466 | 0.935 | 0.416 | 120/340 | 1971 | 0 | 3 | 277M |  |
| gliner2-vladlinv | **53** | 2.8% [1.9%, 3.8%] | 90.7% | 0.957 [0.950, 0.964] | 0.973 | 0.942 | 0.891 | 0.964 | 0.952 | 55/340 | 895 | 0 | 4 | 287M |  |
| bardsai-eu | **54** | 2.9% [2.1%, 3.8%] | 66.0% | 0.897 [0.888, 0.905] | 0.900 | 0.893 | 0.503 | 0.888 | 0.462 | 180/340 | 3001 | 0 | 642 | - |  |
| gliner2-vladlinv-ru | **57** | 3.1% [2.1%, 4.0%] | 90.5% | 0.958 [0.952, 0.966] | 0.977 | 0.941 | 0.891 | 0.965 | 0.954 | 52/340 | 786 | 0 | 7 | 287M |  |
| fef2-secret-ru | **64** | 3.4% [2.5%, 4.5%] | 55.4% | 0.810 [0.797, 0.821] | 0.911 | 0.729 | 0.431 | 0.913 | 0.669 | 133/340 | 2408 | 0 | 2 | 177M |  |
| davlan-mbert | **67** | 3.6% [2.8%, 4.5%] | 52.6% | 0.830 [0.820, 0.840] | 0.923 | 0.754 | 0.434 | 0.910 | 0.423 | 140/340 | 2239 | 0 | 3 | 177M |  |
| ru-legal-ner | **69** | 3.7% [2.8%, 4.6%] | 72.4% | 0.887 [0.878, 0.896] | 0.890 | 0.884 | 0.501 | 0.873 | 0.801 | 141/340 | 2173 | 0 | 2 | 29M |  |
| ner-ru-gherman | **71** | 3.8% [2.9%, 4.8%] | 1.8% | 0.839 [0.831, 0.846] | 0.953 | 0.749 | 0.011 | 0.922 | 0.267 | 132/340 | 1412 | 0 | 3 | 177M |  |
| ru-pii-ner | **75** | 4.0% [3.0%, 5.1%] | 94.2% | 0.952 [0.944, 0.960] | 0.949 | 0.954 | 0.890 | 0.939 | 0.638 | 72/340 | 1254 | 0 | 49 | 358M |  |
| stanza-ru | **78** | 4.2% [3.3%, 5.1%] | 54.8% | 0.761 [0.749, 0.774] | 0.816 | 0.713 | 0.416 | 0.816 | 0.425 | 232/340 | 3518 | 0 | 29 | - |  |
| gliner-urchade | **141** | 7.6% [6.4%, 8.9%] | 90.3% | 0.850 [0.834, 0.864] | 0.847 | 0.852 | 0.781 | 0.806 | 0.847 | 244/340 | 4654 | 0 | 5 | 289M |  |
| traciora | **144** | 7.7% [6.5%, 9.1%] | 76.8% | 0.865 [0.853, 0.875] | 0.839 | 0.893 | 0.571 | 0.865 | 0.836 | 177/340 | 3894 | 0 | 21 | 1.4B |  |
| apararti | **193** | 10.4% [9.0%, 11.8%] | 68.2% | 0.845 [0.834, 0.856] | 0.849 | 0.841 | 0.538 | 0.860 | 0.807 | 157/340 | 3521 | 0 | 60 | 1.4B |  |
| openmed-nemotron | **193** | 10.4% [9.0%, 11.7%] | 16.7% | 0.646 [0.632, 0.659] | 0.641 | 0.650 | 0.075 | 0.657 | 0.500 | 251/340 | 5121 | 0 | 18 | 1.4B |  |
| gliner2-hivetrace-omni-ru | **195** | 10.5% [9.2%, 11.9%] | 78.8% | 0.794 [0.777, 0.810] | 0.842 | 0.750 | 0.701 | 0.836 | 0.745 | 239/340 | 4532 | 0 | 5 | 307M |  |
| gliner2-hivetrace-omni | **198** | 10.6% [9.3%, 11.9%] | 78.8% | 0.782 [0.766, 0.798] | 0.818 | 0.749 | 0.686 | 0.813 | 0.736 | 276/340 | 5531 | 0 | 5 | 307M |  |
| opf-ru-v2 | **203** | 10.9% [9.4%, 12.3%] | 69.1% | 0.874 [0.863, 0.884] | 0.910 | 0.840 | 0.581 | 0.892 | 0.836 | 99/340 | 1925 | 0 | 228 | 1.4B |  |
| gliner2-large | **225** | 12.1% [10.6%, 13.7%] | 51.2% | 0.721 [0.706, 0.736] | 0.748 | 0.695 | 0.372 | 0.718 | 0.685 | 288/340 | 6163 | 0 | 10 | 486M |  |
| gliner2-fastino | **228** | 12.2% [10.8%, 13.8%] | 78.5% | 0.757 [0.739, 0.775] | 0.785 | 0.732 | 0.663 | 0.753 | 0.750 | 278/340 | 6397 | 0 | 5 | 307M |  |
| pii-shield-onnx | **233** | 12.5% [11.0%, 14.0%] | 52.7% | 0.832 [0.821, 0.844] | 0.922 | 0.758 | 0.454 | 0.873 | 0.528 | 117/340 | 2001 | 0 | 1227 | - |  |
| openai-base | **239** | 12.8% [11.1%, 14.6%] | 73.8% | 0.850 [0.838, 0.862] | 0.844 | 0.856 | 0.527 | 0.864 | 0.809 | 118/340 | 3037 | 0 | 31 | 1.4B |  |
| gliner2-fastino-ru | **248** | 13.3% [11.8%, 15.0%] | 78.2% | 0.805 [0.788, 0.823] | 0.906 | 0.725 | 0.776 | 0.869 | 0.801 | 163/340 | 2949 | 0 | 7 | 307M |  |
| gliner-nvidia | **262** | 14.1% [12.4%, 15.8%] | 72.4% | 0.763 [0.745, 0.781] | 0.817 | 0.716 | 0.637 | 0.766 | 0.754 | 215/340 | 4490 | 0 | 9 | 445M |  |
| spacy-ru-lg | **267** | 14.3% [12.7%, 15.9%] | 48.1% | 0.707 [0.692, 0.721] | 0.916 | 0.575 | 0.439 | 0.850 | 0.473 | 125/340 | 1542 | 0 | 3 | - |  |
| opf-kz-ru | **280** | 15.0% [13.5%, 16.6%] | 44.0% | 0.780 [0.768, 0.794] | 0.873 | 0.705 | 0.339 | 0.844 | 0.740 | 135/340 | 2292 | 0 | 54 | 1.4B |  |
| gliner-nvidia-ru | **317** | 17.0% [15.3%, 18.9%] | 60.6% | 0.750 [0.731, 0.768] | 0.895 | 0.645 | 0.602 | 0.842 | 0.731 | 121/340 | 2161 | 0 | 26 | 445M |  |
| openmed-multilingual | **363** | 19.5% [17.7%, 21.3%] | 8.8% | 0.601 [0.587, 0.615] | 0.777 | 0.490 | 0.056 | 0.738 | 0.572 | 222/340 | 3021 | 0 | 17 | 1.4B |  |
| natasha | **389** | 20.9% [19.1%, 22.8%] | 50.1% | 0.676 [0.660, 0.693] | 0.919 | 0.535 | 0.492 | 0.819 | 0.490 | 109/340 | 1387 | 0 | 2 | - |  |
| gliner-stream-pii | **421** | 22.6% [20.7%, 24.6%] | 45.1% | 0.697 [0.680, 0.714] | 0.854 | 0.589 | 0.433 | 0.763 | 0.653 | 263/340 | 3514 | 0 | 34 | 677M |  |
| kalyan-ettin | **469** | 25.2% [23.3%, 27.3%] | 19.9% | 0.585 [0.568, 0.604] | 0.798 | 0.462 | 0.145 | 0.723 | 0.482 | 183/340 | 2561 | 0 | 3 | 68M |  |
| gliner2-hivetrace-uni | **502** | 27.0% [24.9%, 29.1%] | 55.4% | 0.699 [0.681, 0.717] | 0.952 | 0.553 | 0.606 | 0.813 | 0.667 | 84/340 | 936 | 0 | 7 | 147M |  |
| gliner-pii-edge | **508** | 27.3% [25.3%, 29.3%] | 50.4% | 0.646 [0.629, 0.664] | 0.780 | 0.552 | 0.419 | 0.662 | 0.594 | 247/340 | 3179 | 0 | 3 | 45M |  |
| gravitee-small | **631** | 33.9% [31.6%, 36.2%] | 45.9% | 0.665 [0.651, 0.679] | 0.648 | 0.683 | 0.180 | 0.668 | 0.654 | 150/340 | 3159 | 0 | 4 | 29M |  |
| gliner-pii-base | **644** | 34.6% [32.4%, 36.6%] | 51.1% | 0.622 [0.603, 0.644] | 0.893 | 0.477 | 0.555 | 0.720 | 0.601 | 170/340 | 1901 | 0 | 4 | 166M |  |
| gliner-urchade-ru | **974** | 52.3% [49.9%, 54.7%] | 46.7% | 0.645 [0.620, 0.668] | 0.915 | 0.498 | 0.598 | 0.615 | 0.644 | 97/340 | 1685 | 0 | 8 | 289M |  |
| gliner2-hivetrace-uni-ru | **1258** | 67.6% [65.6%, 69.8%] | 28.3% | 0.358 [0.334, 0.380] | 0.926 | 0.222 | 0.417 | 0.478 | 0.348 | 50/340 | 690 | 0 | 8 | 147M |  |
| betterleaks | **1862** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/340 | 0 | 0 | 0 | - |  |
| gitleaks | **1862** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/340 | 0 | 0 | 0 | - |  |
| rules-ru | **1862** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 55/340 | 1387 | 0 | 0 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: gliner25-fastino ≈ gliner-multi-v21; gliner-multi-v21 ≈ pplx; pplx ≈ nym-base; nym-base ≈ nuner-zero; nuner-zero ≈ gliner-multi-v21-ru; gliner-multi-v21-ru ≈ gliner25-fastino-ru; gliner25-fastino-ru ≈ ner-ru-yqelz; ner-ru-yqelz ≈ opf-ru; opf-ru ≈ mmbert32k; mmbert32k ≈ davlan-xlmr; davlan-xlmr ≈ gliner2-vladlinv; gliner2-vladlinv ≈ bardsai-eu; bardsai-eu ≈ gliner2-vladlinv-ru; gliner2-vladlinv-ru ≈ fef2-secret-ru; fef2-secret-ru ≈ davlan-mbert; davlan-mbert ≈ ru-legal-ner; ru-legal-ner ≈ ner-ru-gherman; ner-ru-gherman ≈ ru-pii-ner; ru-pii-ner ≈ stanza-ru; gliner-urchade ≈ traciora; apararti ≈ openmed-nemotron; openmed-nemotron ≈ gliner2-hivetrace-omni-ru; gliner2-hivetrace-omni-ru ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ opf-ru-v2; opf-ru-v2 ≈ gliner2-large; gliner2-large ≈ gliner2-fastino; gliner2-fastino ≈ pii-shield-onnx; pii-shield-onnx ≈ openai-base; openai-base ≈ gliner2-fastino-ru; gliner2-fastino-ru ≈ gliner-nvidia; gliner-nvidia ≈ spacy-ru-lg; spacy-ru-lg ≈ opf-kz-ru; opf-kz-ru ≈ gliner-nvidia-ru; gliner-nvidia-ru ≈ openmed-multilingual; openmed-multilingual ≈ natasha; natasha ≈ gliner-stream-pii; gliner-stream-pii ≈ kalyan-ettin; kalyan-ettin ≈ gliner2-hivetrace-uni; gliner2-hivetrace-uni ≈ gliner-pii-edge; gravitee-small ≈ gliner-pii-base; betterleaks ≈ gitleaks; gitleaks ≈ rules-ru

Legacy runs on this set: betterleaks. Their meta carries no `protocol` and no `bench_sha256`, so the version of the text they were taken from is confirmed only by the row and character counts, not by a fingerprint.

## Missed by group

| model | PERSON | ADDRESS |
|---|---|---|
| spans in gold | 987 | 875 |
| spacy-alrosait | 1 (0.1%) | 0 (0.0%) |
| gliner25-fastino | 6 (0.6%) | 2 (0.2%) |
| gliner-multi-v21 | 1 (0.1%) | 8 (0.9%) |
| pplx | 5 (0.5%) | 5 (0.6%) |
| nym-base | 11 (1.1%) | 1 (0.1%) |
| nuner-zero | 9 (0.9%) | 3 (0.3%) |
| gliner-multi-v21-ru | 11 (1.1%) | 4 (0.5%) |
| gliner25-fastino-ru | 14 (1.4%) | 4 (0.5%) |
| ner-ru-yqelz | 13 (1.3%) | 7 (0.8%) |
| opf-ru | 17 (1.7%) | 5 (0.6%) |
| mmbert32k | 25 (2.5%) | 8 (0.9%) |
| davlan-xlmr | 19 (1.9%) | 16 (1.8%) |
| gliner2-vladlinv | 7 (0.7%) | 46 (5.3%) |
| bardsai-eu | 20 (2.0%) | 34 (3.9%) |
| gliner2-vladlinv-ru | 8 (0.8%) | 49 (5.6%) |
| fef2-secret-ru | 12 (1.2%) | 52 (5.9%) |
| davlan-mbert | 24 (2.4%) | 43 (4.9%) |
| ru-legal-ner | 12 (1.2%) | 57 (6.5%) |
| ner-ru-gherman | 24 (2.4%) | 47 (5.4%) |
| ru-pii-ner | 6 (0.6%) | 69 (7.9%) |
| stanza-ru | 21 (2.1%) | 57 (6.5%) |
| gliner-urchade | 1 (0.1%) | 140 (16.0%) |
| traciora | 73 (7.4%) | 71 (8.1%) |
| apararti | 117 (11.9%) | 76 (8.7%) |
| openmed-nemotron | 102 (10.3%) | 91 (10.4%) |
| gliner2-hivetrace-omni-ru | 1 (0.1%) | 194 (22.2%) |
| gliner2-hivetrace-omni | 1 (0.1%) | 197 (22.5%) |
| opf-ru-v2 | 120 (12.2%) | 83 (9.5%) |
| gliner2-large | 177 (17.9%) | 48 (5.5%) |
| gliner2-fastino | 3 (0.3%) | 225 (25.7%) |
| pii-shield-onnx | 72 (7.3%) | 161 (18.4%) |
| openai-base | 159 (16.1%) | 80 (9.1%) |
| gliner2-fastino-ru | 9 (0.9%) | 239 (27.3%) |
| gliner-nvidia | 79 (8.0%) | 183 (20.9%) |
| spacy-ru-lg | 19 (1.9%) | 248 (28.3%) |
| opf-kz-ru | 199 (20.2%) | 81 (9.3%) |
| gliner-nvidia-ru | 137 (13.9%) | 180 (20.6%) |
| openmed-multilingual | 313 (31.7%) | 50 (5.7%) |
| natasha | 41 (4.2%) | 348 (39.8%) |
| gliner-stream-pii | 175 (17.7%) | 246 (28.1%) |
| kalyan-ettin | 100 (10.1%) | 369 (42.2%) |
| gliner2-hivetrace-uni | 137 (13.9%) | 365 (41.7%) |
| gliner-pii-edge | 102 (10.3%) | 406 (46.4%) |
| gravitee-small | 559 (56.6%) | 72 (8.2%) |
| gliner-pii-base | 117 (11.9%) | 527 (60.2%) |
| gliner-urchade-ru | 822 (83.3%) | 152 (17.4%) |
| gliner2-hivetrace-uni-ru | 476 (48.2%) | 782 (89.4%) |
| betterleaks | 987 (100.0%) | 875 (100.0%) |
| gitleaks | 987 (100.0%) | 875 (100.0%) |
| rules-ru | 987 (100.0%) | 875 (100.0%) |

## Char recall by gold type

| type | group | spacy-alrosait | gliner25-fastino | gliner-multi-v21 | pplx | nym-base | nuner-zero | gliner-multi-v21-ru | gliner25-fastino-ru | ner-ru-yqelz | opf-ru | mmbert32k | davlan-xlmr | gliner2-vladlinv | bardsai-eu | gliner2-vladlinv-ru | fef2-secret-ru | davlan-mbert | ru-legal-ner | ner-ru-gherman | ru-pii-ner | stanza-ru | gliner-urchade | traciora | apararti | openmed-nemotron | gliner2-hivetrace-omni-ru | gliner2-hivetrace-omni | opf-ru-v2 | gliner2-large | gliner2-fastino | pii-shield-onnx | openai-base | gliner2-fastino-ru | gliner-nvidia | spacy-ru-lg | opf-kz-ru | gliner-nvidia-ru | openmed-multilingual | natasha | gliner-stream-pii | kalyan-ettin | gliner2-hivetrace-uni | gliner-pii-edge | gravitee-small | gliner-pii-base | gliner-urchade-ru | gliner2-hivetrace-uni-ru | betterleaks | gitleaks | rules-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADDRESS | ADDRESS | 1.000 | 0.911 | 0.779 | 0.990 | 0.873 | 0.899 | 0.790 | 0.914 | 0.483 | 0.743 | 0.689 | 0.732 | 0.910 | 0.840 | 0.908 | 0.549 | 0.605 | 0.809 | 0.652 | 0.925 | 0.528 | 0.750 | 0.888 | 0.837 | 0.560 | 0.578 | 0.575 | 0.838 | 0.657 | 0.549 | 0.661 | 0.875 | 0.543 | 0.658 | 0.317 | 0.655 | 0.644 | 0.479 | 0.243 | 0.512 | 0.274 | 0.369 | 0.362 | 0.870 | 0.239 | 0.739 | 0.043 | 0.000 | 0.000 | 0.000 |
| NAME | PERSON | 0.999 | 0.987 | 0.998 | 0.995 | 0.936 | 0.989 | 0.987 | 0.974 | 0.984 | 0.891 | 0.897 | 0.975 | 0.988 | 0.970 | 0.987 | 0.985 | 0.966 | 0.991 | 0.887 | 0.996 | 0.977 | 0.998 | 0.900 | 0.845 | 0.778 | 0.996 | 0.997 | 0.842 | 0.751 | 0.993 | 0.898 | 0.828 | 0.985 | 0.798 | 0.944 | 0.778 | 0.646 | 0.506 | 0.953 | 0.698 | 0.732 | 0.815 | 0.824 | 0.416 | 0.818 | 0.153 | 0.477 | 0.000 | 0.000 | 0.000 |

## char F1 by domain

| domain | n | spacy-alrosait | gliner25-fastino | gliner-multi-v21 | pplx | nym-base | nuner-zero | gliner-multi-v21-ru | gliner25-fastino-ru | ner-ru-yqelz | opf-ru | mmbert32k | davlan-xlmr | gliner2-vladlinv | bardsai-eu | gliner2-vladlinv-ru | fef2-secret-ru | davlan-mbert | ru-legal-ner | ner-ru-gherman | ru-pii-ner | stanza-ru | gliner-urchade | traciora | apararti | openmed-nemotron | gliner2-hivetrace-omni-ru | gliner2-hivetrace-omni | opf-ru-v2 | gliner2-large | gliner2-fastino | pii-shield-onnx | openai-base | gliner2-fastino-ru | gliner-nvidia | spacy-ru-lg | opf-kz-ru | gliner-nvidia-ru | openmed-multilingual | natasha | gliner-stream-pii | kalyan-ettin | gliner2-hivetrace-uni | gliner-pii-edge | gravitee-small | gliner-pii-base | gliner-urchade-ru | gliner2-hivetrace-uni-ru | betterleaks | gitleaks | rules-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADDRESS | 34 | 0.992 | 0.927 | 0.900 | 0.928 | 0.910 | 0.886 | 0.893 | 0.935 | 0.667 | 0.838 | 0.854 | 0.821 | 0.968 | 0.855 | 0.973 | 0.693 | 0.685 | 0.825 | 0.720 | 0.908 | 0.657 | 0.916 | 0.867 | 0.835 | 0.645 | 0.884 | 0.866 | 0.800 | 0.801 | 0.812 | 0.736 | 0.868 | 0.817 | 0.881 | 0.445 | 0.761 | 0.793 | 0.551 | 0.387 | 0.724 | 0.444 | 0.550 | 0.670 | 0.766 | 0.484 | 0.975 | 0.095 | 0.000 | 0.000 | 0.000 |
| AUTO | 138 | 1.000 | 0.896 | 0.833 | 0.969 | 0.908 | 0.873 | 0.876 | 0.928 | 0.774 | 0.846 | 0.833 | 0.897 | 0.980 | 0.905 | 0.982 | 0.836 | 0.825 | 0.922 | 0.855 | 0.986 | 0.759 | 0.830 | 0.879 | 0.830 | 0.606 | 0.810 | 0.778 | 0.875 | 0.731 | 0.757 | 0.886 | 0.837 | 0.806 | 0.731 | 0.726 | 0.792 | 0.699 | 0.557 | 0.678 | 0.674 | 0.583 | 0.653 | 0.611 | 0.625 | 0.571 | 0.621 | 0.375 | 0.000 | 0.000 | 0.000 |
| BANK | 134 | 1.000 | 0.891 | 0.857 | 0.969 | 0.932 | 0.892 | 0.887 | 0.922 | 0.796 | 0.863 | 0.868 | 0.894 | 0.980 | 0.907 | 0.978 | 0.850 | 0.826 | 0.919 | 0.851 | 0.976 | 0.758 | 0.854 | 0.883 | 0.849 | 0.683 | 0.798 | 0.777 | 0.885 | 0.755 | 0.761 | 0.836 | 0.869 | 0.802 | 0.765 | 0.728 | 0.786 | 0.800 | 0.621 | 0.680 | 0.700 | 0.595 | 0.716 | 0.653 | 0.657 | 0.619 | 0.650 | 0.433 | 0.000 | 0.000 | 0.000 |
| DELIVERY | 175 | 0.999 | 0.901 | 0.850 | 0.948 | 0.913 | 0.863 | 0.888 | 0.925 | 0.810 | 0.839 | 0.842 | 0.891 | 0.962 | 0.905 | 0.969 | 0.816 | 0.849 | 0.876 | 0.865 | 0.937 | 0.736 | 0.833 | 0.882 | 0.874 | 0.711 | 0.768 | 0.761 | 0.904 | 0.699 | 0.744 | 0.839 | 0.872 | 0.795 | 0.792 | 0.737 | 0.793 | 0.735 | 0.652 | 0.697 | 0.703 | 0.615 | 0.680 | 0.663 | 0.681 | 0.655 | 0.597 | 0.282 | 0.000 | 0.000 | 0.000 |
| DIALOG | 207 | 0.997 | 0.860 | 0.766 | 0.881 | 0.916 | 0.854 | 0.805 | 0.944 | 0.791 | 0.837 | 0.831 | 0.879 | 0.954 | 0.892 | 0.951 | 0.770 | 0.842 | 0.852 | 0.820 | 0.925 | 0.761 | 0.877 | 0.854 | 0.844 | 0.573 | 0.845 | 0.839 | 0.899 | 0.671 | 0.800 | 0.765 | 0.827 | 0.847 | 0.742 | 0.685 | 0.801 | 0.808 | 0.569 | 0.671 | 0.653 | 0.523 | 0.721 | 0.595 | 0.588 | 0.642 | 0.708 | 0.408 | 0.000 | 0.000 | 0.000 |
| GOV | 114 | 1.000 | 0.893 | 0.844 | 0.957 | 0.901 | 0.906 | 0.868 | 0.921 | 0.769 | 0.836 | 0.838 | 0.879 | 0.935 | 0.892 | 0.937 | 0.819 | 0.838 | 0.888 | 0.846 | 0.955 | 0.783 | 0.851 | 0.877 | 0.859 | 0.640 | 0.772 | 0.770 | 0.874 | 0.735 | 0.748 | 0.871 | 0.865 | 0.785 | 0.778 | 0.713 | 0.791 | 0.754 | 0.614 | 0.684 | 0.728 | 0.611 | 0.708 | 0.659 | 0.689 | 0.642 | 0.616 | 0.316 | 0.000 | 0.000 | 0.000 |
| HR | 115 | 0.998 | 0.888 | 0.837 | 0.934 | 0.908 | 0.845 | 0.880 | 0.904 | 0.800 | 0.822 | 0.842 | 0.886 | 0.956 | 0.877 | 0.956 | 0.810 | 0.817 | 0.872 | 0.822 | 0.939 | 0.753 | 0.853 | 0.842 | 0.815 | 0.663 | 0.773 | 0.760 | 0.801 | 0.731 | 0.740 | 0.823 | 0.831 | 0.802 | 0.791 | 0.714 | 0.768 | 0.751 | 0.608 | 0.681 | 0.696 | 0.563 | 0.694 | 0.682 | 0.676 | 0.645 | 0.633 | 0.410 | 0.000 | 0.000 | 0.000 |
| LEGAL | 107 | 0.993 | 0.900 | 0.843 | 0.949 | 0.894 | 0.901 | 0.879 | 0.916 | 0.720 | 0.825 | 0.828 | 0.861 | 0.966 | 0.889 | 0.967 | 0.764 | 0.807 | 0.895 | 0.852 | 0.969 | 0.746 | 0.831 | 0.869 | 0.859 | 0.675 | 0.736 | 0.729 | 0.898 | 0.764 | 0.700 | 0.829 | 0.869 | 0.740 | 0.736 | 0.660 | 0.800 | 0.687 | 0.578 | 0.665 | 0.730 | 0.596 | 0.742 | 0.658 | 0.684 | 0.631 | 0.619 | 0.392 | 0.000 | 0.000 | 0.000 |
| MEDICAL | 96 | 1.000 | 0.902 | 0.835 | 0.954 | 0.909 | 0.888 | 0.866 | 0.927 | 0.735 | 0.829 | 0.830 | 0.874 | 0.956 | 0.888 | 0.967 | 0.829 | 0.834 | 0.889 | 0.845 | 0.953 | 0.799 | 0.807 | 0.871 | 0.836 | 0.644 | 0.777 | 0.771 | 0.860 | 0.738 | 0.729 | 0.856 | 0.865 | 0.790 | 0.725 | 0.699 | 0.768 | 0.706 | 0.619 | 0.697 | 0.712 | 0.639 | 0.642 | 0.692 | 0.701 | 0.622 | 0.579 | 0.332 | 0.000 | 0.000 | 0.000 |
| NAME | 32 | 1.000 | 0.902 | 0.924 | 0.979 | 0.953 | 0.914 | 0.927 | 0.902 | 0.986 | 0.953 | 0.942 | 0.980 | 0.965 | 0.967 | 0.965 | 0.987 | 0.975 | 0.961 | 0.936 | 0.983 | 0.944 | 0.953 | 0.925 | 0.884 | 0.673 | 0.948 | 0.951 | 0.844 | 0.725 | 0.884 | 0.959 | 0.842 | 0.922 | 0.793 | 0.978 | 0.822 | 0.640 | 0.678 | 0.963 | 0.854 | 0.861 | 0.852 | 0.884 | 0.518 | 0.833 | 0.283 | 0.584 | 0.000 | 0.000 | 0.000 |
| RE | 91 | 1.000 | 0.899 | 0.845 | 0.914 | 0.911 | 0.882 | 0.868 | 0.941 | 0.769 | 0.825 | 0.857 | 0.874 | 0.932 | 0.910 | 0.935 | 0.803 | 0.819 | 0.900 | 0.830 | 0.951 | 0.770 | 0.825 | 0.842 | 0.824 | 0.657 | 0.757 | 0.753 | 0.856 | 0.737 | 0.748 | 0.813 | 0.837 | 0.793 | 0.761 | 0.703 | 0.711 | 0.730 | 0.592 | 0.650 | 0.679 | 0.585 | 0.727 | 0.598 | 0.697 | 0.571 | 0.617 | 0.315 | 0.000 | 0.000 | 0.000 |
| SOCIAL | 119 | 1.000 | 0.880 | 0.852 | 0.932 | 0.890 | 0.858 | 0.881 | 0.907 | 0.744 | 0.816 | 0.850 | 0.865 | 0.951 | 0.889 | 0.945 | 0.798 | 0.821 | 0.902 | 0.814 | 0.957 | 0.745 | 0.880 | 0.859 | 0.850 | 0.647 | 0.774 | 0.767 | 0.870 | 0.698 | 0.751 | 0.858 | 0.851 | 0.805 | 0.788 | 0.683 | 0.776 | 0.748 | 0.595 | 0.626 | 0.665 | 0.593 | 0.660 | 0.639 | 0.721 | 0.586 | 0.687 | 0.259 | 0.000 | 0.000 | 0.000 |
| TELECOM | 138 | 0.999 | 0.885 | 0.813 | 0.950 | 0.910 | 0.860 | 0.852 | 0.902 | 0.804 | 0.848 | 0.835 | 0.899 | 0.942 | 0.903 | 0.943 | 0.813 | 0.832 | 0.867 | 0.833 | 0.943 | 0.766 | 0.833 | 0.839 | 0.828 | 0.648 | 0.801 | 0.775 | 0.857 | 0.707 | 0.754 | 0.811 | 0.836 | 0.813 | 0.750 | 0.712 | 0.751 | 0.753 | 0.623 | 0.697 | 0.719 | 0.565 | 0.734 | 0.639 | 0.658 | 0.611 | 0.636 | 0.374 | 0.000 | 0.000 | 0.000 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| gliner25-fastino | 8 (0.4%) | 6 (0.3%) | 5 (0.3%) | 5 (0.3%) |
| gliner-multi-v21 | 9 (0.5%) | 1 (0.1%) | 1 (0.1%) | 1 (0.1%) |
| nym-base | 12 (0.6%) | 12 (0.6%) | 12 (0.6%) | 12 (0.6%) |
| nuner-zero | 12 (0.6%) | 5 (0.3%) | 4 (0.2%) | 4 (0.2%) |
| gliner-multi-v21-ru | 15 (0.8%) | 2 (0.1%) | 1 (0.1%) | 1 (0.1%) |
| gliner25-fastino-ru | 18 (1.0%) | 13 (0.7%) | 13 (0.7%) | 12 (0.6%) |
| ner-ru-yqelz | 20 (1.1%) | 13 (0.7%) | 13 (0.7%) | 13 (0.7%) |
| opf-ru | 22 (1.2%) | 21 (1.1%) | 21 (1.1%) | 21 (1.1%) |
| mmbert32k | 33 (1.8%) | 11 (0.6%) | 10 (0.5%) | 9 (0.5%) |
| davlan-xlmr | 35 (1.9%) | 32 (1.7%) | 32 (1.7%) | 32 (1.7%) |
| gliner2-vladlinv | 53 (2.8%) | 43 (2.3%) | 42 (2.3%) | 39 (2.1%) |
| bardsai-eu | 54 (2.9%) | 48 (2.6%) | 48 (2.6%) | 48 (2.6%) |
| gliner2-vladlinv-ru | 57 (3.1%) | 48 (2.6%) | 45 (2.4%) | 43 (2.3%) |
| fef2-secret-ru | 64 (3.4%) | 39 (2.1%) | 37 (2.0%) | 37 (2.0%) |
| davlan-mbert | 67 (3.6%) | 63 (3.4%) | 63 (3.4%) | 63 (3.4%) |
| ru-legal-ner | 69 (3.7%) | 34 (1.8%) | 29 (1.6%) | 27 (1.5%) |
| ner-ru-gherman | 71 (3.8%) | 62 (3.3%) | 62 (3.3%) | 62 (3.3%) |
| gliner-urchade | 141 (7.6%) | 112 (6.0%) | 90 (4.8%) | 59 (3.2%) |
| traciora | 144 (7.7%) | 144 (7.7%) | 144 (7.7%) | 144 (7.7%) |
| apararti | 193 (10.4%) | 186 (10.0%) | 185 (9.9%) | 185 (9.9%) |
| openmed-nemotron | 193 (10.4%) | 136 (7.3%) | 135 (7.3%) | 135 (7.3%) |
| gliner2-hivetrace-omni-ru | 195 (10.5%) | 171 (9.2%) | 156 (8.4%) | 142 (7.6%) |
| gliner2-hivetrace-omni | 198 (10.6%) | 175 (9.4%) | 158 (8.5%) | 139 (7.5%) |
| opf-ru-v2 | 203 (10.9%) | 202 (10.8%) | 201 (10.8%) | 201 (10.8%) |
| gliner2-large | 225 (12.1%) | 144 (7.7%) | 121 (6.5%) | 82 (4.4%) |
| gliner2-fastino | 228 (12.2%) | 207 (11.1%) | 191 (10.3%) | 172 (9.2%) |
| pii-shield-onnx | 233 (12.5%) | 147 (7.9%) | 133 (7.1%) | 132 (7.1%) |
| openai-base | 239 (12.8%) | 238 (12.8%) | 238 (12.8%) | 238 (12.8%) |
| gliner2-fastino-ru | 248 (13.3%) | 224 (12.0%) | 210 (11.3%) | 183 (9.8%) |
| gliner-nvidia | 262 (14.1%) | 177 (9.5%) | 152 (8.2%) | 140 (7.5%) |
| opf-kz-ru | 280 (15.0%) | 276 (14.8%) | 276 (14.8%) | 276 (14.8%) |
| gliner-nvidia-ru | 317 (17.0%) | 195 (10.5%) | 159 (8.5%) | 133 (7.1%) |
| openmed-multilingual | 363 (19.5%) | 224 (12.0%) | 215 (11.5%) | 215 (11.5%) |
| gliner-stream-pii | 421 (22.6%) | 201 (10.8%) | 138 (7.4%) | 64 (3.4%) |
| kalyan-ettin | 469 (25.2%) | 339 (18.2%) | 320 (17.2%) | 319 (17.1%) |
| gliner2-hivetrace-uni | 502 (27.0%) | 226 (12.1%) | 107 (5.7%) | 42 (2.3%) |
| gliner-pii-edge | 508 (27.3%) | 35 (1.9%) | 4 (0.2%) | 1 (0.1%) |
| gravitee-small | 631 (33.9%) | 597 (32.1%) | 597 (32.1%) | 597 (32.1%) |
| gliner-pii-base | 644 (34.6%) | 103 (5.5%) | 24 (1.3%) | 1 (0.1%) |
| gliner-urchade-ru | 974 (52.3%) | 758 (40.7%) | 625 (33.6%) | 384 (20.6%) |
| gliner2-hivetrace-uni-ru | 1258 (67.6%) | 757 (40.7%) | 494 (26.5%) | 202 (10.8%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
