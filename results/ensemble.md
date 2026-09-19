# Ensembles

Computed over the saved predictions: union of characters, or a k-of-N vote. Main metric - missed spans, a gold span no character of the composition touched. The unit of counting is the gold span of `score.py`, so the numbers match the per-set reports. `-` means one of the members has no run on that set; `train` means one of them was trained on the source of the set (its slices and corrupted copies count), so the composition is not scored there.

## Missed spans, % of the gold spans of the set

| composition | alexen2 | alrosait | ameau01 | arthur-passwords | corrupt-hivetrace | corrupt-redmadrobot | corrupt-secrets-issues | creddata | dialogpii-en | dialogpii-multi | factrueval | gretel-multi | hivetrace | jayguard | kiji-en | kiji-multi | leak-museum | leaky-repo | multiconer-ru | nemotron-pii | nerel | nym-en | nym-multi | nym-ru | privy | redact-multi | redact-ru | redmadrobot | rubai-ru | russian-pii-66k | scanpatch | secrets-issues | secrets-rules | synth-env-configs | synth-jira-comments | synth-ru-tickets | synth-secrets-en | synth-secrets-ru | synth-wiki-tables | tab-echr | tonicai |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gitleaks | - | 100.0% (1862) | - | - | - | - | - | - | - | - | - | - | 99.0% (1650) | 100.0% (1195) | - | - | - | 76.8% (73) | - | - | - | - | - | 100.0% (9497) | - | - | - | 100.0% (5516) | - | 100.0% (4805) | 100.0% (8708) | 45.1% (130) | train | - | - | - | - | - | - | - | - |
| pplx | 5.2% (66) | 0.5% (10) | 17.5% (393) | 0.0% (0) | 3.5% (58) | 13.5% (748) | 4.2% (12) | 5.8% (45) | 24.1% (744) | 29.2% (3017) | 87.4% (6964) | 18.2% (818) | 2.7% (45) | 16.5% (197) | 4.1% (310) | 4.2% (318) | 16.8% (17) | 7.4% (7) | 80.7% (975) | 12.2% (1149) | 87.3% (21282) | 3.9% (138) | 2.8% (227) | 3.9% (374) | 5.1% (96) | 10.6% (2427) | 9.5% (881) | 14.1% (775) | 0.5% (16) | 0.2% (11) | 12.4% (1084) | 4.2% (12) | 3.9% (29) | 0.0% (0) | 0.1% (2) | 2.6% (849) | 0.2% (1) | 0.0% (0) | 5.6% (734) | 60.4% (2314) | 20.8% (502) |
| gitleaks+pplx | - | 0.5% (10) | - | - | - | - | - | - | - | - | - | - | 2.7% (45) | 16.5% (197) | - | - | - | 7.4% (7) | - | - | - | - | - | 3.9% (374) | - | - | - | 14.1% (775) | - | 0.2% (11) | 12.4% (1084) | 2.4% (7) | train | - | - | - | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | 0.1% (2) | - | - | - | - | - | - | - | - | - | - | 0.7% (12) | 9.5% (113) | - | - | - | 2.1% (2) | - | train | - | - | - | 0.6% (53) | - | - | - | 2.4% (134) | - | 0.0% (0) | 4.6% (401) | 1.7% (5) | train | - | - | - | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | 0.1% (1) | - | - | - | - | - | - | - | - | - | - | 0.7% (12) | 7.6% (91) | - | - | - | 1.1% (1) | - | train | - | - | - | 0.2% (16) | - | - | - | 1.0% (54) | - | 0.0% (0) | 2.3% (199) | 1.0% (3) | train | - | - | - | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | 0.1% (1) | - | - | - | - | - | - | - | - | - | - | 0.4% (6) | 9.0% (108) | - | - | - | 1.1% (1) | - | train | - | - | - | 0.2% (22) | - | - | - | 2.1% (115) | - | 0.0% (0) | 3.9% (340) | 1.0% (3) | train | - | - | - | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | 0.0% (0) | - | - | - | - | - | - | - | - | - | - | 0.4% (6) | 7.4% (89) | - | - | - | 1.1% (1) | - | train | - | - | - | 0.2% (15) | - | - | - | 0.9% (48) | - | 0.0% (0) | 2.0% (177) | 1.0% (3) | train | - | - | - | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | 0.2% (3) | - | - | - | - | - | - | - | - | - | - | 1.1% (19) | 9.0% (108) | - | - | - | 3.2% (3) | - | - | - | - | - | 0.5% (44) | - | - | - | 5.3% (293) | - | 0.0% (1) | 5.1% (443) | 1.0% (3) | train | - | - | - | - | - | - | - | - |
| fastino | 0.2% (3) | 12.2% (228) | 7.1% (160) | 17.5% (49) | 30.3% (505) | 30.6% (1692) | 35.4% (102) | 14.3% (111) | 10.1% (313) | 22.1% (2286) | 17.1% (1362) | 17.3% (777) | 27.1% (451) | 10.5% (126) | 3.2% (245) | 4.2% (319) | 19.8% (20) | 17.9% (17) | 7.9% (95) | 7.5% (703) | 10.5% (2554) | 15.6% (560) | 24.6% (2007) | 18.8% (1790) | 20.1% (381) | 15.5% (3535) | 14.4% (1325) | 22.3% (1230) | 30.6% (1059) | 5.1% (243) | 18.8% (1638) | 34.7% (100) | 4.6% (34) | 46.2% (181) | 13.7% (371) | 4.1% (1312) | 35.5% (206) | 35.1% (204) | 11.8% (1549) | 1.6% (60) | 4.5% (108) |
| pplx+fastino | 0.1% (1) | 0.1% (2) | 3.3% (74) | 0.0% (0) | 1.3% (22) | 4.3% (238) | 2.8% (8) | 1.7% (13) | 5.8% (180) | 11.4% (1180) | 14.2% (1131) | 10.9% (488) | 0.7% (11) | 7.6% (91) | 0.4% (29) | 0.4% (32) | 2.0% (2) | 1.1% (1) | 7.2% (87) | 0.9% (87) | 9.7% (2352) | 0.8% (27) | 0.9% (76) | 0.3% (24) | 0.9% (18) | 3.0% (685) | 2.6% (240) | 2.8% (153) | 0.3% (12) | 0.0% (2) | 4.1% (354) | 2.4% (7) | 0.7% (5) | 0.0% (0) | 0.1% (2) | 0.1% (31) | 0.2% (1) | 0.0% (0) | 0.7% (87) | 1.4% (53) | 2.7% (66) |
| pplx+fastino+mmbert | 0.1% (1) | 0.1% (1) | 1.1% (25) | 0.0% (0) | 0.5% (8) | 2.1% (116) | 1.4% (4) | 0.1% (1) | 5.3% (163) | 8.2% (845) | 5.8% (459) | 10.4% (465) | 0.3% (5) | 7.1% (85) | 0.1% (9) | 0.3% (25) | 2.0% (2) | 1.1% (1) | 5.8% (70) | 0.2% (23) | 6.3% (1533) | 0.4% (15) | 0.3% (26) | 0.1% (10) | 0.5% (10) | 1.5% (341) | 1.6% (150) | 1.1% (61) | 0.3% (9) | 0.0% (0) | 1.4% (125) | 2.1% (6) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (10) | 0.0% (0) | 0.0% (0) | 0.3% (37) | 1.1% (43) | 2.6% (62) |
| pplx+fastino+bardsai | 0.1% (1) | 0.1% (1) | 1.7% (38) | 0.0% (0) | 1.0% (17) | 3.1% (169) | 0.3% (1) | 0.8% (6) | 4.8% (148) | 8.7% (895) | 1.5% (121) | 10.1% (451) | 0.4% (6) | 7.2% (86) | 0.1% (11) | 0.3% (23) | 2.0% (2) | 1.1% (1) | 6.8% (82) | 0.5% (46) | 3.7% (909) | 0.3% (12) | 0.5% (39) | 0.1% (5) | 0.9% (17) | 1.9% (444) | 1.9% (179) | 1.5% (82) | 0.2% (8) | 0.0% (0) | 3.0% (261) | 0.3% (1) | 0.3% (2) | 0.0% (0) | 0.1% (2) | 0.0% (6) | 0.0% (0) | 0.0% (0) | 0.6% (77) | 1.2% (47) | 2.6% (62) |
| pplx+fastino+bardsai+mmbert | 0.1% (1) | 0.1% (1) | 0.4% (9) | 0.0% (0) | 0.5% (8) | 1.6% (89) | 0.0% (0) | 0.1% (1) | 4.5% (139) | 6.6% (687) | 1.4% (108) | 9.8% (440) | 0.3% (5) | 7.0% (84) | 0.1% (7) | 0.3% (22) | 2.0% (2) | 1.1% (1) | 5.6% (68) | 0.1% (14) | 3.5% (843) | 0.2% (8) | 0.3% (21) | 0.0% (2) | 0.5% (10) | 1.3% (289) | 1.4% (127) | 0.8% (44) | 0.2% (8) | 0.0% (0) | 0.9% (82) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (3) | 0.0% (0) | 0.0% (0) | 0.3% (35) | 1.0% (37) | 2.4% (59) |
| vote2(pplx,opf2,nvidia) | 2.2% (28) | 0.9% (17) | 25.1% (563) | 0.0% (0) | 6.4% (106) | 24.7% (1368) | 5.9% (17) | 3.6% (28) | 27.4% (846) | 39.0% (4036) | 73.8% (5879) | 19.4% (871) | 2.5% (41) | 22.1% (264) | 4.8% (363) | 5.8% (437) | 23.8% (24) | 10.5% (10) | 84.7% (1023) | train | 79.6% (19408) | 8.8% (315) | 11.8% (962) | 7.7% (727) | 12.7% (242) | 16.9% (3854) | 12.8% (1186) | 19.0% (1050) | 1.1% (39) | 0.3% (16) | 19.7% (1716) | 4.2% (12) | 2.9% (22) | 2.0% (8) | 5.8% (157) | 26.9% (8620) | 2.4% (14) | 1.9% (11) | 15.4% (2019) | 63.9% (2446) | 21.0% (507) |
| vote2(gitleaks,pplx,opf2,nvidia) | - | 0.9% (17) | - | - | - | - | - | - | - | - | - | - | 2.5% (41) | 22.1% (264) | - | - | - | 10.5% (10) | - | train | - | - | - | 7.7% (727) | - | - | - | 19.0% (1050) | - | 0.3% (16) | 19.7% (1716) | 2.4% (7) | train | - | - | - | - | - | - | - | - |

## char F1, reference

| composition | alexen2 | alrosait | ameau01 | arthur-passwords | corrupt-hivetrace | corrupt-redmadrobot | corrupt-secrets-issues | creddata | dialogpii-en | dialogpii-multi | factrueval | gretel-multi | hivetrace | jayguard | kiji-en | kiji-multi | leak-museum | leaky-repo | multiconer-ru | nemotron-pii | nerel | nym-en | nym-multi | nym-ru | privy | redact-multi | redact-ru | redmadrobot | rubai-ru | russian-pii-66k | scanpatch | secrets-issues | secrets-rules | synth-env-configs | synth-jira-comments | synth-ru-tickets | synth-secrets-en | synth-secrets-ru | synth-wiki-tables | tab-echr | tonicai |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gitleaks | - | 0.000 | - | - | - | - | - | - | - | - | - | - | 0.175 | 0.000 | - | - | - | 0.705 | - | - | - | - | - | 0.000 | - | - | - | 0.000 | - | 0.000 | 0.000 | 0.538 | train | - | - | - | - | - | - | - | - |
| pplx | 0.905 | 0.938 | 0.688 | 0.295 | 0.904 | 0.787 | 0.306 | 0.782 | 0.761 | 0.679 | 0.188 | 0.720 | 0.915 | 0.555 | 0.863 | 0.865 | 0.604 | 0.713 | 0.240 | 0.829 | 0.241 | 0.927 | 0.933 | 0.911 | 0.419 | 0.705 | 0.709 | 0.800 | 0.941 | 0.955 | 0.862 | 0.288 | 0.753 | 0.418 | 0.818 | 0.833 | 0.330 | 0.328 | 0.944 | 0.306 | 0.848 |
| gitleaks+pplx | - | 0.938 | - | - | - | - | - | - | - | - | - | - | 0.915 | 0.555 | - | - | - | 0.797 | - | - | - | - | - | 0.911 | - | - | - | 0.800 | - | 0.955 | 0.862 | 0.292 | train | - | - | - | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | 0.886 | - | - | - | - | - | - | - | - | - | - | 0.826 | 0.555 | - | - | - | 0.795 | - | train | - | - | - | 0.924 | - | - | - | 0.825 | - | 0.945 | 0.874 | 0.275 | train | - | - | - | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | 0.867 | - | - | - | - | - | - | - | - | - | - | 0.820 | 0.472 | - | - | - | 0.709 | - | train | - | - | - | 0.904 | - | - | - | 0.702 | - | 0.942 | 0.865 | 0.219 | train | - | - | - | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | 0.876 | - | - | - | - | - | - | - | - | - | - | 0.821 | 0.529 | - | - | - | 0.825 | - | train | - | - | - | 0.911 | - | - | - | 0.814 | - | 0.937 | 0.872 | 0.265 | train | - | - | - | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | 0.858 | - | - | - | - | - | - | - | - | - | - | 0.815 | 0.459 | - | - | - | 0.711 | - | train | - | - | - | 0.892 | - | - | - | 0.697 | - | 0.935 | 0.862 | 0.217 | train | - | - | - | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | 0.909 | - | - | - | - | - | - | - | - | - | - | 0.909 | 0.480 | - | - | - | 0.715 | - | - | - | - | - | 0.912 | - | - | - | 0.700 | - | 0.952 | 0.874 | 0.228 | train | - | - | - | - | - | - | - | - |
| fastino | 0.969 | 0.757 | 0.765 | 0.750 | 0.692 | 0.721 | 0.332 | 0.573 | 0.602 | 0.538 | 0.758 | 0.765 | 0.732 | 0.585 | 0.878 | 0.871 | 0.414 | 0.510 | 0.646 | 0.866 | 0.831 | 0.876 | 0.826 | 0.871 | 0.630 | 0.694 | 0.685 | 0.797 | 0.633 | 0.965 | 0.781 | 0.352 | 0.684 | 0.287 | 0.801 | 0.917 | 0.466 | 0.475 | 0.898 | 0.635 | 0.885 |
| pplx+fastino | 0.921 | 0.872 | 0.703 | 0.292 | 0.894 | 0.821 | 0.251 | 0.724 | 0.613 | 0.573 | 0.767 | 0.714 | 0.906 | 0.511 | 0.861 | 0.856 | 0.408 | 0.638 | 0.638 | 0.882 | 0.825 | 0.919 | 0.935 | 0.930 | 0.413 | 0.690 | 0.691 | 0.845 | 0.928 | 0.957 | 0.891 | 0.253 | 0.677 | 0.375 | 0.814 | 0.835 | 0.327 | 0.325 | 0.981 | 0.552 | 0.855 |
| pplx+fastino+mmbert | 0.919 | 0.869 | 0.667 | 0.276 | 0.846 | 0.764 | 0.217 | 0.694 | 0.584 | 0.526 | 0.786 | 0.662 | 0.903 | 0.477 | 0.858 | 0.826 | 0.388 | 0.622 | 0.624 | 0.870 | 0.808 | 0.906 | 0.882 | 0.927 | 0.401 | 0.629 | 0.660 | 0.822 | 0.923 | 0.953 | 0.897 | 0.215 | 0.623 | 0.340 | 0.800 | 0.803 | 0.300 | 0.299 | 0.979 | 0.540 | 0.848 |
| pplx+fastino+bardsai | 0.917 | 0.864 | 0.653 | 0.274 | 0.886 | 0.793 | 0.231 | 0.750 | 0.603 | 0.569 | 0.757 | 0.674 | 0.893 | 0.462 | 0.840 | 0.835 | 0.400 | 0.694 | 0.626 | 0.850 | 0.791 | 0.893 | 0.923 | 0.919 | 0.408 | 0.673 | 0.676 | 0.806 | 0.920 | 0.950 | 0.889 | 0.233 | 0.665 | 0.347 | 0.813 | 0.821 | 0.317 | 0.315 | 0.910 | 0.543 | 0.835 |
| pplx+fastino+bardsai+mmbert | 0.916 | 0.862 | 0.627 | 0.262 | 0.838 | 0.743 | 0.207 | 0.715 | 0.576 | 0.523 | 0.744 | 0.633 | 0.890 | 0.441 | 0.838 | 0.809 | 0.380 | 0.666 | 0.613 | 0.840 | 0.770 | 0.882 | 0.873 | 0.917 | 0.396 | 0.619 | 0.649 | 0.790 | 0.918 | 0.947 | 0.893 | 0.206 | 0.619 | 0.335 | 0.799 | 0.794 | 0.298 | 0.297 | 0.909 | 0.533 | 0.829 |
| vote2(pplx,opf2,nvidia) | 0.966 | 0.947 | 0.680 | 0.394 | 0.926 | 0.747 | 0.453 | 0.857 | 0.740 | 0.638 | 0.370 | 0.777 | 0.961 | 0.598 | 0.880 | 0.884 | 0.659 | 0.791 | 0.197 | train | 0.345 | 0.923 | 0.909 | 0.923 | 0.474 | 0.715 | 0.739 | 0.800 | 0.952 | 0.961 | 0.799 | 0.451 | 0.754 | 0.451 | 0.935 | 0.696 | 0.395 | 0.397 | 0.814 | 0.390 | 0.887 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | 0.947 | - | - | - | - | - | - | - | - | - | - | 0.961 | 0.598 | - | - | - | 0.877 | - | train | - | - | - | 0.923 | - | - | - | 0.800 | - | 0.961 | 0.799 | 0.431 | train | - | - | - | - | - | - | - | - |

## Precision / recall / rows without annotations

`Rows touched` counts rows the source left without annotations where a composition masked something. It is not a false-alarm rate: the absence of annotations is not evidence that these rows hold nothing sensitive. The exact CSV keeps the technical column name `fp_rows` for the same count.

### alexen2

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 66 (5.2%) | 0.876 | 0.937 | 0.905 | 7/40 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 3 (0.2%) | 0.989 | 0.949 | 0.969 | 14/40 |
| pplx+fastino | 1 (0.1%) | 0.873 | 0.975 | 0.921 | 19/40 |
| pplx+fastino+mmbert | 1 (0.1%) | 0.869 | 0.975 | 0.919 | 25/40 |
| pplx+fastino+bardsai | 1 (0.1%) | 0.865 | 0.977 | 0.917 | 23/40 |
| pplx+fastino+bardsai+mmbert | 1 (0.1%) | 0.862 | 0.977 | 0.916 | 25/40 |
| vote2(pplx,opf2,nvidia) | 28 (2.2%) | 0.991 | 0.943 | 0.966 | 8/40 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### alrosait

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | 1862 (100.0%) | 0.000 | 0.000 | 0.000 | 0/340 |
| pplx | 10 (0.5%) | 0.889 | 0.992 | 0.938 | 122/340 |
| gitleaks+pplx | 10 (0.5%) | 0.889 | 0.992 | 0.938 | 122/340 |
| gitleaks+pplx+nvidia | 2 (0.1%) | 0.799 | 0.995 | 0.886 | 262/340 |
| gitleaks+pplx+nvidia+legal | 1 (0.1%) | 0.766 | 0.998 | 0.867 | 280/340 |
| gitleaks+pplx+opf2+nvidia | 1 (0.1%) | 0.780 | 0.998 | 0.876 | 275/340 |
| gitleaks+pplx+opf2+nvidia+legal | 0 (0.0%) | 0.751 | 0.999 | 0.858 | 285/340 |
| gitleaks+pplx+legal+vladlinv | 3 (0.2%) | 0.835 | 0.998 | 0.909 | 199/340 |
| fastino | 228 (12.2%) | 0.785 | 0.732 | 0.757 | 278/340 |
| pplx+fastino | 2 (0.1%) | 0.776 | 0.997 | 0.872 | 297/340 |
| pplx+fastino+mmbert | 1 (0.1%) | 0.770 | 0.997 | 0.869 | 308/340 |
| pplx+fastino+bardsai | 1 (0.1%) | 0.762 | 0.997 | 0.864 | 309/340 |
| pplx+fastino+bardsai+mmbert | 1 (0.1%) | 0.759 | 0.998 | 0.862 | 309/340 |
| vote2(pplx,opf2,nvidia) | 17 (0.9%) | 0.934 | 0.960 | 0.947 | 105/340 |
| vote2(gitleaks,pplx,opf2,nvidia) | 17 (0.9%) | 0.934 | 0.960 | 0.947 | 105/340 |

### ameau01

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 393 (17.5%) | 0.612 | 0.785 | 0.688 | 173/702 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 160 (7.1%) | 0.661 | 0.909 | 0.765 | 241/702 |
| pplx+fastino | 74 (3.3%) | 0.556 | 0.955 | 0.703 | 299/702 |
| pplx+fastino+mmbert | 25 (1.1%) | 0.506 | 0.979 | 0.667 | 391/702 |
| pplx+fastino+bardsai | 38 (1.7%) | 0.492 | 0.972 | 0.653 | 397/702 |
| pplx+fastino+bardsai+mmbert | 9 (0.4%) | 0.459 | 0.987 | 0.627 | 455/702 |
| vote2(pplx,opf2,nvidia) | 563 (25.1%) | 0.691 | 0.670 | 0.680 | 150/702 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### arthur-passwords

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 0 (0.0%) | 0.173 | 1.000 | 0.295 | 227/236 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 49 (17.5%) | 0.687 | 0.825 | 0.750 | 55/236 |
| pplx+fastino | 0 (0.0%) | 0.171 | 1.000 | 0.292 | 228/236 |
| pplx+fastino+mmbert | 0 (0.0%) | 0.160 | 1.000 | 0.276 | 235/236 |
| pplx+fastino+bardsai | 0 (0.0%) | 0.158 | 1.000 | 0.274 | 232/236 |
| pplx+fastino+bardsai+mmbert | 0 (0.0%) | 0.151 | 1.000 | 0.262 | 236/236 |
| vote2(pplx,opf2,nvidia) | 0 (0.0%) | 0.245 | 1.000 | 0.394 | 209/236 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### corrupt-hivetrace

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 58 (3.5%) | 0.842 | 0.975 | 0.904 | 51/378 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 505 (30.3%) | 0.923 | 0.553 | 0.692 | 36/378 |
| pplx+fastino | 22 (1.3%) | 0.818 | 0.986 | 0.894 | 81/378 |
| pplx+fastino+mmbert | 8 (0.5%) | 0.737 | 0.993 | 0.846 | 130/378 |
| pplx+fastino+bardsai | 17 (1.0%) | 0.801 | 0.990 | 0.886 | 86/378 |
| pplx+fastino+bardsai+mmbert | 8 (0.5%) | 0.725 | 0.994 | 0.838 | 133/378 |
| vote2(pplx,opf2,nvidia) | 106 (6.4%) | 0.934 | 0.919 | 0.926 | 32/378 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### corrupt-redmadrobot

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 748 (13.5%) | 0.787 | 0.787 | 0.787 | 170/371 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 1692 (30.6%) | 0.871 | 0.615 | 0.721 | 117/371 |
| pplx+fastino | 238 (4.3%) | 0.765 | 0.886 | 0.821 | 223/371 |
| pplx+fastino+mmbert | 116 (2.1%) | 0.657 | 0.915 | 0.764 | 301/371 |
| pplx+fastino+bardsai | 169 (3.1%) | 0.707 | 0.903 | 0.793 | 244/371 |
| pplx+fastino+bardsai+mmbert | 89 (1.6%) | 0.621 | 0.924 | 0.743 | 308/371 |
| vote2(pplx,opf2,nvidia) | 1368 (24.7%) | 0.882 | 0.647 | 0.747 | 105/371 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### corrupt-secrets-issues

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 12 (4.2%) | 0.183 | 0.943 | 0.306 | 202/250 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 102 (35.4%) | 0.223 | 0.650 | 0.332 | 219/250 |
| pplx+fastino | 8 (2.8%) | 0.145 | 0.949 | 0.251 | 245/250 |
| pplx+fastino+mmbert | 4 (1.4%) | 0.122 | 0.957 | 0.217 | 250/250 |
| pplx+fastino+bardsai | 1 (0.3%) | 0.131 | 0.963 | 0.231 | 248/250 |
| pplx+fastino+bardsai+mmbert | 0 (0.0%) | 0.116 | 0.964 | 0.207 | 250/250 |
| vote2(pplx,opf2,nvidia) | 17 (5.9%) | 0.301 | 0.914 | 0.453 | 155/250 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### creddata

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 45 (5.8%) | 0.747 | 0.821 | 0.782 | 169/727 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 111 (14.3%) | 0.617 | 0.534 | 0.573 | 566/727 |
| pplx+fastino | 13 (1.7%) | 0.620 | 0.871 | 0.724 | 596/727 |
| pplx+fastino+mmbert | 1 (0.1%) | 0.566 | 0.896 | 0.694 | 627/727 |
| pplx+fastino+bardsai | 6 (0.8%) | 0.615 | 0.960 | 0.750 | 598/727 |
| pplx+fastino+bardsai+mmbert | 1 (0.1%) | 0.569 | 0.963 | 0.715 | 628/727 |
| vote2(pplx,opf2,nvidia) | 28 (3.6%) | 0.881 | 0.835 | 0.857 | 129/727 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### dialogpii-en

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 744 (24.1%) | 0.822 | 0.708 | 0.761 | 1/1 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 313 (10.1%) | 0.462 | 0.866 | 0.602 | 1/1 |
| pplx+fastino | 180 (5.8%) | 0.456 | 0.934 | 0.613 | 1/1 |
| pplx+fastino+mmbert | 163 (5.3%) | 0.425 | 0.937 | 0.584 | 1/1 |
| pplx+fastino+bardsai | 148 (4.8%) | 0.444 | 0.943 | 0.603 | 1/1 |
| pplx+fastino+bardsai+mmbert | 139 (4.5%) | 0.414 | 0.944 | 0.576 | 1/1 |
| vote2(pplx,opf2,nvidia) | 846 (27.4%) | 0.849 | 0.656 | 0.740 | 1/1 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### dialogpii-multi

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 3017 (29.2%) | 0.789 | 0.595 | 0.679 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 2286 (22.1%) | 0.431 | 0.714 | 0.538 | no negatives |
| pplx+fastino | 1180 (11.4%) | 0.438 | 0.827 | 0.573 | no negatives |
| pplx+fastino+mmbert | 845 (8.2%) | 0.380 | 0.853 | 0.526 | no negatives |
| pplx+fastino+bardsai | 895 (8.7%) | 0.427 | 0.857 | 0.569 | no negatives |
| pplx+fastino+bardsai+mmbert | 687 (6.6%) | 0.373 | 0.873 | 0.523 | no negatives |
| vote2(pplx,opf2,nvidia) | 4036 (39.0%) | 0.898 | 0.495 | 0.638 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### factrueval

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 6964 (87.4%) | 0.879 | 0.105 | 0.188 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 1362 (17.1%) | 0.699 | 0.828 | 0.758 | no negatives |
| pplx+fastino | 1131 (14.2%) | 0.697 | 0.852 | 0.767 | no negatives |
| pplx+fastino+mmbert | 459 (5.8%) | 0.682 | 0.926 | 0.786 | no negatives |
| pplx+fastino+bardsai | 121 (1.5%) | 0.620 | 0.972 | 0.757 | no negatives |
| pplx+fastino+bardsai+mmbert | 108 (1.4%) | 0.602 | 0.973 | 0.744 | no negatives |
| vote2(pplx,opf2,nvidia) | 5879 (73.8%) | 0.968 | 0.229 | 0.370 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### gretel-multi

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 818 (18.2%) | 0.622 | 0.854 | 0.720 | 12/18 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 777 (17.3%) | 0.753 | 0.778 | 0.765 | 13/18 |
| pplx+fastino | 488 (10.9%) | 0.582 | 0.924 | 0.714 | 17/18 |
| pplx+fastino+mmbert | 465 (10.4%) | 0.514 | 0.927 | 0.662 | 17/18 |
| pplx+fastino+bardsai | 451 (10.1%) | 0.529 | 0.930 | 0.674 | 17/18 |
| pplx+fastino+bardsai+mmbert | 440 (9.8%) | 0.479 | 0.933 | 0.633 | 17/18 |
| vote2(pplx,opf2,nvidia) | 871 (19.4%) | 0.749 | 0.807 | 0.777 | 10/18 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### hivetrace

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | 1650 (99.0%) | 1.000 | 0.096 | 0.175 | 0/378 |
| pplx | 45 (2.7%) | 0.860 | 0.979 | 0.915 | 33/378 |
| gitleaks+pplx | 45 (2.7%) | 0.860 | 0.979 | 0.915 | 33/378 |
| gitleaks+pplx+nvidia | 12 (0.7%) | 0.706 | 0.995 | 0.826 | 126/378 |
| gitleaks+pplx+nvidia+legal | 12 (0.7%) | 0.696 | 0.999 | 0.820 | 129/378 |
| gitleaks+pplx+opf2+nvidia | 6 (0.4%) | 0.698 | 0.996 | 0.821 | 131/378 |
| gitleaks+pplx+opf2+nvidia+legal | 6 (0.4%) | 0.688 | 0.999 | 0.815 | 134/378 |
| gitleaks+pplx+legal+vladlinv | 19 (1.1%) | 0.835 | 0.997 | 0.909 | 54/378 |
| fastino | 451 (27.1%) | 0.927 | 0.605 | 0.732 | 46/378 |
| pplx+fastino | 11 (0.7%) | 0.834 | 0.993 | 0.906 | 73/378 |
| pplx+fastino+mmbert | 5 (0.3%) | 0.826 | 0.995 | 0.903 | 84/378 |
| pplx+fastino+bardsai | 6 (0.4%) | 0.810 | 0.994 | 0.893 | 78/378 |
| pplx+fastino+bardsai+mmbert | 5 (0.3%) | 0.806 | 0.995 | 0.890 | 87/378 |
| vote2(pplx,opf2,nvidia) | 41 (2.5%) | 0.942 | 0.980 | 0.961 | 20/378 |
| vote2(gitleaks,pplx,opf2,nvidia) | 41 (2.5%) | 0.942 | 0.980 | 0.961 | 20/378 |

### jayguard

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | 1195 (100.0%) | 0.000 | 0.000 | 0.000 | 0/170 |
| pplx | 197 (16.5%) | 0.412 | 0.853 | 0.555 | 87/170 |
| gitleaks+pplx | 197 (16.5%) | 0.412 | 0.853 | 0.555 | 87/170 |
| gitleaks+pplx+nvidia | 113 (9.5%) | 0.398 | 0.920 | 0.555 | 126/170 |
| gitleaks+pplx+nvidia+legal | 91 (7.6%) | 0.316 | 0.935 | 0.472 | 152/170 |
| gitleaks+pplx+opf2+nvidia | 108 (9.0%) | 0.370 | 0.924 | 0.529 | 133/170 |
| gitleaks+pplx+opf2+nvidia+legal | 89 (7.4%) | 0.304 | 0.938 | 0.459 | 153/170 |
| gitleaks+pplx+legal+vladlinv | 108 (9.0%) | 0.325 | 0.924 | 0.480 | 142/170 |
| fastino | 126 (10.5%) | 0.433 | 0.902 | 0.585 | 116/170 |
| pplx+fastino | 91 (7.6%) | 0.350 | 0.941 | 0.511 | 132/170 |
| pplx+fastino+mmbert | 85 (7.1%) | 0.319 | 0.945 | 0.477 | 157/170 |
| pplx+fastino+bardsai | 86 (7.2%) | 0.306 | 0.945 | 0.462 | 139/170 |
| pplx+fastino+bardsai+mmbert | 84 (7.0%) | 0.287 | 0.947 | 0.441 | 158/170 |
| vote2(pplx,opf2,nvidia) | 264 (22.1%) | 0.477 | 0.800 | 0.598 | 73/170 |
| vote2(gitleaks,pplx,opf2,nvidia) | 264 (22.1%) | 0.477 | 0.800 | 0.598 | 73/170 |

### kiji-en

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 310 (4.1%) | 0.801 | 0.935 | 0.863 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 245 (3.2%) | 0.821 | 0.943 | 0.878 | no negatives |
| pplx+fastino | 29 (0.4%) | 0.759 | 0.993 | 0.861 | no negatives |
| pplx+fastino+mmbert | 9 (0.1%) | 0.752 | 0.998 | 0.858 | no negatives |
| pplx+fastino+bardsai | 11 (0.1%) | 0.726 | 0.996 | 0.840 | no negatives |
| pplx+fastino+bardsai+mmbert | 7 (0.1%) | 0.722 | 0.998 | 0.838 | no negatives |
| vote2(pplx,opf2,nvidia) | 363 (4.8%) | 0.841 | 0.922 | 0.880 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### kiji-multi

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 318 (4.2%) | 0.792 | 0.952 | 0.865 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 319 (4.2%) | 0.814 | 0.936 | 0.871 | no negatives |
| pplx+fastino | 32 (0.4%) | 0.750 | 0.995 | 0.856 | no negatives |
| pplx+fastino+mmbert | 25 (0.3%) | 0.705 | 0.997 | 0.826 | no negatives |
| pplx+fastino+bardsai | 23 (0.3%) | 0.718 | 0.997 | 0.835 | no negatives |
| pplx+fastino+bardsai+mmbert | 22 (0.3%) | 0.681 | 0.997 | 0.809 | no negatives |
| vote2(pplx,opf2,nvidia) | 437 (5.8%) | 0.841 | 0.933 | 0.884 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### leak-museum

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 17 (16.8%) | 0.501 | 0.760 | 0.604 | 10/45 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 20 (19.8%) | 0.284 | 0.766 | 0.414 | 39/45 |
| pplx+fastino | 2 (2.0%) | 0.263 | 0.906 | 0.408 | 42/45 |
| pplx+fastino+mmbert | 2 (2.0%) | 0.246 | 0.908 | 0.388 | 43/45 |
| pplx+fastino+bardsai | 2 (2.0%) | 0.256 | 0.906 | 0.400 | 42/45 |
| pplx+fastino+bardsai+mmbert | 2 (2.0%) | 0.241 | 0.908 | 0.380 | 43/45 |
| vote2(pplx,opf2,nvidia) | 24 (23.8%) | 0.638 | 0.682 | 0.659 | 5/45 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### leaky-repo

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | 73 (76.8%) | 1.000 | 0.545 | 0.705 | 0/16 |
| pplx | 7 (7.4%) | 0.675 | 0.755 | 0.713 | 11/16 |
| gitleaks+pplx | 7 (7.4%) | 0.713 | 0.904 | 0.797 | 11/16 |
| gitleaks+pplx+nvidia | 2 (2.1%) | 0.700 | 0.919 | 0.795 | 11/16 |
| gitleaks+pplx+nvidia+legal | 1 (1.1%) | 0.555 | 0.983 | 0.709 | 15/16 |
| gitleaks+pplx+opf2+nvidia | 1 (1.1%) | 0.703 | 0.997 | 0.825 | 12/16 |
| gitleaks+pplx+opf2+nvidia+legal | 1 (1.1%) | 0.553 | 0.998 | 0.711 | 15/16 |
| gitleaks+pplx+legal+vladlinv | 3 (3.2%) | 0.563 | 0.979 | 0.715 | 15/16 |
| fastino | 17 (17.9%) | 0.515 | 0.506 | 0.510 | 12/16 |
| pplx+fastino | 1 (1.1%) | 0.511 | 0.848 | 0.638 | 13/16 |
| pplx+fastino+mmbert | 1 (1.1%) | 0.482 | 0.876 | 0.622 | 15/16 |
| pplx+fastino+bardsai | 1 (1.1%) | 0.535 | 0.987 | 0.694 | 13/16 |
| pplx+fastino+bardsai+mmbert | 1 (1.1%) | 0.502 | 0.987 | 0.666 | 15/16 |
| vote2(pplx,opf2,nvidia) | 10 (10.5%) | 0.859 | 0.733 | 0.791 | 2/16 |
| vote2(gitleaks,pplx,opf2,nvidia) | 10 (10.5%) | 0.879 | 0.875 | 0.877 | 2/16 |

### multiconer-ru

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 975 (80.7%) | 0.542 | 0.154 | 0.240 | 51/420 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 95 (7.9%) | 0.526 | 0.838 | 0.646 | 293/420 |
| pplx+fastino | 87 (7.2%) | 0.512 | 0.846 | 0.638 | 297/420 |
| pplx+fastino+mmbert | 70 (5.8%) | 0.489 | 0.861 | 0.624 | 324/420 |
| pplx+fastino+bardsai | 82 (6.8%) | 0.492 | 0.860 | 0.626 | 303/420 |
| pplx+fastino+bardsai+mmbert | 68 (5.6%) | 0.472 | 0.872 | 0.613 | 327/420 |
| vote2(pplx,opf2,nvidia) | 1023 (84.7%) | 0.670 | 0.115 | 0.197 | 26/420 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### nemotron-pii

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 1149 (12.2%) | 0.831 | 0.828 | 0.829 | 5/5 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | train | train | train | train | train |
| gitleaks+pplx+nvidia+legal | train | train | train | train | train |
| gitleaks+pplx+opf2+nvidia | train | train | train | train | train |
| gitleaks+pplx+opf2+nvidia+legal | train | train | train | train | train |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 703 (7.5%) | 0.915 | 0.823 | 0.866 | 2/5 |
| pplx+fastino | 87 (0.9%) | 0.812 | 0.965 | 0.882 | 5/5 |
| pplx+fastino+mmbert | 23 (0.2%) | 0.785 | 0.975 | 0.870 | 5/5 |
| pplx+fastino+bardsai | 46 (0.5%) | 0.757 | 0.969 | 0.850 | 5/5 |
| pplx+fastino+bardsai+mmbert | 14 (0.1%) | 0.738 | 0.976 | 0.840 | 5/5 |
| vote2(pplx,opf2,nvidia) | train | train | train | train | train |
| vote2(gitleaks,pplx,opf2,nvidia) | train | train | train | train | train |

### nerel

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 21282 (87.3%) | 0.837 | 0.141 | 0.241 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 2554 (10.5%) | 0.795 | 0.871 | 0.831 | no negatives |
| pplx+fastino | 2352 (9.7%) | 0.778 | 0.877 | 0.825 | no negatives |
| pplx+fastino+mmbert | 1533 (6.3%) | 0.732 | 0.900 | 0.808 | no negatives |
| pplx+fastino+bardsai | 909 (3.7%) | 0.685 | 0.934 | 0.791 | no negatives |
| pplx+fastino+bardsai+mmbert | 843 (3.5%) | 0.654 | 0.937 | 0.770 | no negatives |
| vote2(pplx,opf2,nvidia) | 19408 (79.6%) | 0.989 | 0.209 | 0.345 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### nym-en

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 138 (3.9%) | 0.903 | 0.952 | 0.927 | 37/149 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 560 (15.6%) | 0.913 | 0.842 | 0.876 | 18/149 |
| pplx+fastino | 27 (0.8%) | 0.860 | 0.988 | 0.919 | 50/149 |
| pplx+fastino+mmbert | 15 (0.4%) | 0.833 | 0.993 | 0.906 | 70/149 |
| pplx+fastino+bardsai | 12 (0.3%) | 0.811 | 0.992 | 0.893 | 51/149 |
| pplx+fastino+bardsai+mmbert | 8 (0.2%) | 0.792 | 0.995 | 0.882 | 71/149 |
| vote2(pplx,opf2,nvidia) | 315 (8.8%) | 0.945 | 0.902 | 0.923 | 19/149 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### nym-multi

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 227 (2.8%) | 0.904 | 0.964 | 0.933 | 5/7 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 2007 (24.6%) | 0.949 | 0.731 | 0.826 | 1/7 |
| pplx+fastino | 76 (0.9%) | 0.888 | 0.988 | 0.935 | 5/7 |
| pplx+fastino+mmbert | 26 (0.3%) | 0.792 | 0.996 | 0.882 | 5/7 |
| pplx+fastino+bardsai | 39 (0.5%) | 0.862 | 0.995 | 0.923 | 5/7 |
| pplx+fastino+bardsai+mmbert | 21 (0.3%) | 0.777 | 0.997 | 0.873 | 5/7 |
| vote2(pplx,opf2,nvidia) | 962 (11.8%) | 0.948 | 0.874 | 0.909 | 2/7 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### nym-ru

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | 9497 (100.0%) | 0.000 | 0.000 | 0.000 | no negatives |
| pplx | 374 (3.9%) | 0.899 | 0.925 | 0.911 | no negatives |
| gitleaks+pplx | 374 (3.9%) | 0.899 | 0.925 | 0.911 | no negatives |
| gitleaks+pplx+nvidia | 53 (0.6%) | 0.874 | 0.979 | 0.924 | no negatives |
| gitleaks+pplx+nvidia+legal | 16 (0.2%) | 0.827 | 0.998 | 0.904 | no negatives |
| gitleaks+pplx+opf2+nvidia | 22 (0.2%) | 0.846 | 0.987 | 0.911 | no negatives |
| gitleaks+pplx+opf2+nvidia+legal | 15 (0.2%) | 0.806 | 0.998 | 0.892 | no negatives |
| gitleaks+pplx+legal+vladlinv | 44 (0.5%) | 0.844 | 0.993 | 0.912 | no negatives |
| fastino | 1790 (18.8%) | 0.956 | 0.800 | 0.871 | no negatives |
| pplx+fastino | 24 (0.3%) | 0.884 | 0.980 | 0.930 | no negatives |
| pplx+fastino+mmbert | 10 (0.1%) | 0.877 | 0.984 | 0.927 | no negatives |
| pplx+fastino+bardsai | 5 (0.1%) | 0.856 | 0.993 | 0.919 | no negatives |
| pplx+fastino+bardsai+mmbert | 2 (0.0%) | 0.851 | 0.994 | 0.917 | no negatives |
| vote2(pplx,opf2,nvidia) | 727 (7.7%) | 0.940 | 0.907 | 0.923 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | 727 (7.7%) | 0.940 | 0.907 | 0.923 | no negatives |

### privy

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 96 (5.1%) | 0.270 | 0.930 | 0.419 | 402/530 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 381 (20.1%) | 0.535 | 0.766 | 0.630 | 272/530 |
| pplx+fastino | 18 (0.9%) | 0.261 | 0.993 | 0.413 | 473/530 |
| pplx+fastino+mmbert | 10 (0.5%) | 0.251 | 0.996 | 0.401 | 484/530 |
| pplx+fastino+bardsai | 17 (0.9%) | 0.257 | 0.993 | 0.408 | 474/530 |
| pplx+fastino+bardsai+mmbert | 10 (0.5%) | 0.247 | 0.996 | 0.396 | 485/530 |
| vote2(pplx,opf2,nvidia) | 242 (12.7%) | 0.326 | 0.870 | 0.474 | 371/530 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### redact-multi

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 2427 (10.6%) | 0.626 | 0.806 | 0.705 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 3535 (15.5%) | 0.686 | 0.701 | 0.694 | no negatives |
| pplx+fastino | 685 (3.0%) | 0.559 | 0.901 | 0.690 | no negatives |
| pplx+fastino+mmbert | 341 (1.5%) | 0.477 | 0.921 | 0.629 | no negatives |
| pplx+fastino+bardsai | 444 (1.9%) | 0.531 | 0.920 | 0.673 | no negatives |
| pplx+fastino+bardsai+mmbert | 289 (1.3%) | 0.464 | 0.929 | 0.619 | no negatives |
| vote2(pplx,opf2,nvidia) | 3854 (16.9%) | 0.719 | 0.712 | 0.715 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### redact-ru

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 881 (9.5%) | 0.625 | 0.821 | 0.709 | 1/1 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 1325 (14.4%) | 0.683 | 0.687 | 0.685 | 1/1 |
| pplx+fastino | 240 (2.6%) | 0.563 | 0.893 | 0.691 | 1/1 |
| pplx+fastino+mmbert | 150 (1.6%) | 0.521 | 0.900 | 0.660 | 1/1 |
| pplx+fastino+bardsai | 179 (1.9%) | 0.537 | 0.913 | 0.676 | 1/1 |
| pplx+fastino+bardsai+mmbert | 127 (1.4%) | 0.502 | 0.916 | 0.649 | 1/1 |
| vote2(pplx,opf2,nvidia) | 1186 (12.8%) | 0.711 | 0.769 | 0.739 | 1/1 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### redmadrobot

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | 5516 (100.0%) | 0.000 | 0.000 | 0.000 | 0/371 |
| pplx | 775 (14.1%) | 0.799 | 0.802 | 0.800 | 152/371 |
| gitleaks+pplx | 775 (14.1%) | 0.799 | 0.802 | 0.800 | 152/371 |
| gitleaks+pplx+nvidia | 134 (2.4%) | 0.741 | 0.929 | 0.825 | 216/371 |
| gitleaks+pplx+nvidia+legal | 54 (1.0%) | 0.557 | 0.949 | 0.702 | 301/371 |
| gitleaks+pplx+opf2+nvidia | 115 (2.1%) | 0.721 | 0.934 | 0.814 | 238/371 |
| gitleaks+pplx+opf2+nvidia+legal | 48 (0.9%) | 0.550 | 0.952 | 0.697 | 310/371 |
| gitleaks+pplx+legal+vladlinv | 293 (5.3%) | 0.576 | 0.893 | 0.700 | 276/371 |
| fastino | 1230 (22.3%) | 0.892 | 0.720 | 0.797 | 102/371 |
| pplx+fastino | 153 (2.8%) | 0.780 | 0.920 | 0.845 | 208/371 |
| pplx+fastino+mmbert | 61 (1.1%) | 0.729 | 0.941 | 0.822 | 289/371 |
| pplx+fastino+bardsai | 82 (1.5%) | 0.708 | 0.935 | 0.806 | 238/371 |
| pplx+fastino+bardsai+mmbert | 44 (0.8%) | 0.676 | 0.949 | 0.790 | 299/371 |
| vote2(pplx,opf2,nvidia) | 1050 (19.0%) | 0.888 | 0.728 | 0.800 | 99/371 |
| vote2(gitleaks,pplx,opf2,nvidia) | 1050 (19.0%) | 0.888 | 0.728 | 0.800 | 99/371 |

### rubai-ru

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 16 (0.5%) | 0.924 | 0.960 | 0.941 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 1059 (30.6%) | 0.927 | 0.480 | 0.633 | no negatives |
| pplx+fastino | 12 (0.3%) | 0.897 | 0.961 | 0.928 | no negatives |
| pplx+fastino+mmbert | 9 (0.3%) | 0.887 | 0.961 | 0.923 | no negatives |
| pplx+fastino+bardsai | 8 (0.2%) | 0.876 | 0.967 | 0.920 | no negatives |
| pplx+fastino+bardsai+mmbert | 8 (0.2%) | 0.873 | 0.967 | 0.918 | no negatives |
| vote2(pplx,opf2,nvidia) | 39 (1.1%) | 0.966 | 0.939 | 0.952 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### russian-pii-66k

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | 4805 (100.0%) | 0.000 | 0.000 | 0.000 | no negatives |
| pplx | 11 (0.2%) | 0.920 | 0.993 | 0.955 | no negatives |
| gitleaks+pplx | 11 (0.2%) | 0.920 | 0.993 | 0.955 | no negatives |
| gitleaks+pplx+nvidia | 0 (0.0%) | 0.899 | 0.996 | 0.945 | no negatives |
| gitleaks+pplx+nvidia+legal | 0 (0.0%) | 0.893 | 0.998 | 0.942 | no negatives |
| gitleaks+pplx+opf2+nvidia | 0 (0.0%) | 0.884 | 0.997 | 0.937 | no negatives |
| gitleaks+pplx+opf2+nvidia+legal | 0 (0.0%) | 0.879 | 0.998 | 0.935 | no negatives |
| gitleaks+pplx+legal+vladlinv | 1 (0.0%) | 0.911 | 0.997 | 0.952 | no negatives |
| fastino | 243 (5.1%) | 0.983 | 0.948 | 0.965 | no negatives |
| pplx+fastino | 2 (0.0%) | 0.920 | 0.997 | 0.957 | no negatives |
| pplx+fastino+mmbert | 0 (0.0%) | 0.912 | 0.998 | 0.953 | no negatives |
| pplx+fastino+bardsai | 0 (0.0%) | 0.906 | 0.998 | 0.950 | no negatives |
| pplx+fastino+bardsai+mmbert | 0 (0.0%) | 0.901 | 0.998 | 0.947 | no negatives |
| vote2(pplx,opf2,nvidia) | 16 (0.3%) | 0.936 | 0.988 | 0.961 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | 16 (0.3%) | 0.936 | 0.988 | 0.961 | no negatives |

### scanpatch

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | 8708 (100.0%) | 0.000 | 0.000 | 0.000 | 0/171 |
| pplx | 1084 (12.4%) | 0.875 | 0.850 | 0.862 | 28/171 |
| gitleaks+pplx | 1084 (12.4%) | 0.875 | 0.850 | 0.862 | 28/171 |
| gitleaks+pplx+nvidia | 401 (4.6%) | 0.821 | 0.935 | 0.874 | 100/171 |
| gitleaks+pplx+nvidia+legal | 199 (2.3%) | 0.790 | 0.957 | 0.865 | 104/171 |
| gitleaks+pplx+opf2+nvidia | 340 (3.9%) | 0.810 | 0.945 | 0.872 | 102/171 |
| gitleaks+pplx+opf2+nvidia+legal | 177 (2.0%) | 0.781 | 0.963 | 0.862 | 105/171 |
| gitleaks+pplx+legal+vladlinv | 443 (5.1%) | 0.832 | 0.922 | 0.874 | 50/171 |
| fastino | 1638 (18.8%) | 0.858 | 0.717 | 0.781 | 73/171 |
| pplx+fastino | 354 (4.1%) | 0.846 | 0.942 | 0.891 | 77/171 |
| pplx+fastino+mmbert | 125 (1.4%) | 0.843 | 0.959 | 0.897 | 82/171 |
| pplx+fastino+bardsai | 261 (3.0%) | 0.831 | 0.955 | 0.889 | 79/171 |
| pplx+fastino+bardsai+mmbert | 82 (0.9%) | 0.829 | 0.969 | 0.893 | 82/171 |
| vote2(pplx,opf2,nvidia) | 1716 (19.7%) | 0.891 | 0.724 | 0.799 | 31/171 |
| vote2(gitleaks,pplx,opf2,nvidia) | 1716 (19.7%) | 0.891 | 0.724 | 0.799 | 31/171 |

### secrets-issues

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | 130 (45.1%) | 0.428 | 0.727 | 0.538 | 16/250 |
| pplx | 12 (4.2%) | 0.173 | 0.878 | 0.288 | 191/250 |
| gitleaks+pplx | 7 (2.4%) | 0.173 | 0.948 | 0.292 | 191/250 |
| gitleaks+pplx+nvidia | 5 (1.7%) | 0.161 | 0.954 | 0.275 | 227/250 |
| gitleaks+pplx+nvidia+legal | 3 (1.0%) | 0.124 | 0.957 | 0.219 | 244/250 |
| gitleaks+pplx+opf2+nvidia | 3 (1.0%) | 0.154 | 0.956 | 0.265 | 229/250 |
| gitleaks+pplx+opf2+nvidia+legal | 3 (1.0%) | 0.122 | 0.958 | 0.217 | 244/250 |
| gitleaks+pplx+legal+vladlinv | 3 (1.0%) | 0.129 | 0.954 | 0.228 | 235/250 |
| fastino | 100 (34.7%) | 0.236 | 0.691 | 0.352 | 219/250 |
| pplx+fastino | 7 (2.4%) | 0.146 | 0.957 | 0.253 | 243/250 |
| pplx+fastino+mmbert | 6 (2.1%) | 0.121 | 0.958 | 0.215 | 250/250 |
| pplx+fastino+bardsai | 1 (0.3%) | 0.132 | 0.964 | 0.233 | 248/250 |
| pplx+fastino+bardsai+mmbert | 0 (0.0%) | 0.115 | 0.966 | 0.206 | 250/250 |
| vote2(pplx,opf2,nvidia) | 12 (4.2%) | 0.298 | 0.926 | 0.451 | 151/250 |
| vote2(gitleaks,pplx,opf2,nvidia) | 7 (2.4%) | 0.280 | 0.933 | 0.431 | 151/250 |

### secrets-rules

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | train | train | train | train | train |
| pplx | 29 (3.9%) | 0.625 | 0.949 | 0.753 | 385/750 |
| gitleaks+pplx | train | train | train | train | train |
| gitleaks+pplx+nvidia | train | train | train | train | train |
| gitleaks+pplx+nvidia+legal | train | train | train | train | train |
| gitleaks+pplx+opf2+nvidia | train | train | train | train | train |
| gitleaks+pplx+opf2+nvidia+legal | train | train | train | train | train |
| gitleaks+pplx+legal+vladlinv | train | train | train | train | train |
| fastino | 34 (4.6%) | 0.554 | 0.894 | 0.684 | 573/750 |
| pplx+fastino | 5 (0.7%) | 0.518 | 0.980 | 0.677 | 638/750 |
| pplx+fastino+mmbert | 0 (0.0%) | 0.453 | 1.000 | 0.623 | 713/750 |
| pplx+fastino+bardsai | 2 (0.3%) | 0.499 | 0.998 | 0.665 | 661/750 |
| pplx+fastino+bardsai+mmbert | 0 (0.0%) | 0.448 | 1.000 | 0.619 | 716/750 |
| vote2(pplx,opf2,nvidia) | 22 (2.9%) | 0.621 | 0.957 | 0.754 | 389/750 |
| vote2(gitleaks,pplx,opf2,nvidia) | train | train | train | train | train |

### synth-env-configs

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 0 (0.0%) | 0.265 | 0.996 | 0.418 | 193/200 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 181 (46.2%) | 0.261 | 0.320 | 0.287 | 196/200 |
| pplx+fastino | 0 (0.0%) | 0.231 | 0.996 | 0.375 | 200/200 |
| pplx+fastino+mmbert | 0 (0.0%) | 0.205 | 0.997 | 0.340 | 200/200 |
| pplx+fastino+bardsai | 0 (0.0%) | 0.210 | 0.997 | 0.347 | 200/200 |
| pplx+fastino+bardsai+mmbert | 0 (0.0%) | 0.201 | 0.998 | 0.335 | 200/200 |
| vote2(pplx,opf2,nvidia) | 8 (2.0%) | 0.309 | 0.835 | 0.451 | 187/200 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### synth-jira-comments

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 2 (0.1%) | 0.693 | 0.998 | 0.818 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 371 (13.7%) | 0.902 | 0.720 | 0.801 | no negatives |
| pplx+fastino | 2 (0.1%) | 0.688 | 0.998 | 0.814 | no negatives |
| pplx+fastino+mmbert | 0 (0.0%) | 0.667 | 0.999 | 0.800 | no negatives |
| pplx+fastino+bardsai | 2 (0.1%) | 0.686 | 0.998 | 0.813 | no negatives |
| pplx+fastino+bardsai+mmbert | 0 (0.0%) | 0.666 | 0.999 | 0.799 | no negatives |
| vote2(pplx,opf2,nvidia) | 157 (5.8%) | 0.932 | 0.939 | 0.935 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### synth-ru-tickets

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 849 (2.6%) | 0.732 | 0.967 | 0.833 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 1312 (4.1%) | 0.964 | 0.875 | 0.917 | no negatives |
| pplx+fastino | 31 (0.1%) | 0.722 | 0.991 | 0.835 | no negatives |
| pplx+fastino+mmbert | 10 (0.0%) | 0.675 | 0.992 | 0.803 | no negatives |
| pplx+fastino+bardsai | 6 (0.0%) | 0.699 | 0.994 | 0.821 | no negatives |
| pplx+fastino+bardsai+mmbert | 3 (0.0%) | 0.661 | 0.994 | 0.794 | no negatives |
| vote2(pplx,opf2,nvidia) | 8620 (26.9%) | 0.931 | 0.556 | 0.696 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### synth-secrets-en

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 1 (0.2%) | 0.198 | 0.981 | 0.330 | 275/300 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 206 (35.5%) | 0.555 | 0.402 | 0.466 | 159/300 |
| pplx+fastino | 1 (0.2%) | 0.196 | 0.984 | 0.327 | 285/300 |
| pplx+fastino+mmbert | 0 (0.0%) | 0.177 | 0.986 | 0.300 | 300/300 |
| pplx+fastino+bardsai | 0 (0.0%) | 0.189 | 0.986 | 0.317 | 290/300 |
| pplx+fastino+bardsai+mmbert | 0 (0.0%) | 0.176 | 0.987 | 0.298 | 300/300 |
| vote2(pplx,opf2,nvidia) | 14 (2.4%) | 0.255 | 0.881 | 0.395 | 276/300 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### synth-secrets-ru

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 0 (0.0%) | 0.197 | 0.983 | 0.328 | 285/300 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 204 (35.1%) | 0.566 | 0.409 | 0.475 | 158/300 |
| pplx+fastino | 0 (0.0%) | 0.195 | 0.985 | 0.325 | 289/300 |
| pplx+fastino+mmbert | 0 (0.0%) | 0.176 | 0.985 | 0.299 | 300/300 |
| pplx+fastino+bardsai | 0 (0.0%) | 0.187 | 0.986 | 0.315 | 292/300 |
| pplx+fastino+bardsai+mmbert | 0 (0.0%) | 0.175 | 0.986 | 0.297 | 300/300 |
| vote2(pplx,opf2,nvidia) | 11 (1.9%) | 0.255 | 0.903 | 0.397 | 281/300 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### synth-wiki-tables

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 734 (5.6%) | 0.993 | 0.900 | 0.944 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 1549 (11.8%) | 0.995 | 0.818 | 0.898 | no negatives |
| pplx+fastino | 87 (0.7%) | 0.990 | 0.973 | 0.981 | no negatives |
| pplx+fastino+mmbert | 37 (0.3%) | 0.984 | 0.974 | 0.979 | no negatives |
| pplx+fastino+bardsai | 77 (0.6%) | 0.853 | 0.976 | 0.910 | no negatives |
| pplx+fastino+bardsai+mmbert | 35 (0.3%) | 0.850 | 0.977 | 0.909 | no negatives |
| vote2(pplx,opf2,nvidia) | 2019 (15.4%) | 0.992 | 0.691 | 0.814 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### tab-echr

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 2314 (60.4%) | 0.360 | 0.266 | 0.306 | no negatives |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 60 (1.6%) | 0.479 | 0.942 | 0.635 | no negatives |
| pplx+fastino | 53 (1.4%) | 0.389 | 0.950 | 0.552 | no negatives |
| pplx+fastino+mmbert | 43 (1.1%) | 0.377 | 0.951 | 0.540 | no negatives |
| pplx+fastino+bardsai | 47 (1.2%) | 0.378 | 0.966 | 0.543 | no negatives |
| pplx+fastino+bardsai+mmbert | 37 (1.0%) | 0.368 | 0.967 | 0.533 | no negatives |
| vote2(pplx,opf2,nvidia) | 2446 (63.9%) | 0.958 | 0.245 | 0.390 | no negatives |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

### tonicai

| composition | missed | P | R | F1 | rows touched |
|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - |
| pplx | 502 (20.8%) | 0.881 | 0.817 | 0.848 | 41/440 |
| gitleaks+pplx | - | - | - | - | - |
| gitleaks+pplx+nvidia | - | - | - | - | - |
| gitleaks+pplx+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia | - | - | - | - | - |
| gitleaks+pplx+opf2+nvidia+legal | - | - | - | - | - |
| gitleaks+pplx+legal+vladlinv | - | - | - | - | - |
| fastino | 108 (4.5%) | 0.822 | 0.958 | 0.885 | 154/440 |
| pplx+fastino | 66 (2.7%) | 0.762 | 0.975 | 0.855 | 176/440 |
| pplx+fastino+mmbert | 62 (2.6%) | 0.749 | 0.977 | 0.848 | 190/440 |
| pplx+fastino+bardsai | 62 (2.6%) | 0.727 | 0.979 | 0.835 | 180/440 |
| pplx+fastino+bardsai+mmbert | 59 (2.4%) | 0.719 | 0.980 | 0.829 | 193/440 |
| vote2(pplx,opf2,nvidia) | 507 (21.0%) | 0.976 | 0.813 | 0.887 | 7/440 |
| vote2(gitleaks,pplx,opf2,nvidia) | - | - | - | - | - |

## Paired bootstrap, 95% (char F1 difference, 500 resamples)

| set | gitleaks+pplx+nvidia+legal - gitleaks+pplx+opf2+nvidia | gitleaks+pplx+nvidia+legal - pplx | pplx+fastino - fastino | pplx+fastino - pplx | pplx+fastino+bardsai - pplx+fastino | pplx+fastino+bardsai+mmbert - pplx+fastino+bardsai | vote2(pplx,opf2,nvidia) - pplx |
|---|---|---|---|---|---|---|---|
| alexen2 | - | - | [-0.057, -0.040] | [+0.011, +0.022] | [-0.006, -0.002] | [-0.003, -0.001] | [+0.053, +0.071] |
| alrosait | [-0.012, -0.006] | [-0.079, -0.064] | [+0.097, +0.132] | [-0.073, -0.057] | [-0.011, -0.006] | [-0.003, -0.002] | [+0.003, +0.016] |
| ameau01 | - | - | [-0.074, -0.052] | [-0.000, +0.030] | [-0.056, -0.043] | [-0.030, -0.022] | [-0.020, +0.004] |
| arthur-passwords | - | - | [-0.494, -0.424] | [-0.005, -0.002] | [-0.023, -0.014] | [-0.014, -0.008] | [+0.086, +0.113] |
| corrupt-hivetrace | - | - | [+0.171, +0.231] | [-0.013, -0.006] | [-0.012, -0.005] | [-0.056, -0.039] | [+0.013, +0.031] |
| corrupt-redmadrobot | - | - | [+0.087, +0.113] | [+0.027, +0.041] | [-0.034, -0.021] | [-0.060, -0.042] | [-0.055, -0.029] |
| corrupt-secrets-issues | - | - | [-0.138, -0.006] | [-0.071, -0.037] | [-0.030, -0.009] | [-0.032, -0.015] | [+0.104, +0.178] |
| creddata | - | - | [+0.092, +0.208] | [-0.088, -0.035] | [-0.000, +0.060] | [-0.049, -0.024] | [+0.056, +0.101] |
| dialogpii-en | - | - | [+0.002, +0.021] | [-0.179, -0.122] | [-0.014, -0.006] | [-0.031, -0.024] | [-0.038, -0.005] |
| dialogpii-multi | - | - | [+0.027, +0.044] | [-0.123, -0.088] | [-0.007, +0.000] | [-0.053, -0.041] | [-0.055, -0.026] |
| factrueval | - | - | [+0.006, +0.012] | [+0.547, +0.613] | [-0.022, +0.001] | [-0.014, -0.011] | [+0.163, +0.201] |
| gretel-multi | - | - | [-0.065, -0.037] | [-0.014, +0.002] | [-0.046, -0.034] | [-0.045, -0.036] | [+0.046, +0.068] |
| hivetrace | [-0.003, +0.002] | [-0.105, -0.085] | [+0.145, +0.203] | [-0.013, -0.005] | [-0.017, -0.010] | [-0.004, -0.001] | [+0.039, +0.052] |
| jayguard | [-0.068, -0.046] | [-0.099, -0.069] | [-0.089, -0.058] | [-0.059, -0.031] | [-0.059, -0.039] | [-0.028, -0.016] | [+0.029, +0.056] |
| kiji-en | - | - | [-0.022, -0.012] | [-0.008, +0.002] | [-0.023, -0.018] | [-0.002, -0.001] | [+0.013, +0.020] |
| kiji-multi | - | - | [-0.020, -0.010] | [-0.013, -0.005] | [-0.024, -0.019] | [-0.028, -0.023] | [+0.016, +0.024] |
| leak-museum | - | - | [-0.081, +0.051] | [-0.370, -0.053] | [-0.012, -0.004] | [-0.029, -0.012] | [+0.001, +0.100] |
| leaky-repo | [-0.182, -0.066] | [-0.178, +0.103] | [-0.054, +0.260] | [-0.181, -0.004] | [-0.013, +0.102] | [-0.045, -0.014] | [+0.031, +0.169] |
| multiconer-ru | - | - | [-0.012, -0.005] | [+0.364, +0.431] | [-0.019, -0.004] | [-0.016, -0.010] | [-0.063, -0.025] |
| nemotron-pii | - | - | [+0.006, +0.026] | [+0.044, +0.062] | [-0.036, -0.027] | [-0.012, -0.007] | - |
| nerel | - | - | [-0.008, -0.005] | [+0.567, +0.600] | [-0.038, -0.030] | [-0.022, -0.019] | [+0.095, +0.112] |
| nym-en | - | - | [+0.035, +0.052] | [-0.014, -0.002] | [-0.032, -0.022] | [-0.014, -0.008] | [-0.009, +0.001] |
| nym-multi | - | - | [+0.098, +0.122] | [-0.000, +0.005] | [-0.014, -0.010] | [-0.054, -0.046] | [-0.030, -0.017] |
| nym-ru | [-0.009, -0.003] | [-0.012, -0.002] | [+0.054, +0.064] | [+0.015, +0.022] | [-0.013, -0.008] | [-0.003, -0.002] | [+0.008, +0.015] |
| privy | - | - | [-0.236, -0.193] | [-0.012, +0.000] | [-0.008, -0.003] | [-0.013, -0.010] | [+0.047, +0.063] |
| redact-multi | - | - | [-0.014, +0.006] | [-0.020, -0.008] | [-0.019, -0.015] | [-0.059, -0.051] | [+0.004, +0.018] |
| redact-ru | - | - | [-0.008, +0.019] | [-0.026, -0.012] | [-0.017, -0.011] | [-0.032, -0.024] | [+0.021, +0.037] |
| redmadrobot | [-0.140, -0.086] | [-0.130, -0.070] | [+0.033, +0.061] | [+0.035, +0.054] | [-0.048, -0.031] | [-0.021, -0.012] | [-0.012, +0.013] |
| rubai-ru | - | - | [+0.280, +0.314] | [-0.015, -0.012] | [-0.010, -0.007] | [-0.002, -0.001] | [+0.008, +0.014] |
| russian-pii-66k | [+0.004, +0.007] | [-0.015, -0.011] | [-0.012, -0.004] | [+0.001, +0.002] | [-0.009, -0.006] | [-0.004, -0.002] | [+0.004, +0.008] |
| scanpatch | [-0.010, -0.004] | [-0.003, +0.009] | [+0.098, +0.121] | [+0.023, +0.036] | [-0.005, -0.000] | [+0.003, +0.006] | [-0.072, -0.056] |
| secrets-issues | [-0.061, -0.029] | [-0.100, -0.033] | [-0.157, -0.029] | [-0.064, +0.002] | [-0.029, -0.011] | [-0.036, -0.017] | [+0.106, +0.201] |
| secrets-rules | - | - | [-0.026, +0.014] | [-0.105, -0.053] | [-0.030, +0.005] | [-0.053, -0.041] | [-0.021, +0.016] |
| synth-env-configs | - | - | [+0.044, +0.127] | [-0.050, -0.036] | [-0.034, -0.022] | [-0.014, -0.011] | [+0.018, +0.048] |
| synth-jira-comments | - | - | [-0.002, +0.029] | [-0.004, -0.003] | [-0.001, -0.001] | [-0.016, -0.013] | [+0.109, +0.126] |
| synth-ru-tickets | - | - | [-0.089, -0.076] | [+0.000, +0.003] | [-0.015, -0.013] | [-0.028, -0.025] | [-0.141, -0.132] |
| synth-secrets-en | - | - | [-0.198, -0.084] | [-0.004, -0.002] | [-0.014, -0.007] | [-0.021, -0.017] | [+0.056, +0.075] |
| synth-secrets-ru | - | - | [-0.207, -0.089] | [-0.003, -0.001] | [-0.015, -0.007] | [-0.019, -0.016] | [+0.061, +0.078] |
| synth-wiki-tables | - | - | [+0.073, +0.094] | [+0.032, +0.043] | [-0.076, -0.065] | [-0.002, -0.001] | [-0.146, -0.115] |
| tab-echr | - | - | [-0.092, -0.076] | [+0.212, +0.281] | [-0.012, -0.005] | [-0.011, -0.009] | [+0.065, +0.103] |
| tonicai | - | - | [-0.036, -0.023] | [-0.008, +0.019] | [-0.027, -0.016] | [-0.007, -0.004] | [+0.032, +0.047] |

