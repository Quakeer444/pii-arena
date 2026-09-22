"use client";
import {
  useCallback,
  useEffect,
  useMemo,
  useState,
  ReactNode,
  CSSProperties,
} from "react";
import { flushSync } from "react-dom";
import Link from "next/link";
import Image from "next/image";
import { useRouter } from "next/navigation";
import {
  ArrowDown,
  ArrowDownUp,
  ArrowRight,
  ArrowUpRight,
  BookOpen,
  Braces,
  CircleHelp,
  Columns3,
  Copy,
  Database,
  Download,
  ExternalLink,
  FileJson,
  Files,
  Gauge,
  Globe2,
  Layers3,
  Search,
  ShieldCheck,
  SlidersHorizontal,
  Table2,
  X,
} from "lucide-react";
import { SidebarProvider } from "@/components/ui/sidebar";
import {
  Select,
  SelectTrigger,
  SelectValue,
  SelectContent,
  SelectItem,
} from "@/components/ui/select";
import { Checkbox } from "@/components/ui/checkbox";
import {
  Table,
  TableHeader,
  TableBody,
  TableRow,
  TableCell,
  TableHead,
} from "@/components/ui/table";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetDescription,
} from "@/components/ui/sheet";
import {
  Tooltip,
  TooltipTrigger,
  TooltipContent,
  TooltipProvider,
} from "@/components/ui/tooltip";
import { Toaster } from "@/components/ui/sonner";
import { toast } from "sonner";
import {
  Benchmark,
  Score,
  adapterNote,
  aggregate,
  categoryScores,
  compareExportContext,
  compareScores,
  n,
  percent,
  ratio,
  REF,
  colors,
  detectorSlug,
  download,
  exportCsv,
  sourceUrls,
} from "@/lib/benchmark";
import {
  MaskBars,
  SpeedQuality,
  Tradeoff,
} from "@/components/benchmark-charts";
import { EvidenceViewer } from "@/components/evidence-viewer";
import { nav, SiteNav, SiteTopbar } from "@/components/site-nav";
import {
  DecisionDashboard,
  type DecisionDashboardState,
} from "@/components/decision-dashboard";
import { difficultyFor } from "@/lib/decision-data";
import { readExplorerSearch, writeExplorerSearch } from "@/lib/explorer-url";

const descriptions: Record<string, string> = {
  leaderboard:
    "Find which detector best hides the sensitive data you care about.",
  compare: "Compare on the same datasets, with the same denominator.",
  ensembles: "Explore the masking tradeoffs of fixed detector compositions.",
  entities: "Look beyond pooled averages. See which data types remain visible.",
  datasets: "Every retained source, its composition, provenance and results.",
  performance:
    "Measured batch throughput, with the hardware and workload in view.",
  methodology:
    "A transparent scoring contract. Every number has a denominator.",
  downloads:
    "Original reports, publication figures and machine-readable results.",
};
const help: Record<string, string> = {
  untouched:
    "Sensitive items with no detector overlap. Lower is better. This is not a production leak rate.",
  fullyHidden:
    "Sensitive items whose whole normalized value is covered by the mask. This is the main ranking metric.",
  detected:
    "Sensitive items with any detector overlap. Part of the value may still remain visible.",
  extra:
    "Text masked in rows with no labels. These rows were not manually verified clean, so this is not a false-positive rate.",
  f1: "Character-level balance of precision and recall. It measures masked characters, not entity types.",
  cpu: "Seconds per 10,000 characters from a saved CPU reference measurement. Dataset workloads differ by detector, so this is not a strict same-input speedup or request latency.",
  gpu: "Seconds per 10,000 characters from a saved GPU reference measurement. Dataset workloads differ by detector, so this is not a strict same-input speedup or request latency.",
};
function AdapterStatus({
  score,
  inventory = false,
}: {
  score: Score;
  inventory?: boolean;
}) {
  const note = adapterNote(score);
  if (!note) return null;
  return (
    <p className="adapter-status">
      <span>{note.slice || "No scanner runs in this slice"}</span>
      {inventory && note.inventory && (
        <span>
          Full inventory: {note.inventory}. These counts cover every stored
          run, including runs left out of this slice.
        </span>
      )}
    </p>
  );
}
function Pick({
  value,
  onChange,
  items,
  label,
  className = "",
}: {
  value: string;
  onChange: (v: string) => void;
  items: { value: string; label: string }[];
  label: string;
  className?: string;
}) {
  return (
    <Select value={value} onValueChange={onChange}>
      <SelectTrigger aria-label={label} className={`pick ${className}`}>
        {/* Explicit text keeps the value visible before hydration. */}
        <SelectValue>
          {items.find((i) => i.value === value)?.label}
        </SelectValue>
      </SelectTrigger>
      <SelectContent position="popper">
        {items.map((i) => (
          <SelectItem key={i.value} value={i.value}>
            {i.label}
          </SelectItem>
        ))}
      </SelectContent>
    </Select>
  );
}
function Segmented({
  value,
  onChange,
  items,
  label,
}: {
  value: string;
  onChange: (v: string) => void;
  items: { value: string; label: string }[];
  label: string;
}) {
  return (
    <div className="view-tabs" role="group" aria-label={label}>
      {items.map((item) => (
        <button
          type="button"
          key={item.value}
          aria-pressed={value === item.value}
          onClick={() => onChange(item.value)}
        >
          {item.label}
        </button>
      ))}
    </div>
  );
}
function Hint({ name }: { name: string }) {
  return (
    <Tooltip>
      <TooltipTrigger asChild>
        <button className="hint" aria-label={`About ${name}`}>
          <CircleHelp size={14} />
        </button>
      </TooltipTrigger>
      <TooltipContent className="max-w-80 leading-relaxed">
        {help[name] ?? name}
      </TooltipContent>
    </Tooltip>
  );
}
function DatasetSource({ source }: { source: string }) {
  const urls = sourceUrls(source);
  return urls.length ? (
    <span className="dataset-source-links">
      {urls.map((url, index) => (
        <a href={url} target="_blank" rel="noreferrer" key={url}>
          {urls.length > 1
            ? url.split("/").filter(Boolean).at(-1)
            : "Original source"}
          <ExternalLink size={12} />
          {index < urls.length - 1 && <span>+</span>}
        </a>
      ))}
    </span>
  ) : (
    <span>Generated in this project</span>
  );
}
function Panel({
  title,
  subtitle,
  children,
  action,
  className = "",
}: {
  title: string;
  subtitle?: string;
  children: ReactNode;
  action?: ReactNode;
  className?: string;
}) {
  return (
    <section className={`panel ${className}`}>
      <div className="panel-heading">
        <div>
          <h2>{title}</h2>
          {subtitle && <p>{subtitle}</p>}
        </div>
        {action}
      </div>
      {children}
    </section>
  );
}

export function BenchmarkExplorer({
  data,
  initialView = "leaderboard",
  initialTask = "all",
  titleOverride,
  descriptionOverride,
}: {
  data: Benchmark;
  initialView?: string;
  initialTask?: string;
  titleOverride?: string;
  descriptionOverride?: string;
}) {
  const router = useRouter();
  const [view, setView] = useState(initialView),
    [language, setLanguage] = useState("all"),
    [task, setTask] = useState(initialTask),
    [dataset, setDataset] = useState("all"),
    [sensitivity, setSensitivity] = useState(false),
    [query, setQuery] = useState(""),
    [family, setFamily] = useState("all"),
    [coverage, setCoverage] = useState("complete"),
    [sort, setSort] = useState("fullyHidden"),
    [ascending, setAscending] = useState(false),
    [selected, setSelected] = useState<string[]>([]),
    [detail, setDetail] = useState<string | null>(null),
    [report, setReport] = useState<string | null>(null),
    [notice, setNotice] = useState(""),
    [urlReady, setUrlReady] = useState(false);
  const [entitySystem, setEntitySystem] = useState(REF),
    [datasetQuery, setDatasetQuery] = useState(""),
    [device, setDevice] = useState("cpu"),
    [speedGroup, setSpeedGroup] = useState("reference"),
    [includeHistorical, setIncludeHistorical] = useState(false),
    [sourceFiles, setSourceFiles] = useState<{ path: string; bytes: number }[]>(
      [],
    );
  const [dashboard, setDashboard] = useState<DecisionDashboardState>({
    difficultyTier: "All",
    difficultyQuery: "",
    robustnessQuery: "",
    domainQuery: "",
    category: "overview",
  });
  useEffect(() => {
    setView(initialView);
  }, [initialView]);
  useEffect(() => {
    const apply = () => {
      const next = readExplorerSearch(
        window.location.search,
        initialTask,
        data.systems,
        data.datasets.map((item) => item.id),
        data.categories.map((item) => item.id),
      );
      setLanguage(next.language);
      setTask(next.task);
      setDataset(next.dataset);
      setSensitivity(next.sensitivity);
      setQuery(next.query);
      setFamily(next.family);
      setCoverage(next.coverage);
      setSort(next.sort);
      setAscending(next.ascending);
      setSelected(next.selected);
      setEntitySystem(next.entitySystem);
      setDatasetQuery(next.datasetQuery);
      setDevice(next.device);
      setSpeedGroup(next.speedGroup);
      setIncludeHistorical(next.includeHistorical);
      setDashboard(next.dashboard);
      setUrlReady(true);
    };
    apply();
    window.addEventListener("popstate", apply);
    return () => window.removeEventListener("popstate", apply);
  }, [data.systems, data.datasets, data.categories, initialTask]);
  const urlSearch = useMemo(
    () =>
      writeExplorerSearch({
        language,
        task,
        dataset,
        sensitivity,
        query,
        family,
        coverage,
        sort,
        ascending,
        selected,
        entitySystem,
        datasetQuery,
        device,
        speedGroup,
        includeHistorical,
        dashboard,
      }),
    [
      language,
      task,
      dataset,
      sensitivity,
      query,
      family,
      coverage,
      sort,
      ascending,
      selected,
      entitySystem,
      datasetQuery,
      device,
      speedGroup,
      includeHistorical,
      dashboard,
    ],
  );
  const searchSuffix = urlSearch ? `?${urlSearch}` : "";
  const navigate = useCallback(
    (nextView: string) => {
      setView(nextView);
      router.push(`/${nextView}${searchSuffix}`);
      window.scrollTo({ top: 0, behavior: "instant" });
    },
    [router, searchSuffix],
  );
  useEffect(() => {
    if (!urlReady) return;
    window.history.replaceState(
      null,
      "",
      `${window.location.pathname}${searchSuffix}${window.location.hash}`,
    );
  }, [urlReady, searchSuffix]);
  useEffect(() => {
    if (view !== "downloads") return;
    fetch("/data/files.json")
      .then((r) => (r.ok ? r.json() : []))
      .then((value) =>
        setSourceFiles(
          Array.isArray(value)
            ? (value as { path: string; bytes: number }[])
            : [],
        ),
      )
      .catch(() => setSourceFiles([]));
  }, [view]);
  useEffect(() => {
    if (!notice) return;
    toast(notice);
    setNotice("");
  }, [notice]);
  const activeDatasets = useMemo(
    () =>
      data.datasets.filter(
        (d) =>
          (language === "all" || d.lang === language) &&
          (task === "all" || d.kind === task) &&
          (dataset === "all" || d.id === dataset) &&
          (!sensitivity ||
            !data.sensitivity.excluded_dataset_ids.includes(d.id)),
      ),
    [data, language, task, dataset, sensitivity],
  );
  const ids = useMemo(
    () => new Set(activeDatasets.map((d) => d.id)),
    [activeDatasets],
  );
  // Leaderboard filters scope only the table; the dashboard keeps the page's own task.
  const baseDatasets = useMemo(
    () =>
      data.datasets.filter(
        (d) => initialTask === "all" || d.kind === initialTask,
      ),
    [data, initialTask],
  );
  const baseIds = useMemo(
    () => new Set(baseDatasets.map((d) => d.id)),
    [baseDatasets],
  );
  const scores = useMemo(() => aggregate(data, ids), [data, ids]);
  const rows = useMemo(
    () =>
      scores
        .filter(
          (r) =>
            (coverage !== "complete" || r.sets === ids.size) &&
            (family === "all" || r.family === family) &&
            r.name.toLowerCase().includes(query.toLowerCase()),
        )
        .sort((a, b) => compareScores(a, b, sort as keyof Score, ascending)),
    [scores, coverage, ids, family, query, sort, ascending],
  );
  const ensembles = useMemo(
    () => aggregate(data, ids, "composition"),
    [data, ids],
  );
  const scope = {
    view: "leaderboard",
    rowOrder: `${sort}:${ascending ? "ascending" : "descending"}`,
    language,
    task,
    dataset,
    sensitivity,
    family,
    query,
    coverage,
    sort,
    direction: ascending ? "ascending" : "descending",
    scopeDatasetIds: [...ids],
    experimentDate: data.meta.experimentDate,
    resultRevision: data.meta.revision,
    snapshotHash: data.meta.snapshotHash,
    threshold: data.meta.threshold,
  };
  const setSortColumn = (key: string) => {
    if (key === sort) setAscending(!ascending);
    else {
      setSort(key);
      setAscending(["untouched", "extra", "cpu", "gpu", "name"].includes(key));
    }
  };
  const toggle = (id: string) =>
    setSelected((prev) =>
      prev.includes(id)
        ? prev.filter((x) => x !== id)
        : prev.length < 4
          ? [...prev, id]
          : prev,
    );
  const picked = selected.length
    ? selected
    : ["model:gliner2-fastino", "model:pplx"];
  const historicalIds = new Set(
    picked.filter((id) =>
      data.records.some(
        (row) =>
          row.system === id && row.adapterStatus === "historical-pre-fix",
      ),
    ),
  );
  const policyKeys = new Set(
    picked.flatMap((id) =>
      data.records
        .filter((row) => row.system === id && row.adapterStatus)
        .map((row) => `${row.adapterStatus}|${row.adapterPolicy ?? ""}`),
    ),
  );
  const policiesDiffer = policyKeys.size > 1;
  const scoredIds =
    policiesDiffer && !includeHistorical && historicalIds.size < picked.length
      ? picked.filter((id) => !historicalIds.has(id))
      : picked;
  const commonIds = new Set(
    [...ids].filter((id) =>
      scoredIds.every((s) =>
        data.records.some(
          (r) => r.system === s && r.dataset === id && !r.train,
        ),
      ),
    ),
  );
  const comparedScores = aggregate(data, commonIds);
  const compared = scoredIds.flatMap(
    (id) => comparedScores.find((score) => score.id === id) ?? [],
  );
  const leftOut = picked.filter((id) => !scoredIds.includes(id));
  const inspect = detail
    ? (view === "compare" ? compared : [...scores, ...ensembles]).find(
        (s) => s.id === detail,
      )
    : null;
  const inspectIds = view === "compare" ? commonIds : ids;
  const categories = categoryScores(data, entitySystem, ids);
  const sortedCategories = [...categories].sort(
    (a, b) =>
      (ratio(a.hidden, a.gold) ?? Infinity) -
      (ratio(b.hidden, b.gold) ?? Infinity),
  );
  const visibleDatasets = activeDatasets.filter((d) =>
    d.id.toLowerCase().includes(datasetQuery.toLowerCase().trim()),
  );
  const reference = ensembles.find((e) => e.id === REF);
  const reportButton = (path: string, label = "Read report") => (
    <button className="text-button" onClick={() => setReport(path)}>
      {label}
      <ArrowUpRight size={15} />
    </button>
  );
  const reset = () => {
    setLanguage("all");
    setTask("all");
    setDataset("all");
    setSensitivity(false);
    setQuery("");
    setDatasetQuery("");
    setFamily("all");
    setCoverage("complete");
    setSort("fullyHidden");
    setAscending(false);
  };
  const changeDashboard = <K extends keyof DecisionDashboardState>(
    key: K,
    value: DecisionDashboardState[K],
  ) => setDashboard((current) => ({ ...current, [key]: value }));
  const tableOnly = view === "leaderboard";
  const scopeDatasets = tableOnly ? baseDatasets : activeDatasets;
  const scopeKind = tableOnly ? initialTask : task;
  const scopeLanguage =
    tableOnly || language === "all"
      ? "All languages"
      : language === "en"
        ? "English"
        : language === "ru"
          ? "Russian"
          : "Multilingual";
  const scopeTask =
    scopeKind === "all"
      ? "PII + secrets"
      : scopeKind === "pii"
        ? "PII datasets"
        : "Secrets datasets";
  const scopeGold = scopeDatasets.reduce(
    (sum, item) => sum + item.gold_spans,
    0,
  );
  const sortLabels: Record<string, string> = {
    name: "detector name",
    fullyHidden: "fully hidden",
    detected: "detected",
    extra: "extra masking",
    f1: "character F1",
    cpu: "CPU seconds / 10k characters",
    gpu: "GPU seconds / 10k characters",
  };
  const copyLink = async () => {
    try {
      await navigator.clipboard.writeText(window.location.href);
      setNotice("Link copied");
    } catch {
      setNotice("Copy the URL from the address bar.");
    }
  };
  const datasetFilters = (
    <>
      <Pick
        value={language}
        label="Language"
        onChange={(v) => {
          setLanguage(v);
          setDataset("all");
        }}
        items={[
          { value: "all", label: "All languages" },
          { value: "en", label: "English · EN" },
          { value: "ru", label: "Russian · RU" },
          { value: "multi", label: "Multilingual" },
        ]}
      />
      <Pick
        value={task}
        label="Sensitive data type"
        onChange={(v) => {
          setTask(v);
          setDataset("all");
        }}
        items={[
          { value: "all", label: "Personal data + secrets" },
          { value: "pii", label: "Personal data only" },
          { value: "secrets", label: "Secrets only" },
        ]}
      />
      <Pick
        value={dataset}
        label="Dataset"
        onChange={setDataset}
        items={[
          { value: "all", label: "All datasets" },
          ...data.datasets
            .filter(
              (d) =>
                (language === "all" || d.lang === language) &&
                (task === "all" || d.kind === task),
            )
            .map((d) => ({ value: d.id, label: d.id })),
        ]}
      />
      <label className="check-label">
        <Checkbox
          checked={sensitivity}
          onCheckedChange={(v) => setSensitivity(v === true)}
        />
        Exclude generated/corrupt data
        <Hint name="Excludes six project-generated synthetic datasets and three corrupted copies. Upstream synthetic sources may remain." />
      </label>
      {(language !== "all" ||
        task !== "all" ||
        dataset !== "all" ||
        sensitivity) && (
        <button className="text-button reset" onClick={reset}>
          Reset
          <X size={13} />
        </button>
      )}
    </>
  );
  useEffect(() => {
    const context = (
      document as unknown as {
        modelContext?: {
          registerTool: (t: unknown, o: unknown) => Promise<void> | void;
        };
      }
    ).modelContext;
    if (!context) return;
    const controller = new AbortController();
    const tool = {
      name: "explore_benchmark",
      title: "Explore benchmark results",
      description:
        "Filter the visible benchmark leaderboard by language and task, with complete dataset coverage. Returns the top five configurations on that slice.",
      inputSchema: {
        type: "object",
        properties: {
          language: { type: "string", enum: ["all", "en", "ru", "multi"] },
          task: { type: "string", enum: ["all", "pii", "secrets"] },
        },
        additionalProperties: false,
      },
      annotations: { readOnlyHint: false, untrustedContentHint: false },
      execute(input: unknown) {
        if (!input || typeof input !== "object" || Array.isArray(input))
          throw Error("Expected filter object");
        const args = input as Record<string, unknown>;
        if (Object.keys(args).some((k) => !["language", "task"].includes(k)))
          throw Error("Unknown filter");
        const l = args.language ?? "all",
          t = args.task ?? "all";
        if (
          !["all", "en", "ru", "multi"].includes(String(l)) ||
          !["all", "pii", "secrets"].includes(String(t))
        )
          throw Error("Invalid language or task");
        const ds = data.datasets.filter(
          (d) => (l === "all" || d.lang === l) && (t === "all" || d.kind === t),
        );
        flushSync(() => {
          reset();
          setLanguage(String(l));
          setTask(String(t));
          setView("leaderboard");
          setSort("fullyHidden");
          setAscending(false);
        });
        router.replace("/leaderboard");
        const s = aggregate(data, new Set(ds.map((d) => d.id)))
          .filter((r) => r.sets === ds.length)
          .sort(
            (a, b) =>
              (b.fullyHidden ?? -Infinity) - (a.fullyHidden ?? -Infinity),
          );
        return {
          datasets: ds.length,
          configurations: s.length,
          top: s.slice(0, 5).map((r) => ({
            name: r.name,
            fullyHidden: percent(r.fullyHidden),
            detected: percent(r.detected),
            extraMasking: percent(r.extra),
          })),
        };
      },
    };
    try {
      void Promise.resolve(
        context.registerTool(tool, { signal: controller.signal }),
      ).catch(() => {});
    } catch {}
    return () => controller.abort();
  }, [data, router]);

  return (
    <TooltipProvider>
      <SidebarProvider style={{ "--sidebar-width": "212px" } as CSSProperties}>
        <SiteNav view={view} search={searchSuffix} />
        <main
          className={`workspace ${view === "leaderboard" ? "" : "compact-workspace"}`}
        >
          <SiteTopbar view={view} />
          <div className="page-content">
            <div className="page-title">
              <div>
                <h1>
                  {titleOverride ?? nav.find((v) => v.id === view)?.label}
                </h1>
                <p>{descriptionOverride ?? descriptions[view]}</p>
              </div>
              <button className="action small" onClick={copyLink}>
                <Copy size={14} />
                Copy link
              </button>
            </div>
            {[
              "leaderboard",
              "compare",
              "ensembles",
              "entities",
              "datasets",
            ].includes(view) && (
              <div
                className="analysis-scope"
                role="region"
                aria-label="Current analysis scope"
              >
                <span>
                  <strong>Scope</strong>
                  {scopeLanguage}
                </span>
                <span>{scopeTask}</span>
                <span>{scopeDatasets.length} datasets</span>
                <span>{n(scopeGold)} normalized annotations</span>
                <span>
                  {view === "leaderboard" ||
                  view === "compare" ||
                  view === "ensembles"
                    ? "Pooled annotations"
                    : "Dataset task / annotation type"}
                </span>
                <span className="mono">{data.meta.revision}</span>
              </div>
            )}
            {view === "leaderboard" && (
              <DecisionDashboard
                data={data}
                datasetIds={baseIds}
                state={dashboard}
                onChange={changeDashboard}
              />
            )}
            {["compare", "ensembles", "entities", "datasets"].includes(
              view,
            ) && (
              <div className="global-filters">
                <div className="filter-heading">
                  <SlidersHorizontal size={16} />
                  <span>Dataset slice</span>
                </div>
                {datasetFilters}
              </div>
            )}
            {view === "leaderboard" && (
              <>
                <Panel
                  title="Detector leaderboard"
                  subtitle={`${rows.length} detector setups · ${ids.size} datasets · sorted by ${sortLabels[sort]} ${ascending ? "ascending" : "descending"}`}
                  action={
                    <div className="panel-actions">
                      <button
                        className="text-button"
                        onClick={() => exportCsv(rows, scope)}
                      >
                        <Download size={15} />
                        Download current CSV
                      </button>
                      {reportButton("results/detectors.md", "Open full report")}
                    </div>
                  }
                  className="leaderboard-panel"
                >
                  <div className="table-controls leaderboard-controls">
                    <div className="search-box">
                      <Search size={14} />
                      <input
                        aria-label="Search detectors"
                        placeholder="Search detectors…"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                      />
                      {query && (
                        <button
                          aria-label="Clear search"
                          onClick={() => setQuery("")}
                        >
                          <X size={13} />
                        </button>
                      )}
                    </div>
                    {datasetFilters}
                    <Pick
                      value={family}
                      label="Detector family"
                      onChange={setFamily}
                      items={[
                        { value: "all", label: "All detector families" },
                        ...[...new Set(scores.map((s) => s.family))]
                          .sort()
                          .map((v) => ({ value: v, label: v.toUpperCase() })),
                      ]}
                    />
                    <Pick
                      value={coverage}
                      label="Dataset coverage"
                      onChange={setCoverage}
                      items={[
                        { value: "complete", label: "All datasets covered" },
                        { value: "all", label: "Include partial coverage" },
                      ]}
                    />
                  </div>
                  {coverage === "all" && (
                    <div className="inline-note">
                      Some detector setups were tested on fewer datasets. Select
                      detectors to compare them only on shared datasets.
                    </div>
                  )}
                  <Table className="leaderboard-table">
                    <TableHeader>
                      <TableRow>
                        <TableHead className="checkbox-col">
                          <span className="sr-only">Compare</span>
                        </TableHead>
                        <TableHead title="Position in the current sort">
                          Rank
                        </TableHead>
                        <TableHead
                          aria-sort={
                            sort === "name"
                              ? ascending
                                ? "ascending"
                                : "descending"
                              : "none"
                          }
                        >
                          <button onClick={() => setSortColumn("name")}>
                            Detector{" "}
                            {sort === "name" ? (
                              <ArrowDown
                                size={12}
                                className={ascending ? "rotate-180" : ""}
                              />
                            ) : (
                              <ArrowDownUp size={12} />
                            )}
                          </button>
                        </TableHead>
                        <TableHead>Family</TableHead>
                        {[
                          ["fullyHidden", "Fully hidden"],
                          ["detected", "Any overlap"],
                          ["extra", "Extra masked"],
                          ["f1", "Char F1"],
                          ["cpu", "CPU s/10k"],
                          ["gpu", "GPU s/10k"],
                        ].map(([k, l]) => (
                          <TableHead
                            key={k}
                            className={sort === k ? "sorted" : ""}
                            aria-sort={
                              sort === k
                                ? ascending
                                  ? "ascending"
                                  : "descending"
                                : "none"
                            }
                          >
                            <span className="metric-th">
                              <button onClick={() => setSortColumn(k)}>
                                {l}
                                {sort === k && (
                                  <ArrowDown
                                    size={12}
                                    className={ascending ? "rotate-180" : ""}
                                  />
                                )}
                              </button>
                              <Hint name={k} />
                            </span>
                          </TableHead>
                        ))}
                      </TableRow>
                    </TableHeader>
                    <TableBody>
                      {rows.map((r, i) => (
                        <TableRow
                          key={r.id}
                          data-state={
                            selected.includes(r.id) ? "selected" : undefined
                          }
                        >
                          <TableCell>
                            <Checkbox
                              aria-label={`Compare ${r.name}`}
                              checked={selected.includes(r.id)}
                              disabled={
                                selected.length >= 4 && !selected.includes(r.id)
                              }
                              onCheckedChange={() => toggle(r.id)}
                            />
                          </TableCell>
                          <TableCell className="rank mono">
                            {String(i + 1).padStart(2, "0")}
                          </TableCell>
                          <TableCell>
                            <Link
                              className="detector-name"
                              href={`/detectors/${detectorSlug(r.id)}`}
                            >
                              <span>
                                {r.name}
                                {r.sets !== ids.size && (
                                  <span
                                    className="coverage-marker"
                                    title={`Covers ${r.sets} of ${ids.size} datasets`}
                                  >
                                    <CircleHelp size={10} />
                                  </span>
                                )}
                              </span>
                              <ArrowUpRight size={13} />
                            </Link>
                            <AdapterStatus score={r} />
                          </TableCell>
                          <TableCell>
                            <span className="family-pill">
                              {r.family.toUpperCase()}
                            </span>
                          </TableCell>
                          <TableCell className="number metric-emphasis">
                            <span
                              className="compact-metric"
                              title={`${n(r.hidden)} of ${n(r.gold)} annotations completely hidden`}
                            >
                              {percent(r.fullyHidden)}
                              <ShieldCheck size={10} />
                            </span>
                          </TableCell>
                          <TableCell className="number">
                            {percent(r.detected)}
                          </TableCell>
                          <TableCell className="number">
                            {percent(r.extra)}
                          </TableCell>
                          <TableCell>
                            <div className="f1-cell">
                              <span className="mono">
                                {r.f1?.toFixed(3) ?? "—"}
                              </span>
                              <span>
                                <i style={{ width: `${(r.f1 ?? 0) * 100}%` }} />
                              </span>
                            </div>
                          </TableCell>
                          <TableCell className="number dim">
                            {r.cpu?.toFixed(2) ?? "—"}
                          </TableCell>
                          <TableCell className="number dim">
                            {r.gpu?.toFixed(2) ?? "—"}
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                  {!rows.length && (
                    <div className="empty">
                      <Search size={25} />
                      <h3>No matching measurements</h3>
                      <p>Try a broader slice or include partial coverage.</p>
                      <button className="action" onClick={reset}>
                        Reset filters
                      </button>
                    </div>
                  )}
                  <div className="table-footer">
                    <span>
                      <ShieldCheck size={14} />
                      Known training overlaps removed
                    </span>
                    <span>
                      Detection threshold {data.meta.threshold} ·
                      Character-level scoring
                    </span>
                  </div>
                </Panel>
                <div className="interpretation">
                  <CircleHelp size={17} />
                  <p>
                    <strong>How to read these numbers.</strong> Completely
                    hidden means the whole sensitive value was masked. Found at
                    least partly can still leave text visible. Extra text masked
                    is measured on unlabeled rows and is not a verified
                    false-positive rate.
                  </p>
                  {reportButton("docs/metrics.md", "Metric definitions")}
                </div>
                <div className="benchmark-footprint">
                  <div className="insights-heading">
                    <div>
                      <span>Benchmark size</span>
                      <h2>What was tested</h2>
                    </div>
                    <p>
                      These counts describe the test data; they do not show
                      which detector is best.
                    </p>
                  </div>
                  <div className="stats-strip footprint">
                    {[
                      {
                        label: "Detector setups tested",
                        value: n(
                          data.systems.filter((s) => s.kind === "model").length,
                        ),
                        sub: `${data.meta.catalogRecords} catalog records · variants included`,
                        icon: Layers3,
                      },
                      {
                        label: "Language groups",
                        value: n(
                          new Set(scopeDatasets.map((d) => d.lang)).size,
                        ),
                        sub: [...new Set(scopeDatasets.map((d) => d.lang))]
                          .map(
                            (lang) =>
                              ({
                                en: "English",
                                ru: "Russian",
                                multi: "Multilingual",
                              })[lang] ?? lang,
                          )
                          .join(" · "),
                        icon: Globe2,
                      },
                      {
                        label: "Text rows tested",
                        value: n(
                          scopeDatasets.reduce((a, d) => a + d.rows, 0),
                        ),
                        sub: `${n(data.meta.runs)} saved prediction runs overall`,
                        icon: Braces,
                      },
                      {
                        label: "Labeled sensitive items",
                        value: n(
                          scopeDatasets.reduce((a, d) => a + d.gold_spans, 0),
                        ),
                        sub: "Values expanded to word boundaries",
                        icon: ShieldCheck,
                      },
                    ].map((s, i) => (
                      <div className="stat" key={s.label}>
                        <span className="stat-label">{s.label}</span>
                        <strong
                          className={`stat-value mono ${i === 3 ? "accent-text" : ""}`}
                        >
                          {s.value}
                        </strong>
                        <small>{s.sub}</small>
                      </div>
                    ))}
                  </div>
                </div>
              </>
            )}
            {view === "compare" && (
              <>
                <Panel
                  title="Choose up to four detectors"
                  subtitle="Comparison uses only datasets available to every selected detector. The current selection is shareable from the URL."
                  action={
                    <div className="panel-actions">
                      <button
                        className="text-button"
                        onClick={() =>
                          exportCsv(
                            compared,
                            compareExportContext(scope, scoredIds, [...commonIds]),
                          )
                        }
                      >
                        <Download size={15} />
                        Download comparison CSV
                      </button>
                      <button className="text-button" onClick={copyLink}>
                        <Copy size={15} />
                        Copy link
                      </button>
                    </div>
                  }
                >
                  <div className="compare-pickers">
                    {picked.map((id, i) => (
                      <div key={`${id}-${i}`} className="compare-picker">
                        <span
                          className="compare-dot"
                          style={{ background: colors[i] }}
                        />
                        <Pick
                          value={id}
                          label={`Detector ${i + 1}`}
                          onChange={(v) => {
                            const arr = [...picked];
                            arr[i] = v;
                            setSelected(arr);
                          }}
                          items={data.systems
                            .filter(
                              (s) =>
                                s.kind === "model" &&
                                (s.id === id || !picked.includes(s.id)),
                            )
                            .map((s) => ({ value: s.id, label: s.name }))}
                        />
                        {picked.length > 2 && (
                          <button
                            className="icon-button"
                            aria-label={`Remove detector ${i + 1}`}
                            onClick={() =>
                              setSelected(
                                picked.filter((_, j) => j !== i),
                              )
                            }
                          >
                            <X size={16} />
                          </button>
                        )}
                      </div>
                    ))}
                    {picked.length < 4 && (
                      <button
                        className="action"
                        onClick={() =>
                          setSelected([
                            ...picked,
                            ...scores
                              .filter((s) => !picked.includes(s.id))
                              .slice(0, 1)
                              .map((s) => s.id),
                          ])
                        }
                      >
                        + Add detector
                      </button>
                    )}
                  </div>
                  {policiesDiffer && (
                    <p className="publication-note" role="status">
                      These detectors use different scanner mapping policies, so
                      their numbers are not one measurement.
                      {leftOut.length > 0 && (
                        <>
                          {" "}
                          Left out until you include historical pre-fix
                          results:{" "}
                          {leftOut
                            .map(
                              (id) =>
                                data.systems.find((system) => system.id === id)
                                  ?.name,
                            )
                            .join(", ")}
                          .
                        </>
                      )}
                      {historicalIds.size > 0 && (
                        <label className="scanner-choice">
                          <Checkbox
                            checked={includeHistorical}
                            onCheckedChange={(value) =>
                              setIncludeHistorical(value === true)
                            }
                          />
                          Include historical pre-fix results
                        </label>
                      )}
                    </p>
                  )}
                  <div className="inline-note">
                    <ShieldCheck size={15} />
                    {commonIds.size} shared datasets ·{" "}
                    {n(
                      data.datasets
                        .filter((d) => commonIds.has(d.id))
                        .reduce((s, d) => s + d.gold_spans, 0),
                    )}{" "}
                    normalized gold annotations · Known training-source overlaps
                    excluded
                  </div>
                </Panel>
                {!commonIds.size ? (
                  <div className="empty">
                    <h3>No shared eligible datasets</h3>
                    <p>Choose other detectors or broaden the dataset slice.</p>
                  </div>
                ) : (
                  <>
                    <div className="comparison-cards">
                      {compared.map((r, i) => (
                        <section
                          key={r.id}
                          className="comparison-card"
                          style={
                            { "--compare-color": colors[i] } as CSSProperties
                          }
                        >
                          <div className="compare-card-head">
                            <span className="family-pill">
                              {r.family.toUpperCase()}
                            </span>
                            <Link
                              className="icon-button"
                              aria-label={`Open ${r.name} profile`}
                              href={`/detectors/${detectorSlug(r.id)}`}
                            >
                              <ArrowUpRight size={18} />
                            </Link>
                          </div>
                          <h2>{r.name}</h2>
                          <AdapterStatus score={r} inventory />
                          <div className="comparison-main mono">
                            {percent(r.fullyHidden)}
                            <span>fully hidden</span>
                          </div>
                          {[
                            ["Detected / any overlap", percent(r.detected)],
                            ["Extra masking", percent(r.extra)],
                            ["Character F1", r.f1?.toFixed(3) ?? "—"],
                            ["CPU s / 10k chars", r.cpu?.toFixed(2) ?? "—"],
                            ["Untouched", percent(r.untouched)],
                            ["Gold annotations", n(r.gold)],
                          ].map(([l, v]) => (
                            <div className="compare-stat" key={l}>
                              <span>{l}</span>
                              <b className="mono">{v}</b>
                            </div>
                          ))}
                        </section>
                      ))}
                    </div>
                    <div className="charts-grid compare-charts">
                      <Panel
                        title="Coverage vs extra masking"
                        subtitle="Same shared dataset intersection"
                      >
                        <Tradeoff rows={compared} onSelect={setDetail} />
                      </Panel>
                      <Panel
                        title="Coverage vs CPU speed"
                        subtitle="Speed uses saved reference measurements with detector-specific workloads; quality uses the shared dataset intersection"
                      >
                        <SpeedQuality rows={compared} onSelect={setDetail} />
                      </Panel>
                    </div>
                    <Panel
                      title="Full hiding by data type"
                      subtitle="Same dataset intersection for every column. Each cell retains its own annotation count."
                    >
                      <Table className="analysis-table">
                        <TableHeader>
                          <TableRow>
                            <TableHead>Data type</TableHead>
                            <TableHead>Gold annotations</TableHead>
                            {compared.map((r) => (
                              <TableHead key={r.id}>{r.name}</TableHead>
                            ))}
                          </TableRow>
                        </TableHeader>
                        <TableBody>
                          {data.categories.map((c) => {
                            const cs = compared.map(
                              (s) =>
                                categoryScores(data, s.id, commonIds).find(
                                  (x) => x.id === c.id,
                                )!,
                            );
                            return (
                              <TableRow key={c.id}>
                                <TableCell>{c.title}</TableCell>
                                <TableCell className="mono">
                                  {n(cs[0]?.gold ?? 0)}
                                </TableCell>
                                {cs.map((v, i) => (
                                  <TableCell key={i}>
                                    <div className="comparison-bar">
                                      <span className="mono">
                                        {percent(ratio(v.hidden, v.gold))}
                                      </span>
                                      <i
                                        style={{
                                          width: `${ratio(v.hidden, v.gold) ?? 0}%`,
                                          background: colors[i],
                                        }}
                                      />
                                    </div>
                                  </TableCell>
                                ))}
                              </TableRow>
                            );
                          })}
                        </TableBody>
                      </Table>
                    </Panel>
                  </>
                )}
              </>
            )}
            {view === "ensembles" && (
              <>
                <div className="reference-banner">
                  <div>
                    <span className="eyebrow">FIXED REFERENCE COMPOSITION</span>
                    <h2>PPLX + Fastino + mmBERT + BardsAI</h2>
                    <p>
                      Three mutually exclusive outcomes on one fixed dataset
                      slice. Extra masking is reported separately below.
                    </p>
                  </div>
                  <div>
                    <strong className="mono">
                      {percent(reference?.fullyHidden ?? null)}
                    </strong>
                    <span>
                      {reference
                        ? `${n(reference.hidden)} / ${n(reference.gold)}`
                        : "—"}{" "}
                      fully hidden
                    </span>
                  </div>
                  <div>
                    <strong className="mono">
                      {reference
                        ? percent(
                            ratio(
                              reference.hit - reference.hidden,
                              reference.gold,
                            ),
                          )
                        : "—"}
                    </strong>
                    <span>
                      {reference ? n(reference.hit - reference.hidden) : "—"}{" "}
                      partially hidden
                    </span>
                  </div>
                  <div>
                    <strong className="mono">
                      {percent(reference?.untouched ?? null)}
                    </strong>
                    <span>
                      {reference ? n(reference.missed) : "—"} untouched
                    </span>
                  </div>
                </div>
                <Panel
                  title="Composition outcomes"
                  subtitle="Manually selected compositions evaluated on this benchmark; no independent selection holdout."
                  action={reportButton("results/ensemble.md")}
                >
                  <Table className="analysis-table">
                    <TableHeader>
                      <TableRow>
                        {[
                          "Composition",
                          "Untouched ↓",
                          "Fully hidden ↑",
                          "Extra masking ↓",
                          "Char F1 ↑",
                        ].map((h) => (
                          <TableHead key={h}>{h}</TableHead>
                        ))}
                      </TableRow>
                    </TableHeader>
                    <TableBody>
                      {ensembles.map((r) => (
                        <TableRow key={r.id}>
                          <TableCell>
                            <button
                              className="text-button composition-label"
                              onClick={() => setDetail(r.id)}
                            >
                              {r.name}
                              <ArrowUpRight size={14} />
                            </button>
                            {r.sets !== ids.size && (
                              <span className="coverage">
                                Partial coverage · {r.sets}/{ids.size} datasets
                              </span>
                            )}
                          </TableCell>
                          <TableCell
                            className="number"
                            title={`${n(r.missed)} of ${n(r.gold)} annotations untouched`}
                          >
                            {percent(r.untouched)}
                          </TableCell>
                          <TableCell className="number metric-emphasis">
                            {percent(r.fullyHidden)}
                          </TableCell>
                          <TableCell className="number">
                            {percent(r.extra)}
                          </TableCell>
                          <TableCell className="number">
                            {r.f1?.toFixed(3) ?? "—"}
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </Panel>
                <Panel
                  title="Detection and full hiding"
                  subtitle="A larger union can hide more annotations while masking more unannotated text."
                >
                  <MaskBars
                    rows={ensembles
                      .filter((r) => r.sets === ids.size)
                      .sort(
                        (a, b) => (a.untouched ?? 100) - (b.untouched ?? 100),
                      )}
                    onSelect={setDetail}
                  />
                </Panel>
                <div className="interpretation">
                  <CircleHelp size={18} />
                  <p>
                    Ensemble costs in the source report are derived from member
                    throughput, not measured end-to-end latency. Compositions
                    containing BardsAI have a mixed-device GPU estimate.
                  </p>
                  {reportButton("results/overview.md")}
                </div>
              </>
            )}
            {view === "entities" && (
              <>
                <div className="section-toolbar">
                  <div>
                    <h2>Coverage by data type</h2>
                    <p>
                      Weakest categories first · full hiding after word-boundary
                      expansion
                    </p>
                  </div>
                  <Pick
                    label="Data type detector"
                    value={entitySystem}
                    onChange={setEntitySystem}
                    className="system-picker"
                    items={[
                      ...data.systems.filter((s) => s.kind === "composition"),
                      ...data.systems.filter((s) => s.kind === "model"),
                    ].map((s) => ({ value: s.id, label: s.name }))}
                  />
                </div>
                <div className="entity-cards">
                  {sortedCategories.map((c, i) => (
                    <section key={c.id} className="entity-card">
                      <div>
                        <span className="entity-index mono">
                          {String(i + 1).padStart(2, "0")}
                        </span>
                        <h3>{c.title}</h3>
                      </div>
                      <strong className="mono">
                        {percent(ratio(c.hidden, c.gold))}
                      </strong>
                      <div className="entity-track">
                        <i
                          style={{
                            width: `${ratio(c.hidden, c.gold) ?? 0}%`,
                            background: "var(--chart-1)",
                          }}
                        />
                      </div>
                      <p>
                        {n(c.hidden)} / {n(c.gold)} fully hidden
                      </p>
                      <span>
                        Any overlap{" "}
                        <b className="mono">{percent(ratio(c.hit, c.gold))}</b>
                      </span>
                    </section>
                  ))}
                </div>
                <Panel
                  title="Dataset × data type"
                  subtitle="Full hiding percentage. A dash is labeled as no annotations or no eligible measurement on hover."
                  action={reportButton("results/by-entity.md")}
                >
                  <div className="heatmap-scroll">
                    <Table className="heatmap">
                      <TableHeader>
                        <TableRow>
                          <TableHead>Dataset</TableHead>
                          {data.categories.map((c) => (
                            <TableHead key={c.id} title={c.title}>
                              {c.id}
                            </TableHead>
                          ))}
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        {activeDatasets.map((d) => {
                          const row = data.records.find(
                            (r) =>
                              r.system === entitySystem &&
                              r.dataset === d.id &&
                              !r.train,
                          );
                          return (
                            <TableRow key={d.id}>
                              <TableCell>
                                <Link href={`/datasets/${d.id}`}>{d.id}</Link>
                              </TableCell>
                              {data.categories.map((c) => {
                                const v = row?.categories.find(
                                    (x) => x.id === c.id,
                                  ),
                                  pct = v ? ratio(v.hidden, v.gold) : null,
                                  missing = !row
                                    ? "No eligible measurement"
                                    : !v || !v.gold
                                      ? "No gold annotations"
                                      : `${c.title}: ${n(v.hidden)} / ${n(v.gold)}`;
                                return (
                                  <TableCell key={c.id}>
                                    <div
                                      title={missing}
                                      className="heat-cell"
                                      style={
                                        pct !== null
                                          ? {
                                              background: `color-mix(in srgb, var(--heat-high) ${pct}%, var(--heat-low))`,
                                              color: "var(--foreground)",
                                            }
                                          : {}
                                      }
                                    >
                                      {pct === null ? "—" : percent(pct, 0)}
                                    </div>
                                  </TableCell>
                                );
                              })}
                            </TableRow>
                          );
                        })}
                      </TableBody>
                    </Table>
                  </div>
                  <div className="table-footer">
                    {data.systems.find((s) => s.id === entitySystem)?.name}
                    <span className="heat-legend">
                      0%
                      <i />
                      100%
                    </span>
                  </div>
                </Panel>
              </>
            )}
            {view === "datasets" && (
              <>
                <div className="dataset-summary">
                  <div>
                    <Database size={22} />
                    <strong>{visibleDatasets.length}</strong>
                    <span>
                      {datasetQuery ? "matching datasets" : "datasets"}
                    </span>
                  </div>
                  <div>
                    <Globe2 size={22} />
                    <strong>
                      {new Set(visibleDatasets.map((d) => d.lang)).size}
                    </strong>
                    <span>language groups</span>
                  </div>
                  <div>
                    <Braces size={22} />
                    <strong>
                      {n(visibleDatasets.reduce((s, d) => s + d.rows, 0))}
                    </strong>
                    <span>input rows</span>
                  </div>
                  <div>
                    <ShieldCheck size={22} />
                    <strong>
                      {n(visibleDatasets.reduce((s, d) => s + d.gold_spans, 0))}
                    </strong>
                    <span>gold annotations</span>
                  </div>
                </div>
                <Panel
                  title="Dataset catalog"
                  subtitle={`${visibleDatasets.length} of ${activeDatasets.length} datasets in this slice · synthetic flags identify project-generated datasets; upstream sources may also be synthetic.`}
                  action={reportButton("docs/datasets.md")}
                >
                  <div className="table-controls">
                    <div className="search-box">
                      <Search size={16} />
                      <input
                        aria-label="Search datasets"
                        placeholder="Search datasets…"
                        value={datasetQuery}
                        onChange={(e) => setDatasetQuery(e.target.value)}
                      />
                      {datasetQuery && (
                        <button
                          aria-label="Clear dataset search"
                          onClick={() => setDatasetQuery("")}
                        >
                          <X size={13} />
                        </button>
                      )}
                    </div>
                  </div>
                  <div className="dataset-cards">
                    {visibleDatasets.map((d) => (
                      <article key={d.id} className="dataset-card">
                        <div className="dataset-card-top">
                          <span className="dataset-icon">
                            <Database size={19} />
                          </span>
                          <span className="subtle-badge">
                            {d.lang.toUpperCase()}
                          </span>
                          <span className="subtle-badge">
                            {d.kind.toUpperCase()}
                          </span>
                          {difficultyFor(d.id) && (
                            <span
                              className={`difficulty-badge tier-${difficultyFor(d.id)!.tier.toLowerCase()}`}
                            >
                              {difficultyFor(d.id)!.tier} ·{" "}
                              {percent(difficultyFor(d.id)!.score, 1)}
                            </span>
                          )}
                        </div>
                        <h3>{d.id}</h3>
                        <div className="dataset-counts">
                          <span>
                            <strong className="mono">{n(d.rows)}</strong> rows
                          </span>
                          <span>
                            <strong className="mono">{n(d.gold_spans)}</strong>{" "}
                            annotations
                          </span>
                        </div>
                        <div className="dataset-tags">
                          {d.synthetic && <span>Project synthetic</span>}
                          {d.corrupted && <span>Corrupted copy</span>}
                          <span>{d.license}</span>
                        </div>
                        <div className="dataset-source">
                          <DatasetSource source={d.source} />
                          <code title={d.bench_sha256}>
                            SHA {d.bench_sha256.slice(0, 8)}
                          </code>
                        </div>
                        <div className="dataset-actions">
                          <Link
                            className="text-button"
                            href={`/datasets/${d.id}`}
                          >
                            View results
                            <ArrowRight size={14} />
                          </Link>
                          <button
                            className="icon-button"
                            title="Original dataset report"
                            aria-label={`Report for ${d.id}`}
                            onClick={() =>
                              setReport(`results/datasets/${d.id}.md`)
                            }
                          >
                            <BookOpen size={16} />
                          </button>
                        </div>
                      </article>
                    ))}
                  </div>
                  {!activeDatasets.length && (
                    <div className="empty">
                      <h3>No datasets in this slice</h3>
                      <p>
                        Multilingual secrets have no retained dataset. Russian
                        secrets use one project-generated synthetic dataset.
                      </p>
                      <button onClick={reset} className="action">
                        Reset filters
                      </button>
                    </div>
                  )}
                  {activeDatasets.length > 0 && !visibleDatasets.length && (
                    <div className="empty">
                      <Search size={25} />
                      <h3>No matching datasets</h3>
                      <p>
                        No dataset name matches “{datasetQuery}” in the current{" "}
                        {activeDatasets.length}-dataset slice.
                      </p>
                      <button
                        onClick={() => setDatasetQuery("")}
                        className="action"
                      >
                        Clear search
                      </button>
                    </div>
                  )}
                </Panel>
              </>
            )}
            {view === "performance" && (
              <>
                <div className="section-toolbar">
                  <Segmented
                    value={device}
                    onChange={setDevice}
                    label="Throughput device"
                    items={[
                      { value: "cpu", label: "CPU throughput" },
                      { value: "cuda", label: "GPU throughput" },
                    ]}
                  />
                  <Pick
                    label="Measurement group"
                    value={speedGroup}
                    onChange={setSpeedGroup}
                    items={[
                      { value: "reference", label: "Reference machine group" },
                      { value: "all", label: "All measurement conditions" },
                    ]}
                  />
                </div>
                <div className="hardware-card">
                  <Gauge size={24} />
                  <div>
                    <h2>
                      {speedGroup === "all"
                        ? "All recorded hardware groups"
                        : device === "cpu"
                          ? "AMD EPYC 9K84"
                          : "NVIDIA GeForce RTX 5090"}
                    </h2>
                    <p>
                      {speedGroup === "all"
                        ? "Hardware, concurrency and dataset counts vary. Read each row before comparing."
                        : device === "cpu"
                          ? "Saved reference measurements · 16 threads per process · 24 concurrent workers · workloads differ"
                          : "Saved reference measurements · 2 concurrent workers · workloads differ"}
                    </p>
                  </div>
                  <span className="subtle-badge">BATCH THROUGHPUT</span>
                </div>
                <Performance data={data} device={device} group={speedGroup} />
                <div className="interpretation">
                  <CircleHelp size={18} />
                  <p>
                    p50 and p95 are amortized compute per row, not individually
                    timed request latency. Missing measurements stay blank.
                    Dataset counts differ across runs.
                  </p>
                  {reportButton("results/speed.md", "All conditions")}
                </div>
              </>
            )}
            {view === "methodology" && (
              <>
                <div className="method-intro">
                  <span className="method-icon">
                    <ShieldCheck size={34} />
                  </span>
                  <div>
                    <h2>A benchmark you can inspect.</h2>
                    <p>
                      Frozen inputs. Declared masking rules. Exact counts.
                      <br />A descriptive comparison under one protocol.
                    </p>
                  </div>
                  <div className="method-version">
                    <span>EXPERIMENT</span>
                    <b className="mono">2026-09-09</b>
                    <span>RESULT REVISION</span>
                    <b className="mono">{data.meta.revision}</b>
                  </div>
                </div>
                <div className="method-grid">
                  {[
                    {
                      title: "01 · The inputs",
                      body: "41 retained dataset cuts cover Russian, English and multilingual PII and secrets. Rows and normalized gold annotations retain their source identity.",
                      path: "docs/datasets.md",
                      label: "Dataset catalog",
                    },
                    {
                      title: "02 · The mask",
                      body: "Predicted offsets are normalized to word boundaries. Detection requires any character overlap; full hiding requires every annotated character to be covered.",
                      path: "docs/metrics.md",
                      label: "Scoring contract",
                    },
                    {
                      title: "03 · The comparison",
                      body: "Known training-source overlaps are excluded. Complete coverage is the default. Pairwise comparisons use the intersection of eligible datasets.",
                      path: "docs/methodology.md",
                      label: "Full methodology",
                    },
                    {
                      title: "04 · The limits",
                      body: "Unannotated rows are not verified clean. Compositions were inspected on this benchmark. Observed percentages are not production leak probabilities.",
                      path: "docs/limitations.md",
                      label: "Limitations",
                    },
                  ].map((c) => (
                    <section key={c.title} className="method-card">
                      <h3>{c.title}</h3>
                      <p>{c.body}</p>
                      {reportButton(c.path, c.label)}
                    </section>
                  ))}
                </div>
                <Panel title="How to read the metrics">
                  <div className="definitions">
                    {Object.entries(help).map(([key, value]) => (
                      <div key={key}>
                        <h3>
                          {
                            {
                              untouched: "Untouched",
                              fullyHidden: "Fully hidden",
                              detected: "Detected / any overlap",
                              extra: "Extra masking",
                              f1: "Character F1",
                              cpu: "CPU throughput",
                              gpu: "GPU throughput",
                            }[key]
                          }
                        </h3>
                        <p>{value}</p>
                      </div>
                    ))}
                  </div>
                </Panel>
                <Panel
                  title="One artificial example"
                  subtitle="Illustrative text, not corpus. Extra masking counts only rows that have no labels. Unlabeled does not mean verified clean."
                >
                  <div className="metric-example">
                    <div>
                      <span>Input</span>
                      <code>Account: alex@example.com</code>
                    </div>
                    <div>
                      <span>Partial prediction</span>
                      <code>
                        Account: <mark>alex</mark>@example.com
                      </code>
                      <small>Detected, but not fully hidden</small>
                    </div>
                    <div>
                      <span>Complete mask</span>
                      <code>
                        Account: <mark>████████████████</mark>
                      </code>
                      <small>Detected and fully hidden</small>
                    </div>
                    <div>
                      <span>Extra masking</span>
                      <code>
                        <mark>Hello</mark> there
                      </code>
                      <small>
                        A different row, with no labels: 5 masked characters /
                        11 characters. The email row above is not in this
                        denominator.
                      </small>
                    </div>
                  </div>
                </Panel>
                <Panel
                  title="Reproduce and extend"
                  subtitle="The public verification regenerates publication artifacts; it does not rerun inference."
                >
                  <div className="code-block">
                    <pre>
                      uv sync --frozen{"\n"}uv run python scripts/verify.py
                      {"\n"}uv run python scripts/render.py{"\n"}uv run python
                      scripts/verify.py
                    </pre>
                    <button
                      className="icon-button"
                      aria-label="Copy reproduction commands"
                      onClick={async () => {
                        try {
                          await navigator.clipboard.writeText(
                            "uv sync --frozen\nuv run python scripts/verify.py\nuv run python scripts/render.py\nuv run python scripts/verify.py",
                          );
                          setNotice("Commands copied");
                        } catch {
                          setNotice("Select and copy the commands shown here.");
                        }
                      }}
                    >
                      <Copy size={16} />
                    </button>
                  </div>
                  <div className="resource-links">
                    {reportButton("docs/usage.md", "Evaluate your detector")}
                    {reportButton("docs/reproduce.md", "Reproduction guide")}
                    {reportButton("docs/sources.md", "Source provenance")}
                    {reportButton(
                      "docs/comparison.md",
                      "Other evaluation methods",
                    )}
                    {reportButton("CHANGELOG.md", "Changelog")}
                  </div>
                </Panel>
                <div className="integrity-box">
                  <FileJson size={20} />
                  <div>
                    <strong>Source snapshot SHA-256</strong>
                    <code>{data.meta.snapshotHash}</code>
                  </div>
                  <a
                    className="action"
                    href="/evidence/results/snapshot.json"
                    download
                  >
                    <Download size={15} />
                    Snapshot
                  </a>
                </div>
              </>
            )}
            {view === "downloads" && (
              <Downloads files={sourceFiles} onReport={setReport} />
            )}
            <footer className="page-footer">
              <span>
                <Braces size={15} />
                PII Arena <span className="footer-dot">·</span> Frozen 09 Sep
                2026
              </span>
              <span>
                Publication v{data.meta.version}{" "}
                <span className="footer-dot">·</span> MIT licensed{" "}
                <button onClick={() => setReport("LICENSE")}>
                  License
                  <ArrowUpRight size={12} />
                </button>
              </span>
            </footer>
          </div>
          {selected.length > 0 && view === "leaderboard" && (
            <div className="selection-bar">
              <span>
                <Columns3 size={18} />
                {selected.length} selected
              </span>
              <div className="selected-names">
                {selected.map((id) => (
                  <button key={id} onClick={() => toggle(id)}>
                    {id.replace("model:", "")}
                    <X size={12} />
                  </button>
                ))}
              </div>
              <button
                className="action primary"
                disabled={selected.length < 2}
                onClick={() => navigate("compare")}
              >
                Compare detectors
                <ArrowRight size={15} />
              </button>
              <button
                className="icon-button"
                aria-label="Clear selection"
                onClick={() => setSelected([])}
              >
                <X size={17} />
              </button>
            </div>
          )}
          <Toaster position="bottom-right" />
        </main>
        <Sheet
          open={!!detail}
          onOpenChange={(o) => {
            if (!o) setDetail(null);
          }}
        >
          <SheetContent className="details-sheet">
            <SheetHeader>
              <SheetTitle>
                {inspect?.name ?? "No measurement in this slice"}
              </SheetTitle>
              <SheetDescription>
                {inspect?.family.toUpperCase()} · {inspect?.sets ?? 0} eligible
                datasets · Threshold {data.meta.threshold}
              </SheetDescription>
            </SheetHeader>
            {inspect && (
              <div className="detail-content">
                <div className="detail-kpis">
                  <div>
                    <span>Fully hidden</span>
                    <strong className="metric-emphasis mono">
                      {percent(inspect.fullyHidden)}
                    </strong>
                  </div>
                  <div>
                    <span>Detected / any overlap</span>
                    <strong className="mono">
                      {percent(inspect.detected)}
                    </strong>
                  </div>
                  <div>
                    <span>Extra masking</span>
                    <strong className="mono">{percent(inspect.extra)}</strong>
                  </div>
                </div>
                <div className="detail-counts">
                  {[
                    ["Gold annotations", n(inspect.gold)],
                    ["Fully hidden", n(inspect.hidden)],
                    ["Any overlap", n(inspect.hit)],
                    ["Untouched", n(inspect.missed)],
                    ["Hidden by raw offsets", n(inspect.rawHidden)],
                    [
                      "Residual annotated rows",
                      `${n(inspect.residualRows)} / ${n(inspect.positiveRows)}`,
                    ],
                    [
                      "Extra masked characters",
                      `${n(inspect.maskedNegativeChars)} / ${n(inspect.negativeChars)}`,
                    ],
                    ["Character F1", inspect.f1?.toFixed(6) ?? "—"],
                    [
                      "Character precision",
                      inspect.precision?.toFixed(6) ?? "—",
                    ],
                    ["Character recall", inspect.recall?.toFixed(6) ?? "—"],
                  ].map(([l, v]) => (
                    <div key={l}>
                      <span>{l}</span>
                      <b className="mono">{v}</b>
                    </div>
                  ))}
                </div>
                {inspect.kind === "composition" ? (
                  <div className="detail-revision">
                    <span>Member revisions</span>
                    {(inspect.participants ?? []).map((item) => (
                      <div key={item.member}>
                        <code>
                          {item.member} {item.revision || "not recorded"}
                        </code>
                        {item.upstream && (
                          <a href={item.upstream} target="_blank" rel="noreferrer">
                            {item.upstream}
                          </a>
                        )}
                        {item.flags && item.flags !== "-" && (
                          <span>{item.flags}</span>
                        )}
                      </div>
                    ))}
                    <span>
                      These are member pins. Result revision {data.meta.revision}{" "}
                      identifies the published ensemble.
                    </span>
                  </div>
                ) : (
                  <>
                    {inspect.upstream && (
                      <a
                        href={inspect.upstream}
                        target="_blank"
                        rel="noreferrer"
                        className="action"
                      >
                        <ExternalLink size={15} />
                        Upstream model
                      </a>
                    )}
                    {inspect.revision && (
                      <div className="detail-revision">
                        <span>Pinned revision / version</span>
                        <code>{inspect.revision}</code>
                      </div>
                    )}
                    {inspect.flags && inspect.flags !== "-" && (
                      <p className="inline-note">{inspect.flags}</p>
                    )}
                  </>
                )}
                {inspect.kind === "model" && (
                  <Link
                    className="action"
                    href={`/detectors/${detectorSlug(inspect.id)}`}
                  >
                    Full detector profile
                    <ArrowUpRight size={15} />
                  </Link>
                )}
                <AdapterStatus score={inspect} inventory />
                <h3>Results by dataset</h3>
                <Table>
                  <TableHeader>
                    <TableRow>
                      <TableHead>Dataset</TableHead>
                      <TableHead>Detected / any overlap</TableHead>
                      <TableHead>Fully hidden</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {data.records
                      .filter(
                        (r) =>
                          r.system === detail &&
                          !r.train &&
                          inspectIds.has(r.dataset),
                      )
                      .sort((a, b) => a.hidden / a.gold - b.hidden / b.gold)
                      .map((r) => (
                        <TableRow key={r.dataset}>
                          <TableCell>
                            <Link
                              className="text-button"
                              href={`/datasets/${r.dataset}`}
                              onClick={() => setDetail(null)}
                            >
                              {r.dataset}
                            </Link>
                          </TableCell>
                          <TableCell
                            className="number"
                            title={`${n(r.hit)} of ${n(r.gold)} annotations detected`}
                          >
                            {percent(ratio(r.hit, r.gold))}
                          </TableCell>
                          <TableCell className="mono">
                            {percent(ratio(r.hidden, r.gold))}
                          </TableCell>
                        </TableRow>
                      ))}
                  </TableBody>
                </Table>
                <button
                  className="action"
                  onClick={() =>
                    download(
                      `${inspect.name.replace(/[^a-z0-9-]/gi, "_")}.json`,
                      JSON.stringify(
                        {
                          scope: {
                            ...(view === "compare"
                              ? compareExportContext(scope, scoredIds, [...commonIds])
                              : scope),
                            datasetIds: [...inspectIds],
                          },
                          score: inspect,
                          records: data.records.filter(
                            (r) =>
                              r.system === detail &&
                              !r.train &&
                              inspectIds.has(r.dataset),
                          ),
                        },
                        null,
                        2,
                      ),
                      "application/json",
                    )
                  }
                >
                  <Download size={15} />
                  Download result JSON
                </button>
              </div>
            )}
          </SheetContent>
        </Sheet>
        <EvidenceViewer
          path={report}
          onClose={() => setReport(null)}
          onNavigate={setReport}
        />
      </SidebarProvider>
    </TooltipProvider>
  );
}
function Performance({
  data,
  device,
  group,
}: {
  data: Benchmark;
  device: string;
  group: string;
}) {
  const [q, setQ] = useState("");
  const rows = data.speed
    .filter(
      (r) =>
        r.device === device &&
        (group === "all" ||
          (device === "cpu"
            ? r.hardware.includes("AMD EPYC 9K84") &&
              r.threads === "16" &&
              r.workers === "24"
            : r.hardware === "NVIDIA GeForce RTX 5090" && r.workers === "2")) &&
        r.model.toLowerCase().includes(q.toLowerCase()),
    )
    .sort((a, b) => b.chars_per_second - a.chars_per_second);
  const top = rows.slice(0, 10),
    max = top[0]?.chars_per_second ?? 1;
  return (
    <>
      <Panel
        title="Throughput at a glance"
        subtitle={`${rows.length} measurements · characters per second · higher is better`}
      >
        <div className="speed-bars">
          {top.map((r, i) => (
            <div key={`${r.model}-${i}`}>
              <span>{r.model.replace("+cpu-speed", "")}</span>
              <div>
                <i
                  style={{
                    width: `${(r.chars_per_second / max) * 100}%`,
                    background: "var(--chart-1)",
                  }}
                />
              </div>
              <b className="mono">{n(r.chars_per_second)}</b>
            </div>
          ))}
        </div>
      </Panel>
      <Panel
        title="All speed measurements"
        subtitle="Every row retains its original hardware and workload. p50/p95 are amortized compute per row, not request latency."
      >
        <div className="table-controls">
          <div className="search-box">
            <Search size={16} />
            <input
              aria-label="Search speed measurements"
              placeholder="Search detector…"
              value={q}
              onChange={(e) => setQ(e.target.value)}
            />
          </div>
          <a className="action small" href="/data/speed.json" download>
            <Download size={14} />
            JSON
          </a>
        </div>
        <Table className="analysis-table performance-table">
          <TableHeader>
            <TableRow>
              {[
                "Detector / variant",
                "s / 10k chars ↓",
                "Chars / s ↑",
                "Rows / s",
                "p50 ms / row (amortized)",
                "p95 ms / row (amortized)",
                "Peak RSS MB",
                "Datasets",
                "Hardware",
                "Threads",
                "Workers",
              ].map((h) => (
                <TableHead key={h}>{h}</TableHead>
              ))}
            </TableRow>
          </TableHeader>
          <TableBody>
            {rows.map((r, i) => (
              <TableRow key={i}>
                <TableCell className="mono">{r.model}</TableCell>
                <TableCell className="number metric-emphasis">
                  {(10000 / r.chars_per_second).toFixed(3)}
                </TableCell>
                <TableCell className="number">
                  {n(r.chars_per_second)}
                </TableCell>
                <TableCell className="number">
                  {r.rows_per_second.toFixed(2)}
                </TableCell>
                <TableCell className="number">{n(r.p50_ms_reported)}</TableCell>
                <TableCell className="number">{n(r.p95_ms_reported)}</TableCell>
                <TableCell className="number">
                  {r.rss_mb === null ? "—" : n(r.rss_mb)}
                </TableCell>
                <TableCell className="number">{r.datasets}</TableCell>
                <TableCell className="hardware-cell">{r.hardware}</TableCell>
                <TableCell className="mono">{r.threads}</TableCell>
                <TableCell className="mono">{r.workers}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        {!rows.length && (
          <div className="empty">No matching speed measurements.</div>
        )}
      </Panel>
    </>
  );
}
function Downloads({
  files,
  onReport,
}: {
  files: { path: string; bytes: number }[];
  onReport: (p: string) => void;
}) {
  const [tab, setTab] = useState("reports"),
    [q, setQ] = useState("");
  const kind = (path: string) =>
    /\.(svg|png|jpe?g|webp)$/i.test(path)
      ? "figures"
      : /\.(json|csv)$/i.test(path)
        ? "data"
        : /\.md$/i.test(path) || !path.includes(".")
          ? "reports"
          : "other";
  const filtered = files.filter(
    (f) =>
      (tab === "all" || kind(f.path) === tab) &&
      f.path.toLowerCase().includes(q.toLowerCase()),
  );
  const guides = [
    ["results/overview.md", "Results overview"],
    ["results/ensemble.md", "Ensemble report"],
    ["results/by-dataset.md", "Dataset results"],
    ["docs/methodology.md", "Methodology"],
    ["docs/limitations.md", "Limitations"],
    ["docs/reproduce.md", "Reproduction guide"],
  ];
  return (
    <>
      <div className="download-featured">
        <div>
          <FileJson size={28} />
          <h2>Complete numeric snapshot</h2>
          <p>
            All systems, per-dataset counts, entity breakdowns, throughput and
            provenance.
          </p>
          <a
            className="action primary"
            href="/evidence/results/snapshot.json"
            download
          >
            <Download size={16} />
            Download snapshot · 12.1 MB
          </a>
        </div>
        <div>
          <Table2 size={28} />
          <h2>Analysis-ready exports</h2>
          <p>
            Exact counts from the snapshot, including coverage and
            training-overlap flags.
          </p>
          <div className="flex gap-3 flex-wrap">
            <a className="action" href="/data/all-results.csv" download>
              <Download size={16} />
              Results CSV
            </a>
            <a className="action" href="/data/categories.csv" download>
              <Download size={16} />
              Categories CSV
            </a>
          </div>
        </div>
      </div>
      <Panel
        title="Start with a report"
        subtitle="Six reader-facing documents before the full technical archive."
      >
        <div className="download-guides">
          {guides.map(([path, label]) => (
            <button
              className="action"
              key={path}
              onClick={() => onReport(path)}
            >
              <BookOpen size={15} />
              {label}
            </button>
          ))}
        </div>
      </Panel>
      <Panel
        title="Publication archive"
        subtitle={`${files.length} files and figures from this benchmark`}
      >
        <div className="table-controls">
          <Segmented
            value={tab}
            onChange={setTab}
            label="Archive file type"
            items={[
              { value: "reports", label: "Reports" },
              { value: "figures", label: "Figures" },
              { value: "data", label: "Data" },
              { value: "other", label: "Other" },
              { value: "all", label: "All files" },
            ]}
          />
          <div className="search-box">
            <Search size={16} />
            <input
              aria-label="Search reports and files"
              placeholder="Search files…"
              value={q}
              onChange={(e) => setQ(e.target.value)}
            />
          </div>
        </div>
        {!filtered.length ? (
          <div className="empty">No matching files.</div>
        ) : tab === "figures" ? (
          <div className="figure-grid">
            {filtered.map((f) => (
              <a
                className="figure-card"
                href={`/evidence/${f.path}`}
                target="_blank"
                rel="noreferrer"
                key={f.path}
              >
                <div>
                  <Image
                    src={`/evidence/${f.path}`}
                    alt={
                      f.path
                        .split("/")
                        .at(-1)
                        ?.replace(/\.(svg|png|jpe?g|webp)$/i, "")
                        .replaceAll("-", " ") ?? "Benchmark figure"
                    }
                    fill
                    sizes="(max-width: 767px) 100vw, (max-width: 1280px) 50vw, 33vw"
                    unoptimized
                  />
                </div>
                <span>
                  {f.path.split("/").at(-1)}
                  <ArrowUpRight size={15} />
                </span>
              </a>
            ))}
          </div>
        ) : (
          <Table className="analysis-table">
            <TableHeader>
              <TableRow>
                <TableHead>File</TableHead>
                <TableHead>Format</TableHead>
                <TableHead>Size</TableHead>
                <TableHead>
                  <span className="sr-only">Actions</span>
                </TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {filtered.map((f) => (
                <TableRow key={f.path}>
                  <TableCell>
                    <button
                      className="file-link"
                      onClick={() =>
                        f.path.endsWith(".md") || !f.path.includes(".")
                          ? onReport(f.path)
                          : window.open(
                              `/evidence/${f.path}`,
                              "_blank",
                              "noopener",
                            )
                      }
                    >
                      <Files size={17} />
                      <span>{f.path}</span>
                    </button>
                  </TableCell>
                  <TableCell>
                    <span className="subtle-badge">
                      {f.path.split(".").at(-1)?.toUpperCase().slice(0, 8)}
                    </span>
                  </TableCell>
                  <TableCell className="mono dim">
                    {f.bytes > 1000000
                      ? (f.bytes / 1000000).toFixed(1) + " MB"
                      : (f.bytes / 1000).toFixed(1) + " KB"}
                  </TableCell>
                  <TableCell>
                    <a
                      className="icon-button"
                      href={`/evidence/${f.path}`}
                      download
                      aria-label={`Download ${f.path}`}
                    >
                      <Download size={16} />
                    </a>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </Panel>
    </>
  );
}
