export type DifficultyTier = "Easy" | "Medium" | "Hard" | "Extreme";

export const MODEL_LABELS: Record<string,string> = {
  "model:gliner2-fastino": "Fastino",
  "model:gliner2-hivetrace-omni": "HiveTrace Omni",
  "model:pplx": "PPLX",
  "model:nuner-zero": "NuNER Zero"
};

export const DIFFICULTY = [{"dataset": "arthur-passwords", "score": 7.14, "tier": "Easy", "gold": 280}, {"dataset": "russian-pii-66k", "score": 10.18, "tier": "Easy", "gold": 4805}, {"dataset": "secrets-rules", "score": 12.6, "tier": "Easy", "gold": 746}, {"dataset": "kiji-en", "score": 15.64, "tier": "Easy", "gold": 7623}, {"dataset": "creddata", "score": 17.91, "tier": "Easy", "gold": 776}, {"dataset": "alrosait", "score": 21.54, "tier": "Easy", "gold": 1862}, {"dataset": "nym-en", "score": 22.0, "tier": "Easy", "gold": 3584}, {"dataset": "redact-ru", "score": 23.26, "tier": "Easy", "gold": 9230}, {"dataset": "kiji-multi", "score": 23.34, "tier": "Easy", "gold": 7565}, {"dataset": "hivetrace", "score": 25.49, "tier": "Medium", "gold": 1667}, {"dataset": "nerel", "score": 25.91, "tier": "Medium", "gold": 24369}, {"dataset": "ameau01", "score": 27.52, "tier": "Medium", "gold": 2242}, {"dataset": "nym-multi", "score": 27.96, "tier": "Medium", "gold": 8169}, {"dataset": "jayguard", "score": 28.03, "tier": "Medium", "gold": 1195}, {"dataset": "gretel-multi", "score": 29.44, "tier": "Medium", "gold": 4484}, {"dataset": "nemotron-pii", "score": 29.61, "tier": "Medium", "gold": 9391}, {"dataset": "scanpatch", "score": 29.78, "tier": "Medium", "gold": 8708}, {"dataset": "nym-ru", "score": 30.25, "tier": "Medium", "gold": 9497}, {"dataset": "dialogpii-en", "score": 31.0, "tier": "Medium", "gold": 3087}, {"dataset": "synth-wiki-tables", "score": 31.44, "tier": "Medium", "gold": 13094}, {"dataset": "redact-multi", "score": 31.83, "tier": "Medium", "gold": 22864}, {"dataset": "synth-jira-comments", "score": 32.87, "tier": "Medium", "gold": 2705}, {"dataset": "synth-ru-tickets", "score": 33.35, "tier": "Medium", "gold": 32099}, {"dataset": "tonicai", "score": 34.63, "tier": "Medium", "gold": 2417}, {"dataset": "redmadrobot", "score": 34.83, "tier": "Medium", "gold": 5516}, {"dataset": "corrupt-hivetrace", "score": 35.57, "tier": "Medium", "gold": 1667}, {"dataset": "privy", "score": 36.18, "tier": "Medium", "gold": 1899}, {"dataset": "leaky-repo", "score": 40.0, "tier": "Medium", "gold": 95}, {"dataset": "synth-secrets-ru", "score": 40.45, "tier": "Medium", "gold": 581}, {"dataset": "dialogpii-multi", "score": 40.85, "tier": "Medium", "gold": 10345}, {"dataset": "synth-secrets-en", "score": 42.0, "tier": "Medium", "gold": 581}, {"dataset": "corrupt-redmadrobot", "score": 46.65, "tier": "Hard", "gold": 5531}, {"dataset": "leak-museum", "score": 47.52, "tier": "Hard", "gold": 101}, {"dataset": "synth-env-configs", "score": 50.51, "tier": "Hard", "gold": 392}, {"dataset": "secrets-issues", "score": 55.56, "tier": "Hard", "gold": 288}, {"dataset": "tab-echr", "score": 56.27, "tier": "Hard", "gold": 3830}, {"dataset": "factrueval", "score": 57.81, "tier": "Hard", "gold": 7966}, {"dataset": "corrupt-secrets-issues", "score": 64.24, "tier": "Hard", "gold": 288}, {"dataset": "multiconer-ru", "score": 67.55, "tier": "Extreme", "gold": 1208}, {"dataset": "alexen2", "score": 73.04, "tier": "Extreme", "gold": 1261}, {"dataset": "rubai-ru", "score": 92.71, "tier": "Extreme", "gold": 3458}] as const;
export const STACK_GAIN = [{"models": ["GLiNER2 Fastino"], "fully_hidden_pct": 79.86, "residual_spans": 45819, "extra_masking_pct": 5.88, "incremental_hidden": null}, {"models": ["GLiNER2 Fastino", "PPLX"], "fully_hidden_pct": 91.94, "residual_spans": 18344, "extra_masking_pct": 15.27, "incremental_hidden": 27475}, {"models": ["GLiNER2 Fastino", "PPLX", "BardsAI EU"], "fully_hidden_pct": 94.08, "residual_spans": 13471, "extra_masking_pct": 17.1, "incremental_hidden": 4873}, {"models": ["GLiNER2 Fastino", "PPLX", "BardsAI EU", "mmBERT32k"], "fully_hidden_pct": 94.4, "residual_spans": 12728, "extra_masking_pct": 19.82, "incremental_hidden": 743}] as const;
export const PARETO = [{"label": "GLiNER2 Fastino", "abbr": "F", "fully_hidden_pct": 79.86, "extra_masking_pct": 5.88, "pareto": true, "hardware": "GPU eligible"}, {"label": "PPLX", "abbr": "P", "fully_hidden_pct": 74.92, "extra_masking_pct": 11.42, "pareto": false, "hardware": "GPU eligible"}, {"label": "PPLX + GLiNER2 Fastino", "abbr": "P+F", "fully_hidden_pct": 91.94, "extra_masking_pct": 15.27, "pareto": true, "hardware": "GPU eligible"}, {"label": "PPLX + GLiNER2 Fastino + mmBERT32k", "abbr": "P+F+M", "fully_hidden_pct": 92.96, "extra_masking_pct": 18.84, "pareto": false, "hardware": "GPU eligible"}, {"label": "PPLX + GLiNER2 Fastino + BardsAI EU", "abbr": "P+F+B", "fully_hidden_pct": 94.08, "extra_masking_pct": 17.1, "pareto": true, "hardware": "Hybrid"}, {"label": "PPLX + GLiNER2 Fastino + BardsAI EU + mmBERT32k", "abbr": "P+F+B+M", "fully_hidden_pct": 94.4, "extra_masking_pct": 19.82, "pareto": true, "hardware": "Hybrid"}] as const;
export const LANGUAGES = [{"language": "Russian", "system": "model:gliner2-fastino", "fully_hidden_pct": 78.55, "datasets": 19, "gold": 136419, "panel_label": "3-finalist shared panel"}, {"language": "English", "system": "model:gliner2-fastino", "fully_hidden_pct": 85.21, "datasets": 16, "gold": 28229, "panel_label": "3-finalist shared panel"}, {"language": "Multilingual", "system": "model:pplx", "fully_hidden_pct": 84.77, "datasets": 5, "gold": 53427, "panel_label": "3-finalist shared panel"}] as const;
export const CATEGORY_LEADERS = [{"label": "Keys & tokens", "system": "model:pplx", "value": 93.66, "gold": 6278}, {"label": "Logins", "system": "model:pplx", "value": 98.84, "gold": 11082}, {"label": "Banking & cards", "system": "model:pplx", "value": 72.19, "gold": 4433}, {"label": "Documents & IDs", "system": "model:pplx", "value": 90.07, "gold": 14097}, {"label": "People's names", "system": "model:gliner2-fastino", "value": 85.92, "gold": 61233}, {"label": "Phone & email", "system": "model:pplx", "value": 94.64, "gold": 20450}, {"label": "Addresses", "system": "model:gliner2-fastino", "value": 77.77, "gold": 37510}, {"label": "Dates & times", "system": "model:pplx", "value": 96.04, "gold": 5205}, {"label": "Organizations", "system": "model:gliner2-fastino", "value": 77.67, "gold": 17979}, {"label": "Network IDs", "system": "model:nuner-zero", "value": 96.35, "gold": 24593}, {"label": "Customer IDs", "system": "model:pplx", "value": 86.04, "gold": 7524}, {"label": "Other sensitive", "system": "model:pplx", "value": 53.29, "gold": 3207}] as const;

export const HARDWARE = [
  {
    id: "cpu",
    label: "CPU only",
    status: "Reference pair",
    name: "PPLX + Fastino",
    value: "",
    note: "Saved prediction union: 91.94% Fully Hidden. Both models have CPU throughput measurements in their reference precision. CPU output parity and full-stack latency are unmeasured."
  },
  {
    id: "cuda",
    label: "NVIDIA CUDA",
    status: "Measured quality",
    name: "PPLX + Fastino + mmBERT",
    value: "92.96%",
    note: "Best saved GPU-eligible union. Quality comes from saved predictions; full-stack latency and peak memory were not measured end-to-end."
  },
  {
    id: "hybrid",
    label: "CPU + NVIDIA CUDA",
    status: "Measured quality",
    name: "PPLX + Fastino + BardsAI + mmBERT",
    value: "94.40%",
    note: "Highest Fully Hidden among the saved unions. BardsAI uses the tested CPU-only ONNX configuration; the mixed-device runtime is estimated from member throughput."
  }
] as const;

export const DIFFICULTY_THRESHOLDS = {
  easyMax: 24.42,
  mediumMax: 44.32,
  hardMax: 65.89
} as const;

export function difficultyFor(id:string) {
  return DIFFICULTY.find(row => row.dataset === id) ?? null;
}
