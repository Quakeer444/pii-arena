# Detector catalog

62 execution records: 50 model configurations (40 distinct weights, eight Russian-label variants, two mirrors), ten secret-scanner configurations, one rules layer and Presidio. A catalog entry does not imply a completed run. The `cpu` catalog flag controls the planned CPU sweep, not a universal capability claim.

| Record | Family | Upstream | Pinned revision/version | Flags |
|---|---|---|---|---|
| opf-ru | opf | [bbeglerov/opf-russian-pii-66k](https://huggingface.co/bbeglerov/opf-russian-pii-66k) | `ae813a5aaeb31def75e87064818f0b1fbc65e31f` | source overlap: russian-pii-66k |
| opf-ru-v2 | opf | [pii-anon/opf-ru-v2](https://huggingface.co/pii-anon/opf-ru-v2) | `7975e895ed59a7c58e9ab2dbb7d739fd246086b4` | - |
| traciora | opf | [dzanozin/traciora-opf-ru-pii-v6](https://huggingface.co/dzanozin/traciora-opf-ru-pii-v6) | `ea69da97d598b662ec447bcb8e0022abee0f4010` | - |
| apararti | opf | [apararti/privacy-filter-ru](https://huggingface.co/apararti/privacy-filter-ru) | `a1650a1927ed8aceb9e15fa8ed13ffdf60cbf107` | - |
| openai-base | opf | [openai/privacy-filter](https://huggingface.co/openai/privacy-filter) | `7ffa9a043d54d1be65afb281eddf0ffbe629385b` | - |
| pplx | pplx | [perplexity-ai/pplx-pii-masking](https://huggingface.co/perplexity-ai/pplx-pii-masking) | `f1f90a53823f5df0a1344c1e137d9fffdaab54d6` | - |
| openmed-multilingual | hf | [OpenMed/privacy-filter-multilingual-v2](https://huggingface.co/OpenMed/privacy-filter-multilingual-v2) | `0d0c0430fa386435ace1d9f842f0f966903a9ac8` | source overlap: nemotron-pii, gretel-multi, privy |
| openmed-nemotron | hf | [OpenMed/privacy-filter-nemotron](https://huggingface.co/OpenMed/privacy-filter-nemotron) | `f6f3a633dc6fc96a644d20218633a98ac43f6c71` | source overlap: nemotron-pii |
| gliner-nvidia | gliner | [nvidia/gliner-PII](https://huggingface.co/nvidia/gliner-PII) | `bd23e8ef4425fd04e34c5204ab49ffaa706eae79` | source overlap: nemotron-pii |
| gliner-urchade | gliner | [urchade/gliner_multi_pii-v1](https://huggingface.co/urchade/gliner_multi_pii-v1) | `1fcf13e85f4eef5394e1fcd406cf2ca9ea82351d` | - |
| gliner2-fastino | gliner2 | [fastino/gliner2-privacy-filter-PII-multi](https://huggingface.co/fastino/gliner2-privacy-filter-PII-multi) | `c153999da5f4c509df4322b0c6a1baf3d2c284d7` | - |
| gliner2-hivetrace-omni | gliner2 | [hivetrace/gliner-guard-omni](https://huggingface.co/hivetrace/gliner-guard-omni) | `763f8aa9a7714dd2c3264f3751acdd5d854c5ac4` | source overlap: nemotron-pii, gretel-multi |
| gliner2-hivetrace-uni | gliner2 | [hivetrace/gliner-guard-uniencoder](https://huggingface.co/hivetrace/gliner-guard-uniencoder) | `5644cdb7c953463fa3a370e76617c03c2dd29f92` | source overlap: nemotron-pii, gretel-multi |
| gliner2-vladlinv | gliner2 | [vladlinv/ru-pii-ner-gliner2.5](https://huggingface.co/vladlinv/ru-pii-ner-gliner2.5) | `d4c05667b10d8e8db0f0626934135731d0530983` | - |
| ru-pii-ner | rupii | [vladlinv/ru-pii-ner](https://huggingface.co/vladlinv/ru-pii-ner) | `3b509ebbcec894e522adef32560644017832deea` | - |
| ru-legal-ner | hf | [LLAIMlegal/ru-legal-ner](https://huggingface.co/LLAIMlegal/ru-legal-ner) | `c0313a42ac147ccc38f5c3b0b3e77cab53208683` | - |
| pii-shield-onnx | onnx | [astifer/pii-shield-onnx](https://huggingface.co/astifer/pii-shield-onnx) | `280f050f10a73db88fa9b864e8ca25350e73941e` | - |
| davlan-xlmr | hf | [Davlan/xlm-roberta-base-ner-hrl](https://huggingface.co/Davlan/xlm-roberta-base-ner-hrl) | `253f557bd8249b8515114cfd7f71974fe5fa4d2f` | - |
| davlan-mbert | hf | [Davlan/bert-base-multilingual-cased-ner-hrl](https://huggingface.co/Davlan/bert-base-multilingual-cased-ner-hrl) | `e756de7f7b8f64fea0c3d7c3872f1322fab747b1` | - |
| ner-ru-gherman | hf | [Gherman/bert-base-NER-Russian](https://huggingface.co/Gherman/bert-base-NER-Russian) | `fc6b2c5a2c5d7c82da7416f7fd9c055159bbb984` | - |
| ner-ru-gherman-onnx | onnx | [onnx-community/bert-base-NER-Russian-ONNX](https://huggingface.co/onnx-community/bert-base-NER-Russian-ONNX) | `2bd219a78a06657c59fa8c2540ccbad703972e7c` | mirror of ner-ru-gherman |
| ner-ru-yqelz | hf | [yqelz/xml-roberta-large-ner-russian](https://huggingface.co/yqelz/xml-roberta-large-ner-russian) | `4e03a3a079f5bfdb678eb9ee01235e25a7aef5f6` | - |
| fef2-secret-ru | hf | [fef2/ner_rus_bert-secret_detection](https://huggingface.co/fef2/ner_rus_bert-secret_detection) | `52b5b0745aac14f73fcf2ac0f91d9b5001a85ae4` | - |
| nym-base | hf | [Wismut/nym-pii-multilingual](https://huggingface.co/Wismut/nym-pii-multilingual) | `0ed0242d67a30ca6a83e5f118506ff1e1daf83ca` | source overlap: nym-ru, nym-en, nym-multi |
| nym-small | onnx | [Wismut/nym-pii-multilingual-small](https://huggingface.co/Wismut/nym-pii-multilingual-small) | `4348999cd3c2e20c49615e9af7c6bbb45b64cd85` | source overlap: nym-ru, nym-en, nym-multi |
| kalyan-ettin | hf | [kalyan-ks/ettin-68m-nemotron-pii](https://huggingface.co/kalyan-ks/ettin-68m-nemotron-pii) | `500262a2aaf913825ef750ef255c3fe437cd8e64` | source overlap: nemotron-pii |
| gravitee-small | hf | [gravitee-io/bert-small-pii-detection](https://huggingface.co/gravitee-io/bert-small-pii-detection) | `f8c27a85c51c0168f07b9dcf00265bf0a4097939` | - |
| bardsai-eu | onnx | [bardsai/eu-pii-anonimization-multilang](https://huggingface.co/bardsai/eu-pii-anonimization-multilang) | `0e72e19f030ed4e661b1673e549af8e0dd176386` | - |
| mmbert32k | hf | [llm-semantic-router/mmbert32k-pii-detector-merged](https://huggingface.co/llm-semantic-router/mmbert32k-pii-detector-merged) | `d22c818cf9f2a8bfbbed8508cb417dc16a1ba3ea` | - |
| openai-base-onnx | onnx | [RedHatAI/privacy-filter](https://huggingface.co/RedHatAI/privacy-filter) | `9b7e2f5c794da2c156bd9583bf8e2f5f6bdfd18b` | mirror of openai-base |
| gliner-multi-v21 | gliner | [urchade/gliner_multi-v2.1](https://huggingface.co/urchade/gliner_multi-v2.1) | `443d26d654e0324125a96bebd8e796c14ff2efe6` | - |
| gliner-multi-v21-ru | gliner | [urchade/gliner_multi-v2.1](https://huggingface.co/urchade/gliner_multi-v2.1) | `443d26d654e0324125a96bebd8e796c14ff2efe6` | Russian labels |
| gliner-pii-edge | gliner | [knowledgator/gliner-pii-edge-v1.0](https://huggingface.co/knowledgator/gliner-pii-edge-v1.0) | `9b7f39b0a2da971a5beea78d35f1539d4009c891` | - |
| gliner-pii-base | gliner | [knowledgator/gliner-pii-base-v1.0](https://huggingface.co/knowledgator/gliner-pii-base-v1.0) | `61726e0ad791dcab3e29339bbec3ad42ded65641` | - |
| gliner-stream-pii | gliner | [knowledgator/gliner-stream-pii-v1.0](https://huggingface.co/knowledgator/gliner-stream-pii-v1.0) | `e871777dc4b3b688747a0433fff8d94a36fcc7b0` | disputed scope |
| nuner-zero | gliner | [numind/NuNER_Zero](https://huggingface.co/numind/NuNER_Zero) | `c90187673f464518dca09f41689184ed6976242c` | - |
| gliner2-large | gliner2 | [fastino/gliner2-large-v1](https://huggingface.co/fastino/gliner2-large-v1) | `6a498b5a28ec3908bbc5277aeb47d22bcfc02f33` | - |
| gliner25-fastino | gliner2 | [fastino/gliner2.5-multi-v1](https://huggingface.co/fastino/gliner2.5-multi-v1) | `aaecfe45db1d828c963717054ccb868e8ad1f1d5` | - |
| gliner25-fastino-ru | gliner2 | [fastino/gliner2.5-multi-v1](https://huggingface.co/fastino/gliner2.5-multi-v1) | `aaecfe45db1d828c963717054ccb868e8ad1f1d5` | Russian labels |
| gliner-nvidia-ru | gliner | [nvidia/gliner-PII](https://huggingface.co/nvidia/gliner-PII) | `bd23e8ef4425fd04e34c5204ab49ffaa706eae79` | Russian labels; source overlap: nemotron-pii |
| gliner-urchade-ru | gliner | [urchade/gliner_multi_pii-v1](https://huggingface.co/urchade/gliner_multi_pii-v1) | `1fcf13e85f4eef5394e1fcd406cf2ca9ea82351d` | Russian labels |
| gliner2-fastino-ru | gliner2 | [fastino/gliner2-privacy-filter-PII-multi](https://huggingface.co/fastino/gliner2-privacy-filter-PII-multi) | `c153999da5f4c509df4322b0c6a1baf3d2c284d7` | Russian labels |
| gliner2-hivetrace-omni-ru | gliner2 | [hivetrace/gliner-guard-omni](https://huggingface.co/hivetrace/gliner-guard-omni) | `763f8aa9a7714dd2c3264f3751acdd5d854c5ac4` | Russian labels; source overlap: nemotron-pii, gretel-multi |
| gliner2-hivetrace-uni-ru | gliner2 | [hivetrace/gliner-guard-uniencoder](https://huggingface.co/hivetrace/gliner-guard-uniencoder) | `5644cdb7c953463fa3a370e76617c03c2dd29f92` | Russian labels; source overlap: nemotron-pii, gretel-multi |
| gliner2-vladlinv-ru | gliner2 | [vladlinv/ru-pii-ner-gliner2.5](https://huggingface.co/vladlinv/ru-pii-ner-gliner2.5) | `d4c05667b10d8e8db0f0626934135731d0530983` | Russian labels |
| opf-kz-ru | opf | [QOSIkz/kz-privacy-filter-v1](https://huggingface.co/QOSIkz/kz-privacy-filter-v1) | `b804356ff8ac827fe2b046e8d3d0be2720c6b148` | - |
| natasha | natasha | natasha | `1.6.0` | - |
| spacy-ru-lg | spacy | [spacy/ru_core_news_lg](https://huggingface.co/spacy/ru_core_news_lg) | `fa0b3a0086b7b0d6a424d999ce25480bd67dd455` | - |
| spacy-alrosait | spacy | [alrosait/spacy_ru_core_news_lg_pii](https://huggingface.co/alrosait/spacy_ru_core_news_lg_pii) | `8e0d9e49ae62dcb0772f8d8599ed3ffe28d43d7d` | source overlap: scanpatch, alrosait |
| stanza-ru | stanza | [stanfordnlp/stanza-ru](https://huggingface.co/stanfordnlp/stanza-ru) | `dcbf023decb5a319fff84780779052ed974b9013` | - |
| gitleaks | leaks | [github.com/gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | `8.30.1` | source overlap: secrets-rules |
| betterleaks | leaks | [github.com/betterleaks/betterleaks](https://github.com/betterleaks/betterleaks) | `95237cf` | source overlap: secrets-rules |
| rules-ru | rules | benchmark/rules_ru.py | `1.0` | - |
| presidio-ru | presidio | github.com/microsoft/presidio + github.com/brikkoAI/presidio-ru-recognizers | `presidio-analyzer 2.2.364, presidio-ru-recognizers 0.1.0, ru_core_news_sm 3.8.0` | - |
| trufflehog | leaks | [github.com/trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | `3.97.4` | - |
| detect-secrets | leaks | [github.com/Yelp/detect-secrets](https://github.com/Yelp/detect-secrets) | `1.5.0` | - |
| noseyparker | leaks | [github.com/praetorian-inc/noseyparker](https://github.com/praetorian-inc/noseyparker) | `0.24.0` | - |
| titus | leaks | [github.com/praetorian-inc/titus](https://github.com/praetorian-inc/titus) | `v1.2.9` | source overlap: secrets-rules |
| kingfisher | leaks | [github.com/mongodb/kingfisher](https://github.com/mongodb/kingfisher) | `2.1.0` | source overlap: secrets-rules |
| credsweeper | leaks | [github.com/Samsung/CredSweeper](https://github.com/Samsung/CredSweeper) | `1.18.2` | source overlap: creddata |
| credsweeper-noml | leaks | [github.com/Samsung/CredSweeper](https://github.com/Samsung/CredSweeper) | `1.18.2` | source overlap: creddata |
| deepsecrets | leaks | [github.com/ntoskernel/deepsecrets](https://github.com/ntoskernel/deepsecrets) | `2.0.1` | - |

## Training-source evidence

`train` is a conservative source-overlap exclusion, not proof of memorization. An empty list is absence of known evidence, not proof of independence. Exclusions extend to other cuts and corrupted copies of the same source and to identical-weight records.

- **opf-ru:** Model card: bbeglerov/russian-pi-66k-opf, derived from wolframko/russian-pii-66k train.
- **opf-ru-v2:** Not disclosed. Anonymous ACSAC 2026 OPF checkpoint; repository and revision checked 2026-09-04.
- **traciora:** 121k synthetic examples (v6-ru-all-5k); original sources not disclosed.
- **apararti:** 17k examples; original sources not disclosed.
- **openai-base:** OpenAI; training sources not disclosed.
- **pplx:** Not disclosed.
- **openmed-multilingual:** Model card: ai4privacy 200k/400k/500k/1m, Nemotron-PII, gretel, piimb/privy. All matching source cuts excluded.
- **openmed-nemotron:** Model card: NVIDIA Nemotron-PII training split, 100k examples.
- **gliner-nvidia:** Model card: NVIDIA Nemotron-PII; NVIDIA Open Model License.
- **gliner-urchade:** Model card: urchade/synthetic-pii-ner-mistral-v1.
- **gliner2-fastino:** Model card: 4,910 synthetic texts in EN/FR/ES/DE/IT/PT/NL.
- **gliner2-hivetrace-omni:** HiveTrace/gliner-guard: 467,273 examples including Nemotron-PII and Gretel finance; author declares held-out benchmark test splits.
- **gliner2-hivetrace-uni:** HiveTrace/gliner-guard: 467,273 examples including Nemotron-PII and Gretel finance; author declares held-out benchmark test splits.
- **gliner2-vladlinv:** Not disclosed.
- **ru-pii-ner:** Not disclosed; loaded with vladlinv/ru-pii-ner.
- **ru-legal-ner:** Not disclosed; repository updated 2026-09-03.
- **pii-shield-onnx:** Not disclosed; no model card. CPU ONNX graph.
- **davlan-xlmr:** Training sources not disclosed in card; 10 languages including Russian, PER/ORG/LOC/DATE; AFL-3.0.
- **davlan-mbert:** Same family as davlan-xlmr, mBERT backbone; PER/ORG/LOC/DATE; AFL-3.0.
- **ner-ru-gherman:** Model card: AlexKly/Detailed-NER-Dataset-RU, BIOLU annotation.
- **ner-ru-gherman-onnx:** ONNX export of ner-ru-gherman, int8 graph.
- **ner-ru-yqelz:** Model card: XLM-R large trained on Wikiann/ru; PER/ORG/LOC.
- **fef2-secret-ru:** Model card: synthetic Russian credentials plus 0.35 replay of unnamed public Russian NER corpora.
- **nym-base:** Model card: 724k Wismut/nym-pii-multilingual-data synthetic examples plus 77.5k LLM-labelled Wikipedia examples.
- **nym-small:** Distilled nym-base; ONNX weights only, same 40 labels.
- **kalyan-ettin:** Model card: NVIDIA Nemotron-PII; English, 53 snake_case labels.
- **gravitee-small:** Model card: gravitee-io/pii-detection-dataset; English, 28M parameters.
- **bardsai-eu:** Sources not disclosed; 24 EU languages, no Russian stated; GDPR-oriented labels.
- **mmbert32k:** Model card: ai4privacy/pii-masking-400k plus Presidio annotation; 32k context.
- **openai-base-onnx:** ONNX mirror of openai/privacy-filter; CPU speed reference only.
- **gliner-multi-v21:** Model card: urchade/pile-mistral-v0.1; 289M parameters.
- **gliner-multi-v21-ru:** Same weights as gliner-multi-v21, with Russian zero-shot labels.
- **gliner-pii-edge:** Wordcab/Knowledgator card: training sources not disclosed, 60+ categories, quantization-aware.
- **gliner-pii-base:** Same PII family as gliner-pii-edge; base configuration.
- **gliner-stream-pii:** Qwen3-0.6B decoder backbone; disputed inclusion under the no-LLM scope.
- **nuner-zero:** Model card: numind/NuNER; English claimed, lowercase zero-shot labels.
- **gliner2-large:** Model card: sources not disclosed; EN/FR/ES, 486M parameters.
- **gliner25-fastino:** Sources not disclosed; mDeBERTa-v3-base boundary architecture, 287M parameters.
- **gliner25-fastino-ru:** Same weights as gliner25-fastino, with Russian zero-shot labels.
- **gliner-nvidia-ru:** Same weights as gliner-nvidia, with Russian zero-shot labels.
- **gliner-urchade-ru:** Same weights as gliner-urchade, with Russian zero-shot labels.
- **gliner2-fastino-ru:** Same weights as gliner2-fastino, with Russian zero-shot labels.
- **gliner2-hivetrace-omni-ru:** Same weights as gliner2-hivetrace-omni, with Russian zero-shot labels.
- **gliner2-hivetrace-uni-ru:** Same weights as gliner2-hivetrace-uni, with Russian zero-shot labels.
- **gliner2-vladlinv-ru:** Same weights as gliner2-vladlinv, with Russian zero-shot labels.
- **opf-kz-ru:** OpenAI privacy-filter fine-tune for Kazakh/Russian; original sources not disclosed.
- **natasha:** Slovnet NER trained on Nerus silver Wikipedia/news annotation; package version pins the implementation.
- **spacy-ru-lg:** Nerus silver annotation; spaCy 3.8.
- **spacy-alrosait:** Model card: scanpatch Russian NAME/ADDRESS, AlexKly Detailed NER and alrosait synthetic Russian PII, 13,052 training examples.
- **stanza-ru:** WikiNER silver Wikipedia annotation; Russian default package.
- **gitleaks:** Provider patterns and entropy; no model training.
- **betterleaks:** Gitleaks fork with its own rule set; no model training.
- **rules-ru:** Public checksum algorithms, public token prefixes, and organization forms; no training.
- **presidio-ru:** Presidio and presidio-ru-recognizers rules; spaCy ru_core_news_sm trained on Nerus.
- **trufflehog:** Provider detectors, no training; verification disabled; whole-line spans.
- **detect-secrets:** Entropy and keywords; hashed secrets in native report, whole-line spans.
- **noseyparker:** Praetorian rules; no training. Successor: Titus.
- **titus:** Nosey Parker successor; provider rules and byte offsets, no training.
- **kingfisher:** Provider rules with Betterleaks built-ins; validation disabled, low confidence.
- **credsweeper:** Rules plus ONNX ML classifier trained on Samsung CredData.
- **credsweeper-noml:** CredSweeper with ML filtering disabled via ml_threshold=0.
- **deepsecrets:** Entropy, variable-name semantics and code parsing; training sources not disclosed.

Exact execution settings are in [models.toml](../benchmark/models.toml), observed runtimes in [run-inventory.json](../results/run-inventory.json), and measured coverage in [by-language.md](../results/by-language.md). Model and scanner software licenses are controlled by their upstream projects; this project's MIT license does not relicense their weights.
