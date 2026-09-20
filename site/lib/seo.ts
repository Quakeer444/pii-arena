import type { Metadata } from "next";

export const SITE_NAME = "PII Arena";
export const GITHUB_URL = "https://github.com/Quakeer444/pii-arena";
export const DEFAULT_DESCRIPTION =
  "The independent benchmark for PII and secret detectors. Compare masking quality, coverage and throughput across Russian, English and multilingual datasets.";

function productionOrigin() {
  const configured = process.env.SITE_URL;
  const value = configured ?? "https://www.piiarena.com";
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
      url: path,
      images: [{ url: "/og.png", width: 1280, height: 640, alt: "PII Arena detector leaderboard" }]
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
      images: ["/og.png"]
    }
  };
}

export const VIEW_METADATA = {
  leaderboard: {
    title: "PII & secrets detector leaderboard",
    description: "Rank PII and secret detectors by complete masking, detection, extra masking, character F1 and measured throughput."
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
