import type { Benchmark, Dataset } from "@/lib/benchmark";
import { absoluteUrl, GITHUB_URL } from "@/lib/seo";

const creator = {
  "@type": "Person",
  name: "Quakeer444",
  sameAs: "https://github.com/Quakeer444"
};

export function benchmarkDatasetJsonLd(data: Benchmark) {
  return {
    "@context": "https://schema.org",
    "@type": "Dataset",
    name: `PII Arena Results v${data.meta.version}`,
    description:
      "Reproducible detector measurements across Russian, English and multilingual PII and secrets datasets, including exact masking outcomes, character metrics and CPU/GPU throughput.",
    creator,
    license: "https://opensource.org/license/mit",
    datePublished: data.meta.experimentDate,
    dateModified: data.meta.revision,
    version: data.meta.version,
    url: absoluteUrl("/datasets"),
    sameAs: GITHUB_URL,
    includedInDataCatalog: {
      "@type": "DataCatalog",
      name: "PII Arena",
      url: absoluteUrl("/datasets")
    },
    distribution: [
      {
        "@type": "DataDownload",
        encodingFormat: "application/json",
        contentUrl: absoluteUrl("/evidence/results/snapshot.json")
      },
      {
        "@type": "DataDownload",
        encodingFormat: "text/csv",
        contentUrl: absoluteUrl("/data/all-results.csv")
      },
      {
        "@type": "DataDownload",
        encodingFormat: "text/csv",
        contentUrl: absoluteUrl("/data/categories.csv")
      }
    ]
  };
}

export function datasetJsonLd(dataset: Dataset, data: Benchmark) {
  const basedOn = dataset.source.startsWith("http") ? dataset.source : GITHUB_URL;
  return {
    "@context": "https://schema.org",
    "@type": "Dataset",
    name: `${dataset.id} benchmark evaluation slice`,
    description: `${dataset.id} is evaluated in PII Arena across ${dataset.rows.toLocaleString("en-US")} input rows and ${dataset.gold_spans.toLocaleString("en-US")} normalized gold annotations. This page reports detector outcomes under the frozen ${data.meta.experimentDate} protocol.`,
    creator,
    identifier: dataset.id,
    license: dataset.license,
    datePublished: data.meta.experimentDate,
    dateModified: data.meta.revision,
    url: absoluteUrl(`/datasets/${dataset.id}`),
    isBasedOn: basedOn,
    isPartOf: {
      "@type": "Dataset",
      name: `PII Arena Results v${data.meta.version}`,
      url: absoluteUrl("/datasets")
    }
  };
}

export function jsonLd(value: unknown) {
  return JSON.stringify(value).replace(/</g, "\\u003c");
}
