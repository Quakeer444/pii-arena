# jayguard - ru / pii (850 rows, 1195 spans, 170 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.030 (97.0% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gliner2-fastino | **126** | 10.5% [8.2%, 12.8%] | 77.6% | 0.585 [0.560, 0.613] | 0.433 | 0.902 | 0.302 | 0.600 | 0.581 | 116/170 | 2852 | 0 | 5 | 307M |  |
| gliner2-fastino-ru | **139** | 11.6% [9.2%, 14.0%] | 76.9% | 0.666 [0.642, 0.692] | 0.530 | 0.893 | 0.362 | 0.697 | 0.662 | 92/170 | 1439 | 0 | 9 | 307M |  |
| gliner25-fastino+sent300 | **154** | 12.9% [10.5%, 15.2%] | 75.0% | 0.560 [0.536, 0.587] | 0.409 | 0.887 | 0.276 | 0.563 | 0.555 | 117/170 | 2795 | 0 | 3 | 287M |  |
| nym-base | **156** | 13.1% [10.7%, 15.3%] | 56.3% | 0.546 [0.521, 0.574] | 0.401 | 0.856 | 0.246 | 0.506 | 0.035 | 111/170 | 2982 | 0 | 4 | 308M |  |
| gliner-urchade | **157** | 13.1% [10.7%, 15.5%] | 76.4% | 0.567 [0.544, 0.594] | 0.417 | 0.886 | 0.279 | 0.565 | 0.566 | 115/170 | 2689 | 0 | 4 | 289M |  |
| nym-base+ov100 | **157** | 13.1% [10.7%, 15.5%] | 56.4% | 0.544 [0.519, 0.572] | 0.399 | 0.856 | 0.246 | 0.504 | 0.035 | 113/170 | 3058 | 0 | 4 | 308M |  |
| gliner25-fastino+nochunk | **158** | 13.2% [10.7%, 15.6%] | 74.6% | 0.615 [0.592, 0.642] | 0.472 | 0.885 | 0.311 | 0.634 | 0.611 | 96/170 | 1827 | 0 | 8 | 287M |  |
| gliner-multi-v21 | **158** | 13.2% [10.6%, 15.7%] | 73.2% | 0.556 [0.534, 0.581] | 0.408 | 0.872 | 0.270 | 0.568 | 0.550 | 112/170 | 2814 | 0 | 4 | 289M |  |
| nym-base+sent300 | **158** | 13.2% [10.9%, 15.5%] | 56.3% | 0.540 [0.515, 0.569] | 0.395 | 0.856 | 0.244 | 0.498 | 0.035 | 112/170 | 3126 | 0 | 2 | 308M |  |
| gliner25-fastino+ov100 | **160** | 13.4% [10.9%, 15.7%] | 74.7% | 0.589 [0.564, 0.617] | 0.441 | 0.885 | 0.292 | 0.595 | 0.585 | 107/170 | 2305 | 0 | 4 | 287M |  |
| gliner25-fastino | **162** | 13.6% [11.1%, 15.9%] | 74.5% | 0.597 [0.573, 0.623] | 0.451 | 0.883 | 0.297 | 0.604 | 0.593 | 102/170 | 2107 | 0 | 3 | 287M |  |
| gliner2-hivetrace-omni | **165** | 13.8% [11.2%, 16.3%] | 73.7% | 0.588 [0.564, 0.614] | 0.440 | 0.885 | 0.298 | 0.615 | 0.573 | 124/170 | 2704 | 0 | 5 | 307M |  |
| gliner25-fastino-ru | **170** | 14.2% [11.8%, 16.7%] | 73.1% | 0.623 [0.600, 0.649] | 0.485 | 0.871 | 0.316 | 0.648 | 0.620 | 88/170 | 1471 | 0 | 6 | 287M |  |
| gliner25-fastino-ru+nochunk | **171** | 14.3% [12.0%, 16.7%] | 73.0% | 0.632 [0.610, 0.659] | 0.497 | 0.869 | 0.327 | 0.675 | 0.629 | 86/170 | 1530 | 0 | 12 | 287M |  |
| gliner2-hivetrace-omni-ru | **182** | 15.2% [12.6%, 17.9%] | 71.2% | 0.601 [0.576, 0.628] | 0.461 | 0.863 | 0.303 | 0.637 | 0.585 | 109/170 | 2150 | 0 | 8 | 307M |  |
| nuner-zero | **183** | 15.3% [12.7%, 18.0%] | 71.0% | 0.608 [0.585, 0.635] | 0.471 | 0.859 | 0.293 | 0.605 | 0.603 | 103/170 | 1948 | 0 | 8 | 449M |  |
| pplx+sent300 | **183** | 15.3% [12.8%, 17.7%] | 73.0% | 0.552 [0.529, 0.579] | 0.406 | 0.862 | 0.273 | 0.627 | 0.539 | 93/170 | 2692 | 0 | 71 | 596M |  |
| pplx+ov100 | **192** | 16.1% [13.4%, 18.7%] | 72.3% | 0.553 [0.528, 0.581] | 0.409 | 0.856 | 0.275 | 0.636 | 0.539 | 88/170 | 2449 | 0 | 69 | 596M |  |
| pplx | **197** | 16.5% [13.9%, 19.2%] | 72.0% | 0.555 [0.531, 0.584] | 0.412 | 0.853 | 0.277 | 0.635 | 0.543 | 87/170 | 2396 | 0 | 61 | 596M |  |
| davlan-xlmr | **204** | 17.1% [14.4%, 19.6%] | 67.2% | 0.617 [0.597, 0.640] | 0.491 | 0.832 | 0.302 | 0.648 | 0.354 | 95/170 | 1406 | 0 | 2 | 277M |  |
| bardsai-eu | **205** | 17.2% [14.4%, 19.7%] | 69.0% | 0.525 [0.496, 0.556] | 0.383 | 0.837 | 0.267 | 0.572 | 0.192 | 99/170 | 2497 | 0 | 580 | - |  |
| gliner-multi-v21-ru | **207** | 17.3% [14.5%, 20.0%] | 69.3% | 0.613 [0.591, 0.638] | 0.482 | 0.842 | 0.306 | 0.645 | 0.607 | 88/170 | 1582 | 0 | 8 | 289M |  |
| ner-ru-yqelz | **208** | 17.4% [14.8%, 20.0%] | 60.3% | 0.443 [0.416, 0.471] | 0.306 | 0.804 | 0.205 | 0.477 | 0.260 | 157/170 | 7069 | 0 | 3 | 559M |  |
| ru-legal-ner+sent300 | **236** | 19.7% [17.1%, 22.3%] | 61.7% | 0.445 [0.421, 0.473] | 0.309 | 0.794 | 0.160 | 0.471 | 0.348 | 140/170 | 5269 | 0 | 2 | 29M |  |
| fef2-secret-ru | **243** | 20.3% [17.5%, 23.4%] | 54.5% | 0.563 [0.539, 0.587] | 0.450 | 0.750 | 0.247 | 0.618 | 0.487 | 89/170 | 1383 | 0 | 3 | 177M |  |
| mmbert32k | **246** | 20.6% [17.9%, 23.3%] | 48.8% | 0.486 [0.462, 0.513] | 0.367 | 0.719 | 0.189 | 0.488 | 0.285 | 132/170 | 3547 | 0 | 3 | 308M |  |
| spacy-ru-lg | **248** | 20.8% [18.2%, 23.4%] | 52.6% | 0.488 [0.462, 0.514] | 0.369 | 0.720 | 0.219 | 0.537 | 0.325 | 125/170 | 3700 | 0 | 3 | - |  |
| ru-pii-ner | **250** | 20.9% [18.2%, 23.5%] | 67.8% | 0.556 [0.531, 0.584] | 0.430 | 0.788 | 0.303 | 0.617 | 0.354 | 79/170 | 1651 | 0 | 52 | 358M |  |
| ner-ru-gherman | **251** | 21.0% [18.1%, 23.9%] | 37.2% | 0.595 [0.576, 0.618] | 0.512 | 0.712 | 0.243 | 0.563 | 0.156 | 76/170 | 1005 | 0 | 3 | 177M |  |
| ru-legal-ner+ov100 | **259** | 21.7% [18.8%, 24.4%] | 59.4% | 0.461 [0.437, 0.489] | 0.328 | 0.778 | 0.168 | 0.490 | 0.357 | 135/170 | 4735 | 0 | 2 | 29M |  |
| ru-legal-ner | **265** | 22.2% [19.2%, 24.9%] | 59.0% | 0.467 [0.442, 0.495] | 0.334 | 0.777 | 0.170 | 0.498 | 0.364 | 132/170 | 4534 | 0 | 2 | 29M |  |
| gliner-nvidia+sent300 | **274** | 22.9% [20.0%, 25.6%] | 62.7% | 0.574 [0.548, 0.601] | 0.462 | 0.760 | 0.283 | 0.578 | 0.558 | 120/170 | 2252 | 0 | 9 | 445M |  |
| mmbert32k+nochunk | **288** | 24.1% [21.0%, 27.1%] | 45.9% | 0.480 [0.455, 0.508] | 0.368 | 0.690 | 0.184 | 0.468 | 0.272 | 129/170 | 3421 | 0 | 4 | 308M |  |
| gliner-nvidia+ov100 | **289** | 24.2% [21.3%, 27.3%] | 61.8% | 0.602 [0.577, 0.627] | 0.502 | 0.752 | 0.302 | 0.620 | 0.587 | 117/170 | 1776 | 0 | 10 | 445M |  |
| gliner-nvidia | **294** | 24.6% [21.6%, 27.6%] | 61.1% | 0.611 [0.587, 0.635] | 0.516 | 0.748 | 0.307 | 0.627 | 0.597 | 109/170 | 1582 | 0 | 8 | 445M |  |
| davlan-mbert | **294** | 24.6% [21.3%, 27.8%] | 55.2% | 0.572 [0.547, 0.597] | 0.469 | 0.734 | 0.256 | 0.596 | 0.345 | 102/170 | 1552 | 0 | 3 | 177M |  |
| gliner2-vladlinv-ru | **301** | 25.2% [22.3%, 28.2%] | 64.6% | 0.635 [0.614, 0.660] | 0.554 | 0.745 | 0.353 | 0.688 | 0.628 | 56/170 | 776 | 0 | 4 | 287M |  |
| gliner2-vladlinv | **301** | 25.2% [22.3%, 28.1%] | 64.5% | 0.630 [0.609, 0.655] | 0.547 | 0.743 | 0.353 | 0.686 | 0.623 | 56/170 | 810 | 0 | 4 | 287M |  |
| stanza-ru | **311** | 26.0% [22.7%, 29.3%] | 51.5% | 0.299 [0.272, 0.327] | 0.190 | 0.696 | 0.143 | 0.359 | 0.185 | 145/170 | 10139 | 0 | 35 | - |  |
| gliner2-large | **318** | 26.6% [23.5%, 29.6%] | 58.6% | 0.512 [0.487, 0.539] | 0.394 | 0.732 | 0.236 | 0.513 | 0.497 | 125/170 | 2770 | 0 | 9 | 486M |  |
| opf-ru | **320** | 26.8% [24.0%, 29.9%] | 49.0% | 0.460 [0.437, 0.486] | 0.342 | 0.704 | 0.178 | 0.475 | 0.399 | 139/170 | 3776 | 0 | 163 | 1.4B |  |
| gliner2-hivetrace-uni | **341** | 28.5% [25.5%, 31.3%] | 58.7% | 0.579 [0.554, 0.603] | 0.489 | 0.709 | 0.298 | 0.633 | 0.573 | 115/170 | 1906 | 0 | 8 | 147M |  |
| gliner-pii-edge | **344** | 28.8% [25.9%, 31.6%] | 46.9% | 0.495 [0.471, 0.517] | 0.402 | 0.643 | 0.196 | 0.504 | 0.431 | 136/170 | 2274 | 0 | 6 | 45M |  |
| gliner-nvidia-ru | **345** | 28.9% [26.1%, 31.8%] | 56.2% | 0.616 [0.594, 0.641] | 0.550 | 0.702 | 0.311 | 0.629 | 0.597 | 94/170 | 1126 | 0 | 26 | 445M |  |
| pii-shield-onnx | **379** | 31.7% [28.4%, 35.1%] | 47.7% | 0.408 [0.378, 0.441] | 0.290 | 0.692 | 0.180 | 0.460 | 0.271 | 132/170 | 6838 | 0 | 935 | - |  |
| traciora | **401** | 33.6% [30.6%, 36.5%] | 53.7% | 0.467 [0.445, 0.493] | 0.352 | 0.694 | 0.167 | 0.571 | 0.403 | 80/170 | 2098 | 0 | 226 | 1.4B |  |
| openmed-nemotron | **420** | 35.1% [32.0%, 38.2%] | 38.8% | 0.368 [0.348, 0.392] | 0.261 | 0.628 | 0.147 | 0.354 | 0.280 | 141/170 | 4914 | 0 | 141 | 1.4B |  |
| gliner-pii-base | **440** | 36.8% [33.5%, 40.0%] | 43.7% | 0.474 [0.449, 0.500] | 0.420 | 0.545 | 0.228 | 0.522 | 0.457 | 117/170 | 1813 | 0 | 3 | 166M |  |
| apararti | **458** | 38.3% [35.1%, 41.7%] | 48.5% | 0.423 [0.399, 0.450] | 0.312 | 0.654 | 0.126 | 0.504 | 0.362 | 99/170 | 3514 | 0 | 61 | 1.4B |  |
| gliner-stream-pii | **460** | 38.5% [35.5%, 41.7%] | 45.0% | 0.526 [0.503, 0.551] | 0.479 | 0.583 | 0.230 | 0.554 | 0.491 | 113/170 | 1237 | 0 | 30 | 677M |  |
| natasha | **465** | 38.9% [35.4%, 42.3%] | 44.4% | 0.420 [0.398, 0.447] | 0.338 | 0.556 | 0.194 | 0.470 | 0.320 | 121/170 | 2684 | 0 | 1 | - |  |
| spacy-alrosait | **481** | 40.3% [36.7%, 43.9%] | 48.2% | 0.537 [0.511, 0.565] | 0.471 | 0.623 | 0.208 | 0.573 | 0.205 | 98/170 | 1620 | 0 | 3 | - |  |
| opf-ru-v2+sent300 | **493** | 41.3% [37.6%, 44.6%] | 45.6% | 0.487 [0.463, 0.515] | 0.398 | 0.628 | 0.143 | 0.551 | 0.415 | 59/170 | 1425 | 0 | 533 | 1.4B |  |
| openmed-multilingual | **493** | 41.3% [37.9%, 44.4%] | 28.7% | 0.404 [0.380, 0.429] | 0.322 | 0.543 | 0.146 | 0.381 | 0.374 | 141/170 | 3297 | 0 | 139 | 1.4B |  |
| opf-ru-v2+ov100 | **496** | 41.5% [37.9%, 45.0%] | 45.5% | 0.492 [0.466, 0.519] | 0.406 | 0.623 | 0.149 | 0.561 | 0.418 | 56/170 | 1364 | 0 | 539 | 1.4B |  |
| opf-ru-v2 | **510** | 42.7% [39.0%, 46.1%] | 44.6% | 0.492 [0.467, 0.519] | 0.410 | 0.615 | 0.153 | 0.558 | 0.419 | 54/170 | 1302 | 0 | 224 | 1.4B |  |
| openai-base | **538** | 45.0% [41.5%, 48.6%] | 46.0% | 0.445 [0.420, 0.473] | 0.354 | 0.600 | 0.140 | 0.531 | 0.388 | 56/170 | 2104 | 0 | 268 | 1.4B |  |
| kalyan-ettin | **568** | 47.5% [44.2%, 51.0%] | 29.2% | 0.365 [0.341, 0.392] | 0.320 | 0.426 | 0.173 | 0.385 | 0.311 | 103/170 | 2418 | 0 | 3 | 68M |  |
| opf-kz-ru | **665** | 55.6% [52.2%, 58.8%] | 26.7% | 0.361 [0.337, 0.388] | 0.301 | 0.450 | 0.089 | 0.420 | 0.309 | 82/170 | 2667 | 0 | 53 | 1.4B |  |
| gliner-urchade-ru | **784** | 65.6% [62.2%, 68.7%] | 33.6% | 0.514 [0.477, 0.548] | 0.650 | 0.425 | 0.257 | 0.459 | 0.512 | 42/170 | 483 | 0 | 6 | 289M |  |
| gravitee-small | **841** | 70.4% [67.2%, 73.6%] | 22.0% | 0.255 [0.234, 0.277] | 0.208 | 0.330 | 0.023 | 0.310 | 0.244 | 96/170 | 3354 | 0 | 4 | 29M |  |
| gliner2-hivetrace-uni-ru | **899** | 75.2% [72.4%, 77.8%] | 18.1% | 0.276 [0.248, 0.306] | 0.384 | 0.215 | 0.150 | 0.323 | 0.267 | 70/170 | 1065 | 0 | 8 | 147M |  |
| rules-ru | **1194** | 99.9% [99.7%, 100.0%] | 0.1% | 0.000 [0.000, 0.001] | 0.001 | 0.000 | 0.000 | 0.001 | 0.000 | 16/170 | 957 | 0 | 0 | - |  |
| betterleaks | **1195** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/170 | 0 | 0 | 0 | - |  |
| gitleaks | **1195** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/170 | 0 | 0 | 0 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: gliner2-fastino-ru ≈ gliner25-fastino+sent300; gliner25-fastino+sent300 ≈ nym-base; nym-base ≈ gliner-urchade; gliner-urchade ≈ nym-base+ov100; nym-base+ov100 ≈ gliner25-fastino+nochunk; gliner25-fastino+nochunk ≈ gliner-multi-v21; gliner-multi-v21 ≈ nym-base+sent300; nym-base+sent300 ≈ gliner25-fastino+ov100; gliner25-fastino+ov100 ≈ gliner25-fastino; gliner25-fastino ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ gliner25-fastino-ru; gliner25-fastino-ru ≈ gliner25-fastino-ru+nochunk; gliner25-fastino-ru+nochunk ≈ gliner2-hivetrace-omni-ru; gliner2-hivetrace-omni-ru ≈ nuner-zero; nuner-zero ≈ pplx+sent300; pplx+sent300 ≈ pplx+ov100; pplx+ov100 ≈ pplx; pplx ≈ davlan-xlmr; davlan-xlmr ≈ bardsai-eu; bardsai-eu ≈ gliner-multi-v21-ru; gliner-multi-v21-ru ≈ ner-ru-yqelz; ner-ru-yqelz ≈ ru-legal-ner+sent300; ru-legal-ner+sent300 ≈ fef2-secret-ru; fef2-secret-ru ≈ mmbert32k; mmbert32k ≈ spacy-ru-lg; spacy-ru-lg ≈ ru-pii-ner; ru-pii-ner ≈ ner-ru-gherman; ner-ru-gherman ≈ ru-legal-ner+ov100; ru-legal-ner+ov100 ≈ ru-legal-ner; ru-legal-ner ≈ gliner-nvidia+sent300; gliner-nvidia+sent300 ≈ mmbert32k+nochunk; mmbert32k+nochunk ≈ gliner-nvidia+ov100; gliner-nvidia+ov100 ≈ gliner-nvidia; gliner-nvidia ≈ davlan-mbert; davlan-mbert ≈ gliner2-vladlinv-ru; gliner2-vladlinv-ru ≈ gliner2-vladlinv; gliner2-vladlinv ≈ stanza-ru; stanza-ru ≈ gliner2-large; gliner2-large ≈ opf-ru; opf-ru ≈ gliner2-hivetrace-uni; gliner2-hivetrace-uni ≈ gliner-pii-edge; gliner-pii-edge ≈ gliner-nvidia-ru; gliner-nvidia-ru ≈ pii-shield-onnx; pii-shield-onnx ≈ traciora; traciora ≈ openmed-nemotron; openmed-nemotron ≈ gliner-pii-base; gliner-pii-base ≈ apararti; apararti ≈ gliner-stream-pii; gliner-stream-pii ≈ natasha; natasha ≈ spacy-alrosait; spacy-alrosait ≈ opf-ru-v2+sent300; opf-ru-v2+sent300 ≈ openmed-multilingual; openmed-multilingual ≈ opf-ru-v2+ov100; opf-ru-v2 ≈ openai-base; openai-base ≈ kalyan-ettin; rules-ru ≈ betterleaks; betterleaks ≈ gitleaks

Legacy runs on this set: betterleaks. Their meta carries no `protocol` and no `bench_sha256`, so the version of the text they were taken from is confirmed only by the row and character counts, not by a fingerprint.

## Missed by group

| model | PERSON | ADDRESS |
|---|---|---|
| spans in gold | 806 | 389 |
| gliner2-fastino | 102 (12.7%) | 24 (6.2%) |
| gliner2-fastino-ru | 109 (13.5%) | 30 (7.7%) |
| gliner25-fastino+sent300 | 114 (14.1%) | 40 (10.3%) |
| nym-base | 130 (16.1%) | 26 (6.7%) |
| gliner-urchade | 121 (15.0%) | 36 (9.3%) |
| nym-base+ov100 | 131 (16.3%) | 26 (6.7%) |
| gliner25-fastino+nochunk | 118 (14.6%) | 40 (10.3%) |
| gliner-multi-v21 | 121 (15.0%) | 37 (9.5%) |
| nym-base+sent300 | 132 (16.4%) | 26 (6.7%) |
| gliner25-fastino+ov100 | 120 (14.9%) | 40 (10.3%) |
| gliner25-fastino | 122 (15.1%) | 40 (10.3%) |
| gliner2-hivetrace-omni | 141 (17.5%) | 24 (6.2%) |
| gliner25-fastino-ru | 126 (15.6%) | 44 (11.3%) |
| gliner25-fastino-ru+nochunk | 127 (15.8%) | 44 (11.3%) |
| gliner2-hivetrace-omni-ru | 156 (19.4%) | 26 (6.7%) |
| nuner-zero | 128 (15.9%) | 55 (14.1%) |
| pplx+sent300 | 121 (15.0%) | 62 (15.9%) |
| pplx+ov100 | 130 (16.1%) | 62 (15.9%) |
| pplx | 135 (16.7%) | 62 (15.9%) |
| davlan-xlmr | 143 (17.7%) | 61 (15.7%) |
| bardsai-eu | 142 (17.6%) | 63 (16.2%) |
| gliner-multi-v21-ru | 175 (21.7%) | 32 (8.2%) |
| ner-ru-yqelz | 142 (17.6%) | 66 (17.0%) |
| ru-legal-ner+sent300 | 153 (19.0%) | 83 (21.3%) |
| fef2-secret-ru | 155 (19.2%) | 88 (22.6%) |
| mmbert32k | 170 (21.1%) | 76 (19.5%) |
| spacy-ru-lg | 139 (17.2%) | 109 (28.0%) |
| ru-pii-ner | 107 (13.3%) | 143 (36.8%) |
| ner-ru-gherman | 165 (20.5%) | 86 (22.1%) |
| ru-legal-ner+ov100 | 176 (21.8%) | 83 (21.3%) |
| ru-legal-ner | 182 (22.6%) | 83 (21.3%) |
| gliner-nvidia+sent300 | 233 (28.9%) | 41 (10.5%) |
| mmbert32k+nochunk | 212 (26.3%) | 76 (19.5%) |
| gliner-nvidia+ov100 | 248 (30.8%) | 41 (10.5%) |
| gliner-nvidia | 253 (31.4%) | 41 (10.5%) |
| davlan-mbert | 188 (23.3%) | 106 (27.2%) |
| gliner2-vladlinv-ru | 122 (15.1%) | 179 (46.0%) |
| gliner2-vladlinv | 119 (14.8%) | 182 (46.8%) |
| stanza-ru | 191 (23.7%) | 120 (30.8%) |
| gliner2-large | 265 (32.9%) | 53 (13.6%) |
| opf-ru | 207 (25.7%) | 113 (29.0%) |
| gliner2-hivetrace-uni | 220 (27.3%) | 121 (31.1%) |
| gliner-pii-edge | 225 (27.9%) | 119 (30.6%) |
| gliner-nvidia-ru | 304 (37.7%) | 41 (10.5%) |
| pii-shield-onnx | 267 (33.1%) | 112 (28.8%) |
| traciora | 267 (33.1%) | 134 (34.4%) |
| openmed-nemotron | 283 (35.1%) | 137 (35.2%) |
| gliner-pii-base | 238 (29.5%) | 202 (51.9%) |
| apararti | 343 (42.6%) | 115 (29.6%) |
| gliner-stream-pii | 313 (38.8%) | 147 (37.8%) |
| natasha | 224 (27.8%) | 241 (62.0%) |
| spacy-alrosait | 342 (42.4%) | 139 (35.7%) |
| opf-ru-v2+sent300 | 348 (43.2%) | 145 (37.3%) |
| openmed-multilingual | 396 (49.1%) | 97 (24.9%) |
| opf-ru-v2+ov100 | 351 (43.5%) | 145 (37.3%) |
| opf-ru-v2 | 363 (45.0%) | 147 (37.8%) |
| openai-base | 398 (49.4%) | 140 (36.0%) |
| kalyan-ettin | 359 (44.5%) | 209 (53.7%) |
| opf-kz-ru | 472 (58.6%) | 193 (49.6%) |
| gliner-urchade-ru | 744 (92.3%) | 40 (10.3%) |
| gravitee-small | 698 (86.6%) | 143 (36.8%) |
| gliner2-hivetrace-uni-ru | 573 (71.1%) | 326 (83.8%) |
| rules-ru | 805 (99.9%) | 389 (100.0%) |
| betterleaks | 806 (100.0%) | 389 (100.0%) |
| gitleaks | 806 (100.0%) | 389 (100.0%) |

## Char recall by gold type

| type | group | gliner2-fastino | gliner2-fastino-ru | gliner25-fastino+sent300 | nym-base | gliner-urchade | nym-base+ov100 | gliner25-fastino+nochunk | gliner-multi-v21 | nym-base+sent300 | gliner25-fastino+ov100 | gliner25-fastino | gliner2-hivetrace-omni | gliner25-fastino-ru | gliner25-fastino-ru+nochunk | gliner2-hivetrace-omni-ru | nuner-zero | pplx+sent300 | pplx+ov100 | pplx | davlan-xlmr | bardsai-eu | gliner-multi-v21-ru | ner-ru-yqelz | ru-legal-ner+sent300 | fef2-secret-ru | mmbert32k | spacy-ru-lg | ru-pii-ner | ner-ru-gherman | ru-legal-ner+ov100 | ru-legal-ner | gliner-nvidia+sent300 | mmbert32k+nochunk | gliner-nvidia+ov100 | gliner-nvidia | davlan-mbert | gliner2-vladlinv-ru | gliner2-vladlinv | stanza-ru | gliner2-large | opf-ru | gliner2-hivetrace-uni | gliner-pii-edge | gliner-nvidia-ru | pii-shield-onnx | traciora | openmed-nemotron | gliner-pii-base | apararti | gliner-stream-pii | natasha | spacy-alrosait | opf-ru-v2+sent300 | openmed-multilingual | opf-ru-v2+ov100 | opf-ru-v2 | openai-base | kalyan-ettin | opf-kz-ru | gliner-urchade-ru | gravitee-small | gliner2-hivetrace-uni-ru | rules-ru | betterleaks | gitleaks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GPE | ADDRESS | 0.843 | 0.788 | 0.664 | 0.796 | 0.803 | 0.796 | 0.664 | 0.658 | 0.796 | 0.664 | 0.664 | 0.839 | 0.635 | 0.635 | 0.786 | 0.531 | 0.612 | 0.612 | 0.612 | 0.855 | 0.791 | 0.685 | 0.856 | 0.459 | 0.700 | 0.649 | 0.753 | 0.473 | 0.639 | 0.459 | 0.459 | 0.663 | 0.649 | 0.663 | 0.663 | 0.703 | 0.282 | 0.279 | 0.546 | 0.731 | 0.311 | 0.689 | 0.593 | 0.699 | 0.517 | 0.330 | 0.387 | 0.484 | 0.330 | 0.450 | 0.473 | 0.460 | 0.227 | 0.400 | 0.227 | 0.217 | 0.262 | 0.345 | 0.152 | 0.783 | 0.274 | 0.414 | 0.000 | 0.000 | 0.000 |
| PER | PERSON | 0.892 | 0.881 | 0.883 | 0.846 | 0.867 | 0.846 | 0.878 | 0.872 | 0.846 | 0.878 | 0.875 | 0.846 | 0.869 | 0.866 | 0.819 | 0.868 | 0.862 | 0.852 | 0.848 | 0.848 | 0.845 | 0.811 | 0.852 | 0.840 | 0.836 | 0.771 | 0.853 | 0.882 | 0.794 | 0.812 | 0.810 | 0.680 | 0.722 | 0.666 | 0.659 | 0.787 | 0.874 | 0.876 | 0.778 | 0.693 | 0.761 | 0.746 | 0.726 | 0.580 | 0.713 | 0.707 | 0.652 | 0.726 | 0.615 | 0.617 | 0.744 | 0.623 | 0.616 | 0.488 | 0.607 | 0.596 | 0.555 | 0.513 | 0.444 | 0.069 | 0.137 | 0.279 | 0.000 | 0.000 | 0.000 |
| STREET_ADDRESS | ADDRESS | 0.932 | 0.936 | 0.943 | 0.884 | 0.935 | 0.884 | 0.943 | 0.918 | 0.884 | 0.943 | 0.943 | 0.959 | 0.923 | 0.923 | 0.951 | 0.914 | 0.913 | 0.913 | 0.913 | 0.800 | 0.833 | 0.925 | 0.715 | 0.791 | 0.620 | 0.647 | 0.496 | 0.703 | 0.593 | 0.791 | 0.791 | 0.910 | 0.647 | 0.910 | 0.910 | 0.653 | 0.633 | 0.624 | 0.594 | 0.795 | 0.695 | 0.654 | 0.519 | 0.901 | 0.694 | 0.749 | 0.639 | 0.263 | 0.787 | 0.555 | 0.269 | 0.658 | 0.733 | 0.661 | 0.733 | 0.729 | 0.746 | 0.302 | 0.522 | 0.929 | 0.656 | 0.069 | 0.000 | 0.000 | 0.000 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| gliner2-fastino | 126 (10.5%) | 112 (9.4%) | 106 (8.9%) | 99 (8.3%) |
| gliner2-fastino-ru | 139 (11.6%) | 122 (10.2%) | 116 (9.7%) | 107 (9.0%) |
| gliner25-fastino+sent300 | 154 (12.9%) | 140 (11.7%) | 133 (11.1%) | 128 (10.7%) |
| nym-base | 156 (13.1%) | 149 (12.5%) | 149 (12.5%) | 149 (12.5%) |
| gliner-urchade | 157 (13.1%) | 121 (10.1%) | 112 (9.4%) | 107 (9.0%) |
| nym-base+ov100 | 157 (13.1%) | 152 (12.7%) | 152 (12.7%) | 152 (12.7%) |
| gliner25-fastino+nochunk | 158 (13.2%) | 142 (11.9%) | 133 (11.1%) | 123 (10.3%) |
| gliner-multi-v21 | 158 (13.2%) | 126 (10.5%) | 108 (9.0%) | 95 (7.9%) |
| nym-base+sent300 | 158 (13.2%) | 150 (12.6%) | 150 (12.6%) | 150 (12.6%) |
| gliner25-fastino+ov100 | 160 (13.4%) | 145 (12.1%) | 135 (11.3%) | 130 (10.9%) |
| gliner25-fastino | 162 (13.6%) | 151 (12.6%) | 142 (11.9%) | 137 (11.5%) |
| gliner2-hivetrace-omni | 165 (13.8%) | 144 (12.1%) | 129 (10.8%) | 112 (9.4%) |
| gliner25-fastino-ru | 170 (14.2%) | 159 (13.3%) | 152 (12.7%) | 143 (12.0%) |
| gliner25-fastino-ru+nochunk | 171 (14.3%) | 150 (12.6%) | 140 (11.7%) | 131 (11.0%) |
| gliner2-hivetrace-omni-ru | 182 (15.2%) | 149 (12.5%) | 134 (11.2%) | 117 (9.8%) |
| nuner-zero | 183 (15.3%) | 143 (12.0%) | 123 (10.3%) | 109 (9.1%) |
| davlan-xlmr | 204 (17.1%) | 201 (16.8%) | 201 (16.8%) | 201 (16.8%) |
| bardsai-eu | 205 (17.2%) | 203 (17.0%) | 203 (17.0%) | 203 (17.0%) |
| gliner-multi-v21-ru | 207 (17.3%) | 139 (11.6%) | 116 (9.7%) | 99 (8.3%) |
| ner-ru-yqelz | 208 (17.4%) | 193 (16.2%) | 193 (16.2%) | 193 (16.2%) |
| ru-legal-ner+sent300 | 236 (19.7%) | 195 (16.3%) | 187 (15.6%) | 185 (15.5%) |
| fef2-secret-ru | 243 (20.3%) | 216 (18.1%) | 211 (17.7%) | 209 (17.5%) |
| mmbert32k | 246 (20.6%) | 166 (13.9%) | 158 (13.2%) | 157 (13.1%) |
| ner-ru-gherman | 251 (21.0%) | 242 (20.3%) | 240 (20.1%) | 240 (20.1%) |
| ru-legal-ner+ov100 | 259 (21.7%) | 217 (18.2%) | 207 (17.3%) | 206 (17.2%) |
| ru-legal-ner | 265 (22.2%) | 224 (18.7%) | 213 (17.8%) | 212 (17.7%) |
| gliner-nvidia+sent300 | 274 (22.9%) | 207 (17.3%) | 175 (14.6%) | 133 (11.1%) |
| mmbert32k+nochunk | 288 (24.1%) | 180 (15.1%) | 169 (14.1%) | 166 (13.9%) |
| gliner-nvidia+ov100 | 289 (24.2%) | 221 (18.5%) | 187 (15.6%) | 141 (11.8%) |
| gliner-nvidia | 294 (24.6%) | 226 (18.9%) | 189 (15.8%) | 148 (12.4%) |
| davlan-mbert | 294 (24.6%) | 291 (24.4%) | 291 (24.4%) | 291 (24.4%) |
| gliner2-vladlinv-ru | 301 (25.2%) | 290 (24.3%) | 289 (24.2%) | 287 (24.0%) |
| gliner2-vladlinv | 301 (25.2%) | 294 (24.6%) | 287 (24.0%) | 286 (23.9%) |
| gliner2-large | 318 (26.6%) | 246 (20.6%) | 216 (18.1%) | 173 (14.5%) |
| opf-ru | 320 (26.8%) | 316 (26.4%) | 316 (26.4%) | 316 (26.4%) |
| gliner2-hivetrace-uni | 341 (28.5%) | 241 (20.2%) | 193 (16.2%) | 161 (13.5%) |
| gliner-pii-edge | 344 (28.8%) | 152 (12.7%) | 111 (9.3%) | 75 (6.3%) |
| gliner-nvidia-ru | 345 (28.9%) | 263 (22.0%) | 224 (18.7%) | 185 (15.5%) |
| pii-shield-onnx | 379 (31.7%) | 332 (27.8%) | 326 (27.3%) | 325 (27.2%) |
| traciora | 401 (33.6%) | 399 (33.4%) | 399 (33.4%) | 399 (33.4%) |
| openmed-nemotron | 420 (35.1%) | 349 (29.2%) | 348 (29.1%) | 348 (29.1%) |
| gliner-pii-base | 440 (36.8%) | 172 (14.4%) | 115 (9.6%) | 90 (7.5%) |
| apararti | 458 (38.3%) | 454 (38.0%) | 454 (38.0%) | 454 (38.0%) |
| gliner-stream-pii | 460 (38.5%) | 345 (28.9%) | 291 (24.4%) | 236 (19.7%) |
| opf-ru-v2+sent300 | 493 (41.3%) | 490 (41.0%) | 490 (41.0%) | 490 (41.0%) |
| openmed-multilingual | 493 (41.3%) | 426 (35.6%) | 422 (35.3%) | 422 (35.3%) |
| opf-ru-v2+ov100 | 496 (41.5%) | 494 (41.3%) | 494 (41.3%) | 494 (41.3%) |
| opf-ru-v2 | 510 (42.7%) | 507 (42.4%) | 507 (42.4%) | 507 (42.4%) |
| openai-base | 538 (45.0%) | 536 (44.9%) | 536 (44.9%) | 536 (44.9%) |
| kalyan-ettin | 568 (47.5%) | 439 (36.7%) | 421 (35.2%) | 420 (35.1%) |
| opf-kz-ru | 665 (55.6%) | 662 (55.4%) | 662 (55.4%) | 662 (55.4%) |
| gliner-urchade-ru | 784 (65.6%) | 719 (60.2%) | 647 (54.1%) | 543 (45.4%) |
| gravitee-small | 841 (70.4%) | 815 (68.2%) | 815 (68.2%) | 815 (68.2%) |
| gliner2-hivetrace-uni-ru | 899 (75.2%) | 566 (47.4%) | 401 (33.6%) | 222 (18.6%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
