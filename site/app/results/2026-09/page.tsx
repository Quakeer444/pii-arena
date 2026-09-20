import type { Metadata } from "next";
import Link from "next/link";
import raw from "@/public/data/benchmark.json";
import { PublicationPage } from "@/components/publication-page";
import { aggregate, type Benchmark, n, percent, REF } from "@/lib/benchmark";
import { pageMetadata } from "@/lib/seo";

const title = "PII & secrets benchmark results — September 2026";
const description = "Frozen September 2026 PII and secret detector results across 41 datasets, 227,466 annotations and 2,591 saved prediction runs.";
export const metadata: Metadata = pageMetadata(title, description, "/results/2026-09");

export default function SeptemberResultsPage() {
  const data = raw as Benchmark;
  const score = aggregate(data, new Set(data.datasets.map((dataset) => dataset.id)), "composition").find((entry) => entry.id === REF);
  if (!score) return null;
  return (
    <PublicationPage eyebrow={`Release v${data.meta.version}`} title={title} description={description}>
      <div className="publication-summary">
        <div><strong>{n(data.datasets.length)}</strong><span>datasets</span></div>
        <div><strong>{n(data.datasets.reduce((sum, dataset) => sum + dataset.rows, 0))}</strong><span>input rows</span></div>
        <div><strong>{n(score.gold)}</strong><span>normalized annotations</span></div>
        <div><strong>{n(data.meta.runs)}</strong><span>saved prediction runs</span></div>
      </div>
      <section className="publication-panel publication-copy">
        <h2>Reference composition outcome</h2>
        <p>PPLX + Fastino GLiNER2 + mmBERT + BardsAI is a fixed reference composition used to illustrate masking behavior across the same retained datasets.</p>
        <dl className="publication-definition-list">
          <div><dt>Untouched annotations</dt><dd>{percent(score.untouched)} · {n(score.missed)} / {n(score.gold)}</dd></div>
          <div><dt>Fully hidden annotations</dt><dd>{percent(score.fullyHidden)} · {n(score.hidden)} / {n(score.gold)}</dd></div>
          <div><dt>Characters masked in unannotated rows</dt><dd>{percent(score.extra)}</dd></div>
          <div><dt>Result revision</dt><dd className="mono">{data.meta.revision}</dd></div>
        </dl>
        <p className="publication-note">The composition was inspected on this benchmark rather than selected on an independent deployment holdout. These figures are not production leak probabilities.</p>
        <div className="publication-actions">
          <Link className="action primary" href="/leaderboard">Explore results</Link>
          <Link className="action" href="/methodology">Read methodology</Link>
          <a className="action" href="/evidence/results/snapshot.json">Download snapshot</a>
        </div>
      </section>
    </PublicationPage>
  );
}
