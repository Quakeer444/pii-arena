"use client";

import Link from "next/link";
import { Cpu, Database, Gauge, Laptop, Layers3, ShieldCheck } from "lucide-react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
  CATEGORY_LEADERS,
  DIFFICULTY,
  DOMAINS,
  HARDWARE,
  LANGUAGES,
  MODEL_LABELS,
  PARETO,
  RECOMMENDATIONS,
  ROBUSTNESS,
  STACK_GAIN,
} from "@/lib/decision-data";

const tierOrder = ["Easy", "Medium", "Hard", "Extreme"] as const;

function metric(value:number) {
  return `${value.toFixed(2)}%`;
}

function ShortModel({ id }:{ id:string }) {
  return <>{MODEL_LABELS[id] ?? id.replace("model:", "")}</>;
}

function DecisionCard({ item }:{ item:(typeof RECOMMENDATIONS)[number] }) {
  return <article className="decision-card">
    <div className="decision-card-top">
      <span>{item.eyebrow}</span>
      <span className="evidence-pill">Measured</span>
    </div>
    <h3>{item.name}</h3>
    <div className="decision-value mono">{item.value}<small>{item.metric}</small></div>
    <p>{item.note}</p>
    <footer>{item.evidence}</footer>
  </article>;
}

function HardwareView() {
  const icons = [Cpu, Gauge, Laptop];
  return <section className="decision-view">
    <div className="decision-view-head"><div><span>01</span><h3>Hardware decision</h3></div><p>Only claim a stack where the frozen results support it.</p></div>
    <div className="hardware-choice-grid">
      {HARDWARE.map((item, index) => {
        const Icon = icons[index];
        return <article key={item.id} className="hardware-choice">
          <div className="hardware-choice-title"><Icon size={17}/><span>{item.label}</span><b>{item.status}</b></div>
          <strong>{item.name}</strong>
          <div className="hardware-choice-value mono">{item.value}</div>
          <p>{item.note}</p>
        </article>;
      })}
    </div>
  </section>;
}

function GainView() {
  return <section className="decision-view">
    <div className="decision-view-head"><div><span>02</span><h3>Ensemble gain curve</h3></div><p>Each bar adds one measured component; diminishing returns are explicit.</p></div>
    <div className="gain-list">
      {STACK_GAIN.map((row, index) => <div className="gain-row" key={row.models.join("+")}>
        <div className="gain-label"><span className="mono">{index + 1}</span><b>{row.models.at(-1)}</b><small>{index ? `+${row.incremental_hidden?.toLocaleString("en-US")} newly hidden` : "solo baseline"}</small></div>
        <div className="gain-track"><i style={{width:`${row.fully_hidden_pct}%`}}/></div>
        <strong className="mono">{metric(row.fully_hidden_pct)}</strong>
        <small className="gain-cost mono">{metric(row.extra_masking_pct)} extra</small>
      </div>)}
    </div>
  </section>;
}

function ParetoView() {
  return <section className="decision-view">
    <div className="decision-view-head"><div><span>03</span><h3>Protection / masking Pareto</h3></div><p>Higher protection and less extra masking are preferred. Hollow points are dominated.</p></div>
    <div className="pareto-chart" aria-label="Protection versus extra masking Pareto chart">
      <span className="pareto-axis-y">Fully Hidden ↑</span>
      <div className="pareto-plot">
        {PARETO.map(row => {
          const left = Math.max(2, Math.min(96, row.extra_masking_pct / 22 * 100));
          const bottom = Math.max(4, Math.min(94, (row.fully_hidden_pct - 70) / 27 * 100));
          return <div key={row.abbr} className={`pareto-point ${row.pareto ? "is-pareto" : ""}`} style={{left:`${left}%`,bottom:`${bottom}%`}} title={`${row.label}: ${metric(row.fully_hidden_pct)} hidden, ${metric(row.extra_masking_pct)} extra`}>
            <i/><span>{row.abbr}</span>
          </div>;
        })}
      </div>
      <span className="pareto-axis-x">Extra masking →</span>
    </div>
  </section>;
}

function DifficultyDistribution() {
  const totalGold = DIFFICULTY.reduce((sum,row)=>sum+row.gold,0);
  return <section className="decision-view">
    <div className="decision-view-head"><div><span>04</span><h3>Difficulty distribution</h3></div><p>Natural-break tiers over an observed difficulty score, not hand-picked thresholds.</p></div>
    <div className="difficulty-distribution">
      {tierOrder.map(tier => {
        const rows = DIFFICULTY.filter(row=>row.tier===tier);
        const gold = rows.reduce((sum,row)=>sum+row.gold,0);
        return <div key={tier}><span className={`difficulty-dot tier-${tier.toLowerCase()}`}/><b>{tier}</b><strong className="mono">{rows.length}</strong><small>{(100*gold/totalGold).toFixed(1)}% of gold spans</small></div>;
      })}
    </div>
  </section>;
}

function DifficultyMap() {
  return <section className="decision-view">
    <div className="decision-view-head"><div><span>05</span><h3>Dataset difficulty map</h3></div><p>Score = 100 − median Fully Hidden across the fixed seven-model reference panel.</p></div>
    <div className="difficulty-map">
      {[...DIFFICULTY].sort((a,b)=>b.score-a.score).map(row => <Link href={`/datasets?dataset=${encodeURIComponent(row.dataset)}`} key={row.dataset} className={`difficulty-cell tier-${row.tier.toLowerCase()}`}>
        <span>{row.dataset}</span><strong className="mono">{row.score.toFixed(1)}</strong><small>{row.tier}</small>
      </Link>)}
    </div>
  </section>;
}

function RobustnessView() {
  return <section className="decision-view">
    <div className="decision-view-head"><div><span>06</span><h3>Robustness across difficulty</h3></div><p>How much Fully Hidden survives from Easy to Extreme.</p></div>
    <div className="robustness-table">
      <div className="robustness-head"><span>Detector</span>{tierOrder.map(t=><span key={t}>{t}</span>)}</div>
      {ROBUSTNESS.map(row => <div className="robustness-row" key={row.system}>
        <b><ShortModel id={row.system}/></b>
        {tierOrder.map(tier => {
          const value = row[tier];
          return <span key={tier}><i style={{width:`${value}%`}}/><em className="mono">{value.toFixed(1)}</em></span>;
        })}
      </div>)}
    </div>
  </section>;
}

function DomainView() {
  return <section className="decision-view">
    <div className="decision-view-head"><div><span>07</span><h3>PII vs secrets</h3></div><p>Same finalist panel, split by task. PPLX is visibly secret-specialized.</p></div>
    <div className="domain-bars">
      {DOMAINS.map(row => <div key={row.system}>
        <b><ShortModel id={row.system}/></b>
        <span><small>PII</small><i style={{width:`${row.pii}%`}}/><em className="mono">{row.pii.toFixed(1)}</em></span>
        <span><small>Secrets</small><i style={{width:`${row.secrets}%`}}/><em className="mono">{row.secrets.toFixed(1)}</em></span>
      </div>)}
    </div>
  </section>;
}

function CategoryView() {
  return <section className="decision-view">
    <div className="decision-view-head"><div><span>08</span><h3>Category specialization</h3></div><p>Descriptive leader among the four fixed finalists; gold support is always shown.</p></div>
    <div className="category-leaders">
      {CATEGORY_LEADERS.map(row => <div key={row.label}>
        <span>{row.label}</span><b><ShortModel id={row.system}/></b><strong className="mono">{row.value.toFixed(1)}%</strong><small className="mono">{row.gold.toLocaleString("en-US")} spans</small>
      </div>)}
    </div>
  </section>;
}

function LanguageView() {
  return <section className="decision-view">
    <div className="decision-view-head"><div><span>09</span><h3>Language slices</h3></div><p>Leader in the shared three-finalist comparison panel.</p></div>
    <div className="language-leaders">
      {LANGUAGES.map(row => <article key={row.language}><span>{row.language}</span><b><ShortModel id={row.system}/></b><strong className="mono">{row.fully_hidden_pct.toFixed(2)}%</strong><small>{row.datasets} datasets · {row.gold.toLocaleString("en-US")} gold</small></article>)}
    </div>
  </section>;
}

export function DecisionDashboard() {
  return <div className="decision-dashboard">
    <div className="decision-intro">
      <div><span>Deployment decision map</span><h2>Choose by protection target, hardware and data type</h2><p>Fully Hidden is the safety-oriented metric. Detection alone can leave part of a sensitive value visible.</p></div>
      <Link className="action" href="/ensembles"><Layers3 size={15}/>Protection stacks</Link>
    </div>
    <div className="decision-cards">{RECOMMENDATIONS.map(item=><DecisionCard key={item.eyebrow} item={item}/>)}</div>
    <Tabs defaultValue="stacks" className="decision-tabs">
      <TabsList>
        <TabsTrigger value="stacks"><ShieldCheck size={14}/>Stacks & hardware</TabsTrigger>
        <TabsTrigger value="difficulty"><Database size={14}/>Dataset difficulty</TabsTrigger>
        <TabsTrigger value="specialization"><Gauge size={14}/>Model specialization</TabsTrigger>
      </TabsList>
      <TabsContent value="stacks"><div className="decision-grid"><HardwareView/><GainView/><ParetoView/></div></TabsContent>
      <TabsContent value="difficulty"><div className="decision-grid"><DifficultyDistribution/><DifficultyMap/><RobustnessView/></div></TabsContent>
      <TabsContent value="specialization"><div className="decision-grid"><DomainView/><CategoryView/><LanguageView/></div></TabsContent>
    </Tabs>
    <div className="decision-note"><ShieldCheck size={15}/><p>Measured claims come from the frozen benchmark. CPU stack ranking and Apple MPS remain explicitly unclaimed until a shared end-to-end benchmark exists. Extra masking on unannotated rows is not a false-positive rate.</p></div>
  </div>;
}
