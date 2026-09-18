# Contributing

Contributions are welcome for detector adapters, dataset provenance, scoring defects and reproducible measurements.

## Submit one comparable measurement

1. Choose an existing dataset and detector record, or add their source and license metadata first.
2. Keep source text, model files, predictions and logs under `.local/`.
3. Record the exact model revision, detector version, dataset fingerprint, taxonomy, chunking, threshold, device, processor, threads and concurrent workers.
4. Run the detector, then rescore it with `uv run python scripts/evaluate.py --data <workspace> --dataset <id> --model <id>`. Missing rows, error rows and mismatched fingerprints must fail.
5. Run `uv run python scripts/verify.py`. Run `uv run --group plots python scripts/render.py` only when aggregate publication data changes.

Submit public-safe metadata and aggregates with a synthetic reproduction for adapter or scoring changes. Maintainer review checks provenance, licensing notes, completeness, scoring compatibility and disclosure of execution conditions. Review is best effort; no response-time SLA is promised.

For a new measurement, provide the model revision, detector version, dataset fingerprint, input taxonomy, chunking, threshold, device, processor, thread count and number of concurrent workers. A result without these fields must be labelled as incomplete or legacy, never silently compared as equivalent.

Keep raw corpus text and full predictions in `.local/`. Submit only public-safe metadata and aggregated results after checking the source license. Never submit credentials, internal endpoints, private token formats or incident text. Run `uv run python scripts/scan_secrets.py` with Gitleaks 8.30.1 before a release.

Use the existing scoring implementation. Run `uv run python scripts/verify.py`; regenerate figures with `uv run --group plots python scripts/render.py`. For a scoring change, include one small regression example and explain whether published results need recomputation.

Do not describe a difference within the paired bootstrap interval as a proven gain. Do not rank a composition with missing members as the full composition. Keep trained-on-source measurements out of pooled comparisons.

Protocol changes, dataset snapshot changes and result releases are reviewed separately. Published result bundles remain immutable; corrections create a new release and [changelog](CHANGELOG.md) entry.

This working copy has no public remote yet. Once it is published, use issues for non-sensitive corrections, pull requests for reviewable changes and the private route in [SECURITY.md](SECURITY.md) for vulnerabilities.
