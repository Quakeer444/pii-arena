# Source acquisition and conversion

This public repository distributes metadata, sample IDs, conversion code and aggregate measurements. Corpus text, raw predictions and downloaded model weights are local-only. Source licenses and attribution remain in [LICENSES](../LICENSES/README.md).

## Use the preserved local snapshot

The prepared workspace includes materialized raw sources at `.local/research/BENCH/raw/`, frozen corpora at `.local/research/BENCH/`, and all predictions at `.local/research/RESULTS/`. The raw directory is a real directory, not a link to the older project. The private archive manifest checks file content against the source copy.

The public [catalog](../datasets/catalog.json) records each dataset's raw relative paths, aggregate SHA-256, available source revision, corpus SHA-256 and sample counts. A revision of `-` means the original retrieval did not retain a source commit; a hash identifies the retained bytes but cannot recover them from a newer upstream release.

## Reconstruct a separate workspace

Create an experiment workspace and preserve the published sample selection before running a builder:

```sh
mkdir -p .local/rebuild/BENCH/raw
cp datasets/samples.json .local/rebuild/BENCH/samples.json
```

Obtain source files from the upstream links below. Hugging Face sources use the `hf download` CLI with `--repo-type dataset`; select the archived revision where one exists. Place or rename the downloaded files to the raw paths in the catalog. Hugging Face frequently nests parquet files in `data/`; builders expect the local paths listed below. Gated sources require the upstream owner's access process.

Run builders inside an isolated inference/data environment containing their dependencies (PyArrow for parquet and Faker for the synthetic generator):

```sh
BENCHMARK_DATA=.local/rebuild uv run --no-project python benchmark/bench.py
BENCHMARK_DATA=.local/rebuild uv run --no-project python benchmark/corrupt.py
```

The original data-build dependency environment is not completely pinned in this publication environment. The retained corpora and hashes are the authoritative frozen inputs. Rebuilding with a different Faker or dataset-library version may change text and must not be presented as the same benchmark unless hashes match. Do not replace `.local/research/BENCH/` with a fresh build during reproduction.

## Acquisition map

Paths in this table are relative to the chosen workspace's `BENCH/raw/`. The complete per-cut mapping and hashes are in [catalog.json](../datasets/catalog.json).

| Local raw path | Upstream / acquisition notes |
|---|---|
| `hivetrace/{domain,entity}-00000-of-00001.parquet` | [hivetrace/pii-bench](https://huggingface.co/datasets/hivetrace/pii-bench), files from `data/` |
| `train-00000-of-00001.parquet` | [wolframko/russian-pii-66k](https://huggingface.co/datasets/wolframko/russian-pii-66k), train split; no source license recorded |
| `redmadrobot-test.csv` | [redmadrobot-rnd/pii_benchmark](https://huggingface.co/datasets/redmadrobot-rnd/pii_benchmark), rename `test.csv` |
| `scanpatch/{train,test}.parquet` | [scanpatch/pii-ner-corpus-synthetic-controlled](https://huggingface.co/datasets/scanpatch/pii-ner-corpus-synthetic-controlled), rename the two `data/` parquet files |
| `alrosait-pii-synthetic-ru.jsonl` | [alrosait/pii-synthetic-ru](https://huggingface.co/datasets/alrosait/pii-synthetic-ru), rename `synthetic_pii.jsonl` |
| `jayguard/train.parquet` | [just-ai/jayguard-ner-benchmark](https://huggingface.co/datasets/just-ai/jayguard-ner-benchmark), train parquet |
| `nym-pii-{test,validation}.jsonl` | [Wismut/nym-pii-multilingual-data](https://huggingface.co/datasets/Wismut/nym-pii-multilingual-data), rename both JSONL splits |
| `issue-reports/{test,test_wild}.csv` | [Zenodo 19622962](https://zenodo.org/records/19622962), extract from `Secret-Leak-Detection-Issue-Report.zip` |
| `secret-rules/{gitleaks,betterleaks}_tpfp.jsonl` | Rule fixtures from [Gitleaks](https://github.com/gitleaks/gitleaks) at `b58d3f102cf3a2c84cb7f923d05c25c9b1aed84b` and [Betterleaks](https://github.com/betterleaks/betterleaks) at `95237cf8eb4d8e9f67409595b245e674832992cf`; historical fixture exporter is not in the benchmark. Retained JSONL hashes identify the snapshot. |
| `alexen2-pii-ner-ru-benchmark-test.parquet` | [alexen2/pii-ner-ru-benchmark](https://huggingface.co/datasets/alexen2/pii-ner-ru-benchmark), test parquet; no source license recorded |
| `nerel/{train,dev,test}.jsonl` | [iluvvatar/NEREL](https://huggingface.co/datasets/iluvvatar/NEREL), also retain `ent_types.jsonl`; no source license recorded |
| `factrueval-2016/` | [factRuEval-2016](https://github.com/dialogue-evaluation/factRuEval-2016), clone and check out archived revision `dfe96237` |
| `rubai/data.jsonl` | [islomov/rubai-NER-150K-Personal](https://huggingface.co/datasets/islomov/rubai-NER-150K-Personal) |
| `multiconer-v1/RU-Russian/ru_test.conll` | [tomaarsen/MultiCoNER](https://huggingface.co/datasets/tomaarsen/MultiCoNER), `RU-Russian/` |
| `redact/pii_benchmark_full.json` | [guneeshv/REDACT-PII-Benchmark](https://huggingface.co/datasets/guneeshv/REDACT-PII-Benchmark); obtain access under the upstream custom terms |
| `it-support-tickets/` | [ameau01/synthetic-it-support-tickets](https://huggingface.co/datasets/ameau01/synthetic-it-support-tickets), retain train parquet and PII/retention sidecars |
| `tonicai-privacy-bench/` | [TonicAI/Privacy-Bench](https://huggingface.co/datasets/TonicAI/Privacy-Bench), `tasks/` and `ground_truth/` |
| `kiji/data/test-00000-of-00001.parquet` | [DataikuNLP/kiji-pii-training-data](https://huggingface.co/datasets/DataikuNLP/kiji-pii-training-data), test split |
| `arthur-passwords/sensitive_data_password.csv` | [Arthur-AI/arthur_sensitive_data_password](https://huggingface.co/datasets/Arthur-AI/arthur_sensitive_data_password) |
| `nemotron-pii/data/test-00000-of-00001.parquet` | [nvidia/Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII), test split |
| `tab-echr/echr_test.zip` | [ildpil/text-anonymization-benchmark](https://huggingface.co/datasets/ildpil/text-anonymization-benchmark), retain the ZIP |
| `dialogpii/DialogPII.zip` | [Zenodo 20863452](https://zenodo.org/records/20863452), retain the ZIP |
| `gretel-finance-test.parquet` | [gretelai/synthetic_pii_finance_multilingual](https://huggingface.co/datasets/gretelai/synthetic_pii_finance_multilingual); historical combined test export from language-specific parquet files, verified by raw SHA-256 |
| `privy/privy-dataset.zip` | [beki/privy](https://huggingface.co/datasets/beki/privy), retain the ZIP |
| `creddata/` | [Samsung/CredData](https://github.com/Samsung/CredData), archived metadata at `859b44d1`; reconstruct `data/` using the upstream downloader. Individual source-file licenses apply. |
| `leak-museum/` | [printemps-tokyo/leak-museum](https://github.com/printemps-tokyo/leak-museum), clone at the revision recorded in the catalog |
| `leaky-repo/` | [Plazmaz/leaky-repo](https://github.com/Plazmaz/leaky-repo), clone at the revision recorded in the catalog |

## Conversion caveats that affect interpretation

- **Selection is fixed, not an untouched upstream benchmark.** `samples.json` records row IDs selected by the builders. Some sources contribute multiple splits; this evaluation's source exclusions apply across those splits.
- **NEREL** uses 933 documents from train, dev and test; selected person, organization and location types retain nesting. Discontinuous source spans were omitted. **factRuEval** retains person, organization and location spans and checks token offsets.
- **JayGuard, alexen2 and MultiCoNER** reconstruct text by joining tokens with spaces. **MultiCoNER** is lowercase and has incomplete annotations, so some apparent false positives may be unlabeled entities.
- **Rubai** uses a Russian-character heuristic on an Uzbek/Russian source. Some Cyrillic Uzbek content remains. Generic dates are omitted because the source does not distinguish birth dates.
- **Nym** uses language heuristics; repeated identical negatives are deduplicated. The MULTI cut includes short texts with unresolved language.
- **ameau01** locates declared PII values in ticket fields by substring. Declared values absent from text are skipped. **TonicAI** uses supplied ground-truth spans; **Privy** contains structured JSON, SQL, XML and HTML payloads.
- **TAB/ECHR** takes the first quality-checked annotation per test document. **DialogPII** retains spoken phone/URL forms; some country labels describe languages. Their long documents exercise chunking.
- **Nemotron** omits malformed rows and several demographic, date and profession labels. **Kiji** omits age and title. The source taxonomies are not a uniform definition of sensitive data.
- **Arthur passwords** annotates passwords only; other PII in the text can appear as false positives under its gold labels. **Secrets issues** groups candidate records by issue and includes manually judged negatives. **Scanner rule fixtures** are format tests, with source overlap exclusions for rule-sharing scanners.
- **CredData** builds text from annotated source-file lines, omitting unusable offsets and oversized samples. **Leak Museum** and **Leaky Repo** use source-relative annotation offsets tied to frozen source-file hashes; their annotations are not exhaustive inventories of every possible credential.
- **REDACT** retains most source entity categories but excludes date/time and business-title labels. Its MULTI cut pools 24 non-Russian source languages, including English. Its terms are not a standard open-source license.
- **Project synthetic sets** use seed 0, invented identities, public secret formats and artificial formats. They are useful controlled cases, not evidence about all real Russian secret-bearing prose.
- **Corrupted copies** deterministically alter every row and remap offsets. They inherit training-source exclusions and the original dev/test assignment; they are not independent evidence of unseen training data.

A tested fresh download-to-score route is available for Leak Museum with Gitleaks 8.30.1. A completed pipeline is not claimed for historical cuts whose acquisition steps, raw revisions or dependency versions are missing. Those cuts are listed in the generated [dataset catalog](datasets.md). The preserved local archive supports direct rescoring, and the public snapshot supports exact regeneration of the published comparisons without that archive.
