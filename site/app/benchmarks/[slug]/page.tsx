import type { Metadata } from "next";
import { notFound } from "next/navigation";
import raw from "@/public/data/benchmark.json";
import { BenchmarkExplorer } from "@/components/benchmark-explorer";
import type { Benchmark } from "@/lib/benchmark";
import { pageMetadata } from "@/lib/seo";

const pages = {
  "pii-detection": {
    title: "Open source PII detection benchmark",
    description: "Compare PII detectors on Russian, English and multilingual datasets using exact masking and character-level metrics.",
    view: "leaderboard",
    task: "pii"
  },
  "secrets-detection": {
    title: "Open source secret detection benchmark",
    description: "Compare secret scanners and detection models on retained secrets datasets using the same masking and scoring protocol.",
    view: "leaderboard",
    task: "secrets"
  },
  latency: {
    title: "PII detector latency and throughput benchmark",
    description: "Compare measured CPU and GPU throughput with hardware, worker count, dataset count and amortized row timings visible.",
    view: "performance",
    task: "all"
  }
} as const;

export const dynamicParams = false;
export function generateStaticParams() {
  return Object.keys(pages).map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const page = pages[slug as keyof typeof pages];
  if (!page) return {};
  return pageMetadata(page.title, page.description, `/benchmarks/${slug}`);
}

export default async function BenchmarkPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const page = pages[slug as keyof typeof pages];
  if (!page) notFound();
  return (
    <BenchmarkExplorer
      data={raw as Benchmark}
      initialView={page.view}
      initialTask={page.task}
      titleOverride={page.title}
      descriptionOverride={page.description}
    />
  );
}
