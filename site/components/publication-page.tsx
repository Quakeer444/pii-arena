import type { CSSProperties, ReactNode } from "react";
import { SidebarProvider } from "@/components/ui/sidebar";
import { SiteNav, SiteTopbar } from "@/components/site-nav";
import { GITHUB_URL } from "@/lib/seo";

export function PublicationPage({
  view,
  eyebrow,
  title,
  description,
  children
}: {
  view?: string;
  eyebrow: string;
  title: string;
  description: string;
  children: ReactNode;
}) {
  return (
    <SidebarProvider style={{ "--sidebar-width": "212px" } as CSSProperties}>
      <SiteNav view={view} />
      <main className="workspace">
        <SiteTopbar view={view} fallback={title} />
        <div className="page-content">
          <div className="publication-title">
            <span>{eyebrow}</span>
            <h1>{title}</h1>
            <p>{description}</p>
          </div>
          {children}
          <footer className="page-footer">
            <span>PII Arena · Frozen 09 Sep 2026</span>
            <a href={GITHUB_URL}>Source and reproduction</a>
          </footer>
        </div>
      </main>
    </SidebarProvider>
  );
}
