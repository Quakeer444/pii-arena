import type { MetadataRoute } from "next";
import raw from "@/public/data/benchmark.json";
import type { Benchmark } from "@/lib/benchmark";
import { detectorSlug } from "@/lib/benchmark";
import { absoluteUrl, VIEW_METADATA } from "@/lib/seo";

export default function sitemap(): MetadataRoute.Sitemap {
  const data = raw as Benchmark;
  const lastModified = new Date(`${data.meta.revision}T00:00:00Z`);
  const fixed = [
    ...Object.keys(VIEW_METADATA).map((view) => `/${view}`),
    "/detectors",
    "/benchmarks/pii-detection",
    "/benchmarks/secrets-detection",
    "/benchmarks/latency",
    "/results/2026-09"
  ];
  const detectors = data.systems.filter((system) => system.kind === "model").map((system) => `/detectors/${detectorSlug(system.id)}`);
  const datasets = data.datasets.map((dataset) => `/datasets/${dataset.id}`);
  return [...fixed, ...detectors, ...datasets].map((path) => ({
    url: absoluteUrl(path),
    lastModified
  }));
}
