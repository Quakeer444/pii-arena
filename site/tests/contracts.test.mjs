import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

import { aggregate, compareExportContext, compareScores, filteredCsv, percent } from "../lib/benchmark.ts";
import { buildDecisionMetrics } from "../lib/decision-metrics.ts";
import { evidenceLink, markdownHeadingId } from "../lib/evidence-links.ts";
import { readExplorerSearch, writeExplorerSearch } from "../lib/explorer-url.ts";
import { benchmarkForView } from "../lib/route-data.ts";

test("percent keeps near-boundary values honest", () => {
  assert.equal(percent(null, 1), "—");
  assert.equal(percent(0, 1), "0.0%");
  assert.equal(percent(0.04, 1), "<0.1%");
  assert.equal(percent(99.94, 1), "99.9%");
  assert.equal(percent(99.96, 1), ">99.9%");
  assert.equal(percent(100, 1), "100.0%");
});

test("score comparator treats two missing values as equal before the stable tie-breaker", () => {
  const a = { id: "model:a", name: "A", cpu: null };
  const b = { id: "model:b", name: "B", cpu: null };
  assert.ok(compareScores(a, b, "cpu", true) < 0);
  assert.ok(compareScores(b, a, "cpu", false) > 0);
  assert.ok(compareScores({ ...a, cpu: 1 }, b, "cpu", false) < 0);
});

test("filtered CSV retains exact counts, visible metrics and scope provenance", () => {
  const csv = filteredCsv([
    { id: "model:a", name: "A", kind: "model", family: "test", revision: "abc", sets: 1, datasetIds: ["one"], gold: 10, hit: 9, hidden: 8, rawHidden: 7, missed: 1, positiveRows: 5, residualRows: 2, tp: 30, fp: 3, fn: 4, negativeChars: 100, maskedNegativeChars: 6, untouched: 10, fullyHidden: 80, detected: 90, extra: 6, f1: 0.8, precision: 0.9, recall: 0.7, cpu: null, gpu: null },
  ], { language: "ru", task: "pii", dataset: "all", sensitivity: false, query: "=HYPERLINK(\"https://example.com\",\"open\")", scopeDatasetIds: ["one"], snapshotHash: "sha", resultRevision: "r1" });
  const [header, row] = csv.split("\n");
  for (const key of ["snapshotHash", "scopeDatasetIds", "id", "hit", "hidden", "detected", "fullyHidden"]) assert.match(header, new RegExp(`"${key}"`));
  assert.match(row, /"sha"/);
  assert.match(row, /"\[""one""\]"/);
  assert.match(row, /"'=HYPERLINK/);
});

test("domain coverage is limited to the selected dataset scope", () => {
  const record = { system: "model:test", dataset: "alexen2", train: false, gold: 10, hit: 9, hidden: 8, rawHidden: 8, originalGold: 10, originalHidden: 8, tp: 8, fp: 1, fn: 2, negativeChars: 20, maskedNegativeChars: 1, negativeRows: 1, touchedNegativeRows: 1, positiveRows: 2, residualRows: 1, categories: [] };
  const data = { meta: {}, datasets: [{ id: "alexen2", kind: "pii", lang: "ru" }, { id: "alrosait", kind: "pii", lang: "ru" }], systems: [{ id: "model:test", name: "Test", kind: "model", family: "test", members: ["test"], votes: 1, base: "test", upstream: null, revision: "1", flags: "" }], records: [record], categories: [], speed: [], diagnostics: {}, costs: [], sensitivity: { excluded_dataset_ids: [], included_dataset_ids: [] } };
  const result = buildDecisionMetrics(data, new Set(["alexen2"])).domains[0];
  assert.equal(result.coverage.pii.expected, 1);
  assert.equal(result.coverage.pii.datasets, 1);
  assert.equal(result.coverage.pii.missing, 0);
  assert.equal(result.coverage.secrets.expected, 0);
});

function parseCsv(text) {
  const rows = [];
  let row = [];
  let cell = "";
  let quoted = false;
  for (let i = 0; i < text.length; i++) {
    const char = text[i];
    if (quoted) {
      if (char === '"') {
        if (text[i + 1] === '"') {
          cell += '"';
          i += 1;
        } else quoted = false;
      } else cell += char;
    } else if (char === '"') quoted = true;
    else if (char === ",") {
      row.push(cell);
      cell = "";
    } else if (char === "\n") {
      row.push(cell);
      rows.push(row);
      row = [];
      cell = "";
    } else cell += char;
  }
  if (cell.length || row.length) {
    row.push(cell);
    rows.push(row);
  }
  const [header, ...body] = rows;
  return {
    header,
    rows: body.map((item) => Object.fromEntries(header.map((name, index) => [name, item[index] === "" ? null : item[index]]))),
  };
}

test("filtered CSV keeps both family values and round-trips awkward cells", () => {
  const csv = filteredCsv(
    [
      {
        id: "model:a",
        name: "A \"quoted\"\nname",
        kind: "model",
        family: "pplx",
        revision: "abc",
        sets: 1,
        datasetIds: ["one", "two"],
        gold: 10,
        hit: 9,
        hidden: 8,
        rawHidden: 7,
        missed: 1,
        positiveRows: 5,
        residualRows: 2,
        tp: 30,
        fp: 3,
        fn: 4,
        negativeChars: 100,
        maskedNegativeChars: 6,
        untouched: 10,
        fullyHidden: 80,
        detected: 90,
        extra: 6,
        f1: 0.8,
        precision: 0.9,
        recall: 0.7,
        cpu: null,
        gpu: null,
        adapterSlices: [{ status: "corrected-rerun", policy: "capture-v2", runs: 1, unresolvedSpans: 0 }],
        adapterInventory: [{ status: "corrected-rerun", policy: "capture-v2", runs: 10, unresolvedSpans: 38 }],
      },
    ],
    {
      language: "ru",
      task: "pii",
      dataset: "all",
      sensitivity: false,
      family: "all",
      query: "=HYPERLINK(\"https://example.com\",\"open\")",
      scopeDatasetIds: ["one"],
      snapshotHash: "sha",
    },
  );
  const parsed = parseCsv(csv);
  assert.equal(parsed.header.length, new Set(parsed.header).size);
  assert.equal(parsed.header.includes("family"), false);
  assert.equal(parsed.rows[0].filter_family, "all");
  assert.equal(parsed.rows[0].system_family, "pplx");
  assert.equal(parsed.rows[0].name, "A \"quoted\"\nname");
  assert.equal(parsed.rows[0].cpu, null);
  assert.equal(parsed.rows[0].datasetIds, "[\"one\",\"two\"]");
  assert.match(parsed.rows[0].query, /^'=HYPERLINK/);
  assert.match(parsed.rows[0].adapterSlices, /corrected-rerun/);
  assert.match(parsed.rows[0].adapterInventory, /38/);
});

test("compare export records the selection and drops unused leaderboard filters", () => {
  const context = compareExportContext({
    view: "leaderboard",
    rowOrder: "fullyHidden:ascending",
    language: "ru",
    task: "secrets",
    dataset: "all",
    sensitivity: true,
    family: "pplx",
    query: "NO_MATCH_EXPECTED",
    coverage: "complete",
    sort: "fullyHidden",
    direction: "ascending",
    scopeDatasetIds: ["ignored"],
  }, ["model:gliner2-fastino", "model:pplx"], ["one", "two"]);
  assert.equal(context.sort, undefined);
  assert.equal(context.query, undefined);
  assert.equal(context.family, undefined);
  assert.equal(context.coverage, undefined);
  assert.equal(context.direction, undefined);
  assert.equal(context.language, "ru");
  assert.deepEqual(context.scopeDatasetIds, ["one", "two"]);
  const csv = filteredCsv(
    [{ id: "model:gliner2-fastino", name: "Fastino" }, { id: "model:pplx", name: "PPLX" }],
    context,
  );
  const parsed = parseCsv(csv);
  assert.equal(parsed.header.length, new Set(parsed.header).size);
  assert.deepEqual(parsed.rows.map((row) => row.id), ["model:gliner2-fastino", "model:pplx"]);
  assert.equal(parsed.rows[0].view, "compare");
  assert.equal(parsed.rows[0].rowOrder, "selection");
  assert.equal(parsed.rows[0].sort, null);
  assert.equal(parsed.rows[0].query, null);
  assert.equal(parsed.rows[0].filter_family, null);
  assert.equal(parsed.rows[0].direction, null);
  assert.equal(parsed.rows[0].comparisonSystemIds, "[\"model:gliner2-fastino\",\"model:pplx\"]");
});

test("scanner status follows the runs inside the active slice", () => {
  const benchmark = JSON.parse(fs.readFileSync(new URL("../public/data/benchmark.json", import.meta.url), "utf8"));
  const all = new Set(benchmark.datasets.map((dataset) => dataset.id));
  const gitleaks = aggregate(benchmark, all).find((score) => score.id === "model:gitleaks");
  const trufflehog = aggregate(benchmark, all).find((score) => score.id === "model:trufflehog");
  assert.deepEqual(gitleaks.adapterInventory, [{ status: "corrected-rerun", policy: "capture-v2", runs: 10, unresolvedSpans: 38 }]);
  assert.deepEqual(gitleaks.adapterSlices, [{ status: "corrected-rerun", policy: "capture-v2", runs: 9, unresolvedSpans: 32 }]);
  const oneDataset = aggregate(benchmark, new Set(["alrosait"])).find((score) => score.id === "model:gitleaks");
  assert.equal(oneDataset.adapterSlices[0].runs, 1);
  assert.equal(oneDataset.adapterSlices[0].unresolvedSpans, 0);
  assert.equal(oneDataset.adapterInventory[0].unresolvedSpans, 38);
  const withoutIssues = new Set([...all].filter((id) => id !== "secrets-issues"));
  const narrowed = aggregate(benchmark, withoutIssues).find((score) => score.id === "model:gitleaks");
  assert.equal(narrowed.adapterSlices[0].runs, 8);
  assert.equal(narrowed.adapterSlices[0].unresolvedSpans, 0);
  assert.deepEqual(trufflehog.adapterSlices, [{ status: "historical-pre-fix", policy: "", runs: 3, unresolvedSpans: 0 }]);
});

test("task=all survives every thematic default", () => {
  for (const initialTask of ["all", "pii", "secrets"]) {
    for (const task of ["all", "pii", "secrets"]) {
      const before = readExplorerSearch(`?task=${task}`, initialTask, [], [], []);
      const query = writeExplorerSearch(before);
      const after = readExplorerSearch(`?${query}`, initialTask, [], [], []);
      assert.equal(after.task, task, `${initialTask} ${task} -> ${query}`);
    }
  }
});

test("URL contract round-trips global and dashboard state", () => {
  const systems = [{ id: "model:a", kind: "model" }, { id: "model:b", kind: "model" }];
  const state = readExplorerSearch("?lang=ru&task=pii&compare=model%3Aa%2Cmodel%3Ab&difficulty=Hard&category=contact&domainQuery=fast", "all", systems, ["one"], ["contact"]);
  const encoded = writeExplorerSearch(state);
  const restored = readExplorerSearch(`?${encoded}`, "all", systems, ["one"], ["contact"]);
  assert.deepEqual(restored, state);
  assert.deepEqual(restored.selected, ["model:a", "model:b"]);
  assert.equal(restored.dashboard.difficultyTier, "Hard");
});

test("evidence links keep anchors in place and documents inside the viewer", () => {
  assert.equal(evidenceLink("#методика", "docs/index.md").kind, "anchor");
  assert.deepEqual(evidenceLink("../results/report.md", "docs/index.md"), { kind: "document", href: "/evidence/results/report.md", path: "results/report.md" });
  assert.deepEqual(evidenceLink("../results/report.md#details", "docs/index.md"), { kind: "document", href: "/evidence/results/report.md#details", path: "results/report.md#details" });
  assert.equal(evidenceLink("https://example.com", "docs/index.md").kind, "external");
  const seen = new Map();
  assert.equal(markdownHeadingId("Методика", seen), "методика");
  assert.equal(markdownHeadingId("Методика", seen), "методика-1");
});

test("route payloads include only the records needed by each view", () => {
  const data = { meta: {}, datasets: [], systems: [], records: [{ system: "model:a" }, { system: "composition:a+b" }], categories: [{ id: "x" }], speed: [{ model: "a" }], diagnostics: { large: true }, costs: [{ composition: "a" }], sensitivity: {} };
  assert.equal(benchmarkForView(data, "methodology").records.length, 0);
  assert.deepEqual(benchmarkForView(data, "methodology").categories, data.categories);
  assert.equal(benchmarkForView(data, "performance").speed.length, 1);
  assert.deepEqual(benchmarkForView(data, "compare").records.map(row => row.system), ["model:a"]);
  assert.deepEqual(benchmarkForView(data, "ensembles").records.map(row => row.system), ["composition:a+b"]);
});

test("generated model catalog is complete and site metadata does not depend on Markdown", () => {
  const catalog = JSON.parse(fs.readFileSync(new URL("../../results/model-catalog.json", import.meta.url), "utf8"));
  const benchmark = JSON.parse(fs.readFileSync(new URL("../public/data/benchmark.json", import.meta.url), "utf8"));
  const files = JSON.parse(fs.readFileSync(new URL("../public/data/files.json", import.meta.url), "utf8"));
  assert.equal(catalog.length, 62);
  assert.ok(catalog.every(entry => entry.id && entry.family && entry.revision));
  assert.ok(benchmark.systems.filter(system => system.kind === "model").every(system => system.family && system.revision));
  const four = benchmark.systems.find((system) => system.id === "composition:pplx+fastino+bardsai+mmbert");
  assert.equal(four.revision, null);
  assert.equal(four.upstream, null);
  assert.deepEqual(four.participants.map((item) => item.member), ["pplx", "gliner2-fastino", "bardsai-eu", "mmbert32k"]);
  assert.ok(four.participants.every((item) => item.revision && item.upstream));
  assert.equal(benchmark.systems.find((system) => system.id === "model:pplx").participants, undefined);
  assert.ok(files.some(entry => entry.path === "SECURITY.md"));
});

test("CPU notes separate saved throughput from a same-input comparison", () => {
  const readme = fs.readFileSync(new URL("../../README.md", import.meta.url), "utf8");
  const figure = fs.readFileSync(new URL("../../assets/cpu-speed.svg", import.meta.url), "utf8");
  const detectors = fs.readFileSync(new URL("../../results/detectors.md", import.meta.url), "utf8");
  assert.equal(readme.includes("rows are comparable"), false);
  assert.match(readme, /not a controlled same-input comparison and is not request latency/);
  assert.equal(figure.includes("directly comparable"), false);
  assert.match(figure, /not a same-input comparison/);
  assert.match(detectors, /not a controlled same-input comparison/);
});
