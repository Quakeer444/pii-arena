import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import raw from "@/public/data/benchmark.json";
import { PublicationPage } from "@/components/publication-page";
import { aggregate, categoryScores, type Benchmark, detectorSlug, n, percent, ratio } from "@/lib/benchmark";
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
  const description = `Measured masking quality, character F1, dataset coverage and throughput for ${model.name} under the frozen PII Arena protocol.`;
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
    .sort((a, b) => (ratio(a.hidden, a.gold) ?? -Infinity) - (ratio(b.hidden, b.gold) ?? -Infinity));
  const categoryResults = categoryScores(data, model.id, datasetIds)
    .filter((entry) => entry.gold > 0)
    .sort((a, b) => (ratio(b.hidden, b.gold) ?? -Infinity) - (ratio(a.hidden, a.gold) ?? -Infinity));
  const strengths = categoryResults.slice(0, 3);
  const watchList = categoryResults.slice(-3).reverse();
  const languageScores = ["en", "ru", "multi"].map((language) => {
    const ids = new Set(data.datasets.filter((dataset) => dataset.lang === language).map((dataset) => dataset.id));
    return { language, score: aggregate(data, ids).find((entry) => entry.id === model.id) };
  }).filter((entry) => entry.score);
  const title = `${model.name} PII detection benchmark`;

  return (
    <PublicationPage
      eyebrow={`${model.family.toUpperCase()} detector`}
      title={title}
      description={`Measured on ${score.sets} of ${data.datasets.length} retained datasets under the same frozen scoring and masking protocol.`}
    >
      <div className="publication-summary">
        <div><strong>{percent(score.fullyHidden)}</strong><span>fully hidden annotations</span></div>
        <div><strong>{percent(score.detected)}</strong><span>detected / overlapped</span></div>
        <div><strong>{percent(score.extra)}</strong><span>extra masking</span></div>
        <div><strong>{score.cpu ? n(10_000 / score.cpu) : "—"}</strong><span>CPU characters / second</span></div>
      </div>
      <section className="detector-profile-grid">
        <div className="publication-panel detector-signal detector-signal-good">
          <div className="publication-panel-heading"><div><h2>Strengths</h2><p>Highest complete-masking rates by normalized data type.</p></div></div>
          <div className="detector-signal-list">{strengths.map((entry) => <div key={entry.id}><span>{entry.title}</span><strong>{percent(ratio(entry.hidden, entry.gold))}</strong><small>{n(entry.hidden)} / {n(entry.gold)}</small></div>)}</div>
        </div>
        <div className="publication-panel detector-signal detector-signal-watch">
          <div className="publication-panel-heading"><div><h2>Watch list</h2><p>Lowest observed complete-masking rates; inspect before deployment.</p></div></div>
          <div className="detector-signal-list">{watchList.map((entry) => <div key={entry.id}><span>{entry.title}</span><strong>{percent(ratio(entry.hidden, entry.gold))}</strong><small>{n(entry.hidden)} / {n(entry.gold)}</small></div>)}</div>
        </div>
      </section>
      <section className="publication-panel">
        <div className="publication-panel-heading"><div><h2>Language coverage</h2><p>The overall leader can differ from the best choice for one language slice.</p></div></div>
        <div className="publication-table-scroll"><table className="publication-table"><thead><tr><th>Language</th><th>Datasets</th><th>Fully hidden ↑</th><th>Detected ↑</th><th>Extra masking ↓</th></tr></thead><tbody>{languageScores.map(({language,score:languageScore}) => languageScore && <tr key={language}><td>{language === "en" ? "English" : language === "ru" ? "Russian" : "Multilingual"}</td><td className="number">{languageScore.sets}</td><td className="number metric-emphasis">{percent(languageScore.fullyHidden)}</td><td className="number">{percent(languageScore.detected)}</td><td className="number">{percent(languageScore.extra)}</td></tr>)}</tbody></table></div>
      </section>
      <section className="publication-panel publication-copy">
        <h2>Configuration, source and version</h2>
        <dl className="publication-definition-list">
          <div><dt>Family</dt><dd>{model.family.toUpperCase()}</dd></div>
          <div><dt>Revision</dt><dd className="mono">{model.revision || "Not recorded"}</dd></div>
          <div><dt>Eligible datasets</dt><dd>{score.sets} / {data.datasets.length}</dd></div>
          <div><dt>Character F1</dt><dd>{score.f1?.toFixed(3) ?? "Not measured"}</dd></div>
          <div><dt>Untouched diagnostic</dt><dd className="mono">{percent(score.untouched)} · {n(score.missed)} / {n(score.gold)}</dd></div>
          <div><dt>Benchmark version</dt><dd className="mono">{data.meta.version} · {data.meta.experimentDate}</dd></div>
          <div><dt>CPU seconds / 10k chars</dt><dd>{score.cpu?.toFixed(3) ?? "Not measured"}</dd></div>
          <div><dt>GPU seconds / 10k chars</dt><dd>{score.gpu?.toFixed(3) ?? "Not measured"}</dd></div>
        </dl>
        {model.flags && model.flags !== "-" && <p className="publication-note">{model.flags}</p>}
        <div className="publication-actions">
          {model.upstream && <a className="action" href={model.upstream}>Upstream model</a>}
          <Link className="action" href={`/compare?compare=${encodeURIComponent(`${model.id},model:pplx`)}`}>Compare detectors</Link>
          <a className="action" href="https://github.com/Quakeer444/pii-arena/blob/main/docs/models.md">Model catalog</a>
          <Link className="action" href="/methodology">Read methodology</Link>
        </div>
      </section>
      <section className="publication-panel">
        <div className="publication-panel-heading"><div><h2>Results by dataset</h2><p>Complete masking is primary; detection shows whether any character overlapped.</p></div></div>
        <div className="publication-table-scroll">
          <table className="publication-table">
            <thead><tr><th>Dataset</th><th>Gold annotations</th><th>Fully hidden ↑</th><th>Detected ↑</th><th>Extra masking ↓</th></tr></thead>
            <tbody>
              {rows.map((row) => (
                <tr key={row.dataset}>
                  <td><Link href={`/datasets/${row.dataset}`}>{row.dataset}</Link></td>
                  <td className="number">{n(row.gold)}</td>
                  <td className="number metric-emphasis">{percent(ratio(row.hidden, row.gold))}</td>
                  <td className="number">{percent(ratio(row.hit, row.gold))}</td>
                  <td className="number">{percent(ratio(row.maskedNegativeChars, row.negativeChars))}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </PublicationPage>
  );
}
