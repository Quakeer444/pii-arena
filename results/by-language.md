# Base models by language and task

Coverage-first listing, then observed missed percentage within equal coverage counts. Equal counts do not imply equal dataset subsets: this is **not a leaderboard across unequal subsets**. Missing and training-source runs are excluded, never counted as perfect detections. Inspect the linked per-dataset reports.

A `-ru` suffix changes zero-shot labels to Russian using the same weights. Such runs apply only to Russian cuts. Chunking variants are in the [full quality report](report.md).

**Scanner rows use mixed adapter status (2026-09-18 capture and decoded-content correction).** `gitleaks` rows use corrected positions from a rerun whose mapping policy is recorded in the run inventory; `detect-secrets` was re-run and matched its stored predictions; every other scanner row (`betterleaks`, `trufflehog`, `noseyparker`, `titus`, `kingfisher`, `credsweeper`, `credsweeper-noml`, `deepsecrets`) is a historical result produced before the correction and is marked historical. Scanner coverage is partial; see the [scanner status table](../docs/reproduce.md#scanner-adapter-status).

## RU / PII

18 datasets, 135,838 normalized gold spans. 

| Model | Eligible sets | Missed / eligible gold | Missed % |
|---|---:|---:|---:|
| gliner2-fastino | 18/18 | 17,533 / 135,838 | 12.91% |
| gliner2-fastino-ru | 18/18 | 18,016 / 135,838 | 13.26% |
| nuner-zero | 18/18 | 25,998 / 135,838 | 19.14% |
| gliner2-hivetrace-omni | 18/18 | 27,286 / 135,838 | 20.09% |
| gliner2-hivetrace-omni-ru | 18/18 | 29,383 / 135,838 | 21.63% |
| bardsai-eu | 18/18 | 29,704 / 135,838 | 21.87% |
| mmbert32k | 18/18 | 32,632 / 135,838 | 24.02% |
| pplx | 18/18 | 35,071 / 135,838 | 25.82% |
| ru-legal-ner | 18/18 | 35,601 / 135,838 | 26.21% |
| gliner-urchade | 18/18 | 35,729 / 135,838 | 26.30% |
| gliner25-fastino-ru | 18/18 | 36,178 / 135,838 | 26.63% |
| gliner-pii-edge | 18/18 | 38,386 / 135,838 | 28.26% |
| gliner2-large | 18/18 | 38,450 / 135,838 | 28.31% |
| apararti | 18/18 | 40,487 / 135,838 | 29.81% |
| openmed-nemotron | 18/18 | 40,648 / 135,838 | 29.92% |
| gliner-nvidia | 18/18 | 40,898 / 135,838 | 30.11% |
| gliner25-fastino | 18/18 | 41,555 / 135,838 | 30.59% |
| openmed-multilingual | 18/18 | 41,827 / 135,838 | 30.79% |
| opf-kz-ru | 18/18 | 48,945 / 135,838 | 36.03% |
| openai-base | 18/18 | 49,170 / 135,838 | 36.20% |
| fef2-secret-ru | 18/18 | 50,080 / 135,838 | 36.87% |
| kalyan-ettin | 18/18 | 50,969 / 135,838 | 37.52% |
| gliner-stream-pii | 18/18 | 51,671 / 135,838 | 38.04% |
| gliner-nvidia-ru | 18/18 | 52,938 / 135,838 | 38.97% |
| traciora | 18/18 | 55,302 / 135,838 | 40.71% |
| ru-pii-ner | 18/18 | 56,384 / 135,838 | 41.51% |
| gliner-multi-v21 | 18/18 | 57,738 / 135,838 | 42.51% |
| opf-ru-v2 | 18/18 | 58,606 / 135,838 | 43.14% |
| gliner-urchade-ru | 18/18 | 61,624 / 135,838 | 45.37% |
| gliner-multi-v21-ru | 18/18 | 64,237 / 135,838 | 47.29% |
| gliner2-hivetrace-uni | 18/18 | 66,931 / 135,838 | 49.27% |
| stanza-ru | 18/18 | 67,833 / 135,838 | 49.94% |
| gliner-pii-base | 18/18 | 68,673 / 135,838 | 50.56% |
| ner-ru-yqelz | 18/18 | 70,571 / 135,838 | 51.95% |
| ner-ru-gherman | 18/18 | 70,574 / 135,838 | 51.95% |
| davlan-xlmr | 18/18 | 70,842 / 135,838 | 52.15% |
| gliner2-vladlinv | 18/18 | 71,190 / 135,838 | 52.41% |
| gliner2-vladlinv-ru | 18/18 | 72,208 / 135,838 | 53.16% |
| davlan-mbert | 18/18 | 73,941 / 135,838 | 54.43% |
| spacy-ru-lg | 18/18 | 76,616 / 135,838 | 56.40% |
| natasha | 18/18 | 79,367 / 135,838 | 58.43% |
| gravitee-small | 18/18 | 84,932 / 135,838 | 62.52% |
| rules-ru | 18/18 | 89,774 / 135,838 | 66.09% |
| gliner2-hivetrace-uni-ru | 18/18 | 103,253 / 135,838 | 76.01% |
| nym-base | 17/18 | 22,989 / 126,341 | 18.20% |
| opf-ru | 17/18 | 48,162 / 131,033 | 36.76% |
| spacy-alrosait | 16/18 | 88,917 / 125,268 | 70.98% |
| pii-shield-onnx | 12/18 | 15,721 / 77,451 | 20.30% |
| betterleaks *(historical pre-fix)* | 7/18 | 33,233 / 33,250 | 99.95% |
| gitleaks *(corrected rerun)* | 7/18 | 33,233 / 33,250 | 99.95% |
| nym-small | 4/18 | 15,981 / 40,490 | 39.47% |
| presidio-ru | 2/18 | 3,426 / 7,183 | 47.70% |
| ner-ru-gherman-onnx | 1/18 | 1,164 / 1,667 | 69.83% |
| detect-secrets *(verified unchanged)* | 1/18 | 1,641 / 1,667 | 98.44% |
| kingfisher *(historical pre-fix)* | 1/18 | 1,650 / 1,667 | 98.98% |
| noseyparker *(historical pre-fix)* | 1/18 | 1,650 / 1,667 | 98.98% |
| titus *(historical pre-fix)* | 1/18 | 1,650 / 1,667 | 98.98% |
| credsweeper-noml *(historical pre-fix)* | 1/18 | 1,656 / 1,667 | 99.34% |
| credsweeper *(historical pre-fix)* | 1/18 | 1,659 / 1,667 | 99.52% |
| deepsecrets *(historical pre-fix)* | 1/18 | 1,666 / 1,667 | 99.94% |
| trufflehog *(historical pre-fix)* | 1/18 | 1,666 / 1,667 | 99.94% |

`Missed` means no predicted character touches the normalized annotation; it says nothing about full hiding. A detector that touches nearly every annotation can still leave characters exposed, and one that hides well can mask text without annotations. Full-hiding and extra-masking outcomes for the fixed reference composition are in the [overview](overview.md#headline-masking-outcome).

Datasets: [alexen2](datasets/alexen2.md), [alrosait](datasets/alrosait.md), [corrupt-hivetrace](datasets/corrupt-hivetrace.md), [corrupt-redmadrobot](datasets/corrupt-redmadrobot.md), [factrueval](datasets/factrueval.md), [hivetrace](datasets/hivetrace.md), [jayguard](datasets/jayguard.md), [multiconer-ru](datasets/multiconer-ru.md), [nerel](datasets/nerel.md), [nym-ru](datasets/nym-ru.md), [redact-ru](datasets/redact-ru.md), [redmadrobot](datasets/redmadrobot.md), [rubai-ru](datasets/rubai-ru.md), [russian-pii-66k](datasets/russian-pii-66k.md), [scanpatch](datasets/scanpatch.md), [synth-jira-comments](datasets/synth-jira-comments.md), [synth-ru-tickets](datasets/synth-ru-tickets.md), [synth-wiki-tables](datasets/synth-wiki-tables.md).

## RU / SECRETS

1 datasets, 581 normalized gold spans. Synthetic-only secrets evaluation.

| Model | Eligible sets | Missed / eligible gold | Missed % |
|---|---:|---:|---:|
| pplx | 1/1 | 0 / 581 | 0.00% |
| opf-ru | 1/1 | 1 / 581 | 0.17% |
| apararti | 1/1 | 4 / 581 | 0.69% |
| opf-kz-ru | 1/1 | 4 / 581 | 0.69% |
| openai-base | 1/1 | 12 / 581 | 2.07% |
| opf-ru-v2 | 1/1 | 15 / 581 | 2.58% |
| traciora | 1/1 | 17 / 581 | 2.93% |
| openmed-multilingual | 1/1 | 20 / 581 | 3.44% |
| nym-base | 1/1 | 21 / 581 | 3.61% |
| ru-legal-ner | 1/1 | 52 / 581 | 8.95% |
| bardsai-eu | 1/1 | 55 / 581 | 9.47% |
| gliner-pii-edge | 1/1 | 86 / 581 | 14.80% |
| kalyan-ettin | 1/1 | 86 / 581 | 14.80% |
| openmed-nemotron | 1/1 | 86 / 581 | 14.80% |
| rules-ru | 1/1 | 105 / 581 | 18.07% |
| mmbert32k | 1/1 | 136 / 581 | 23.41% |
| fef2-secret-ru | 1/1 | 150 / 581 | 25.82% |
| nuner-zero | 1/1 | 198 / 581 | 34.08% |
| gliner2-fastino | 1/1 | 204 / 581 | 35.11% |
| gliner-nvidia | 1/1 | 210 / 581 | 36.14% |
| gliner25-fastino | 1/1 | 232 / 581 | 39.93% |
| stanza-ru | 1/1 | 238 / 581 | 40.96% |
| gliner25-fastino-ru | 1/1 | 265 / 581 | 45.61% |
| gliner2-hivetrace-omni | 1/1 | 271 / 581 | 46.64% |
| gliner2-fastino-ru | 1/1 | 284 / 581 | 48.88% |
| gliner-stream-pii | 1/1 | 305 / 581 | 52.50% |
| gliner-nvidia-ru | 1/1 | 331 / 581 | 56.97% |
| gravitee-small | 1/1 | 334 / 581 | 57.49% |
| gliner2-hivetrace-omni-ru | 1/1 | 338 / 581 | 58.18% |
| gliner2-vladlinv-ru | 1/1 | 376 / 581 | 64.72% |
| gliner-urchade | 1/1 | 378 / 581 | 65.06% |
| gliner2-vladlinv | 1/1 | 403 / 581 | 69.36% |
| gliner2-large | 1/1 | 426 / 581 | 73.32% |
| gliner-pii-base | 1/1 | 445 / 581 | 76.59% |
| gliner-multi-v21-ru | 1/1 | 453 / 581 | 77.97% |
| gliner-urchade-ru | 1/1 | 457 / 581 | 78.66% |
| gliner-multi-v21 | 1/1 | 465 / 581 | 80.03% |
| ru-pii-ner | 1/1 | 477 / 581 | 82.10% |
| gliner2-hivetrace-uni-ru | 1/1 | 491 / 581 | 84.51% |
| ner-ru-yqelz | 1/1 | 527 / 581 | 90.71% |
| gliner2-hivetrace-uni | 1/1 | 575 / 581 | 98.97% |
| spacy-ru-lg | 1/1 | 577 / 581 | 99.31% |
| natasha | 1/1 | 580 / 581 | 99.83% |
| davlan-mbert | 1/1 | 581 / 581 | 100.00% |
| davlan-xlmr | 1/1 | 581 / 581 | 100.00% |
| ner-ru-gherman | 1/1 | 581 / 581 | 100.00% |
| spacy-alrosait | 1/1 | 581 / 581 | 100.00% |

`Missed` means no predicted character touches the normalized annotation; it says nothing about full hiding. A detector that touches nearly every annotation can still leave characters exposed, and one that hides well can mask text without annotations. Full-hiding and extra-masking outcomes for the fixed reference composition are in the [overview](overview.md#headline-masking-outcome).

Datasets: [synth-secrets-ru](datasets/synth-secrets-ru.md).

## EN / PII

8 datasets, 34,073 normalized gold spans. 

| Model | Eligible sets | Missed / eligible gold | Missed % |
|---|---:|---:|---:|
| gliner2-fastino | 8/8 | 2,530 / 34,073 | 7.43% |
| gliner2-large | 8/8 | 4,679 / 34,073 | 13.73% |
| bardsai-eu | 8/8 | 5,406 / 34,073 | 15.87% |
| pplx | 8/8 | 5,646 / 34,073 | 16.57% |
| gliner-stream-pii | 8/8 | 5,796 / 34,073 | 17.01% |
| nuner-zero | 8/8 | 6,742 / 34,073 | 19.79% |
| gravitee-small | 8/8 | 6,959 / 34,073 | 20.42% |
| mmbert32k | 8/8 | 7,229 / 34,073 | 21.22% |
| gliner-pii-edge | 8/8 | 8,919 / 34,073 | 26.18% |
| gliner25-fastino | 8/8 | 9,088 / 34,073 | 26.67% |
| gliner-pii-base | 8/8 | 10,282 / 34,073 | 30.18% |
| apararti | 8/8 | 10,317 / 34,073 | 30.28% |
| gliner-multi-v21 | 8/8 | 10,867 / 34,073 | 31.89% |
| opf-kz-ru | 8/8 | 11,128 / 34,073 | 32.66% |
| openai-base | 8/8 | 11,217 / 34,073 | 32.92% |
| gliner-urchade | 8/8 | 11,390 / 34,073 | 33.43% |
| opf-ru | 8/8 | 11,727 / 34,073 | 34.42% |
| stanza-ru | 8/8 | 13,396 / 34,073 | 39.32% |
| ru-pii-ner | 8/8 | 13,670 / 34,073 | 40.12% |
| davlan-xlmr | 8/8 | 14,522 / 34,073 | 42.62% |
| traciora | 8/8 | 14,559 / 34,073 | 42.73% |
| opf-ru-v2 | 8/8 | 14,994 / 34,073 | 44.01% |
| gliner2-vladlinv | 8/8 | 15,206 / 34,073 | 44.63% |
| davlan-mbert | 8/8 | 15,530 / 34,073 | 45.58% |
| ner-ru-yqelz | 8/8 | 15,851 / 34,073 | 46.52% |
| ner-ru-gherman | 8/8 | 17,600 / 34,073 | 51.65% |
| ru-legal-ner | 8/8 | 21,418 / 34,073 | 62.86% |
| spacy-ru-lg | 8/8 | 29,048 / 34,073 | 85.25% |
| fef2-secret-ru | 8/8 | 29,641 / 34,073 | 86.99% |
| rules-ru | 8/8 | 30,078 / 34,073 | 88.28% |
| natasha | 8/8 | 30,412 / 34,073 | 89.26% |
| spacy-alrosait | 8/8 | 34,066 / 34,073 | 99.98% |
| gliner2-hivetrace-omni | 7/8 | 2,778 / 24,682 | 11.26% |
| gliner-nvidia | 7/8 | 3,002 / 24,682 | 12.16% |
| nym-base | 7/8 | 4,613 / 30,489 | 15.13% |
| kalyan-ettin | 7/8 | 5,775 / 24,682 | 23.40% |
| openmed-nemotron | 7/8 | 6,080 / 24,682 | 24.63% |
| gliner2-hivetrace-uni | 7/8 | 9,625 / 24,682 | 39.00% |
| openmed-multilingual | 6/8 | 3,940 / 22,783 | 17.29% |
| pii-shield-onnx | 6/8 | 16,473 / 29,757 | 55.36% |
| nym-small | 3/8 | 2,757 / 15,463 | 17.83% |
| ner-ru-gherman-onnx | 2/8 | 3,272 / 6,072 | 53.89% |

`Missed` means no predicted character touches the normalized annotation; it says nothing about full hiding. A detector that touches nearly every annotation can still leave characters exposed, and one that hides well can mask text without annotations. Full-hiding and extra-masking outcomes for the fixed reference composition are in the [overview](overview.md#headline-masking-outcome).

Datasets: [ameau01](datasets/ameau01.md), [dialogpii-en](datasets/dialogpii-en.md), [kiji-en](datasets/kiji-en.md), [nemotron-pii](datasets/nemotron-pii.md), [nym-en](datasets/nym-en.md), [privy](datasets/privy.md), [tab-echr](datasets/tab-echr.md), [tonicai](datasets/tonicai.md).

## EN / SECRETS

9 datasets, 3,547 normalized gold spans. 

| Model | Eligible sets | Missed / eligible gold | Missed % |
|---|---:|---:|---:|
| opf-ru | 9/9 | 76 / 3,547 | 2.14% |
| apararti | 9/9 | 100 / 3,547 | 2.82% |
| opf-kz-ru | 9/9 | 103 / 3,547 | 2.90% |
| pplx | 9/9 | 123 / 3,547 | 3.47% |
| traciora | 9/9 | 144 / 3,547 | 4.06% |
| nym-base | 9/9 | 156 / 3,547 | 4.40% |
| opf-ru-v2 | 9/9 | 175 / 3,547 | 4.93% |
| openmed-multilingual | 9/9 | 264 / 3,547 | 7.44% |
| openai-base | 9/9 | 272 / 3,547 | 7.67% |
| gliner-pii-edge | 9/9 | 415 / 3,547 | 11.70% |
| ru-legal-ner | 9/9 | 463 / 3,547 | 13.05% |
| kalyan-ettin | 9/9 | 466 / 3,547 | 13.14% |
| bardsai-eu | 9/9 | 467 / 3,547 | 13.17% |
| openmed-nemotron | 9/9 | 489 / 3,547 | 13.79% |
| mmbert32k | 9/9 | 546 / 3,547 | 15.39% |
| gliner2-fastino | 9/9 | 820 / 3,547 | 23.12% |
| gliner25-fastino | 9/9 | 1,014 / 3,547 | 28.59% |
| gliner-stream-pii | 9/9 | 1,060 / 3,547 | 29.88% |
| nuner-zero | 9/9 | 1,088 / 3,547 | 30.67% |
| gliner-nvidia | 9/9 | 1,170 / 3,547 | 32.99% |
| fef2-secret-ru | 9/9 | 1,329 / 3,547 | 37.47% |
| rules-ru | 9/9 | 1,330 / 3,547 | 37.50% |
| gravitee-small | 9/9 | 1,485 / 3,547 | 41.87% |
| gliner-urchade | 9/9 | 1,710 / 3,547 | 48.21% |
| gliner2-hivetrace-omni | 9/9 | 1,915 / 3,547 | 53.99% |
| gliner2-vladlinv | 9/9 | 2,119 / 3,547 | 59.74% |
| stanza-ru | 9/9 | 2,402 / 3,547 | 67.72% |
| gliner2-large | 9/9 | 2,490 / 3,547 | 70.20% |
| ner-ru-yqelz | 9/9 | 2,553 / 3,547 | 71.98% |
| gliner-pii-base | 9/9 | 2,561 / 3,547 | 72.20% |
| gliner-multi-v21 | 9/9 | 2,612 / 3,547 | 73.64% |
| ru-pii-ner | 9/9 | 2,707 / 3,547 | 76.32% |
| gliner2-hivetrace-uni | 9/9 | 3,082 / 3,547 | 86.89% |
| spacy-ru-lg | 9/9 | 3,362 / 3,547 | 94.78% |
| natasha | 9/9 | 3,527 / 3,547 | 99.44% |
| davlan-mbert | 9/9 | 3,536 / 3,547 | 99.69% |
| ner-ru-gherman | 9/9 | 3,542 / 3,547 | 99.86% |
| davlan-xlmr | 9/9 | 3,546 / 3,547 | 99.97% |
| spacy-alrosait | 9/9 | 3,547 / 3,547 | 100.00% |
| pii-shield-onnx | 5/9 | 35 / 1,510 | 2.32% |
| credsweeper-noml *(historical pre-fix)* | 3/9 | 220 / 1,129 | 19.49% |
| deepsecrets *(historical pre-fix)* | 3/9 | 658 / 1,129 | 58.28% |
| detect-secrets *(verified unchanged)* | 3/9 | 680 / 1,129 | 60.23% |
| credsweeper *(historical pre-fix)* | 2/9 | 246 / 1,034 | 23.79% |
| gitleaks *(corrected rerun)* | 2/9 | 203 / 383 | 53.00% |
| trufflehog *(historical pre-fix)* | 2/9 | 802 / 1,034 | 77.56% |
| noseyparker *(historical pre-fix)* | 2/9 | 826 / 1,034 | 79.88% |
| nym-small | 1/9 | 6 / 288 | 2.08% |
| betterleaks *(historical pre-fix)* | 1/9 | 123 / 288 | 42.71% |
| titus *(historical pre-fix)* | 1/9 | 202 / 288 | 70.14% |
| kingfisher *(historical pre-fix)* | 1/9 | 242 / 288 | 84.03% |

`Missed` means no predicted character touches the normalized annotation; it says nothing about full hiding. A detector that touches nearly every annotation can still leave characters exposed, and one that hides well can mask text without annotations. Full-hiding and extra-masking outcomes for the fixed reference composition are in the [overview](overview.md#headline-masking-outcome).

Datasets: [arthur-passwords](datasets/arthur-passwords.md), [corrupt-secrets-issues](datasets/corrupt-secrets-issues.md), [creddata](datasets/creddata.md), [leak-museum](datasets/leak-museum.md), [leaky-repo](datasets/leaky-repo.md), [secrets-issues](datasets/secrets-issues.md), [secrets-rules](datasets/secrets-rules.md), [synth-env-configs](datasets/synth-env-configs.md), [synth-secrets-en](datasets/synth-secrets-en.md).

## MULTI / PII

5 datasets, 53,427 normalized gold spans. 

| Model | Eligible sets | Missed / eligible gold | Missed % |
|---|---:|---:|---:|
| bardsai-eu | 5/5 | 6,751 / 53,427 | 12.64% |
| pplx | 5/5 | 6,807 / 53,427 | 12.74% |
| mmbert32k | 5/5 | 8,290 / 53,427 | 15.52% |
| gliner2-fastino | 5/5 | 8,924 / 53,427 | 16.70% |
| gliner-nvidia | 5/5 | 10,258 / 53,427 | 19.20% |
| gliner-urchade | 5/5 | 13,310 / 53,427 | 24.91% |
| nuner-zero | 5/5 | 14,237 / 53,427 | 26.65% |
| opf-ru | 5/5 | 14,655 / 53,427 | 27.43% |
| openmed-nemotron | 5/5 | 16,800 / 53,427 | 31.44% |
| apararti | 5/5 | 16,803 / 53,427 | 31.45% |
| kalyan-ettin | 5/5 | 17,678 / 53,427 | 33.09% |
| gliner2-large | 5/5 | 17,687 / 53,427 | 33.10% |
| openai-base | 5/5 | 18,054 / 53,427 | 33.79% |
| gliner25-fastino | 5/5 | 18,330 / 53,427 | 34.31% |
| gravitee-small | 5/5 | 18,912 / 53,427 | 35.40% |
| opf-kz-ru | 5/5 | 19,077 / 53,427 | 35.71% |
| gliner-multi-v21 | 5/5 | 19,085 / 53,427 | 35.72% |
| ru-legal-ner | 5/5 | 21,054 / 53,427 | 39.41% |
| davlan-xlmr | 5/5 | 21,225 / 53,427 | 39.73% |
| traciora | 5/5 | 22,008 / 53,427 | 41.19% |
| davlan-mbert | 5/5 | 22,682 / 53,427 | 42.45% |
| gliner-stream-pii | 5/5 | 23,470 / 53,427 | 43.93% |
| opf-ru-v2 | 5/5 | 23,683 / 53,427 | 44.33% |
| ru-pii-ner | 5/5 | 23,883 / 53,427 | 44.70% |
| ner-ru-gherman | 5/5 | 24,200 / 53,427 | 45.30% |
| gliner-pii-edge | 5/5 | 24,297 / 53,427 | 45.48% |
| ner-ru-yqelz | 5/5 | 24,796 / 53,427 | 46.41% |
| gliner2-vladlinv | 5/5 | 25,704 / 53,427 | 48.11% |
| stanza-ru | 5/5 | 27,253 / 53,427 | 51.01% |
| gliner-pii-base | 5/5 | 30,566 / 53,427 | 57.21% |
| spacy-ru-lg | 5/5 | 46,536 / 53,427 | 87.10% |
| fef2-secret-ru | 5/5 | 47,658 / 53,427 | 89.20% |
| rules-ru | 5/5 | 48,473 / 53,427 | 90.73% |
| natasha | 5/5 | 49,810 / 53,427 | 93.23% |
| spacy-alrosait | 5/5 | 53,242 / 53,427 | 99.65% |
| nym-base | 4/5 | 7,975 / 45,258 | 17.62% |
| gliner2-hivetrace-omni | 4/5 | 8,964 / 48,943 | 18.32% |
| openmed-multilingual | 4/5 | 12,068 / 48,943 | 24.66% |
| gliner2-hivetrace-uni | 4/5 | 15,677 / 48,943 | 32.03% |
| nym-small | 1/5 | 204 / 7,565 | 2.70% |
| pii-shield-onnx | 1/5 | 2,409 / 7,565 | 31.84% |
| ner-ru-gherman-onnx | 1/5 | 2,989 / 7,565 | 39.51% |

`Missed` means no predicted character touches the normalized annotation; it says nothing about full hiding. A detector that touches nearly every annotation can still leave characters exposed, and one that hides well can mask text without annotations. Full-hiding and extra-masking outcomes for the fixed reference composition are in the [overview](overview.md#headline-masking-outcome).

Datasets: [dialogpii-multi](datasets/dialogpii-multi.md), [gretel-multi](datasets/gretel-multi.md), [kiji-multi](datasets/kiji-multi.md), [nym-multi](datasets/nym-multi.md), [redact-multi](datasets/redact-multi.md).
