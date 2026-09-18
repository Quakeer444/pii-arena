# Comparing benchmark methods

This project is a frozen, cross-source comparison of detector output under a declared masking contract. It is useful for inspecting failure patterns and choosing candidates for a separate deployment evaluation. It is not an independently certified leaderboard, a replication of every upstream benchmark, or an anonymity guarantee.

The comparison below was checked against primary project documentation on 2026-09-10. Upstream methods can change. Their published percentages must not be ranked against this snapshot without rerunning the same inputs, labels, matching rule and operating point.

## Which projects are worth comparing

The established tool ecosystems and the dedicated research datasets serve different purposes. Presidio Research is an evaluation toolkit within the Microsoft Presidio ecosystem. CredData and TAB are specialized benchmark projects; their narrower audience does not make them less relevant. HiveTrace and redmadrobot directly address Russian text. REDACT is a newer research project, included for its stratification design rather than popularity.

| Project | Evaluation unit and scope | Useful practice | Difference from this snapshot |
|---|---|---|---|
| [Microsoft Presidio Research](https://github.com/microsoft/presidio-research) | PII recognizers and complete analyzer configurations; precision, recall and F-beta | Explicit entity mapping, exploratory analysis, template-separated splits, evaluation of a configured analyzer | We use normalized character masks and annotation coverage; our small Presidio subset does not establish the performance of all Presidio configurations |
| [HiveTrace PII-Bench](https://huggingface.co/datasets/hivetrace/pii-bench) | Russian character spans; entity and scenario splits, including negatives | Human annotation review, consolidated-address caveats, names and addresses reported separately from structured formats | Our combined cut and normalization have their own denominator; the source card explicitly warns that raw and aggregated address spans can give different answers |
| [redmadrobot Russian PII benchmark](https://huggingface.co/datasets/redmadrobot-rnd/pii_benchmark) | BIO annotations; merged same-category overlap micro-F1, with exact matching also available | A common PERSON + LOCATION scope for general NER models; disclose label language and chosen thresholds | We score all retained sensitive labels, with a common frozen threshold and label-blind masking recall; neither scope answers the other's question |
| [Text Anonymization Benchmark (TAB)](https://github.com/NorskRegnesentral/text-anonymization-benchmark) | Court documents, direct/quasi-identifiers, masking decisions, confidential attributes and coreference | Distinguish detecting an entity from protecting the person identified by a document | Our TAB/ECHR slice retains selected semantic labels and one reviewed annotation; it does not evaluate TAB's complete privacy task |
| [Samsung CredData](https://github.com/Samsung/CredData) | Manually reviewed credential candidates in source files, with true/false/unknown judgments and tool benchmarks | Explicit labeling rules, negative candidates, credential categories and acquisition metadata | Our cut uses retained annotated lines and normalized character spans; it does not reproduce a whole-repository scan with upstream exclusions and context |
| [SecretBench](https://github.com/setu1421/SecretBench) and [FPSecretBench](https://github.com/setu1421/FPSecretBench) | Candidate software secrets from repositories; manual labels and false positives from scanner evaluation | Analyze false alarms, categories and repository context, not just how many secret-like strings were found | These are comparison references, not added datasets in this snapshot; SecretBench requires the authors' access process |
| [REDACT](https://github.com/guneeshvats/REDACT-PII-Benchmark) | Exact, partial and fuzzy matching; sensitivity and disclosure-form slices | Show weaknesses by type, language and disclosure form instead of hiding them behind one F1 | Our frozen cuts omit some source labels and do not export disclosure-form or sensitivity-tier evaluation; their scores are not the upstream headline results |
| [NVIDIA Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII) | Synthetic persona-grounded text, structured and unstructured formats, train/test splits | Document generation, industry/locale coverage and intended use in a dataset card | It is a training/evaluation resource, not a neutral universal ranking; our sample omits some labels and malformed rows |
| [AI4Privacy PII Masking 200k](https://huggingface.co/datasets/ai4privacy/pii-masking-200k) | Synthetic PII with its own languages, labels and splits | Broad type coverage and explicit dataset metadata | This specific dataset is a comparison reference; related PII datasets are not interchangeable, and training-source reuse must be checked |

Microsoft's evaluation guidance recommends balancing missed PII against false positives and discusses recall-weighted F2. Its generation workflow separates templates across splits to avoid evaluating a model on the same pattern used in training. Both ideas matter more than copying a chart style. [Presidio evaluation guide](https://microsoft.github.io/presidio/evaluation/), [template generation and splitting](https://github.com/microsoft/presidio-research/blob/master/presidio_evaluator/data_generator/README.md).

## Why two correct benchmarks can disagree

Consider a made-up value consisting of two words. A detector returns only the first word. A label-blind overlap measure counts the annotation as detected. A full-hiding measure records a failure because characters remain visible. Exact-boundary matching records a failure because the returned interval is different. A typed measure can record an additional failure if the detector assigned the wrong category.

Now consider two annotated name parts and one predicted full name. Coverage can correctly credit both annotated parts. A conventional one-to-one entity matcher cannot use one predicted entity as two true positives. Both are coherent definitions, but the numerator and the interpretation differ. The legacy exact/overlap diagnostics in this repository are coverage-oriented, normalized, and label-blind; they must not be described as canonical typed NER micro-F1.

| Question | Appropriate measure here | What it does not establish |
|---|---|---|
| Did the detector notice anything in the annotated value? | Detected spans / normalized gold spans | That the whole value is hidden |
| Would the declared masker hide the complete normalized value? | Fully hidden spans / normalized gold spans | That a raw-offset masker behaves the same way |
| Does the detector itself cover the original annotation? | Raw-offset full hiding / original annotations | Correct entity typing or resistance to re-identification |
| How much annotated content remains visible? | Character recall and residual-span counts | The number of people or credentials at risk |
| How much text is masked outside the gold annotations? | Character precision; masking on rows without annotations | A human-confirmed false-alarm rate when annotation is incomplete |
| How does performance vary across sources? | Every dataset, pooled and dataset-macro views | A production distribution or independent observations across related sources |

Character precision, recall and F1 refer to the union of character positions within each row. Per-type character recall counts characters within each annotation, so nested and cross-label overlaps can contribute more than once. Those denominators must not be silently substituted for one another.

## What this repository does well

| Practice | Current implementation | Boundary |
|---|---|---|
| Immutable input identity | Frozen sample IDs and corpus hashes | A hash identifies archived data; it cannot recover an unavailable revision |
| Complete result validation | Dataset fingerprints, duplicate/missing/error-row rejection | Legacy runs without fingerprints are still disclosed |
| Comparable union membership | Every member required, source-overlap exclusions propagated | Fixed unions were inspected on this benchmark; they are not independently selected winners |
| Distinct detection and masking | Full hiding, residual characters, raw offsets and negative-row masking | Boundary expansion is part of the evaluated masker |
| Visible denominators | Per-dataset, language/task and entity-type counts | Missing coverage and absent entity types remain unmeasured |
| Rebuilt publication | Tables and SVGs generated from the numeric snapshot | Regenerating a figure is not rerunning model inference |
| Public-safe packaging | No corpus text or saved predictions in the public tree | Source acquisition and rights remain the upstream owners' responsibility |

These are substantive strengths. They justify publishing a carefully scoped descriptive comparison. They do not justify a claim that every aspect follows a single universal benchmarking standard.

## What remains weaker than a deployment-grade evaluation

1. **Independent selection and test data.** The fixed compositions and thresholds are descriptive operating points. Row hashing is not a substitute for separating templates, documents, source repositories and future traffic before selecting a system. Existing bootstrap results are conditional on the sampled rows; related rows and templates weaken independence.
2. **Uniform annotation policy.** Sources disagree about names, public organizations, locations, usernames, invalid credentials and missing entities. Some source types are dropped. A low score is evidence of disagreement with retained annotations, not proof that the dataset is defective. A manually reviewed sample is needed before assigning a cause.
3. **Supported-scope comparisons.** Measuring general NER across all retained secret labels is useful for a full masking task, but it does not isolate the quality of a model on its advertised types. The same applies to a secret scanner evaluated on names. A future supported-scope leaderboard needs an explicit shared-type intersection for each comparison, not a larger score obtained by silently dropping difficult types.
4. **Independent reproduction and environments.** Publication validation and one source-to-score CPU route are available. Recreating every historical inference environment and every original corpus on another machine is not established. Do not invent dependency pins or claim that a lightweight check certifies full reproduction.
5. **Operational outcomes.** Throughput under concurrent load does not measure single-request latency. Full hiding of annotations does not establish semantic anonymity, prevention of authentication with a partly visible credential, or a production leak probability.

The reproducibility claim should follow the evidence: artifact availability, successful local execution and independent reproduction are separate achievements. [ACM artifact review terminology](https://www.acm.org/publications/policies/artifact-review-and-badging-current).

## Presenting high percentages without selecting away failures

The homepage fixes one already measured four-member composition for category diagnostics. It shows all retained datasets, exact category denominators and both detected and fully hidden spans. It does not pick a different detector for every category.

The dataset heatmap includes all frozen datasets in a stable language/name order. The detailed category report lists every eligible dataset, including high and low results. The example highlights use the same declared minimum of 100 normalized spans per category/dataset cell; this is a display threshold, not a statistical confidence guarantee. Cells below that threshold remain in the detailed tables and CSV.

The mix-sensitivity view applies the same predeclared exclusion of project-generated synthetic sets and corrupted copies to every fixed composition. The remaining sources still include synthetic text. The dataset-influence table describes how removing each individual dataset would change the average, but removes none of them from the headline.

Zero observed failures is written with its denominator. It does not prove zero population risk. New category plots are descriptive point estimates; no unsupported category confidence intervals or statistical winner badges are supplied. Refer to the existing paired tests for the metric and dataset they actually evaluate, not for a different pooled or category-level claim.

## How to use the evidence

Start with the [usage guide](usage.md), select the language and data types present in the intended workload, then inspect [type-level results](../results/by-entity.md), [dataset effects](../results/by-dataset.md) and [measurement coverage](../results/by-language.md). Verify the pinned upstream detector and license before installation. Evaluate shortlisted systems on unseen, permitted data with the same mask postprocessing used in the application.

For a new public claim of improved quality, freeze the candidate configuration, the evaluation subset and the primary metric before looking at test results. Add paired uncertainty appropriate to the sampling unit. For a latency claim, measure the complete application path under the declared concurrency. The current [limitations](limitations.md) remain part of every result.
