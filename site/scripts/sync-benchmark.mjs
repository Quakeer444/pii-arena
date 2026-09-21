import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const siteRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const repoRoot = path.resolve(siteRoot, "..");
const evidenceRoot = path.join(siteRoot, "public", "evidence");
const dataRoot = path.join(siteRoot, "public", "data");

const copies = [
  ["README.md", "README.md"],
  ["CHANGELOG.md", "CHANGELOG.md"],
  ["CITATION.cff", "CITATION.cff"],
  ["CONTRIBUTING.md", "CONTRIBUTING.md"],
  ["LICENSE", "LICENSE"],
  ["NOTICE", "NOTICE"],
  ["assets", "assets"],
  ["LICENSES", "LICENSES"],
  ["datasets/catalog.json", "datasets/catalog.json"],
  ["datasets/samples.json", "datasets/samples.json"],
  ["docs", "docs"],
  ["results", "results"]
];

for (const [source] of copies) {
  if (!fs.existsSync(path.join(repoRoot, source))) {
    throw new Error(`Missing benchmark source: ${source}. Enable Vercel access outside the site Root Directory.`);
  }
}

fs.rmSync(evidenceRoot, { recursive: true, force: true });
fs.mkdirSync(evidenceRoot, { recursive: true });
for (const [source, destination] of copies) {
  fs.cpSync(path.join(repoRoot, source), path.join(evidenceRoot, destination), { recursive: true });
}

const raw = fs.readFileSync(path.join(evidenceRoot, "results", "snapshot.json"), "utf8");
const source = JSON.parse(raw);
const taxonomy = new Map(source.breakdowns.taxonomy.map((row) => [`${row.dataset}|${row.label}`, row]));
const catalog = fs
  .readFileSync(path.join(evidenceRoot, "docs", "models.md"), "utf8")
  .split("\n")
  .filter((line) => line.startsWith("| ") && !line.startsWith("| Record"))
  .map((line) => line.split("|").slice(1, -1).map((cell) => cell.trim()))
  .filter((cells) => cells.length === 5)
  .map((cells) => ({
    id: cells[0],
    family: cells[1],
    upstream: cells[2].match(/\((https?:[^)]+)\)/)?.[1] ?? null,
    revision: cells[3].replaceAll("`", ""),
    flags: cells[4]
  }));

const systems = source.breakdowns.systems.map((system) => {
  const name = system.id.slice(system.id.indexOf(":") + 1);
  const base = system.members[0].split("+")[0];
  const meta = catalog.find((entry) => entry.id === base);
  const measurement = source.measurements.find((entry) => entry.model === base);
  return {
    ...system,
    name,
    family: system.kind === "composition" ? "ensemble" : meta?.family ?? measurement?.family ?? "other",
    upstream: meta?.upstream ?? null,
    revision: meta?.revision ?? null,
    flags: meta?.flags ?? "",
    base
  };
});

const records = source.breakdowns.results.map((result) => {
  const categories = new Map();
  let gold = 0;
  let hidden = 0;
  let hit = 0;
  let rawHidden = 0;
  let originalGold = 0;
  let originalHidden = 0;
  for (const type of result.types) {
    const reference = taxonomy.get(`${result.dataset}|${type.label}`);
    if (!reference) throw new Error(`Missing taxonomy for ${result.dataset}/${type.label}`);
    gold += reference.gold;
    hit += type.hit;
    hidden += type.hidden;
    rawHidden += type.raw_hidden;
    originalGold += reference.original_gold;
    originalHidden += type.original_hidden;
    const category = categories.get(reference.category) ?? {
      id: reference.category,
      gold: 0,
      hit: 0,
      hidden: 0,
      rawHidden: 0
    };
    category.gold += reference.gold;
    category.hit += type.hit;
    category.hidden += type.hidden;
    category.rawHidden += type.raw_hidden;
    categories.set(category.id, category);
  }
  return {
    system: result.system,
    dataset: result.dataset,
    train: result.train,
    gold,
    hit,
    hidden,
    rawHidden,
    originalGold,
    originalHidden,
    tp: result.char_tp,
    fp: result.char_fp,
    fn: result.char_fn,
    negativeChars: result.negative_characters,
    maskedNegativeChars: result.negative_characters_masked,
    negativeRows: result.negative_rows,
    touchedNegativeRows: result.negative_rows_touched,
    positiveRows: result.positive_rows,
    residualRows: result.residual_rows,
    categories: [...categories.values()]
  };
});

const data = {
  meta: {
    experimentDate: source.experiment_date,
    revision: source.result_revision,
    version: source.code_version,
    threshold: source.threshold,
    schema: source.schema_version,
    snapshotHash: crypto.createHash("sha256").update(raw).digest("hex"),
    runs: Object.keys(source.sources).filter((entry) => /\/pred\..*\.jsonl$/.test(entry)).length,
    catalogRecords: catalog.length
  },
  datasets: source.datasets,
  systems,
  records,
  categories: source.breakdowns.categories,
  speed: source.speed,
  diagnostics: source.masking_diagnostics,
  costs: source.costs,
  sensitivity: source.sensitivity
};

fs.mkdirSync(dataRoot, { recursive: true });
fs.writeFileSync(path.join(dataRoot, "benchmark.json"), JSON.stringify(data));

const cell = (value) => `"${String(value ?? "").replaceAll('"', '""')}"`;
const resultFields = [
  "system", "dataset", "train", "gold", "hit", "hidden", "rawHidden", "tp", "fp", "fn",
  "negativeChars", "maskedNegativeChars", "negativeRows", "touchedNegativeRows", "positiveRows", "residualRows"
];
fs.writeFileSync(
  path.join(dataRoot, "all-results.csv"),
  [resultFields.map(cell).join(","), ...records.map((row) => resultFields.map((key) => cell(row[key])).join(","))].join("\n")
);

const categoryFields = ["system", "dataset", "train", "category", "gold", "hit", "hidden", "rawHidden"];
fs.writeFileSync(
  path.join(dataRoot, "categories.csv"),
  [
    categoryFields.map(cell).join(","),
    ...records.flatMap((row) =>
      row.categories.map((category) =>
        [row.system, row.dataset, row.train, category.id, category.gold, category.hit, category.hidden, category.rawHidden]
          .map(cell)
          .join(",")
      )
    )
  ].join("\n")
);

for (const [key, filename] of [["speed", "speed.json"], ["measurements", "measurements.json"], ["ensembles", "ensembles.json"]]) {
  fs.writeFileSync(path.join(dataRoot, filename), JSON.stringify(source[key]));
}

function walk(directory, prefix = "") {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const relative = path.posix.join(prefix, entry.name);
    const absolute = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(absolute, relative) : [{ path: relative, bytes: fs.statSync(absolute).size }];
  });
}

fs.writeFileSync(path.join(dataRoot, "files.json"), JSON.stringify(walk(evidenceRoot).sort((a, b) => a.path.localeCompare(b.path))));
console.log(`Synced benchmark ${data.meta.version}: ${data.datasets.length} datasets, ${systems.length} systems, ${records.length} records.`);
