# factrueval - ru / pii (254 rows, 7966 spans, 0 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.120 (88.0% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| stanza-ru | **261** | 3.3% [2.8%, 3.8%] | 95.6% | 0.877 [0.866, 0.887] | 0.840 | 0.916 | 0.606 | 0.948 | 0.545 | 0/0 | 0 | 0 | 191 | - |  |
| fef2-secret-ru | **272** | 3.4% [2.8%, 4.1%] | 95.3% | 0.928 [0.921, 0.936] | 0.930 | 0.927 | 0.674 | 0.968 | 0.900 | 0/0 | 0 | 0 | 15 | 177M |  |
| davlan-xlmr | **317** | 4.0% [3.4%, 4.7%] | 94.7% | 0.927 [0.920, 0.933] | 0.936 | 0.918 | 0.607 | 0.974 | 0.649 | 0/0 | 0 | 0 | 17 | 277M |  |
| natasha | **350** | 4.4% [3.8%, 5.1%] | 94.4% | 0.925 [0.917, 0.932] | 0.938 | 0.911 | 0.671 | 0.966 | 0.638 | 0/0 | 0 | 0 | 10 | - |  |
| davlan-mbert | **364** | 4.6% [4.0%, 5.3%] | 94.0% | 0.924 [0.916, 0.930] | 0.943 | 0.905 | 0.633 | 0.970 | 0.642 | 0/0 | 0 | 0 | 20 | 177M |  |
| spacy-ru-lg | **367** | 4.6% [3.8%, 5.5%] | 93.9% | 0.918 [0.910, 0.926] | 0.923 | 0.913 | 0.662 | 0.962 | 0.630 | 0/0 | 0 | 0 | 25 | - |  |
| bardsai-eu | **466** | 5.8% [5.0%, 6.8%] | 93.0% | 0.829 [0.818, 0.841] | 0.756 | 0.919 | 0.550 | 0.903 | 0.204 | 0/0 | 0 | 0 | 2880 | - |  |
| nym-base+ov100 | **839** | 10.5% [8.9%, 12.5%] | 88.0% | 0.788 [0.774, 0.801] | 0.722 | 0.866 | 0.528 | 0.849 | 0.314 | 0/0 | 0 | 0 | 19 | 308M |  |
| nym-base | **903** | 11.3% [9.6%, 13.3%] | 87.2% | 0.792 [0.777, 0.804] | 0.735 | 0.857 | 0.548 | 0.852 | 0.314 | 0/0 | 0 | 0 | 16 | 308M |  |
| gliner2-fastino-ru | **970** | 12.2% [11.0%, 13.4%] | 87.1% | 0.764 [0.747, 0.782] | 0.680 | 0.872 | 0.626 | 0.834 | 0.519 | 0/0 | 0 | 0 | 52 | 307M |  |
| nym-base+sent300 | **1068** | 13.4% [11.6%, 15.3%] | 85.0% | 0.788 [0.776, 0.800] | 0.747 | 0.833 | 0.553 | 0.849 | 0.308 | 0/0 | 0 | 0 | 18 | 308M |  |
| nym-small | **1090** | 13.7% [11.9%, 15.4%] | 84.7% | 0.790 [0.778, 0.802] | 0.755 | 0.829 | 0.551 | 0.847 | 0.296 | 0/0 | 0 | 0 | 426 | - |  |
| gliner-pii-edge | **1227** | 15.4% [14.1%, 16.7%] | 81.5% | 0.733 [0.716, 0.749] | 0.712 | 0.756 | 0.546 | 0.813 | 0.308 | 0/0 | 0 | 0 | 427 | 45M |  |
| gliner2-fastino | **1362** | 17.1% [15.5%, 18.6%] | 81.9% | 0.758 [0.740, 0.775] | 0.699 | 0.828 | 0.753 | 0.813 | 0.493 | 0/0 | 0 | 0 | 32 | 307M |  |
| gliner-nvidia+sent300 | **1435** | 18.0% [16.7%, 19.5%] | 80.9% | 0.811 [0.798, 0.823] | 0.825 | 0.799 | 0.804 | 0.861 | 0.557 | 0/0 | 0 | 0 | 59 | 445M |  |
| ner-ru-yqelz | **1598** | 20.1% [18.4%, 21.7%] | 78.8% | 0.773 [0.757, 0.788] | 0.744 | 0.804 | 0.457 | 0.829 | 0.522 | 0/0 | 0 | 0 | 23 | 559M |  |
| gliner25-fastino-ru | **1735** | 21.8% [20.2%, 23.5%] | 77.5% | 0.798 [0.783, 0.811] | 0.815 | 0.783 | 0.549 | 0.839 | 0.579 | 0/0 | 0 | 0 | 39 | 287M |  |
| gliner-multi-v21 | **1891** | 23.7% [21.7%, 25.9%] | 75.4% | 0.760 [0.744, 0.776] | 0.767 | 0.753 | 0.530 | 0.817 | 0.532 | 0/0 | 0 | 0 | 23 | 289M |  |
| gliner-nvidia+ov100 | **1998** | 25.1% [23.4%, 26.8%] | 73.8% | 0.813 [0.799, 0.826] | 0.928 | 0.723 | 0.796 | 0.843 | 0.574 | 0/0 | 0 | 0 | 45 | 445M |  |
| gliner-nvidia | **2005** | 25.2% [23.4%, 27.0%] | 73.8% | 0.804 [0.790, 0.816] | 0.900 | 0.725 | 0.786 | 0.837 | 0.565 | 0/0 | 0 | 0 | 54 | 445M |  |
| gliner-multi-v21-ru | **2115** | 26.6% [24.7%, 28.5%] | 72.6% | 0.754 [0.739, 0.770] | 0.780 | 0.730 | 0.500 | 0.805 | 0.547 | 0/0 | 0 | 0 | 46 | 289M |  |
| gliner2-large | **2266** | 28.4% [26.3%, 30.6%] | 70.6% | 0.704 [0.683, 0.721] | 0.709 | 0.698 | 0.522 | 0.765 | 0.471 | 0/0 | 0 | 0 | 79 | 486M |  |
| gliner2-hivetrace-omni | **2329** | 29.2% [27.2%, 31.4%] | 69.8% | 0.741 [0.720, 0.761] | 0.805 | 0.687 | 0.734 | 0.787 | 0.505 | 0/0 | 0 | 0 | 32 | 307M |  |
| ner-ru-gherman | **2451** | 30.8% [27.7%, 33.9%] | 66.4% | 0.732 [0.703, 0.758] | 0.978 | 0.584 | 0.778 | 0.812 | 0.073 | 0/0 | 0 | 0 | 21 | 177M |  |
| gliner2-hivetrace-omni-ru | **2488** | 31.2% [29.1%, 33.6%] | 68.0% | 0.744 [0.726, 0.760] | 0.825 | 0.678 | 0.653 | 0.782 | 0.523 | 0/0 | 0 | 0 | 43 | 307M |  |
| ru-legal-ner+sent300 | **3158** | 39.6% [36.7%, 42.9%] | 57.2% | 0.579 [0.559, 0.597] | 0.590 | 0.568 | 0.159 | 0.655 | 0.445 | 0/0 | 0 | 0 | 13 | 29M |  |
| gliner25-fastino+sent300 | **3202** | 40.2% [38.1%, 42.5%] | 59.1% | 0.648 [0.628, 0.668] | 0.667 | 0.631 | 0.592 | 0.673 | 0.364 | 0/0 | 0 | 0 | 16 | 287M |  |
| gliner25-fastino | **3450** | 43.3% [40.8%, 46.0%] | 56.0% | 0.662 [0.640, 0.684] | 0.747 | 0.594 | 0.603 | 0.678 | 0.365 | 0/0 | 0 | 0 | 18 | 287M |  |
| gliner25-fastino+ov100 | **3465** | 43.5% [40.8%, 46.2%] | 55.8% | 0.666 [0.643, 0.690] | 0.758 | 0.595 | 0.605 | 0.679 | 0.369 | 0/0 | 0 | 0 | 17 | 287M |  |
| ru-legal-ner | **3491** | 43.8% [40.8%, 47.4%] | 53.4% | 0.570 [0.548, 0.591] | 0.622 | 0.525 | 0.161 | 0.641 | 0.448 | 0/0 | 0 | 0 | 12 | 29M |  |
| ru-legal-ner+ov100 | **3506** | 44.0% [41.1%, 47.4%] | 53.1% | 0.564 [0.542, 0.585] | 0.617 | 0.519 | 0.156 | 0.641 | 0.444 | 0/0 | 0 | 0 | 14 | 29M |  |
| nuner-zero | **3600** | 45.2% [42.4%, 48.0%] | 53.6% | 0.666 [0.643, 0.689] | 0.798 | 0.572 | 0.605 | 0.671 | 0.371 | 0/0 | 0 | 0 | 60 | 449M |  |
| gliner-nvidia-ru | **3725** | 46.8% [44.8%, 48.9%] | 52.5% | 0.667 [0.647, 0.684] | 0.920 | 0.523 | 0.639 | 0.685 | 0.527 | 0/0 | 0 | 0 | 128 | 445M |  |
| spacy-alrosait | **3781** | 47.5% [45.1%, 50.0%] | 51.0% | 0.610 [0.585, 0.631] | 0.920 | 0.456 | 0.322 | 0.686 | 0.194 | 0/0 | 0 | 0 | 24 | - |  |
| gliner25-fastino-ru+nochunk | **3863** | 48.5% [44.3%, 52.5%] | 50.7% | 0.666 [0.633, 0.698] | 0.865 | 0.542 | 0.464 | 0.667 | 0.463 | 0/0 | 0 | 0 | 33 | 287M |  |
| mmbert32k | **4319** | 54.2% [51.4%, 57.1%] | 42.2% | 0.542 [0.515, 0.568] | 0.841 | 0.399 | 0.317 | 0.576 | 0.420 | 0/0 | 0 | 0 | 20 | 308M |  |
| gliner25-fastino+nochunk | **4424** | 55.5% [51.8%, 59.3%] | 43.6% | 0.611 [0.577, 0.643] | 0.840 | 0.480 | 0.535 | 0.600 | 0.349 | 0/0 | 0 | 0 | 36 | 287M |  |
| kalyan-ettin | **4452** | 55.9% [53.8%, 57.8%] | 40.8% | 0.526 [0.506, 0.545] | 0.831 | 0.385 | 0.492 | 0.582 | 0.413 | 0/0 | 0 | 0 | 110 | 68M |  |
| openmed-nemotron | **4477** | 56.2% [54.2%, 58.2%] | 40.2% | 0.449 [0.430, 0.468] | 0.511 | 0.401 | 0.373 | 0.521 | 0.311 | 0/0 | 0 | 0 | 126 | 1.4B |  |
| gliner-stream-pii | **4546** | 57.1% [54.5%, 59.4%] | 41.1% | 0.545 [0.524, 0.569] | 0.832 | 0.406 | 0.491 | 0.582 | 0.217 | 0/0 | 0 | 0 | 160 | 677M |  |
| pii-shield-onnx | **4619** | 58.0% [55.8%, 60.4%] | 39.9% | 0.511 [0.485, 0.535] | 0.773 | 0.382 | 0.271 | 0.551 | 0.352 | 0/0 | 0 | 0 | 6463 | - |  |
| gliner-pii-base | **4621** | 58.0% [55.7%, 60.4%] | 40.7% | 0.543 [0.521, 0.565] | 0.782 | 0.416 | 0.507 | 0.563 | 0.308 | 0/0 | 0 | 0 | 18 | 166M |  |
| gliner-urchade | **4733** | 59.4% [56.6%, 62.3%] | 40.1% | 0.536 [0.510, 0.562] | 0.639 | 0.461 | 0.412 | 0.536 | 0.341 | 0/0 | 0 | 0 | 23 | 289M |  |
| gliner2-hivetrace-uni-ru | **4898** | 61.5% [59.2%, 63.6%] | 38.1% | 0.505 [0.483, 0.529] | 0.873 | 0.355 | 0.275 | 0.546 | 0.433 | 0/0 | 0 | 0 | 45 | 147M |  |
| opf-ru | **4920** | 61.8% [59.1%, 64.5%] | 36.4% | 0.471 [0.445, 0.499] | 0.799 | 0.334 | 0.199 | 0.529 | 0.360 | 0/0 | 0 | 0 | 155 | 1.4B |  |
| gliner-urchade-ru | **4974** | 62.4% [59.6%, 65.2%] | 37.1% | 0.511 [0.485, 0.538] | 0.623 | 0.434 | 0.379 | 0.507 | 0.335 | 0/0 | 0 | 0 | 36 | 289M |  |
| openmed-multilingual | **5233** | 65.7% [63.7%, 67.5%] | 31.8% | 0.427 [0.405, 0.448] | 0.728 | 0.302 | 0.362 | 0.457 | 0.316 | 0/0 | 0 | 0 | 147 | 1.4B |  |
| gliner2-vladlinv | **5294** | 66.5% [63.6%, 69.4%] | 33.4% | 0.440 [0.407, 0.472] | 0.938 | 0.287 | 0.140 | 0.502 | 0.351 | 0/0 | 0 | 0 | 23 | 287M |  |
| traciora | **5413** | 68.0% [64.8%, 71.2%] | 31.0% | 0.419 [0.389, 0.449] | 0.720 | 0.296 | 0.117 | 0.474 | 0.303 | 0/0 | 0 | 0 | 195 | 1.4B |  |
| gliner2-vladlinv-ru | **5452** | 68.4% [65.5%, 71.3%] | 31.5% | 0.421 [0.387, 0.455] | 0.937 | 0.272 | 0.134 | 0.479 | 0.366 | 0/0 | 0 | 0 | 33 | 287M |  |
| ru-pii-ner | **5589** | 70.2% [66.7%, 73.8%] | 29.8% | 0.401 [0.360, 0.441] | 0.863 | 0.261 | 0.114 | 0.456 | 0.306 | 0/0 | 0 | 0 | 246 | 358M |  |
| pplx+sent300 | **5776** | 72.5% [69.5%, 75.7%] | 27.4% | 0.370 [0.334, 0.402] | 0.829 | 0.238 | 0.122 | 0.421 | 0.352 | 0/0 | 0 | 0 | 384 | 596M |  |
| mmbert32k+nochunk | **5805** | 72.9% [70.6%, 75.1%] | 24.5% | 0.359 [0.334, 0.386] | 0.787 | 0.233 | 0.256 | 0.386 | 0.264 | 0/0 | 0 | 0 | 28 | 308M |  |
| opf-ru-v2+sent300 | **5810** | 72.9% [70.5%, 75.6%] | 26.3% | 0.373 [0.343, 0.400] | 0.820 | 0.241 | 0.060 | 0.421 | 0.307 | 0/0 | 0 | 0 | 28 | 1.4B |  |
| apararti | **5852** | 73.5% [70.7%, 76.1%] | 25.8% | 0.354 [0.324, 0.385] | 0.685 | 0.239 | 0.075 | 0.401 | 0.279 | 0/0 | 0 | 0 | 254 | 1.4B |  |
| opf-ru-v2+ov100 | **5992** | 75.2% [72.8%, 77.8%] | 24.3% | 0.347 [0.318, 0.374] | 0.834 | 0.219 | 0.049 | 0.394 | 0.292 | 0/0 | 0 | 0 | 2173 | 1.4B |  |
| opf-ru-v2 | **6060** | 76.1% [73.7%, 78.5%] | 23.3% | 0.340 [0.313, 0.367] | 0.846 | 0.213 | 0.048 | 0.383 | 0.286 | 0/0 | 0 | 0 | 998 | 1.4B |  |
| pplx+ov100 | **6615** | 83.0% [80.4%, 85.8%] | 16.9% | 0.246 [0.209, 0.279] | 0.863 | 0.144 | 0.062 | 0.287 | 0.240 | 0/0 | 0 | 0 | 259 | 596M |  |
| opf-kz-ru | **6743** | 84.6% [82.8%, 86.4%] | 15.0% | 0.234 [0.211, 0.258] | 0.745 | 0.139 | 0.045 | 0.260 | 0.200 | 0/0 | 0 | 0 | 232 | 1.4B |  |
| gliner2-hivetrace-uni | **6832** | 85.8% [84.5%, 87.0%] | 14.0% | 0.223 [0.206, 0.242] | 0.873 | 0.128 | 0.205 | 0.246 | 0.157 | 0/0 | 0 | 0 | 38 | 147M |  |
| openai-base | **6838** | 85.8% [83.6%, 88.2%] | 14.0% | 0.215 [0.184, 0.243] | 0.822 | 0.124 | 0.020 | 0.247 | 0.192 | 0/0 | 0 | 0 | 284 | 1.4B |  |
| pplx | **6964** | 87.4% [85.1%, 89.8%] | 12.6% | 0.188 [0.155, 0.217] | 0.879 | 0.105 | 0.044 | 0.222 | 0.184 | 0/0 | 0 | 0 | 254 | 596M |  |
| gravitee-small | **7642** | 95.9% [95.0%, 96.8%] | 3.7% | 0.073 [0.057, 0.089] | 0.367 | 0.040 | 0.016 | 0.075 | 0.055 | 0/0 | 0 | 0 | 25 | 29M |  |
| rules-ru | **7922** | 99.4% [99.2%, 99.7%] | 0.6% | 0.014 [0.008, 0.022] | 0.586 | 0.007 | 0.002 | 0.011 | 0.011 | 0/0 | 0 | 0 | 2 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: stanza-ru ≈ fef2-secret-ru; davlan-xlmr ≈ natasha; natasha ≈ davlan-mbert; davlan-mbert ≈ spacy-ru-lg; nym-base ≈ gliner2-fastino-ru; gliner2-fastino-ru ≈ nym-base+sent300; nym-base+sent300 ≈ nym-small; nym-small ≈ gliner-pii-edge; gliner-pii-edge ≈ gliner2-fastino; gliner2-fastino ≈ gliner-nvidia+sent300; ner-ru-yqelz ≈ gliner25-fastino-ru; gliner25-fastino-ru ≈ gliner-multi-v21; gliner-multi-v21 ≈ gliner-nvidia+ov100; gliner-nvidia+ov100 ≈ gliner-nvidia; gliner-nvidia ≈ gliner-multi-v21-ru; gliner-multi-v21-ru ≈ gliner2-large; gliner2-large ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ ner-ru-gherman; ner-ru-gherman ≈ gliner2-hivetrace-omni-ru; ru-legal-ner+sent300 ≈ gliner25-fastino+sent300; gliner25-fastino ≈ gliner25-fastino+ov100; gliner25-fastino+ov100 ≈ ru-legal-ner; ru-legal-ner ≈ ru-legal-ner+ov100; ru-legal-ner+ov100 ≈ nuner-zero; nuner-zero ≈ gliner-nvidia-ru; gliner-nvidia-ru ≈ spacy-alrosait; spacy-alrosait ≈ gliner25-fastino-ru+nochunk; mmbert32k ≈ gliner25-fastino+nochunk; gliner25-fastino+nochunk ≈ kalyan-ettin; kalyan-ettin ≈ openmed-nemotron; openmed-nemotron ≈ gliner-stream-pii; gliner-stream-pii ≈ pii-shield-onnx; pii-shield-onnx ≈ gliner-pii-base; gliner-pii-base ≈ gliner-urchade; gliner-urchade ≈ gliner2-hivetrace-uni-ru; gliner2-hivetrace-uni-ru ≈ opf-ru; opf-ru ≈ gliner-urchade-ru; gliner-urchade-ru ≈ openmed-multilingual; openmed-multilingual ≈ gliner2-vladlinv; gliner2-vladlinv ≈ traciora; traciora ≈ gliner2-vladlinv-ru; gliner2-vladlinv-ru ≈ ru-pii-ner; pplx+sent300 ≈ mmbert32k+nochunk; mmbert32k+nochunk ≈ opf-ru-v2+sent300; opf-ru-v2+sent300 ≈ apararti; pplx+ov100 ≈ opf-kz-ru; opf-kz-ru ≈ gliner2-hivetrace-uni; gliner2-hivetrace-uni ≈ openai-base; openai-base ≈ pplx

## Missed by group

| model | PERSON | ADDRESS | ORG |
|---|---|---|---|
| spans in gold | 3369 | 2396 | 2201 |
| stanza-ru | 30 (0.9%) | 25 (1.0%) | 206 (9.4%) |
| fef2-secret-ru | 62 (1.8%) | 36 (1.5%) | 174 (7.9%) |
| davlan-xlmr | 57 (1.7%) | 57 (2.4%) | 203 (9.2%) |
| natasha | 106 (3.1%) | 50 (2.1%) | 194 (8.8%) |
| davlan-mbert | 44 (1.3%) | 85 (3.5%) | 235 (10.7%) |
| spacy-ru-lg | 100 (3.0%) | 61 (2.5%) | 206 (9.4%) |
| bardsai-eu | 61 (1.8%) | 188 (7.8%) | 217 (9.9%) |
| nym-base+ov100 | 163 (4.8%) | 293 (12.2%) | 383 (17.4%) |
| nym-base | 187 (5.6%) | 303 (12.6%) | 413 (18.8%) |
| gliner2-fastino-ru | 686 (20.4%) | 134 (5.6%) | 150 (6.8%) |
| nym-base+sent300 | 213 (6.3%) | 372 (15.5%) | 483 (21.9%) |
| nym-small | 208 (6.2%) | 358 (14.9%) | 524 (23.8%) |
| gliner-pii-edge | 637 (18.9%) | 240 (10.0%) | 350 (15.9%) |
| gliner2-fastino | 1154 (34.3%) | 54 (2.3%) | 154 (7.0%) |
| gliner-nvidia+sent300 | 340 (10.1%) | 437 (18.2%) | 658 (29.9%) |
| ner-ru-yqelz | 612 (18.2%) | 349 (14.6%) | 637 (28.9%) |
| gliner25-fastino-ru | 725 (21.5%) | 622 (26.0%) | 388 (17.6%) |
| gliner-multi-v21 | 913 (27.1%) | 525 (21.9%) | 453 (20.6%) |
| gliner-nvidia+ov100 | 387 (11.5%) | 698 (29.1%) | 913 (41.5%) |
| gliner-nvidia | 409 (12.1%) | 705 (29.4%) | 891 (40.5%) |
| gliner-multi-v21-ru | 847 (25.1%) | 783 (32.7%) | 485 (22.0%) |
| gliner2-large | 1119 (33.2%) | 573 (23.9%) | 574 (26.1%) |
| gliner2-hivetrace-omni | 963 (28.6%) | 832 (34.7%) | 534 (24.3%) |
| ner-ru-gherman | 148 (4.4%) | 309 (12.9%) | 1994 (90.6%) |
| gliner2-hivetrace-omni-ru | 1083 (32.1%) | 868 (36.2%) | 537 (24.4%) |
| ru-legal-ner+sent300 | 251 (7.5%) | 1800 (75.1%) | 1107 (50.3%) |
| gliner25-fastino+sent300 | 2753 (81.7%) | 156 (6.5%) | 293 (13.3%) |
| gliner25-fastino | 2936 (87.1%) | 182 (7.6%) | 332 (15.1%) |
| gliner25-fastino+ov100 | 2942 (87.3%) | 191 (8.0%) | 332 (15.1%) |
| ru-legal-ner | 345 (10.2%) | 1904 (79.5%) | 1242 (56.4%) |
| ru-legal-ner+ov100 | 356 (10.6%) | 1884 (78.6%) | 1266 (57.5%) |
| nuner-zero | 3142 (93.3%) | 237 (9.9%) | 221 (10.0%) |
| gliner-nvidia-ru | 970 (28.8%) | 1560 (65.1%) | 1195 (54.3%) |
| spacy-alrosait | 893 (26.5%) | 875 (36.5%) | 2013 (91.5%) |
| gliner25-fastino-ru+nochunk | 2181 (64.7%) | 1033 (43.1%) | 649 (29.5%) |
| mmbert32k | 765 (22.7%) | 1976 (82.5%) | 1578 (71.7%) |
| gliner25-fastino+nochunk | 3152 (93.6%) | 663 (27.7%) | 609 (27.7%) |
| kalyan-ettin | 1487 (44.1%) | 1208 (50.4%) | 1757 (79.8%) |
| openmed-nemotron | 1486 (44.1%) | 1356 (56.6%) | 1635 (74.3%) |
| gliner-stream-pii | 2629 (78.0%) | 880 (36.7%) | 1037 (47.1%) |
| pii-shield-onnx | 1379 (40.9%) | 1300 (54.3%) | 1940 (88.1%) |
| gliner-pii-base | 3049 (90.5%) | 902 (37.6%) | 670 (30.4%) |
| gliner-urchade | 3247 (96.4%) | 1017 (42.4%) | 469 (21.3%) |
| gliner2-hivetrace-uni-ru | 1503 (44.6%) | 2149 (89.7%) | 1246 (56.6%) |
| opf-ru | 997 (29.6%) | 1995 (83.3%) | 1928 (87.6%) |
| gliner-urchade-ru | 3272 (97.1%) | 1186 (49.5%) | 516 (23.4%) |
| openmed-multilingual | 1696 (50.3%) | 1676 (69.9%) | 1861 (84.6%) |
| gliner2-vladlinv | 802 (23.8%) | 2316 (96.7%) | 2176 (98.9%) |
| traciora | 1439 (42.7%) | 2065 (86.2%) | 1909 (86.7%) |
| gliner2-vladlinv-ru | 943 (28.0%) | 2327 (97.1%) | 2182 (99.1%) |
| ru-pii-ner | 1043 (31.0%) | 2363 (98.6%) | 2183 (99.2%) |
| pplx+sent300 | 1320 (39.2%) | 2304 (96.2%) | 2152 (97.8%) |
| mmbert32k+nochunk | 1801 (53.5%) | 2170 (90.6%) | 1834 (83.3%) |
| opf-ru-v2+sent300 | 1521 (45.1%) | 2251 (93.9%) | 2038 (92.6%) |
| apararti | 1661 (49.3%) | 2190 (91.4%) | 2001 (90.9%) |
| opf-ru-v2+ov100 | 1648 (48.9%) | 2275 (94.9%) | 2069 (94.0%) |
| opf-ru-v2 | 1699 (50.4%) | 2290 (95.6%) | 2071 (94.1%) |
| pplx+ov100 | 2054 (61.0%) | 2369 (98.9%) | 2192 (99.6%) |
| opf-kz-ru | 2272 (67.4%) | 2333 (97.4%) | 2138 (97.1%) |
| gliner2-hivetrace-uni | 2900 (86.1%) | 2235 (93.3%) | 1697 (77.1%) |
| openai-base | 2334 (69.3%) | 2356 (98.3%) | 2148 (97.6%) |
| pplx | 2380 (70.6%) | 2386 (99.6%) | 2198 (99.9%) |
| gravitee-small | 3191 (94.7%) | 2329 (97.2%) | 2122 (96.4%) |
| rules-ru | 3369 (100.0%) | 2394 (99.9%) | 2159 (98.1%) |

## Char recall by gold type

| type | group | stanza-ru | fef2-secret-ru | davlan-xlmr | natasha | davlan-mbert | spacy-ru-lg | bardsai-eu | nym-base+ov100 | nym-base | gliner2-fastino-ru | nym-base+sent300 | nym-small | gliner-pii-edge | gliner2-fastino | gliner-nvidia+sent300 | ner-ru-yqelz | gliner25-fastino-ru | gliner-multi-v21 | gliner-nvidia+ov100 | gliner-nvidia | gliner-multi-v21-ru | gliner2-large | gliner2-hivetrace-omni | ner-ru-gherman | gliner2-hivetrace-omni-ru | ru-legal-ner+sent300 | gliner25-fastino+sent300 | gliner25-fastino | gliner25-fastino+ov100 | ru-legal-ner | ru-legal-ner+ov100 | nuner-zero | gliner-nvidia-ru | spacy-alrosait | gliner25-fastino-ru+nochunk | mmbert32k | gliner25-fastino+nochunk | kalyan-ettin | openmed-nemotron | gliner-stream-pii | pii-shield-onnx | gliner-pii-base | gliner-urchade | gliner2-hivetrace-uni-ru | opf-ru | gliner-urchade-ru | openmed-multilingual | gliner2-vladlinv | traciora | gliner2-vladlinv-ru | ru-pii-ner | pplx+sent300 | mmbert32k+nochunk | opf-ru-v2+sent300 | apararti | opf-ru-v2+ov100 | opf-ru-v2 | pplx+ov100 | opf-kz-ru | gliner2-hivetrace-uni | openai-base | pplx | gravitee-small | rules-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| loc_name | ADDRESS | 0.973 | 0.974 | 0.963 | 0.966 | 0.953 | 0.960 | 0.928 | 0.875 | 0.871 | 0.937 | 0.843 | 0.847 | 0.847 | 0.966 | 0.817 | 0.886 | 0.747 | 0.793 | 0.706 | 0.705 | 0.697 | 0.742 | 0.650 | 0.815 | 0.635 | 0.281 | 0.926 | 0.911 | 0.911 | 0.228 | 0.239 | 0.886 | 0.361 | 0.606 | 0.579 | 0.188 | 0.713 | 0.479 | 0.411 | 0.619 | 0.484 | 0.598 | 0.602 | 0.103 | 0.173 | 0.532 | 0.312 | 0.034 | 0.151 | 0.028 | 0.021 | 0.044 | 0.098 | 0.075 | 0.098 | 0.063 | 0.055 | 0.013 | 0.034 | 0.068 | 0.018 | 0.005 | 0.029 | 0.001 |
| name | PERSON | 0.998 | 0.981 | 0.984 | 0.978 | 0.986 | 0.975 | 0.986 | 0.978 | 0.977 | 0.769 | 0.978 | 0.974 | 0.763 | 0.709 | 0.940 | 0.925 | 0.844 | 0.792 | 0.920 | 0.917 | 0.815 | 0.652 | 0.667 | 0.958 | 0.617 | 0.972 | 0.172 | 0.131 | 0.121 | 0.953 | 0.953 | 0.051 | 0.710 | 0.826 | 0.422 | 0.821 | 0.066 | 0.694 | 0.577 | 0.156 | 0.711 | 0.064 | 0.021 | 0.576 | 0.738 | 0.019 | 0.578 | 0.807 | 0.649 | 0.756 | 0.728 | 0.644 | 0.578 | 0.649 | 0.572 | 0.611 | 0.597 | 0.420 | 0.396 | 0.099 | 0.368 | 0.322 | 0.048 | 0.000 |
| nickname | PERSON | 0.928 | 0.698 | 0.869 | 0.727 | 0.825 | 0.770 | 0.834 | 0.698 | 0.622 | 0.854 | 0.591 | 0.653 | 0.735 | 0.649 | 0.661 | 0.782 | 0.524 | 0.520 | 0.532 | 0.622 | 0.429 | 0.396 | 0.452 | 0.511 | 0.298 | 0.665 | 0.433 | 0.361 | 0.368 | 0.608 | 0.694 | 0.224 | 0.378 | 0.429 | 0.220 | 0.524 | 0.144 | 0.255 | 0.318 | 0.246 | 0.292 | 0.226 | 0.238 | 0.257 | 0.544 | 0.218 | 0.320 | 0.318 | 0.409 | 0.265 | 0.205 | 0.310 | 0.160 | 0.302 | 0.251 | 0.181 | 0.230 | 0.240 | 0.168 | 0.158 | 0.136 | 0.175 | 0.045 | 0.000 |
| org_name | ORG | 0.807 | 0.843 | 0.824 | 0.820 | 0.794 | 0.830 | 0.852 | 0.777 | 0.762 | 0.901 | 0.728 | 0.709 | 0.639 | 0.894 | 0.694 | 0.739 | 0.808 | 0.752 | 0.590 | 0.601 | 0.741 | 0.702 | 0.712 | 0.068 | 0.725 | 0.437 | 0.854 | 0.824 | 0.829 | 0.385 | 0.363 | 0.834 | 0.457 | 0.078 | 0.709 | 0.193 | 0.716 | 0.157 | 0.235 | 0.432 | 0.095 | 0.588 | 0.773 | 0.362 | 0.092 | 0.760 | 0.112 | 0.008 | 0.127 | 0.006 | 0.007 | 0.017 | 0.110 | 0.061 | 0.075 | 0.048 | 0.050 | 0.003 | 0.025 | 0.160 | 0.017 | 0.002 | 0.039 | 0.019 |
| patronymic | PERSON | 1.000 | 0.971 | 0.971 | 0.988 | 1.000 | 0.988 | 0.988 | 0.997 | 0.997 | 0.772 | 0.997 | 0.997 | 0.807 | 0.452 | 0.718 | 0.916 | 0.859 | 0.588 | 0.599 | 0.501 | 0.527 | 0.608 | 0.248 | 0.945 | 0.323 | 1.000 | 0.360 | 0.138 | 0.161 | 1.000 | 0.988 | 0.026 | 0.435 | 0.957 | 0.170 | 0.654 | 0.006 | 0.481 | 0.821 | 0.092 | 0.683 | 0.061 | 0.063 | 0.499 | 0.865 | 0.063 | 0.631 | 0.680 | 0.879 | 0.651 | 0.882 | 0.608 | 0.173 | 0.839 | 0.911 | 0.859 | 0.790 | 0.470 | 0.758 | 0.176 | 0.594 | 0.357 | 0.066 | 0.000 |
| surname | PERSON | 0.990 | 0.992 | 0.989 | 0.972 | 0.992 | 0.971 | 0.985 | 0.951 | 0.944 | 0.810 | 0.926 | 0.932 | 0.839 | 0.633 | 0.877 | 0.746 | 0.761 | 0.693 | 0.868 | 0.861 | 0.720 | 0.679 | 0.729 | 0.980 | 0.710 | 0.915 | 0.177 | 0.112 | 0.112 | 0.886 | 0.881 | 0.067 | 0.733 | 0.701 | 0.308 | 0.758 | 0.058 | 0.485 | 0.563 | 0.253 | 0.559 | 0.115 | 0.041 | 0.522 | 0.693 | 0.028 | 0.445 | 0.755 | 0.549 | 0.726 | 0.697 | 0.601 | 0.414 | 0.502 | 0.485 | 0.464 | 0.450 | 0.368 | 0.295 | 0.158 | 0.278 | 0.268 | 0.053 | 0.000 |

## char F1 by domain

| domain | n | stanza-ru | fef2-secret-ru | davlan-xlmr | natasha | davlan-mbert | spacy-ru-lg | bardsai-eu | nym-base+ov100 | nym-base | gliner2-fastino-ru | nym-base+sent300 | nym-small | gliner-pii-edge | gliner2-fastino | gliner-nvidia+sent300 | ner-ru-yqelz | gliner25-fastino-ru | gliner-multi-v21 | gliner-nvidia+ov100 | gliner-nvidia | gliner-multi-v21-ru | gliner2-large | gliner2-hivetrace-omni | ner-ru-gherman | gliner2-hivetrace-omni-ru | ru-legal-ner+sent300 | gliner25-fastino+sent300 | gliner25-fastino | gliner25-fastino+ov100 | ru-legal-ner | ru-legal-ner+ov100 | nuner-zero | gliner-nvidia-ru | spacy-alrosait | gliner25-fastino-ru+nochunk | mmbert32k | gliner25-fastino+nochunk | kalyan-ettin | openmed-nemotron | gliner-stream-pii | pii-shield-onnx | gliner-pii-base | gliner-urchade | gliner2-hivetrace-uni-ru | opf-ru | gliner-urchade-ru | openmed-multilingual | gliner2-vladlinv | traciora | gliner2-vladlinv-ru | ru-pii-ner | pplx+sent300 | mmbert32k+nochunk | opf-ru-v2+sent300 | apararti | opf-ru-v2+ov100 | opf-ru-v2 | pplx+ov100 | opf-kz-ru | gliner2-hivetrace-uni | openai-base | pplx | gravitee-small | rules-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| devset | 122 | 0.883 | 0.934 | 0.931 | 0.930 | 0.930 | 0.922 | 0.840 | 0.782 | 0.786 | 0.771 | 0.783 | 0.782 | 0.738 | 0.764 | 0.822 | 0.793 | 0.796 | 0.774 | 0.825 | 0.820 | 0.757 | 0.721 | 0.760 | 0.759 | 0.765 | 0.571 | 0.663 | 0.660 | 0.678 | 0.556 | 0.554 | 0.677 | 0.670 | 0.609 | 0.718 | 0.533 | 0.641 | 0.539 | 0.451 | 0.574 | 0.534 | 0.519 | 0.527 | 0.491 | 0.484 | 0.504 | 0.442 | 0.433 | 0.434 | 0.411 | 0.431 | 0.393 | 0.377 | 0.378 | 0.349 | 0.360 | 0.349 | 0.290 | 0.238 | 0.196 | 0.225 | 0.232 | 0.085 | 0.007 |
| testset | 132 | 0.873 | 0.925 | 0.924 | 0.921 | 0.920 | 0.916 | 0.823 | 0.791 | 0.795 | 0.761 | 0.791 | 0.795 | 0.731 | 0.754 | 0.805 | 0.761 | 0.800 | 0.752 | 0.806 | 0.794 | 0.753 | 0.694 | 0.730 | 0.715 | 0.731 | 0.583 | 0.640 | 0.663 | 0.660 | 0.577 | 0.569 | 0.660 | 0.664 | 0.611 | 0.634 | 0.547 | 0.592 | 0.518 | 0.449 | 0.528 | 0.497 | 0.557 | 0.541 | 0.512 | 0.464 | 0.516 | 0.417 | 0.444 | 0.411 | 0.427 | 0.383 | 0.356 | 0.348 | 0.370 | 0.358 | 0.340 | 0.335 | 0.220 | 0.231 | 0.239 | 0.209 | 0.161 | 0.066 | 0.018 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| fef2-secret-ru | 272 (3.4%) | 269 (3.4%) | 269 (3.4%) | 269 (3.4%) |
| davlan-xlmr | 317 (4.0%) | 309 (3.9%) | 309 (3.9%) | 309 (3.9%) |
| davlan-mbert | 364 (4.6%) | 357 (4.5%) | 357 (4.5%) | 357 (4.5%) |
| bardsai-eu | 466 (5.8%) | 429 (5.4%) | 428 (5.4%) | 428 (5.4%) |
| nym-base+ov100 | 839 (10.5%) | 722 (9.1%) | 721 (9.1%) | 721 (9.1%) |
| nym-base | 903 (11.3%) | 792 (9.9%) | 792 (9.9%) | 792 (9.9%) |
| gliner2-fastino-ru | 970 (12.2%) | 349 (4.4%) | 199 (2.5%) | 77 (1.0%) |
| nym-base+sent300 | 1068 (13.4%) | 948 (11.9%) | 948 (11.9%) | 948 (11.9%) |
| nym-small | 1090 (13.7%) | 960 (12.1%) | 959 (12.0%) | 959 (12.0%) |
| gliner-pii-edge | 1227 (15.4%) | 66 (0.8%) | 13 (0.2%) | 2 (0.0%) |
| gliner2-fastino | 1362 (17.1%) | 587 (7.4%) | 292 (3.7%) | 109 (1.4%) |
| gliner-nvidia+sent300 | 1435 (18.0%) | 924 (11.6%) | 672 (8.4%) | 390 (4.9%) |
| ner-ru-yqelz | 1598 (20.1%) | 1496 (18.8%) | 1494 (18.8%) | 1494 (18.8%) |
| gliner25-fastino-ru | 1735 (21.8%) | 1226 (15.4%) | 1012 (12.7%) | 756 (9.5%) |
| gliner-multi-v21 | 1891 (23.7%) | 928 (11.6%) | 621 (7.8%) | 332 (4.2%) |
| gliner-nvidia+ov100 | 1998 (25.1%) | 1414 (17.8%) | 1100 (13.8%) | 731 (9.2%) |
| gliner-nvidia | 2005 (25.2%) | 1412 (17.7%) | 1099 (13.8%) | 703 (8.8%) |
| gliner-multi-v21-ru | 2115 (26.6%) | 1080 (13.6%) | 752 (9.4%) | 416 (5.2%) |
| gliner2-large | 2266 (28.4%) | 1135 (14.2%) | 764 (9.6%) | 441 (5.5%) |
| gliner2-hivetrace-omni | 2329 (29.2%) | 1574 (19.8%) | 1185 (14.9%) | 756 (9.5%) |
| ner-ru-gherman | 2451 (30.8%) | 2403 (30.2%) | 2396 (30.1%) | 2394 (30.1%) |
| gliner2-hivetrace-omni-ru | 2488 (31.2%) | 1543 (19.4%) | 1101 (13.8%) | 659 (8.3%) |
| ru-legal-ner+sent300 | 3158 (39.6%) | 2749 (34.5%) | 2658 (33.4%) | 2646 (33.2%) |
| gliner25-fastino+sent300 | 3202 (40.2%) | 2751 (34.5%) | 2566 (32.2%) | 2231 (28.0%) |
| gliner25-fastino | 3450 (43.3%) | 3033 (38.1%) | 2819 (35.4%) | 2465 (30.9%) |
| gliner25-fastino+ov100 | 3465 (43.5%) | 2985 (37.5%) | 2749 (34.5%) | 2441 (30.6%) |
| ru-legal-ner | 3491 (43.8%) | 3125 (39.2%) | 3050 (38.3%) | 3041 (38.2%) |
| ru-legal-ner+ov100 | 3506 (44.0%) | 3116 (39.1%) | 3056 (38.4%) | 3047 (38.3%) |
| nuner-zero | 3600 (45.2%) | 3027 (38.0%) | 2695 (33.8%) | 2226 (27.9%) |
| gliner-nvidia-ru | 3725 (46.8%) | 2863 (35.9%) | 2450 (30.8%) | 1871 (23.5%) |
| gliner25-fastino-ru+nochunk | 3863 (48.5%) | 3443 (43.2%) | 3309 (41.5%) | 3186 (40.0%) |
| mmbert32k | 4319 (54.2%) | 3186 (40.0%) | 3021 (37.9%) | 3007 (37.7%) |
| gliner25-fastino+nochunk | 4424 (55.5%) | 4188 (52.6%) | 4078 (51.2%) | 3955 (49.6%) |
| kalyan-ettin | 4452 (55.9%) | 3738 (46.9%) | 3662 (46.0%) | 3657 (45.9%) |
| openmed-nemotron | 4477 (56.2%) | 3905 (49.0%) | 3862 (48.5%) | 3862 (48.5%) |
| gliner-stream-pii | 4546 (57.1%) | 3407 (42.8%) | 2675 (33.6%) | 1800 (22.6%) |
| pii-shield-onnx | 4619 (58.0%) | 4302 (54.0%) | 4281 (53.7%) | 4280 (53.7%) |
| gliner-pii-base | 4621 (58.0%) | 888 (11.1%) | 234 (2.9%) | 51 (0.6%) |
| gliner-urchade | 4733 (59.4%) | 4210 (52.8%) | 3889 (48.8%) | 3518 (44.2%) |
| gliner2-hivetrace-uni-ru | 4898 (61.5%) | 3680 (46.2%) | 2897 (36.4%) | 2047 (25.7%) |
| opf-ru | 4920 (61.8%) | 4886 (61.3%) | 4885 (61.3%) | 4885 (61.3%) |
| gliner-urchade-ru | 4974 (62.4%) | 4375 (54.9%) | 4018 (50.4%) | 3401 (42.7%) |
| openmed-multilingual | 5233 (65.7%) | 4787 (60.1%) | 4769 (59.9%) | 4766 (59.8%) |
| gliner2-vladlinv | 5294 (66.5%) | 5228 (65.6%) | 5187 (65.1%) | 5123 (64.3%) |
| traciora | 5413 (68.0%) | 5408 (67.9%) | 5408 (67.9%) | 5408 (67.9%) |
| gliner2-vladlinv-ru | 5452 (68.4%) | 5377 (67.5%) | 5353 (67.2%) | 5282 (66.3%) |
| mmbert32k+nochunk | 5805 (72.9%) | 4513 (56.7%) | 4249 (53.3%) | 4218 (53.0%) |
| opf-ru-v2+sent300 | 5810 (72.9%) | 5807 (72.9%) | 5807 (72.9%) | 5807 (72.9%) |
| apararti | 5852 (73.5%) | 5805 (72.9%) | 5805 (72.9%) | 5805 (72.9%) |
| opf-ru-v2+ov100 | 5992 (75.2%) | 5990 (75.2%) | 5990 (75.2%) | 5990 (75.2%) |
| opf-ru-v2 | 6060 (76.1%) | 6060 (76.1%) | 6060 (76.1%) | 6060 (76.1%) |
| opf-kz-ru | 6743 (84.6%) | 6735 (84.5%) | 6735 (84.5%) | 6735 (84.5%) |
| gliner2-hivetrace-uni | 6832 (85.8%) | 5412 (67.9%) | 4259 (53.5%) | 2623 (32.9%) |
| openai-base | 6838 (85.8%) | 6837 (85.8%) | 6837 (85.8%) | 6837 (85.8%) |
| gravitee-small | 7642 (95.9%) | 7618 (95.6%) | 7618 (95.6%) | 7618 (95.6%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
