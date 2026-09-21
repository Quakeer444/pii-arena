import type { Benchmark, RecordRow } from "./benchmark";
import { DIFFICULTY, MODEL_LABELS, type DifficultyTier } from "./decision-data";

export type Coverage = {
  datasets: number;
  expected: number;
  trainExcluded: number;
  missing: number;
  gold: number;
};

type ModelResult = {
  system: string;
  name: string;
  family: string;
  fullyHidden: number | null;
  complete: boolean;
};

export type RobustnessRow = ModelResult & Record<DifficultyTier, number | null> & {
  coverage: Record<DifficultyTier, Coverage>;
};

export type DomainRow = ModelResult & {
  pii: number | null;
  secrets: number | null;
  coverage: { pii: Coverage; secrets: Coverage };
};

export type SliceRow = {
  system: string;
  name: string;
  value: number | null;
  complete: boolean;
  coverage: Coverage;
};

export type DecisionMetrics = {
  robustness: RobustnessRow[];
  domains: DomainRow[];
  categories: Record<string, SliceRow[]>;
  languages: Record<string, SliceRow[]>;
};

const tiers: DifficultyTier[] = ["Easy", "Medium", "Hard", "Extreme"];

function coverage(rows: RecordRow[], datasetIds: Set<string>): Coverage {
  const eligible = rows.filter(row => datasetIds.has(row.dataset) && !row.train);
  const present = new Set(eligible.map(row => row.dataset));
  const excluded = new Set(rows.filter(row => datasetIds.has(row.dataset) && row.train).map(row => row.dataset));
  return {
    datasets: present.size,
    expected: datasetIds.size,
    trainExcluded: excluded.size,
    missing: Math.max(0, datasetIds.size - present.size - excluded.size),
    gold: eligible.reduce((sum, row) => sum + row.gold, 0),
  };
}

function fullyHidden(rows: RecordRow[], macro: boolean): number | null {
  const eligible = rows.filter(row => !row.train && row.gold > 0);
  if (!eligible.length) return null;
  if (macro) return eligible.reduce((sum, row) => sum + 100 * row.hidden / row.gold, 0) / eligible.length;
  return 100 * eligible.reduce((sum, row) => sum + row.hidden, 0) / eligible.reduce((sum, row) => sum + row.gold, 0);
}

export function buildDecisionMetrics(data: Benchmark, scopeIds?: Set<string>): DecisionMetrics {
  const datasetIds = scopeIds ?? new Set(data.datasets.map(dataset => dataset.id));
  const tierIds = Object.fromEntries(tiers.map(tier => [
    tier,
    new Set(DIFFICULTY.filter(row => row.tier === tier && datasetIds.has(row.dataset)).map(row => String(row.dataset))),
  ])) as Record<DifficultyTier, Set<string>>;
  const domainIds = {
    pii: new Set(data.datasets.filter(dataset => dataset.kind === "pii").map(dataset => dataset.id)),
    secrets: new Set(data.datasets.filter(dataset => dataset.kind === "secrets").map(dataset => dataset.id)),
  };
  const categoryIds = new Map(data.categories.map(category => [category.id, new Set<string>()]));
  const records = new Map<string, RecordRow[]>();
  for (const row of data.records) {
    if (!datasetIds.has(row.dataset)) continue;
    const rows = records.get(row.system) ?? [];
    rows.push(row);
    records.set(row.system, rows);
    for (const category of row.categories) {
      if (category.gold > 0) categoryIds.get(category.id)?.add(row.dataset);
    }
  }

  const models = data.systems.filter(system => system.kind === "model").map(system => {
    const rows = records.get(system.id) ?? [];
    const measured = coverage(rows, datasetIds);
    return {
      rows,
      system: system.id,
      name: MODEL_LABELS[system.id] ?? system.name,
      family: system.family,
      fullyHidden: fullyHidden(rows, false),
      complete: measured.datasets === measured.expected,
    };
  }).filter(row => row.fullyHidden !== null).sort((a, b) =>
    Number(b.complete) - Number(a.complete)
    || (b.fullyHidden ?? -1) - (a.fullyHidden ?? -1)
    || a.name.localeCompare(b.name),
  );

  function slices(ids: Set<string>, categoryId?: string): SliceRow[] {
    return models.map(model => {
      const rows = model.rows.filter(row => ids.has(row.dataset)).flatMap(row => {
        if (!categoryId) return [row];
        const category = row.categories.find(category => category.id === categoryId && category.gold > 0);
        return category ? [{ ...row, gold: category.gold, hidden: category.hidden }] : [];
      });
      const measured = coverage(rows, ids);
      return {
        system: model.system,
        name: model.name,
        value: fullyHidden(rows, false),
        complete: measured.datasets === measured.expected,
        coverage: measured,
      };
    }).sort((a, b) =>
      Number(b.complete) - Number(a.complete)
      || (b.value ?? -1) - (a.value ?? -1)
      || a.name.localeCompare(b.name),
    );
  }

  return {
    robustness: models.map(({ rows, ...model }) => ({
      ...model,
      ...Object.fromEntries(tiers.map(tier => [tier, fullyHidden(rows.filter(row => tierIds[tier].has(row.dataset)), true)])) as Record<DifficultyTier, number | null>,
      coverage: Object.fromEntries(tiers.map(tier => [tier, coverage(rows, tierIds[tier])])) as Record<DifficultyTier, Coverage>,
    })),
    domains: models.map(({ rows, ...model }) => ({
      ...model,
      pii: fullyHidden(rows.filter(row => domainIds.pii.has(row.dataset)), false),
      secrets: fullyHidden(rows.filter(row => domainIds.secrets.has(row.dataset)), false),
      coverage: {
        pii: coverage(rows, domainIds.pii),
        secrets: coverage(rows, domainIds.secrets),
      },
    })),
    categories: Object.fromEntries([...categoryIds].map(([categoryId, ids]) => [categoryId, slices(ids, categoryId)])),
    languages: Object.fromEntries([...new Set(data.datasets.filter(dataset => datasetIds.has(dataset.id)).map(dataset => dataset.lang))].map(language => [
      language,
      slices(new Set(data.datasets.filter(dataset => datasetIds.has(dataset.id) && dataset.lang === language).map(dataset => dataset.id))),
    ])),
  };
}
