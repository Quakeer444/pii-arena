# Project

Public benchmark of PII and secret detectors. English is the publication language.
The initial release is prepared locally; no GitHub remote is configured.

- Keep corpus text, predictions, logs, caches and research history under ignored `.local/`.
- Preserve the scoring protocol, frozen dataset hashes, training-overlap exclusions and coverage labels.
- Generate public figures and tables from `results/snapshot.json`; do not hand-edit numbers.
- Use `uv`. Run `uv run python scripts/verify.py` before preparing a release.
- Corpus examples, regexes and original taxonomy labels retain their measured languages.
- Do not connect a remote, publish, commit or upload artifacts without an explicit request.
