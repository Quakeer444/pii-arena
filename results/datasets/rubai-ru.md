# rubai-ru - ru / pii (1500 rows, 3458 spans, 0 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.257 (74.3% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pplx | **16** | 0.5% [0.2%, 0.7%] | 10.7% | 0.941 [0.939, 0.944] | 0.924 | 0.960 | 0.082 | 0.878 | 0.931 | 0/0 | 0 | 0 | 54 | 596M |  |
| nym-base | **56** | 1.6% [1.2%, 2.1%] | 5.3% | 0.730 [0.724, 0.736] | 0.936 | 0.598 | 0.034 | 0.934 | 0.100 | 0/0 | 0 | 0 | 3 | 308M |  |
| mmbert32k | **56** | 1.6% [1.2%, 2.1%] | 5.7% | 0.651 [0.643, 0.657] | 0.911 | 0.506 | 0.026 | 0.894 | 0.289 | 0/0 | 0 | 0 | 4 | 308M |  |
| nym-small | **60** | 1.7% [1.3%, 2.2%] | 5.0% | 0.716 [0.710, 0.723] | 0.953 | 0.574 | 0.030 | 0.942 | 0.095 | 0/0 | 0 | 0 | 42 | - |  |
| gliner25-fastino | **71** | 2.1% [1.6%, 2.6%] | 7.9% | 0.957 [0.955, 0.960] | 0.962 | 0.952 | 0.059 | 0.943 | 0.874 | 0/0 | 0 | 0 | 2 | 287M |  |
| gliner25-fastino-ru | **75** | 2.2% [1.7%, 2.7%] | 7.9% | 0.961 [0.959, 0.964] | 0.972 | 0.951 | 0.061 | 0.958 | 0.912 | 0/0 | 0 | 0 | 8 | 287M |  |
| opf-ru | **83** | 2.4% [1.9%, 3.0%] | 5.6% | 0.639 [0.633, 0.647] | 0.900 | 0.496 | 0.028 | 0.897 | 0.442 | 0/0 | 0 | 0 | 34 | 1.4B |  |
| traciora | **142** | 4.1% [3.5%, 4.8%] | 7.1% | 0.924 [0.921, 0.928] | 0.934 | 0.915 | 0.041 | 0.919 | 0.878 | 0/0 | 0 | 0 | 232 | 1.4B |  |
| nuner-zero | **160** | 4.6% [4.0%, 5.3%] | 7.5% | 0.894 [0.889, 0.899] | 0.922 | 0.868 | 0.045 | 0.859 | 0.794 | 0/0 | 0 | 0 | 10 | 449M |  |
| apararti | **175** | 5.1% [4.4%, 5.8%] | 5.8% | 0.928 [0.924, 0.931] | 0.941 | 0.915 | 0.040 | 0.929 | 0.819 | 0/0 | 0 | 0 | 59 | 1.4B |  |
| ru-pii-ner | **177** | 5.1% [4.4%, 5.8%] | 8.0% | 0.923 [0.918, 0.928] | 0.942 | 0.905 | 0.061 | 0.877 | 0.477 | 0/0 | 0 | 0 | 63 | 358M |  |
| bardsai-eu | **179** | 5.2% [4.5%, 5.9%] | 18.2% | 0.783 [0.775, 0.791] | 0.939 | 0.671 | 0.136 | 0.913 | 0.479 | 0/0 | 0 | 0 | 294 | - |  |
| opf-ru-v2 | **189** | 5.5% [4.7%, 6.3%] | 5.4% | 0.919 [0.915, 0.923] | 0.952 | 0.888 | 0.036 | 0.932 | 0.851 | 0/0 | 0 | 0 | 437 | 1.4B |  |
| openai-base | **236** | 6.8% [6.0%, 7.7%] | 26.2% | 0.924 [0.919, 0.928] | 0.933 | 0.915 | 0.203 | 0.928 | 0.849 | 0/0 | 0 | 0 | 72 | 1.4B |  |
| opf-kz-ru | **242** | 7.0% [6.2%, 7.9%] | 4.2% | 0.915 [0.910, 0.919] | 0.931 | 0.899 | 0.026 | 0.904 | 0.774 | 0/0 | 0 | 0 | 55 | 1.4B |  |
| openmed-multilingual | **251** | 7.3% [6.4%, 8.1%] | 4.0% | 0.633 [0.625, 0.640] | 0.941 | 0.477 | 0.029 | 0.883 | 0.566 | 0/0 | 0 | 0 | 29 | 1.4B |  |
| ru-legal-ner | **347** | 10.0% [9.1%, 11.1%] | 6.7% | 0.697 [0.689, 0.704] | 0.855 | 0.588 | 0.032 | 0.773 | 0.491 | 0/0 | 0 | 0 | 3 | 29M |  |
| gliner2-large | **360** | 10.4% [9.5%, 11.3%] | 6.4% | 0.750 [0.742, 0.759] | 0.887 | 0.650 | 0.035 | 0.805 | 0.652 | 0/0 | 0 | 0 | 8 | 486M |  |
| pii-shield-onnx | **405** | 11.7% [10.6%, 12.8%] | 5.1% | 0.845 [0.840, 0.850] | 0.959 | 0.755 | 0.030 | 0.888 | 0.745 | 0/0 | 0 | 0 | 66 | - |  |
| gliner-multi-v21 | **470** | 13.6% [12.6%, 14.6%] | 6.0% | 0.760 [0.753, 0.768] | 0.938 | 0.639 | 0.032 | 0.814 | 0.627 | 0/0 | 0 | 0 | 3 | 289M |  |
| gliner-stream-pii | **490** | 14.2% [13.1%, 15.3%] | 4.2% | 0.777 [0.769, 0.784] | 0.969 | 0.648 | 0.035 | 0.884 | 0.749 | 0/0 | 0 | 0 | 41 | 677M |  |
| openmed-nemotron | **537** | 15.5% [14.4%, 16.7%] | 2.9% | 0.664 [0.656, 0.672] | 0.789 | 0.574 | 0.016 | 0.681 | 0.612 | 0/0 | 0 | 0 | 31 | 1.4B |  |
| gliner-multi-v21-ru | **586** | 16.9% [15.8%, 18.0%] | 5.6% | 0.781 [0.774, 0.788] | 0.954 | 0.662 | 0.029 | 0.827 | 0.662 | 0/0 | 0 | 0 | 10 | 289M |  |
| gliner-nvidia | **679** | 19.6% [18.4%, 20.8%] | 7.2% | 0.764 [0.751, 0.776] | 0.934 | 0.646 | 0.062 | 0.819 | 0.718 | 0/0 | 0 | 0 | 8 | 445M |  |
| gliner2-vladlinv | **685** | 19.8% [18.4%, 21.3%] | 6.8% | 0.861 [0.851, 0.869] | 0.966 | 0.776 | 0.061 | 0.857 | 0.784 | 0/0 | 0 | 0 | 3 | 287M |  |
| gliner-urchade | **744** | 21.5% [20.3%, 22.9%] | 7.2% | 0.748 [0.736, 0.761] | 0.908 | 0.637 | 0.049 | 0.722 | 0.684 | 0/0 | 0 | 0 | 3 | 289M |  |
| gliner2-vladlinv-ru | **795** | 23.0% [21.6%, 24.5%] | 6.6% | 0.850 [0.840, 0.859] | 0.969 | 0.757 | 0.060 | 0.842 | 0.839 | 0/0 | 0 | 0 | 7 | 287M |  |
| gliner-nvidia-ru | **827** | 23.9% [22.5%, 25.3%] | 6.0% | 0.743 [0.729, 0.757] | 0.953 | 0.609 | 0.061 | 0.824 | 0.737 | 0/0 | 0 | 0 | 30 | 445M |  |
| gliner-pii-edge | **846** | 24.5% [23.0%, 25.8%] | 6.3% | 0.661 [0.649, 0.674] | 0.900 | 0.523 | 0.046 | 0.737 | 0.420 | 0/0 | 0 | 0 | 3 | 45M |  |
| gliner2-hivetrace-omni | **879** | 25.4% [24.1%, 26.7%] | 7.3% | 0.653 [0.639, 0.668] | 0.899 | 0.513 | 0.060 | 0.768 | 0.573 | 0/0 | 0 | 0 | 5 | 307M |  |
| fef2-secret-ru | **930** | 26.9% [25.5%, 28.3%] | 5.8% | 0.430 [0.420, 0.440] | 0.878 | 0.285 | 0.048 | 0.793 | 0.247 | 0/0 | 0 | 0 | 3 | 177M |  |
| gliner2-hivetrace-omni-ru | **967** | 28.0% [26.7%, 29.3%] | 7.2% | 0.637 [0.623, 0.651] | 0.898 | 0.494 | 0.062 | 0.764 | 0.593 | 0/0 | 0 | 0 | 3 | 307M |  |
| gliner2-fastino | **1059** | 30.6% [29.2%, 32.1%] | 7.3% | 0.633 [0.617, 0.648] | 0.927 | 0.480 | 0.065 | 0.766 | 0.581 | 0/0 | 0 | 0 | 4 | 307M |  |
| gliner2-fastino-ru | **1087** | 31.4% [30.0%, 32.9%] | 7.2% | 0.635 [0.619, 0.651] | 0.959 | 0.474 | 0.070 | 0.789 | 0.624 | 0/0 | 0 | 0 | 6 | 307M |  |
| gliner-urchade-ru | **1112** | 32.2% [30.6%, 33.7%] | 3.1% | 0.732 [0.718, 0.746] | 0.950 | 0.595 | 0.029 | 0.771 | 0.700 | 0/0 | 0 | 0 | 8 | 289M |  |
| kalyan-ettin | **1206** | 34.9% [33.3%, 36.4%] | 2.7% | 0.446 [0.434, 0.459] | 0.860 | 0.301 | 0.023 | 0.701 | 0.387 | 0/0 | 0 | 0 | 12 | 68M |  |
| gliner-pii-base | **1252** | 36.2% [34.7%, 37.6%] | 6.1% | 0.534 [0.521, 0.547] | 0.904 | 0.379 | 0.053 | 0.681 | 0.428 | 0/0 | 0 | 0 | 4 | 166M |  |
| stanza-ru | **1308** | 37.8% [36.8%, 38.8%] | 5.4% | 0.348 [0.341, 0.355] | 0.679 | 0.234 | 0.043 | 0.598 | 0.087 | 0/0 | 0 | 0 | 35 | - |  |
| gravitee-small | **1329** | 38.4% [36.9%, 39.9%] | 3.6% | 0.595 [0.584, 0.606] | 0.824 | 0.465 | 0.007 | 0.700 | 0.523 | 0/0 | 0 | 0 | 6 | 29M |  |
| ner-ru-yqelz | **1512** | 43.7% [42.6%, 44.8%] | 4.5% | 0.457 [0.450, 0.466] | 0.805 | 0.319 | 0.032 | 0.607 | 0.082 | 0/0 | 0 | 0 | 4 | 559M |  |
| ner-ru-gherman | **1545** | 44.7% [43.7%, 45.6%] | 1.8% | 0.655 [0.647, 0.664] | 0.967 | 0.495 | 0.014 | 0.677 | 0.168 | 0/0 | 0 | 0 | 4 | 177M |  |
| davlan-xlmr | **1549** | 44.8% [43.8%, 45.7%] | 4.5% | 0.417 [0.409, 0.425] | 0.901 | 0.272 | 0.041 | 0.669 | 0.088 | 0/0 | 0 | 0 | 3 | 277M |  |
| davlan-mbert | **1552** | 44.9% [43.9%, 45.9%] | 4.0% | 0.408 [0.400, 0.415] | 0.888 | 0.264 | 0.038 | 0.649 | 0.088 | 0/0 | 0 | 0 | 3 | 177M |  |
| natasha | **1601** | 46.3% [45.2%, 47.4%] | 4.3% | 0.300 [0.292, 0.307] | 0.795 | 0.185 | 0.043 | 0.607 | 0.093 | 0/0 | 0 | 0 | 2 | - |  |
| spacy-ru-lg | **1647** | 47.6% [46.5%, 48.7%] | 4.0% | 0.300 [0.292, 0.308] | 0.853 | 0.182 | 0.039 | 0.643 | 0.093 | 0/0 | 0 | 0 | 4 | - |  |
| spacy-alrosait | **1714** | 49.6% [48.4%, 50.6%] | 2.7% | 0.628 [0.617, 0.639] | 0.971 | 0.464 | 0.030 | 0.658 | 0.531 | 0/0 | 0 | 0 | 4 | - |  |
| gliner2-hivetrace-uni | **1763** | 51.0% [49.4%, 52.6%] | 4.8% | 0.342 [0.331, 0.353] | 0.843 | 0.215 | 0.042 | 0.569 | 0.229 | 0/0 | 0 | 0 | 8 | 147M |  |
| gliner2-hivetrace-uni-ru | **2349** | 67.9% [66.5%, 69.4%] | 3.6% | 0.225 [0.215, 0.236] | 0.943 | 0.128 | 0.040 | 0.473 | 0.195 | 0/0 | 0 | 0 | 10 | 147M |  |
| rules-ru | **3339** | 96.6% [95.9%, 97.1%] | 0.2% | 0.051 [0.042, 0.060] | 1.000 | 0.026 | 0.003 | 0.067 | 0.051 | 0/0 | 0 | 0 | 0 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: nym-base ≈ mmbert32k; mmbert32k ≈ nym-small; nym-small ≈ gliner25-fastino; gliner25-fastino ≈ gliner25-fastino-ru; gliner25-fastino-ru ≈ opf-ru; traciora ≈ nuner-zero; nuner-zero ≈ apararti; apararti ≈ ru-pii-ner; ru-pii-ner ≈ bardsai-eu; bardsai-eu ≈ opf-ru-v2; openai-base ≈ opf-kz-ru; opf-kz-ru ≈ openmed-multilingual; ru-legal-ner ≈ gliner2-large; gliner2-large ≈ pii-shield-onnx; gliner-multi-v21 ≈ gliner-stream-pii; gliner-stream-pii ≈ openmed-nemotron; gliner-nvidia ≈ gliner2-vladlinv; gliner-urchade ≈ gliner2-vladlinv-ru; gliner2-vladlinv-ru ≈ gliner-nvidia-ru; gliner-nvidia-ru ≈ gliner-pii-edge; gliner-pii-edge ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ fef2-secret-ru; fef2-secret-ru ≈ gliner2-hivetrace-omni-ru; gliner2-fastino-ru ≈ gliner-urchade-ru; kalyan-ettin ≈ gliner-pii-base; gliner-pii-base ≈ stanza-ru; stanza-ru ≈ gravitee-small; ner-ru-gherman ≈ davlan-xlmr; davlan-xlmr ≈ davlan-mbert; spacy-alrosait ≈ gliner2-hivetrace-uni

## Missed by group

| model | PERSON | ADDRESS | CONTACT | ID |
|---|---|---|---|---|
| spans in gold | 430 | 1501 | 205 | 1322 |
| pplx | 5 (1.2%) | 2 (0.1%) | 1 (0.5%) | 8 (0.6%) |
| nym-base | 17 (4.0%) | 18 (1.2%) | 1 (0.5%) | 20 (1.5%) |
| mmbert32k | 12 (2.8%) | 3 (0.2%) | 1 (0.5%) | 40 (3.0%) |
| nym-small | 22 (5.1%) | 19 (1.3%) | 0 (0.0%) | 19 (1.4%) |
| gliner25-fastino | 6 (1.4%) | 4 (0.3%) | 1 (0.5%) | 60 (4.5%) |
| gliner25-fastino-ru | 7 (1.6%) | 6 (0.4%) | 1 (0.5%) | 61 (4.6%) |
| opf-ru | 23 (5.3%) | 10 (0.7%) | 0 (0.0%) | 50 (3.8%) |
| traciora | 92 (21.4%) | 5 (0.3%) | 3 (1.5%) | 42 (3.2%) |
| nuner-zero | 8 (1.9%) | 2 (0.1%) | 3 (1.5%) | 147 (11.1%) |
| apararti | 151 (35.1%) | 7 (0.5%) | 0 (0.0%) | 17 (1.3%) |
| ru-pii-ner | 10 (2.3%) | 154 (10.3%) | 2 (1.0%) | 11 (0.8%) |
| bardsai-eu | 12 (2.8%) | 18 (1.2%) | 4 (2.0%) | 145 (11.0%) |
| opf-ru-v2 | 137 (31.9%) | 25 (1.7%) | 1 (0.5%) | 26 (2.0%) |
| openai-base | 167 (38.8%) | 33 (2.2%) | 2 (1.0%) | 34 (2.6%) |
| opf-kz-ru | 199 (46.3%) | 25 (1.7%) | 0 (0.0%) | 18 (1.4%) |
| openmed-multilingual | 123 (28.6%) | 101 (6.7%) | 1 (0.5%) | 26 (2.0%) |
| ru-legal-ner | 7 (1.6%) | 85 (5.7%) | 11 (5.4%) | 244 (18.5%) |
| gliner2-large | 59 (13.7%) | 22 (1.5%) | 17 (8.3%) | 262 (19.8%) |
| pii-shield-onnx | 74 (17.2%) | 110 (7.3%) | 45 (22.0%) | 176 (13.3%) |
| gliner-multi-v21 | 11 (2.6%) | 4 (0.3%) | 6 (2.9%) | 449 (34.0%) |
| gliner-stream-pii | 143 (33.3%) | 188 (12.5%) | 55 (26.8%) | 104 (7.9%) |
| openmed-nemotron | 76 (17.7%) | 24 (1.6%) | 19 (9.3%) | 418 (31.6%) |
| gliner-multi-v21-ru | 18 (4.2%) | 4 (0.3%) | 7 (3.4%) | 557 (42.1%) |
| gliner-nvidia | 22 (5.1%) | 376 (25.0%) | 8 (3.9%) | 273 (20.7%) |
| gliner2-vladlinv | 15 (3.5%) | 256 (17.1%) | 8 (3.9%) | 406 (30.7%) |
| gliner-urchade | 7 (1.6%) | 376 (25.0%) | 1 (0.5%) | 360 (27.2%) |
| gliner2-vladlinv-ru | 15 (3.5%) | 250 (16.7%) | 15 (7.3%) | 515 (39.0%) |
| gliner-nvidia-ru | 28 (6.5%) | 384 (25.6%) | 10 (4.9%) | 405 (30.6%) |
| gliner-pii-edge | 60 (14.0%) | 467 (31.1%) | 37 (18.0%) | 282 (21.3%) |
| gliner2-hivetrace-omni | 12 (2.8%) | 549 (36.6%) | 17 (8.3%) | 301 (22.8%) |
| fef2-secret-ru | 1 (0.2%) | 49 (3.3%) | 174 (84.9%) | 706 (53.4%) |
| gliner2-hivetrace-omni-ru | 11 (2.6%) | 557 (37.1%) | 17 (8.3%) | 382 (28.9%) |
| gliner2-fastino | 6 (1.4%) | 761 (50.7%) | 17 (8.3%) | 275 (20.8%) |
| gliner2-fastino-ru | 9 (2.1%) | 782 (52.1%) | 17 (8.3%) | 279 (21.1%) |
| gliner-urchade-ru | 357 (83.0%) | 369 (24.6%) | 2 (1.0%) | 384 (29.0%) |
| kalyan-ettin | 52 (12.1%) | 375 (25.0%) | 127 (62.0%) | 652 (49.3%) |
| gliner-pii-base | 54 (12.6%) | 838 (55.8%) | 40 (19.5%) | 320 (24.2%) |
| stanza-ru | 1 (0.2%) | 26 (1.7%) | 204 (99.5%) | 1077 (81.5%) |
| gravitee-small | 297 (69.1%) | 241 (16.1%) | 51 (24.9%) | 740 (56.0%) |
| ner-ru-yqelz | 11 (2.6%) | 33 (2.2%) | 198 (96.6%) | 1270 (96.1%) |
| ner-ru-gherman | 17 (4.0%) | 1 (0.1%) | 205 (100.0%) | 1322 (100.0%) |
| davlan-xlmr | 7 (1.6%) | 15 (1.0%) | 205 (100.0%) | 1322 (100.0%) |
| davlan-mbert | 5 (1.2%) | 20 (1.3%) | 205 (100.0%) | 1322 (100.0%) |
| natasha | 6 (1.4%) | 102 (6.8%) | 205 (100.0%) | 1288 (97.4%) |
| spacy-ru-lg | 11 (2.6%) | 110 (7.3%) | 205 (100.0%) | 1321 (99.9%) |
| spacy-alrosait | 104 (24.2%) | 162 (10.8%) | 183 (89.3%) | 1265 (95.7%) |
| gliner2-hivetrace-uni | 55 (12.8%) | 630 (42.0%) | 51 (24.9%) | 1027 (77.7%) |
| gliner2-hivetrace-uni-ru | 124 (28.8%) | 975 (65.0%) | 198 (96.6%) | 1052 (79.6%) |
| rules-ru | 430 (100.0%) | 1501 (100.0%) | 186 (90.7%) | 1222 (92.4%) |

## Char recall by gold type

| type | group | pplx | nym-base | mmbert32k | nym-small | gliner25-fastino | gliner25-fastino-ru | opf-ru | traciora | nuner-zero | apararti | ru-pii-ner | bardsai-eu | opf-ru-v2 | openai-base | opf-kz-ru | openmed-multilingual | ru-legal-ner | gliner2-large | pii-shield-onnx | gliner-multi-v21 | gliner-stream-pii | openmed-nemotron | gliner-multi-v21-ru | gliner-nvidia | gliner2-vladlinv | gliner-urchade | gliner2-vladlinv-ru | gliner-nvidia-ru | gliner-pii-edge | gliner2-hivetrace-omni | fef2-secret-ru | gliner2-hivetrace-omni-ru | gliner2-fastino | gliner2-fastino-ru | gliner-urchade-ru | kalyan-ettin | gliner-pii-base | stanza-ru | gravitee-small | ner-ru-yqelz | ner-ru-gherman | davlan-xlmr | davlan-mbert | natasha | spacy-ru-lg | spacy-alrosait | gliner2-hivetrace-uni | gliner2-hivetrace-uni-ru | rules-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADDRESS | ADDRESS | 0.967 | 0.402 | 0.316 | 0.368 | 0.966 | 0.965 | 0.325 | 0.953 | 0.902 | 0.932 | 0.882 | 0.629 | 0.906 | 0.941 | 0.917 | 0.261 | 0.495 | 0.622 | 0.728 | 0.614 | 0.665 | 0.581 | 0.680 | 0.598 | 0.809 | 0.595 | 0.813 | 0.586 | 0.422 | 0.397 | 0.210 | 0.393 | 0.332 | 0.324 | 0.606 | 0.223 | 0.191 | 0.243 | 0.514 | 0.410 | 0.712 | 0.343 | 0.332 | 0.198 | 0.201 | 0.637 | 0.162 | 0.086 | 0.000 |
| CARD_NUMBER | ID | 0.958 | 0.957 | 0.798 | 0.947 | 0.947 | 0.940 | 0.742 | 0.891 | 0.759 | 0.937 | 0.956 | 0.668 | 0.897 | 0.923 | 0.939 | 0.892 | 0.702 | 0.638 | 0.877 | 0.623 | 0.631 | 0.545 | 0.566 | 0.649 | 0.659 | 0.625 | 0.597 | 0.566 | 0.641 | 0.611 | 0.305 | 0.546 | 0.639 | 0.638 | 0.639 | 0.400 | 0.640 | 0.003 | 0.415 | 0.013 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.060 | 0.082 | 0.024 | 0.088 |
| DOCUMENT_ID | ID | 0.877 | 0.841 | 0.775 | 0.852 | 0.757 | 0.779 | 0.836 | 0.767 | 0.867 | 0.858 | 0.871 | 0.811 | 0.836 | 0.862 | 0.863 | 0.812 | 0.628 | 0.849 | 0.458 | 0.350 | 0.651 | 0.131 | 0.242 | 0.845 | 0.617 | 0.649 | 0.468 | 0.745 | 0.852 | 0.875 | 0.547 | 0.859 | 0.860 | 0.856 | 0.508 | 0.188 | 0.706 | 0.832 | 0.047 | 0.076 | 0.000 | 0.000 | 0.000 | 0.115 | 0.004 | 0.000 | 0.603 | 0.810 | 0.000 |
| NAME | PERSON | 0.941 | 0.804 | 0.868 | 0.787 | 0.940 | 0.938 | 0.846 | 0.736 | 0.941 | 0.676 | 0.930 | 0.921 | 0.696 | 0.653 | 0.569 | 0.592 | 0.943 | 0.794 | 0.719 | 0.939 | 0.641 | 0.748 | 0.932 | 0.879 | 0.928 | 0.941 | 0.928 | 0.801 | 0.773 | 0.937 | 0.926 | 0.938 | 0.943 | 0.939 | 0.175 | 0.774 | 0.847 | 0.941 | 0.294 | 0.936 | 0.843 | 0.938 | 0.932 | 0.935 | 0.911 | 0.796 | 0.864 | 0.716 | 0.000 |
| PHONE | CONTACT | 0.936 | 0.934 | 0.924 | 0.935 | 0.934 | 0.934 | 0.868 | 0.847 | 0.917 | 0.929 | 0.929 | 0.906 | 0.874 | 0.891 | 0.912 | 0.852 | 0.752 | 0.840 | 0.638 | 0.911 | 0.485 | 0.699 | 0.904 | 0.897 | 0.896 | 0.934 | 0.861 | 0.888 | 0.761 | 0.844 | 0.117 | 0.844 | 0.844 | 0.844 | 0.929 | 0.212 | 0.749 | 0.005 | 0.615 | 0.013 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.104 | 0.681 | 0.029 | 0.106 |

## char F1 by domain

| domain | n | pplx | nym-base | mmbert32k | nym-small | gliner25-fastino | gliner25-fastino-ru | opf-ru | traciora | nuner-zero | apararti | ru-pii-ner | bardsai-eu | opf-ru-v2 | openai-base | opf-kz-ru | openmed-multilingual | ru-legal-ner | gliner2-large | pii-shield-onnx | gliner-multi-v21 | gliner-stream-pii | openmed-nemotron | gliner-multi-v21-ru | gliner-nvidia | gliner2-vladlinv | gliner-urchade | gliner2-vladlinv-ru | gliner-nvidia-ru | gliner-pii-edge | gliner2-hivetrace-omni | fef2-secret-ru | gliner2-hivetrace-omni-ru | gliner2-fastino | gliner2-fastino-ru | gliner-urchade-ru | kalyan-ettin | gliner-pii-base | stanza-ru | gravitee-small | ner-ru-yqelz | ner-ru-gherman | davlan-xlmr | davlan-mbert | natasha | spacy-ru-lg | spacy-alrosait | gliner2-hivetrace-uni | gliner2-hivetrace-uni-ru | rules-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| artificial_intelligence | 1 | 1.000 | 1.000 | 0.941 | 1.000 | 1.000 | 1.000 | 0.542 | 0.622 | 1.000 | 1.000 | 1.000 | 1.000 | 0.769 | 0.897 | 0.667 | 1.000 | 0.172 | 0.667 | 0.207 | 1.000 | 0.968 | 0.203 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.727 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.914 | 0.000 | 0.459 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| general | 1499 | 0.941 | 0.730 | 0.650 | 0.716 | 0.957 | 0.961 | 0.640 | 0.924 | 0.894 | 0.928 | 0.923 | 0.783 | 0.919 | 0.924 | 0.915 | 0.633 | 0.697 | 0.750 | 0.845 | 0.760 | 0.777 | 0.664 | 0.781 | 0.764 | 0.861 | 0.748 | 0.850 | 0.743 | 0.661 | 0.653 | 0.430 | 0.637 | 0.632 | 0.635 | 0.732 | 0.446 | 0.534 | 0.348 | 0.595 | 0.457 | 0.655 | 0.417 | 0.408 | 0.300 | 0.300 | 0.628 | 0.342 | 0.225 | 0.051 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| nym-base | 56 (1.6%) | 46 (1.3%) | 46 (1.3%) | 46 (1.3%) |
| mmbert32k | 56 (1.6%) | 19 (0.5%) | 15 (0.4%) | 13 (0.4%) |
| nym-small | 60 (1.7%) | 54 (1.6%) | 54 (1.6%) | 54 (1.6%) |
| gliner25-fastino | 71 (2.1%) | 55 (1.6%) | 49 (1.4%) | 47 (1.4%) |
| gliner25-fastino-ru | 75 (2.2%) | 61 (1.8%) | 58 (1.7%) | 57 (1.6%) |
| opf-ru | 83 (2.4%) | 70 (2.0%) | 70 (2.0%) | 70 (2.0%) |
| traciora | 142 (4.1%) | 133 (3.8%) | 133 (3.8%) | 133 (3.8%) |
| nuner-zero | 160 (4.6%) | 124 (3.6%) | 105 (3.0%) | 78 (2.3%) |
| apararti | 175 (5.1%) | 173 (5.0%) | 173 (5.0%) | 173 (5.0%) |
| bardsai-eu | 179 (5.2%) | 63 (1.8%) | 61 (1.8%) | 61 (1.8%) |
| opf-ru-v2 | 189 (5.5%) | 186 (5.4%) | 186 (5.4%) | 186 (5.4%) |
| openai-base | 236 (6.8%) | 236 (6.8%) | 236 (6.8%) | 236 (6.8%) |
| opf-kz-ru | 242 (7.0%) | 240 (6.9%) | 240 (6.9%) | 240 (6.9%) |
| openmed-multilingual | 251 (7.3%) | 116 (3.4%) | 111 (3.2%) | 111 (3.2%) |
| ru-legal-ner | 347 (10.0%) | 28 (0.8%) | 21 (0.6%) | 20 (0.6%) |
| gliner2-large | 360 (10.4%) | 282 (8.2%) | 243 (7.0%) | 157 (4.5%) |
| pii-shield-onnx | 405 (11.7%) | 276 (8.0%) | 262 (7.6%) | 261 (7.5%) |
| gliner-multi-v21 | 470 (13.6%) | 306 (8.8%) | 278 (8.0%) | 260 (7.5%) |
| gliner-stream-pii | 490 (14.2%) | 298 (8.6%) | 209 (6.0%) | 128 (3.7%) |
| openmed-nemotron | 537 (15.5%) | 465 (13.4%) | 462 (13.4%) | 462 (13.4%) |
| gliner-multi-v21-ru | 586 (16.9%) | 347 (10.0%) | 284 (8.2%) | 259 (7.5%) |
| gliner-nvidia | 679 (19.6%) | 652 (18.9%) | 645 (18.7%) | 633 (18.3%) |
| gliner2-vladlinv | 685 (19.8%) | 652 (18.9%) | 633 (18.3%) | 604 (17.5%) |
| gliner-urchade | 744 (21.5%) | 629 (18.2%) | 577 (16.7%) | 526 (15.2%) |
| gliner2-vladlinv-ru | 795 (23.0%) | 754 (21.8%) | 730 (21.1%) | 708 (20.5%) |
| gliner-nvidia-ru | 827 (23.9%) | 772 (22.3%) | 748 (21.6%) | 716 (20.7%) |
| gliner-pii-edge | 846 (24.5%) | 268 (7.8%) | 169 (4.9%) | 76 (2.2%) |
| gliner2-hivetrace-omni | 879 (25.4%) | 792 (22.9%) | 746 (21.6%) | 673 (19.5%) |
| fef2-secret-ru | 930 (26.9%) | 875 (25.3%) | 875 (25.3%) | 875 (25.3%) |
| gliner2-hivetrace-omni-ru | 967 (28.0%) | 857 (24.8%) | 780 (22.6%) | 684 (19.8%) |
| gliner2-fastino | 1059 (30.6%) | 1011 (29.2%) | 980 (28.3%) | 945 (27.3%) |
| gliner2-fastino-ru | 1087 (31.4%) | 1024 (29.6%) | 1008 (29.1%) | 987 (28.5%) |
| gliner-urchade-ru | 1112 (32.2%) | 924 (26.7%) | 815 (23.6%) | 662 (19.1%) |
| kalyan-ettin | 1206 (34.9%) | 948 (27.4%) | 909 (26.3%) | 908 (26.3%) |
| gliner-pii-base | 1252 (36.2%) | 352 (10.2%) | 274 (7.9%) | 230 (6.7%) |
| gravitee-small | 1329 (38.4%) | 1141 (33.0%) | 1130 (32.7%) | 1130 (32.7%) |
| ner-ru-yqelz | 1512 (43.7%) | 1454 (42.0%) | 1454 (42.0%) | 1454 (42.0%) |
| ner-ru-gherman | 1545 (44.7%) | 1544 (44.7%) | 1544 (44.7%) | 1544 (44.7%) |
| davlan-xlmr | 1549 (44.8%) | 1547 (44.7%) | 1547 (44.7%) | 1547 (44.7%) |
| davlan-mbert | 1552 (44.9%) | 1552 (44.9%) | 1552 (44.9%) | 1552 (44.9%) |
| gliner2-hivetrace-uni | 1763 (51.0%) | 1016 (29.4%) | 711 (20.6%) | 423 (12.2%) |
| gliner2-hivetrace-uni-ru | 2349 (67.9%) | 1545 (44.7%) | 1084 (31.3%) | 609 (17.6%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
