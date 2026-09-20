"use client";

import { useMemo, useState, type CSSProperties, type ReactNode } from "react";
import Link from "next/link";
import { ArrowDown, ArrowRight, Cpu, Gauge, Layers3, Search } from "lucide-react";
import { aggregate, detectorSlug, percent, type Benchmark } from "@/lib/benchmark";
import { CATEGORY_LEADERS, DIFFICULTY, HARDWARE, MODEL_LABELS, STACK_GAIN, type DifficultyTier } from "@/lib/decision-data";
import { buildDecisionMetrics, type DecisionMetrics, type DomainRow, type RobustnessRow, type SliceRow } from "@/lib/decision-metrics";

const tiers: DifficultyTier[] = ["Easy", "Medium", "Hard", "Extreme"];
const configurations = [
  { id: "pplx", name: "PPLX", label: "Single model", kind: "solo" },
  { id: "fastino", name: "GLiNER2 Fastino", label: "Single model", kind: "solo" },
  { id: "pplx+fastino", name: "Fastino + PPLX", label: "CUDA pair", kind: "cuda" },
  { id: "pplx+fastino+mmbert", name: "Fastino + PPLX + mmBERT", label: "Best CUDA stack", kind: "cuda" },
  { id: "pplx+fastino+bardsai", name: "Fastino + PPLX + BardsAI EU", label: "Hybrid stack", kind: "hybrid" },
  { id: "pplx+fastino+bardsai+mmbert", name: "Fastino + PPLX + BardsAI EU + mmBERT", label: "Maximum protection", kind: "hybrid" },
] as const;

function label(id: string) {
  return MODEL_LABELS[id] ?? id.replace("model:", "");
}

function matchesModel(row: { name: string; system: string }, query: string) {
  return `${row.name} ${row.system}`.toLowerCase().includes(query.toLowerCase().trim());
}

function SectionTitle({ id, number, title, children }: { id: string; number: string; title: string; children: ReactNode }) {
  return <header className="decision-section-title" id={id}>
    <span className="decision-section-number mono">{number}</span>
    <div><h2>{title}</h2><p>{children}</p></div>
  </header>;
}

function Card({ title, description, children, tools, className = "" }: { title: string; description: string; children: ReactNode; tools?: ReactNode; className?: string }) {
  return <article className={`decision-view ${className}`}>
    <div className="decision-view-head"><div><h3>{title}</h3><p>{description}</p></div>{tools}</div>
    {children}
  </article>;
}

function Scroll({ label, children, className = "" }: { label: string; children: ReactNode; className?: string }) {
  return <div className={`decision-scroll ${className}`} role="region" aria-label={label} tabIndex={0}>{children}</div>;
}

function ModelName({ system, name, complete = true }: { system: string; name?: string; complete?: boolean }) {
  return <div className="decision-model-name">
    <Link href={`/detectors/${detectorSlug(system)}`} title={name ?? label(system)}>{name ?? label(system)}</Link>
    {!complete && <small className="coverage-note" title="Some datasets are missing or excluded for training overlap. Compare the available slices with care.">Partial coverage</small>}
  </div>;
}

function SearchBox({ value, onChange, placeholder, label: accessibleLabel }: { value: string; onChange: (value: string) => void; placeholder: string; label: string }) {
  return <label className="decision-search"><Search size={14}/><input aria-label={accessibleLabel} value={value} onChange={event => onChange(event.target.value)} placeholder={placeholder}/></label>;
}

function DifficultyMap() {
  const [tier, setTier] = useState<DifficultyTier | "All">("All");
  const [query, setQuery] = useState("");
  const rows = [...DIFFICULTY].filter(row => (tier === "All" || row.tier === tier) && row.dataset.includes(query.toLowerCase().trim())).sort((a, b) => b.score - a.score);
  return <Card title="Dataset difficulty map" description="Higher scores mean more sensitive data was left exposed by the reference models.">
    <div className="difficulty-filters" role="group" aria-label="Filter datasets by difficulty">
      <button type="button" aria-pressed={tier === "All"} onClick={() => setTier("All")}>All levels</button>
      {tiers.map(item => <button type="button" key={item} className={`tier-${item.toLowerCase()}`} aria-pressed={tier === item} onClick={() => setTier(item)}><i/>{item}<span className="mono">{DIFFICULTY.filter(row => row.tier === item).length}</span></button>)}
    </div>
    <SearchBox value={query} onChange={setQuery} placeholder="Find a dataset…" label="Search difficulty datasets"/>
    <Scroll label="Dataset difficulty results" className="difficulty-scroll">
      <div className="difficulty-map">{rows.map(row => <Link href={`/datasets?dataset=${encodeURIComponent(row.dataset)}`} key={row.dataset} className={`difficulty-cell tier-${row.tier.toLowerCase()}`}>
        <span title={row.dataset}>{row.dataset}</span>
        <div><strong className="mono">{row.score.toFixed(1)}</strong><small>{row.tier}</small></div>
        <div className="difficulty-meter"><i style={{ width: `${row.score}%` }}/></div>
      </Link>)}</div>
      {!rows.length && <p className="decision-empty">No datasets match this search.</p>}
    </Scroll>
    <p className="decision-caption">Score = 100 − median Fully Hidden across a fixed reference panel. Levels follow the observed score distribution.</p>
  </Card>;
}

function Robustness({ rows }: { rows: RobustnessRow[] }) {
  const [query, setQuery] = useState("");
  const filtered = rows.filter(row => matchesModel(row, query));
  return <Card title="Robustness across difficulty" description="Every model, from easy inputs to the hardest cases. Fully Hidden %, higher is better.">
    <SearchBox value={query} onChange={setQuery} placeholder="Find any model or variant…" label="Search robustness models"/>
    <Scroll label="All model robustness results" className="robustness-scroll">
      <table className="robustness-table"><thead><tr><th scope="col">Model</th>{tiers.map(tier => <th scope="col" key={tier} className={`tier-${tier.toLowerCase()}`}><i className="difficulty-dot"/>{tier}</th>)}</tr></thead>
        <tbody>{filtered.map(row => <tr key={row.system}>
          <th scope="row"><ModelName system={row.system} name={row.name} complete={row.complete}/></th>
          {tiers.map(tier => <td key={tier} className={`tier-${tier.toLowerCase()}`} title={`${tier}: ${percent(row[tier])}; ${row.coverage[tier].gold.toLocaleString("en-US")} annotated spans`}>
            <span className="robustness-value" style={{ "--value": `${row[tier] ?? 0}%` } as CSSProperties}>{row[tier] === null ? "—" : row[tier].toFixed(1)}</span>
          </td>)}
        </tr>)}</tbody>
      </table>
      {!filtered.length && <p className="decision-empty">No models match this search.</p>}
    </Scroll>
    <p className="decision-caption">Average of dataset scores within each level. Full coverage first; training overlaps excluded. Scroll to explore every model.</p>
  </Card>;
}

function Protection({ data }: { data: Benchmark }) {
  const rows = useMemo(() => {
    const scores = aggregate(data, new Set(data.datasets.map(row => row.id)), "composition");
    return configurations.flatMap(config => {
      const score = scores.find(row => row.id === `composition:${config.id}`);
      return score ? [{ ...config, ...score, title: config.name, kind: config.kind }] : [];
    });
  }, [data]);
  return <Card title="Protection, side by side" description="Single models, CUDA stacks and the maximum measured combination on the same scale." tools={<Link className="decision-text-link" href="/ensembles">Explore stacks<ArrowRight size={14}/></Link>} className="protection-card">
    <Scroll label="Compare single model and stack protection" className="protection-scroll">
      <table className="protection-table"><thead><tr>
        <th scope="col">Configuration</th><th scope="col">Fully Hidden ↑<div className="protection-ruler mono"><span>0%</span><span>50%</span><span>100%</span></div></th><th scope="col">Extra masking ↓</th><th scope="col">Residual spans ↓</th>
      </tr></thead><tbody>{rows.map(row => <tr key={row.id} className={`protection-${row.kind}`}>
        <th scope="row"><span className="configuration-kind">{row.label}</span><strong>{row.title}</strong></th>
        <td><div className="protection-bar"><i style={{ width: `${row.fullyHidden ?? 0}%` }}/><b className="mono">{percent(row.fullyHidden)}</b></div></td>
        <td><div className="extra-bar"><i style={{ width: `${row.extra ?? 0}%` }}/><span className="mono">{percent(row.extra)}</span></div></td>
        <td className="mono protection-residual">{(row.gold - row.hidden).toLocaleString("en-US")}</td>
      </tr>)}</tbody></table>
    </Scroll>
    <div className="protection-foot"><div className="decision-legend"><span><i className="legend-solo"/>Single model</span><span><i className="legend-cuda"/>CUDA eligible</span><span><i className="legend-hybrid"/>CPU + GPU</span></div><p>Saved prediction unions. Extra masking measures annotated-negative text, not a false-positive rate.</p></div>
  </Card>;
}

function Domains({ rows }: { rows: DomainRow[] }) {
  const [query, setQuery] = useState("");
  const filtered = rows.filter(row => matchesModel(row, query));
  return <Card title="PII vs secrets" description="Find the right detector for personal data, credentials, or both.">
    <SearchBox value={query} onChange={setQuery} placeholder="Find any model or variant…" label="Search specialization models"/>
    <Scroll label="All model PII and secrets results" className="domain-scroll">
      <div className="domain-head"><span>Model</span><span>PII</span><span>Secrets</span></div>
      {filtered.map(row => <div className="domain-row" key={row.system}>
        <ModelName system={row.system} name={row.name} complete={row.complete}/>
        {(["pii", "secrets"] as const).map(domain => <div className={`domain-value domain-${domain}`} key={domain} title={`${domain === "pii" ? "PII" : "Secrets"}: ${percent(row[domain])}`}><i style={{ width: `${row[domain] ?? 0}%` }}/><span className="mono">{row[domain] === null ? "—" : row[domain].toFixed(1)}</span></div>)}
      </div>)}
      {!filtered.length && <p className="decision-empty">No models match this search.</p>}
    </Scroll>
    <p className="decision-caption">Fully Hidden, weighted by annotated spans in each task. Full coverage first.</p>
  </Card>;
}

function Rankings({ rows, className = "" }: { rows: SliceRow[]; className?: string }) {
  return <div className={`slice-rankings ${className}`}>{rows.map(row => <div className="slice-row" key={row.system}>
    <ModelName system={row.system} name={row.name} complete={row.complete}/>
    <div className="slice-score mono" title={`${row.coverage.gold.toLocaleString("en-US")} annotated spans`}>{percent(row.value, 1)}<div className="slice-track"><i style={{ width: `${row.value ?? 0}%` }}/></div></div>
  </div>)}</div>;
}

function Categories({ data, slices }: { data: Benchmark; slices: DecisionMetrics["categories"] }) {
  const [category, setCategory] = useState("overview");
  return <Card title="Category specialists" description="Explore the leaders, or choose a category to compare every model.">
    <div className="slice-controls"><select className="decision-select" aria-label="Choose specialization category" value={category} onChange={event => setCategory(event.target.value)}><option value="overview">Specialist overview</option>{data.categories.map(item => <option key={item.id} value={item.id}>{item.title}</option>)}</select><span>Fully Hidden ↑</span></div>
    <Scroll label="Category specialization results" className="category-scroll">
      {category === "overview" ? <div className="category-leaders">{CATEGORY_LEADERS.map(row => <div key={row.label}>
        <span>{row.label}</span><strong className="mono">{row.value.toFixed(1)}%</strong>
        <Link href={`/detectors/${detectorSlug(row.system)}`}>{label(row.system)}</Link><small>{row.gold.toLocaleString("en-US")} spans</small>
        <div className="category-meter"><i style={{ width: `${row.value}%` }}/></div>
      </div>)}</div> : <Rankings rows={slices[category] ?? []}/>}
    </Scroll>
    <p className="decision-caption">{category === "overview" ? "Overview uses the shared four-model finalist panel." : "All models, weighted by annotated spans. Full coverage first; training overlaps excluded."}</p>
  </Card>;
}

function Languages({ slices }: { slices: DecisionMetrics["languages"] }) {
  const [language, setLanguage] = useState("ru");
  const [query, setQuery] = useState("");
  const rows = (slices[language] ?? []).filter(row => matchesModel(row, query));
  return <Card title="Language performance" description="Compare every model in Russian, English and multilingual inputs." className="language-card" tools={<select className="decision-select" aria-label="Choose language performance slice" value={language} onChange={event => setLanguage(event.target.value)}><option value="ru">Russian</option><option value="en">English</option><option value="multi">Multilingual</option></select>}>
    <SearchBox value={query} onChange={setQuery} placeholder="Find any model or variant…" label="Search language models"/>
    <Scroll label="All model language results" className="language-scroll"><Rankings rows={rows} className="language-rankings"/>{!rows.length && <p className="decision-empty">No models match this search.</p>}</Scroll>
    <p className="decision-caption">Fully Hidden, weighted by annotated spans in the selected language. Full coverage first; training overlaps excluded.</p>
  </Card>;
}

function Gain() {
  return <Card title="What each model adds" description="Follow one saved combination from a single detector to maximum protection.">
    <Scroll label="Incremental protection from each model" className="gain-scroll"><ol className="gain-list">
      {STACK_GAIN.map((row, index) => <li key={row.models.join("+")}>
        <span className="gain-step mono">{index + 1}</span><div className="gain-content"><div><strong>{index ? "+ " : ""}{row.models.at(-1)}</strong><b className="mono">{percent(row.fully_hidden_pct)}</b></div>
          <div className="gain-track"><i style={{ width: `${row.fully_hidden_pct}%` }}/></div>
          <p>{index ? <><span className="gain-improvement mono">+{(row.fully_hidden_pct - STACK_GAIN[index - 1].fully_hidden_pct).toFixed(2)} pp</span><span>{row.incremental_hidden?.toLocaleString("en-US")} more spans fully hidden</span></> : <span>Single detector reference</span>}<small>{percent(row.extra_masking_pct)} extra masking</small></p>
        </div>
      </li>)}
    </ol></Scroll>
    <p className="decision-caption">Models run on the original text and their masks are combined. This is not a measured sequence of re-masked inputs.</p>
  </Card>;
}

function Hardware() {
  const icons = { cpu: Cpu, cuda: Gauge, hybrid: Layers3 };
  return <Card title="Choose your hardware" description="Start with the measured quality evidence, then validate the complete runtime.">
    <Scroll label="CPU and NVIDIA hardware recommendations" className="hardware-scroll"><div className="hardware-choice-grid">
      {HARDWARE.map(item => {
        const Icon = icons[item.id as keyof typeof icons] ?? Cpu;
        return <article key={item.id} className="hardware-choice">
          <div className="hardware-choice-title"><Icon size={16}/><h4>{item.label}</h4><span>{item.status}</span></div>
          <strong>{item.name}</strong><p>{item.note}</p>
        </article>;
      })}
    </div></Scroll>
  </Card>;
}

export function DecisionDashboard({ data }: { data: Benchmark }) {
  const metrics = useMemo(() => buildDecisionMetrics(data), [data]);
  return <div className="decision-dashboard">
    <nav className="decision-jump-links" aria-label="Leaderboard analysis sections">
      <a href="#dataset-difficulty">Dataset difficulty</a><a href="#protection-comparison">Protection</a><a href="#model-specialization">Specialization</a><a href="#stacks-hardware">Stacks & hardware</a><a href="#detector-results">Detector table<ArrowDown size={12}/></a>
    </nav>
    <SectionTitle id="dataset-difficulty" number="01" title="Start with the data">Understand the hard cases, then see how each model holds up.</SectionTitle>
    <div className="decision-grid difficulty-grid"><DifficultyMap/><Robustness rows={metrics.robustness}/></div>
    <SectionTitle id="protection-comparison" number="02" title="One model or a stack?">Compare the protection gained and the extra text masked.</SectionTitle>
    <Protection data={data}/>
    <SectionTitle id="model-specialization" number="03" title="Match the model to the task">Explore personal data, secrets and the categories that matter to your application.</SectionTitle>
    <div className="decision-grid specialization-grid"><Domains rows={metrics.domains}/><Categories data={data} slices={metrics.categories}/><Languages slices={metrics.languages}/></div>
    <SectionTitle id="stacks-hardware" number="04" title="Build a practical stack">See which additions pay off and where each configuration can run.</SectionTitle>
    <div className="decision-grid stacks-grid"><Gain/><Hardware/></div>
    <div id="detector-results" className="decision-table-anchor"/>
  </div>;
}
