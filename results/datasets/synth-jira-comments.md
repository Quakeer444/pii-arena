# synth-jira-comments - ru / pii (300 rows, 2705 spans, 0 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.293 (70.7% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pplx | **2** | 0.1% [0.0%, 0.2%] | 99.6% | 0.818 [0.811, 0.825] | 0.693 | 0.998 | 0.600 | 0.836 | 0.749 | 0/0 | 0 | 0 | 95 | 596M |  |
| pii-shield-onnx | **238** | 8.8% [7.6%, 9.9%] | 85.6% | 0.667 [0.654, 0.679] | 0.520 | 0.931 | 0.282 | 0.621 | 0.337 | 0/0 | 0 | 0 | 349 | - |  |
| gliner2-hivetrace-omni | **287** | 10.6% [9.7%, 11.6%] | 88.7% | 0.898 [0.886, 0.909] | 0.951 | 0.850 | 0.872 | 0.899 | 0.781 | 0/0 | 0 | 0 | 30 | 307M |  |
| mmbert32k | **310** | 11.5% [10.3%, 12.7%] | 47.3% | 0.724 [0.712, 0.735] | 0.742 | 0.707 | 0.211 | 0.564 | 0.356 | 0/0 | 0 | 0 | 17 | 308M |  |
| gliner-nvidia | **369** | 13.6% [12.4%, 14.9%] | 81.4% | 0.895 [0.885, 0.905] | 0.947 | 0.849 | 0.815 | 0.884 | 0.596 | 0/0 | 0 | 0 | 15 | 445M |  |
| gliner2-fastino | **371** | 13.7% [12.6%, 14.9%] | 84.9% | 0.801 [0.786, 0.814] | 0.902 | 0.720 | 0.810 | 0.832 | 0.763 | 0/0 | 0 | 26 | 11 | 307M |  |
| gliner2-fastino-ru | **413** | 15.3% [14.2%, 16.4%] | 83.8% | 0.803 [0.790, 0.816] | 0.898 | 0.726 | 0.817 | 0.831 | 0.787 | 0/0 | 0 | 46 | 23 | 307M |  |
| nuner-zero | **485** | 17.9% [16.6%, 19.2%] | 79.0% | 0.704 [0.688, 0.719] | 0.670 | 0.741 | 0.694 | 0.770 | 0.629 | 0/0 | 0 | 0 | 15 | 449M |  |
| gliner25-fastino | **490** | 18.1% [16.7%, 19.5%] | 81.1% | 0.807 [0.791, 0.823] | 0.910 | 0.726 | 0.820 | 0.854 | 0.728 | 0/0 | 0 | 0 | 7 | 287M |  |
| ru-legal-ner | **597** | 22.1% [19.8%, 24.4%] | 43.4% | 0.644 [0.627, 0.659] | 0.629 | 0.660 | 0.217 | 0.599 | 0.243 | 0/0 | 0 | 0 | 12 | 29M |  |
| gliner2-hivetrace-omni-ru | **611** | 22.6% [21.2%, 24.0%] | 76.7% | 0.784 [0.767, 0.799] | 0.928 | 0.680 | 0.806 | 0.835 | 0.731 | 0/0 | 0 | 0 | 21 | 307M |  |
| kalyan-ettin | **634** | 23.4% [22.3%, 24.5%] | 49.5% | 0.731 [0.718, 0.743] | 0.909 | 0.611 | 0.436 | 0.751 | 0.686 | 0/0 | 0 | 0 | 24 | 68M |  |
| opf-kz-ru | **639** | 23.6% [22.3%, 25.1%] | 67.7% | 0.713 [0.701, 0.724] | 0.712 | 0.714 | 0.490 | 0.766 | 0.619 | 0/0 | 0 | 0 | 31 | 1.4B |  |
| apararti | **673** | 24.9% [23.5%, 26.2%] | 63.6% | 0.727 [0.715, 0.738] | 0.751 | 0.704 | 0.502 | 0.767 | 0.647 | 0/0 | 0 | 0 | 62 | 1.4B |  |
| openmed-nemotron | **694** | 25.7% [24.8%, 26.6%] | 52.3% | 0.661 [0.650, 0.672] | 0.666 | 0.656 | 0.461 | 0.735 | 0.609 | 0/0 | 0 | 0 | 48 | 1.4B |  |
| gliner-pii-edge | **708** | 26.2% [24.2%, 28.2%] | 67.1% | 0.752 [0.736, 0.767] | 0.781 | 0.725 | 0.663 | 0.739 | 0.466 | 0/0 | 0 | 0 | 170 | 45M |  |
| gliner2-large | **713** | 26.4% [25.0%, 27.6%] | 70.7% | 0.738 [0.724, 0.752] | 0.908 | 0.621 | 0.738 | 0.791 | 0.709 | 0/0 | 0 | 0 | 29 | 486M |  |
| gliner25-fastino-ru | **749** | 27.7% [26.2%, 29.4%] | 71.6% | 0.728 [0.711, 0.744] | 0.908 | 0.607 | 0.776 | 0.796 | 0.676 | 0/0 | 0 | 0 | 8 | 287M |  |
| opf-ru-v2 | **778** | 28.8% [27.9%, 29.6%] | 65.1% | 0.778 [0.769, 0.788] | 0.948 | 0.660 | 0.646 | 0.772 | 0.739 | 0/0 | 0 | 0 | 929 | 1.4B |  |
| rules-ru | **807** | 29.8% [29.4%, 30.3%] | 70.2% | 0.728 [0.719, 0.737] | 0.675 | 0.791 | 0.717 | 0.717 | 0.727 | 0/0 | 0 | 0 | 1 | - |  |
| nym-small | **813** | 30.1% [28.6%, 31.6%] | 36.0% | 0.753 [0.740, 0.765] | 0.864 | 0.667 | 0.280 | 0.700 | 0.338 | 0/0 | 0 | 0 | 160 | - |  |
| gliner-urchade | **846** | 31.3% [29.6%, 33.1%] | 67.1% | 0.723 [0.705, 0.739] | 0.927 | 0.592 | 0.740 | 0.768 | 0.653 | 0/0 | 0 | 0 | 10 | 289M |  |
| opf-ru | **855** | 31.6% [30.2%, 33.1%] | 51.7% | 0.730 [0.718, 0.742] | 0.910 | 0.610 | 0.512 | 0.740 | 0.692 | 0/0 | 0 | 0 | 71 | 1.4B |  |
| nym-base | **861** | 31.8% [30.3%, 33.4%] | 37.7% | 0.742 [0.730, 0.753] | 0.872 | 0.645 | 0.315 | 0.686 | 0.363 | 0/0 | 0 | 0 | 10 | 308M |  |
| openmed-multilingual | **897** | 33.2% [32.1%, 34.4%] | 51.9% | 0.612 [0.600, 0.624] | 0.639 | 0.587 | 0.459 | 0.636 | 0.593 | 0/0 | 0 | 0 | 66 | 1.4B |  |
| openai-base | **899** | 33.2% [31.4%, 35.0%] | 60.8% | 0.731 [0.718, 0.743] | 0.812 | 0.665 | 0.559 | 0.751 | 0.651 | 0/0 | 0 | 0 | 75 | 1.4B |  |
| traciora | **970** | 35.9% [34.3%, 37.4%] | 56.7% | 0.751 [0.739, 0.761] | 0.938 | 0.625 | 0.600 | 0.747 | 0.680 | 0/0 | 0 | 0 | 502 | 1.4B |  |
| gravitee-small | **1008** | 37.3% [36.2%, 38.4%] | 54.8% | 0.624 [0.608, 0.637] | 0.794 | 0.514 | 0.522 | 0.707 | 0.610 | 0/0 | 0 | 0 | 11 | 29M |  |
| gliner-nvidia-ru | **1040** | 38.4% [37.0%, 40.0%] | 55.5% | 0.619 [0.601, 0.638] | 0.927 | 0.464 | 0.644 | 0.726 | 0.565 | 0/0 | 0 | 0 | 57 | 445M |  |
| bardsai-eu | **1056** | 39.0% [37.6%, 40.5%] | 44.8% | 0.689 [0.677, 0.700] | 0.885 | 0.564 | 0.416 | 0.682 | 0.136 | 0/0 | 0 | 0 | 673 | - |  |
| gliner-stream-pii | **1069** | 39.5% [37.8%, 41.0%] | 54.8% | 0.609 [0.591, 0.627] | 0.883 | 0.465 | 0.624 | 0.700 | 0.444 | 0/0 | 0 | 0 | 13 | 677M |  |
| gliner-pii-base | **1426** | 52.7% [51.5%, 54.0%] | 45.8% | 0.533 [0.515, 0.552] | 0.961 | 0.369 | 0.605 | 0.625 | 0.394 | 0/0 | 0 | 0 | 8 | 166M |  |
| gliner-multi-v21-ru | **1435** | 53.0% [51.0%, 54.9%] | 39.9% | 0.461 [0.444, 0.479] | 0.938 | 0.306 | 0.521 | 0.618 | 0.384 | 0/0 | 0 | 0 | 19 | 289M |  |
| gliner-multi-v21 | **1491** | 55.1% [53.5%, 56.7%] | 38.1% | 0.442 [0.428, 0.456] | 0.881 | 0.295 | 0.483 | 0.573 | 0.222 | 0/0 | 0 | 0 | 9 | 289M |  |
| ru-pii-ner | **1512** | 55.9% [54.3%, 57.5%] | 43.8% | 0.505 [0.486, 0.524] | 0.885 | 0.353 | 0.539 | 0.567 | 0.347 | 0/0 | 0 | 0 | 213 | 358M |  |
| gliner2-vladlinv-ru | **1606** | 59.4% [58.2%, 60.6%] | 40.0% | 0.539 [0.520, 0.559] | 0.939 | 0.378 | 0.542 | 0.551 | 0.406 | 0/0 | 0 | 0 | 11 | 287M |  |
| gliner2-vladlinv | **1625** | 60.1% [58.9%, 61.1%] | 39.3% | 0.528 [0.510, 0.548] | 0.975 | 0.362 | 0.552 | 0.561 | 0.490 | 0/0 | 0 | 0 | 7 | 287M |  |
| gliner2-hivetrace-uni | **1716** | 63.4% [62.3%, 64.5%] | 35.5% | 0.459 [0.442, 0.476] | 0.973 | 0.300 | 0.507 | 0.528 | 0.446 | 0/0 | 0 | 0 | 12 | 147M |  |
| gliner-urchade-ru | **1770** | 65.4% [63.6%, 67.5%] | 33.8% | 0.439 [0.415, 0.461] | 0.899 | 0.290 | 0.477 | 0.498 | 0.414 | 0/0 | 0 | 0 | 17 | 289M |  |
| fef2-secret-ru | **1801** | 66.6% [65.1%, 68.1%] | 30.1% | 0.548 [0.528, 0.567] | 0.921 | 0.390 | 0.394 | 0.467 | 0.188 | 0/0 | 0 | 0 | 12 | 177M |  |
| ner-ru-gherman | **1974** | 73.0% [71.9%, 74.1%] | 2.3% | 0.307 [0.295, 0.319] | 0.994 | 0.181 | 0.029 | 0.424 | 0.000 | 0/0 | 0 | 0 | 12 | 177M |  |
| stanza-ru | **1992** | 73.6% [72.8%, 74.5%] | 22.8% | 0.264 [0.252, 0.276] | 0.304 | 0.234 | 0.167 | 0.196 | 0.186 | 0/0 | 0 | 0 | 72 | - |  |
| gliner2-hivetrace-uni-ru | **2022** | 74.8% [73.6%, 75.9%] | 24.4% | 0.372 [0.353, 0.391] | 0.858 | 0.237 | 0.356 | 0.372 | 0.188 | 0/0 | 0 | 0 | 22 | 147M |  |
| ner-ru-yqelz | **2039** | 75.4% [74.5%, 76.3%] | 21.7% | 0.288 [0.275, 0.301] | 0.531 | 0.197 | 0.265 | 0.301 | 0.243 | 0/0 | 0 | 0 | 13 | 559M |  |
| davlan-xlmr | **2116** | 78.2% [77.6%, 78.9%] | 21.0% | 0.291 [0.281, 0.302] | 0.996 | 0.171 | 0.341 | 0.358 | 0.285 | 0/0 | 0 | 0 | 11 | 277M |  |
| davlan-mbert | **2143** | 79.2% [78.6%, 79.8%] | 20.0% | 0.282 [0.272, 0.293] | 0.998 | 0.164 | 0.330 | 0.344 | 0.280 | 0/0 | 0 | 0 | 12 | 177M |  |
| spacy-alrosait | **2322** | 85.8% [84.6%, 87.0%] | 14.1% | 0.225 [0.208, 0.243] | 1.000 | 0.127 | 0.247 | 0.248 | 0.000 | 0/0 | 0 | 0 | 12 | - |  |
| natasha | **2348** | 86.8% [85.7%, 88.0%] | 12.1% | 0.191 [0.175, 0.206] | 0.707 | 0.111 | 0.081 | 0.232 | 0.190 | 0/0 | 0 | 0 | 5 | - |  |
| spacy-ru-lg | **2434** | 90.0% [88.9%, 91.0%] | 5.8% | 0.129 [0.116, 0.142] | 0.469 | 0.074 | 0.077 | 0.164 | 0.125 | 0/0 | 0 | 0 | 13 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: gliner2-hivetrace-omni ≈ mmbert32k; gliner-nvidia ≈ gliner2-fastino; nuner-zero ≈ gliner25-fastino; ru-legal-ner ≈ gliner2-hivetrace-omni-ru; gliner2-hivetrace-omni-ru ≈ kalyan-ettin; kalyan-ettin ≈ opf-kz-ru; opf-kz-ru ≈ apararti; apararti ≈ openmed-nemotron; openmed-nemotron ≈ gliner-pii-edge; gliner-pii-edge ≈ gliner2-large; gliner2-large ≈ gliner25-fastino-ru; gliner25-fastino-ru ≈ opf-ru-v2; rules-ru ≈ nym-small; nym-small ≈ gliner-urchade; gliner-urchade ≈ opf-ru; opf-ru ≈ nym-base; nym-base ≈ openmed-multilingual; openmed-multilingual ≈ openai-base; traciora ≈ gravitee-small; gravitee-small ≈ gliner-nvidia-ru; gliner-nvidia-ru ≈ bardsai-eu; bardsai-eu ≈ gliner-stream-pii; gliner-pii-base ≈ gliner-multi-v21-ru; gliner-multi-v21 ≈ ru-pii-ner; gliner2-hivetrace-uni ≈ gliner-urchade-ru; gliner-urchade-ru ≈ fef2-secret-ru; ner-ru-gherman ≈ stanza-ru; stanza-ru ≈ gliner2-hivetrace-uni-ru; gliner2-hivetrace-uni-ru ≈ ner-ru-yqelz

## Missed by group

| model | PERSON | CONTACT | NET | ACCOUNT | SECRET |
|---|---|---|---|---|---|
| spans in gold | 566 | 442 | 1132 | 221 | 344 |
| pplx | 0 (0.0%) | 0 (0.0%) | 2 (0.2%) | 0 (0.0%) | 0 (0.0%) |
| pii-shield-onnx | 210 (37.1%) | 0 (0.0%) | 3 (0.3%) | 25 (11.3%) | 0 (0.0%) |
| gliner2-hivetrace-omni | 0 (0.0%) | 0 (0.0%) | 24 (2.1%) | 129 (58.4%) | 134 (39.0%) |
| mmbert32k | 5 (0.9%) | 0 (0.0%) | 210 (18.6%) | 45 (20.4%) | 50 (14.5%) |
| gliner-nvidia | 112 (19.8%) | 2 (0.5%) | 54 (4.8%) | 150 (67.9%) | 51 (14.8%) |
| gliner2-fastino | 10 (1.8%) | 0 (0.0%) | 97 (8.6%) | 5 (2.3%) | 259 (75.3%) |
| gliner2-fastino-ru | 7 (1.2%) | 0 (0.0%) | 25 (2.2%) | 94 (42.5%) | 287 (83.4%) |
| nuner-zero | 125 (22.1%) | 0 (0.0%) | 0 (0.0%) | 166 (75.1%) | 194 (56.4%) |
| gliner25-fastino | 3 (0.5%) | 0 (0.0%) | 134 (11.8%) | 149 (67.4%) | 204 (59.3%) |
| ru-legal-ner | 126 (22.3%) | 15 (3.4%) | 389 (34.4%) | 46 (20.8%) | 21 (6.1%) |
| gliner2-hivetrace-omni-ru | 0 (0.0%) | 0 (0.0%) | 186 (16.4%) | 183 (82.8%) | 242 (70.3%) |
| kalyan-ettin | 12 (2.1%) | 6 (1.4%) | 545 (48.1%) | 0 (0.0%) | 71 (20.6%) |
| opf-kz-ru | 33 (5.8%) | 2 (0.5%) | 541 (47.8%) | 58 (26.2%) | 5 (1.5%) |
| apararti | 37 (6.5%) | 1 (0.2%) | 502 (44.3%) | 131 (59.3%) | 2 (0.6%) |
| openmed-nemotron | 22 (3.9%) | 12 (2.7%) | 572 (50.5%) | 53 (24.0%) | 35 (10.2%) |
| gliner-pii-edge | 269 (47.5%) | 37 (8.4%) | 343 (30.3%) | 47 (21.3%) | 12 (3.5%) |
| gliner2-large | 177 (31.3%) | 0 (0.0%) | 108 (9.5%) | 141 (63.8%) | 287 (83.4%) |
| gliner25-fastino-ru | 1 (0.2%) | 0 (0.0%) | 310 (27.4%) | 166 (75.1%) | 272 (79.1%) |
| opf-ru-v2 | 28 (4.9%) | 1 (0.2%) | 590 (52.1%) | 140 (63.3%) | 19 (5.5%) |
| rules-ru | 566 (100.0%) | 0 (0.0%) | 0 (0.0%) | 214 (96.8%) | 27 (7.8%) |
| nym-small | 0 (0.0%) | 0 (0.0%) | 729 (64.4%) | 76 (34.4%) | 8 (2.3%) |
| gliner-urchade | 0 (0.0%) | 48 (10.9%) | 382 (33.7%) | 156 (70.6%) | 260 (75.6%) |
| opf-ru | 31 (5.5%) | 6 (1.4%) | 791 (69.9%) | 24 (10.9%) | 3 (0.9%) |
| nym-base | 0 (0.0%) | 2 (0.5%) | 790 (69.8%) | 66 (29.9%) | 3 (0.9%) |
| openmed-multilingual | 222 (39.2%) | 0 (0.0%) | 566 (50.0%) | 106 (48.0%) | 3 (0.9%) |
| openai-base | 39 (6.9%) | 7 (1.6%) | 765 (67.6%) | 74 (33.5%) | 14 (4.1%) |
| traciora | 61 (10.8%) | 4 (0.9%) | 809 (71.5%) | 79 (35.7%) | 17 (4.9%) |
| gravitee-small | 113 (20.0%) | 7 (1.6%) | 566 (50.0%) | 182 (82.4%) | 140 (40.7%) |
| gliner-nvidia-ru | 115 (20.3%) | 5 (1.1%) | 483 (42.7%) | 183 (82.8%) | 254 (73.8%) |
| bardsai-eu | 0 (0.0%) | 1 (0.2%) | 974 (86.0%) | 36 (16.3%) | 45 (13.1%) |
| gliner-stream-pii | 375 (66.3%) | 27 (6.1%) | 478 (42.2%) | 58 (26.2%) | 131 (38.1%) |
| gliner-pii-base | 471 (83.2%) | 69 (15.6%) | 565 (49.9%) | 152 (68.8%) | 169 (49.1%) |
| gliner-multi-v21-ru | 96 (17.0%) | 126 (28.5%) | 843 (74.5%) | 78 (35.3%) | 292 (84.9%) |
| gliner-multi-v21 | 14 (2.5%) | 152 (34.4%) | 952 (84.1%) | 64 (29.0%) | 309 (89.8%) |
| ru-pii-ner | 2 (0.4%) | 49 (11.1%) | 1096 (96.8%) | 43 (19.5%) | 322 (93.6%) |
| gliner2-vladlinv-ru | 8 (1.4%) | 74 (16.7%) | 1132 (100.0%) | 212 (95.9%) | 180 (52.3%) |
| gliner2-vladlinv | 8 (1.4%) | 58 (13.1%) | 1132 (100.0%) | 212 (95.9%) | 215 (62.5%) |
| gliner2-hivetrace-uni | 49 (8.7%) | 19 (4.3%) | 1132 (100.0%) | 176 (79.6%) | 340 (98.8%) |
| gliner-urchade-ru | 553 (97.7%) | 138 (31.2%) | 587 (51.9%) | 186 (84.2%) | 306 (89.0%) |
| fef2-secret-ru | 177 (31.3%) | 220 (49.8%) | 1129 (99.7%) | 136 (61.5%) | 139 (40.4%) |
| ner-ru-gherman | 0 (0.0%) | 361 (81.7%) | 1132 (100.0%) | 137 (62.0%) | 344 (100.0%) |
| stanza-ru | 0 (0.0%) | 407 (92.1%) | 1101 (97.3%) | 221 (100.0%) | 263 (76.5%) |
| gliner2-hivetrace-uni-ru | 191 (33.7%) | 273 (61.8%) | 1125 (99.4%) | 183 (82.8%) | 250 (72.7%) |
| ner-ru-yqelz | 0 (0.0%) | 431 (97.5%) | 1071 (94.6%) | 221 (100.0%) | 316 (91.9%) |
| davlan-xlmr | 0 (0.0%) | 429 (97.1%) | 1132 (100.0%) | 211 (95.5%) | 344 (100.0%) |
| davlan-mbert | 4 (0.7%) | 442 (100.0%) | 1132 (100.0%) | 221 (100.0%) | 344 (100.0%) |
| spacy-alrosait | 183 (32.3%) | 442 (100.0%) | 1132 (100.0%) | 221 (100.0%) | 344 (100.0%) |
| natasha | 209 (36.9%) | 442 (100.0%) | 1132 (100.0%) | 221 (100.0%) | 344 (100.0%) |
| spacy-ru-lg | 304 (53.7%) | 441 (99.8%) | 1130 (99.8%) | 216 (97.7%) | 343 (99.7%) |

## Char recall by gold type

| type | group | pplx | pii-shield-onnx | gliner2-hivetrace-omni | mmbert32k | gliner-nvidia | gliner2-fastino | gliner2-fastino-ru | nuner-zero | gliner25-fastino | ru-legal-ner | gliner2-hivetrace-omni-ru | kalyan-ettin | opf-kz-ru | apararti | openmed-nemotron | gliner-pii-edge | gliner2-large | gliner25-fastino-ru | opf-ru-v2 | rules-ru | nym-small | gliner-urchade | opf-ru | nym-base | openmed-multilingual | openai-base | traciora | gravitee-small | gliner-nvidia-ru | bardsai-eu | gliner-stream-pii | gliner-pii-base | gliner-multi-v21-ru | gliner-multi-v21 | ru-pii-ner | gliner2-vladlinv-ru | gliner2-vladlinv | gliner2-hivetrace-uni | gliner-urchade-ru | fef2-secret-ru | ner-ru-gherman | stanza-ru | gliner2-hivetrace-uni-ru | ner-ru-yqelz | davlan-xlmr | davlan-mbert | spacy-alrosait | natasha | spacy-ru-lg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| email | CONTACT | 1.000 | 1.000 | 1.000 | 0.932 | 0.974 | 1.000 | 1.000 | 0.974 | 1.000 | 0.829 | 1.000 | 0.926 | 1.000 | 0.983 | 0.996 | 0.811 | 1.000 | 1.000 | 0.950 | 1.000 | 0.976 | 0.820 | 0.963 | 0.948 | 0.997 | 0.984 | 1.000 | 0.905 | 1.000 | 0.701 | 0.736 | 0.826 | 0.269 | 0.215 | 0.901 | 0.757 | 0.806 | 1.000 | 0.521 | 0.968 | 0.138 | 0.174 | 0.739 | 0.001 | 0.019 | 0.000 | 0.000 | 0.000 | 0.004 |
| hostname | NET | 0.994 | 0.972 | 0.951 | 0.356 | 0.936 | 0.817 | 0.955 | 1.000 | 0.784 | 0.380 | 0.668 | 0.012 | 0.131 | 0.173 | 0.000 | 0.527 | 0.824 | 0.471 | 0.000 | 1.000 | 0.384 | 0.532 | 0.023 | 0.183 | 0.000 | 0.144 | 0.004 | 0.001 | 0.214 | 0.055 | 0.115 | 0.012 | 0.025 | 0.030 | 0.041 | 0.000 | 0.000 | 0.000 | 0.375 | 0.004 | 0.000 | 0.011 | 0.003 | 0.036 | 0.000 | 0.000 | 0.000 | 0.000 | 0.004 |
| ip | NET | 1.000 | 0.993 | 1.000 | 0.944 | 0.974 | 1.000 | 1.000 | 1.000 | 0.976 | 0.322 | 1.000 | 0.913 | 0.762 | 0.735 | 0.960 | 0.847 | 0.984 | 0.982 | 0.917 | 1.000 | 0.129 | 0.795 | 0.300 | 0.307 | 0.990 | 0.416 | 0.503 | 0.997 | 0.937 | 0.057 | 0.961 | 0.981 | 0.437 | 0.212 | 0.022 | 0.000 | 0.000 | 0.000 | 0.592 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| login | ACCOUNT | 1.000 | 0.858 | 0.417 | 0.693 | 0.307 | 0.979 | 0.580 | 0.232 | 0.319 | 0.764 | 0.172 | 0.994 | 0.693 | 0.385 | 0.734 | 0.786 | 0.374 | 0.247 | 0.319 | 0.034 | 0.616 | 0.300 | 0.881 | 0.683 | 0.494 | 0.649 | 0.598 | 0.142 | 0.143 | 0.786 | 0.708 | 0.319 | 0.654 | 0.686 | 0.823 | 0.036 | 0.035 | 0.192 | 0.164 | 0.383 | 0.363 | 0.000 | 0.179 | 0.000 | 0.041 | 0.000 | 0.000 | 0.000 | 0.021 |
| password | SECRET | 1.000 | 1.000 | 0.750 | 0.647 | 0.641 | 0.837 | 0.728 | 0.842 | 0.674 | 0.735 | 0.606 | 0.628 | 0.911 | 0.964 | 0.628 | 0.911 | 0.498 | 0.443 | 0.705 | 0.516 | 0.946 | 0.600 | 0.956 | 0.964 | 0.992 | 0.792 | 0.703 | 0.750 | 0.410 | 0.466 | 0.418 | 0.534 | 0.451 | 0.371 | 0.071 | 0.427 | 0.443 | 0.000 | 0.532 | 0.761 | 0.000 | 0.148 | 0.282 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.018 |
| person | PERSON | 1.000 | 0.672 | 0.999 | 0.906 | 0.640 | 0.966 | 0.971 | 0.741 | 0.990 | 0.805 | 0.998 | 0.765 | 0.933 | 0.910 | 0.842 | 0.496 | 0.574 | 0.991 | 0.936 | 0.000 | 0.942 | 1.000 | 0.897 | 0.943 | 0.398 | 0.918 | 0.881 | 0.803 | 0.579 | 0.991 | 0.267 | 0.137 | 0.834 | 0.968 | 0.995 | 0.983 | 0.983 | 0.859 | 0.031 | 0.742 | 0.923 | 1.000 | 0.606 | 0.998 | 0.996 | 0.979 | 0.753 | 0.660 | 0.430 |
| phone | CONTACT | 1.000 | 0.998 | 1.000 | 0.921 | 0.993 | 1.000 | 1.000 | 1.000 | 1.000 | 0.957 | 1.000 | 0.964 | 0.993 | 1.000 | 0.952 | 1.000 | 1.000 | 1.000 | 0.993 | 1.000 | 1.000 | 0.898 | 0.980 | 1.000 | 0.982 | 0.984 | 0.981 | 0.980 | 0.981 | 0.999 | 0.977 | 0.868 | 0.741 | 0.764 | 0.861 | 0.902 | 0.924 | 0.920 | 0.845 | 0.010 | 0.000 | 0.000 | 0.013 | 0.013 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| secret | SECRET | 0.998 | 1.000 | 0.546 | 0.702 | 0.845 | 0.099 | 0.037 | 0.261 | 0.258 | 0.876 | 0.204 | 0.747 | 0.993 | 0.983 | 0.881 | 0.919 | 0.070 | 0.133 | 0.921 | 1.000 | 0.848 | 0.167 | 0.922 | 0.888 | 0.901 | 0.976 | 0.957 | 0.428 | 0.154 | 0.884 | 0.481 | 0.328 | 0.042 | 0.024 | 0.031 | 0.341 | 0.254 | 0.010 | 0.022 | 0.610 | 0.000 | 0.181 | 0.221 | 0.079 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## char F1 by domain

| domain | n | pplx | pii-shield-onnx | gliner2-hivetrace-omni | mmbert32k | gliner-nvidia | gliner2-fastino | gliner2-fastino-ru | nuner-zero | gliner25-fastino | ru-legal-ner | gliner2-hivetrace-omni-ru | kalyan-ettin | opf-kz-ru | apararti | openmed-nemotron | gliner-pii-edge | gliner2-large | gliner25-fastino-ru | opf-ru-v2 | rules-ru | nym-small | gliner-urchade | opf-ru | nym-base | openmed-multilingual | openai-base | traciora | gravitee-small | gliner-nvidia-ru | bardsai-eu | gliner-stream-pii | gliner-pii-base | gliner-multi-v21-ru | gliner-multi-v21 | ru-pii-ner | gliner2-vladlinv-ru | gliner2-vladlinv | gliner2-hivetrace-uni | gliner-urchade-ru | fef2-secret-ru | ner-ru-gherman | stanza-ru | gliner2-hivetrace-uni-ru | ner-ru-yqelz | davlan-xlmr | davlan-mbert | spacy-alrosait | natasha | spacy-ru-lg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| en | 90 | 0.813 | 0.622 | 0.876 | 0.679 | 0.927 | 0.787 | 0.785 | 0.711 | 0.801 | 0.529 | 0.730 | 0.730 | 0.692 | 0.687 | 0.658 | 0.673 | 0.762 | 0.711 | 0.771 | 0.741 | 0.692 | 0.671 | 0.695 | 0.674 | 0.639 | 0.688 | 0.720 | 0.657 | 0.588 | 0.664 | 0.695 | 0.545 | 0.404 | 0.407 | 0.402 | 0.504 | 0.505 | 0.431 | 0.416 | 0.419 | 0.227 | 0.214 | 0.333 | 0.224 | 0.236 | 0.220 | 0.000 | 0.027 | 0.006 |
| ru | 210 | 0.820 | 0.685 | 0.906 | 0.742 | 0.882 | 0.806 | 0.810 | 0.701 | 0.810 | 0.683 | 0.806 | 0.731 | 0.721 | 0.742 | 0.662 | 0.781 | 0.727 | 0.734 | 0.781 | 0.723 | 0.776 | 0.742 | 0.744 | 0.767 | 0.601 | 0.747 | 0.762 | 0.612 | 0.630 | 0.699 | 0.572 | 0.529 | 0.484 | 0.455 | 0.544 | 0.552 | 0.537 | 0.470 | 0.449 | 0.595 | 0.337 | 0.285 | 0.387 | 0.314 | 0.313 | 0.306 | 0.302 | 0.248 | 0.173 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| pii-shield-onnx | 238 (8.8%) | 212 (7.8%) | 211 (7.8%) | 211 (7.8%) |
| gliner2-hivetrace-omni | 287 (10.6%) | 130 (4.8%) | 88 (3.3%) | 51 (1.9%) |
| mmbert32k | 310 (11.5%) | 33 (1.2%) | 8 (0.3%) | 6 (0.2%) |
| gliner-nvidia | 369 (13.6%) | 231 (8.5%) | 169 (6.2%) | 116 (4.3%) |
| gliner2-fastino | 371 (13.7%) | 281 (10.4%) | 222 (8.2%) | 104 (3.8%) |
| gliner2-fastino-ru | 413 (15.3%) | 282 (10.4%) | 180 (6.7%) | 66 (2.4%) |
| nuner-zero | 485 (17.9%) | 156 (5.8%) | 54 (2.0%) | 5 (0.2%) |
| gliner25-fastino | 490 (18.1%) | 382 (14.1%) | 336 (12.4%) | 287 (10.6%) |
| ru-legal-ner | 597 (22.1%) | 278 (10.3%) | 257 (9.5%) | 256 (9.5%) |
| gliner2-hivetrace-omni-ru | 611 (22.6%) | 285 (10.5%) | 182 (6.7%) | 105 (3.9%) |
| kalyan-ettin | 634 (23.4%) | 557 (20.6%) | 553 (20.4%) | 553 (20.4%) |
| opf-kz-ru | 639 (23.6%) | 624 (23.1%) | 623 (23.0%) | 623 (23.0%) |
| apararti | 673 (24.9%) | 641 (23.7%) | 641 (23.7%) | 641 (23.7%) |
| openmed-nemotron | 694 (25.7%) | 658 (24.3%) | 656 (24.3%) | 656 (24.3%) |
| gliner-pii-edge | 708 (26.2%) | 61 (2.3%) | 12 (0.4%) | 1 (0.0%) |
| gliner2-large | 713 (26.4%) | 524 (19.4%) | 411 (15.2%) | 248 (9.2%) |
| gliner25-fastino-ru | 749 (27.7%) | 663 (24.5%) | 588 (21.7%) | 499 (18.4%) |
| opf-ru-v2 | 778 (28.8%) | 763 (28.2%) | 763 (28.2%) | 763 (28.2%) |
| nym-small | 813 (30.1%) | 807 (29.8%) | 807 (29.8%) | 807 (29.8%) |
| gliner-urchade | 846 (31.3%) | 482 (17.8%) | 278 (10.3%) | 97 (3.6%) |
| opf-ru | 855 (31.6%) | 808 (29.9%) | 807 (29.8%) | 807 (29.8%) |
| nym-base | 861 (31.8%) | 851 (31.5%) | 851 (31.5%) | 851 (31.5%) |
| openmed-multilingual | 897 (33.2%) | 848 (31.3%) | 846 (31.3%) | 846 (31.3%) |
| openai-base | 899 (33.2%) | 876 (32.4%) | 876 (32.4%) | 876 (32.4%) |
| traciora | 970 (35.9%) | 956 (35.3%) | 953 (35.2%) | 953 (35.2%) |
| gravitee-small | 1008 (37.3%) | 976 (36.1%) | 976 (36.1%) | 976 (36.1%) |
| gliner-nvidia-ru | 1040 (38.4%) | 865 (32.0%) | 748 (27.7%) | 617 (22.8%) |
| bardsai-eu | 1056 (39.0%) | 985 (36.4%) | 980 (36.2%) | 980 (36.2%) |
| gliner-stream-pii | 1069 (39.5%) | 865 (32.0%) | 745 (27.5%) | 597 (22.1%) |
| gliner-pii-base | 1426 (52.7%) | 161 (6.0%) | 6 (0.2%) | 0 (0.0%) |
| gliner-multi-v21-ru | 1435 (53.0%) | 780 (28.8%) | 567 (21.0%) | 264 (9.8%) |
| gliner-multi-v21 | 1491 (55.1%) | 911 (33.7%) | 602 (22.3%) | 285 (10.5%) |
| gliner2-vladlinv-ru | 1606 (59.4%) | 1576 (58.3%) | 1560 (57.7%) | 1531 (56.6%) |
| gliner2-vladlinv | 1625 (60.1%) | 1597 (59.0%) | 1580 (58.4%) | 1561 (57.7%) |
| gliner2-hivetrace-uni | 1716 (63.4%) | 1489 (55.0%) | 1216 (45.0%) | 731 (27.0%) |
| gliner-urchade-ru | 1770 (65.4%) | 1264 (46.7%) | 923 (34.1%) | 598 (22.1%) |
| fef2-secret-ru | 1801 (66.6%) | 1797 (66.4%) | 1797 (66.4%) | 1797 (66.4%) |
| ner-ru-gherman | 1974 (73.0%) | 1972 (72.9%) | 1972 (72.9%) | 1972 (72.9%) |
| gliner2-hivetrace-uni-ru | 2022 (74.8%) | 1459 (53.9%) | 1132 (41.8%) | 702 (26.0%) |
| ner-ru-yqelz | 2039 (75.4%) | 2014 (74.5%) | 2014 (74.5%) | 2014 (74.5%) |
| davlan-xlmr | 2116 (78.2%) | 2114 (78.2%) | 2114 (78.2%) | 2114 (78.2%) |
| davlan-mbert | 2143 (79.2%) | 2142 (79.2%) | 2142 (79.2%) | 2142 (79.2%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
