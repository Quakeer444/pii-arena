import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import raw from "@/public/data/benchmark.json";
import { PublicationPage } from "@/components/publication-page";
import { aggregate, type Benchmark, detectorSlug, n, percent } from "@/lib/benchmark";
import { pageMetadata } from "@/lib/seo";
import { datasetJsonLd, jsonLd } from "@/lib/structured-data";

const data = raw as Benchmark;
export const dynamicParams = false;

export function generateStaticParams() {
  return data.datasets.map((dataset) => ({ id: dataset.id }));
}

function getDataset(id: string) {
  return data.datasets.find((dataset) => dataset.id === id);
}

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const { id } = await params;
  const dataset = getDataset(id);
  if (!dataset) return {};
  const title = `${dataset.id} PII detection benchmark results`;
  const description = `${dataset.id}: ${n(dataset.rows)} rows and ${n(dataset.gold_spans)} normalized annotations, with detector-level PII and secret masking outcomes.`;
  return pageMetadata(title, description, `/datasets/${id}`);
}

export default async function DatasetPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const dataset = getDataset(id);
  if (!dataset) notFound();
  const scores = aggregate(data, new Set([dataset.id]))
    .filter((score) => score.sets === 1)
    .sort((a, b) => (a.untouched ?? Infinity) - (b.untouched ?? Infinity));
  const title = `${dataset.id} PII detection benchmark results`;

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: jsonLd(datasetJsonLd(dataset, data)) }} />
      <PublicationPage
        eyebrow={`${dataset.lang.toUpperCase()} · ${dataset.kind.toUpperCase()}`}
        title={title}
        description={`A frozen evaluation slice with ${n(dataset.rows)} rows, ${n(dataset.gold_spans)} normalized gold annotations and source-level provenance.`}
      >
        <div className="publication-summary">
          <div><strong>{n(dataset.rows)}</strong><span>input rows</span></div>
          <div><strong>{n(dataset.gold_spans)}</strong><span>gold annotations</span></div>
          <div><strong>{n(dataset.characters)}</strong><span>characters</span></div>
          <div><strong>{n(scores.length)}</strong><span>measured detectors</span></div>
        </div>
        <section className="publication-panel publication-copy">
          <h2>Dataset provenance</h2>
          <dl className="publication-definition-list">
            <div><dt>Language group</dt><dd>{dataset.lang.toUpperCase()}</dd></div>
            <div><dt>Task</dt><dd>{dataset.kind.toUpperCase()}</dd></div>
            <div><dt>License</dt><dd>{dataset.license}</dd></div>
            <div><dt>Data categories</dt><dd>{dataset.groups.join(", ")}</dd></div>
            <div><dt>Project generated</dt><dd>{dataset.synthetic ? "Yes" : "No"}</dd></div>
            <div><dt>Corrupted copy</dt><dd>{dataset.corrupted ? "Yes" : "No"}</dd></div>
          </dl>
          <div className="publication-actions">
            {dataset.source.startsWith("http") && <a className="action" href={dataset.source}>Original source</a>}
            <a className="action" href={`/evidence/results/datasets/${dataset.id}.md`}>Dataset report</a>
            <Link className="action" href="/datasets">All datasets</Link>
          </div>
          <p className="publication-note">Rows without annotations are not verified clean. Reported extra masking is not a human-confirmed false-positive rate.</p>
        </section>
        <section className="publication-panel">
          <div className="publication-panel-heading"><div><h2>Detector outcomes</h2><p>Sorted by untouched annotations. Training-source overlaps are excluded.</p></div></div>
          <div className="publication-table-scroll">
            <table className="publication-table">
              <thead><tr><th>Detector</th><th>Family</th><th>Untouched ↓</th><th>Fully hidden ↑</th><th>Extra masking ↓</th><th>Char F1 ↑</th></tr></thead>
              <tbody>
                {scores.map((score) => (
                  <tr key={score.id}>
                    <td><Link href={`/detectors/${detectorSlug(score.id)}`}>{score.name}</Link></td>
                    <td>{score.family.toUpperCase()}</td>
                    <td className="number">{percent(score.untouched)}</td>
                    <td className="number">{percent(score.fullyHidden)}</td>
                    <td className="number">{percent(score.extra)}</td>
                    <td className="number">{score.f1?.toFixed(3) ?? "—"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      </PublicationPage>
    </>
  );
}
