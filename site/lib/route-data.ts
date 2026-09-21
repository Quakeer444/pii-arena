import type { Benchmark } from "./benchmark.ts";

const fullRecordViews = new Set(["leaderboard", "entities"]);

export function benchmarkForView(data: Benchmark, view: string): Benchmark {
  const records = fullRecordViews.has(view)
    ? data.records
    : view === "compare"
      ? data.records.filter((row) => row.system.startsWith("model:"))
      : view === "ensembles"
        ? data.records.filter((row) => row.system.startsWith("composition:"))
        : [];
  const needsSpeed = ["leaderboard", "compare", "performance"].includes(view);
  return {
    ...data,
    records,
    speed: needsSpeed ? data.speed : [],
    diagnostics: {},
    costs: [],
  };
}
