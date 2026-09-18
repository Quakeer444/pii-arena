# What this release does not establish

- It does not establish zero leaks or production suitability for an unseen workload. A detected fragment may remain partly visible.
- Russian secrets have one synthetic dataset. There is no separate multilingual-secrets cut. Multilingual means a collection of mixed-language datasets, not a per-language guarantee.
- Annotation quality is inherited from the sources. Structural and offset checks do not establish that every real sensitive entity was annotated.
- Synthetic sources and corrupted copies contribute substantial weight. Read per-dataset and macro results alongside pooled numbers.
- Source-overlap evidence is incomplete. `train` is a source relationship, not demonstrated memorisation.
- Secret scanners have predictions on only part of the 41 datasets, and Presidio has two. Their absence from the main complete-coverage compositions is disclosed, not treated as proof that scanners are unnecessary.
- The primary compositions are hand-picked. No usable greedy optimum was produced with all candidates.
- CPU throughput is calibrated, and GPU throughput was measured under concurrent load. Neither is a single-request SLA or a monetary cost estimate.
- Compositions containing `bardsai-eu` use an ONNX CPU member. Its CPU cost borrows an eight-thread measurement and is an estimate; a GPU deployment is a mixed-device estimate.
- The CPU queue was intentionally stopped at 440/506 triples; int8 at 117/147. Missing records are not assigned invented performance.
- One open CPU subset has a tested source-to-score route. Exact full inference reproduction still requires historical model environments and source data; the public lightweight validation does not download all models or rerun the full experiment.
- The headline masking view measures residual annotated characters and masking on unannotated rows under the published boundary expansion. It is not a production incident probability, and raw-offset maskers have a different result.
- The sensitivity cut excludes project synthetic sets and corrupted copies, but its remaining 32 datasets still include upstream synthetic material and shared source lineage.
- Source licensing notes are retained from the research audit. Unlicensed, gated and per-file licensed corpora are not bundled with this public tree.
- The legacy normalized exact/overlap diagnostics allow one prediction to cover multiple gold annotations and do not establish typed, one-to-one NER micro-F1.
- New category plots are descriptive point estimates. A fixed minimum count used to select displayed high/low examples is not a statistical confidence bound; all smaller cells remain available.
- Source SECRET labels can include credential-like resource identifiers, salts or UUIDs. Presentation categories preserve this annotation policy and do not prove that every value is a usable secret.
- The TAB/ECHR slice retains selected semantic labels rather than the full source privacy task, including target-specific masking decisions and coreference evaluation.

See [dataset provenance](datasets.md), [detector catalog](models.md), [methodology](methodology.md) and [reproduction](reproduce.md).
