# Secrets: a miss costs more than playing safe

Span recall - the share of annotated spans a detector touched with at least one character. **Missed** - annotated spans not touched at all. **Untouched annotations** are the same missed count stated plainly: it does not mean partially hidden spans are safe. **Unannotated rows touched** - rows without annotations where the detector found something; the volume of that extra masking in characters is next to it. Rows without annotations are not guaranteed to be free of sensitive content.
Score threshold 0.5; spans without a score always count.

## Scanner-coordinate status (2026-09-18 capture and decoded-content correction)

Gitleaks rows were produced by a re-run whose adapter locates the capture-group Secret inside the reported Match range only when the Match contains exactly one copy; with two or more copies, or for a finding that only exists in decoded content, the span keeps the reported range and is counted as unresolved instead of being moved to a copy of the value elsewhere in the document. 38 findings are stored as unresolved and are scored at that reported range, neither dropped nor treated as a false positive; the per-run counts and reasons are in the run inventory. `detect-secrets` was re-run earlier and matched its stored predictions exactly. The other scanners keep stored predictions made before the correction; the rows that use them are marked `historical pre-fix` and can mix with corrected members in the same composition. See the [changelog](../CHANGELOG.md) and [reproduction](../docs/reproduce.md#scanner-adapter-status).

## Scanner runs: status and unresolved findings

`Unresolved` counts findings whose exact secret range the adapter could not place: the span keeps the range the scanner reported (for a decoded finding, the encoded segment) and is scored there, so it can mask more text than the credential occupies. Such a run stays comparable, but the count is part of reading it; per-run counts are in the [run inventory](../results/run-inventory.json) as `unresolved_spans` and `adapter_status`. `Mapping` is the adapter policy recorded in the run metadata; a run without one predates policy recording.

| scanner | release status | runs | datasets | unresolved findings | mapping |
|---|---|---:|---:|---:|---|
| `gitleaks` | corrected-rerun | 10 | 10 | 38 | capture-v2 |
| `detect-secrets` | verified-unchanged | 4 | 4 | 0 | not recorded |
| `betterleaks` | historical-pre-fix | 9 | 9 | 0 | not recorded |
| `trufflehog` | historical-pre-fix | 3 | 3 | 0 | not recorded |
| `noseyparker` | historical-pre-fix | 3 | 3 | 0 | not recorded |
| `titus` | historical-pre-fix | 3 | 3 | 0 | not recorded |
| `kingfisher` | historical-pre-fix | 3 | 3 | 0 | not recorded |
| `credsweeper` | historical-pre-fix | 3 | 3 | 0 | not recorded |
| `credsweeper-noml` | historical-pre-fix | 4 | 4 | 0 | not recorded |
| `deepsecrets` | historical-pre-fix | 4 | 4 | 0 | not recorded |

## Partial compositions: the members that actually ran

A row marked `[k/N]` is not the composition its name lists: only these members have a run on that dataset.

| dataset | composition | k/N | members used |
|---|---|---:|---|
| alexen2 | gitleaks + pplx | 1/2 | `pplx` |
| alexen2 | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| alexen2 | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| alexen2 | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| alexen2 | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| alexen2 | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| alexen2 | gitleaks + all 52 models | 48/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| ameau01 | gitleaks + pplx | 1/2 | `pplx` |
| ameau01 | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| ameau01 | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| ameau01 | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| ameau01 | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| ameau01 | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| ameau01 | gitleaks + all 52 models | 42/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-gherman-onnx` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `nym-small` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| arthur-passwords | gitleaks + pplx | 1/2 | `pplx` |
| arthur-passwords | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| arthur-passwords | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| arthur-passwords | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| arthur-passwords | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| arthur-passwords | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| arthur-passwords | gitleaks + all 52 models | 40/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| corrupt-hivetrace | gitleaks + pplx | 1/2 | `pplx` |
| corrupt-hivetrace | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| corrupt-hivetrace | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| corrupt-hivetrace | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| corrupt-hivetrace | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| corrupt-hivetrace | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| corrupt-hivetrace | gitleaks + all 52 models | 48/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| corrupt-redmadrobot | gitleaks + pplx | 1/2 | `pplx` |
| corrupt-redmadrobot | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| corrupt-redmadrobot | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| corrupt-redmadrobot | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| corrupt-redmadrobot | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| corrupt-redmadrobot | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| corrupt-redmadrobot | gitleaks + all 52 models | 47/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| corrupt-secrets-issues | gitleaks + pplx | 1/2 | `pplx` |
| corrupt-secrets-issues | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| corrupt-secrets-issues | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| corrupt-secrets-issues | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| corrupt-secrets-issues | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| corrupt-secrets-issues | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| corrupt-secrets-issues | gitleaks + all 52 models | 39/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| creddata | gitleaks + pplx | 1/2 | `pplx` |
| creddata | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| creddata | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| creddata | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| creddata | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| creddata | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| creddata | gitleaks + all 52 models | 39/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| dialogpii-en | gitleaks + pplx | 1/2 | `pplx` |
| dialogpii-en | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| dialogpii-en | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| dialogpii-en | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| dialogpii-en | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| dialogpii-en | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| dialogpii-en | gitleaks + all 52 models | 40/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| dialogpii-multi | gitleaks + pplx | 1/2 | `pplx` |
| dialogpii-multi | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| dialogpii-multi | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| dialogpii-multi | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| dialogpii-multi | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| dialogpii-multi | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| dialogpii-multi | gitleaks + all 52 models | 39/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| factrueval | gitleaks + pplx | 1/2 | `pplx` |
| factrueval | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| factrueval | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| factrueval | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| factrueval | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| factrueval | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| factrueval | gitleaks + all 52 models | 48/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| gretel-multi | gitleaks + pplx | 1/2 | `pplx` |
| gretel-multi | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| gretel-multi | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| gretel-multi | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| gretel-multi | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| gretel-multi | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| hivetrace | gitleaks + all 52 models | 52/53 | `gitleaks` + `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-gherman-onnx` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `nym-small` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `presidio-ru` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| jayguard | gitleaks + all 52 models | 49/53 | `gitleaks` + `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| kiji-en | gitleaks + pplx | 1/2 | `pplx` |
| kiji-en | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| kiji-en | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| kiji-en | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| kiji-en | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| kiji-en | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| kiji-en | gitleaks + all 52 models | 40/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| kiji-multi | gitleaks + pplx | 1/2 | `pplx` |
| kiji-multi | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| kiji-multi | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| kiji-multi | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| kiji-multi | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| kiji-multi | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| kiji-multi | gitleaks + all 52 models | 42/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-gherman-onnx` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `nym-small` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| leak-museum | gitleaks + pplx | 1/2 | `pplx` |
| leak-museum | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| leak-museum | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| leak-museum | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| leak-museum | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| leak-museum | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| leak-museum | gitleaks + all 52 models | 40/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| leaky-repo | gitleaks + betterleaks | 1/2 | `gitleaks` |
| leaky-repo | gitleaks + all 52 models | 41/53 | `gitleaks` + `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| multiconer-ru | gitleaks + pplx | 1/2 | `pplx` |
| multiconer-ru | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| multiconer-ru | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| multiconer-ru | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| multiconer-ru | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| multiconer-ru | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| multiconer-ru | gitleaks + all 52 models | 49/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `nym-small` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| nemotron-pii | gitleaks + pplx | 1/2 | `pplx` |
| nemotron-pii | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| nerel | gitleaks + pplx | 1/2 | `pplx` |
| nerel | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| nerel | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| nerel | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| nerel | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| nerel | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| nerel | gitleaks + all 52 models | 47/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| nym-en | gitleaks + pplx | 1/2 | `pplx` |
| nym-en | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| nym-en | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| nym-en | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| nym-en | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| nym-en | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| nym-multi | gitleaks + pplx | 1/2 | `pplx` |
| nym-multi | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| nym-multi | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| nym-multi | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| nym-multi | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| nym-multi | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| privy | gitleaks + pplx | 1/2 | `pplx` |
| privy | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| privy | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| privy | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| privy | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| privy | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| redact-multi | gitleaks + pplx | 1/2 | `pplx` |
| redact-multi | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| redact-multi | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| redact-multi | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| redact-multi | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| redact-multi | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| redact-multi | gitleaks + all 52 models | 39/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| redact-ru | gitleaks + pplx | 1/2 | `pplx` |
| redact-ru | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| redact-ru | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| redact-ru | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| redact-ru | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| redact-ru | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| redact-ru | gitleaks + all 52 models | 47/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| redmadrobot | gitleaks + all 52 models | 51/53 | `gitleaks` + `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `nym-small` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `presidio-ru` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| rubai-ru | gitleaks + pplx | 1/2 | `pplx` |
| rubai-ru | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| rubai-ru | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| rubai-ru | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| rubai-ru | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| rubai-ru | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| rubai-ru | gitleaks + all 52 models | 47/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| secrets-issues | gitleaks + all 52 models | 42/53 | `gitleaks` + `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `nym-small` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| synth-env-configs | gitleaks + pplx | 1/2 | `pplx` |
| synth-env-configs | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| synth-env-configs | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| synth-env-configs | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| synth-env-configs | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| synth-env-configs | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| synth-env-configs | gitleaks + all 52 models | 39/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| synth-jira-comments | gitleaks + pplx | 1/2 | `pplx` |
| synth-jira-comments | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| synth-jira-comments | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| synth-jira-comments | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| synth-jira-comments | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| synth-jira-comments | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| synth-jira-comments | gitleaks + all 52 models | 47/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| synth-ru-tickets | gitleaks + pplx | 1/2 | `pplx` |
| synth-ru-tickets | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| synth-ru-tickets | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| synth-ru-tickets | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| synth-ru-tickets | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| synth-ru-tickets | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| synth-ru-tickets | gitleaks + all 52 models | 49/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `nym-small` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| synth-secrets-en | gitleaks + pplx | 1/2 | `pplx` |
| synth-secrets-en | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| synth-secrets-en | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| synth-secrets-en | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| synth-secrets-en | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| synth-secrets-en | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| synth-secrets-en | gitleaks + all 52 models | 39/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| synth-secrets-ru | gitleaks + pplx | 1/2 | `pplx` |
| synth-secrets-ru | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| synth-secrets-ru | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| synth-secrets-ru | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| synth-secrets-ru | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| synth-secrets-ru | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| synth-secrets-ru | gitleaks + all 52 models | 47/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| synth-wiki-tables | gitleaks + pplx | 1/2 | `pplx` |
| synth-wiki-tables | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| synth-wiki-tables | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| synth-wiki-tables | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| synth-wiki-tables | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| synth-wiki-tables | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| synth-wiki-tables | gitleaks + all 52 models | 47/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-multi-v21-ru` + `gliner-nvidia` + `gliner-nvidia-ru` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner-urchade-ru` + `gliner2-fastino` + `gliner2-fastino-ru` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-omni-ru` + `gliner2-hivetrace-uni` + `gliner2-hivetrace-uni-ru` + `gliner2-large` + `gliner2-vladlinv` + `gliner2-vladlinv-ru` + `gliner25-fastino` + `gliner25-fastino-ru` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| tab-echr | gitleaks + pplx | 1/2 | `pplx` |
| tab-echr | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| tab-echr | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| tab-echr | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| tab-echr | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| tab-echr | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| tab-echr | gitleaks + all 52 models | 42/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-gherman-onnx` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `nym-small` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pii-shield-onnx` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |
| tonicai | gitleaks + pplx | 1/2 | `pplx` |
| tonicai | gitleaks + pplx + gliner-nvidia | 2/3 | `pplx` + `gliner-nvidia` |
| tonicai | gitleaks + pplx + gliner-nvidia + ru-legal-ner | 3/4 | `pplx` + `gliner-nvidia` + `ru-legal-ner` |
| tonicai | gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 3/4 | `pplx` + `opf-ru-v2` + `gliner-nvidia` |
| tonicai | gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 4/5 | `pplx` + `opf-ru-v2` + `gliner-nvidia` + `ru-legal-ner` |
| tonicai | gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 3/4 | `pplx` + `ru-legal-ner` + `gliner2-vladlinv` |
| tonicai | gitleaks + all 52 models | 39/53 | `apararti` + `bardsai-eu` + `davlan-mbert` + `davlan-xlmr` + `fef2-secret-ru` + `gliner-multi-v21` + `gliner-nvidia` + `gliner-pii-base` + `gliner-pii-edge` + `gliner-stream-pii` + `gliner-urchade` + `gliner2-fastino` + `gliner2-hivetrace-omni` + `gliner2-hivetrace-uni` + `gliner2-large` + `gliner2-vladlinv` + `gliner25-fastino` + `gravitee-small` + `kalyan-ettin` + `mmbert32k` + `natasha` + `ner-ru-gherman` + `ner-ru-yqelz` + `nuner-zero` + `nym-base` + `openai-base` + `openmed-multilingual` + `openmed-nemotron` + `opf-kz-ru` + `opf-ru` + `opf-ru-v2` + `pplx` + `ru-legal-ner` + `ru-pii-ner` + `rules-ru` + `spacy-alrosait` + `spacy-ru-lg` + `stanza-ru` + `traciora` |

## arthur-passwords (516 rows, 280 annotated spans, 236 rows without annotations)

| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |
|---|---|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - | - | - |
| betterleaks | - | - | - | - | - | - | - |
| gitleaks + betterleaks | - | - | - | - | - | - | - |
| pplx | 1.000 | **0** | 0.173 | 1.000 | 0.295 | 227/236 | 7898 (17.7% of the text) |
| gitleaks + pplx [1/2] | 1.000 | **0** | 0.173 | 1.000 | 0.295 | 227/236 | 7898 (17.7% of the text) |
| gitleaks + pplx + gliner-nvidia [2/3] | 1.000 | **0** | 0.172 | 1.000 | 0.294 | 229/236 | 8022 (18.0% of the text) |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner [3/4] | 1.000 | **0** | 0.165 | 1.000 | 0.283 | 232/236 | 8425 (18.9% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia [3/4] | 1.000 | **0** | 0.170 | 1.000 | 0.291 | 230/236 | 8137 (18.3% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner [4/5] | 1.000 | **0** | 0.163 | 1.000 | 0.280 | 232/236 | 8527 (19.1% of the text) |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv [3/4] | 1.000 | **0** | 0.165 | 1.000 | 0.284 | 231/236 | 8331 (18.7% of the text) |
| pplx + gliner2-fastino | 1.000 | **0** | 0.171 | 1.000 | 0.292 | 228/236 | 8167 (18.3% of the text) |
| pplx + gliner2-fastino + mmbert32k | 1.000 | **0** | 0.160 | 1.000 | 0.276 | 235/236 | 8883 (19.9% of the text) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 1.000 | **0** | 0.151 | 1.000 | 0.262 | 236/236 | 9587 (21.5% of the text) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 1.000 | **0** | 0.245 | 1.000 | 0.394 | 209/236 | 5578 (12.5% of the text) |
| gitleaks + all 52 models [40/53] | 1.000 | **0** | 0.075 | 1.000 | 0.140 | 236/236 | 20796 (46.7% of the text) |

`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.

## corrupt-secrets-issues (500 rows, 288 annotated spans, 250 rows without annotations)

| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |
|---|---|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - | - | - |
| betterleaks | - | - | - | - | - | - | - |
| gitleaks + betterleaks | - | - | - | - | - | - | - |
| pplx | 0.958 | **12** | 0.183 | 0.943 | 0.306 | 202/250 | 59676 (10.1% of the text) |
| gitleaks + pplx [1/2] | 0.958 | **12** | 0.183 | 0.943 | 0.306 | 202/250 | 59676 (10.1% of the text) |
| gitleaks + pplx + gliner-nvidia [2/3] | 0.965 | **10** | 0.165 | 0.947 | 0.282 | 235/250 | 69943 (11.8% of the text) |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner [3/4] | 0.972 | **8** | 0.121 | 0.950 | 0.214 | 248/250 | 115623 (19.6% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia [3/4] | 0.993 | **2** | 0.153 | 0.959 | 0.264 | 238/250 | 76606 (13.0% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner [4/5] | 0.993 | **2** | 0.118 | 0.960 | 0.211 | 248/250 | 118582 (20.1% of the text) |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv [3/4] | 0.972 | **8** | 0.127 | 0.947 | 0.224 | 243/250 | 107831 (18.3% of the text) |
| pplx + gliner2-fastino | 0.972 | **8** | 0.145 | 0.949 | 0.251 | 245/250 | 84087 (14.2% of the text) |
| pplx + gliner2-fastino + mmbert32k | 0.986 | **4** | 0.122 | 0.957 | 0.217 | 250/250 | 105898 (17.9% of the text) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 1.000 | **0** | 0.116 | 0.964 | 0.207 | 250/250 | 112610 (19.1% of the text) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 0.941 | **17** | 0.301 | 0.914 | 0.453 | 155/250 | 17737 (3.0% of the text) |
| gitleaks + all 52 models [39/53] | 1.000 | **0** | 0.054 | 0.986 | 0.102 | 250/250 | 307828 (52.1% of the text) |

`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.

## creddata (1477 rows, 776 annotated spans, 727 rows without annotations)

| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |
|---|---|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - | - | - |
| betterleaks | - | - | - | - | - | - | - |
| gitleaks + betterleaks | - | - | - | - | - | - | - |
| pplx | 0.942 | **45** | 0.747 | 0.821 | 0.782 | 169/727 | 10878 (7.2% of the text) |
| gitleaks + pplx [1/2] | 0.942 | **45** | 0.747 | 0.821 | 0.782 | 169/727 | 10878 (7.2% of the text) |
| gitleaks + pplx + gliner-nvidia [2/3] | 0.983 | **13** | 0.674 | 0.845 | 0.750 | 477/727 | 18553 (12.3% of the text) |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner [3/4] | 1.000 | **0** | 0.602 | 0.952 | 0.737 | 585/727 | 29230 (19.4% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia [3/4] | 0.996 | **3** | 0.691 | 0.989 | 0.813 | 485/727 | 20055 (13.3% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner [4/5] | 1.000 | **0** | 0.605 | 0.992 | 0.752 | 588/727 | 29650 (19.7% of the text) |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv [3/4] | 1.000 | **0** | 0.630 | 0.951 | 0.758 | 461/727 | 25232 (16.8% of the text) |
| pplx + gliner2-fastino | 0.983 | **13** | 0.620 | 0.871 | 0.724 | 596/727 | 23213 (15.4% of the text) |
| pplx + gliner2-fastino + mmbert32k | 0.999 | **1** | 0.566 | 0.896 | 0.694 | 627/727 | 30623 (20.3% of the text) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 0.999 | **1** | 0.569 | 0.963 | 0.715 | 628/727 | 33016 (21.9% of the text) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 0.964 | **28** | 0.881 | 0.835 | 0.857 | 129/727 | 4317 (2.9% of the text) |
| gitleaks + all 52 models [39/53] | 1.000 | **0** | 0.376 | 0.999 | 0.546 | 727/727 | 75931 (50.4% of the text) |

`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.

## leak-museum (97 rows, 101 annotated spans, 45 rows without annotations)

| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |
|---|---|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - | - | - |
| betterleaks | - | - | - | - | - | - | - |
| gitleaks + betterleaks | - | - | - | - | - | - | - |
| pplx | 0.832 | **17** | 0.501 | 0.760 | 0.604 | 10/45 | 1552 (4.7% of the text) |
| gitleaks + pplx [1/2] | 0.832 | **17** | 0.501 | 0.760 | 0.604 | 10/45 | 1552 (4.7% of the text) |
| gitleaks + pplx + gliner-nvidia [2/3] | 0.891 | **11** | 0.448 | 0.844 | 0.585 | 20/45 | 2030 (6.2% of the text) |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner [3/4] | 0.921 | **8** | 0.366 | 0.860 | 0.514 | 34/45 | 2640 (8.0% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia [3/4] | 0.911 | **9** | 0.458 | 0.888 | 0.604 | 20/45 | 2064 (6.3% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner [4/5] | 0.941 | **6** | 0.378 | 0.904 | 0.533 | 34/45 | 2640 (8.0% of the text) |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv [3/4] | 0.881 | **12** | 0.390 | 0.782 | 0.520 | 28/45 | 2168 (6.6% of the text) |
| pplx + gliner2-fastino | 0.980 | **2** | 0.263 | 0.906 | 0.408 | 42/45 | 4704 (14.3% of the text) |
| pplx + gliner2-fastino + mmbert32k | 0.980 | **2** | 0.246 | 0.908 | 0.388 | 43/45 | 4881 (14.9% of the text) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 0.980 | **2** | 0.241 | 0.908 | 0.380 | 43/45 | 5005 (15.3% of the text) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 0.762 | **24** | 0.638 | 0.682 | 0.659 | 5/45 | 865 (2.6% of the text) |
| gitleaks + all 52 models [40/53] | 1.000 | **0** | 0.092 | 1.000 | 0.168 | 45/45 | 14929 (45.5% of the text) |

`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.

## leaky-repo (59 rows, 95 annotated spans, 16 rows without annotations)

| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |
|---|---|---|---|---|---|---|---|
| gitleaks | 0.232 | **73** | 1.000 | 0.545 | 0.705 | 0/16 | 0 (0.0% of the text) |
| betterleaks | - | - | - | - | - | - | - |
| gitleaks + betterleaks [1/2] | 0.232 | **73** | 1.000 | 0.545 | 0.705 | 0/16 | 0 (0.0% of the text) |
| pplx | 0.926 | **7** | 0.675 | 0.755 | 0.713 | 11/16 | 998 (3.3% of the text) |
| gitleaks + pplx | 0.926 | **7** | 0.713 | 0.904 | 0.797 | 11/16 | 998 (3.3% of the text) |
| gitleaks + pplx + gliner-nvidia | 0.979 | **2** | 0.700 | 0.919 | 0.795 | 11/16 | 1175 (3.9% of the text) |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner | 0.989 | **1** | 0.555 | 0.983 | 0.709 | 15/16 | 3479 (11.6% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 0.989 | **1** | 0.703 | 0.997 | 0.825 | 12/16 | 1269 (4.2% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 0.989 | **1** | 0.553 | 0.998 | 0.711 | 15/16 | 3554 (11.8% of the text) |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 0.968 | **3** | 0.563 | 0.979 | 0.715 | 15/16 | 3315 (11.0% of the text) |
| pplx + gliner2-fastino | 0.989 | **1** | 0.511 | 0.848 | 0.638 | 13/16 | 3393 (11.3% of the text) |
| pplx + gliner2-fastino + mmbert32k | 0.989 | **1** | 0.482 | 0.876 | 0.622 | 15/16 | 3922 (13.1% of the text) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 0.989 | **1** | 0.502 | 0.987 | 0.666 | 15/16 | 4087 (13.6% of the text) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 0.895 | **10** | 0.859 | 0.733 | 0.791 | 2/16 | 73 (0.2% of the text) |
| gitleaks + all 52 models [41/53] | 1.000 | **0** | 0.229 | 1.000 | 0.373 | 16/16 | 15307 (51.0% of the text) |

`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.

## secrets-issues (500 rows, 288 annotated spans, 250 rows without annotations)

| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |
|---|---|---|---|---|---|---|---|
| gitleaks | 0.549 | **130** | 0.428 | 0.727 | 0.538 | 16/250 | 4720 (0.8% of the text) |
| betterleaks `historical pre-fix` | 0.573 | **123** | 0.432 | 0.726 | 0.541 | 32/250 | 5812 (1.0% of the text) |
| gitleaks + betterleaks `historical pre-fix` | 0.587 | **119** | 0.413 | 0.732 | 0.528 | 33/250 | 5917 (1.0% of the text) |
| pplx | 0.958 | **12** | 0.173 | 0.878 | 0.288 | 191/250 | 57544 (9.9% of the text) |
| gitleaks + pplx | 0.976 | **7** | 0.173 | 0.948 | 0.292 | 191/250 | 60470 (10.4% of the text) |
| gitleaks + pplx + gliner-nvidia | 0.983 | **5** | 0.161 | 0.954 | 0.275 | 227/250 | 69704 (12.0% of the text) |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner | 0.990 | **3** | 0.124 | 0.957 | 0.219 | 244/250 | 99338 (17.1% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 0.990 | **3** | 0.154 | 0.956 | 0.265 | 229/250 | 72471 (12.4% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 0.990 | **3** | 0.122 | 0.958 | 0.217 | 244/250 | 100453 (17.2% of the text) |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 0.990 | **3** | 0.129 | 0.954 | 0.228 | 235/250 | 91603 (15.7% of the text) |
| pplx + gliner2-fastino | 0.976 | **7** | 0.146 | 0.957 | 0.253 | 243/250 | 82299 (14.1% of the text) |
| pplx + gliner2-fastino + mmbert32k | 0.979 | **6** | 0.121 | 0.958 | 0.215 | 250/250 | 108424 (18.6% of the text) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 1.000 | **0** | 0.115 | 0.966 | 0.206 | 250/250 | 115510 (19.8% of the text) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 0.958 | **12** | 0.298 | 0.926 | 0.451 | 151/250 | 17672 (3.0% of the text) |
| gitleaks + all 52 models [42/53] | 1.000 | **0** | 0.050 | 0.990 | 0.095 | 250/250 | 326629 (56.1% of the text) |

`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.

## secrets-rules (1496 rows, 746 annotated spans, 750 rows without annotations)

| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |
|---|---|---|---|---|---|---|---|
| gitleaks | train | train | train | train | train | train | train |
| betterleaks | train | train | train | train | train | train | train |
| gitleaks + betterleaks | train | train | train | train | train | train | train |
| pplx | 0.961 | **29** | 0.625 | 0.949 | 0.753 | 385/750 | 21139 (36.7% of the text) |
| gitleaks + pplx | train | train | train | train | train | train | train |
| gitleaks + pplx + gliner-nvidia | train | train | train | train | train | train | train |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner | train | train | train | train | train | train | train |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia | train | train | train | train | train | train | train |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | train | train | train | train | train | train | train |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | train | train | train | train | train | train | train |
| pplx + gliner2-fastino | 0.993 | **5** | 0.518 | 0.980 | 0.677 | 638/750 | 32915 (57.2% of the text) |
| pplx + gliner2-fastino + mmbert32k | 1.000 | **0** | 0.453 | 1.000 | 0.623 | 713/750 | 40757 (70.8% of the text) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 1.000 | **0** | 0.448 | 1.000 | 0.619 | 716/750 | 41382 (71.9% of the text) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 0.971 | **22** | 0.621 | 0.957 | 0.754 | 389/750 | 21782 (37.8% of the text) |
| gitleaks + all 52 models | train | train | train | train | train | train | train |

`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.

## synth-env-configs (400 rows, 392 annotated spans, 200 rows without annotations)

| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |
|---|---|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - | - | - |
| betterleaks | - | - | - | - | - | - | - |
| gitleaks + betterleaks | - | - | - | - | - | - | - |
| pplx | 1.000 | **0** | 0.265 | 0.996 | 0.418 | 193/200 | 25405 (29.2% of the text) |
| gitleaks + pplx [1/2] | 1.000 | **0** | 0.265 | 0.996 | 0.418 | 193/200 | 25405 (29.2% of the text) |
| gitleaks + pplx + gliner-nvidia [2/3] | 1.000 | **0** | 0.245 | 0.996 | 0.394 | 198/200 | 28781 (33.1% of the text) |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner [3/4] | 1.000 | **0** | 0.225 | 0.997 | 0.368 | 199/200 | 32512 (37.4% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia [3/4] | 1.000 | **0** | 0.235 | 0.997 | 0.380 | 198/200 | 30349 (34.9% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner [4/5] | 1.000 | **0** | 0.221 | 0.997 | 0.361 | 199/200 | 33293 (38.3% of the text) |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv [3/4] | 1.000 | **0** | 0.238 | 0.997 | 0.384 | 194/200 | 29965 (34.5% of the text) |
| pplx + gliner2-fastino | 1.000 | **0** | 0.231 | 0.996 | 0.375 | 200/200 | 31877 (36.7% of the text) |
| pplx + gliner2-fastino + mmbert32k | 1.000 | **0** | 0.205 | 0.997 | 0.340 | 200/200 | 37836 (43.6% of the text) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 1.000 | **0** | 0.201 | 0.998 | 0.335 | 200/200 | 38909 (44.8% of the text) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 0.980 | **8** | 0.309 | 0.835 | 0.451 | 187/200 | 17556 (20.2% of the text) |
| gitleaks + all 52 models [39/53] | 1.000 | **0** | 0.146 | 1.000 | 0.255 | 200/200 | 55147 (63.5% of the text) |

`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.

## synth-secrets-en (600 rows, 581 annotated spans, 300 rows without annotations)

| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |
|---|---|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - | - | - |
| betterleaks | - | - | - | - | - | - | - |
| gitleaks + betterleaks | - | - | - | - | - | - | - |
| pplx | 0.998 | **1** | 0.198 | 0.981 | 0.330 | 275/300 | 53318 (43.9% of the text) |
| gitleaks + pplx [1/2] | 0.998 | **1** | 0.198 | 0.981 | 0.330 | 275/300 | 53318 (43.9% of the text) |
| gitleaks + pplx + gliner-nvidia [2/3] | 1.000 | **0** | 0.194 | 0.983 | 0.324 | 286/300 | 55796 (46.0% of the text) |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner [3/4] | 1.000 | **0** | 0.180 | 0.983 | 0.305 | 294/300 | 60855 (50.1% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia [3/4] | 1.000 | **0** | 0.186 | 0.993 | 0.313 | 288/300 | 59037 (48.6% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner [4/5] | 1.000 | **0** | 0.176 | 0.993 | 0.298 | 294/300 | 63256 (52.1% of the text) |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv [3/4] | 1.000 | **0** | 0.182 | 0.983 | 0.308 | 290/300 | 59673 (49.2% of the text) |
| pplx + gliner2-fastino | 0.998 | **1** | 0.196 | 0.984 | 0.327 | 285/300 | 54705 (45.1% of the text) |
| pplx + gliner2-fastino + mmbert32k | 1.000 | **0** | 0.177 | 0.986 | 0.300 | 300/300 | 63390 (52.2% of the text) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 1.000 | **0** | 0.176 | 0.987 | 0.298 | 300/300 | 64076 (52.8% of the text) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 0.976 | **14** | 0.255 | 0.881 | 0.395 | 276/300 | 36673 (30.2% of the text) |
| gitleaks + all 52 models [39/53] | 1.000 | **0** | 0.129 | 1.000 | 0.228 | 300/300 | 92225 (76.0% of the text) |

`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.

## synth-secrets-ru (600 rows, 581 annotated spans, 300 rows without annotations)

| composition | span recall | missed | char P | char R | F1 | unannotated rows touched | over-masked |
|---|---|---|---|---|---|---|---|
| gitleaks | - | - | - | - | - | - | - |
| betterleaks | - | - | - | - | - | - | - |
| gitleaks + betterleaks | - | - | - | - | - | - | - |
| pplx | 1.000 | **0** | 0.197 | 0.983 | 0.328 | 285/300 | 54077 (44.7% of the text) |
| gitleaks + pplx [1/2] | 1.000 | **0** | 0.197 | 0.983 | 0.328 | 285/300 | 54077 (44.7% of the text) |
| gitleaks + pplx + gliner-nvidia [2/3] | 1.000 | **0** | 0.192 | 0.983 | 0.321 | 289/300 | 56966 (47.1% of the text) |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner [3/4] | 1.000 | **0** | 0.178 | 0.983 | 0.302 | 292/300 | 62044 (51.3% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia [3/4] | 1.000 | **0** | 0.183 | 0.994 | 0.309 | 290/300 | 60631 (50.1% of the text) |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner [4/5] | 1.000 | **0** | 0.173 | 0.995 | 0.295 | 292/300 | 64477 (53.3% of the text) |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv [3/4] | 1.000 | **0** | 0.180 | 0.983 | 0.305 | 292/300 | 60526 (50.0% of the text) |
| pplx + gliner2-fastino | 1.000 | **0** | 0.195 | 0.985 | 0.325 | 289/300 | 55071 (45.5% of the text) |
| pplx + gliner2-fastino + mmbert32k | 1.000 | **0** | 0.176 | 0.985 | 0.299 | 300/300 | 63552 (52.5% of the text) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 1.000 | **0** | 0.175 | 0.986 | 0.297 | 300/300 | 64314 (53.1% of the text) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 0.981 | **11** | 0.255 | 0.903 | 0.397 | 281/300 | 37565 (31.0% of the text) |
| gitleaks + all 52 models [47/53] | 1.000 | **0** | 0.129 | 1.000 | 0.229 | 300/300 | 92561 (76.5% of the text) |

`[k/N]` - only k of the N members of the composition have a run on this set, so the row is that partial composition, not the one the name lists; the members that ran are listed above. `historical pre-fix` - the row uses a scanner whose stored predictions predate the 2026-09-18 offset and capture-position correction.

## Every set: annotated spans nobody noticed at all

The number is spans not touched by a single character, the share of all spans of the set in brackets. `[k/N]` - only k of the N members of the composition have a run on that set: the cell is that partial composition. `-` - a vote with an incomplete composition, or nobody ran. `historical pre-fix` - the named composition includes a scanner with stored pre-correction predictions; the per-set tables above name the members that actually ran.

| composition | alexen2 | alrosait | ameau01 | arthur-passwords | corrupt-hivetrace | corrupt-redmadrobot | corrupt-secrets-issues | creddata | dialogpii-en | dialogpii-multi | factrueval | gretel-multi | hivetrace | jayguard | kiji-en | kiji-multi | leak-museum | leaky-repo | multiconer-ru | nemotron-pii | nerel | nym-en | nym-multi | nym-ru | privy | redact-multi | redact-ru | redmadrobot | rubai-ru | russian-pii-66k | scanpatch | secrets-issues | secrets-rules | synth-env-configs | synth-jira-comments | synth-ru-tickets | synth-secrets-en | synth-secrets-ru | synth-wiki-tables | tab-echr | tonicai |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gitleaks | - | 1862 (100.0%) | - | - | - | - | - | - | - | - | - | - | 1650 (99.0%) | 1195 (100.0%) | - | - | - | 73 (76.8%) | - | - | - | - | - | 9497 (100.0%) | - | - | - | 5516 (100.0%) | - | 4805 (100.0%) | 8708 (100.0%) | 130 (45.1%) | train | - | - | - | - | - | - | - | - |
| betterleaks `historical pre-fix` | - | 1862 (100.0%) | - | - | - | - | - | - | - | - | - | - | 1650 (99.0%) | 1195 (100.0%) | - | - | - | - | - | - | - | - | - | 9497 (100.0%) | - | - | - | 5516 (100.0%) | - | 4805 (100.0%) | 8708 (100.0%) | 123 (42.7%) | train | - | - | - | - | - | - | - | - |
| gitleaks + betterleaks `historical pre-fix` | - | 1862 (100.0%) | - | - | - | - | - | - | - | - | - | - | 1650 (99.0%) | 1195 (100.0%) | - | - | - | 73 (76.8%) [1/2] | - | - | - | - | - | 9497 (100.0%) | - | - | - | 5516 (100.0%) | - | 4805 (100.0%) | 8708 (100.0%) | 119 (41.3%) | train | - | - | - | - | - | - | - | - |
| pplx | 66 (5.2%) | 10 (0.5%) | 393 (17.5%) | 0 (0.0%) | 58 (3.5%) | 748 (13.5%) | 12 (4.2%) | 45 (5.8%) | 744 (24.1%) | 3017 (29.2%) | 6964 (87.4%) | 818 (18.2%) | 45 (2.7%) | 197 (16.5%) | 310 (4.1%) | 318 (4.2%) | 17 (16.8%) | 7 (7.4%) | 975 (80.7%) | 1149 (12.2%) | 21282 (87.3%) | 138 (3.9%) | 227 (2.8%) | 374 (3.9%) | 96 (5.1%) | 2427 (10.6%) | 881 (9.5%) | 775 (14.1%) | 16 (0.5%) | 11 (0.2%) | 1084 (12.4%) | 12 (4.2%) | 29 (3.9%) | 0 (0.0%) | 2 (0.1%) | 849 (2.6%) | 1 (0.2%) | 0 (0.0%) | 734 (5.6%) | 2314 (60.4%) | 502 (20.8%) |
| gitleaks + pplx | 66 (5.2%) [1/2] | 10 (0.5%) | 393 (17.5%) [1/2] | 0 (0.0%) [1/2] | 58 (3.5%) [1/2] | 748 (13.5%) [1/2] | 12 (4.2%) [1/2] | 45 (5.8%) [1/2] | 744 (24.1%) [1/2] | 3017 (29.2%) [1/2] | 6964 (87.4%) [1/2] | 818 (18.2%) [1/2] | 45 (2.7%) | 197 (16.5%) | 310 (4.1%) [1/2] | 318 (4.2%) [1/2] | 17 (16.8%) [1/2] | 7 (7.4%) | 975 (80.7%) [1/2] | 1149 (12.2%) [1/2] | 21282 (87.3%) [1/2] | 138 (3.9%) [1/2] | 227 (2.8%) [1/2] | 374 (3.9%) | 96 (5.1%) [1/2] | 2427 (10.6%) [1/2] | 881 (9.5%) [1/2] | 775 (14.1%) | 16 (0.5%) [1/2] | 11 (0.2%) | 1084 (12.4%) | 7 (2.4%) | train | 0 (0.0%) [1/2] | 2 (0.1%) [1/2] | 849 (2.6%) [1/2] | 1 (0.2%) [1/2] | 0 (0.0%) [1/2] | 734 (5.6%) [1/2] | 2314 (60.4%) [1/2] | 502 (20.8%) [1/2] |
| gitleaks + pplx + gliner-nvidia | 6 (0.5%) [2/3] | 2 (0.1%) | 154 (6.9%) [2/3] | 0 (0.0%) [2/3] | 25 (1.5%) [2/3] | 286 (5.2%) [2/3] | 10 (3.5%) [2/3] | 13 (1.7%) [2/3] | 287 (9.3%) [2/3] | 1710 (16.5%) [2/3] | 1938 (24.3%) [2/3] | 516 (11.5%) [2/3] | 12 (0.7%) | 113 (9.5%) | 21 (0.3%) [2/3] | 49 (0.6%) [2/3] | 11 (10.9%) [2/3] | 2 (2.1%) | 432 (35.8%) [2/3] | train | 7383 (30.3%) [2/3] | 19 (0.5%) [2/3] | 69 (0.8%) [2/3] | 53 (0.6%) | 15 (0.8%) [2/3] | 957 (4.2%) [2/3] | 286 (3.1%) [2/3] | 134 (2.4%) | 15 (0.4%) [2/3] | 0 (0.0%) | 401 (4.6%) | 5 (1.7%) | train | 0 (0.0%) [2/3] | 0 (0.0%) [2/3] | 81 (0.3%) [2/3] | 0 (0.0%) [2/3] | 0 (0.0%) [2/3] | 156 (1.2%) [2/3] | 567 (14.8%) [2/3] | 111 (4.6%) [2/3] |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner | 5 (0.4%) [3/4] | 1 (0.1%) | 149 (6.6%) [3/4] | 0 (0.0%) [3/4] | 19 (1.1%) [3/4] | 131 (2.4%) [3/4] | 8 (2.8%) [3/4] | 0 (0.0%) [3/4] | 270 (8.7%) [3/4] | 961 (9.3%) [3/4] | 1202 (15.1%) [3/4] | 282 (6.3%) [3/4] | 12 (0.7%) | 91 (7.6%) | 20 (0.3%) [3/4] | 31 (0.4%) [3/4] | 8 (7.9%) [3/4] | 1 (1.1%) | 259 (21.4%) [3/4] | train | 3637 (14.9%) [3/4] | 15 (0.4%) [3/4] | 29 (0.4%) [3/4] | 16 (0.2%) | 11 (0.6%) [3/4] | 457 (2.0%) [3/4] | 196 (2.1%) [3/4] | 54 (1.0%) | 8 (0.2%) [3/4] | 0 (0.0%) | 199 (2.3%) | 3 (1.0%) | train | 0 (0.0%) [3/4] | 0 (0.0%) [3/4] | 14 (0.0%) [3/4] | 0 (0.0%) [3/4] | 0 (0.0%) [3/4] | 33 (0.3%) [3/4] | 521 (13.6%) [3/4] | 100 (4.1%) [3/4] |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 6 (0.5%) [3/4] | 1 (0.1%) | 151 (6.7%) [3/4] | 0 (0.0%) [3/4] | 15 (0.9%) [3/4] | 247 (4.5%) [3/4] | 2 (0.7%) [3/4] | 3 (0.4%) [3/4] | 279 (9.0%) [3/4] | 1604 (15.5%) [3/4] | 1789 (22.5%) [3/4] | 506 (11.3%) [3/4] | 6 (0.4%) | 108 (9.0%) | 20 (0.3%) [3/4] | 46 (0.6%) [3/4] | 9 (8.9%) [3/4] | 1 (1.1%) | 412 (34.1%) [3/4] | train | 6623 (27.2%) [3/4] | 17 (0.5%) [3/4] | 66 (0.8%) [3/4] | 22 (0.2%) | 11 (0.6%) [3/4] | 865 (3.8%) [3/4] | 242 (2.6%) [3/4] | 115 (2.1%) | 14 (0.4%) [3/4] | 0 (0.0%) | 340 (3.9%) | 3 (1.0%) | train | 0 (0.0%) [3/4] | 0 (0.0%) [3/4] | 39 (0.1%) [3/4] | 0 (0.0%) [3/4] | 0 (0.0%) [3/4] | 136 (1.0%) [3/4] | 548 (14.3%) [3/4] | 110 (4.6%) [3/4] |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 5 (0.4%) [4/5] | 0 (0.0%) | 146 (6.5%) [4/5] | 0 (0.0%) [4/5] | 11 (0.7%) [4/5] | 117 (2.1%) [4/5] | 2 (0.7%) [4/5] | 0 (0.0%) [4/5] | 265 (8.6%) [4/5] | 887 (8.6%) [4/5] | 1162 (14.6%) [4/5] | 277 (6.2%) [4/5] | 6 (0.4%) | 89 (7.4%) | 19 (0.2%) [4/5] | 28 (0.4%) [4/5] | 6 (5.9%) [4/5] | 1 (1.1%) | 256 (21.2%) [4/5] | train | 3525 (14.5%) [4/5] | 13 (0.4%) [4/5] | 29 (0.4%) [4/5] | 15 (0.2%) | 10 (0.5%) [4/5] | 416 (1.8%) [4/5] | 176 (1.9%) [4/5] | 48 (0.9%) | 8 (0.2%) [4/5] | 0 (0.0%) | 177 (2.0%) | 3 (1.0%) | train | 0 (0.0%) [4/5] | 0 (0.0%) [4/5] | 9 (0.0%) [4/5] | 0 (0.0%) [4/5] | 0 (0.0%) [4/5] | 33 (0.3%) [4/5] | 506 (13.2%) [4/5] | 100 (4.1%) [4/5] |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 0 (0.0%) [3/4] | 3 (0.2%) | 368 (16.4%) [3/4] | 0 (0.0%) [3/4] | 25 (1.5%) [3/4] | 295 (5.3%) [3/4] | 8 (2.8%) [3/4] | 0 (0.0%) [3/4] | 666 (21.6%) [3/4] | 1359 (13.1%) [3/4] | 3184 (40.0%) [3/4] | 499 (11.1%) [3/4] | 19 (1.1%) | 108 (9.0%) | 214 (2.8%) [3/4] | 172 (2.3%) [3/4] | 12 (11.9%) [3/4] | 3 (3.2%) | 402 (33.3%) [3/4] | 1017 (10.8%) [3/4] | 9323 (38.3%) [3/4] | 103 (2.9%) [3/4] | 95 (1.2%) [3/4] | 44 (0.5%) | 56 (2.9%) [3/4] | 1068 (4.7%) [3/4] | 478 (5.2%) [3/4] | 293 (5.3%) | 7 (0.2%) [3/4] | 1 (0.0%) | 443 (5.1%) | 3 (1.0%) | train | 0 (0.0%) [3/4] | 2 (0.1%) [3/4] | 43 (0.1%) [3/4] | 0 (0.0%) [3/4] | 0 (0.0%) [3/4] | 160 (1.2%) [3/4] | 2067 (54.0%) [3/4] | 283 (11.7%) [3/4] |
| pplx + gliner2-fastino | 1 (0.1%) | 2 (0.1%) | 74 (3.3%) | 0 (0.0%) | 22 (1.3%) | 238 (4.3%) | 8 (2.8%) | 13 (1.7%) | 180 (5.8%) | 1180 (11.4%) | 1131 (14.2%) | 488 (10.9%) | 11 (0.7%) | 91 (7.6%) | 29 (0.4%) | 32 (0.4%) | 2 (2.0%) | 1 (1.1%) | 87 (7.2%) | 87 (0.9%) | 2352 (9.7%) | 27 (0.8%) | 76 (0.9%) | 24 (0.3%) | 18 (0.9%) | 685 (3.0%) | 240 (2.6%) | 153 (2.8%) | 12 (0.3%) | 2 (0.0%) | 354 (4.1%) | 7 (2.4%) | 5 (0.7%) | 0 (0.0%) | 2 (0.1%) | 31 (0.1%) | 1 (0.2%) | 0 (0.0%) | 87 (0.7%) | 53 (1.4%) | 66 (2.7%) |
| pplx + gliner2-fastino + mmbert32k | 1 (0.1%) | 1 (0.1%) | 25 (1.1%) | 0 (0.0%) | 8 (0.5%) | 116 (2.1%) | 4 (1.4%) | 1 (0.1%) | 163 (5.3%) | 845 (8.2%) | 459 (5.8%) | 465 (10.4%) | 5 (0.3%) | 85 (7.1%) | 9 (0.1%) | 25 (0.3%) | 2 (2.0%) | 1 (1.1%) | 70 (5.8%) | 23 (0.2%) | 1533 (6.3%) | 15 (0.4%) | 26 (0.3%) | 10 (0.1%) | 10 (0.5%) | 341 (1.5%) | 150 (1.6%) | 61 (1.1%) | 9 (0.3%) | 0 (0.0%) | 125 (1.4%) | 6 (2.1%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 10 (0.0%) | 0 (0.0%) | 0 (0.0%) | 37 (0.3%) | 43 (1.1%) | 62 (2.6%) |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 1 (0.1%) | 1 (0.1%) | 9 (0.4%) | 0 (0.0%) | 8 (0.5%) | 89 (1.6%) | 0 (0.0%) | 1 (0.1%) | 139 (4.5%) | 687 (6.6%) | 108 (1.4%) | 440 (9.8%) | 5 (0.3%) | 84 (7.0%) | 7 (0.1%) | 22 (0.3%) | 2 (2.0%) | 1 (1.1%) | 68 (5.6%) | 14 (0.1%) | 843 (3.5%) | 8 (0.2%) | 21 (0.3%) | 2 (0.0%) | 10 (0.5%) | 289 (1.3%) | 127 (1.4%) | 44 (0.8%) | 8 (0.2%) | 0 (0.0%) | 82 (0.9%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 3 (0.0%) | 0 (0.0%) | 0 (0.0%) | 35 (0.3%) | 37 (1.0%) | 59 (2.4%) |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 28 (2.2%) | 17 (0.9%) | 563 (25.1%) | 0 (0.0%) | 106 (6.4%) | 1368 (24.7%) | 17 (5.9%) | 28 (3.6%) | 846 (27.4%) | 4036 (39.0%) | 5879 (73.8%) | 871 (19.4%) | 41 (2.5%) | 264 (22.1%) | 363 (4.8%) | 437 (5.8%) | 24 (23.8%) | 10 (10.5%) | 1023 (84.7%) | train | 19408 (79.6%) | 315 (8.8%) | 962 (11.8%) | 727 (7.7%) | 242 (12.7%) | 3854 (16.9%) | 1186 (12.8%) | 1050 (19.0%) | 39 (1.1%) | 16 (0.3%) | 1716 (19.7%) | 12 (4.2%) | 22 (2.9%) | 8 (2.0%) | 157 (5.8%) | 8620 (26.9%) | 14 (2.4%) | 11 (1.9%) | 2019 (15.4%) | 2446 (63.9%) | 507 (21.0%) |
| gitleaks + all 52 models | 0 (0.0%) [48/53] | train | 0 (0.0%) [42/53] | 0 (0.0%) [40/53] | 0 (0.0%) [48/53] | 2 (0.0%) [47/53] | 0 (0.0%) [39/53] | 0 (0.0%) [39/53] | 22 (0.7%) [40/53] | 67 (0.6%) [39/53] | 11 (0.1%) [48/53] | train | 0 (0.0%) [52/53] | 58 (4.9%) [49/53] | 0 (0.0%) [40/53] | 3 (0.0%) [42/53] | 0 (0.0%) [40/53] | 0 (0.0%) [41/53] | 1 (0.1%) [49/53] | train | 61 (0.3%) [47/53] | train | train | train | train | 25 (0.1%) [39/53] | 14 (0.2%) [47/53] | 0 (0.0%) [51/53] | 3 (0.1%) [47/53] | train | train | 0 (0.0%) [42/53] | train | 0 (0.0%) [39/53] | 0 (0.0%) [47/53] | 0 (0.0%) [49/53] | 0 (0.0%) [39/53] | 0 (0.0%) [47/53] | 0 (0.0%) [47/53] | 3 (0.1%) [42/53] | 34 (1.4%) [39/53] |

## Every option in percent

One table per composition. **Untouched annotations** - entities not touched by a single character, as a share of all entities of the set; partially hidden entities are not counted as untouched and remain partly exposed. **Over-masked** and **unannotated rows touched** are pooled over every set that has rows without annotations. F1 is the char-level detection without type, median over the pii sets. Rows/s is over every set: detectors run one after another, so their times add up. `[k/N]` marks a set where only k of the N members have a run; the pooled columns to the right mix such sets in, so they describe the actually available members, not the full composition. `historical pre-fix` - the named composition includes a scanner with stored pre-correction predictions; the per-set tables above name the members that actually ran.

| composition | untouched, arthur-passwords | untouched, corrupt-secrets-issues | untouched, creddata | untouched, leak-museum | untouched, leaky-repo | untouched, secrets-issues | untouched, secrets-rules | untouched, synth-env-configs | untouched, synth-secrets-en | untouched, synth-secrets-ru | pii untouched, worst set | pii untouched, median | over-masked | unannotated rows touched | pii F1, median | rows/s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gitleaks | - | - | - | - | 76.8% | 45.1% | train | - | - | - | 100.0% | 100.0% | 0.4% | 0.9% | 0.000 | 5893.9 |
| betterleaks `historical pre-fix` | - | - | - | - | - | 42.7% | train | - | - | - | 100.0% | 100.0% | 0.6% | 1.9% | 0.000 | 6427.1 |
| gitleaks + betterleaks `historical pre-fix` | - | - | - | - | 76.8% [1/2] | 41.3% | train | - | - | - | 100.0% | 100.0% | 0.6% | 1.9% | 0.000 | 3074.5 |
| pplx | 0.0% | 4.2% | 5.8% | 16.8% | 7.4% | 4.2% | 3.9% | 0.0% | 0.2% | 0.0% | 87.4% | 9.5% | 11.4% | 44.0% | 0.829 | 8.2 |
| gitleaks + pplx | 0.0% [1/2] | 4.2% [1/2] | 5.8% [1/2] | 16.8% [1/2] | 7.4% | 2.4% | train | 0.0% [1/2] | 0.2% [1/2] | 0.0% [1/2] | 87.4% | 9.5% | 11.0% | 43.1% | 0.829 | 8.1 |
| gitleaks + pplx + gliner-nvidia | 0.0% [2/3] | 3.5% [2/3] | 1.7% [2/3] | 10.9% [2/3] | 2.1% | 1.7% | train | 0.0% [2/3] | 0.0% [2/3] | 0.0% [2/3] | 35.8% | 2.0% | 13.1% | 65.0% | 0.824 | 7.0 |
| gitleaks + pplx + gliner-nvidia + ru-legal-ner | 0.0% [3/4] | 2.8% [3/4] | 0.0% [3/4] | 7.9% [3/4] | 1.1% | 1.0% | train | 0.0% [3/4] | 0.0% [3/4] | 0.0% [3/4] | 21.4% | 1.1% | 19.7% | 76.3% | 0.729 | 6.6 |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia | 0.0% [3/4] | 0.7% [3/4] | 0.4% [3/4] | 8.9% [3/4] | 1.1% | 1.0% | train | 0.0% [3/4] | 0.0% [3/4] | 0.0% [3/4] | 34.1% | 1.6% | 14.0% | 66.8% | 0.815 | 1.6 |
| gitleaks + pplx + opf-ru-v2 + gliner-nvidia + ru-legal-ner | 0.0% [4/5] | 0.7% [4/5] | 0.0% [4/5] | 5.9% [4/5] | 1.1% | 1.0% | train | 0.0% [4/5] | 0.0% [4/5] | 0.0% [4/5] | 21.2% | 0.8% | 20.1% | 77.2% | 0.724 | 1.6 |
| gitleaks + pplx + ru-legal-ner + gliner2-vladlinv | 0.0% [3/4] | 2.8% [3/4] | 0.0% [3/4] | 11.9% [3/4] | 3.2% | 1.0% | train | 0.0% [3/4] | 0.0% [3/4] | 0.0% [3/4] | 54.0% | 4.7% | 18.1% | 66.3% | 0.738 | 7.2 |
| pplx + gliner2-fastino | 0.0% | 2.8% | 1.7% | 2.0% | 1.1% | 2.4% | 0.7% | 0.0% | 0.2% | 0.0% | 14.2% | 1.3% | 15.3% | 68.9% | 0.845 | 7.3 |
| pplx + gliner2-fastino + mmbert32k | 0.0% | 1.4% | 0.1% | 2.0% | 1.1% | 2.1% | 0.0% | 0.0% | 0.0% | 0.0% | 10.4% | 0.5% | 18.8% | 76.6% | 0.822 | 6.8 |
| pplx + gliner2-fastino + bardsai-eu + mmbert32k | 0.0% | 0.0% | 0.1% | 2.0% | 1.1% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 9.8% | 0.5% | 19.8% | 78.0% | 0.799 | 1.1 |
| vote 2 of 3 (pplx, opf-ru-v2, gliner-nvidia) | 0.0% | 5.9% | 3.6% | 23.8% | 10.5% | 4.2% | 2.9% | 2.0% | 2.4% | 1.9% | 84.7% | 16.1% | 6.4% | 37.6% | 0.800 | 1.6 |
| gitleaks + all 52 models | 0.0% [40/53] | 0.0% [39/53] | 0.0% [39/53] | 0.0% [40/53] | 0.0% [41/53] | 0.0% [42/53] | train | 0.0% [39/53] | 0.0% [39/53] | 0.0% [47/53] | 4.9% | 0.1% | 51.2% | 99.0% | 0.444 | 0.2 |

