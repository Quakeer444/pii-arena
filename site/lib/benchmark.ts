export type Dataset = {
  id: string;
  lang: string;
  kind: string;
  rows: number;
  gold_spans: number;
  characters: number;
  negative_rows: number;
  source: string;
  license: string;
  synthetic: boolean;
  corrupted: boolean;
  bench_sha256: string;
  groups: string[];
  raw: {
    revision: string;
    sha256: string;
    paths?: string[];
    files?: number;
    bytes?: number;
  } | null;
};
export type MemberProvenance = {
  member: string;
  revision: string | null;
  upstream: string | null;
  flags: string;
};
export type System = {
  id: string;
  name: string;
  kind: string;
  family: string;
  members: string[];
  votes: number;
  base: string;
  upstream: string | null;
  revision: string | null;
  flags: string;
  participants?: MemberProvenance[];
};
export type CategoryResult = {
  id: string;
  gold: number;
  hit: number;
  hidden: number;
  rawHidden: number;
};
export type RecordRow = {
  system: string;
  dataset: string;
  train: boolean;
  gold: number;
  hit: number;
  hidden: number;
  rawHidden: number;
  originalGold: number;
  originalHidden: number;
  tp: number;
  fp: number;
  fn: number;
  negativeChars: number;
  maskedNegativeChars: number;
  negativeRows: number;
  touchedNegativeRows: number;
  positiveRows: number;
  residualRows: number;
  categories: CategoryResult[];
  adapterStatus?: string;
  adapterPolicy?: string;
  unresolvedSpans?: number;
};
export type AdapterSlice = {
  status: string;
  policy: string;
  runs: number;
  unresolvedSpans: number;
};
export type Speed = {
  device: string;
  model: string;
  chars_per_second: number;
  rows_per_second: number;
  p50_ms_reported: number;
  p95_ms_reported: number;
  hardware: string;
  threads: string;
  workers: string;
  quant: string;
  variant: string;
  rss_mb: number | null;
  datasets: number;
};
export type Benchmark = {
  meta: {
    experimentDate: string;
    revision: string;
    version: string;
    threshold: number;
    schema: number;
    snapshotHash: string;
    runs: number;
    catalogRecords: number;
  };
  datasets: Dataset[];
  systems: System[];
  records: RecordRow[];
  categories: {
    id: string;
    title: string;
    description: string;
    family: string;
  }[];
  speed: Speed[];
  diagnostics: Record<string, unknown>;
  costs: {
    composition: string;
    cpu_seconds_10k: number;
    gpu_seconds_10k: number;
    mixed_device_estimate: boolean;
  }[];
  sensitivity: {
    excluded_dataset_ids: string[];
    included_dataset_ids: string[];
  };
};
export type Score = System & {
  gold: number;
  hit: number;
  hidden: number;
  rawHidden: number;
  tp: number;
  fp: number;
  fn: number;
  negativeChars: number;
  maskedNegativeChars: number;
  positiveRows: number;
  residualRows: number;
  sets: number;
  missed: number;
  untouched: number | null;
  fullyHidden: number | null;
  detected: number | null;
  extra: number | null;
  f1: number | null;
  precision: number | null;
  recall: number | null;
  cpu: number | null;
  gpu: number | null;
  datasetIds: string[];
  adapterSlices: AdapterSlice[];
  adapterInventory: AdapterSlice[];
};
export type ExportContext = {
  view?: string;
  rowOrder?: string;
  language: string;
  task: string;
  dataset: string;
  sensitivity: boolean;
  family?: string;
  query?: string;
  coverage?: string;
  sort?: string;
  direction?: string;
  comparisonSystemIds?: string[];
  scopeDatasetIds?: string[];
  experimentDate?: string;
  resultRevision?: string;
  snapshotHash?: string;
  threshold?: number;
};
export const REF = "composition:pplx+fastino+bardsai+mmbert";
export const colors = [
  "var(--chart-1)",
  "var(--chart-3)",
  "var(--chart-4)",
  "var(--chart-5)",
  "var(--chart-6)",
  "var(--chart-7)",
  "var(--chart-2)",
];
export const detectorSlug = (id: string) =>
  id
    .replace(/^model:/, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
export const sourceUrls = (source: string) =>
  source.match(/https:\/\/[^\s)]+/g) ?? [];
export function colorFor(family: string) {
  const fs = ["gliner2", "gliner", "hf", "opf", "onnx", "pplx"];
  return colors[Math.max(0, fs.indexOf(family)) % colors.length];
}
export const n = (value: number) => value.toLocaleString("en-US");
export function percent(value: number | null, decimals = 2) {
  if (value === null || !Number.isFinite(value)) return "—";
  const step = 10 ** -decimals;
  if (value > 0 && value < step / 2)
    return "<" + step.toFixed(decimals) + "%";
  if (value < 100 && value >= 100 - step / 2)
    return ">" + (100 - step).toFixed(decimals) + "%";
  return value.toFixed(decimals) + "%";
}
export function ratio(a: number, b: number) {
  return b ? (100 * a) / b : null;
}
export function speedFor(data: Benchmark, s: System, device: "cpu" | "cuda") {
  const matches = (model: string) =>
    data.speed.find(
      (x) =>
        x.device === device &&
        x.model === model &&
        (device === "cpu"
          ? x.hardware.includes("AMD EPYC 9K84") &&
            x.threads === "16" &&
            x.workers === "24"
          : x.hardware === "NVIDIA GeForce RTX 5090" && x.workers === "2"),
    );
  return (
    matches(s.name) ??
    (device === "cpu" ? matches(s.name + "+cpu-speed") : undefined) ??
    null
  );
}
const ADAPTER_STATUS_LABEL: Record<string, string> = {
  "corrected-rerun": "corrected rerun",
  "verified-unchanged": "verified unchanged",
  "historical-pre-fix": "historical pre-fix",
};
export function summarizeAdapterRuns(
  rows: Pick<RecordRow, "adapterStatus" | "adapterPolicy" | "unresolvedSpans">[],
): AdapterSlice[] {
  const groups = new Map<string, AdapterSlice>();
  for (const row of rows) {
    if (!row.adapterStatus) continue;
    const policy = row.adapterPolicy ?? "";
    const key = `${row.adapterStatus}\0${policy}`;
    const item = groups.get(key) ?? {
      status: row.adapterStatus,
      policy,
      runs: 0,
      unresolvedSpans: 0,
    };
    item.runs += 1;
    item.unresolvedSpans += row.unresolvedSpans ?? 0;
    groups.set(key, item);
  }
  return [...groups.values()].sort(
    (a, b) => a.status.localeCompare(b.status) || a.policy.localeCompare(b.policy),
  );
}
export function adapterSliceText(slice: AdapterSlice) {
  const label = ADAPTER_STATUS_LABEL[slice.status] ?? slice.status;
  const policy = slice.policy ? ` · ${slice.policy}` : "";
  return `${label}${policy} · ${slice.runs} runs · ${slice.unresolvedSpans} unresolved spans`;
}
export function adapterNote(score: Pick<Score, "adapterSlices" | "adapterInventory">) {
  if (!score.adapterSlices.length && !score.adapterInventory.length) return null;
  const slice = score.adapterSlices.map(adapterSliceText).join("; ");
  const inventory = score.adapterInventory.map(adapterSliceText).join("; ");
  return { slice, inventory: inventory !== slice ? inventory : null };
}
export function aggregate(
  data: Benchmark,
  ids: Set<string>,
  kind = "model",
): Score[] {
  return data.systems
    .filter((s) => s.kind === kind)
    .map((s) => {
      const rows = data.records.filter(
        (r) => r.system === s.id && ids.has(r.dataset) && !r.train,
      );
      const sum = (
        k: Exclude<
          keyof RecordRow,
          | "system"
          | "dataset"
          | "train"
          | "categories"
          | "adapterStatus"
          | "adapterPolicy"
          | "unresolvedSpans"
        >,
      ) => rows.reduce((a, r) => a + r[k], 0);
      const gold = sum("gold"),
        hit = sum("hit"),
        hidden = sum("hidden"),
        tp = sum("tp"),
        fp = sum("fp"),
        fn = sum("fn"),
        neg = sum("negativeChars"),
        extra = sum("maskedNegativeChars");
      const cpu = speedFor(data, s, "cpu"),
        gpu = speedFor(data, s, "cuda");
      return {
        ...s,
        gold,
        hit,
        hidden,
        rawHidden: sum("rawHidden"),
        tp,
        fp,
        fn,
        negativeChars: neg,
        maskedNegativeChars: extra,
        positiveRows: sum("positiveRows"),
        residualRows: sum("residualRows"),
        sets: rows.length,
        missed: gold - hit,
        untouched: ratio(gold - hit, gold),
        fullyHidden: ratio(hidden, gold),
        detected: ratio(hit, gold),
        extra: ratio(extra, neg),
        f1: 2 * tp + fp + fn ? (2 * tp) / (2 * tp + fp + fn) : null,
        precision: tp + fp ? tp / (tp + fp) : null,
        recall: tp + fn ? tp / (tp + fn) : null,
        cpu: cpu ? 10000 / cpu.chars_per_second : null,
        gpu: gpu ? 10000 / gpu.chars_per_second : null,
        datasetIds: rows.map((r) => r.dataset),
        adapterSlices: summarizeAdapterRuns(rows),
        adapterInventory: summarizeAdapterRuns(
          data.records.filter((row) => row.system === s.id),
        ),
      };
    })
    .filter((x) => x.sets > 0);
}
export function categoryScores(
  data: Benchmark,
  system: string,
  ids: Set<string>,
) {
  return data.categories.map((c) => {
    const rows = data.records
      .filter((r) => r.system === system && !r.train && ids.has(r.dataset))
      .flatMap((r) => r.categories.filter((x) => x.id === c.id));
    return {
      ...c,
      gold: rows.reduce((s, r) => s + r.gold, 0),
      hit: rows.reduce((s, r) => s + r.hit, 0),
      hidden: rows.reduce((s, r) => s + r.hidden, 0),
      rawHidden: rows.reduce((s, r) => s + r.rawHidden, 0),
    };
  });
}
export function download(name: string, content: string, type: string) {
  const url = URL.createObjectURL(new Blob([content], { type }));
  const link = document.createElement("a");
  link.href = url;
  link.download = name;
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 5000);
}
export function compareScores(
  a: Score,
  b: Score,
  key: keyof Score,
  ascending: boolean,
) {
  const av = a[key],
    bv = b[key];
  if (av === null && bv === null)
    return a.name.localeCompare(b.name) || a.id.localeCompare(b.id);
  if (av === null) return 1;
  if (bv === null) return -1;
  const direction = ascending ? 1 : -1;
  const compared =
    typeof av === "string"
      ? String(av).localeCompare(String(bv))
      : Number(av) - Number(bv);
  return (
    compared * direction ||
    a.name.localeCompare(b.name) ||
    a.id.localeCompare(b.id)
  );
}
export function compareExportContext(
  applied: ExportContext,
  systemIds: string[],
  datasetIds: string[],
): ExportContext {
  // Leaderboard search and sort do not select these rows, so they stay out of the file.
  return {
    view: "compare",
    rowOrder: "selection",
    language: applied.language,
    task: applied.task,
    dataset: applied.dataset,
    sensitivity: applied.sensitivity,
    comparisonSystemIds: [...systemIds],
    scopeDatasetIds: [...datasetIds],
    experimentDate: applied.experimentDate,
    resultRevision: applied.resultRevision,
    snapshotHash: applied.snapshotHash,
    threshold: applied.threshold,
  };
}
export function filteredCsv(rows: Score[], context: ExportContext) {
  // Two different facts shared the header `family`, so a dict reader kept only the second.
  const contextColumns: [string, unknown][] = [
    ["view", context.view],
    ["rowOrder", context.rowOrder],
    ["language", context.language],
    ["task", context.task],
    ["dataset", context.dataset],
    ["sensitivity", context.sensitivity],
    ["filter_family", context.family],
    ["query", context.query],
    ["coverage", context.coverage],
    ["sort", context.sort],
    ["direction", context.direction],
    ["comparisonSystemIds", context.comparisonSystemIds],
    ["scopeDatasetIds", context.scopeDatasetIds],
    ["experimentDate", context.experimentDate],
    ["resultRevision", context.resultRevision],
    ["snapshotHash", context.snapshotHash],
    ["threshold", context.threshold],
  ];
  const scoreColumns = (row: Partial<Score> = {}): [string, unknown][] => [
    ["id", row.id],
    ["name", row.name],
    ["kind", row.kind],
    ["system_family", row.family],
    ["revision", row.revision],
    ["sets", row.sets],
    ["datasetIds", row.datasetIds],
    ["gold", row.gold],
    ["hit", row.hit],
    ["hidden", row.hidden],
    ["rawHidden", row.rawHidden],
    ["missed", row.missed],
    ["positiveRows", row.positiveRows],
    ["residualRows", row.residualRows],
    ["tp", row.tp],
    ["fp", row.fp],
    ["fn", row.fn],
    ["negativeChars", row.negativeChars],
    ["maskedNegativeChars", row.maskedNegativeChars],
    ["untouched", row.untouched],
    ["fullyHidden", row.fullyHidden],
    ["detected", row.detected],
    ["extra", row.extra],
    ["f1", row.f1],
    ["precision", row.precision],
    ["recall", row.recall],
    ["cpu", row.cpu],
    ["gpu", row.gpu],
    ["adapterSlices", row.adapterSlices ?? []],
    ["adapterInventory", row.adapterInventory ?? []],
  ];
  const value = (item: unknown) =>
    Array.isArray(item) || (item !== null && typeof item === "object")
      ? JSON.stringify(item)
      : item;
  const escape = (item: unknown) => {
    const normalized = value(item);
    const cell = normalized === null || normalized === undefined ? "" : String(normalized);
    const safe =
      typeof normalized === "string" && /^[=+\-@\t\r]/.test(cell)
        ? `'${cell}`
        : cell;
    return '"' + safe.replaceAll('"', '""') + '"';
  };
  const header = [
    ...contextColumns.map(([name]) => name),
    ...scoreColumns().map(([name]) => name),
  ];
  return [
    header.map(escape).join(","),
    ...rows.map((row) =>
      [...contextColumns.map(([, item]) => item), ...scoreColumns(row).map(([, item]) => item)]
        .map(escape)
        .join(","),
    ),
  ].join("\n");
}
export function exportCsv(rows: Score[], context: ExportContext) {
  download(
    "pii-benchmark-filtered.csv",
    filteredCsv(rows, context),
    "text/csv;charset=utf-8",
  );
}
