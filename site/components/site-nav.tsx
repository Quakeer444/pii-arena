"use client";
import Link from "next/link";
import { ChevronRight } from "lucide-react";
import {
  Sidebar,
  SidebarHeader,
  SidebarContent,
  SidebarGroup,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuItem,
  SidebarMenuButton,
  SidebarTrigger,
  useSidebar,
} from "@/components/ui/sidebar";
import { ThemeToggle } from "@/components/theme-toggle";
import { GITHUB_URL } from "@/lib/seo";

export const nav = [
  { id: "leaderboard", label: "Leaderboard" },
  { id: "compare", label: "Compare detectors" },
  { id: "ensembles", label: "Ensembles" },
  { id: "entities", label: "Data types" },
  { id: "datasets", label: "Datasets" },
  { id: "performance", label: "Performance" },
  { id: "methodology", label: "Methodology" },
  { id: "downloads", label: "Reports & data" },
];
const resources = [
  { id: "detectors", label: "Detector index", href: "/detectors" },
  { id: "results", label: "September release", href: "/results/2026-09" },
];

export function SiteNav({ view, search = "" }: { view?: string; search?: string }) {
  const { setOpenMobile } = useSidebar();
  const item = (id: string, label: string, href: string) => (
    <SidebarMenuItem key={id}>
      <SidebarMenuButton asChild className="nav-button" isActive={view === id}>
        <Link href={href} prefetch={false} onClick={() => setOpenMobile(false)}>
          <span>{label}</span>
        </Link>
      </SidebarMenuButton>
    </SidebarMenuItem>
  );
  return (
    <Sidebar role="navigation" aria-label="Primary">
      <SidebarHeader className="brand">
        <Link
          href={`/leaderboard${search}`}
          prefetch={false}
          onClick={() => setOpenMobile(false)}
          className="brand-link"
        >
          PII <span className="brand-light">Arena</span>
          <small>PII & secret detector benchmark</small>
        </Link>
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Explore</SidebarGroupLabel>
          <SidebarMenu>
            {nav.slice(0, 6).map((v) => item(v.id, v.label, `/${v.id}${search}`))}
          </SidebarMenu>
        </SidebarGroup>
        <SidebarGroup>
          <SidebarGroupLabel>Resources</SidebarGroupLabel>
          <SidebarMenu>
            {nav.slice(6).map((v) => item(v.id, v.label, `/${v.id}${search}`))}
            {resources.map((v) => item(v.id, v.label, v.href))}
          </SidebarMenu>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  );
}

export function SiteTopbar({ view, fallback = "Benchmark" }: { view?: string; fallback?: string }) {
  const label = [...nav, ...resources].find((v) => v.id === view)?.label ?? fallback;
  return (
    <header className="topbar">
      <div className="breadcrumb">
        <SidebarTrigger className="mobile-trigger" />
        <span>PII Arena</span>
        <ChevronRight size={14} />
        <strong>{label}</strong>
      </div>
      <div className="topbar-right">
        <span className="revision">
          Results updated <strong>19 Sep 2026</strong>
        </span>
        <a
          className="icon-button"
          href={GITHUB_URL}
          target="_blank"
          rel="noreferrer"
          aria-label="Open GitHub repository"
          title="Open GitHub repository"
        >
          <GithubMark />
        </a>
        <ThemeToggle />
      </div>
    </header>
  );
}

function GithubMark() {
  return (
    <svg
      aria-hidden="true"
      viewBox="0 0 16 16"
      width="17"
      height="17"
      fill="currentColor"
    >
      <path d="M8 0C3.58 0 0 3.64 0 8.13c0 3.59 2.29 6.64 5.47 7.71.4.08.55-.18.55-.39 0-.19-.01-.83-.01-1.5-2.01.38-2.53-.5-2.69-.96-.09-.23-.48-.96-.82-1.15-.28-.15-.68-.53-.01-.54.63-.01 1.08.59 1.23.83.72 1.23 1.87.88 2.33.67.07-.53.28-.88.51-1.08-1.78-.2-3.64-.9-3.64-4.01 0-.89.31-1.62.82-2.19-.08-.2-.36-1.04.08-2.16 0 0 .67-.22 2.2.84A7.5 7.5 0 0 1 8 3.93a7.5 7.5 0 0 1 2 .27c1.53-1.06 2.2-.84 2.2-.84.44 1.12.16 1.96.08 2.16.51.57.82 1.3.82 2.19 0 3.12-1.87 3.81-3.65 4.01.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.47.55.39A8.14 8.14 0 0 0 16 8.13C16 3.64 12.42 0 8 0Z" />
    </svg>
  );
}
