import { REF, type System } from "./benchmark.ts";
import type { DecisionDashboardState } from "@/components/decision-dashboard";

export type ExplorerSearchState = {
  language: string;
  task: string;
  dataset: string;
  sensitivity: boolean;
  query: string;
  family: string;
  coverage: string;
  sort: string;
  ascending: boolean;
  selected: string[];
  entitySystem: string;
  datasetQuery: string;
  device: string;
  speedGroup: string;
  dashboard: DecisionDashboardState;
};

const choice = (value: string | null, allowed: string[], fallback: string) =>
  value && allowed.includes(value) ? value : fallback;

export function readExplorerSearch(
  search: string,
  initialTask: string,
  systems: System[],
  datasetIds: string[],
  categoryIds: string[],
): ExplorerSearchState {
  const params = new URLSearchParams(search);
  const systemIds = new Set(systems.map((system) => system.id));
  const selected = (params.get("compare") ?? "")
    .split(",")
    .filter(
      (id, index, items) =>
        id &&
        items.indexOf(id) === index &&
        systems.some((system) => system.id === id && system.kind === "model"),
    )
    .slice(0, 4);
  return {
    language: choice(params.get("lang"), ["all", "en", "ru", "multi"], "all"),
    task: choice(params.get("task"), ["all", "pii", "secrets"], initialTask),
    dataset: choice(params.get("dataset"), ["all", ...datasetIds], "all"),
    sensitivity: params.get("sensitivity") === "1",
    query: params.get("q") ?? "",
    family: params.get("family") ?? "all",
    coverage: choice(params.get("coverage"), ["complete", "all"], "complete"),
    sort: choice(
      params.get("sort"),
      ["name", "fullyHidden", "detected", "extra", "f1", "cpu", "gpu"],
      "fullyHidden",
    ),
    ascending: params.get("dir") === "asc",
    selected,
    entitySystem: systemIds.has(params.get("entity") ?? "")
      ? params.get("entity")!
      : REF,
    datasetQuery: params.get("datasetQuery") ?? "",
    device: choice(params.get("device"), ["cpu", "cuda"], "cpu"),
    speedGroup: choice(
      params.get("speedGroup"),
      ["reference", "all"],
      "reference",
    ),
    dashboard: {
      difficultyTier: choice(
        params.get("difficulty"),
        ["All", "Easy", "Medium", "Hard", "Extreme"],
        "All",
      ) as DecisionDashboardState["difficultyTier"],
      difficultyQuery: params.get("difficultyQuery") ?? "",
      robustnessQuery: params.get("robustnessQuery") ?? "",
      domainQuery: params.get("domainQuery") ?? "",
      category: choice(
        params.get("category"),
        ["overview", ...categoryIds],
        "overview",
      ),
    },
  };
}

export function writeExplorerSearch(state: ExplorerSearchState) {
  const params = new URLSearchParams();
  const set = (key: string, value: string, fallback: string) => {
    if (value !== fallback) params.set(key, value);
  };
  set("lang", state.language, "all");
  set("task", state.task, "all");
  set("dataset", state.dataset, "all");
  if (state.sensitivity) params.set("sensitivity", "1");
  if (state.query) params.set("q", state.query);
  set("family", state.family, "all");
  set("coverage", state.coverage, "complete");
  set("sort", state.sort, "fullyHidden");
  if (state.ascending) params.set("dir", "asc");
  if (state.selected.length) params.set("compare", state.selected.join(","));
  set("entity", state.entitySystem, REF);
  if (state.datasetQuery) params.set("datasetQuery", state.datasetQuery);
  set("device", state.device, "cpu");
  set("speedGroup", state.speedGroup, "reference");
  set("difficulty", state.dashboard.difficultyTier, "All");
  if (state.dashboard.difficultyQuery)
    params.set("difficultyQuery", state.dashboard.difficultyQuery);
  if (state.dashboard.robustnessQuery)
    params.set("robustnessQuery", state.dashboard.robustnessQuery);
  if (state.dashboard.domainQuery)
    params.set("domainQuery", state.dashboard.domainQuery);
  set("category", state.dashboard.category, "overview");
  return params.toString();
}
