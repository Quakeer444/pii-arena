"use client";

import { useState } from "react";
import { colorFor, n, percent, type Score } from "@/lib/benchmark";

export function MaskBars({ rows, onSelect }: { rows: Score[]; onSelect: (id: string) => void }) {
  return (
    <div className="mask-bars">
      {rows.slice(0, 7).map((row, index) => (
        <button
          className="mask-bar-row"
          key={row.id}
          onClick={() => onSelect(row.id)}
          title={`${row.name}: ${n(row.hidden)} / ${n(row.gold)} fully hidden; ${n(row.missed)} untouched`}
        >
          <span className="bar-name"><span className="chart-rank mono">{String(index + 1).padStart(2, "0")}</span>{row.name}</span>
          <span className="bar-track">
            <span className="bar-hidden" style={{ width: `${row.fullyHidden ?? 0}%` }} />
            <span className="bar-partial" style={{ width: `${Math.max(0, (row.detected ?? 0) - (row.fullyHidden ?? 0))}%` }} />
          </span>
          <span className="bar-value mono">{percent(row.fullyHidden, 1)}</span>
        </button>
      ))}
      {!rows.length && <p className="empty">No comparable measurements in this slice.</p>}
      <div className="legend">
        <span><i className="hidden-key" />Fully hidden</span>
        <span><i className="partial-key" />Partially hidden</span>
        <span><i className="untouched-key" />Untouched</span>
      </div>
    </div>
  );
}

export function Tradeoff({ rows, onSelect }: { rows: Score[]; onSelect: (id: string) => void }) {
  const [hover, setHover] = useState<Score | null>(null);
  const points = rows.filter((row) => row.extra !== null && row.fullyHidden !== null);
  const maxX = Math.max(10, Math.ceil(Math.max(...points.map((row) => row.extra ?? 0), 0) / 10) * 10);
  const width = 500;
  const height = 237;
  const left = 47;
  const right = 22;
  const top = 14;
  const bottom = 40;
  const x = (value: number) => left + value / maxX * (width - left - right);
  const y = (value: number) => height - bottom - value / 100 * (height - bottom - top);

  return (
    <div className="scatter-wrap">
      <svg
        role="group"
        aria-label="Scatter plot: full hiding versus characters masked in unannotated rows"
        viewBox={`0 0 ${width} ${height}`}
        className="scatter"
      >
        {[0, 25, 50, 75, 100].map((value) => (
          <g key={value}>
            <line x1={left} x2={width - right} y1={y(value)} y2={y(value)} stroke="var(--border)" strokeDasharray="3 5" />
            <text x={left - 9} y={y(value) + 4} textAnchor="end" fill="var(--muted-foreground)" fontSize="12">{value}%</text>
          </g>
        ))}
        {[0, 1, 2, 3, 4].map((index) => (
          <text
            key={index}
            x={x(maxX * index / 4)}
            y={height - bottom + 22}
            textAnchor="middle"
            fill="var(--muted-foreground)"
            fontSize="12"
          >
            {maxX * index / 4}%
          </text>
        ))}
        {points.map((row) => (
          <circle
            key={row.id}
            cx={x(row.extra!)}
            cy={y(row.fullyHidden!)}
            r={hover?.id === row.id ? 7 : 5}
            fill={colorFor(row.family)}
            fillOpacity={hover && hover.id !== row.id ? 0.45 : 0.86}
            stroke="var(--card)"
            strokeWidth="1.5"
            tabIndex={0}
            role="button"
            aria-label={`${row.name}: ${percent(row.fullyHidden)} fully hidden, ${percent(row.extra)} extra masking`}
            onMouseEnter={() => setHover(row)}
            onMouseLeave={() => setHover(null)}
            onFocus={() => setHover(row)}
            onBlur={() => setHover(null)}
            onClick={() => onSelect(row.id)}
            onKeyDown={(event) => {
              if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                onSelect(row.id);
              }
            }}
          >
            <title>{row.name}</title>
          </circle>
        ))}
      </svg>
      {hover && (
        <div className="chart-tooltip">
          <strong>{hover.name}</strong>
          <span>Fully hidden <b>{percent(hover.fullyHidden)}</b></span>
          <span>Extra masking <b>{percent(hover.extra)}</b></span>
        </div>
      )}
      <p className="axis-caption">Characters masked in unannotated rows →</p>
    </div>
  );
}
