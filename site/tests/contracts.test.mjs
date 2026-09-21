import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

import { compareScores, filteredCsv, percent } from "../lib/benchmark.ts";
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
  assert.ok(files.some(entry => entry.path === "SECURITY.md"));
});
