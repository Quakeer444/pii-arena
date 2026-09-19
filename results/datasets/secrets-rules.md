# secrets-rules - en / secrets (1496 rows, 746 spans, 750 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.340 (66.0% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| traciora | **1** | 0.1% [0.0%, 0.4%] | 97.5% | 0.728 [0.693, 0.765] | 0.573 | 0.997 | 0.550 | 0.657 | 0.676 | 503/750 | 27643 | 0 | 200 | 1.4B |  |
| pii-shield-onnx | **1** | 0.1% [0.0%, 0.4%] | 98.5% | 0.602 [0.561, 0.645] | 0.431 | 0.999 | 0.450 | 0.511 | 0.581 | 714/750 | 46268 | 0 | 96 | - |  |
| opf-ru | **3** | 0.4% [0.0%, 0.9%] | 98.4% | 0.716 [0.684, 0.752] | 0.560 | 0.995 | 0.529 | 0.632 | 0.678 | 555/750 | 28309 | 0 | 158 | 1.4B |  |
| apararti | **3** | 0.4% [0.0%, 0.9%] | 98.8% | 0.697 [0.657, 0.738] | 0.535 | 0.998 | 0.586 | 0.681 | 0.672 | 527/750 | 31472 | 0 | 47 | 1.4B |  |
| opf-kz-ru | **5** | 0.7% [0.1%, 1.3%] | 98.4% | 0.700 [0.666, 0.736] | 0.540 | 0.993 | 0.560 | 0.673 | 0.680 | 508/750 | 29471 | 0 | 47 | 1.4B |  |
| openai-base | **7** | 0.9% [0.3%, 1.7%] | 98.0% | 0.718 [0.683, 0.757] | 0.565 | 0.986 | 0.578 | 0.705 | 0.694 | 435/750 | 26308 | 0 | 204 | 1.4B |  |
| nym-base | **8** | 1.1% [0.4%, 1.9%] | 83.2% | 0.743 [0.710, 0.780] | 0.603 | 0.970 | 0.495 | 0.665 | 0.098 | 463/750 | 24424 | 0 | 2 | 308M |  |
| opf-ru-v2 | **9** | 1.2% [0.5%, 2.1%] | 97.2% | 0.754 [0.719, 0.792] | 0.610 | 0.987 | 0.643 | 0.743 | 0.731 | 415/750 | 23171 | 0 | 379 | 1.4B |  |
| gliner-pii-edge | **13** | 1.7% [0.9%, 2.8%] | 88.6% | 0.666 [0.636, 0.696] | 0.511 | 0.957 | 0.475 | 0.571 | 0.666 | 667/750 | 30751 | 0 | 9 | 45M |  |
| gitleaks | **18** | 2.4% [1.4%, 3.5%] | 97.6% | 0.913 [0.894, 0.930] | 0.862 | 0.971 | 0.915 | 0.919 | 0.913 | 110/750 | 5977 | 0 | 0 | - | train |
| nym-small | **20** | 2.7% [1.6%, 3.9%] | 79.1% | 0.713 [0.681, 0.750] | 0.573 | 0.945 | 0.436 | 0.623 | 0.091 | 531/750 | 26647 | 0 | 27 | - |  |
| ru-legal-ner | **23** | 3.1% [1.9%, 4.4%] | 65.0% | 0.695 [0.664, 0.726] | 0.581 | 0.862 | 0.281 | 0.558 | 0.000 | 450/750 | 20871 | 0 | 2 | 29M |  |
| betterleaks | **27** | 3.6% [2.3%, 5.1%] | 96.4% | 0.917 [0.898, 0.934] | 0.870 | 0.970 | 0.915 | 0.919 | 0.917 | 100/750 | 5571 | 0 | 0 | - | train |
| pplx | **29** | 3.9% [2.5%, 5.4%] | 93.4% | 0.753 [0.720, 0.786] | 0.625 | 0.949 | 0.630 | 0.743 | 0.713 | 385/750 | 21139 | 0 | 65 | 596M |  |
| gliner2-fastino | **34** | 4.6% [3.2%, 6.1%] | 87.4% | 0.684 [0.644, 0.720] | 0.554 | 0.894 | 0.539 | 0.611 | 0.684 | 573/750 | 26148 | 0 | 7 | 307M |  |
| gliner-stream-pii | **37** | 5.0% [3.4%, 6.6%] | 78.3% | 0.718 [0.687, 0.747] | 0.625 | 0.843 | 0.529 | 0.666 | 0.718 | 557/750 | 18826 | 0 | 5 | 677M |  |
| gliner25-fastino | **43** | 5.8% [4.2%, 7.7%] | 89.9% | 0.691 [0.660, 0.722] | 0.582 | 0.849 | 0.608 | 0.641 | 0.691 | 594/750 | 23134 | 4 | 3 | 287M |  |
| mmbert32k | **46** | 6.2% [4.5%, 7.9%] | 56.4% | 0.626 [0.596, 0.658] | 0.501 | 0.835 | 0.237 | 0.464 | 0.000 | 580/750 | 27698 | 0 | 3 | 308M |  |
| bardsai-eu | **73** | 9.8% [7.8%, 12.0%] | 82.2% | 0.741 [0.705, 0.779] | 0.617 | 0.925 | 0.612 | 0.714 | 0.000 | 358/750 | 21474 | 0 | 168 | - |  |
| openmed-multilingual | **90** | 12.1% [9.8%, 14.5%] | 74.1% | 0.669 [0.635, 0.705] | 0.543 | 0.871 | 0.424 | 0.586 | 0.553 | 568/750 | 27212 | 0 | 120 | 1.4B |  |
| kalyan-ettin | **109** | 14.6% [12.1%, 17.2%] | 57.5% | 0.654 [0.620, 0.687] | 0.556 | 0.794 | 0.356 | 0.585 | 0.286 | 447/750 | 22619 | 0 | 6 | 68M |  |
| openmed-nemotron | **110** | 14.7% [12.1%, 17.4%] | 64.1% | 0.655 [0.622, 0.691] | 0.529 | 0.861 | 0.340 | 0.579 | 0.574 | 504/750 | 27851 | 0 | 125 | 1.4B |  |
| credsweeper-noml | **126** | 16.9% [14.3%, 19.8%] | 82.2% | 0.773 [0.743, 0.801] | 0.754 | 0.793 | 0.768 | 0.779 | 0.773 | 224/750 | 9937 | 0 | 4 | - |  |
| credsweeper | **170** | 22.8% [19.9%, 25.9%] | 76.4% | 0.769 [0.737, 0.797] | 0.799 | 0.741 | 0.776 | 0.787 | 0.769 | 141/750 | 7171 | 0 | 90 | - |  |
| rules-ru | **182** | 24.4% [21.4%, 27.5%] | 74.5% | 0.641 [0.609, 0.673] | 0.585 | 0.709 | 0.574 | 0.617 | 0.635 | 450/750 | 18500 | 0 | 0 | - |  |
| gravitee-small | **202** | 27.1% [23.9%, 30.2%] | 58.2% | 0.676 [0.643, 0.708] | 0.647 | 0.708 | 0.514 | 0.658 | 0.671 | 308/750 | 14602 | 0 | 2 | 29M |  |
| nuner-zero | **205** | 27.5% [24.7%, 30.8%] | 65.7% | 0.559 [0.530, 0.585] | 0.476 | 0.678 | 0.349 | 0.420 | 0.559 | 587/750 | 21602 | 0 | 9 | 449M |  |
| gliner-nvidia | **249** | 33.4% [29.9%, 36.8%] | 65.5% | 0.607 [0.571, 0.641] | 0.553 | 0.674 | 0.501 | 0.543 | 0.607 | 441/750 | 18775 | 0 | 8 | 445M |  |
| gliner-urchade | **369** | 49.5% [45.8%, 53.1%] | 46.6% | 0.471 [0.435, 0.505] | 0.457 | 0.487 | 0.311 | 0.349 | 0.471 | 467/750 | 15850 | 0 | 5 | 289M |  |
| fef2-secret-ru | **370** | 49.6% [46.0%, 53.2%] | 43.0% | 0.436 [0.400, 0.473] | 0.481 | 0.398 | 0.378 | 0.463 | 0.065 | 394/750 | 16169 | 0 | 2 | 177M |  |
| kingfisher | **398** | 53.4% [49.7%, 56.9%] | 46.6% | 0.639 [0.600, 0.679] | 0.923 | 0.488 | 0.625 | 0.625 | 0.639 | 19/750 | 1563 | 0 | 1 | - | train |
| detect-secrets | **405** | 54.3% [50.8%, 58.2%] | 45.7% | 0.452 [0.406, 0.497] | 0.423 | 0.484 | 0.008 | 0.512 | 0.452 | 237/750 | 17723 | 0 | 12 | - |  |
| gliner2-vladlinv | **416** | 55.8% [52.2%, 59.3%] | 41.0% | 0.392 [0.358, 0.430] | 0.644 | 0.282 | 0.471 | 0.510 | 0.392 | 215/750 | 5931 | 0 | 4 | 287M |  |
| titus | **421** | 56.4% [52.9%, 60.2%] | 43.2% | 0.522 [0.482, 0.561] | 0.625 | 0.449 | 0.298 | 0.535 | 0.522 | 145/750 | 8136 | 0 | 5 | - | train |
| deepsecrets | **432** | 57.9% [54.3%, 61.3%] | 40.9% | 0.519 [0.476, 0.563] | 0.769 | 0.392 | 0.062 | 0.542 | 0.519 | 98/750 | 4139 | 0 | 17 | - |  |
| ner-ru-yqelz | **537** | 72.0% [68.5%, 75.1%] | 18.8% | 0.247 [0.217, 0.281] | 0.281 | 0.221 | 0.131 | 0.201 | 0.000 | 511/750 | 15694 | 0 | 3 | 559M |  |
| trufflehog | **558** | 74.8% [71.6%, 77.9%] | 23.6% | 0.360 [0.316, 0.404] | 0.770 | 0.235 | 0.355 | 0.383 | 0.360 | 47/750 | 2640 | 0 | 5 | - |  |
| gliner-pii-base | **581** | 77.9% [74.9%, 80.9%] | 20.8% | 0.216 [0.184, 0.246] | 0.341 | 0.158 | 0.225 | 0.247 | 0.216 | 374/750 | 10960 | 0 | 3 | 166M |  |
| stanza-ru | **597** | 80.0% [77.1%, 82.6%] | 9.9% | 0.172 [0.138, 0.211] | 0.169 | 0.175 | 0.040 | 0.131 | 0.000 | 685/750 | 25529 | 0 | 16 | - |  |
| gliner2-hivetrace-omni | **612** | 82.0% [79.4%, 84.6%] | 18.0% | 0.253 [0.218, 0.291] | 0.449 | 0.176 | 0.243 | 0.243 | 0.253 | 208/750 | 8278 | 0 | 8 | 307M |  |
| noseyparker | **625** | 83.8% [81.0%, 86.5%] | 16.2% | 0.245 [0.204, 0.286] | 0.481 | 0.165 | 0.165 | 0.246 | 0.245 | 117/750 | 6318 | 0 | 1 | - |  |
| gliner2-hivetrace-uni | **635** | 85.1% [82.6%, 87.6%] | 13.8% | 0.149 [0.123, 0.177] | 0.568 | 0.085 | 0.209 | 0.225 | 0.149 | 126/750 | 2474 | 0 | 9 | 147M |  |
| ru-pii-ner | **639** | 85.7% [83.1%, 88.1%] | 9.9% | 0.129 [0.105, 0.156] | 0.280 | 0.084 | 0.083 | 0.170 | 0.000 | 272/750 | 6885 | 0 | 49 | 358M |  |
| spacy-ru-lg | **692** | 92.8% [90.9%, 94.7%] | 6.7% | 0.155 [0.107, 0.206] | 0.328 | 0.102 | 0.063 | 0.110 | 0.000 | 158/750 | 7190 | 0 | 1 | - |  |
| gliner2-large | **706** | 94.6% [93.1%, 96.3%] | 4.3% | 0.049 [0.032, 0.070] | 0.069 | 0.038 | 0.030 | 0.041 | 0.049 | 452/750 | 11915 | 0 | 14 | 486M |  |
| gliner-multi-v21 | **722** | 96.8% [95.5%, 98.0%] | 1.5% | 0.034 [0.015, 0.058] | 0.061 | 0.023 | 0.011 | 0.027 | 0.034 | 312/750 | 5966 | 0 | 5 | 289M |  |
| davlan-mbert | **745** | 99.9% [99.6%, 100.0%] | 0.1% | 0.002 [0.000, 0.007] | 0.069 | 0.001 | 0.003 | 0.003 | 0.000 | 33/750 | 458 | 0 | 2 | 177M |  |
| ner-ru-gherman | **745** | 99.9% [99.6%, 100.0%] | 0.1% | 0.001 [0.000, 0.003] | 0.167 | 0.001 | 0.003 | 0.003 | 0.000 | 5/750 | 77 | 0 | 2 | 177M |  |
| davlan-xlmr | **746** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 6/750 | 49 | 0 | 2 | 277M |  |
| natasha | **746** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 43/750 | 1077 | 0 | 1 | - |  |
| spacy-alrosait | **746** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/750 | 0 | 0 | 1 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: traciora ≈ pii-shield-onnx; pii-shield-onnx ≈ opf-ru; opf-ru ≈ apararti; apararti ≈ opf-kz-ru; opf-kz-ru ≈ openai-base; openai-base ≈ nym-base; nym-base ≈ opf-ru-v2; opf-ru-v2 ≈ gliner-pii-edge; gliner-pii-edge ≈ gitleaks; gitleaks ≈ nym-small; nym-small ≈ ru-legal-ner; ru-legal-ner ≈ betterleaks; betterleaks ≈ pplx; pplx ≈ gliner2-fastino; gliner2-fastino ≈ gliner-stream-pii; gliner-stream-pii ≈ gliner25-fastino; gliner25-fastino ≈ mmbert32k; bardsai-eu ≈ openmed-multilingual; openmed-multilingual ≈ kalyan-ettin; kalyan-ettin ≈ openmed-nemotron; openmed-nemotron ≈ credsweeper-noml; credsweeper ≈ rules-ru; rules-ru ≈ gravitee-small; gravitee-small ≈ nuner-zero; gliner-urchade ≈ fef2-secret-ru; fef2-secret-ru ≈ kingfisher; kingfisher ≈ detect-secrets; detect-secrets ≈ gliner2-vladlinv; gliner2-vladlinv ≈ titus; titus ≈ deepsecrets; ner-ru-yqelz ≈ trufflehog; trufflehog ≈ gliner-pii-base; gliner-pii-base ≈ stanza-ru; stanza-ru ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ noseyparker; noseyparker ≈ gliner2-hivetrace-uni; gliner2-hivetrace-uni ≈ ru-pii-ner; spacy-ru-lg ≈ gliner2-large; davlan-mbert ≈ ner-ru-gherman; ner-ru-gherman ≈ davlan-xlmr; davlan-xlmr ≈ natasha; natasha ≈ spacy-alrosait

Legacy runs on this set: betterleaks, credsweeper, credsweeper-noml, deepsecrets, detect-secrets, kingfisher, noseyparker, pii-shield-onnx, titus, trufflehog. Their meta carries no `protocol` and no `bench_sha256`, so the version of the text they were taken from is confirmed only by the row and character counts, not by a fingerprint.

detect-secrets, trufflehog mark a whole line at a time (`granularity` in the meta line), so their char P / R / F1 and entity exact are not comparable with the rest; their missed count is.

## Missed by group

| model | SECRET |
|---|---|
| spans in gold | 746 |
| traciora | 1 (0.1%) |
| pii-shield-onnx | 1 (0.1%) |
| opf-ru | 3 (0.4%) |
| apararti | 3 (0.4%) |
| opf-kz-ru | 5 (0.7%) |
| openai-base | 7 (0.9%) |
| nym-base | 8 (1.1%) |
| opf-ru-v2 | 9 (1.2%) |
| gliner-pii-edge | 13 (1.7%) |
| gitleaks | 18 (2.4%) |
| nym-small | 20 (2.7%) |
| ru-legal-ner | 23 (3.1%) |
| betterleaks | 27 (3.6%) |
| pplx | 29 (3.9%) |
| gliner2-fastino | 34 (4.6%) |
| gliner-stream-pii | 37 (5.0%) |
| gliner25-fastino | 43 (5.8%) |
| mmbert32k | 46 (6.2%) |
| bardsai-eu | 73 (9.8%) |
| openmed-multilingual | 90 (12.1%) |
| kalyan-ettin | 109 (14.6%) |
| openmed-nemotron | 110 (14.7%) |
| credsweeper-noml | 126 (16.9%) |
| credsweeper | 170 (22.8%) |
| rules-ru | 182 (24.4%) |
| gravitee-small | 202 (27.1%) |
| nuner-zero | 205 (27.5%) |
| gliner-nvidia | 249 (33.4%) |
| gliner-urchade | 369 (49.5%) |
| fef2-secret-ru | 370 (49.6%) |
| kingfisher | 398 (53.4%) |
| detect-secrets | 405 (54.3%) |
| gliner2-vladlinv | 416 (55.8%) |
| titus | 421 (56.4%) |
| deepsecrets | 432 (57.9%) |
| ner-ru-yqelz | 537 (72.0%) |
| trufflehog | 558 (74.8%) |
| gliner-pii-base | 581 (77.9%) |
| stanza-ru | 597 (80.0%) |
| gliner2-hivetrace-omni | 612 (82.0%) |
| noseyparker | 625 (83.8%) |
| gliner2-hivetrace-uni | 635 (85.1%) |
| ru-pii-ner | 639 (85.7%) |
| spacy-ru-lg | 692 (92.8%) |
| gliner2-large | 706 (94.6%) |
| gliner-multi-v21 | 722 (96.8%) |
| davlan-mbert | 745 (99.9%) |
| ner-ru-gherman | 745 (99.9%) |
| davlan-xlmr | 746 (100.0%) |
| natasha | 746 (100.0%) |
| spacy-alrosait | 746 (100.0%) |

## Char recall by gold type

| type | group | traciora | pii-shield-onnx | opf-ru | apararti | opf-kz-ru | openai-base | nym-base | opf-ru-v2 | gliner-pii-edge | gitleaks | nym-small | ru-legal-ner | betterleaks | pplx | gliner2-fastino | gliner-stream-pii | gliner25-fastino | mmbert32k | bardsai-eu | openmed-multilingual | kalyan-ettin | openmed-nemotron | credsweeper-noml | credsweeper | rules-ru | gravitee-small | nuner-zero | gliner-nvidia | gliner-urchade | fef2-secret-ru | kingfisher | detect-secrets | gliner2-vladlinv | titus | deepsecrets | ner-ru-yqelz | trufflehog | gliner-pii-base | stanza-ru | gliner2-hivetrace-omni | noseyparker | gliner2-hivetrace-uni | ru-pii-ner | spacy-ru-lg | gliner2-large | gliner-multi-v21 | davlan-mbert | ner-ru-gherman | davlan-xlmr | natasha | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SECRET | SECRET | 0.997 | 0.999 | 0.995 | 0.998 | 0.993 | 0.986 | 0.970 | 0.987 | 0.957 | 0.971 | 0.945 | 0.862 | 0.970 | 0.949 | 0.894 | 0.843 | 0.849 | 0.835 | 0.925 | 0.871 | 0.794 | 0.861 | 0.793 | 0.741 | 0.709 | 0.708 | 0.678 | 0.674 | 0.487 | 0.398 | 0.488 | 0.484 | 0.282 | 0.449 | 0.392 | 0.221 | 0.235 | 0.158 | 0.175 | 0.176 | 0.165 | 0.085 | 0.084 | 0.102 | 0.038 | 0.023 | 0.001 | 0.001 | 0.000 | 0.000 | 0.000 |

## char F1 by domain

| domain | n | traciora | pii-shield-onnx | opf-ru | apararti | opf-kz-ru | openai-base | nym-base | opf-ru-v2 | gliner-pii-edge | gitleaks | nym-small | ru-legal-ner | betterleaks | pplx | gliner2-fastino | gliner-stream-pii | gliner25-fastino | mmbert32k | bardsai-eu | openmed-multilingual | kalyan-ettin | openmed-nemotron | credsweeper-noml | credsweeper | rules-ru | gravitee-small | nuner-zero | gliner-nvidia | gliner-urchade | fef2-secret-ru | kingfisher | detect-secrets | gliner2-vladlinv | titus | deepsecrets | ner-ru-yqelz | trufflehog | gliner-pii-base | stanza-ru | gliner2-hivetrace-omni | noseyparker | gliner2-hivetrace-uni | ru-pii-ner | spacy-ru-lg | gliner2-large | gliner-multi-v21 | davlan-mbert | ner-ru-gherman | davlan-xlmr | natasha | spacy-alrosait |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| betterleaks | 846 | 0.717 | 0.614 | 0.700 | 0.696 | 0.683 | 0.705 | 0.736 | 0.737 | 0.662 | 0.861 | 0.713 | 0.720 | 0.889 | 0.753 | 0.680 | 0.667 | 0.693 | 0.607 | 0.746 | 0.664 | 0.656 | 0.655 | 0.749 | 0.750 | 0.618 | 0.694 | 0.534 | 0.590 | 0.443 | 0.435 | 0.633 | 0.461 | 0.401 | 0.485 | 0.498 | 0.243 | 0.308 | 0.223 | 0.144 | 0.254 | 0.210 | 0.161 | 0.114 | 0.084 | 0.035 | 0.021 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| gitleaks | 650 | 0.740 | 0.590 | 0.734 | 0.697 | 0.718 | 0.733 | 0.751 | 0.772 | 0.669 | 0.971 | 0.713 | 0.667 | 0.948 | 0.754 | 0.688 | 0.772 | 0.688 | 0.647 | 0.735 | 0.673 | 0.652 | 0.656 | 0.801 | 0.790 | 0.667 | 0.656 | 0.588 | 0.626 | 0.504 | 0.437 | 0.644 | 0.440 | 0.382 | 0.562 | 0.539 | 0.252 | 0.410 | 0.208 | 0.201 | 0.251 | 0.284 | 0.135 | 0.146 | 0.228 | 0.066 | 0.049 | 0.004 | 0.002 | 0.000 | 0.000 | 0.000 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| traciora | 1 (0.1%) | 1 (0.1%) | 1 (0.1%) | 1 (0.1%) |
| opf-ru | 3 (0.4%) | 2 (0.3%) | 2 (0.3%) | 2 (0.3%) |
| apararti | 3 (0.4%) | 3 (0.4%) | 3 (0.4%) | 3 (0.4%) |
| opf-kz-ru | 5 (0.7%) | 5 (0.7%) | 5 (0.7%) | 5 (0.7%) |
| openai-base | 7 (0.9%) | 7 (0.9%) | 7 (0.9%) | 7 (0.9%) |
| nym-base | 8 (1.1%) | 5 (0.7%) | 5 (0.7%) | 5 (0.7%) |
| opf-ru-v2 | 9 (1.2%) | 9 (1.2%) | 9 (1.2%) | 9 (1.2%) |
| gliner-pii-edge | 13 (1.7%) | 4 (0.5%) | 1 (0.1%) | 0 (0.0%) |
| nym-small | 20 (2.7%) | 7 (0.9%) | 7 (0.9%) | 7 (0.9%) |
| ru-legal-ner | 23 (3.1%) | 14 (1.9%) | 13 (1.7%) | 13 (1.7%) |
| gliner2-fastino | 34 (4.6%) | 8 (1.1%) | 7 (0.9%) | 7 (0.9%) |
| gliner-stream-pii | 37 (5.0%) | 15 (2.0%) | 6 (0.8%) | 1 (0.1%) |
| gliner25-fastino | 43 (5.8%) | 22 (2.9%) | 20 (2.7%) | 14 (1.9%) |
| mmbert32k | 46 (6.2%) | 1 (0.1%) | 1 (0.1%) | 1 (0.1%) |
| bardsai-eu | 73 (9.8%) | 49 (6.6%) | 49 (6.6%) | 49 (6.6%) |
| openmed-multilingual | 90 (12.1%) | 70 (9.4%) | 70 (9.4%) | 70 (9.4%) |
| kalyan-ettin | 109 (14.6%) | 66 (8.8%) | 65 (8.7%) | 65 (8.7%) |
| openmed-nemotron | 110 (14.7%) | 82 (11.0%) | 82 (11.0%) | 82 (11.0%) |
| gravitee-small | 202 (27.1%) | 196 (26.3%) | 196 (26.3%) | 196 (26.3%) |
| nuner-zero | 205 (27.5%) | 95 (12.7%) | 59 (7.9%) | 34 (4.6%) |
| gliner-nvidia | 249 (33.4%) | 142 (19.0%) | 79 (10.6%) | 29 (3.9%) |
| gliner-urchade | 369 (49.5%) | 35 (4.7%) | 7 (0.9%) | 1 (0.1%) |
| fef2-secret-ru | 370 (49.6%) | 360 (48.3%) | 360 (48.3%) | 360 (48.3%) |
| gliner2-vladlinv | 416 (55.8%) | 405 (54.3%) | 398 (53.4%) | 390 (52.3%) |
| ner-ru-yqelz | 537 (72.0%) | 534 (71.6%) | 534 (71.6%) | 534 (71.6%) |
| gliner-pii-base | 581 (77.9%) | 104 (13.9%) | 3 (0.4%) | 0 (0.0%) |
| gliner2-hivetrace-omni | 612 (82.0%) | 107 (14.3%) | 36 (4.8%) | 25 (3.4%) |
| gliner2-hivetrace-uni | 635 (85.1%) | 243 (32.6%) | 72 (9.7%) | 17 (2.3%) |
| gliner2-large | 706 (94.6%) | 641 (85.9%) | 575 (77.1%) | 425 (57.0%) |
| gliner-multi-v21 | 722 (96.8%) | 255 (34.2%) | 55 (7.4%) | 4 (0.5%) |
| davlan-mbert | 745 (99.9%) | 745 (99.9%) | 745 (99.9%) | 745 (99.9%) |
| ner-ru-gherman | 745 (99.9%) | 745 (99.9%) | 745 (99.9%) | 745 (99.9%) |
| davlan-xlmr | 746 (100.0%) | 746 (100.0%) | 746 (100.0%) | 746 (100.0%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
