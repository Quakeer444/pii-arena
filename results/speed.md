# Speed

Chars/s = chars / elapsed_s pooled over the sets of the run, rows/s the same way. `chars` comes from the meta line of the prediction file, or is counted from `bench.csv` for older runs. `x pplx` is the speed relative to the `pplx` run made under the same conditions - same machine (device + gpu or cpu model + threads + W), same cutting variant, same quantization; a row with no such pplx run carries `-`. `gpu / cpu` names the accelerator or, on CPU, the processor model (older files carry `-` and fall into one machine). `W` is how many run.py processes shared the node (`meta.workers`): every number here is batch throughput under that load, not the latency of one request - that takes a separate W=1, batch=1 run. Amortized ms/row p50 / p95 are quantiles of the per-row share of measured compute, not individually timed request latency: for model runs the batch time is divided across the pieces of the row and summed over its pieces, for scanners the whole run time is divided by the row count, so every row of a scanner run carries the same value. Timing boundaries differ between the paths: model timing covers the inference loop only (model load, text preparation, normalization and chunk-list construction happen outside `elapsed_s`), scanner timing includes process start and the whole scan. `rss MB` is the largest peak among the runs pooled into the row. Partial runs (`meta.limit`) are here but not in the quality tables.

Left out: pii-shield-onnx - onnx runs whose meta says `cuda`. The graph always goes through `CPUExecutionProvider`, so the run was CPU-bound while the meta names a GPU and no processor: there is no machine to attribute the speed to. Their quality numbers stay in the reports.

## cpu

| model | chars/s | rows/s | x pplx | amortized ms/row p50 | p95 | gpu / cpu | threads | W | quant | variant | rss MB | sets |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| betterleaks | 1934632 | 6427.14 | - | 0 | 0 | - | - | - | - | - | - | 9 |
| titus | 174472 | 453.10 | - | 1 | 5 | - | - | - | - | - | - | 3 |
| noseyparker | 142288 | 369.51 | - | 2 | 10 | - | - | - | - | - | - | 3 |
| kingfisher | 136969 | 355.70 | - | 2 | 11 | - | - | - | - | - | - | 3 |
| credsweeper-noml | 52155 | 135.44 | - | 4 | 37 | - | - | - | - | - | - | 3 |
| trufflehog | 27652 | 71.81 | - | 12 | 48 | - | - | - | - | - | - | 3 |
| detect-secrets | 18599 | 48.30 | - | 12 | 90 | - | - | - | - | - | - | 3 |
| deepsecrets | 12516 | 32.50 | - | 24 | 96 | - | - | - | - | - | - | 3 |
| presidio-ru | 4846 | 30.66 | - | 23 | 95 | - | - | - | - | - | - | 2 |
| credsweeper | 2466 | 6.40 | - | 193 | 219 | - | - | - | - | - | - | 3 |
| ru-legal-ner+cpu | 30172 | 80.65 | - | 11 | 23 | - | 1 | - | - | cpu | 550 | 2 |
| openai-base-onnx | 3152 | 0.91 | - | 938 | 2329 | AMD EPYC 7713P 64-Core Processor | 8 | 1 | - | - | 8894 | 3 |
| gliner-urchade-ru+cpu-int8 | 843 | 3.88 | - | 230 | 605 | AMD EPYC 7713P 64-Core Processor | 8 | 1 | int8 | cpu-int8 | 3559 | 3 |
| nym-small | 3375 | 6.39 | - | 66 | 572 | AMD EPYC 7713P 64-Core Processor | 8 | 2 | - | - | 3986 | 15 |
| pii-shield-onnx | 1167 | 3.80 | - | 224 | 732 | AMD EPYC 7713P 64-Core Processor | 8 | 2 | - | - | 3820 | 7 |
| pii-shield-onnx | 1236 | 0.79 | - | 514 | 5031 | AMD EPYC 7713P 64-Core Processor | 8 | 3 | - | - | 8601 | 8 |
| ner-ru-gherman+cpu-int8 | 5693 | 1.33 | - | 728 | 1230 | AMD EPYC 7763 64-Core Processor | 8 | 1 | int8 | cpu-int8 | 1524 | 1 |
| gliner-nvidia-ru+cpu-int8 | 493 | 0.11 | - | 8614 | 15117 | AMD EPYC 7B13 64-Core Processor | 16 | 1 | int8 | cpu-int8 | 3947 | 1 |
| gliner-pii-edge+cpu-int8 | 250 | 0.26 | - | 2610 | 10948 | AMD EPYC 7B13 64-Core Processor | 40 | 1 | int8 | cpu-int8 | 4967 | 1 |
| gliner-urchade-ru+cpu-int8 | 983 | 0.23 | - | 4308 | 7126 | AMD EPYC 7B13 64-Core Processor | 8 | 1 | int8 | cpu-int8 | 3098 | 1 |
| ru-legal-ner+cpu-int8 | 54911 | 85.09 | - | 5 | 50 | AMD EPYC 9654 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 1110 | 9 |
| ru-legal-ner+cpu-speed | 33180 | 500.00 | 45.67 | 2 | 4 | AMD EPYC 9654 96-Core Processor | 16 | 24 | - | cpu-speed | 755 | 1 |
| nym-base+cpu-int8 | 5230 | 8.10 | - | 45 | 579 | AMD EPYC 9654 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 2627 | 9 |
| mmbert32k+cpu-int8 | 5136 | 7.96 | - | 45 | 589 | AMD EPYC 9654 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 2875 | 9 |
| nym-base+cpu-speed | 2998 | 7.54 | 4.13 | 73 | 470 | AMD EPYC 9654 96-Core Processor | 16 | 24 | - | cpu-speed | 1790 | 3 |
| opf-ru+cpu-speed | 2808 | 6.33 | 3.86 | 136 | 300 | AMD EPYC 9654 96-Core Processor | 16 | 24 | - | cpu-speed | 2949 | 1 |
| gliner2-vladlinv-ru+cpu-speed | 2245 | 0.53 | 3.09 | 1837 | 3379 | AMD EPYC 9654 96-Core Processor | 16 | 24 | - | cpu-speed | 3452 | 1 |
| gliner-nvidia+cpu-speed | 1182 | 4.29 | 1.63 | 211 | 483 | AMD EPYC 9654 96-Core Processor | 16 | 24 | - | cpu-speed | 4250 | 1 |
| opf-ru-v2+cpu-speed | 1125 | 16.95 | 1.55 | 53 | 88 | AMD EPYC 9654 96-Core Processor | 16 | 24 | - | cpu-speed | 2700 | 1 |
| gliner-nvidia+cpu-int8 | 932 | 1.44 | - | 370 | 2733 | AMD EPYC 9654 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 4882 | 9 |
| pplx+cpu-speed | 727 | 2.85 | 1.00 | 374 | 748 | AMD EPYC 9654 96-Core Processor | 16 | 24 | - | cpu-speed | 3959 | 2 |
| bardsai-eu | 615 | 0.95 | - | 594 | 3914 | AMD EPYC 9654 96-Core Processor | 8 | 36 | - | - | 2139 | 9 |
| nym-small | 487 | 0.76 | - | 770 | 4487 | AMD EPYC 9654 96-Core Processor | 8 | 36 | - | - | 2403 | 9 |
| pii-shield-onnx | 339 | 0.53 | - | 1126 | 6573 | AMD EPYC 9654 96-Core Processor | 8 | 36 | - | - | 4222 | 9 |
| pplx+cpu-int8 | 218 | 0.34 | 1.00 | 145 | 2483 | AMD EPYC 9654 96-Core Processor | 8 | 36 | int8 | cpu-int8 | 4775 | 9 |
| natasha+cpu-speed | 130799 | 83.33 | 130.02 | 3 | 49 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 209 | 9 |
| spacy-alrosait+cpu-speed | 53307 | 33.96 | 52.99 | 9 | 121 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 1492 | 9 |
| spacy-ru-lg+cpu-speed | 52320 | 33.33 | 52.01 | 7 | 128 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 1494 | 9 |
| ru-legal-ner+cpu-speed | 50942 | 28.99 | 50.64 | 11 | 134 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 903 | 8 |
| gravitee-small+cpu-speed | 15141 | 9.65 | 15.05 | 40 | 485 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 1065 | 9 |
| gravitee-small+cpu-int8 | 12174 | 18.87 | - | 16 | 188 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 1210 | 9 |
| kalyan-ettin+cpu-speed | 8742 | 5.57 | 8.69 | 65 | 873 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 1148 | 9 |
| ru-pii-ner+cpu-speed | 7053 | 4.49 | 7.01 | 64 | 1023 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 2774 | 9 |
| gliner2-hivetrace-uni-ru+cpu-speed | 4906 | 4.04 | 4.88 | 106 | 1025 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 2088 | 4 |
| davlan-xlmr+cpu-speed | 4431 | 2.82 | 4.40 | 90 | 1552 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 1612 | 9 |
| mmbert32k+cpu-speed | 4313 | 2.75 | 4.29 | 85 | 1514 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 1856 | 9 |
| davlan-xlmr+cpu-int8 | 4108 | 6.37 | - | 38 | 777 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 2012 | 9 |
| ner-ru-gherman+cpu-speed | 4026 | 2.56 | 4.00 | 118 | 1659 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 1332 | 9 |
| davlan-mbert+cpu-speed | 3983 | 2.54 | 3.96 | 109 | 1686 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 1367 | 9 |
| ner-ru-gherman+cpu-int8 | 3509 | 6.89 | - | 57 | 520 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 1706 | 8 |
| gliner2-hivetrace-uni+cpu-speed | 3424 | 1.74 | 3.40 | 242 | 2108 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 2495 | 7 |
| openmed-nemotron+cpu-speed | 3287 | 2.09 | 3.27 | 118 | 1844 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 2848 | 9 |
| fef2-secret-ru+cpu-speed | 3278 | 2.09 | 3.26 | 113 | 2073 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 1395 | 9 |
| davlan-mbert+cpu-int8 | 3201 | 6.28 | - | 76 | 550 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 1618 | 8 |
| nym-base+cpu-speed | 3116 | 1.45 | 3.10 | 168 | 3014 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 2053 | 6 |
| openmed-multilingual+cpu-speed | 3076 | 1.96 | 3.06 | 117 | 2130 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 2783 | 9 |
| traciora+cpu-speed | 3040 | 1.94 | 3.02 | 130 | 1977 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3544 | 9 |
| opf-kz-ru+cpu-speed | 2950 | 1.88 | 2.93 | 128 | 2165 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3807 | 9 |
| opf-ru-v2+cpu-speed | 2886 | 1.64 | 2.87 | 197 | 2264 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3626 | 8 |
| opf-ru+cpu-speed | 2839 | 1.66 | 2.82 | 149 | 2145 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3721 | 8 |
| fef2-secret-ru+cpu-int8 | 2821 | 6.21 | - | 75 | 648 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 1664 | 7 |
| apararti+cpu-speed | 2446 | 1.56 | 2.43 | 158 | 2499 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3999 | 9 |
| openai-base+cpu-speed | 2378 | 1.51 | 2.36 | 159 | 2679 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 4188 | 9 |
| gliner-pii-base+cpu-speed | 1907 | 1.21 | 1.90 | 310 | 3302 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3054 | 9 |
| gliner-urchade+cpu-int8 | 1624 | 2.73 | - | 174 | 1416 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 4498 | 8 |
| gliner-urchade-ru+cpu-speed | 1608 | 1.32 | 1.60 | 333 | 2893 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3141 | 4 |
| gliner-multi-v21+cpu-int8 | 1586 | 2.67 | - | 198 | 1398 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 4578 | 8 |
| gliner-multi-v21-ru+cpu-speed | 1491 | 1.23 | 1.48 | 332 | 3447 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3122 | 4 |
| gliner-pii-edge+cpu-speed | 1454 | 0.93 | 1.45 | 435 | 3678 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3842 | 9 |
| ner-ru-yqelz+cpu-speed | 1413 | 0.90 | 1.40 | 298 | 4727 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 2506 | 9 |
| gliner-pii-edge+cpu-int8 | 1327 | 2.49 | - | 265 | 1340 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 2343 | 7 |
| gliner25-fastino-ru+cpu-speed | 1301 | 1.07 | 1.29 | 499 | 3438 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3157 | 4 |
| gliner-pii-base+cpu-int8 | 1266 | 5.04 | - | 112 | 544 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | int8 | cpu-int8 | 2743 | 5 |
| gliner-stream-pii+cpu-speed | 1219 | 0.78 | 1.21 | 453 | 5465 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 5957 | 9 |
| stanza-ru+cpu-speed | 1198 | 0.76 | 1.19 | 257 | 6290 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 1467 | 9 |
| gliner2-hivetrace-omni-ru+cpu-speed | 1163 | 0.96 | 1.16 | 683 | 3647 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3330 | 4 |
| gliner2-fastino-ru+cpu-speed | 1123 | 0.92 | 1.12 | 697 | 3585 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3324 | 4 |
| gliner-urchade+cpu-speed | 1033 | 0.66 | 1.03 | 437 | 6519 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3139 | 9 |
| gliner-multi-v21+cpu-speed | 1011 | 0.64 | 1.00 | 483 | 6741 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3244 | 9 |
| pplx+cpu-speed | 1006 | 0.52 | 1.00 | 642 | 7479 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 4133 | 7 |
| gliner25-fastino+cpu-speed | 802 | 0.51 | 0.80 | 714 | 8092 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 4490 | 9 |
| gliner2-vladlinv+cpu-speed | 690 | 0.44 | 0.69 | 860 | 9428 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 4536 | 9 |
| gliner2-hivetrace-omni+cpu-speed | 676 | 0.43 | 0.67 | 865 | 9516 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 4567 | 9 |
| gliner2-fastino+cpu-speed | 670 | 0.43 | 0.67 | 914 | 10073 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 4665 | 9 |
| gliner2-vladlinv-ru+cpu-speed | 569 | 2.64 | 0.57 | 373 | 942 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 3155 | 3 |
| gliner-nvidia-ru+cpu-speed | 500 | 0.41 | 0.50 | 1223 | 8802 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 4266 | 4 |
| nuner-zero+cpu-speed | 497 | 0.32 | 0.49 | 1573 | 12582 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 4263 | 9 |
| gliner-nvidia+cpu-speed | 442 | 0.26 | 0.44 | 2184 | 15780 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 4259 | 8 |
| gliner2-large+cpu-speed | 405 | 0.26 | 0.40 | 2079 | 14714 | AMD EPYC 9K84 96-Core Processor | 16 | 24 | - | cpu-speed | 5969 | 9 |
| natasha | 148920 | 268.66 | - | 2 | 14 | AMD EPYC 9K84 96-Core Processor | 2 | 123 | - | - | 209 | 41 |
| spacy-alrosait | 63466 | 114.50 | - | 4 | 38 | AMD EPYC 9K84 96-Core Processor | 2 | 123 | - | - | 1522 | 41 |
| spacy-ru-lg | 61081 | 110.20 | - | 4 | 40 | AMD EPYC 9K84 96-Core Processor | 2 | 123 | - | - | 1495 | 41 |
| ner-ru-gherman-onnx | 1857 | 5.00 | - | 146 | 403 | AMD EPYC 9K84 96-Core Processor | 8 | 24 | - | - | 1065 | 4 |
| bardsai-eu | 1248 | 1.91 | - | 298 | 1645 | AMD EPYC 9K84 96-Core Processor | 8 | 24 | - | - | 1726 | 17 |
| bardsai-eu | 403 | 1.16 | - | 532 | 2611 | AMD EPYC 9K84 96-Core Processor | 8 | 32 | - | - | 1751 | 15 |
| nym-small | 260 | 1.91 | - | 390 | 1140 | AMD EPYC 9K84 96-Core Processor | 8 | 32 | - | - | 1554 | 2 |
| pii-shield-onnx | 188 | 0.60 | - | 1022 | 4964 | AMD EPYC 9K84 96-Core Processor | 8 | 32 | - | - | 1937 | 12 |
| gliner-pii-edge+cpu-int8 | 5958 | 1.17 | - | 602 | 1928 | AMD EPYC 9K84 96-Core Processor | 8 | 48 | int8 | cpu-int8 | 1237 | 1 |
| gliner-urchade+cpu-int8 | 5108 | 1.00 | - | 841 | 2273 | AMD EPYC 9K84 96-Core Processor | 8 | 48 | int8 | cpu-int8 | 3312 | 1 |
| gliner-multi-v21+cpu-int8 | 4583 | 0.90 | - | 862 | 2748 | AMD EPYC 9K84 96-Core Processor | 8 | 48 | int8 | cpu-int8 | 3160 | 1 |
| gitleaks | 1793782 | 5893.91 | - | 0 | 0 | Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz | - | 1 | - | - | - | 10 |
| rules-ru | 714630 | 1289.26 | - | 0 | 3 | Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz | - | 1 | - | - | - | 41 |
| detect-secrets | 23323 | 21.85 | - | 45 | 45 | Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz | - | 1 | - | - | - | 1 |
| credsweeper-noml | 15359 | 14.39 | - | 69 | 69 | Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz | - | 1 | - | - | - | 1 |
| deepsecrets | 12851 | 12.04 | - | 82 | 82 | Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz | - | 1 | - | - | - | 1 |
| openai-base-onnx | 1496 | 9.12 | - | 83 | 226 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 3 | 1 | - | - | 6079 | 2 |
| nym-small | 2137 | 17.68 | - | 54 | 98 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 3 | 2 | - | - | 1290 | 4 |
| davlan-mbert+cpu-int8 | 3231 | 0.75 | - | 1289 | 2150 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 8 | 10 | int8 | cpu-int8 | 1412 | 1 |
| fef2-secret-ru+cpu-int8 | 3230 | 0.72 | - | 1353 | 2399 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 8 | 10 | int8 | cpu-int8 | 1443 | 2 |
| gliner-pii-base+cpu-int8 | 1837 | 0.92 | - | 749 | 3116 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 8 | 10 | int8 | cpu-int8 | 3948 | 4 |
| nym-small | 2286 | 2.74 | - | 162 | 1336 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 8 | 2 | - | - | 2020 | 11 |
| ner-ru-gherman-onnx | 1913 | 2.32 | - | 186 | 1745 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 8 | 2 | - | - | 2446 | 5 |
| openai-base-onnx | 1263 | 2.80 | - | 261 | 940 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 8 | 2 | - | - | 8355 | 4 |
| pii-shield-onnx | 430 | 2.14 | - | 376 | 1088 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 8 | 3 | - | - | 1988 | 2 |
| gliner-multi-v21-ru+cpu-int8 | 823 | 1.77 | - | 346 | 2316 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 8 | 4 | int8 | cpu-int8 | 3477 | 4 |
| gliner-nvidia-ru+cpu-int8 | 149 | 0.68 | - | 1076 | 4144 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 8 | 4 | int8 | cpu-int8 | 4647 | 3 |
| kalyan-ettin+cpu-int8 | 3243 | 5.03 | - | 110 | 716 | Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz | 8 | 6 | int8 | cpu-int8 | 1408 | 9 |

## cuda

| model | chars/s | rows/s | x pplx | amortized ms/row p50 | p95 | gpu / cpu | threads | W | quant | variant | rss MB | sets |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fef2-secret-ru | 108162 | 121.64 | 111.47 | 1 | 37 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 1547 | 2 |
| gliner2-hivetrace-omni | 76484 | 87.64 | 78.82 | 2 | 53 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3439 | 2 |
| gliner2-vladlinv-ru | 63859 | 241.10 | 65.81 | 4 | 10 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3336 | 2 |
| gravitee-small | 53212 | 307.13 | 54.84 | 3 | 5 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 1232 | 3 |
| gliner2-hivetrace-uni-ru | 50761 | 60.46 | 52.31 | 13 | 39 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 2073 | 2 |
| gliner25-fastino+nochunk | 38440 | 74.50 | - | 2 | 75 | NVIDIA GeForce RTX 5090 | - | 1 | - | nochunk | 3343 | 2 |
| gliner2-vladlinv | 31052 | 759.17 | 32.00 | 1 | 4 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3342 | 1 |
| gliner-nvidia+sent300 | 28402 | 16.50 | - | 45 | 153 | NVIDIA GeForce RTX 5090 | - | 1 | - | sent300 | 4258 | 1 |
| ru-legal-ner | 26616 | 650.71 | 27.43 | 1 | 1 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 1299 | 1 |
| gliner2-fastino-ru | 24841 | 607.33 | 25.60 | 1 | 4 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3336 | 1 |
| gliner-multi-v21-ru | 23289 | 569.38 | 24.00 | 1 | 2 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3615 | 1 |
| gliner25-fastino-ru | 23289 | 569.38 | 24.00 | 1 | 7 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3331 | 1 |
| ner-ru-gherman | 23289 | 569.38 | 24.00 | 1 | 2 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 1540 | 1 |
| nym-base | 23289 | 569.38 | 24.00 | 2 | 2 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 2492 | 1 |
| davlan-mbert | 21919 | 535.88 | 22.59 | 1 | 2 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 1524 | 1 |
| ner-ru-yqelz | 21919 | 535.88 | 22.59 | 2 | 2 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3441 | 1 |
| gliner25-fastino | 18631 | 455.50 | 19.20 | 1 | 8 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 2753 | 1 |
| davlan-xlmr | 17744 | 433.81 | 18.29 | 1 | 1 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 2193 | 1 |
| mmbert32k | 17744 | 433.81 | 18.29 | 2 | 2 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 2459 | 1 |
| gliner2-fastino | 15526 | 379.58 | 16.00 | 2 | 8 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3473 | 1 |
| kalyan-ettin | 15526 | 379.58 | 16.00 | 2 | 3 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 1497 | 1 |
| gliner2-hivetrace-omni-ru | 13801 | 337.41 | 14.22 | 2 | 9 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3346 | 1 |
| gliner-multi-v21 | 12849 | 314.14 | 13.24 | 2 | 3 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3633 | 1 |
| gliner-urchade-ru | 12849 | 314.14 | 13.24 | 2 | 3 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3232 | 1 |
| gliner2-large | 12421 | 303.67 | 12.80 | 3 | 8 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 4534 | 1 |
| gliner-pii-base | 12020 | 293.87 | 12.39 | 2 | 2 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 2146 | 1 |
| gliner-pii-edge | 12020 | 293.87 | 12.39 | 2 | 15 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 1569 | 1 |
| gliner-nvidia-ru | 11292 | 276.06 | 11.64 | 3 | 4 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 4311 | 1 |
| gliner-urchade | 10959 | 267.94 | 11.29 | 3 | 3 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3151 | 1 |
| gliner-nvidia | 10646 | 260.29 | 10.97 | 3 | 4 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 4214 | 1 |
| nuner-zero | 8872 | 216.90 | 9.14 | 4 | 5 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 4352 | 1 |
| gliner2-hivetrace-uni | 8280 | 202.44 | 8.53 | 5 | 5 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 2056 | 1 |
| traciora | 6424 | 157.07 | 6.62 | 6 | 6 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 5061 | 1 |
| opf-kz-ru | 5733 | 140.15 | 5.91 | 7 | 7 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 4520 | 1 |
| stanza-ru | 5323 | 130.14 | 5.49 | 7 | 8 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 1908 | 1 |
| apararti | 5248 | 128.31 | 5.41 | 8 | 8 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 4041 | 1 |
| openai-base | 3298 | 80.62 | 3.40 | 12 | 12 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 4148 | 1 |
| openmed-multilingual | 2889 | 70.62 | 2.98 | 13 | 15 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3916 | 1 |
| opf-ru | 2606 | 63.71 | 2.69 | 15 | 16 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3887 | 1 |
| openmed-nemotron | 2518 | 61.55 | 2.59 | 15 | 17 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3894 | 1 |
| ru-pii-ner | 1509 | 36.88 | 1.55 | 26 | 29 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 3493 | 1 |
| pplx | 970 | 23.72 | 1.00 | 39 | 42 | NVIDIA GeForce RTX 5090 | - | 1 | - | - | 4267 | 1 |
| gliner25-fastino+ov100 | 84624 | 61.82 | 16.31 | 9 | 52 | NVIDIA GeForce RTX 5090 | - | 2 | - | ov100 | 2816 | 11 |
| ru-legal-ner+sent300 | 79749 | 58.26 | 22.62 | 9 | 71 | NVIDIA GeForce RTX 5090 | - | 2 | - | sent300 | 1372 | 11 |
| ru-legal-ner+ov100 | 77809 | 56.85 | 15.00 | 9 | 72 | NVIDIA GeForce RTX 5090 | - | 2 | - | ov100 | 1325 | 11 |
| ru-legal-ner | 76562 | 135.32 | 16.82 | 3 | 29 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 1367 | 40 |
| gliner25-fastino+sent300 | 75466 | 55.13 | 21.41 | 10 | 63 | NVIDIA GeForce RTX 5090 | - | 2 | - | sent300 | 2839 | 11 |
| davlan-xlmr | 73674 | 130.22 | 16.19 | 4 | 30 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 2184 | 40 |
| nym-base+sent300 | 73145 | 53.44 | 20.75 | 10 | 76 | NVIDIA GeForce RTX 5090 | - | 2 | - | sent300 | 2456 | 11 |
| nym-base | 72492 | 128.13 | 15.93 | 4 | 30 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 2456 | 40 |
| nym-base+ov100 | 71675 | 52.36 | 13.82 | 11 | 73 | NVIDIA GeForce RTX 5090 | - | 2 | - | ov100 | 2456 | 11 |
| ru-legal-ner+homoglyph | 69717 | 181.37 | 15.01 | 2 | 24 | NVIDIA GeForce RTX 5090 | - | 2 | - | homoglyph | 1301 | 3 |
| davlan-mbert | 68000 | 120.19 | 14.94 | 4 | 32 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 1522 | 40 |
| fef2-secret-ru | 66971 | 140.02 | 14.72 | 4 | 24 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 1547 | 35 |
| ner-ru-gherman | 66682 | 117.86 | 14.65 | 4 | 33 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 1541 | 40 |
| gliner25-fastino | 65451 | 115.68 | 14.38 | 4 | 35 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 2856 | 40 |
| gliner-pii-base | 63679 | 112.55 | 13.99 | 4 | 37 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 2123 | 40 |
| gliner2-vladlinv+homoglyph | 61681 | 160.47 | 13.28 | 4 | 18 | NVIDIA GeForce RTX 5090 | - | 2 | - | homoglyph | 3208 | 3 |
| nym-base+homoglyph | 59103 | 153.76 | 12.73 | 3 | 24 | NVIDIA GeForce RTX 5090 | - | 2 | - | homoglyph | 2455 | 3 |
| ner-ru-gherman+homoglyph | 58063 | 151.06 | 12.50 | 3 | 24 | NVIDIA GeForce RTX 5090 | - | 2 | - | homoglyph | 1539 | 3 |
| gliner2-vladlinv | 57801 | 102.16 | 12.70 | 4 | 39 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3229 | 40 |
| ner-ru-yqelz | 56345 | 99.59 | 12.38 | 5 | 38 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3300 | 40 |
| mmbert32k | 54765 | 96.80 | 12.03 | 4 | 40 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 2434 | 40 |
| gliner-multi-v21 | 53869 | 95.21 | 11.84 | 5 | 39 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3182 | 40 |
| gliner25-fastino+nochunk | 52570 | 37.96 | - | 16 | 84 | NVIDIA GeForce RTX 5090 | - | 2 | - | nochunk | 2774 | 4 |
| gliner-urchade | 49158 | 86.89 | 10.80 | 5 | 46 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3140 | 40 |
| gliner-stream-pii | 48113 | 64.04 | 10.57 | 7 | 61 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 4868 | 11 |
| mmbert32k+nochunk | 39995 | 29.22 | - | 17 | 138 | NVIDIA GeForce RTX 5090 | - | 2 | - | nochunk | 2433 | 11 |
| gliner2-fastino | 37693 | 66.62 | 8.28 | 7 | 57 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3348 | 40 |
| gliner2-hivetrace-omni | 34790 | 67.59 | 7.65 | 7 | 56 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3334 | 30 |
| gliner-nvidia+ov100 | 29500 | 21.55 | 5.69 | 30 | 146 | NVIDIA GeForce RTX 5090 | - | 2 | - | ov100 | 4231 | 11 |
| gliner-nvidia+homoglyph | 27769 | 72.24 | 5.98 | 9 | 38 | NVIDIA GeForce RTX 5090 | - | 2 | - | homoglyph | 4247 | 3 |
| gliner-nvidia | 26888 | 47.52 | 5.91 | 9 | 80 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 4255 | 40 |
| nuner-zero | 26176 | 46.27 | 5.75 | 10 | 82 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 4287 | 40 |
| gliner-nvidia+sent300 | 25597 | 27.66 | 7.26 | 24 | 104 | NVIDIA GeForce RTX 5090 | - | 2 | - | sent300 | 4257 | 7 |
| gliner2-large | 16474 | 29.12 | 3.62 | 16 | 130 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 4506 | 40 |
| openmed-multilingual | 11953 | 17.15 | 2.63 | 30 | 211 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3821 | 31 |
| openmed-nemotron | 11447 | 16.42 | 2.52 | 31 | 222 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3821 | 31 |
| opf-ru | 8946 | 12.83 | 1.97 | 42 | 275 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3817 | 31 |
| traciora | 7361 | 11.17 | 1.62 | 52 | 347 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3814 | 10 |
| opf-kz-ru | 6275 | 11.09 | 1.38 | 59 | 298 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3814 | 40 |
| apararti | 5933 | 10.49 | 1.30 | 62 | 320 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3815 | 40 |
| openai-base | 5543 | 7.95 | 1.22 | 71 | 437 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 3814 | 31 |
| pplx+ov100 | 5187 | 3.79 | 1.00 | 143 | 854 | NVIDIA GeForce RTX 5090 | - | 2 | - | ov100 | 4234 | 11 |
| pplx+homoglyph | 4645 | 12.08 | 1.00 | 54 | 241 | NVIDIA GeForce RTX 5090 | - | 2 | - | homoglyph | 4234 | 3 |
| pplx | 4551 | 8.04 | 1.00 | 60 | 426 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 4234 | 40 |
| pplx+sent300 | 3525 | 2.58 | 1.00 | 215 | 1387 | NVIDIA GeForce RTX 5090 | - | 2 | - | sent300 | 4234 | 11 |
| gliner-pii-edge | 1723 | 9.29 | 0.38 | 22 | 435 | NVIDIA GeForce RTX 5090 | - | 2 | - | - | 1685 | 6 |
| gravitee-small | 67914 | 97.03 | - | 6 | 38 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 1250 | 26 |
| fef2-secret-ru | 63108 | 53.40 | - | 11 | 60 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 1534 | 4 |
| gliner2-vladlinv-ru | 44875 | 105.86 | - | 6 | 31 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 3221 | 17 |
| gliner25-fastino-ru | 38527 | 91.22 | - | 7 | 31 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 3229 | 18 |
| gliner-urchade-ru | 35298 | 83.57 | - | 8 | 38 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 3154 | 18 |
| gliner2-hivetrace-omni | 27995 | 39.20 | - | 11 | 104 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 3335 | 9 |
| gliner-multi-v21-ru | 27925 | 66.11 | - | 10 | 45 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 3141 | 18 |
| gliner25-fastino-ru+nochunk | 27579 | 54.84 | - | 12 | 89 | NVIDIA GeForce RTX 5090 | - | 4 | - | nochunk | 3192 | 1 |
| kalyan-ettin | 24459 | 43.23 | - | 7 | 97 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 1528 | 40 |
| gliner2-hivetrace-uni | 23368 | 41.30 | - | 14 | 82 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 2110 | 40 |
| gliner2-hivetrace-omni-ru | 23192 | 50.54 | - | 12 | 58 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 3343 | 16 |
| gliner-nvidia+sent300 | 21204 | 6.12 | - | 131 | 429 | NVIDIA GeForce RTX 5090 | - | 4 | - | sent300 | 4260 | 3 |
| gliner2-hivetrace-uni-ru | 19647 | 53.04 | - | 12 | 52 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 2072 | 17 |
| gliner2-fastino-ru | 17889 | 42.35 | - | 16 | 64 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 3342 | 18 |
| gliner-nvidia-ru | 7770 | 18.40 | - | 32 | 167 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 4272 | 18 |
| stanza-ru | 7663 | 13.54 | - | 38 | 276 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 1893 | 40 |
| ru-pii-ner | 4133 | 7.30 | - | 65 | 496 | NVIDIA GeForce RTX 5090 | - | 4 | - | - | 2218 | 40 |
| gravitee-small | 66918 | 163.33 | - | 2 | 28 | NVIDIA GeForce RTX 5090 | - | 8 | - | - | 1218 | 12 |
| opf-ru-v2+ov100 | 74698 | 42.24 | - | 16 | 74 | NVIDIA H200 NVL | - | 1 | - | ov100 | 3812 | 4 |
| opf-ru-v2+sent300 | 52422 | 26.83 | - | 25 | 120 | NVIDIA H200 NVL | - | 1 | - | sent300 | 3816 | 8 |
| opf-ru-v2+homoglyph | 43329 | 79.74 | - | 8 | 36 | NVIDIA H200 NVL | - | 1 | - | homoglyph | 4161 | 2 |
| opf-ru-v2+ov100 | 662 | 0.67 | - | 574 | 5185 | NVIDIA H200 NVL | - | 24 | - | ov100 | 3810 | 7 |
| opf-ru-v2+sent300 | 335 | 1.05 | - | 528 | 3150 | NVIDIA H200 NVL | - | 24 | - | sent300 | 3809 | 3 |
| gliner2-hivetrace-omni-ru | 71039 | 294.12 | - | 3 | 3 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 1 | - | - | 3238 | 1 |
| gliner25-fastino+nochunk | 37505 | 19.38 | - | 32 | 154 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 1 | - | nochunk | 2920 | 3 |
| gliner25-fastino-ru+nochunk | 33041 | 14.89 | - | 45 | 165 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 1 | - | nochunk | 3054 | 4 |
| openmed-multilingual | 10520 | 57.47 | - | 17 | 19 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 1 | - | - | 3777 | 1 |
| openmed-nemotron | 10132 | 55.35 | - | 18 | 19 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 1 | - | - | 3745 | 1 |
| opf-ru | 8829 | 48.23 | - | 20 | 22 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 1 | - | - | 3954 | 1 |
| traciora | 8346 | 45.59 | - | 21 | 23 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 1 | - | - | 3806 | 1 |
| gliner-stream-pii | 7763 | 189.79 | - | 5 | 5 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 1 | - | - | 4859 | 1 |
| openai-base | 5805 | 31.71 | - | 31 | 32 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 1 | - | - | 3806 | 1 |
| opf-ru-v2 | 2286 | 55.89 | - | 17 | 19 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 1 | - | - | 4196 | 1 |
| gliner2-hivetrace-omni-ru | 31086 | 238.10 | - | 4 | 4 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 10 | - | - | 3232 | 1 |
| gliner-stream-pii | 8919 | 17.07 | - | 38 | 188 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 10 | - | - | 4862 | 29 |
| openmed-multilingual | 2176 | 6.89 | - | 134 | 294 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 10 | - | - | 3807 | 8 |
| openmed-nemotron | 2102 | 6.66 | - | 139 | 302 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 10 | - | - | 3807 | 8 |
| opf-ru | 1736 | 5.50 | - | 156 | 370 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 10 | - | - | 3805 | 8 |
| traciora | 1481 | 2.68 | - | 250 | 1079 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 10 | - | - | 3806 | 29 |
| openai-base | 1174 | 3.72 | - | 254 | 550 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 10 | - | - | 3805 | 8 |
| opf-ru-v2 | 1101 | 2.92 | - | 242 | 863 | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | - | 10 | - | - | 3807 | 18 |
| opf-ru-v2 | 35703 | 20.76 | - | 27 | 131 | NVIDIA RTX PRO 6000 Blackwell Server Edition | - | 1 | - | - | 4144 | 2 |
| opf-ru-v2 | 870 | 1.51 | - | 469 | 975 | NVIDIA RTX PRO 6000 Blackwell Server Edition | - | 16 | - | - | 3797 | 2 |
| opf-ru-v2+homoglyph | 1419 | 15.62 | - | 64 | 79 | NVIDIA RTX PRO 6000 Blackwell Server Edition | - | 20 | - | homoglyph | 3793 | 1 |
| opf-ru-v2 | 970 | 1.56 | - | 438 | 1928 | NVIDIA RTX PRO 6000 Blackwell Server Edition | - | 20 | - | - | 3804 | 18 |
| gliner25-fastino+nochunk | 28048 | 35.93 | - | 7 | 141 | NVIDIA RTX PRO 6000 Blackwell Workstation Edition | - | 1 | - | nochunk | 3219 | 1 |
| gliner-pii-edge | 2550 | 1.05 | - | 563 | 3200 | NVIDIA RTX PRO 6000 Blackwell Workstation Edition | - | 1 | - | - | 1702 | 1 |
| gliner25-fastino+nochunk | 14889 | 6.23 | - | 114 | 496 | NVIDIA RTX PRO 6000 Blackwell Workstation Edition | - | 8 | - | nochunk | 3222 | 1 |
| gliner-pii-edge | 1435 | 2.19 | - | 96 | 1822 | NVIDIA RTX PRO 6000 Blackwell Workstation Edition | - | 8 | - | - | 1920 | 33 |

