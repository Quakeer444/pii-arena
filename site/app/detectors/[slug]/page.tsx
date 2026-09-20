import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import raw from "@/public/data/benchmark.json";
import { PublicationPage } from "@/components/publication-page";
import { aggregate, type Benchmark, detectorSlug, n, percent, ratio } from "@/lib/benchmark";
import { pageMetadata } from "@/lib/seo";

const data = raw as Benchmark;
const models = data.systems.filter((system) => system.kind === "model");
export const dynamicParams = false;

export function generateStaticParams() {
  return models.map((model) => ({ slug: detectorSlug(model.id) }));
}

function getModel(slug: string) {
  return models.find((model) => detectorSlug(model.id) === slug);
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const model = getModel(slug);
  if (!model) return {};
  const title = `${model.name} PII detection benchmark`;
  const description = `Measured masking quality, character F1, dataset coverage and throughput for ${model.name} under the frozen PII & Secrets Detection Benchmark protocol.`;
  return pageMetadata(title, description, `/detectors/${slug}`);
}

export default async function DetectorPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const model = getModel(slug);
  if (!model) notFound();
  const datasetIds = new Set(data.datasets.map((dataset) => dataset.id));
  const score = aggregate(data, datasetIds).find((entry) => entry.id === model.id);
  if (!score) notFound();
  const rows = data.records
    .filter((row) => row.system === model.id && !row.train)
    .sort((a, b) => (ratio(a.gold - a.hit, a.gold) ?? Infinity) - (ratio(b.gold - b.hit, b.gold) ?? Infinity));
  const title = `${model.name} PII detection benchmark`;

  return (
    <PublicationPage
      eyebrow={`${model.family.toUpperCase()} detector`}
      title={title}
      description={`Measured on ${score.sets} of ${data.datasets.length} retained datasets under the same frozen scoring and masking protocol.`}
    >
      <div className="publication-summary">
        <div><strong>{percent(score.untouched)}</strong><span>untouched annotations</span></div>
        <div><strong>{percent(score.fullyHidden)}</strong><span>fully hidden annotations</span></div>
        <div><strong>{score.f1?.toFixed(3) ?? "—"}</strong><span>pooled character F1</span></div>
        <div><strong>{score.sets}/{data.datasets.length}</strong><span>eligible datasets</span></div>
      </div>
      <section className="publication-panel publication-copy">
        <h2>Configuration</h2>
        <dl className="publication-definition-list">
          <div><dt>Family</dt><dd>{model.family.toUpperCase()}</dd></div>
          <div><dt>Revision</dt><dd className="mono">{model.revision || "Not recorded"}</dd></div>
          <div><dt>Untouched count</dt><dd className="mono">{n(score.missed)} / {n(score.gold)}</dd></div>
          <div><dt>Additional masked text</dt><dd>{percent(score.extra)}</dd></div>
          <div><dt>CPU seconds / 10k chars</dt><dd>{score.cpu?.toFixed(3) ?? "Not measured"}</dd></div>
          <div><dt>GPU seconds / 10k chars</dt><dd>{score.gpu?.toFixed(3) ?? "Not measured"}</dd></div>
        </dl>
        {model.flags && model.flags !== "-" && <p className="publication-note">{model.flags}</p>}
        <div className="publication-actions">
          {model.upstream && <a className="action" href={model.upstream}>Upstream model</a>}
          <Link className="action" href="/compare">Compare detectors</Link>
          <Link className="action" href="/methodology">Read methodology</Link>
        </div>
      </section>
      <section className="publication-panel">
        <div className="publication-panel-heading"><div><h2>Results by dataset</h2><p>Lower untouched and higher fully hidden are better. Counts remain visible.</p></div></div>
        <div className="publication-table-scroll">
          <table className="publication-table">
            <thead><tr><th>Dataset</th><th>Gold annotations</th><th>Untouched ↓</th><th>Fully hidden ↑</th></tr></thead>
            <tbody>
              {rows.map((row) => (
                <tr key={row.dataset}>
                  <td><Link href={`/datasets/${row.dataset}`}>{row.dataset}</Link></td>
                  <td className="number">{n(row.gold)}</td>
                  <td className="number">{percent(ratio(row.gold - row.hit, row.gold))}</td>
                  <td className="number">{percent(ratio(row.hidden, row.gold))}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </PublicationPage>
  );
}
