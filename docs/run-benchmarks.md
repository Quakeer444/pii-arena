# Run models on your own CPU or GPU

This is the developer entry point for **preparing inputs and collecting new measurements**. It does not change the website or published results. For exact regeneration of the existing tables, use [release reproduction](reproduce.md).

**Current boundary:** the public clone does not include the 41 frozen corpora. Only Leak Museum has an audited automatic acquisition recipe. The tool can import and validate **any or all 41 datasets** from a workspace you are authorized to use. A clean clone is not yet an unattended download-and-rerun of every historical configuration. Missing inputs and unsupported adapters are errors, not silently skipped successes.

## 1. Start without installing models

Run commands from the repository root. Use Python **3.12**, Git and [uv](https://docs.astral.sh/uv/). Linux is the primary execution target; the inherited adapters use POSIX facilities. Use WSL2 rather than native Windows. macOS CPU execution is conditional on the selected model's dependencies; this wrapper does not provide MPS, ROCm, multi-GPU or distributed execution.

```sh
uv sync --frozen
uv run python scripts/onboarding.py inventory
uv run python scripts/onboarding.py inventory --json
```

`inventory` is read-only. The JSON includes each dataset's upstream source, archived license label, retained revision, expected raw paths, preparation status and whether an automatic download recipe exists. A missing dataset is normal in a clean clone. Reading the inventory does not download data, install Torch, contact a model provider or accept any dataset terms.

## 2. Prepare one public dataset

```sh
uv run python scripts/onboarding.py prepare --datasets leak-museum --download
uv run python scripts/onboarding.py verify --datasets leak-museum
```

Preparation checks out the revision already pinned by [the public CPU reproduction script](../scripts/reproduce_cpu.py), runs the existing source-relative converter, validates the exact frozen CSV hash and copies the verified inputs into `.local/benchmark/BENCH/leak-museum/`. A second identical preparation reuses the verified copy. It does not need a model environment or Gitleaks.

Expected verification status: `leak-museum ready`, with **97 rows**. Download/build output is local in `.local/benchmark/prepare.log`; temporary source checkout files are removed after preparation. The persistent normalized inputs are reused across models and devices.

For the existing end-to-end baseline, install **Gitleaks 8.30.1** and run its separately maintained command:

```sh
uv run python scripts/reproduce_cpu.py
```

That command uses its own ignored workspace and additionally verifies the frozen expected score: 101 gold spans, 15 fully hidden and 86 missed. The new matrix wrapper does not relabel historical scanner adapters as verified model loaders.

## 3. Prepare all datasets from permitted frozen inputs

The source must contain `BENCH/<dataset>/bench.csv` and `BENCH/<dataset>/meta.json`. Downloaded model weights, historical predictions and raw source archives are not required for this import.

```sh
uv run python scripts/onboarding.py prepare \
  --datasets all --from-workspace /absolute/path/to/permitted-workspace
uv run python scripts/onboarding.py verify --datasets all
```

For a checkout that already has the preserved archive, use `--from-workspace .local/research`. The destination is a different workspace; the tool refuses to write into `.local/research` or outside this repository's `.local/` boundary. Select a subset with, for example, `--datasets hivetrace,redmadrobot`.

The importer validates the entire requested source selection before copying anything. It then stages and verifies each dataset before promoting it. It checks exact CSV SHA-256, schema, unique IDs, annotation boundaries and type mapping, row and annotation counts, character totals as published in the catalog (each CRLF counts as one character), and metadata language/task. Existing mismatched inputs are never overwritten. The published `datasets/samples.json` is copied unchanged; importing does not resample.

`meta.json` is essential, especially for GLiNER label lists. The public catalog does not authenticate every historical metadata byte. The wrapper validates metadata structure and records its hash, but a valid new label list is not proof that it equals the original experiment's label list. Exact historical reproduction also requires the original metadata and runtime/profile.

An archive is not supplied by this branch. Use [source acquisition](sources.md) and the [license notices](../LICENSES/README.md) to establish what you may obtain. `source_mode=files` in archived metadata is not permission to redistribute a dataset. Gated, unclear-license and missing-exporter cases need maintainer work; they are not bypassed by `--download all`.

## 4. See the complete plan before a costly run

```sh
uv run python scripts/onboarding.py plan --datasets all --models all --device cpu
uv run python scripts/onboarding.py plan --datasets all --models all --device cuda --json
```

Every requested model/dataset pair appears as `planned` or `blocked`, with reasons and a training-overlap flag. `planned` means the inputs and adapter route are admissible, **not** that the environment or model inference has already passed. `run` probes environments before starting inference and refuses a selection with any blocked cells.

The current catalog has 62 execution definitions; some are variants, mirrors, scanners or rules, not independent architectures. `--models all` refers to those definitions, not every historical `+variant` prediction file. The wrapper does not automatically reconstruct the historical variant settings.

| Existing loader family | CPU selection | CUDA selection | Additional requirement |
|---|---|---|---|
| `hf`, `opf` | Supported route | Supported route | Compatible isolated runtime; OPF conversion dependencies |
| `gliner`, `gliner2` | Supported route | Supported route | Compatible family runtime and dataset-specific labels |
| `pplx` | Supported route | Supported route | Explicit `--trust-remote-code` |
| `onnx`, `spacy` | Supported route | Blocked | These existing adapters execute on CPU |
| Package-based historical loaders, scanners, rules and Presidio | Not admitted by this wrapper | Not admitted by this wrapper | See the existing loader/scanner status in [reproduction](reproduce.md) |

A supported route is not a hardware test result. The catalog's historical `cpu` boolean is not used as a capability flag. For CUDA, the selected interpreter must actually report CUDA availability; there is no silent CPU fallback. Use a separate CPU campaign for CPU-only tools rather than label them GPU measurements.

## 5. Supply an inference environment

The publication `.venv` intentionally has no inference dependencies. This branch does **not** invent a universal lockfile for historically incompatible model families. Use a Python 3.12 environment validated for the selected model, with the observed versions in [run-inventory.json](../results/run-inventory.json) as evidence, not as a complete dependency lock.

For a first **experimental HF CPU environment**, the following creates a fresh, unpinned runtime. It is a starting point for a new measurement, not a certified way to reproduce the historical score or run every family:

```sh
uv venv --python 3.12 .local/envs/hf-cpu
uv pip install --python .local/envs/hf-cpu/bin/python \
  torch --index-url https://download.pytorch.org/whl/cpu
uv pip install --python .local/envs/hf-cpu/bin/python transformers
uv pip freeze --python .local/envs/hf-cpu/bin/python > .local/hf-cpu-observed.txt
```

For GPU environments, select the CUDA wheel index compatible with your driver and runtime using [uv's official PyTorch guide](https://docs.astral.sh/uv/guides/integration/pytorch/). Do not assume the host's `nvcc` version identifies the wheel in the selected Python environment. Install the selected family dependencies in that environment and first run one small prepared dataset. A successful package import alone does not establish adapter compatibility.

Pass one interpreter with `--python`. For several families, create an ignored TOML file with a `[python]` table. [The example](onboarding-environments.example.toml) documents the format; its paths are illustrative and do not create or populate environments.

## 6. Run and resume

After the preceding CPU setup and public data preparation, this is a first new HF measurement:

```sh
uv run python scripts/onboarding.py run \
  --models ru-legal-ner --datasets leak-museum --device cpu \
  --python .local/envs/hf-cpu/bin/python
```

After importing all datasets and validating the selected runtime:

```sh
uv run python scripts/onboarding.py run \
  --models ru-legal-ner --datasets all --device cpu \
  --python .local/envs/hf-cpu/bin/python --threads 4 --batch 4
```

A CUDA example **requires an already prepared GLiNER2 CUDA environment**, not the HF CPU environment above:

```sh
uv run python scripts/onboarding.py run \
  --models gliner2-fastino --datasets all --device cuda \
  --python .local/envs/gliner2-cuda/bin/python --threads 4 --batch 4
```

Repeat the same command with `--resume` to continue or revalidate a completed campaign. The identity includes input/metadata hashes, model configuration and revision, adapter/scorer/wrapper hashes, installed package versions, CPU/platform, GPU name/CUDA runtime when applicable, device, batch, threads and thresholds. A completed prediction is reused only when its recorded identity and file digest match; the scorer runs again even on reused predictions. Changed data, packages, settings or code must not reuse old results as though nothing changed.

The wrapper fixes inference threshold `0.1`, scoring threshold `0.5` by default, chunk size `600`, character chunking, no normalization and no quantization. `--score-threshold` may be changed explicitly. These are a declared **new-run profile**, not a reconstruction of every historical profile. Inherited `OUT`, `LIMIT`, `THRESH`, variant and permissive scoring environment overrides are cleared. Models that execute remote code require opt-in; only review and enable code you trust.

## Where everything goes

```text
.local/benchmark/
  BENCH/                  verified CSVs, metadata and frozen sample selection
  MODELS/                 converted model artifacts used by inherited adapters
  cache/                  model/library download caches
  staging/                temporary acquisition and import work
  runs/<identity>/
    BENCH -> ../../BENCH  same inputs for inference and scoring
    MODELS -> ../../MODELS
    identity.json         provenance and selected runtime/profile
    plan.json             complete requested matrix
    RESULTS/              per-dataset prediction files
    completed/            completion receipts and scoring metrics
    summary.json          completed, reused and failed cells
    *.log                 local process output
```

Only internal workspace links are used. New measurements are not written to public `results/`, `site/`, the preserved archive, or the published snapshot. Inputs are checked again immediately before inference and before scoring. Corpus-bearing process errors stay in ignored logs, not terminal summaries or CI artifacts. Authentication may be inherited for authorized downloads, but environment variables/tokens are not serialized into the run identity.

## Failure behavior and practical limits

| Situation | Behavior / next action |
|---|---|
| Missing corpus, wrong hash or incomplete metadata | No matrix inference starts. Obtain the exact authorized inputs; do not disable validation. |
| Missing dependency, wrong Python version, unavailable CUDA | Environment preflight fails. Repair the selected interpreter, not the publication environment. |
| Model exception or invalid/incomplete predictions | Cell is failed, no completion receipt survives, other admitted cells can finish; inspect its local log. |
| Out of memory | No automatic device/batch downgrade. Lower `--batch` explicitly; that creates a different run identity. |
| Interrupted campaign | Repeat with `--resume`. An incomplete cell is recomputed; there is no mid-cell checkpoint. |
| Stale `.running` lock | Confirm no process is still using the run before manually removing the lock. No automatic lock stealing. |
| Changed package or input hash | Different identity or failed validation; never silently reuse incompatible predictions. |
| Training-source overlap | Kept as explicit per-cell metadata; do not pool it into held-out results. Corrupted copies inherit their parent's flag. |

Exit status is `0` for success (including a read-only inventory), `2` for inadmissible input/environment/plan, and `3` for a campaign with failed cells. CLI usage errors also use `2`. JSON output is available for inventory, preparation, verification and planning; campaigns write their summary to disk.

Execution is sequential, one model/dataset process at a time. This limits concurrent RAM/VRAM pressure but reloads a model between datasets. There is no disk-space estimator, persistent model worker, prediction compression, fully offline environment bundle, guaranteed remote-resource isolation, or universal dependency resolver in this first layer. The `pplx` remote-code opt-in is not a sandbox. Review local artifacts before sharing them.

## Maintainer validation

```sh
uv run python -m unittest discover -s scripts -p 'test_onboarding.py' -v
uv run python scripts/verify.py
```

The onboarding workflow additionally prepares Leak Museum in a clean checkout and checks its frozen hash. The offline tests use fabricated, non-sensitive fixture text and simulated inference/scoring processes; they do not establish correctness of actual GPU inference or complete reproduction of the historical matrix.

The [design and release checklist](benchmark-onboarding-design.md) explains the upstream patterns, the current 41-dataset blockers, and the evidence required before advertising a one-command full CPU/GPU campaign.
