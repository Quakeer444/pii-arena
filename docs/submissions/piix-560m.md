# PIIX-560m submission

PIIX-560m returns character spans to mask. The default setting balances precision and recall. Recall 8 masks more text. The submitted measurements cover 40 of the 41 frozen datasets in PII Arena v1.0.3 at commit `1aa2c3f52d5bdf05f600a7843ffc230fd87badcb`. Each setting processed 40,147 records containing 226,720 normalized gold spans. The remaining dataset is `secrets-rules`.

| Setting | Gold spans with any character visible ↓ | Gold spans missed entirely ↓ | Character precision ↑ | Character recall ↑ | Character F1 ↑ |
|---|---:|---:|---:|---:|---:|
| Default | 9.36% (21,212) | 6.55% (14,847) | 69.26% | 93.04% | 79.41% |
| Recall 8 | 3.46% (7,843) | 2.16% (4,895) | 54.26% | 97.45% | 69.71% |

Percentages pool the underlying counts across datasets. Character F1 is `2 × TP / (2 × TP + FP + FN)`. All 80 prediction files passed strict rescoring with zero inference errors and zero dropped spans. Each CSV row identifies one dataset by its frozen corpus SHA-256 and one setting by its recall value. Join `bench_sha256` to the same field in the Arena catalog to recover its dataset ID. [Per-dataset counts](piix-560m.csv) · [Dataset catalog](../../datasets/catalog.json)

## Detector and execution settings

The adapter loads the weights, tokenizer, and Python inference code from revision `26d15846b62cb2bd1822871946c884f73879ca47` of `Tracer-ML/PIIX-560m` (Apache-2.0). The weights have SHA-256 `9c9ff5288a2902f073cce4a016d8018f734ea3a021b64d4c8aa29e1f821fe4a4`. The executed Python modules are `piix.py`, `rules.py`, and `type_filter.py`. [Pinned model release](https://huggingface.co/Tracer-ML/PIIX-560m/tree/26d15846b62cb2bd1822871946c884f73879ca47)

For each dataset, PIIX receives its published English label list from `meta.json` and returns merged, untyped mask intervals. The CSV records the metadata fingerprint. PIIX uses 512-token windows with 128-token overlap and a batch size of 32. Arena chunking is disabled and text normalization is `none`. The runner recorded an inference threshold of 0.1. PIIX emits mask intervals without confidence scores. Strict scoring used protocol 1 at the Arena default threshold of 0.5.

| Device | Datasets | Processor | Precision | Python | PyTorch | Transformers | Hub client |
|---|---:|---|---|---|---|---|---|
| MPS | 30 | Apple M5 Max | float32 | 3.12.14 | 2.8.0 | 5.3.0 | 1.33.0 |
| CUDA | 10 | NVIDIA A100-SXM4-40GB, Intel Xeon at 2.20 GHz | bfloat16 autocast | 3.12.3 | 2.9.1+cu128 | 5.20.2 | 2.4.0 |

Both settings for a dataset ran on the same device. At the coverage cutoff, the submission used the Mac for each dataset where both settings had completed and the A100 for the rest. Each worker used one CPU thread. The CSV records the concurrency reported in each prediction header.

## Reproduce one dataset

Use a Python 3.12 environment with PyTorch, Transformers, Hugging Face Hub and safetensors. From the repository root, point `BENCHMARK_DATA` at a workspace containing the frozen `BENCH/<dataset>/bench.csv` and `meta.json`. Set `DEVICE` to the backend being used. Each invocation writes predictions beneath that workspace.

```sh
export BENCHMARK_DATA="$PWD/.local/research"
export DEVICE=cuda THREADS=1 W=1 THRESH=0.1
export NORMALIZE=none LIMIT=0
unset OUT ALLOW_ERR ALLOW_STALE
dataset=leak-museum
python benchmark/run_piix.py "$dataset" --recall 0 --batch 32
python benchmark/run_piix.py "$dataset" --recall 8 --batch 32
THRESH=0.5 python scripts/evaluate.py --data "$BENCHMARK_DATA" --dataset "$dataset" --model piix-560m
THRESH=0.5 python scripts/evaluate.py --data "$BENCHMARK_DATA" --dataset "$dataset" --model piix-560m+r8
```

The same commands apply to `secrets-rules` in a workspace that contains its frozen inputs. Run `python tests/test_piix.py` for a synthetic, offline check of both settings.
