# Dataset catalog

41 datasets, 41,643 rows, 230,446 original annotations; scoring normalization leaves 227,466 gold spans. Raw texts and annotations are stored only in the ignored local workspace. Public metadata, source links, row-selection IDs, checksums and aggregate results remain available.

The `synthetic` flag in the machine-readable catalog identifies only this project's six `synth-*` datasets; other sources also contain synthetic material. Corrupted copies inherit their source and training-overlap exclusions. License labels describe the archived 2026-09-05 source audit, not a fresh legal review.

| Dataset | Language | Task | Rows | Normalized spans | Source license | Report |
|---|---|---|---:|---:|---|---|
| [alexen2](https://huggingface.co/datasets/alexen2/pii-ner-ru-benchmark) | ru | pii | 911 | 1,261 | not specified | [Results](../results/datasets/alexen2.md) |
| [alrosait](https://huggingface.co/datasets/alrosait/pii-synthetic-ru) | ru | pii | 1,500 | 1,862 | mit | [Results](../results/datasets/alrosait.md) |
| [ameau01](https://huggingface.co/datasets/ameau01/synthetic-it-support-tickets) | en | pii | 1,452 | 2,242 | mit | [Results](../results/datasets/ameau01.md) |
| [arthur-passwords](https://huggingface.co/datasets/Arthur-AI/arthur_sensitive_data_password) | en | secrets | 516 | 280 | apache-2.0 | [Results](../results/datasets/arthur-passwords.md) |
| [corrupt-hivetrace](https://huggingface.co/datasets/hivetrace/pii-bench) | ru | pii | 1,810 | 1,667 | apache-2.0 | [Results](../results/datasets/corrupt-hivetrace.md) |
| [corrupt-redmadrobot](https://huggingface.co/datasets/redmadrobot-rnd/pii_benchmark) | ru | pii | 2,841 | 5,531 | mit | [Results](../results/datasets/corrupt-redmadrobot.md) |
| [corrupt-secrets-issues](https://zenodo.org/records/19622962) | en | secrets | 500 | 288 | cc-by-4.0 | [Results](../results/datasets/corrupt-secrets-issues.md) |
| [creddata](https://github.com/Samsung/CredData) | en | secrets | 1,477 | 776 | apache-2.0 (meta); file texts under their repositories' licenses | [Results](../results/datasets/creddata.md) |
| [dialogpii-en](https://zenodo.org/records/20863452) | en | pii | 147 | 3,087 | cc-by-4.0 | [Results](../results/datasets/dialogpii-en.md) |
| [dialogpii-multi](https://zenodo.org/records/20863452) | multi | pii | 500 | 10,345 | cc-by-4.0 | [Results](../results/datasets/dialogpii-multi.md) |
| [factrueval](https://github.com/dialogue-evaluation/factRuEval-2016) | ru | pii | 254 | 7,966 | mit | [Results](../results/datasets/factrueval.md) |
| [gretel-multi](https://huggingface.co/datasets/gretelai/synthetic_pii_finance_multilingual) | multi | pii | 697 | 4,484 | apache-2.0 | [Results](../results/datasets/gretel-multi.md) |
| [hivetrace](https://huggingface.co/datasets/hivetrace/pii-bench) | ru | pii | 1,810 | 1,667 | apache-2.0 | [Results](../results/datasets/hivetrace.md) |
| [jayguard](https://huggingface.co/datasets/just-ai/jayguard-ner-benchmark) | ru | pii | 850 | 1,195 | mit (yaml) / apache-2.0 (card text) | [Results](../results/datasets/jayguard.md) |
| [kiji-en](https://huggingface.co/datasets/DataikuNLP/kiji-pii-training-data) | en | pii | 1,000 | 7,623 | apache-2.0 | [Results](../results/datasets/kiji-en.md) |
| [kiji-multi](https://huggingface.co/datasets/DataikuNLP/kiji-pii-training-data) | multi | pii | 1,000 | 7,565 | apache-2.0 | [Results](../results/datasets/kiji-multi.md) |
| [leak-museum](https://github.com/printemps-tokyo/leak-museum) | en | secrets | 97 | 101 | mit | [Results](../results/datasets/leak-museum.md) |
| [leaky-repo](https://github.com/Plazmaz/leaky-repo) | en | secrets | 59 | 95 | mit | [Results](../results/datasets/leaky-repo.md) |
| [multiconer-ru](https://huggingface.co/datasets/tomaarsen/MultiCoNER) | ru | pii | 1,500 | 1,208 | cc-by-4.0 | [Results](../results/datasets/multiconer-ru.md) |
| [nemotron-pii](https://huggingface.co/datasets/nvidia/Nemotron-PII) | en | pii | 1,491 | 9,391 | cc-by-4.0 | [Results](../results/datasets/nemotron-pii.md) |
| [nerel](https://huggingface.co/datasets/iluvvatar/NEREL) | ru | pii | 933 | 24,369 | not specified | [Results](../results/datasets/nerel.md) |
| [nym-en](https://huggingface.co/datasets/Wismut/nym-pii-multilingual-data) | en | pii | 734 | 3,584 | mit | [Results](../results/datasets/nym-en.md) |
| [nym-multi](https://huggingface.co/datasets/Wismut/nym-pii-multilingual-data) | multi | pii | 1,500 | 8,169 | mit | [Results](../results/datasets/nym-multi.md) |
| [nym-ru](https://huggingface.co/datasets/Wismut/nym-pii-multilingual-data) | ru | pii | 1,500 | 9,497 | mit | [Results](../results/datasets/nym-ru.md) |
| [privy](https://huggingface.co/datasets/beki/privy) | en | pii | 1,500 | 1,899 | mit | [Results](../results/datasets/privy.md) |
| [redact-multi](https://huggingface.co/datasets/guneeshv/REDACT-PII-Benchmark) | multi | pii | 1,000 | 22,864 | other (gated, terms accepted) | [Results](../results/datasets/redact-multi.md) |
| [redact-ru](https://huggingface.co/datasets/guneeshv/REDACT-PII-Benchmark) | ru | pii | 500 | 9,230 | other (gated, terms accepted) | [Results](../results/datasets/redact-ru.md) |
| [redmadrobot](https://huggingface.co/datasets/redmadrobot-rnd/pii_benchmark) | ru | pii | 2,841 | 5,516 | mit | [Results](../results/datasets/redmadrobot.md) |
| [rubai-ru](https://huggingface.co/datasets/islomov/rubai-NER-150K-Personal) | ru | pii | 1,500 | 3,458 | apache-2.0 | [Results](../results/datasets/rubai-ru.md) |
| [russian-pii-66k](https://huggingface.co/datasets/wolframko/russian-pii-66k) | ru | pii | 1,500 | 4,805 | not specified | [Results](../results/datasets/russian-pii-66k.md) |
| [scanpatch](https://huggingface.co/datasets/scanpatch/pii-ner-corpus-synthetic-controlled) | ru | pii | 1,500 | 8,708 | mit | [Results](../results/datasets/scanpatch.md) |
| [secrets-issues](https://zenodo.org/records/19622962) | en | secrets | 500 | 288 | cc-by-4.0 | [Results](../results/datasets/secrets-issues.md) |
| secrets-rules ([gitleaks](https://github.com/gitleaks/gitleaks) + [betterleaks](https://github.com/betterleaks/betterleaks); rule test cases) | en | secrets | 1,496 | 746 | mit | [Results](../results/datasets/secrets-rules.md) |
| synth-env-configs | en | secrets | 400 | 392 | cc-by-4.0 | [Results](../results/datasets/synth-env-configs.md) |
| synth-jira-comments | ru | pii | 300 | 2,705 | cc-by-4.0 | [Results](../results/datasets/synth-jira-comments.md) |
| synth-ru-tickets | ru | pii | 400 | 32,099 | cc-by-4.0 | [Results](../results/datasets/synth-ru-tickets.md) |
| synth-secrets-en | en | secrets | 600 | 581 | cc-by-4.0 | [Results](../results/datasets/synth-secrets-en.md) |
| synth-secrets-ru | ru | secrets | 600 | 581 | cc-by-4.0 | [Results](../results/datasets/synth-secrets-ru.md) |
| synth-wiki-tables | ru | pii | 300 | 13,094 | cc-by-4.0 | [Results](../results/datasets/synth-wiki-tables.md) |
| [tab-echr](https://huggingface.co/datasets/ildpil/text-anonymization-benchmark) | en | pii | 127 | 3,830 | mit | [Results](../results/datasets/tab-echr.md) |
| [tonicai](https://huggingface.co/datasets/TonicAI/Privacy-Bench) | en | pii | 1,500 | 2,417 | cc-by-4.0 | [Results](../results/datasets/tonicai.md) |

## Reconstruction status

The public Leak Museum route is tested from source download through CPU inference and scoring. The following 22 historical cuts have no retained raw-source revision and cannot be reconstructed exactly from an upstream revision alone:

`alexen2`, `alrosait`, `ameau01`, `corrupt-hivetrace`, `corrupt-redmadrobot`, `corrupt-secrets-issues`, `gretel-multi`, `hivetrace`, `jayguard`, `nerel`, `nym-en`, `nym-multi`, `nym-ru`, `redmadrobot`, `russian-pii-66k`, `scanpatch`, `synth-env-configs`, `synth-jira-comments`, `synth-ru-tickets`, `synth-secrets-en`, `synth-secrets-ru`, `synth-wiki-tables`.

A retained aggregate raw hash identifies the archived bytes where available but does not make a newer upstream download equivalent. Other dependency and acquisition gaps are documented in [source acquisition](sources.md).

See [source acquisition and conversion caveats](sources.md), [license notices](../LICENSES/README.md), [catalog.json](../datasets/catalog.json) and [samples.json](../datasets/samples.json). A source publication mode of `files` in archived metadata describes the original experiment; this repository distributes no corpus text.
