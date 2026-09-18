# Results by sensitive-data type

All figures and tables on this page use **PPLX + Fastino + mmBERT + BardsAI**, threshold 0.5. The same fixed composition is used in every cell. It is an illustration of category behavior, not an independently selected winner.

![Full hiding by data type](../assets/entity-types.svg)

## Pooled category results

| Category | Fully hidden / normalized gold | Hidden % | Detected % | Raw mask / same normalized gold | Raw mask / original annotations | Datasets |
|---|---:|---:|---:|---:|---:|---:|
| Passwords, keys & tokens | 6,606 / 6,870 | 96.16% | 99.81% | 95.62% | 6,585/6,871 (95.84%) | 25 |
| Logins & usernames | 11,308 / 11,382 | 99.35% | 99.94% | 99.23% | 11,307/11,387 (99.30%) | 13 |
| Bank accounts & cards | 4,270 / 5,253 | 81.29% | 99.68% | 79.80% | 4,262/5,260 (81.03%) | 16 |
| Documents & identifiers | 14,007 / 15,034 | 93.17% | 98.24% | 92.06% | 14,121/15,200 (92.90%) | 20 |
| People's names | 63,718 / 65,736 | 96.93% | 98.84% | 95.95% | 64,317/66,498 (96.72%) | 31 |
| Phone numbers & email | 21,191 / 21,981 | 96.41% | 99.45% | 95.85% | 21,206/22,018 (96.31%) | 25 |
| Addresses & locations | 36,766 / 39,602 | 92.84% | 97.65% | 91.84% | 37,170/40,266 (92.31%) | 27 |
| Dates & times | 5,401 / 5,502 | 98.16% | 99.53% | 95.55% | 5,399/5,537 (97.51%) | 11 |
| Organizations | 16,650 / 19,274 | 86.39% | 96.57% | 85.41% | 17,618/20,455 (86.13%) | 20 |
| Network identifiers | 25,129 / 25,631 | 98.04% | 99.77% | 97.87% | 25,111/25,656 (97.88%) | 19 |
| Customer & employee IDs | 7,352 / 7,994 | 91.97% | 99.99% | 90.87% | 7,346/8,008 (91.73%) | 10 |
| Other sensitive attributes | 2,340 / 3,207 | 72.97% | 87.78% | 68.07% | 2,338/3,290 (71.06%) | 5 |

The last two percentage columns have explicitly different gold boundaries. A source label remains a separate annotation unit after normalization even if another label has the same boundaries. The presentation mapping does not change scoring protocol 1. No per-category precision is invented from label-blind masks: false-positive characters cannot be uniquely assigned to a gold category.

Credentials groups include passwords, keys, tokens and explicitly labeled usernames/logins. Customer IDs, employee references, badge numbers and ambiguous social identifiers have their own row. Some upstream SECRET labels describe salts, UUIDs or resource identifiers; this chart preserves their source annotation policy and does not assert that every value is a usable secret. Dates include only the date/time labels actually retained in the frozen inputs.

## Every category on every contributing dataset

Dataset order is stable. Absent categories are not measured and do not become 100%. Counts below 100 spans are marked small; the cutoff is a display convention, not a confidence bound. All entries remain in the CSV.

### Passwords, keys & tokens

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [corrupt-hivetrace](types/corrupt-hivetrace.md) | 95 | 95 (100.00%) | 100.00% | 96.84% | small |
| [hivetrace](types/hivetrace.md) | 95 | 95 (100.00%) | 100.00% | 100.00% | small |
| [nym-ru](types/nym-ru.md) | 307 | 305 (99.35%) | 100.00% | 99.35% | - |
| [redact-ru](types/redact-ru.md) | 11 | 8 (72.73%) | 100.00% | 72.73% | small |
| [russian-pii-66k](types/russian-pii-66k.md) | 194 | 194 (100.00%) | 100.00% | 100.00% | - |
| [synth-jira-comments](types/synth-jira-comments.md) | 344 | 340 (98.84%) | 100.00% | 98.84% | - |
| [synth-ru-tickets](types/synth-ru-tickets.md) | 364 | 364 (100.00%) | 100.00% | 100.00% | - |
| [synth-secrets-ru](types/synth-secrets-ru.md) | 581 | 571 (98.28%) | 100.00% | 97.76% | - |
| [kiji-en](types/kiji-en.md) | 211 | 209 (99.05%) | 99.53% | 99.05% | - |
| [nemotron-pii](types/nemotron-pii.md) | 375 | 331 (88.27%) | 100.00% | 87.73% | - |
| [nym-en](types/nym-en.md) | 39 | 38 (97.44%) | 100.00% | 97.44% | small |
| [privy](types/privy.md) | 30 | 30 (100.00%) | 100.00% | 100.00% | small |
| [arthur-passwords](types/arthur-passwords.md) | 280 | 280 (100.00%) | 100.00% | 100.00% | - |
| [corrupt-secrets-issues](types/corrupt-secrets-issues.md) | 288 | 230 (79.86%) | 100.00% | 78.12% | - |
| [creddata](types/creddata.md) | 776 | 743 (95.75%) | 99.87% | 95.23% | - |
| [leak-museum](types/leak-museum.md) | 101 | 96 (95.05%) | 98.02% | 95.05% | - |
| [leaky-repo](types/leaky-repo.md) | 95 | 88 (92.63%) | 98.95% | 92.63% | small |
| [secrets-issues](types/secrets-issues.md) | 288 | 229 (79.51%) | 100.00% | 78.82% | - |
| [secrets-rules](types/secrets-rules.md) | 746 | 740 (99.20%) | 100.00% | 98.93% | - |
| [synth-env-configs](types/synth-env-configs.md) | 392 | 387 (98.72%) | 100.00% | 98.47% | - |
| [synth-secrets-en](types/synth-secrets-en.md) | 581 | 569 (97.93%) | 100.00% | 97.59% | - |
| [gretel-multi](types/gretel-multi.md) | 217 | 217 (100.00%) | 100.00% | 100.00% | - |
| [kiji-multi](types/kiji-multi.md) | 255 | 246 (96.47%) | 97.25% | 96.47% | - |
| [nym-multi](types/nym-multi.md) | 173 | 172 (99.42%) | 100.00% | 91.91% | - |
| [redact-multi](types/redact-multi.md) | 32 | 29 (90.62%) | 96.88% | 90.62% | small |

### Logins & usernames

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [nym-ru](types/nym-ru.md) | 315 | 315 (100.00%) | 100.00% | 99.68% | - |
| [russian-pii-66k](types/russian-pii-66k.md) | 311 | 311 (100.00%) | 100.00% | 100.00% | - |
| [synth-jira-comments](types/synth-jira-comments.md) | 221 | 221 (100.00%) | 100.00% | 100.00% | - |
| [synth-ru-tickets](types/synth-ru-tickets.md) | 7,565 | 7,565 (100.00%) | 100.00% | 100.00% | - |
| [synth-wiki-tables](types/synth-wiki-tables.md) | 1,597 | 1,597 (100.00%) | 100.00% | 100.00% | - |
| [ameau01](types/ameau01.md) | 627 | 621 (99.04%) | 99.52% | 98.88% | - |
| [kiji-en](types/kiji-en.md) | 46 | 46 (100.00%) | 100.00% | 100.00% | small |
| [nemotron-pii](types/nemotron-pii.md) | 229 | 229 (100.00%) | 100.00% | 100.00% | - |
| [nym-en](types/nym-en.md) | 57 | 57 (100.00%) | 100.00% | 100.00% | small |
| [tonicai](types/tonicai.md) | 96 | 32 (33.33%) | 100.00% | 33.33% | small |
| [gretel-multi](types/gretel-multi.md) | 71 | 71 (100.00%) | 100.00% | 100.00% | small |
| [kiji-multi](types/kiji-multi.md) | 55 | 55 (100.00%) | 100.00% | 100.00% | small |
| [nym-multi](types/nym-multi.md) | 192 | 188 (97.92%) | 97.92% | 91.67% | - |

### Bank accounts & cards

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [corrupt-hivetrace](types/corrupt-hivetrace.md) | 169 | 161 (95.27%) | 95.86% | 92.31% | - |
| [corrupt-redmadrobot](types/corrupt-redmadrobot.md) | 203 | 198 (97.54%) | 100.00% | 97.54% | - |
| [hivetrace](types/hivetrace.md) | 169 | 164 (97.04%) | 97.04% | 96.45% | - |
| [nym-ru](types/nym-ru.md) | 596 | 596 (100.00%) | 100.00% | 99.83% | - |
| [redact-ru](types/redact-ru.md) | 65 | 51 (78.46%) | 100.00% | 78.46% | small |
| [redmadrobot](types/redmadrobot.md) | 202 | 201 (99.50%) | 100.00% | 99.01% | - |
| [rubai-ru](types/rubai-ru.md) | 1,054 | 168 (15.94%) | 100.00% | 15.94% | - |
| [russian-pii-66k](types/russian-pii-66k.md) | 448 | 448 (100.00%) | 100.00% | 100.00% | - |
| [kiji-en](types/kiji-en.md) | 153 | 153 (100.00%) | 100.00% | 100.00% | - |
| [nemotron-pii](types/nemotron-pii.md) | 698 | 695 (99.57%) | 99.57% | 99.14% | - |
| [nym-en](types/nym-en.md) | 267 | 265 (99.25%) | 99.25% | 99.25% | - |
| [privy](types/privy.md) | 122 | 122 (100.00%) | 100.00% | 100.00% | - |
| [gretel-multi](types/gretel-multi.md) | 122 | 122 (100.00%) | 100.00% | 100.00% | - |
| [kiji-multi](types/kiji-multi.md) | 215 | 213 (99.07%) | 100.00% | 99.07% | - |
| [nym-multi](types/nym-multi.md) | 632 | 632 (100.00%) | 100.00% | 90.03% | - |
| [redact-multi](types/redact-multi.md) | 138 | 81 (58.70%) | 100.00% | 55.80% | - |

### Documents & identifiers

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [corrupt-hivetrace](types/corrupt-hivetrace.md) | 609 | 600 (98.52%) | 100.00% | 96.39% | - |
| [corrupt-redmadrobot](types/corrupt-redmadrobot.md) | 2,076 | 1,890 (91.04%) | 98.55% | 89.21% | - |
| [hivetrace](types/hivetrace.md) | 609 | 598 (98.19%) | 100.00% | 98.19% | - |
| [nym-ru](types/nym-ru.md) | 1,170 | 1,169 (99.91%) | 100.00% | 99.74% | - |
| [redact-ru](types/redact-ru.md) | 473 | 453 (95.77%) | 100.00% | 95.77% | - |
| [redmadrobot](types/redmadrobot.md) | 2,055 | 1,881 (91.53%) | 98.54% | 90.85% | - |
| [rubai-ru](types/rubai-ru.md) | 268 | 53 (19.78%) | 97.39% | 19.78% | - |
| [russian-pii-66k](types/russian-pii-66k.md) | 784 | 784 (100.00%) | 100.00% | 100.00% | - |
| [scanpatch](types/scanpatch.md) | 655 | 611 (93.28%) | 96.64% | 92.06% | - |
| [dialogpii-en](types/dialogpii-en.md) | 260 | 199 (76.54%) | 87.31% | 75.77% | - |
| [kiji-en](types/kiji-en.md) | 725 | 720 (99.31%) | 99.31% | 99.31% | - |
| [nemotron-pii](types/nemotron-pii.md) | 886 | 885 (99.89%) | 100.00% | 99.89% | - |
| [nym-en](types/nym-en.md) | 338 | 338 (100.00%) | 100.00% | 100.00% | - |
| [privy](types/privy.md) | 276 | 273 (98.91%) | 100.00% | 98.91% | - |
| [tab-echr](types/tab-echr.md) | 334 | 316 (94.61%) | 96.71% | 93.41% | - |
| [dialogpii-multi](types/dialogpii-multi.md) | 818 | 559 (68.34%) | 84.96% | 67.97% | - |
| [gretel-multi](types/gretel-multi.md) | 51 | 51 (100.00%) | 100.00% | 100.00% | small |
| [kiji-multi](types/kiji-multi.md) | 877 | 875 (99.77%) | 99.77% | 99.77% | - |
| [nym-multi](types/nym-multi.md) | 941 | 941 (100.00%) | 100.00% | 92.14% | - |
| [redact-multi](types/redact-multi.md) | 829 | 811 (97.83%) | 99.88% | 96.74% | - |

### People's names

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [alexen2](types/alexen2.md) | 571 | 368 (64.45%) | 99.82% | 64.45% | - |
| [alrosait](types/alrosait.md) | 987 | 987 (100.00%) | 100.00% | 99.90% | - |
| [corrupt-hivetrace](types/corrupt-hivetrace.md) | 228 | 223 (97.81%) | 99.56% | 95.61% | - |
| [corrupt-redmadrobot](types/corrupt-redmadrobot.md) | 1,260 | 1,216 (96.51%) | 98.65% | 94.13% | - |
| [factrueval](types/factrueval.md) | 3,369 | 3,353 (99.53%) | 99.55% | 98.49% | - |
| [hivetrace](types/hivetrace.md) | 228 | 228 (100.00%) | 100.00% | 100.00% | - |
| [jayguard](types/jayguard.md) | 806 | 605 (75.06%) | 89.95% | 75.06% | - |
| [multiconer-ru](types/multiconer-ru.md) | 305 | 244 (80.00%) | 99.02% | 79.34% | - |
| [nerel](types/nerel.md) | 9,496 | 9,430 (99.30%) | 99.51% | 97.42% | - |
| [nym-ru](types/nym-ru.md) | 2,036 | 2,036 (100.00%) | 100.00% | 99.85% | - |
| [redact-ru](types/redact-ru.md) | 3,854 | 3,847 (99.82%) | 100.00% | 99.20% | - |
| [redmadrobot](types/redmadrobot.md) | 1,260 | 1,240 (98.41%) | 99.76% | 98.33% | - |
| [rubai-ru](types/rubai-ru.md) | 430 | 147 (34.19%) | 99.77% | 34.19% | - |
| [russian-pii-66k](types/russian-pii-66k.md) | 1,151 | 1,151 (100.00%) | 100.00% | 99.91% | - |
| [scanpatch](types/scanpatch.md) | 3,798 | 3,791 (99.82%) | 99.95% | 99.68% | - |
| [synth-jira-comments](types/synth-jira-comments.md) | 566 | 566 (100.00%) | 100.00% | 100.00% | - |
| [synth-ru-tickets](types/synth-ru-tickets.md) | 1,992 | 1,992 (100.00%) | 100.00% | 100.00% | - |
| [synth-wiki-tables](types/synth-wiki-tables.md) | 1,597 | 1,597 (100.00%) | 100.00% | 100.00% | - |
| [ameau01](types/ameau01.md) | 382 | 381 (99.74%) | 100.00% | 99.74% | - |
| [dialogpii-en](types/dialogpii-en.md) | 1,558 | 1,489 (95.57%) | 98.14% | 95.57% | - |
| [kiji-en](types/kiji-en.md) | 1,926 | 1,925 (99.95%) | 100.00% | 99.95% | - |
| [nemotron-pii](types/nemotron-pii.md) | 2,245 | 2,242 (99.87%) | 99.91% | 99.82% | - |
| [nym-en](types/nym-en.md) | 820 | 816 (99.51%) | 99.76% | 99.39% | - |
| [privy](types/privy.md) | 428 | 427 (99.77%) | 99.77% | 99.30% | - |
| [tab-echr](types/tab-echr.md) | 1,030 | 842 (81.75%) | 99.61% | 82.23% | - |
| [tonicai](types/tonicai.md) | 1,530 | 1,526 (99.74%) | 99.74% | 99.61% | - |
| [dialogpii-multi](types/dialogpii-multi.md) | 5,083 | 4,819 (94.81%) | 97.66% | 94.71% | - |
| [gretel-multi](types/gretel-multi.md) | 2,258 | 1,805 (79.94%) | 82.46% | 79.81% | - |
| [kiji-multi](types/kiji-multi.md) | 1,866 | 1,852 (99.25%) | 99.41% | 99.25% | - |
| [nym-multi](types/nym-multi.md) | 1,806 | 1,797 (99.50%) | 99.56% | 91.64% | - |
| [redact-multi](types/redact-multi.md) | 10,870 | 10,776 (99.14%) | 99.87% | 97.24% | - |

### Phone numbers & email

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [alexen2](types/alexen2.md) | 690 | 439 (63.62%) | 100.00% | 63.62% | - |
| [corrupt-hivetrace](types/corrupt-hivetrace.md) | 390 | 388 (99.49%) | 100.00% | 98.97% | - |
| [corrupt-redmadrobot](types/corrupt-redmadrobot.md) | 389 | 359 (92.29%) | 100.00% | 91.52% | - |
| [hivetrace](types/hivetrace.md) | 390 | 390 (100.00%) | 100.00% | 100.00% | - |
| [nym-ru](types/nym-ru.md) | 962 | 962 (100.00%) | 100.00% | 99.58% | - |
| [redact-ru](types/redact-ru.md) | 1,199 | 1,172 (97.75%) | 100.00% | 97.66% | - |
| [redmadrobot](types/redmadrobot.md) | 389 | 369 (94.86%) | 100.00% | 94.86% | - |
| [rubai-ru](types/rubai-ru.md) | 205 | 70 (34.15%) | 100.00% | 34.15% | - |
| [russian-pii-66k](types/russian-pii-66k.md) | 793 | 793 (100.00%) | 100.00% | 100.00% | - |
| [scanpatch](types/scanpatch.md) | 588 | 585 (99.49%) | 99.66% | 99.32% | - |
| [synth-jira-comments](types/synth-jira-comments.md) | 442 | 442 (100.00%) | 100.00% | 100.00% | - |
| [synth-ru-tickets](types/synth-ru-tickets.md) | 3,149 | 3,149 (100.00%) | 100.00% | 100.00% | - |
| [synth-wiki-tables](types/synth-wiki-tables.md) | 4,791 | 4,791 (100.00%) | 100.00% | 100.00% | - |
| [ameau01](types/ameau01.md) | 141 | 141 (100.00%) | 100.00% | 100.00% | - |
| [dialogpii-en](types/dialogpii-en.md) | 200 | 141 (70.50%) | 90.50% | 70.50% | - |
| [kiji-en](types/kiji-en.md) | 484 | 484 (100.00%) | 100.00% | 100.00% | - |
| [nemotron-pii](types/nemotron-pii.md) | 1,199 | 1,192 (99.42%) | 99.83% | 99.42% | - |
| [nym-en](types/nym-en.md) | 403 | 401 (99.50%) | 100.00% | 99.50% | - |
| [privy](types/privy.md) | 87 | 87 (100.00%) | 100.00% | 100.00% | small |
| [tonicai](types/tonicai.md) | 365 | 365 (100.00%) | 100.00% | 100.00% | - |
| [dialogpii-multi](types/dialogpii-multi.md) | 750 | 539 (71.87%) | 87.20% | 70.67% | - |
| [gretel-multi](types/gretel-multi.md) | 332 | 325 (97.89%) | 99.70% | 97.89% | - |
| [kiji-multi](types/kiji-multi.md) | 259 | 259 (100.00%) | 100.00% | 100.00% | - |
| [nym-multi](types/nym-multi.md) | 860 | 859 (99.88%) | 100.00% | 90.47% | - |
| [redact-multi](types/redact-multi.md) | 2,524 | 2,489 (98.61%) | 100.00% | 97.78% | - |

### Addresses & locations

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [alrosait](types/alrosait.md) | 875 | 842 (96.23%) | 99.89% | 96.34% | - |
| [corrupt-hivetrace](types/corrupt-hivetrace.md) | 176 | 172 (97.73%) | 100.00% | 95.45% | - |
| [corrupt-redmadrobot](types/corrupt-redmadrobot.md) | 1,242 | 1,148 (92.43%) | 97.18% | 90.98% | - |
| [factrueval](types/factrueval.md) | 2,396 | 2,359 (98.46%) | 98.83% | 97.95% | - |
| [hivetrace](types/hivetrace.md) | 176 | 174 (98.86%) | 100.00% | 96.59% | - |
| [jayguard](types/jayguard.md) | 389 | 376 (96.66%) | 99.23% | 96.66% | - |
| [multiconer-ru](types/multiconer-ru.md) | 379 | 294 (77.57%) | 92.61% | 76.52% | - |
| [nerel](types/nerel.md) | 8,861 | 7,989 (90.16%) | 92.75% | 88.66% | - |
| [nym-ru](types/nym-ru.md) | 1,316 | 1,286 (97.72%) | 100.00% | 97.34% | - |
| [redact-ru](types/redact-ru.md) | 835 | 796 (95.33%) | 99.76% | 95.21% | - |
| [redmadrobot](types/redmadrobot.md) | 1,249 | 1,206 (96.56%) | 99.52% | 95.76% | - |
| [rubai-ru](types/rubai-ru.md) | 1,501 | 469 (31.25%) | 100.00% | 31.25% | - |
| [russian-pii-66k](types/russian-pii-66k.md) | 901 | 866 (96.12%) | 100.00% | 95.89% | - |
| [scanpatch](types/scanpatch.md) | 1,637 | 1,505 (91.94%) | 99.08% | 91.51% | - |
| [synth-ru-tickets](types/synth-ru-tickets.md) | 386 | 385 (99.74%) | 100.00% | 99.74% | - |
| [ameau01](types/ameau01.md) | 184 | 183 (99.46%) | 99.46% | 98.91% | - |
| [dialogpii-en](types/dialogpii-en.md) | 483 | 458 (94.82%) | 96.07% | 94.82% | - |
| [kiji-en](types/kiji-en.md) | 3,541 | 3,540 (99.97%) | 99.97% | 99.94% | - |
| [nemotron-pii](types/nemotron-pii.md) | 1,468 | 1,447 (98.57%) | 99.59% | 98.57% | - |
| [nym-en](types/nym-en.md) | 692 | 687 (99.28%) | 99.57% | 99.13% | - |
| [privy](types/privy.md) | 699 | 689 (98.57%) | 99.00% | 97.57% | - |
| [tab-echr](types/tab-echr.md) | 516 | 480 (93.02%) | 99.61% | 93.02% | - |
| [dialogpii-multi](types/dialogpii-multi.md) | 1,868 | 1,682 (90.04%) | 93.68% | 87.96% | - |
| [gretel-multi](types/gretel-multi.md) | 624 | 619 (99.20%) | 99.52% | 98.56% | - |
| [kiji-multi](types/kiji-multi.md) | 3,612 | 3,608 (99.89%) | 99.94% | 99.86% | - |
| [nym-multi](types/nym-multi.md) | 1,489 | 1,479 (99.33%) | 99.80% | 93.75% | - |
| [redact-multi](types/redact-multi.md) | 2,107 | 2,027 (96.20%) | 99.67% | 93.36% | - |

### Dates & times

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [nym-ru](types/nym-ru.md) | 1,440 | 1,439 (99.93%) | 100.00% | 99.65% | - |
| [redact-ru](types/redact-ru.md) | 324 | 323 (99.69%) | 100.00% | 99.69% | - |
| [russian-pii-66k](types/russian-pii-66k.md) | 223 | 223 (100.00%) | 100.00% | 100.00% | - |
| [scanpatch](types/scanpatch.md) | 650 | 561 (86.31%) | 96.00% | 81.54% | - |
| [kiji-en](types/kiji-en.md) | 135 | 135 (100.00%) | 100.00% | 100.00% | - |
| [nemotron-pii](types/nemotron-pii.md) | 277 | 277 (100.00%) | 100.00% | 100.00% | - |
| [nym-en](types/nym-en.md) | 570 | 568 (99.65%) | 100.00% | 99.30% | - |
| [gretel-multi](types/gretel-multi.md) | 20 | 20 (100.00%) | 100.00% | 100.00% | small |
| [kiji-multi](types/kiji-multi.md) | 144 | 144 (100.00%) | 100.00% | 100.00% | - |
| [nym-multi](types/nym-multi.md) | 1,091 | 1,088 (99.73%) | 100.00% | 90.65% | - |
| [redact-multi](types/redact-multi.md) | 628 | 623 (99.20%) | 100.00% | 97.93% | - |

### Organizations

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [factrueval](types/factrueval.md) | 2,201 | 2,099 (95.37%) | 97.05% | 94.68% | - |
| [multiconer-ru](types/multiconer-ru.md) | 524 | 404 (77.10%) | 92.94% | 75.57% | - |
| [nerel](types/nerel.md) | 6,012 | 5,414 (90.05%) | 97.44% | 89.44% | - |
| [nym-ru](types/nym-ru.md) | 454 | 271 (59.69%) | 99.78% | 57.71% | - |
| [redact-ru](types/redact-ru.md) | 366 | 276 (75.41%) | 98.91% | 75.96% | - |
| [scanpatch](types/scanpatch.md) | 277 | 251 (90.61%) | 96.03% | 88.81% | - |
| [synth-ru-tickets](types/synth-ru-tickets.md) | 1,172 | 742 (63.31%) | 99.74% | 62.20% | - |
| [synth-wiki-tables](types/synth-wiki-tables.md) | 300 | 168 (56.00%) | 100.00% | 51.67% | - |
| [dialogpii-en](types/dialogpii-en.md) | 579 | 496 (85.66%) | 93.26% | 85.49% | - |
| [kiji-en](types/kiji-en.md) | 241 | 241 (100.00%) | 100.00% | 100.00% | - |
| [nemotron-pii](types/nemotron-pii.md) | 843 | 837 (99.29%) | 99.88% | 99.05% | - |
| [nym-en](types/nym-en.md) | 170 | 147 (86.47%) | 99.41% | 87.65% | - |
| [privy](types/privy.md) | 79 | 77 (97.47%) | 100.00% | 96.20% | small |
| [tab-echr](types/tab-echr.md) | 1,950 | 1,738 (89.13%) | 98.97% | 88.97% | - |
| [tonicai](types/tonicai.md) | 426 | 357 (83.80%) | 87.09% | 83.80% | - |
| [dialogpii-multi](types/dialogpii-multi.md) | 1,806 | 1,366 (75.64%) | 87.21% | 73.53% | - |
| [gretel-multi](types/gretel-multi.md) | 452 | 391 (86.50%) | 91.37% | 86.28% | - |
| [kiji-multi](types/kiji-multi.md) | 149 | 149 (100.00%) | 100.00% | 100.00% | - |
| [nym-multi](types/nym-multi.md) | 256 | 239 (93.36%) | 100.00% | 85.94% | - |
| [redact-multi](types/redact-multi.md) | 1,017 | 987 (97.05%) | 99.90% | 94.30% | - |

### Network identifiers

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [corrupt-redmadrobot](types/corrupt-redmadrobot.md) | 361 | 257 (71.19%) | 98.06% | 68.98% | - |
| [nym-ru](types/nym-ru.md) | 194 | 168 (86.60%) | 100.00% | 86.60% | - |
| [redact-ru](types/redact-ru.md) | 54 | 51 (94.44%) | 100.00% | 94.44% | small |
| [redmadrobot](types/redmadrobot.md) | 361 | 283 (78.39%) | 98.61% | 77.84% | - |
| [scanpatch](types/scanpatch.md) | 1,103 | 1,063 (96.37%) | 99.64% | 96.10% | - |
| [synth-jira-comments](types/synth-jira-comments.md) | 1,132 | 1,129 (99.73%) | 100.00% | 99.73% | - |
| [synth-ru-tickets](types/synth-ru-tickets.md) | 16,675 | 16,674 (99.99%) | 100.00% | 99.99% | - |
| [synth-wiki-tables](types/synth-wiki-tables.md) | 3,212 | 3,092 (96.26%) | 98.91% | 96.26% | - |
| [ameau01](types/ameau01.md) | 777 | 749 (96.40%) | 99.36% | 95.37% | - |
| [dialogpii-en](types/dialogpii-en.md) | 7 | 6 (85.71%) | 100.00% | 85.71% | small |
| [kiji-en](types/kiji-en.md) | 161 | 156 (96.89%) | 100.00% | 96.27% | - |
| [nemotron-pii](types/nemotron-pii.md) | 762 | 709 (93.04%) | 100.00% | 92.39% | - |
| [nym-en](types/nym-en.md) | 15 | 13 (86.67%) | 100.00% | 86.67% | small |
| [privy](types/privy.md) | 178 | 165 (92.70%) | 98.88% | 92.70% | - |
| [dialogpii-multi](types/dialogpii-multi.md) | 20 | 6 (30.00%) | 100.00% | 30.00% | small |
| [gretel-multi](types/gretel-multi.md) | 276 | 274 (99.28%) | 99.64% | 99.28% | - |
| [kiji-multi](types/kiji-multi.md) | 133 | 132 (99.25%) | 100.00% | 99.25% | - |
| [nym-multi](types/nym-multi.md) | 99 | 92 (92.93%) | 100.00% | 77.78% | small |
| [redact-multi](types/redact-multi.md) | 111 | 110 (99.10%) | 100.00% | 96.40% | - |

### Customer & employee IDs

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [nym-ru](types/nym-ru.md) | 483 | 483 (100.00%) | 100.00% | 99.59% | - |
| [redact-ru](types/redact-ru.md) | 1,160 | 1,132 (97.59%) | 100.00% | 97.24% | - |
| [synth-ru-tickets](types/synth-ru-tickets.md) | 796 | 555 (69.72%) | 100.00% | 69.47% | - |
| [synth-wiki-tables](types/synth-wiki-tables.md) | 1,597 | 1,268 (79.40%) | 100.00% | 79.40% | - |
| [ameau01](types/ameau01.md) | 131 | 131 (100.00%) | 100.00% | 100.00% | - |
| [nemotron-pii](types/nemotron-pii.md) | 409 | 409 (100.00%) | 100.00% | 100.00% | - |
| [nym-en](types/nym-en.md) | 195 | 194 (99.49%) | 100.00% | 99.49% | - |
| [gretel-multi](types/gretel-multi.md) | 61 | 61 (100.00%) | 100.00% | 100.00% | small |
| [nym-multi](types/nym-multi.md) | 493 | 493 (100.00%) | 100.00% | 91.48% | - |
| [redact-multi](types/redact-multi.md) | 2,669 | 2,626 (98.39%) | 99.96% | 96.97% | - |

### Other sensitive attributes

| Dataset | Gold spans | Fully hidden | Detected | Raw full hiding | Sample |
|---|---:|---:|---:|---:|---|
| [nym-ru](types/nym-ru.md) | 224 | 223 (99.55%) | 99.55% | 98.66% | - |
| [redact-ru](types/redact-ru.md) | 889 | 636 (71.54%) | 86.39% | 67.49% | - |
| [nym-en](types/nym-en.md) | 18 | 18 (100.00%) | 100.00% | 100.00% | small |
| [nym-multi](types/nym-multi.md) | 137 | 131 (95.62%) | 95.62% | 85.40% | - |
| [redact-multi](types/redact-multi.md) | 1,939 | 1,332 (68.70%) | 86.38% | 63.28% | - |

## All detectors, configurations and original labels

[category-metrics.csv](category-metrics.csv) contains exact category counts for every measured configuration and the seven recomputed compositions. [entity-metrics.csv](entity-metrics.csv) retains the original source labels. [dataset-metrics.csv](dataset-metrics.csv) adds exact character precision/recall/F1 and document residuals. Training-source rows are marked and excluded from pooled results. Missing runs have no fabricated rows.

[Metric and taxonomy contract](../docs/metrics.md) · [Dataset effects](by-dataset.md) · [Methods compared with other projects](../docs/comparison.md)
