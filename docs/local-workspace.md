# Local research workspace

Everything needed to retain the original research is stored under `.local/`, which is excluded by the root `.gitignore`. Hiding a directory name alone does not exclude it from Git; the ignore rule and publication verification do.

| Location | Contents |
|---|---|
| `.local/research/BENCH/` | All 41 frozen corpora, sample IDs, complete original metadata and materialized raw sources |
| `.local/research/RESULTS/` | All predictions, original reports and timing records |
| `.local/research/SCRIPTS/` | Original research code, preserved as received |
| `.local/research/NODES/` | Original experiment orchestration and local node state |
| `.local/research/logs/` | Research logs and recorded environments |
| `.local/research/hf_cache/` | Existing local model cache |
| `.local/research/.git-history/` | Historical Git files retained as an inactive archive |
| `.local/research/REVIEW/` | Historical audit notes |
| `.local/previews/` | Raster previews of the published vector figures |
| `.local/archive-manifest.json` | Local inventory and verification of the preserved archive |

Original archived materials retain their original language and contents. Public documentation, navigation, explanations and chart labels are English. Multilingual corpus examples, regexes and taxonomy identifiers retain their measured languages.

The original source directory is preserved. The new project has no GitHub remote. Do not use `git add -f .local`; it would override the intended publication boundary. Run `uv run python scripts/verify.py` before preparing a release.

Archived virtual environments retain their original interpreter links and are not portable installations. Recreate an environment before running inference on another machine; the retained data and prediction files do not depend on those links.
