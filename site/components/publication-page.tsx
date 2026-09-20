import Link from "next/link";
import type { ReactNode } from "react";
import { ThemeToggle } from "@/components/theme-toggle";

export function PublicationPage({
  eyebrow,
  title,
  description,
  children
}: {
  eyebrow: string;
  title: string;
  description: string;
  children: ReactNode;
}) {
  return (
    <div className="publication-shell">
      <header className="publication-header">
        <Link href="/leaderboard" className="publication-brand">PII<span>Bench</span></Link>
        <nav aria-label="Primary">
          <Link href="/leaderboard">Leaderboard</Link>
          <Link href="/detectors">Detectors</Link>
          <Link href="/datasets">Datasets</Link>
          <Link href="/methodology">Methodology</Link>
        </nav>
        <ThemeToggle />
      </header>
      <main className="publication-main">
        <div className="publication-title">
          <span>{eyebrow}</span>
          <h1>{title}</h1>
          <p>{description}</p>
        </div>
        {children}
      </main>
      <footer className="publication-footer">
        <span>Frozen experiment · 09 September 2026</span>
        <a href="https://github.com/Quakeer444/pii-secrets-benchmark">Source and reproduction</a>
      </footer>
    </div>
  );
}
