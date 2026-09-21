"use client";

import { useMemo, type CSSProperties, type ReactNode } from "react";
import Link from "next/link";
import { ArrowRight, CircleHelp, Search } from "lucide-react";
import {
  aggregate,
  detectorSlug,
  percent,
  type Benchmark,
} from "@/lib/benchmark";
import {
  DIFFICULTY,
  MODEL_LABELS,
  type DifficultyTier,
} from "@/lib/decision-data";
import {
  buildDecisionMetrics,
  type DecisionMetrics,
  type DomainRow,
  type RobustnessRow,
  type SliceRow,
} from "@/lib/decision-metrics";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip";

const tiers: DifficultyTier[] = ["Easy", "Medium", "Hard", "Extreme"];
export type DecisionDashboardState = {
  difficultyTier: DifficultyTier | "All";
  difficultyQuery: string;
  robustnessQuery: string;
  domainQuery: string;
  category: string;
};
const configurations = [
  { id: "pplx", name: "PPLX", label: "Single detector", kind: "solo" },
  {
    id: "fastino",
    name: "GLiNER2 Fastino",
    label: "Single detector",
    kind: "solo",
  },
  {
    id: "pplx+fastino",
    name: "Fastino + PPLX",
    label: "Two detectors",
    kind: "cuda",
  },
  {
    id: "pplx+fastino+mmbert",
    name: "Fastino + PPLX + mmBERT",
    label: "Three detectors",
    kind: "cuda",
  },
  {
    id: "pplx+fastino+bardsai",
    name: "Fastino + PPLX + BardsAI EU",
    label: "CPU + GPU",
    kind: "hybrid",
  },
  {
    id: "pplx+fastino+bardsai+mmbert",
    name: "Fastino + PPLX + BardsAI EU + mmBERT",
    label: "Four detectors",
    kind: "hybrid",
  },
] as const;

function label(id: string) {
  return MODEL_LABELS[id] ?? id.replace("model:", "");
}

function matchesModel(row: { name: string; system: string }, query: string) {
  return `${row.name} ${row.system}`
    .toLowerCase()
    .includes(query.toLowerCase().trim());
}

function SectionTitle({
  id,
  number,
  title,
  children,
}: {
  id: string;
  number: string;
  title: string;
  children: ReactNode;
}) {
  return (
    <header className="decision-section-title" id={id}>
      <span className="decision-section-number mono">{number}</span>
      <div>
        <h2>{title}</h2>
        <p>{children}</p>
      </div>
    </header>
  );
}

function Card({
  title,
  description,
  children,
  tools,
  note,
  className = "",
}: {
  title: string;
  description: string;
  children: ReactNode;
  tools?: ReactNode;
  note?: string;
  className?: string;
}) {
  return (
    <article className={`decision-view ${className}`}>
      <div className="decision-view-head">
        <div>
          <h3>
            {title}
            {note && (
              <Tooltip>
                <TooltipTrigger asChild>
                  <button
                    type="button"
                    className="decision-info"
                    aria-label={`About ${title}`}
                  >
                    <CircleHelp />
                  </button>
                </TooltipTrigger>
                <TooltipContent className="max-w-80 leading-relaxed">
                  {note}
                </TooltipContent>
              </Tooltip>
            )}
          </h3>
          <p>{description}</p>
        </div>
        {tools}
      </div>
      {children}
    </article>
  );
}

function Scroll({
  label,
  children,
  className = "",
}: {
  label: string;
  children: ReactNode;
  className?: string;
}) {
  return (
    <div
      className={`decision-scroll ${className}`}
      role="region"
      aria-label={label}
      tabIndex={0}
    >
      {children}
    </div>
  );
}

function ModelName({
  system,
  name,
  complete = true,
}: {
  system: string;
  name?: string;
  complete?: boolean;
}) {
  return (
    <div className="decision-model-name">
      <Link
        href={`/detectors/${detectorSlug(system)}`}
        title={name ?? label(system)}
      >
        {name ?? label(system)}
      </Link>
      {!complete && (
        <small
          className="coverage-note"
          title="Some datasets are missing or excluded because of training overlap. Compare only shared datasets."
        >
          Not all datasets
        </small>
      )}
    </div>
  );
}

function SearchBox({
  value,
  onChange,
  placeholder,
  label: accessibleLabel,
}: {
  value: string;
  onChange: (value: string) => void;
  placeholder: string;
  label: string;
}) {
  return (
    <label className="decision-search">
      <Search size={14} />
      <input
        aria-label={accessibleLabel}
        value={value}
        onChange={(event) => onChange(event.target.value)}
        placeholder={placeholder}
      />
    </label>
  );
}

function DifficultyMap({
  datasetIds,
  tier,
  query,
  onTier,
  onQuery,
}: {
  datasetIds: Set<string>;
  tier: DifficultyTier | "All";
  query: string;
  onTier: (value: DifficultyTier | "All") => void;
  onQuery: (value: string) => void;
}) {
  const scopedRows = [...DIFFICULTY].filter((row) =>
    datasetIds.has(row.dataset),
  );
  const rows = scopedRows
    .filter(
      (row) =>
        (tier === "All" || row.tier === tier) &&
        row.dataset.includes(query.toLowerCase().trim()),
    )
    .sort((a, b) => b.score - a.score);
  return (
    <Card
      title="Hardest datasets"
      description="Higher scores mean the dataset was harder for the tested detectors."
      note="Difficulty is empirical: 100 minus the median fully hidden score of the frozen four-detector panel in release v1.0.3. Tiers use the recorded release thresholds."
      tools={
        <SearchBox
          value={query}
          onChange={onQuery}
          placeholder="Find a dataset…"
          label="Search datasets by difficulty"
        />
      }
    >
      <div
        className="difficulty-filters"
        role="group"
        aria-label="Filter datasets by difficulty"
      >
        <button
          type="button"
          aria-pressed={tier === "All"}
          onClick={() => onTier("All")}
        >
          All levels
        </button>
        {tiers.map((item) => (
          <button
            type="button"
            key={item}
            className={`tier-${item.toLowerCase()}`}
            aria-pressed={tier === item}
            onClick={() => onTier(item)}
          >
            <i />
            {item}
            <span className="mono">
              {scopedRows.filter((row) => row.tier === item).length}
            </span>
          </button>
        ))}
      </div>
      <Scroll label="Dataset difficulty results" className="difficulty-scroll">
        <div className="difficulty-map">
          {rows.map((row) => (
            <Link
              href={`/datasets/${row.dataset}`}
              key={row.dataset}
              className={`difficulty-cell tier-${row.tier.toLowerCase()}`}
            >
              <span title={row.dataset}>{row.dataset}</span>
              <div>
                <strong className="mono">{percent(row.score, 1)}</strong>
                <small>{row.tier}</small>
              </div>
              <div className="difficulty-meter">
                <i style={{ width: `${row.score}%` }} />
              </div>
            </Link>
          ))}
        </div>
        {!rows.length && (
          <p className="decision-empty">No datasets match this search.</p>
        )}
      </Scroll>
    </Card>
  );
}

function Robustness({
  rows,
  query,
  onQuery,
}: {
  rows: RobustnessRow[];
  query: string;
  onQuery: (value: string) => void;
}) {
  const filtered = rows.filter((row) => matchesModel(row, query));
  return (
    <Card
      title="Performance from easy to extreme"
      description="Dataset average · see how much sensitive data each detector hides completely at every difficulty level. Higher is better."
      note="Each value is the average across datasets in that level. Known training overlaps are removed; detectors covering all datasets are shown first."
      tools={
        <SearchBox
          value={query}
          onChange={onQuery}
          placeholder="Find a detector…"
          label="Search detectors by difficulty"
        />
      }
    >
      <Scroll
        label="Detector results by difficulty"
        className="robustness-scroll"
      >
        <table className="robustness-table">
          <thead>
            <tr>
              <th scope="col">Detector</th>
              {tiers.map((tier) => (
                <th
                  scope="col"
                  key={tier}
                  className={`tier-${tier.toLowerCase()}`}
                >
                  <i className="difficulty-dot" />
                  {tier}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {filtered.map((row) => (
              <tr key={row.system}>
                <th scope="row">
                  <ModelName
                    system={row.system}
                    name={row.name}
                    complete={row.complete}
                  />
                </th>
                {tiers.map((tier) => (
                  <td
                    key={tier}
                    className={`tier-${tier.toLowerCase()}`}
                    title={`${tier}: ${percent(row[tier])}; ${row.coverage[tier].gold.toLocaleString("en-US")} labeled items`}
                  >
                    <span
                      className="robustness-value"
                      style={
                        { "--value": `${row[tier] ?? 0}%` } as CSSProperties
                      }
                    >
                      {percent(row[tier], 1)}
                    </span>
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
        {!filtered.length && (
          <p className="decision-empty">No detectors match this search.</p>
        )}
      </Scroll>
    </Card>
  );
}

function Protection({
  data,
  datasetIds,
}: {
  data: Benchmark;
  datasetIds: Set<string>;
}) {
  const rows = useMemo(() => {
    const scores = aggregate(data, datasetIds, "composition");
    return configurations.flatMap((config) => {
      const score = scores.find((row) => row.id === `composition:${config.id}`);
      return score
        ? [{ ...config, ...score, title: config.name, kind: config.kind }]
        : [];
    });
  }, [data, datasetIds]);
  return (
    <Card
      title="One detector vs several combined"
      description="See whether combining detectors hides more sensitive data and how much extra text it masks."
      note="These combinations merge saved predictions. Extra text masked is measured on rows without labels, not verified false positives."
      tools={
        <Link className="decision-text-link" href="/ensembles">
          See combinations
          <ArrowRight size={14} />
        </Link>
      }
      className="protection-card"
    >
      <Scroll
        label="Compare single and combined detectors"
        className="protection-scroll"
      >
        <table className="protection-table">
          <thead>
            <tr>
              <th scope="col">Detector setup</th>
              <th scope="col">
                Completely hidden, % ↑
                <div className="protection-ruler mono">
                  <span>0%</span>
                  <span>50%</span>
                  <span>100%</span>
                </div>
              </th>
              <th scope="col">Extra text masked, % ↓</th>
              <th scope="col">Not fully hidden, items ↓</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((row) => (
              <tr key={row.id} className={`protection-${row.kind}`}>
                <th scope="row">
                  <span className="configuration-kind">{row.label}</span>
                  <strong>{row.title}</strong>
                </th>
                <td>
                  <div className="protection-bar">
                    <b className="mono">{percent(row.fullyHidden)}</b>
                    <span>
                      <i style={{ width: `${row.fullyHidden ?? 0}%` }} />
                    </span>
                  </div>
                </td>
                <td>
                  <div className="extra-bar">
                    <i style={{ width: `${row.extra ?? 0}%` }} />
                    <span className="mono">{percent(row.extra)}</span>
                  </div>
                </td>
                <td className="mono protection-residual">
                  {(row.gold - row.hidden).toLocaleString("en-US")}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Scroll>
      <div className="protection-foot">
        <div className="decision-legend">
          <span>
            <i className="legend-solo" />
            Single detector
          </span>
          <span>
            <i className="legend-cuda" />
            Runs on CUDA
          </span>
          <span>
            <i className="legend-hybrid" />
            CPU + GPU
          </span>
        </div>
      </div>
    </Card>
  );
}

function Domains({
  rows,
  query,
  onQuery,
}: {
  rows: DomainRow[];
  query: string;
  onQuery: (value: string) => void;
}) {
  const filtered = rows.filter((row) => matchesModel(row, query));
  return (
    <Card
      title="PII datasets vs secrets datasets"
      description="Pooled annotations · compare how well each detector hides labeled items in datasets assigned to each task."
      note="This split uses each dataset's task. Category results below instead group individual annotations by type. Detectors covering all datasets are shown first."
      tools={
        <SearchBox
          value={query}
          onChange={onQuery}
          placeholder="Find a detector…"
          label="Search detectors by data type"
        />
      }
    >
      <Scroll
        label="Detector results for personal data and secrets"
        className="domain-scroll"
      >
        <div className="domain-head">
          <span>Detector</span>
          <span>PII datasets</span>
          <span>Secrets datasets</span>
        </div>
        {filtered.map((row) => (
          <div className="domain-row" key={row.system}>
            <ModelName
              system={row.system}
              name={row.name}
              complete={row.complete}
            />
            {(["pii", "secrets"] as const).map((domain) => (
              <div
                className={`domain-value domain-${domain}`}
                key={domain}
                title={`${domain === "pii" ? "PII datasets" : "Secrets datasets"}: ${percent(row[domain])}`}
              >
                <i style={{ width: `${row[domain] ?? 0}%` }} />
                <span className="mono">{percent(row[domain], 1)}</span>
              </div>
            ))}
          </div>
        ))}
        {!filtered.length && (
          <p className="decision-empty">No detectors match this search.</p>
        )}
      </Scroll>
    </Card>
  );
}

function Rankings({
  rows,
  className = "",
}: {
  rows: SliceRow[];
  className?: string;
}) {
  return (
    <div className={`slice-rankings ${className}`}>
      {rows.map((row) => (
        <div className="slice-row" key={row.system}>
          <ModelName
            system={row.system}
            name={row.name}
            complete={row.complete}
          />
          <div
            className="slice-score mono"
            title={`${row.coverage.gold.toLocaleString("en-US")} labeled items`}
          >
            {percent(row.value, 1)}
            <div className="slice-track">
              <i style={{ width: `${row.value ?? 0}%` }} />
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

function Categories({
  data,
  slices,
  category,
  onCategory,
}: {
  data: Benchmark;
  slices: DecisionMetrics["categories"];
  category: string;
  onCategory: (value: string) => void;
}) {
  const leaders = data.categories.flatMap((item) => {
    const winner = slices[item.id]?.[0];
    return winner?.value === null || winner === undefined
      ? []
      : [{ ...winner, label: item.title }];
  });
  return (
    <Card
      title="Best detector by data type"
      description="Pooled annotations by annotation type · choose what sensitive data you need to hide."
      note="Overview and expanded rankings use the same scoped datasets, all measured configurations, complete coverage first, and known training-overlap exclusions."
      tools={
        <select
          className="decision-select"
          aria-label="Choose a sensitive data type"
          value={category}
          onChange={(event) => onCategory(event.target.value)}
        >
          <option value="overview">All data types</option>
          {data.categories.map((item) => (
            <option key={item.id} value={item.id}>
              {item.title}
            </option>
          ))}
        </select>
      }
    >
      <Scroll
        label="Category specialization results"
        className="category-scroll"
      >
        {category === "overview" ? (
          <div className="category-leaders">
            {leaders.map((row) => (
              <div key={row.label}>
                <span>{row.label}</span>
                <strong className="mono">{percent(row.value, 1)}</strong>
                <Link href={`/detectors/${detectorSlug(row.system)}`}>
                  {row.name}
                </Link>
                <small>
                  {row.coverage.gold.toLocaleString("en-US")} labeled items
                </small>
                <div className="category-meter">
                  <i style={{ width: `${row.value}%` }} />
                </div>
              </div>
            ))}
          </div>
        ) : (
          <Rankings rows={slices[category] ?? []} />
        )}
      </Scroll>
    </Card>
  );
}

export function DecisionDashboard({
  data,
  datasetIds,
  state,
  onChange,
}: {
  data: Benchmark;
  datasetIds: Set<string>;
  state: DecisionDashboardState;
  onChange: <K extends keyof DecisionDashboardState>(
    key: K,
    value: DecisionDashboardState[K],
  ) => void;
}) {
  const metrics = useMemo(
    () => buildDecisionMetrics(data, datasetIds),
    [data, datasetIds],
  );
  return (
    <div className="decision-dashboard">
      <SectionTitle
        id="dataset-difficulty"
        number="01"
        title="Start with what you need to protect"
      >
        Compare personal data, secrets, and the datasets where detectors
        struggle.
      </SectionTitle>
      <div className="decision-grid difficulty-grid">
        <Robustness
          rows={metrics.robustness}
          query={state.robustnessQuery}
          onQuery={(value) => onChange("robustnessQuery", value)}
        />
        <Domains
          rows={metrics.domains}
          query={state.domainQuery}
          onQuery={(value) => onChange("domainQuery", value)}
        />
      </div>
      <SectionTitle
        id="protection-comparison"
        number="02"
        title="Use one detector or combine several?"
      >
        See what combining detectors adds and how much extra text it masks.
      </SectionTitle>
      <Protection data={data} datasetIds={datasetIds} />
      <SectionTitle
        id="model-specialization"
        number="03"
        title="Find the best detector for each data type"
      >
        Focus on the sensitive information your application needs to protect.
      </SectionTitle>
      <div className="decision-grid specialization-grid">
        <DifficultyMap
          datasetIds={datasetIds}
          tier={state.difficultyTier}
          query={state.difficultyQuery}
          onTier={(value) => onChange("difficultyTier", value)}
          onQuery={(value) => onChange("difficultyQuery", value)}
        />
        <Categories
          data={data}
          slices={metrics.categories}
          category={state.category}
          onCategory={(value) => onChange("category", value)}
        />
      </div>
      <div id="detector-results" className="decision-table-anchor" />
    </div>
  );
}
