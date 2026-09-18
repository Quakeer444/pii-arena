# Methodology

The frozen run compares ready-made detectors of personally identifiable information and secrets. It covers token classifiers, zero-shot NER, secret scanners and public deterministic rules. Generative LLM evaluation is outside this release. A decoder-backed span detector is separately marked as disputed in the catalog.

## What counts as a miss

The primary metric is **a gold span untouched by every predicted character**. The unit is one gold span after normalization. Two annotations with the same boundaries but different labels remain two units. An empty prediction on nonempty gold misses 100%.

Touching one character counts as detection. It does not prove that the whole value has been hidden. Fully hidden spans and character recall are separate measurements. Hidden is computed after word-boundary normalization, so it describes a masker applying that same normalization, not necessarily the raw detector output.

Gold and predicted boundaries receive the same normalization: trim whitespace, expand to word boundaries, and merge adjacent pieces with the same label. Invalid predicted intervals are dropped and counted. Inference adapters clip malformed spans to the chunk boundary and record clipping separately.

The masking view applies those normalized predicted boundaries. For text `key=abc123`, a raw prediction covering only `abc` touches the gold value and is a detection, but leaves `123` exposed unless boundary expansion extends the mask across the whole token. Run `uv run python benchmark/selftest.py` to execute the normalization and incomplete-result checks used by this contract. A masker that uses raw detector offsets must use the separate raw-offset diagnostic.

## Comparable inputs

Zero-shot detectors receive each dataset's taxonomy, using the English or Russian label variant declared by the detector configuration. Russian-label variants are evaluated only on Russian datasets. Model inference retains scores down to 0.1; the frozen report threshold is 0.5. Reports also show 0.3, 0.2 and 0.1 operating points.

Chunking is a run parameter shared across detectors. Variants include the base 600-character cut, 300-character sentence chunks, overlapping windows and unchunked long-context runs. Input normalization variants are recorded, not silently applied to one detector.

## Coverage and training overlap

Each dataset has a language cut (`ru`, `en`, `multi`) and kind (`pii`, `secrets`). Pooled missed rate sums missed spans and divides by the gold spans of the eligible datasets. Macro missed rate gives each eligible dataset equal weight.

Every table shows coverage. A composition is eligible only where all its members have a usable prediction and no member was trained on that source. Missing coverage is not a measured zero. `train` means evidence of training on the source, including other slices and corrupted copies of that source. It does not prove memorisation; an empty overlap list does not establish cleanliness.

Unions combine all predicted characters. A k-of-N vote requires the full N-member composition. Hand-picked compositions in this release were evaluated on the frozen benchmark; they are not claimed to be an independently selected optimum. Greedy selection was unusable because the common candidate pool collapsed to one dataset.

The overview also reports macro results and a frozen sensitivity cut excluding this project's six synthetic datasets and three corrupted copies. The remaining 32 datasets still contain upstream synthetic material. The cut changes only the reporting denominator; candidate selection and the source-lineage dev/test assignment remain frozen.

## Uncertainty

Detailed dataset reports retain 95% bootstrap intervals over rows, using 1,000 shared resamples. Adjacent models are compared with paired bootstrap differences. Indistinguishability is not transitive, so pairs are not merged into a chain.

Overview charts show descriptive point estimates. They do not establish statistical superiority. The JSON export preserves exact missed counts and denominators; metrics marked `_reported` retain the published rounding. Do not reconstruct exact hidden counts or character totals from rounded percentages.

## Speed

Speed is throughput under the recorded concurrent load, not single-request latency. Compare hardware, threads, concurrent workers, chunking and quantization together. CPU reference costs are calibrated through a same-condition pplx run to 1,100 characters/second. RTX 5090 reference costs use two concurrent processes. CPU runs used 24 processes with 16 threads each on the measured node.

Compositions assume sequential detectors, so their per-character times add. Estimates borrowing a speed from another thread count are marked explicitly. ONNX records loaded with CPUExecutionProvider have no GPU inference path. Dynamic int8 quantization was closed after the observed quality and speed results; this release does not require the intentionally omitted runs to be completed.

Any future service-latency result must measure the complete candidate at one concurrent request, declare batch size, warmup, repeated trials, preprocessing, postprocessing, workload-size distribution, peak memory and latency percentiles. It must be reported separately from concurrent throughput. This release has no such W=1 measurement and makes no application-latency SLA claim.

## Integrity

Predictions with errors, duplicate rows, missing rows or mismatched dataset fingerprints must fail validation. Partial speed runs do not enter quality. Legacy files lacking both protocol and dataset hash are disclosed. Frozen sample IDs and corpus hashes identify the release; recomputing a fingerprint is not a substitute for checking it against the frozen value.

See [limitations](limitations.md), [reproduction](reproduce.md) and the [detailed summary](../results/report.md).

The [metric contract](metrics.md) defines the exact schema 3 category fields. Presentation categories split financial identifiers from documents, and explicit logins from other account references, while preserving the original labels and protocol groups. The [external-method comparison](comparison.md) explains why these masking scores cannot be directly ranked against differently scoped, typed or one-to-one NER results.

Historical secrets-report labels such as `all 52 models` mean all non-scanner catalog records, including rules, Presidio, mirrors and label variants. They do not mean 52 distinct learned models. Partial membership is shown as `[k/N]`.
