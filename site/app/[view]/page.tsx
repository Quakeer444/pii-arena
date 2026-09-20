import type { Metadata } from "next";
import { notFound } from "next/navigation";
import raw from "@/public/data/benchmark.json";
import { BenchmarkExplorer } from "@/components/benchmark-explorer";
import type { Benchmark } from "@/lib/benchmark";
import { benchmarkDatasetJsonLd, jsonLd } from "@/lib/structured-data";
import { pageMetadata, type BenchmarkView, VIEW_METADATA } from "@/lib/seo";

const views = Object.keys(VIEW_METADATA) as BenchmarkView[];
export const dynamicParams = false;

export function generateStaticParams() {
  return views.map((view) => ({ view }));
}

export async function generateMetadata({ params }: { params: Promise<{ view: string }> }): Promise<Metadata> {
  const { view } = await params;
  if (!views.includes(view as BenchmarkView)) return {};
  const entry = VIEW_METADATA[view as BenchmarkView];
  return pageMetadata(entry.title, entry.description, `/${view}`);
}

export default async function ViewPage({ params }: { params: Promise<{ view: string }> }) {
  const { view } = await params;
  if (!views.includes(view as BenchmarkView)) notFound();
  const data = raw as Benchmark;
  return (
    <>
      {view === "datasets" && (
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: jsonLd(benchmarkDatasetJsonLd(data)) }} />
      )}
      <BenchmarkExplorer data={data} initialView={view as BenchmarkView} />
    </>
  );
}
