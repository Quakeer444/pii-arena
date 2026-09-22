import type { Metadata } from "next";
import Link from "next/link";
import raw from "@/public/data/benchmark.json";
import { PublicationPage } from "@/components/publication-page";
import { aggregate, type Benchmark, detectorSlug, n, percent } from "@/lib/benchmark";
import { pageMetadata } from "@/lib/seo";

const title = "Open source PII detector benchmark index";
const description = "Browse measured PII and secret detectors with direct pages for coverage, masking quality, character metrics and dataset-level outcomes.";
export const metadata: Metadata = pageMetadata(title, description, "/detectors");

export default function DetectorsPage() {
  const data = raw as Benchmark;
  const datasetIds = new Set(data.datasets.map((dataset) => dataset.id));
  const rows = aggregate(data, datasetIds)
    .sort((a, b) => Number(b.sets === datasetIds.size) - Number(a.sets === datasetIds.size) || (b.fullyHidden ?? -Infinity) - (a.fullyHidden ?? -Infinity));

  return (
    <PublicationPage view="detectors" eyebrow="Detector directory" title={title} description={description}>
      <div className="publication-summary">
        <div><strong>{n(rows.length)}</strong><span>measured configurations</span></div>
        <div><strong>{n(data.datasets.length)}</strong><span>retained datasets</span></div>
        <div><strong>{n(data.meta.runs)}</strong><span>saved prediction runs</span></div>
      </div>
      <section className="publication-panel">
        <div className="publication-panel-heading">
          <div><h2>All detector configurations</h2><p>Complete-coverage rows appear first, then rank by fully hidden annotations. Partial rows keep their original denominator.</p></div>
          <Link className="text-button" href="/compare">Interactive comparison</Link>
        </div>
        <div className="publication-table-scroll">
          <table className="publication-table">
            <thead><tr><th>Detector</th><th>Family</th><th>Datasets</th><th>Fully hidden ↑</th><th>Detected / any overlap ↑</th><th>Char F1 ↑</th></tr></thead>
            <tbody>
              {rows.map((row) => (
                <tr key={row.id}>
                  <td><Link href={`/detectors/${detectorSlug(row.id)}`}>{row.name}</Link></td>
                  <td>{row.family.toUpperCase()}</td>
                  <td className="mono">{row.sets}/{datasetIds.size}</td>
                  <td className="number">{percent(row.fullyHidden)}</td>
                  <td className="number">{percent(row.detected)}</td>
                  <td className="number">{row.f1?.toFixed(3) ?? "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
      <p className="publication-note">These measurements describe one frozen protocol. They are not a production-safety certification or a universal model ranking.</p>
    </PublicationPage>
  );
}
