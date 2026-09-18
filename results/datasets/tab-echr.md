# tab-echr - en / pii (127 rows, 3830 spans, 0 negatives)

Main metric: **missed** - gold spans no predicted character touched. Score threshold 0.5; spans without a score always count. `hidden` - gold spans every character of which is covered: touching one character counts as detection, not as hiding. `hidden` is counted over normalized predictions - a prediction is stretched to whole words before it is compared, so it is what a masker that repeats the same normalization would hide; a masker that masks the raw offsets of the model hides no more than this. Char P / R / F1 are reference only. Trivial baseline, mask everything: 0 missed, 100% hidden, char P 0.095 (90.5% of the text over-masked). `rows touched` / `chars masked` count rows the source left without annotations where a mask touched something, and the characters masked in them; that absence of annotations is not evidence that those rows hold nothing sensitive, so this is not a false-alarm rate. The exact CSVs keep the technical column names `fp_rows` and `fp_chars`.

| model | missed | missed % [95% CI] | hidden | char F1 [95% CI] | P | R | entity exact | entity overlap | typed F1 | rows touched | chars masked | dropped spans | ms/row | params | train |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gliner2-fastino | **60** | 1.6% [0.8%, 2.7%] | 81.3% | 0.635 [0.618, 0.653] | 0.479 | 0.942 | 0.427 | 0.550 | 0.489 | 0/0 | 0 | 0 | 45 | 307M |  |
| gliner25-fastino+sent300 | **118** | 3.1% [2.2%, 4.3%] | 85.1% | 0.671 [0.654, 0.690] | 0.529 | 0.918 | 0.478 | 0.594 | 0.532 | 0/0 | 0 | 0 | 49 | 287M |  |
| nuner-zero | **148** | 3.9% [2.4%, 6.0%] | 84.6% | 0.729 [0.711, 0.747] | 0.597 | 0.937 | 0.536 | 0.659 | 0.562 | 0/0 | 0 | 0 | 60 | 449M |  |
| gliner25-fastino | **153** | 4.0% [3.0%, 5.3%] | 86.8% | 0.695 [0.678, 0.715] | 0.557 | 0.925 | 0.519 | 0.623 | 0.562 | 0/0 | 0 | 0 | 20 | 287M |  |
| gliner25-fastino+ov100 | **158** | 4.1% [3.0%, 5.4%] | 87.7% | 0.701 [0.684, 0.720] | 0.564 | 0.927 | 0.526 | 0.630 | 0.569 | 0/0 | 0 | 0 | 23 | 287M |  |
| gliner2-large | **241** | 6.3% [3.7%, 9.5%] | 83.4% | 0.650 [0.633, 0.669] | 0.504 | 0.915 | 0.459 | 0.560 | 0.513 | 0/0 | 0 | 0 | 74 | 486M |  |
| gliner-multi-v21 | **375** | 9.8% [7.7%, 12.7%] | 83.6% | 0.690 [0.673, 0.707] | 0.559 | 0.902 | 0.547 | 0.625 | 0.569 | 0/0 | 0 | 0 | 28 | 289M |  |
| gliner2-hivetrace-omni | **408** | 10.7% [8.8%, 12.6%] | 71.4% | 0.717 [0.702, 0.732] | 0.626 | 0.838 | 0.522 | 0.700 | 0.553 | 0/0 | 0 | 0 | 98 | 307M |  |
| davlan-mbert+cpu-int8 | **492** | 12.8% [9.3%, 16.9%] | 54.5% | 0.829 [0.813, 0.844] | 0.831 | 0.826 | 0.490 | 0.817 | 0.649 | 0/0 | 0 | 0 | 239 | 177M |  |
| davlan-mbert | **494** | 12.9% [9.4%, 17.0%] | 53.8% | 0.823 [0.807, 0.838] | 0.819 | 0.826 | 0.474 | 0.801 | 0.630 | 0/0 | 0 | 0 | 36 | 177M |  |
| davlan-xlmr | **514** | 13.4% [10.0%, 17.6%] | 54.6% | 0.834 [0.817, 0.849] | 0.841 | 0.826 | 0.502 | 0.827 | 0.646 | 0/0 | 0 | 0 | 35 | 277M |  |
| bardsai-eu | **515** | 13.4% [10.2%, 17.3%] | 65.5% | 0.819 [0.802, 0.837] | 0.782 | 0.860 | 0.563 | 0.804 | 0.065 | 0/0 | 0 | 0 | 6643 | - |  |
| gliner-pii-edge | **530** | 13.8% [10.4%, 17.7%] | 77.9% | 0.778 [0.762, 0.795] | 0.715 | 0.855 | 0.631 | 0.725 | 0.630 | 0/0 | 0 | 0 | 159 | 45M |  |
| stanza-ru | **613** | 16.0% [12.6%, 20.0%] | 77.3% | 0.370 [0.356, 0.383] | 0.233 | 0.891 | 0.174 | 0.590 | 0.030 | 0/0 | 0 | 0 | 422 | - |  |
| gliner-nvidia+sent300 | **637** | 16.6% [13.6%, 20.2%] | 65.6% | 0.786 [0.769, 0.804] | 0.764 | 0.810 | 0.592 | 0.783 | 0.595 | 0/0 | 0 | 0 | 212 | 445M |  |
| gliner-pii-base | **640** | 16.7% [14.0%, 19.9%] | 77.7% | 0.744 [0.729, 0.759] | 0.670 | 0.837 | 0.615 | 0.675 | 0.637 | 0/0 | 0 | 0 | 28 | 166M |  |
| gliner-stream-pii | **742** | 19.4% [16.8%, 22.3%] | 68.1% | 0.721 [0.705, 0.740] | 0.675 | 0.774 | 0.550 | 0.673 | 0.583 | 0/0 | 0 | 0 | 51 | 677M |  |
| gliner-urchade | **778** | 20.3% [17.0%, 24.4%] | 76.9% | 0.679 [0.661, 0.696] | 0.571 | 0.836 | 0.537 | 0.597 | 0.591 | 0/0 | 0 | 0 | 42 | 289M |  |
| davlan-xlmr+cpu-int8 | **818** | 21.4% [18.0%, 25.4%] | 36.2% | 0.757 [0.739, 0.775] | 0.865 | 0.673 | 0.347 | 0.808 | 0.555 | 0/0 | 0 | 0 | 259 | 277M |  |
| nym-small | **876** | 22.9% [19.6%, 26.0%] | 44.3% | 0.534 [0.514, 0.554] | 0.448 | 0.663 | 0.246 | 0.562 | 0.223 | 0/0 | 0 | 0 | 7488 | - |  |
| nym-base+ov100 | **882** | 23.0% [19.9%, 26.2%] | 46.2% | 0.560 [0.535, 0.584] | 0.488 | 0.657 | 0.287 | 0.575 | 0.199 | 0/0 | 0 | 0 | 37 | 308M |  |
| gliner-nvidia | **917** | 23.9% [20.4%, 27.8%] | 58.2% | 0.763 [0.743, 0.782] | 0.805 | 0.725 | 0.582 | 0.789 | 0.593 | 0/0 | 0 | 0 | 75 | 445M |  |
| nym-base | **917** | 23.9% [20.6%, 27.1%] | 43.7% | 0.551 [0.527, 0.575] | 0.482 | 0.644 | 0.271 | 0.570 | 0.196 | 0/0 | 0 | 0 | 35 | 308M |  |
| gliner-nvidia+ov100 | **943** | 24.6% [21.3%, 28.2%] | 56.9% | 0.757 [0.738, 0.778] | 0.818 | 0.705 | 0.576 | 0.791 | 0.598 | 0/0 | 0 | 0 | 93 | 445M |  |
| ner-ru-yqelz | **948** | 24.8% [21.5%, 28.5%] | 55.5% | 0.628 [0.612, 0.645] | 0.544 | 0.742 | 0.420 | 0.668 | 0.465 | 0/0 | 0 | 0 | 40 | 559M |  |
| nym-base+cpu-int8 | **964** | 25.2% [22.0%, 28.2%] | 41.5% | 0.533 [0.510, 0.556] | 0.470 | 0.616 | 0.247 | 0.563 | 0.182 | 0/0 | 0 | 0 | 406 | 308M |  |
| nym-base+sent300 | **1004** | 26.2% [23.1%, 29.6%] | 39.3% | 0.530 [0.506, 0.552] | 0.465 | 0.616 | 0.239 | 0.560 | 0.199 | 0/0 | 0 | 0 | 50 | 308M |  |
| openmed-multilingual | **1369** | 35.7% [32.6%, 39.0%] | 24.2% | 0.433 [0.407, 0.455] | 0.433 | 0.432 | 0.166 | 0.510 | 0.256 | 0/0 | 0 | 0 | 237 | 1.4B |  |
| gliner25-fastino+nochunk | **1415** | 36.9% [31.9%, 41.8%] | 56.2% | 0.737 [0.708, 0.764] | 0.851 | 0.649 | 0.602 | 0.736 | 0.609 | 0/0 | 0 | 0 | 134 | 287M |  |
| pplx+cpu-int8 | **1635** | 42.7% [39.0%, 46.8%] | 47.9% | 0.420 [0.385, 0.452] | 0.415 | 0.424 | 0.347 | 0.503 | 0.307 | 0/0 | 0 | 0 | 1337 | 596M |  |
| gravitee-small | **1667** | 43.5% [40.1%, 47.4%] | 40.9% | 0.494 [0.470, 0.516] | 0.481 | 0.508 | 0.339 | 0.499 | 0.444 | 0/0 | 0 | 0 | 29 | 29M |  |
| ner-ru-gherman | **1683** | 43.9% [40.0%, 47.9%] | 15.2% | 0.496 [0.469, 0.522] | 0.965 | 0.334 | 0.179 | 0.708 | 0.060 | 0/0 | 0 | 0 | 37 | 177M |  |
| ner-ru-gherman-onnx | **1687** | 44.0% [40.1%, 48.1%] | 14.4% | 0.492 [0.465, 0.519] | 0.965 | 0.330 | 0.169 | 0.707 | 0.060 | 0/0 | 0 | 0 | 1492 | - |  |
| gravitee-small+cpu-int8 | **1697** | 44.3% [40.8%, 48.1%] | 40.2% | 0.495 [0.471, 0.517] | 0.486 | 0.504 | 0.335 | 0.496 | 0.446 | 0/0 | 0 | 0 | 54 | 29M |  |
| ner-ru-gherman+cpu-int8 | **1702** | 44.4% [40.7%, 48.2%] | 13.8% | 0.473 [0.447, 0.498] | 0.969 | 0.313 | 0.163 | 0.705 | 0.062 | 0/0 | 0 | 0 | 205 | 177M |  |
| openmed-nemotron | **1739** | 45.4% [42.2%, 49.0%] | 15.0% | 0.355 [0.328, 0.380] | 0.370 | 0.342 | 0.114 | 0.466 | 0.232 | 0/0 | 0 | 0 | 268 | 1.4B |  |
| kalyan-ettin | **1828** | 47.7% [43.8%, 51.7%] | 12.3% | 0.329 [0.304, 0.354] | 0.367 | 0.298 | 0.101 | 0.466 | 0.224 | 0/0 | 0 | 0 | 40 | 68M |  |
| mmbert32k | **2015** | 52.6% [49.2%, 56.7%] | 14.5% | 0.351 [0.320, 0.380] | 0.489 | 0.273 | 0.093 | 0.334 | 0.258 | 0/0 | 0 | 0 | 42 | 308M |  |
| pplx+sent300 | **2016** | 52.6% [48.7%, 56.8%] | 28.4% | 0.331 [0.296, 0.362] | 0.374 | 0.297 | 0.224 | 0.448 | 0.284 | 0/0 | 0 | 0 | 979 | 596M |  |
| pplx+ov100 | **2136** | 55.8% [51.8%, 60.2%] | 29.7% | 0.323 [0.286, 0.357] | 0.370 | 0.287 | 0.268 | 0.428 | 0.293 | 0/0 | 0 | 0 | 909 | 596M |  |
| pplx | **2314** | 60.4% [56.3%, 64.8%] | 28.4% | 0.306 [0.270, 0.339] | 0.360 | 0.266 | 0.270 | 0.397 | 0.290 | 0/0 | 0 | 0 | 481 | 596M |  |
| mmbert32k+nochunk | **2368** | 61.8% [58.3%, 65.5%] | 8.7% | 0.285 [0.258, 0.310] | 0.427 | 0.213 | 0.056 | 0.278 | 0.210 | 0/0 | 0 | 0 | 76 | 308M |  |
| mmbert32k+cpu-int8 | **2481** | 64.8% [61.8%, 68.0%] | 5.9% | 0.258 [0.236, 0.278] | 0.465 | 0.178 | 0.044 | 0.296 | 0.170 | 0/0 | 0 | 0 | 425 | 308M |  |
| gliner2-hivetrace-uni | **2555** | 66.7% [63.7%, 69.6%] | 24.6% | 0.465 [0.440, 0.493] | 0.849 | 0.321 | 0.338 | 0.484 | 0.440 | 0/0 | 0 | 0 | 62 | 147M |  |
| gliner2-vladlinv | **2642** | 69.0% [64.9%, 73.1%] | 19.1% | 0.344 [0.304, 0.383] | 0.856 | 0.215 | 0.275 | 0.455 | 0.288 | 0/0 | 0 | 0 | 21 | 287M |  |
| pii-shield-onnx | **2658** | 69.4% [66.0%, 72.4%] | 12.4% | 0.216 [0.192, 0.244] | 0.303 | 0.168 | 0.121 | 0.313 | 0.078 | 0/0 | 0 | 0 | 8670 | - |  |
| ru-pii-ner | **2668** | 69.7% [66.1%, 73.2%] | 15.7% | 0.265 [0.234, 0.296] | 0.354 | 0.212 | 0.145 | 0.342 | 0.206 | 0/0 | 0 | 0 | 769 | 358M |  |
| apararti | **2725** | 71.1% [67.3%, 75.3%] | 26.4% | 0.281 [0.245, 0.317] | 0.397 | 0.218 | 0.285 | 0.334 | 0.244 | 0/0 | 0 | 0 | 560 | 1.4B |  |
| opf-ru | **2794** | 73.0% [69.6%, 76.3%] | 19.6% | 0.267 [0.235, 0.300] | 0.464 | 0.188 | 0.230 | 0.336 | 0.228 | 0/0 | 0 | 0 | 401 | 1.4B |  |
| opf-kz-ru | **2804** | 73.2% [69.7%, 76.7%] | 23.3% | 0.254 [0.221, 0.286] | 0.370 | 0.193 | 0.247 | 0.313 | 0.226 | 0/0 | 0 | 0 | 559 | 1.4B |  |
| spacy-ru-lg | **2812** | 73.4% [70.4%, 76.3%] | 25.4% | 0.260 [0.241, 0.281] | 0.256 | 0.264 | 0.123 | 0.369 | 0.114 | 0/0 | 0 | 0 | 60 | - |  |
| ru-legal-ner+sent300 | **2824** | 73.7% [70.9%, 76.7%] | 7.7% | 0.185 [0.163, 0.207] | 0.221 | 0.158 | 0.047 | 0.275 | 0.079 | 0/0 | 0 | 0 | 35 | 29M |  |
| openai-base | **2944** | 76.9% [73.5%, 80.5%] | 22.2% | 0.258 [0.221, 0.294] | 0.479 | 0.177 | 0.277 | 0.310 | 0.236 | 0/0 | 0 | 0 | 593 | 1.4B |  |
| opf-ru-v2+sent300 | **2957** | 77.2% [74.2%, 80.3%] | 19.1% | 0.293 [0.258, 0.328] | 0.912 | 0.174 | 0.286 | 0.362 | 0.275 | 0/0 | 0 | 0 | 73 | 1.4B |  |
| opf-ru-v2+ov100 | **2958** | 77.2% [74.1%, 80.2%] | 19.8% | 0.296 [0.262, 0.332] | 0.944 | 0.175 | 0.300 | 0.365 | 0.277 | 0/0 | 0 | 0 | 5028 | 1.4B |  |
| opf-ru-v2 | **3000** | 78.3% [75.3%, 81.2%] | 19.2% | 0.287 [0.254, 0.323] | 0.934 | 0.170 | 0.290 | 0.350 | 0.273 | 0/0 | 0 | 0 | 4189 | 1.4B |  |
| traciora | **3040** | 79.4% [76.5%, 82.2%] | 16.9% | 0.271 [0.240, 0.303] | 0.928 | 0.158 | 0.258 | 0.337 | 0.255 | 0/0 | 0 | 0 | 1561 | 1.4B |  |
| ru-legal-ner+cpu-int8 | **3067** | 80.1% [76.5%, 83.4%] | 6.1% | 0.140 [0.115, 0.166] | 0.184 | 0.113 | 0.029 | 0.222 | 0.060 | 0/0 | 0 | 0 | 30 | 29M |  |
| ru-legal-ner | **3080** | 80.4% [76.8%, 83.8%] | 5.9% | 0.138 [0.113, 0.163] | 0.181 | 0.111 | 0.029 | 0.218 | 0.061 | 0/0 | 0 | 0 | 31 | 29M |  |
| ru-legal-ner+ov100 | **3095** | 80.8% [77.0%, 84.4%] | 6.3% | 0.133 [0.109, 0.160] | 0.174 | 0.108 | 0.033 | 0.215 | 0.060 | 0/0 | 0 | 0 | 34 | 29M |  |
| natasha | **3233** | 84.4% [82.1%, 86.8%] | 14.3% | 0.223 [0.192, 0.253] | 0.734 | 0.132 | 0.185 | 0.260 | 0.104 | 0/0 | 0 | 0 | 23 | - |  |
| fef2-secret-ru | **3482** | 90.9% [89.2%, 92.6%] | 2.1% | 0.114 [0.094, 0.135] | 0.969 | 0.061 | 0.035 | 0.166 | 0.104 | 0/0 | 0 | 0 | 42 | 177M |  |
| gliner-pii-edge+cpu-int8 | **3684** | 96.2% [95.5%, 97.0%] | 3.3% | 0.057 [0.043, 0.069] | 0.927 | 0.029 | 0.063 | 0.073 | 0.035 | 0/0 | 0 | 0 | 602 | 45M |  |
| spacy-alrosait | **3829** | 100.0% [99.9%, 100.0%] | 0.0% | 0.000 [0.000, 0.001] | 1.000 | 0.000 | 0.000 | 0.001 | 0.000 | 0/0 | 0 | 0 | 58 | - |  |
| gliner-multi-v21+cpu-int8 | **3830** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/0 | 0 | 0 | 862 | 289M |  |
| gliner-nvidia+cpu-int8 | **3830** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/0 | 0 | 0 | 1720 | 445M |  |
| gliner-urchade+cpu-int8 | **3830** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/0 | 0 | 0 | 841 | 289M |  |
| rules-ru | **3830** | 100.0% [100.0%, 100.0%] | 0.0% | 0.000 [0.000, 0.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/0 | 0 | 0 | 5 | - |  |

Neighbours by rank a paired bootstrap cannot tell apart (95%, missed %) - pairs, not a transitive chain, so `a ≈ b` and `b ≈ c` do not make `a ≈ c`: gliner25-fastino+sent300 ≈ nuner-zero; nuner-zero ≈ gliner25-fastino; gliner25-fastino ≈ gliner25-fastino+ov100; gliner25-fastino+ov100 ≈ gliner2-large; gliner-multi-v21 ≈ gliner2-hivetrace-omni; gliner2-hivetrace-omni ≈ davlan-mbert+cpu-int8; davlan-mbert+cpu-int8 ≈ davlan-mbert; davlan-mbert ≈ davlan-xlmr; davlan-xlmr ≈ bardsai-eu; bardsai-eu ≈ gliner-pii-edge; stanza-ru ≈ gliner-nvidia+sent300; gliner-nvidia+sent300 ≈ gliner-pii-base; gliner-stream-pii ≈ gliner-urchade; gliner-urchade ≈ davlan-xlmr+cpu-int8; davlan-xlmr+cpu-int8 ≈ nym-small; nym-small ≈ nym-base+ov100; nym-base+ov100 ≈ gliner-nvidia; gliner-nvidia ≈ nym-base; nym-base ≈ gliner-nvidia+ov100; gliner-nvidia+ov100 ≈ ner-ru-yqelz; ner-ru-yqelz ≈ nym-base+cpu-int8; nym-base+cpu-int8 ≈ nym-base+sent300; openmed-multilingual ≈ gliner25-fastino+nochunk; gliner25-fastino+nochunk ≈ pplx+cpu-int8; pplx+cpu-int8 ≈ gravitee-small; gravitee-small ≈ ner-ru-gherman; ner-ru-gherman ≈ ner-ru-gherman-onnx; ner-ru-gherman-onnx ≈ gravitee-small+cpu-int8; gravitee-small+cpu-int8 ≈ ner-ru-gherman+cpu-int8; ner-ru-gherman+cpu-int8 ≈ openmed-nemotron; openmed-nemotron ≈ kalyan-ettin; mmbert32k ≈ pplx+sent300; pplx ≈ mmbert32k+nochunk; mmbert32k+cpu-int8 ≈ gliner2-hivetrace-uni; gliner2-hivetrace-uni ≈ gliner2-vladlinv; gliner2-vladlinv ≈ pii-shield-onnx; pii-shield-onnx ≈ ru-pii-ner; ru-pii-ner ≈ apararti; opf-ru ≈ opf-kz-ru; opf-kz-ru ≈ spacy-ru-lg; spacy-ru-lg ≈ ru-legal-ner+sent300; openai-base ≈ opf-ru-v2+sent300; opf-ru-v2+sent300 ≈ opf-ru-v2+ov100; opf-ru-v2 ≈ traciora; traciora ≈ ru-legal-ner+cpu-int8; ru-legal-ner+cpu-int8 ≈ ru-legal-ner; ru-legal-ner ≈ ru-legal-ner+ov100; ru-legal-ner+ov100 ≈ natasha; spacy-alrosait ≈ gliner-multi-v21+cpu-int8; gliner-multi-v21+cpu-int8 ≈ gliner-nvidia+cpu-int8; gliner-nvidia+cpu-int8 ≈ gliner-urchade+cpu-int8; gliner-urchade+cpu-int8 ≈ rules-ru

## Missed by group

| model | PERSON | ADDRESS | ID | ORG |
|---|---|---|---|---|
| spans in gold | 1030 | 516 | 334 | 1950 |
| gliner2-fastino | 11 (1.1%) | 2 (0.4%) | 22 (6.6%) | 25 (1.3%) |
| gliner25-fastino+sent300 | 11 (1.1%) | 4 (0.8%) | 25 (7.5%) | 78 (4.0%) |
| nuner-zero | 33 (3.2%) | 8 (1.6%) | 50 (15.0%) | 57 (2.9%) |
| gliner25-fastino | 18 (1.7%) | 8 (1.6%) | 34 (10.2%) | 93 (4.8%) |
| gliner25-fastino+ov100 | 29 (2.8%) | 10 (1.9%) | 33 (9.9%) | 86 (4.4%) |
| gliner2-large | 37 (3.6%) | 6 (1.2%) | 128 (38.3%) | 70 (3.6%) |
| gliner-multi-v21 | 33 (3.2%) | 20 (3.9%) | 166 (49.7%) | 156 (8.0%) |
| gliner2-hivetrace-omni | 48 (4.7%) | 28 (5.4%) | 37 (11.1%) | 295 (15.1%) |
| davlan-mbert+cpu-int8 | 28 (2.7%) | 12 (2.3%) | 334 (100.0%) | 118 (6.1%) |
| davlan-mbert | 25 (2.4%) | 8 (1.6%) | 333 (99.7%) | 128 (6.6%) |
| davlan-xlmr | 19 (1.8%) | 10 (1.9%) | 334 (100.0%) | 151 (7.7%) |
| bardsai-eu | 34 (3.3%) | 18 (3.5%) | 211 (63.2%) | 252 (12.9%) |
| gliner-pii-edge | 37 (3.6%) | 12 (2.3%) | 330 (98.8%) | 151 (7.7%) |
| stanza-ru | 67 (6.5%) | 70 (13.6%) | 329 (98.5%) | 147 (7.5%) |
| gliner-nvidia+sent300 | 155 (15.0%) | 27 (5.2%) | 176 (52.7%) | 279 (14.3%) |
| gliner-pii-base | 122 (11.8%) | 50 (9.7%) | 246 (73.7%) | 222 (11.4%) |
| gliner-stream-pii | 256 (24.9%) | 32 (6.2%) | 177 (53.0%) | 277 (14.2%) |
| gliner-urchade | 54 (5.2%) | 80 (15.5%) | 332 (99.4%) | 312 (16.0%) |
| davlan-xlmr+cpu-int8 | 59 (5.7%) | 35 (6.8%) | 334 (100.0%) | 390 (20.0%) |
| nym-small | 37 (3.6%) | 17 (3.3%) | 83 (24.9%) | 739 (37.9%) |
| nym-base+ov100 | 42 (4.1%) | 15 (2.9%) | 61 (18.3%) | 764 (39.2%) |
| gliner-nvidia | 231 (22.4%) | 42 (8.1%) | 175 (52.4%) | 469 (24.1%) |
| nym-base | 43 (4.2%) | 19 (3.7%) | 62 (18.6%) | 793 (40.7%) |
| gliner-nvidia+ov100 | 227 (22.0%) | 40 (7.8%) | 173 (51.8%) | 503 (25.8%) |
| ner-ru-yqelz | 259 (25.1%) | 28 (5.4%) | 331 (99.1%) | 330 (16.9%) |
| nym-base+cpu-int8 | 47 (4.6%) | 24 (4.7%) | 55 (16.5%) | 838 (43.0%) |
| nym-base+sent300 | 56 (5.4%) | 25 (4.8%) | 70 (21.0%) | 853 (43.7%) |
| openmed-multilingual | 78 (7.6%) | 59 (11.4%) | 64 (19.2%) | 1168 (59.9%) |
| gliner25-fastino+nochunk | 375 (36.4%) | 65 (12.6%) | 199 (59.6%) | 776 (39.8%) |
| pplx+cpu-int8 | 11 (1.1%) | 131 (25.4%) | 6 (1.8%) | 1487 (76.3%) |
| gravitee-small | 122 (11.8%) | 124 (24.0%) | 298 (89.2%) | 1123 (57.6%) |
| ner-ru-gherman | 105 (10.2%) | 27 (5.2%) | 334 (100.0%) | 1217 (62.4%) |
| ner-ru-gherman-onnx | 105 (10.2%) | 26 (5.0%) | 334 (100.0%) | 1222 (62.7%) |
| gravitee-small+cpu-int8 | 122 (11.8%) | 151 (29.3%) | 292 (87.4%) | 1132 (58.1%) |
| ner-ru-gherman+cpu-int8 | 109 (10.6%) | 30 (5.8%) | 334 (100.0%) | 1229 (63.0%) |
| openmed-nemotron | 84 (8.2%) | 100 (19.4%) | 255 (76.3%) | 1300 (66.7%) |
| kalyan-ettin | 103 (10.0%) | 146 (28.3%) | 244 (73.1%) | 1335 (68.5%) |
| mmbert32k | 81 (7.9%) | 338 (65.5%) | 20 (6.0%) | 1576 (80.8%) |
| pplx+sent300 | 53 (5.1%) | 181 (35.1%) | 96 (28.7%) | 1686 (86.5%) |
| pplx+ov100 | 38 (3.7%) | 283 (54.8%) | 40 (12.0%) | 1775 (91.0%) |
| pplx | 53 (5.1%) | 341 (66.1%) | 46 (13.8%) | 1874 (96.1%) |
| mmbert32k+nochunk | 157 (15.2%) | 401 (77.7%) | 35 (10.5%) | 1775 (91.0%) |
| mmbert32k+cpu-int8 | 376 (36.5%) | 369 (71.5%) | 64 (19.2%) | 1672 (85.7%) |
| gliner2-hivetrace-uni | 388 (37.7%) | 477 (92.4%) | 319 (95.5%) | 1371 (70.3%) |
| gliner2-vladlinv | 47 (4.6%) | 345 (66.9%) | 329 (98.5%) | 1921 (98.5%) |
| pii-shield-onnx | 654 (63.5%) | 206 (39.9%) | 121 (36.2%) | 1677 (86.0%) |
| ru-pii-ner | 111 (10.8%) | 363 (70.3%) | 285 (85.3%) | 1909 (97.9%) |
| apararti | 163 (15.8%) | 488 (94.6%) | 193 (57.8%) | 1881 (96.5%) |
| opf-ru | 219 (21.3%) | 478 (92.6%) | 243 (72.8%) | 1854 (95.1%) |
| opf-kz-ru | 243 (23.6%) | 504 (97.7%) | 160 (47.9%) | 1897 (97.3%) |
| spacy-ru-lg | 459 (44.6%) | 410 (79.5%) | 334 (100.0%) | 1609 (82.5%) |
| ru-legal-ner+sent300 | 524 (50.9%) | 426 (82.6%) | 143 (42.8%) | 1731 (88.8%) |
| openai-base | 273 (26.5%) | 504 (97.7%) | 239 (71.6%) | 1928 (98.9%) |
| opf-ru-v2+sent300 | 239 (23.2%) | 508 (98.4%) | 310 (92.8%) | 1900 (97.4%) |
| opf-ru-v2+ov100 | 237 (23.0%) | 506 (98.1%) | 314 (94.0%) | 1901 (97.5%) |
| opf-ru-v2 | 261 (25.3%) | 506 (98.1%) | 319 (95.5%) | 1914 (98.2%) |
| traciora | 314 (30.5%) | 485 (94.0%) | 327 (97.9%) | 1914 (98.2%) |
| ru-legal-ner+cpu-int8 | 605 (58.7%) | 475 (92.1%) | 155 (46.4%) | 1832 (93.9%) |
| ru-legal-ner | 613 (59.5%) | 478 (92.6%) | 155 (46.4%) | 1834 (94.1%) |
| ru-legal-ner+ov100 | 610 (59.2%) | 482 (93.4%) | 144 (43.1%) | 1859 (95.3%) |
| natasha | 686 (66.6%) | 368 (71.3%) | 334 (100.0%) | 1845 (94.6%) |
| fef2-secret-ru | 798 (77.5%) | 453 (87.8%) | 334 (100.0%) | 1897 (97.3%) |
| gliner-pii-edge+cpu-int8 | 977 (94.9%) | 456 (88.4%) | 334 (100.0%) | 1917 (98.3%) |
| spacy-alrosait | 1029 (99.9%) | 516 (100.0%) | 334 (100.0%) | 1950 (100.0%) |
| gliner-multi-v21+cpu-int8 | 1030 (100.0%) | 516 (100.0%) | 334 (100.0%) | 1950 (100.0%) |
| gliner-nvidia+cpu-int8 | 1030 (100.0%) | 516 (100.0%) | 334 (100.0%) | 1950 (100.0%) |
| gliner-urchade+cpu-int8 | 1030 (100.0%) | 516 (100.0%) | 334 (100.0%) | 1950 (100.0%) |
| rules-ru | 1030 (100.0%) | 516 (100.0%) | 334 (100.0%) | 1950 (100.0%) |

## Char recall by gold type

| type | group | gliner2-fastino | gliner25-fastino+sent300 | nuner-zero | gliner25-fastino | gliner25-fastino+ov100 | gliner2-large | gliner-multi-v21 | gliner2-hivetrace-omni | davlan-mbert+cpu-int8 | davlan-mbert | davlan-xlmr | bardsai-eu | gliner-pii-edge | stanza-ru | gliner-nvidia+sent300 | gliner-pii-base | gliner-stream-pii | gliner-urchade | davlan-xlmr+cpu-int8 | nym-small | nym-base+ov100 | gliner-nvidia | nym-base | gliner-nvidia+ov100 | ner-ru-yqelz | nym-base+cpu-int8 | nym-base+sent300 | openmed-multilingual | gliner25-fastino+nochunk | pplx+cpu-int8 | gravitee-small | ner-ru-gherman | ner-ru-gherman-onnx | gravitee-small+cpu-int8 | ner-ru-gherman+cpu-int8 | openmed-nemotron | kalyan-ettin | mmbert32k | pplx+sent300 | pplx+ov100 | pplx | mmbert32k+nochunk | mmbert32k+cpu-int8 | gliner2-hivetrace-uni | gliner2-vladlinv | pii-shield-onnx | ru-pii-ner | apararti | opf-ru | opf-kz-ru | spacy-ru-lg | ru-legal-ner+sent300 | openai-base | opf-ru-v2+sent300 | opf-ru-v2+ov100 | opf-ru-v2 | traciora | ru-legal-ner+cpu-int8 | ru-legal-ner | ru-legal-ner+ov100 | natasha | fef2-secret-ru | gliner-pii-edge+cpu-int8 | spacy-alrosait | gliner-multi-v21+cpu-int8 | gliner-nvidia+cpu-int8 | gliner-urchade+cpu-int8 | rules-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CODE | ID | 0.952 | 0.940 | 0.858 | 0.904 | 0.894 | 0.634 | 0.510 | 0.909 | 0.000 | 0.000 | 0.000 | 0.345 | 0.011 | 0.009 | 0.494 | 0.276 | 0.348 | 0.012 | 0.000 | 0.698 | 0.823 | 0.501 | 0.821 | 0.505 | 0.005 | 0.813 | 0.782 | 0.672 | 0.415 | 0.987 | 0.093 | 0.000 | 0.000 | 0.114 | 0.000 | 0.143 | 0.138 | 0.801 | 0.738 | 0.912 | 0.896 | 0.735 | 0.553 | 0.046 | 0.014 | 0.375 | 0.152 | 0.405 | 0.191 | 0.506 | 0.000 | 0.486 | 0.297 | 0.049 | 0.037 | 0.028 | 0.013 | 0.450 | 0.449 | 0.473 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| LOC | ADDRESS | 0.933 | 0.928 | 0.922 | 0.917 | 0.913 | 0.916 | 0.918 | 0.842 | 0.907 | 0.911 | 0.909 | 0.902 | 0.924 | 0.842 | 0.842 | 0.800 | 0.878 | 0.846 | 0.800 | 0.885 | 0.895 | 0.809 | 0.890 | 0.806 | 0.890 | 0.850 | 0.848 | 0.764 | 0.736 | 0.763 | 0.699 | 0.752 | 0.751 | 0.665 | 0.751 | 0.696 | 0.646 | 0.305 | 0.571 | 0.415 | 0.333 | 0.174 | 0.247 | 0.074 | 0.302 | 0.471 | 0.327 | 0.064 | 0.075 | 0.034 | 0.180 | 0.161 | 0.037 | 0.032 | 0.028 | 0.029 | 0.066 | 0.075 | 0.069 | 0.060 | 0.225 | 0.091 | 0.109 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| ORG | ORG | 0.951 | 0.905 | 0.941 | 0.913 | 0.917 | 0.920 | 0.899 | 0.824 | 0.884 | 0.883 | 0.881 | 0.878 | 0.859 | 0.929 | 0.850 | 0.857 | 0.797 | 0.842 | 0.676 | 0.569 | 0.547 | 0.742 | 0.535 | 0.708 | 0.786 | 0.503 | 0.507 | 0.254 | 0.633 | 0.170 | 0.385 | 0.205 | 0.199 | 0.383 | 0.174 | 0.194 | 0.158 | 0.080 | 0.059 | 0.040 | 0.020 | 0.034 | 0.060 | 0.281 | 0.005 | 0.076 | 0.013 | 0.024 | 0.028 | 0.015 | 0.175 | 0.065 | 0.007 | 0.014 | 0.015 | 0.011 | 0.012 | 0.036 | 0.036 | 0.031 | 0.058 | 0.019 | 0.012 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| PERSON | PERSON | 0.915 | 0.949 | 0.945 | 0.971 | 0.970 | 0.955 | 0.978 | 0.864 | 0.776 | 0.777 | 0.781 | 0.888 | 0.975 | 0.962 | 0.737 | 0.897 | 0.743 | 0.971 | 0.745 | 0.853 | 0.869 | 0.684 | 0.846 | 0.695 | 0.688 | 0.834 | 0.826 | 0.799 | 0.708 | 0.961 | 0.886 | 0.625 | 0.627 | 0.883 | 0.625 | 0.694 | 0.618 | 0.750 | 0.831 | 0.872 | 0.871 | 0.678 | 0.440 | 0.591 | 0.861 | 0.289 | 0.789 | 0.837 | 0.722 | 0.742 | 0.621 | 0.381 | 0.729 | 0.743 | 0.750 | 0.737 | 0.670 | 0.301 | 0.294 | 0.293 | 0.343 | 0.187 | 0.056 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## char F1 by domain

| domain | n | gliner2-fastino | gliner25-fastino+sent300 | nuner-zero | gliner25-fastino | gliner25-fastino+ov100 | gliner2-large | gliner-multi-v21 | gliner2-hivetrace-omni | davlan-mbert+cpu-int8 | davlan-mbert | davlan-xlmr | bardsai-eu | gliner-pii-edge | stanza-ru | gliner-nvidia+sent300 | gliner-pii-base | gliner-stream-pii | gliner-urchade | davlan-xlmr+cpu-int8 | nym-small | nym-base+ov100 | gliner-nvidia | nym-base | gliner-nvidia+ov100 | ner-ru-yqelz | nym-base+cpu-int8 | nym-base+sent300 | openmed-multilingual | gliner25-fastino+nochunk | pplx+cpu-int8 | gravitee-small | ner-ru-gherman | ner-ru-gherman-onnx | gravitee-small+cpu-int8 | ner-ru-gherman+cpu-int8 | openmed-nemotron | kalyan-ettin | mmbert32k | pplx+sent300 | pplx+ov100 | pplx | mmbert32k+nochunk | mmbert32k+cpu-int8 | gliner2-hivetrace-uni | gliner2-vladlinv | pii-shield-onnx | ru-pii-ner | apararti | opf-ru | opf-kz-ru | spacy-ru-lg | ru-legal-ner+sent300 | openai-base | opf-ru-v2+sent300 | opf-ru-v2+ov100 | opf-ru-v2 | traciora | ru-legal-ner+cpu-int8 | ru-legal-ner | ru-legal-ner+ov100 | natasha | fef2-secret-ru | gliner-pii-edge+cpu-int8 | spacy-alrosait | gliner-multi-v21+cpu-int8 | gliner-nvidia+cpu-int8 | gliner-urchade+cpu-int8 | rules-ru |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| echr | 127 | 0.635 | 0.671 | 0.729 | 0.695 | 0.701 | 0.650 | 0.690 | 0.717 | 0.829 | 0.823 | 0.834 | 0.819 | 0.778 | 0.370 | 0.786 | 0.744 | 0.721 | 0.679 | 0.757 | 0.534 | 0.560 | 0.763 | 0.551 | 0.757 | 0.628 | 0.533 | 0.530 | 0.433 | 0.737 | 0.420 | 0.494 | 0.496 | 0.492 | 0.495 | 0.473 | 0.355 | 0.329 | 0.351 | 0.331 | 0.323 | 0.306 | 0.285 | 0.258 | 0.465 | 0.344 | 0.216 | 0.265 | 0.281 | 0.267 | 0.254 | 0.260 | 0.185 | 0.258 | 0.293 | 0.296 | 0.287 | 0.271 | 0.140 | 0.138 | 0.133 | 0.223 | 0.114 | 0.057 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Missed at thresholds 0.5 / 0.3 / 0.2 / 0.1

Only models that return a score. A lower threshold keeps more spans: fewer misses, more masking.

| model | 0.5 | 0.3 | 0.2 | 0.1 |
|---|---|---|---|---|
| gliner2-fastino | 60 (1.6%) | 28 (0.7%) | 20 (0.5%) | 11 (0.3%) |
| gliner25-fastino+sent300 | 118 (3.1%) | 59 (1.5%) | 44 (1.1%) | 29 (0.8%) |
| nuner-zero | 148 (3.9%) | 66 (1.7%) | 42 (1.1%) | 26 (0.7%) |
| gliner25-fastino | 153 (4.0%) | 102 (2.7%) | 79 (2.1%) | 49 (1.3%) |
| gliner25-fastino+ov100 | 158 (4.1%) | 92 (2.4%) | 73 (1.9%) | 60 (1.6%) |
| gliner2-large | 241 (6.3%) | 184 (4.8%) | 164 (4.3%) | 115 (3.0%) |
| gliner-multi-v21 | 375 (9.8%) | 151 (3.9%) | 97 (2.5%) | 36 (0.9%) |
| gliner2-hivetrace-omni | 408 (10.7%) | 256 (6.7%) | 189 (4.9%) | 119 (3.1%) |
| davlan-mbert+cpu-int8 | 492 (12.8%) | 481 (12.6%) | 481 (12.6%) | 481 (12.6%) |
| davlan-mbert | 494 (12.9%) | 493 (12.9%) | 493 (12.9%) | 493 (12.9%) |
| davlan-xlmr | 514 (13.4%) | 511 (13.3%) | 511 (13.3%) | 511 (13.3%) |
| bardsai-eu | 515 (13.4%) | 488 (12.7%) | 488 (12.7%) | 488 (12.7%) |
| gliner-pii-edge | 530 (13.8%) | 242 (6.3%) | 181 (4.7%) | 111 (2.9%) |
| gliner-nvidia+sent300 | 637 (16.6%) | 449 (11.7%) | 366 (9.6%) | 261 (6.8%) |
| gliner-pii-base | 640 (16.7%) | 108 (2.8%) | 44 (1.1%) | 13 (0.3%) |
| gliner-stream-pii | 742 (19.4%) | 409 (10.7%) | 282 (7.4%) | 145 (3.8%) |
| gliner-urchade | 778 (20.3%) | 564 (14.7%) | 442 (11.5%) | 330 (8.6%) |
| davlan-xlmr+cpu-int8 | 818 (21.4%) | 710 (18.5%) | 707 (18.5%) | 707 (18.5%) |
| nym-small | 876 (22.9%) | 801 (20.9%) | 801 (20.9%) | 801 (20.9%) |
| nym-base+ov100 | 882 (23.0%) | 811 (21.2%) | 808 (21.1%) | 808 (21.1%) |
| gliner-nvidia | 917 (23.9%) | 666 (17.4%) | 541 (14.1%) | 398 (10.4%) |
| nym-base | 917 (23.9%) | 848 (22.1%) | 845 (22.1%) | 845 (22.1%) |
| gliner-nvidia+ov100 | 943 (24.6%) | 694 (18.1%) | 556 (14.5%) | 421 (11.0%) |
| ner-ru-yqelz | 948 (24.8%) | 893 (23.3%) | 893 (23.3%) | 893 (23.3%) |
| nym-base+cpu-int8 | 964 (25.2%) | 896 (23.4%) | 886 (23.1%) | 886 (23.1%) |
| nym-base+sent300 | 1004 (26.2%) | 927 (24.2%) | 925 (24.2%) | 925 (24.2%) |
| openmed-multilingual | 1369 (35.7%) | 1236 (32.3%) | 1230 (32.1%) | 1230 (32.1%) |
| gliner25-fastino+nochunk | 1415 (36.9%) | 1411 (36.8%) | 1409 (36.8%) | 1407 (36.7%) |
| gravitee-small | 1667 (43.5%) | 1550 (40.5%) | 1550 (40.5%) | 1550 (40.5%) |
| ner-ru-gherman | 1683 (43.9%) | 1660 (43.3%) | 1654 (43.2%) | 1653 (43.2%) |
| ner-ru-gherman-onnx | 1687 (44.0%) | 1666 (43.5%) | 1658 (43.3%) | 1658 (43.3%) |
| gravitee-small+cpu-int8 | 1697 (44.3%) | 1588 (41.5%) | 1588 (41.5%) | 1588 (41.5%) |
| ner-ru-gherman+cpu-int8 | 1702 (44.4%) | 1674 (43.7%) | 1669 (43.6%) | 1669 (43.6%) |
| openmed-nemotron | 1739 (45.4%) | 1503 (39.2%) | 1483 (38.7%) | 1483 (38.7%) |
| kalyan-ettin | 1828 (47.7%) | 1660 (43.3%) | 1649 (43.1%) | 1649 (43.1%) |
| mmbert32k | 2015 (52.6%) | 1662 (43.4%) | 1615 (42.2%) | 1610 (42.0%) |
| mmbert32k+nochunk | 2368 (61.8%) | 1971 (51.5%) | 1908 (49.8%) | 1894 (49.5%) |
| mmbert32k+cpu-int8 | 2481 (64.8%) | 1765 (46.1%) | 1636 (42.7%) | 1623 (42.4%) |
| gliner2-hivetrace-uni | 2555 (66.7%) | 1748 (45.6%) | 1283 (33.5%) | 696 (18.2%) |
| gliner2-vladlinv | 2642 (69.0%) | 2620 (68.4%) | 2607 (68.1%) | 2587 (67.5%) |
| pii-shield-onnx | 2658 (69.4%) | 2254 (58.9%) | 2224 (58.1%) | 2223 (58.0%) |
| apararti | 2725 (71.1%) | 2720 (71.0%) | 2720 (71.0%) | 2720 (71.0%) |
| opf-ru | 2794 (73.0%) | 2773 (72.4%) | 2772 (72.4%) | 2772 (72.4%) |
| opf-kz-ru | 2804 (73.2%) | 2804 (73.2%) | 2804 (73.2%) | 2804 (73.2%) |
| ru-legal-ner+sent300 | 2824 (73.7%) | 2177 (56.8%) | 2090 (54.6%) | 2080 (54.3%) |
| openai-base | 2944 (76.9%) | 2943 (76.8%) | 2943 (76.8%) | 2943 (76.8%) |
| opf-ru-v2+sent300 | 2957 (77.2%) | 2951 (77.0%) | 2950 (77.0%) | 2950 (77.0%) |
| opf-ru-v2+ov100 | 2958 (77.2%) | 2956 (77.2%) | 2955 (77.2%) | 2955 (77.2%) |
| opf-ru-v2 | 3000 (78.3%) | 2997 (78.3%) | 2997 (78.3%) | 2997 (78.3%) |
| traciora | 3040 (79.4%) | 3040 (79.4%) | 3040 (79.4%) | 3040 (79.4%) |
| ru-legal-ner+cpu-int8 | 3067 (80.1%) | 2446 (63.9%) | 2376 (62.0%) | 2366 (61.8%) |
| ru-legal-ner | 3080 (80.4%) | 2485 (64.9%) | 2419 (63.2%) | 2411 (63.0%) |
| ru-legal-ner+ov100 | 3095 (80.8%) | 2503 (65.4%) | 2419 (63.2%) | 2409 (62.9%) |
| fef2-secret-ru | 3482 (90.9%) | 3480 (90.9%) | 3480 (90.9%) | 3480 (90.9%) |
| gliner-pii-edge+cpu-int8 | 3684 (96.2%) | 2878 (75.1%) | 2154 (56.2%) | 1167 (30.5%) |
| gliner-nvidia+cpu-int8 | 3830 (100.0%) | 3830 (100.0%) | 3828 (99.9%) | 3710 (96.9%) |
| gliner-urchade+cpu-int8 | 3830 (100.0%) | 3830 (100.0%) | 3830 (100.0%) | 3827 (99.9%) |

Notes: the unit of counting is one gold span after boundary normalization - the same unit in `missed`, in the group table, in the threshold table and in the ensembles; two annotations that share boundaries but not type are two spans, so an empty answer misses 100%. Gold and predicted boundaries are normalized the same way (whitespace, word boundaries, merge of adjacent same-label pieces). `dropped spans` - predicted intervals outside the text: rejected, not clipped to fit. A run made before `run.py` started clipping span ends to the piece it fed the model can carry them; `meta.clipped` counts what the clipping fixes in newer runs. Zero-shot models get the taxonomy of the set as labels (the `labels` field of `meta.json`). `train` - the model was trained on the source of this set (its slices and corrupted copies included): its row is not comparable with the others and stays out of the pooled numbers; an empty `contaminated` list in `benchmark/models.toml` means no evidence of overlap was found, not proof of none. `hidden` - gold spans every character of which is covered; a touched span counts as detected, not as hidden. missed % and char F1 carry 95% bootstrap intervals over rows (1000 resamples, the same rows for every model of the set). The group of a gold type comes from `BENCH/<set>/meta.json`; a model label with no group falls into OTHER. ms/row is a median and includes chunking of long texts; hardware and batch are in the meta line of the prediction file.
