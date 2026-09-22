# Benchmark onboarding: evidence, design and release gates

Research date: **2026-09-22**. Repository baseline: `c2cdefb7b925c48005e3f27cb4001a1a8bf7d4cd`.

Scope: a developer clones PII Arena, prepares the intended datasets, chooses CPU or CUDA, runs detectors, understands incomplete coverage and can resume safely. This is repository work, not a website redesign, scorer replacement or regeneration of the published measurements. The practical entry point is [Run benchmarks](run-benchmarks.md).

## Decision

Keep the existing benchmark protocol and add a thin, dependency-free preparation and execution layer around it. Separate **input acquisition**, **frozen-input verification**, **runtime selection**, **inference**, **scoring** and **publication**. Do not solve onboarding by turning the publication environment into a single installation containing every historical model dependency.

The strongest eventual distribution is a **versioned, permitted, normalized data pack**, accompanied by exact source/conversion provenance and separate family/device environment locks. A user normally consumes the prepared pack; maintainers own the difficult upstream reconstruction. Sources that cannot be redistributed remain user-authorized acquisition/import routes. This is the proposed destination, not a data pack published by this branch.

## What popular projects actually do

The following are primary-source observations, not claims that another framework can reproduce PII Arena's masking protocol unchanged.

| Project / official source | Observed pattern | Decision for PII Arena |
|---|---|---|
| [EleutherAI lm-evaluation-harness: CLI](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md) | Separate list, validate and run commands; model/task/device selection; separate request and response caches; explicit fixed samples; limited-example runs marked for testing. | Expose inventory/verify/plan before inference. Account for every requested cell. Do not present a small test run as the full benchmark. |
| [MTEB: usage](https://docs.mteb.org/) and [caching](https://docs.mteb.org/get_started/advanced_usage/cache_embeddings/) | Select models and tasks separately. Reuse expensive embeddings through a cache wrapper; different prompt types have separate cache locations. | Keep normalized inputs independent of model outputs. Bind prediction reuse to inputs, labels, model revision and execution profile rather than a convenient filename. |
| [OpenCompass: installation and data preparation](https://opencompass.readthedocs.io/en/latest/get_started/installation.html) | Optional dependency groups, separate environments for conflicting backends, automatic Hub sources and downloadable prepared bundles for other datasets. | Offer a small publication environment and explicit inference environments. Make prepared permitted inputs the ordinary path instead of forcing every user to reproduce a research workstation. |
| [Hugging Face Datasets: loading](https://huggingface.co/docs/datasets/loading) | Explicit source revision, split and file selection, alongside local-file loading. | Record an immutable source identity and exact selected files. A URL plus a dataset name is not a frozen benchmark definition. |
| [uv: PyTorch integration](https://docs.astral.sh/uv/guides/integration/pytorch/) | Accelerator-specific wheels/indexes and explicit package-source mappings. | Treat CPU/CUDA wheel choice as part of a runtime profile. Do not infer it from an arbitrary `cpu` field or blindly install the latest common environment. |

The useful commonality is **separation of concerns with inspectable configuration**, not the number of dependencies or the presence of a dashboard. PII Arena does not need to migrate into an LLM or embedding evaluation framework to obtain these benefits. Such a migration would introduce unrelated task, output and metric semantics and create new protocol-comparison work.

The wrapper takes a deliberately conservative position on convenience. Automatic device fallback, automatically shrinking a benchmark after download failures and treating any existing output as reusable would make a demonstration easier, but a benchmark less trustworthy. Explicit selection and actionable failure are preferable to a green check on an unknown denominator.

## Audit of this repository's starting point

### Publication reproducibility is not inference reproducibility

[Release reproduction](reproduce.md) already distinguishes validation, rendering, archive export, rescoring and fresh inference. This is valuable and must remain visible. `uv sync --frozen` installs the small publication project; it is not an installation of all detectors. Rendering `results/snapshot.json` reproduces public artifacts without obtaining corpus texts or running models.

The public comparison contains 41 datasets, 41,643 rows and 227,466 normalized gold spans. The 62 catalog execution definitions include model families, label variants, mirrors, scanners and rules. A Cartesian plan over these definitions and all datasets has 2,542 requested cells, which is not the same thing as the 2,591 saved historical prediction runs. Historical `+variant` files have additional settings; treating them as default model runs loses that identity.

### The data gap is substantive

The [dataset reconstruction section](datasets.md#reconstruction-status) identifies 22 cuts without a retained raw-source revision. A hash can verify that someone has the correct archived bytes, but cannot make an unavailable file downloadable. Fetching today's upstream `main`, getting valid JSON and using the same random seed do not establish equivalence.

The [acquisition map](sources.md#acquisition-map) also identifies missing or non-trivial transforms: a historical combined Gretel export, scanner-rule fixture export, reconstructed CredData source files and synthetic outputs depending on generator/runtime versions. Several datasets use selected or reconstructed text, not an untouched upstream test split. Merely adding a loop around `hf download` would not reproduce those cuts.

The existing Leak Museum route is a useful anchor: pinned source, source-relative annotations, frozen normalized hash, fixed binary version and an exact expected score. Extend this evidence chain one source family at a time; do not promote the other 40 datasets to the same support label merely because they have source links.

### Metadata is an input, not documentation

The CSV contains gold entity types, while `meta.json` supplies group mappings, language/task metadata and, for zero-shot models, actual inference labels. `datasets/samples.json` fixes the selected IDs. Corpus hash equality without the intended metadata and label lists is insufficient for historical equivalence.

The new verifier checks the normalized CSV bytes and shape, counts, IDs, offsets, label mapping and language/task. Character totals use the published catalog rule: each CRLF counts as one character, while annotation offsets stay on the untranslated CSV text. It records metadata SHA-256 for run identity. Because the existing public catalog does not publish every metadata digest, this is **structural verification plus new-run identity**, not authentication of every original metadata byte. Publishing a reviewed metadata manifest remains a release gate.

### CPU and GPU are adapter properties too

The existing ONNX loader requests `CPUExecutionProvider`. The spaCy adapter does not initialize GPU execution. Other families expose CUDA, while package-based loaders and scanner fallbacks have different revision/runtime guarantees. A historical `cpu=false` field cannot be used to declare an adapter incapable of CPU inference; conversely, accepting `DEVICE=cuda` does not prove that every loader used a GPU.

The user-facing choice should eventually be two explicit campaigns: CPU-capable routes and GPU-capable routes, with CPU-only tools visibly separate. A complete quality comparison may include both, but a GPU speed table must not silently include CPU fallback timings. This branch blocks unsupported device/adapter combinations rather than implement a misleading universal GPU switch.

### Output routing needs a whole workspace

`benchmark/run.py` can use `OUT`, but the existing scorer derives `RESULTS` from `BENCHMARK_DATA`. Simply redirecting inference output risks scoring a different old file. The new wrapper gives each campaign a complete ignored workspace containing its own `RESULTS` and internal links to verified shared `BENCH` and `MODELS`. Both processes receive the same workspace identity. No published measurement is rewritten.

## Data distribution design

### Three distinct user promises

**Open, versioned suite:** inputs whose redistribution and normalization have been reviewed, supplied as a prepared immutable bundle or an audited source recipe. Its definition explicitly names the included datasets and version. Do not call a smaller open suite the complete historical 41-dataset comparison.

**Historical frozen suite:** all original cuts with matching CSV and metadata hashes, sample IDs and original profiles. Where lawful redistribution is unavailable, users import authorized copies. A run is incomplete until every requested eligible input is present. This is an exactness promise, not necessarily a public-download promise.

**Custom experiment:** changed sources, sample selection, labels, chunking or dependency/runtime choices. Preserve the resulting provenance and permit analysis, but assign a new experiment identity. Do not overwrite the existing frozen dataset identity or publish an old benchmark label over new inputs.

These are proposed named release profiles. The current CLI accepts explicit catalog IDs or `all`; it does not yet implement named suites or a custom-data conversion API.

### A pack manifest must describe bytes, not intentions

For each prepared dataset, the future reviewed manifest should contain the dataset/cut ID, schema/protocol version, source repository and immutable revision, exact source paths and per-file hashes, source license/attribution/access policy, converter code identity and dependencies, selected-ID manifest digest, normalized CSV digest, metadata digest, row/character/original-annotation counts and derived-parent links.

Record expected download size and unpacked size only when measured. Model weight storage must be estimated separately; a small dataset bundle says nothing about the storage needed by dozens of models and conversion caches. An upstream archive hash and a post-extraction file inventory protect different boundaries and should not be conflated.

Do not insert guessed source revisions to fill empty fields. A recreated source that does not match frozen bytes belongs to a new experimental version unless a documented correction process establishes a new release. Preserve the old missing-revision fact for auditability.

### Keep the authoritative format stable

For this release, retain the existing UTF-8 CSV byte representation and end-exclusive character offsets as the canonical scoring input. Normalization of newlines, Unicode, whitespace, annotation ordering or JSON serialization can change hashes and offsets. A Parquet/Arrow cache could later speed loading, but must be a verified derivative keyed by the canonical hash, not a silent replacement of the benchmark definition.

Bundle normalized inputs, metadata, frozen selections, manifest and notices. Do not put predictions, user tokens, browser files, raw model caches or the entire `.local/research` archive into a convenience ZIP. Keep corpus-bearing downloads outside Git. An external dataset release or Hub repository is a distribution option only after rights and redaction review; no such upload is authorized or performed by this implementation.

A future pack importer must reject traversal paths and unsafe links, bound archive expansion, verify every manifest entry before promotion, and leave the previous usable dataset untouched on a partial download. The current implementation imports a directory, not an archive, and uses per-dataset staging and verification. It intentionally does not claim the unimplemented archive-security properties.

### Close the 41-dataset gaps systematically

| Existing source class | Work required before a public full-suite claim |
|---|---|
| Leak Museum | Keep the current frozen source-to-score contract as the regression anchor; extend it to the new preparation interface. |
| Retained-revision sources | Convert source notes into tested file-level acquisition recipes; verify conversion dependencies, frozen selections and output hashes. A revision alone is insufficient. |
| Missing-revision cuts | Recover the original authorized material or identify and verify the exact upstream bytes. Otherwise retain an archive-only label or publish a separately named new cut. |
| Synthetic datasets | Pin generator code and Faker/dependency closure; verify bytes against the frozen outputs rather than rely only on seed 0. |
| Corrupted datasets | Declare parent hash, transform version and parameters; preserve inherited training-source exclusions. |
| Derived scanner fixtures / combined exports | Restore and audit the missing exporter or distribute an authorized normalized artifact with provenance. |
| Gated or unclear-license sources | Resolve access/redistribution outside the launcher. Never accept upstream terms on behalf of a user or infer permission from archived `source_mode`. |

The next maintainer action should be an inventory of available original normalized CSVs **and metadata**, with hashes and rights classification. That is more valuable than another generic dataset downloader. Use that inventory to choose which exact public pack can honestly be shipped first.

## Runtime and execution design

Keep one dependency-free publication environment. Maintain separate environment profiles where model families conflict, then split CPU and CUDA builds where necessary. Use explicit package indexes and versioned locks generated by a real resolver. A historical list of observed packages is evidence for reconstructing a runtime, but may omit transitive dependencies, resources, wheel origins and platform-specific binary constraints.

The branch accepts a validated Python interpreter per family, probes required imports and Python 3.12, checks actual CUDA availability, and records installed distributions plus hardware/platform information. It does not yet ship validated locks for every family, binary installers, a container image, a GPU test farm or a dependency conflict solver. The experimental CPU setup in the guide is labeled unpinned and is not evidence of historical equivalence.

The new-run identity includes the selected definitions and immutable model revisions, verified input and metadata hashes, code hashes, device, batch/threads, chunking/normalization/quantization choices, scoring threshold and observed runtime. This is conservative: even an irrelevant package change may prevent reuse. Correctness is preferred to maximizing cache hits in the first implementation.

Run one cell per subprocess so a model failure cannot quietly turn into the next model's success. Record a completion receipt only after strict scoring succeeds. Reuse requires both a matching identity and a matching prediction digest, and scoring is repeated on reuse. An interrupted cell is recomputed rather than inferred complete from its output filename. No broad `ALLOW_ERR` or `ALLOW_STALE` override is inherited.

Initially execute sequentially. This avoids launching dozens of memory-heavy models at once and makes resource attribution clearer, at the cost of repeated model loading. A persistent worker per model could improve throughput later, but needs GPU-memory cleanup, timeout and crash-recovery tests. Likewise, a batch-size reduction changes performance conditions and should create a declared profile rather than happen invisibly.

The wrapper reports per-cell outcomes, including training overlap, and intentionally does not create a new pooled leaderboard. Quality comparisons must use the intended common eligible dataset intersection, while missing measurements remain missing. Speed comparisons additionally require comparable device, hardware, batch, thread, warm-up, load-time and concurrency conditions. Existing prediction timing metadata is not a controlled cross-machine performance experiment.

## What this branch implements, and what it does not

Implemented: read-only inventory; frozen-input validation; staged authorized-directory import; the audited Leak Museum download/conversion route; explicit full-matrix planning; pinned-loader/device/remote-code admission checks; per-family interpreter selection; environment preflight; isolated inference and strict scoring; content-bound resume; local logs and campaign summaries; offline contract tests and a clean-checkout source-preparation CI job.

Not implemented: automatic acquisition of all 41 cuts; a reviewed redistributable full data pack; authenticated original metadata manifests; validated dependency locks for every model/device; scanner and package-loader modernization; all historical variant profiles; GPU end-to-end qualification; mid-cell checkpoints; model prefetch/offline bundles; disk/VRAM cost estimates; public result submission or website publication.

This boundary is intentional, but it is not the final user experience. The branch should not be marketed as “clone and run every historical configuration with one command” while those requirements remain open.

## Acceptance gates for the final experience

| Gate | Evidence required |
|---|---|
| Clean installation | Linux CPU and CUDA environments created from committed, resolver-produced locks; publication dependencies stay minimal. |
| Prepared data | Fresh acquisition or authorized pack import verifies every requested CSV, metadata file and selected-ID manifest. |
| No hidden subset | Planned, excluded, blocked, completed and failed cells reconcile to the exact requested matrix. |
| Protocol integrity | Existing scorer and strict expected-result tests pass; no changed frozen hashes, exclusions or website data. |
| Inference qualification | A real small-input test for every admitted family/device and a complete requested campaign on suitable hardware. |
| Interruption and reuse | Kill a run mid-cell, resume it, corrupt a receipt/prediction and change settings; only compatible complete work is reused. |
| Access and privacy | Gated access is explicit, unsupported rights are visible, credentials stay out of logs/manifests, corpus-bearing artifacts remain local. |
| Reproducible report | New-run identity, model revisions, dataset/metadata digests, actual device/runtime, coverage and error states accompany every result. |

Order the remaining work as **data manifest and permitted pack**, then **validated family/device environments**, then **full-matrix qualification**. Add prettier progress displays, persistent workers and prefetch optimization only after those gates. These improvements must remain separate from an intentional, reviewed publication step.
