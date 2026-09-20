import type { Metadata } from "next";

export const SITE_NAME = "PII Bench";
export const GITHUB_URL = "https://github.com/Quakeer444/pii-secrets-benchmark";
export const DEFAULT_DESCRIPTION =
  "Compare PII and secret detectors across Russian, English and multilingual datasets with exact masking, quality and throughput measurements.";

function productionOrigin() {
  const configured = process.env.SITE_URL;
  const vercel = process.env.VERCEL_PROJECT_PRODUCTION_URL;
  const value = configured ?? (vercel ? `https://${vercel}` : "http://localhost:3000");
  return value.replace(/\/$/, "");
}

export const SITE_URL = productionOrigin();

export function absoluteUrl(path = "/") {
  return new URL(path, `${SITE_URL}/`).toString();
}

export function pageMetadata(title: string, description: string, path: string): Metadata {
  return {
    title,
    description,
    alternates: { canonical: path },
    openGraph: {
      type: "website",
      siteName: SITE_NAME,
      title,
      description,
      url: path
    },
    twitter: {
      card: "summary",
      title,
      description
    }
  };
}

export const VIEW_METADATA = {
  leaderboard: {
    title: "PII & secrets detector leaderboard",
    description: "Rank PII and secret detectors by untouched annotations, complete masking, character F1 and measured throughput."
  },
  compare: {
    title: "Compare PII detectors",
    description: "Compare up to four PII and secret detectors on the same eligible datasets and denominator."
  },
  ensembles: {
    title: "PII detector ensembles",
    description: "Compare fixed detector compositions and the tradeoff between complete masking and additional masked text."
  },
  entities: {
    title: "PII detection by data type",
    description: "Inspect complete masking for names, credentials, addresses, identifiers, network data and other sensitive data types."
  },
  datasets: {
    title: "PII benchmark datasets",
    description: "Browse 41 Russian, English and multilingual PII and secrets datasets with provenance, licenses and measured outcomes."
  },
  performance: {
    title: "PII detector speed benchmark",
    description: "Compare measured CPU and GPU throughput for PII and secret detectors with hardware and workload conditions visible."
  },
  methodology: {
    title: "PII benchmark methodology",
    description: "Read the frozen benchmark protocol, scoring contract, masking rules, exclusions, denominators and limitations."
  },
  downloads: {
    title: "PII benchmark reports and data",
    description: "Download the complete benchmark snapshot, CSV exports, reports, figures and reproducibility evidence."
  }
} as const;

export type BenchmarkView = keyof typeof VIEW_METADATA;
