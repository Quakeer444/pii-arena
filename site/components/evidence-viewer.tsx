"use client";
import React, { useEffect, useState } from "react";
import {
  ArrowLeft,
  Download,
  ExternalLink,
  FileText,
  LoaderCircle,
  RotateCw,
} from "lucide-react";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";
import {
  Table,
  TableBody,
  TableRow,
  TableCell,
  TableHead,
  TableHeader,
} from "@/components/ui/table";
import { evidenceLink, markdownHeadingId } from "@/lib/evidence-links";

export function EvidenceViewer({
  path,
  onClose,
  onNavigate,
}: {
  path: string | null;
  onClose: () => void;
  onNavigate: (path: string) => void;
}) {
  const [text, setText] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [retry, setRetry] = useState(0);
  const [history, setHistory] = useState<string[]>([]);
  const [documentPath, fragment = ""] = (path ?? "").split("#", 2);
  useEffect(() => {
    setText("");
    setError("");
    if (!path) {
      setHistory([]);
      return;
    }
    setLoading(true);
    const c = new AbortController();
    fetch(`/evidence/${documentPath}`, { signal: c.signal })
      .then((r) => {
        if (!r.ok) throw Error("This report could not be loaded.");
        return r.text();
      })
      .then(setText)
      .catch((e) => {
        if (e.name !== "AbortError") setError(e.message);
      })
      .finally(() => {
        if (!c.signal.aborted) setLoading(false);
      });
    return () => c.abort();
  }, [path, documentPath, retry]);
  useEffect(() => {
    if (!text || !fragment) return;
    document
      .getElementById(decodeURIComponent(fragment))
      ?.scrollIntoView({ block: "start" });
  }, [text, fragment]);
  const navigate = (next: string) => {
    if (path) setHistory((previous) => [...previous, path]);
    onNavigate(next);
  };
  const back = () =>
    setHistory((previous) => {
      const next = [...previous];
      const target = next.pop();
      if (target) onNavigate(target);
      return next;
    });
  return (
    <Sheet
      open={!!path}
      onOpenChange={(open) => {
        if (!open) onClose();
      }}
    >
      <SheetContent className="evidence-sheet">
        <SheetHeader>
          <SheetTitle className="flex gap-3 items-center">
            <FileText size={20} />
            {documentPath.split("/").at(-1)}
          </SheetTitle>
          <SheetDescription>
            Original publication report · Frozen experiment 09 Sep 2026
          </SheetDescription>
        </SheetHeader>
        <div className="px-6 pb-3 border-b border-border flex gap-2">
          {history.length > 0 && (
            <button className="action small" onClick={back}>
              <ArrowLeft size={15} />
              Previous report
            </button>
          )}
          <a
            className="action small"
            href={`/evidence/${documentPath}`}
            download
          >
            <Download size={15} />
            Download source
          </a>
        </div>
        <div className="report-content">
          {error ? (
            <div role="alert">
              <p>{error}</p>
              <button
                className="action small"
                onClick={() => setRetry((value) => value + 1)}
              >
                <RotateCw size={15} />
                Retry
              </button>
            </div>
          ) : loading ? (
            <p className="flex gap-2">
              <LoaderCircle className="animate-spin" />
              Loading report…
            </p>
          ) : text ? (
            <Markdown
              text={text}
              path={documentPath}
              onNavigate={navigate}
            />
          ) : (
            <p>This report is empty.</p>
          )}
        </div>
      </SheetContent>
    </Sheet>
  );
}
function inline(
  text: string,
  path: string,
  onNavigate: (path: string) => void,
): React.ReactNode[] {
  return text
    .split(/(\*\*[^*]+\*\*|`[^`]+`|!?\[[^\]]*\]\([^)]+\))/g)
    .map((part, i) => {
      if (part.startsWith("**"))
        return <strong key={i}>{part.slice(2, -2)}</strong>;
      if (part.startsWith("`")) return <code key={i}>{part.slice(1, -1)}</code>;
      const link = part.match(/^(!?)\[([^\]]*)\]\(([^)]+)\)$/);
      if (link) {
        const target = evidenceLink(link[3], path);
        if (target.kind === "anchor")
          return (
            <a
              key={i}
              href={target.href}
              onClick={(event) => {
                event.preventDefault();
                document
                  .getElementById(target.href.slice(1))
                  ?.scrollIntoView({ block: "start" });
              }}
            >
              {link[2]}
            </a>
          );
        if (target.kind === "document")
          return (
            <a
              key={i}
              href={target.href}
              onClick={(event) => {
                event.preventDefault();
                onNavigate(target.path!);
              }}
            >
              {link[2]}
            </a>
          );
        return (
          <a key={i} href={target.href} target="_blank" rel="noreferrer">
            {link[2]} <ExternalLink size={12} className="inline" />
          </a>
        );
      }
      return part;
    });
}
function Markdown({
  text,
  path,
  onNavigate,
}: {
  text: string;
  path: string;
  onNavigate: (path: string) => void;
}) {
  const lines = text.split("\n");
  const blocks: React.ReactNode[] = [];
  const headings = new Map<string, number>();
  for (let i = 0; i < lines.length; i++) {
    const l = lines[i];
    if (
      !l.trim() ||
      l.startsWith("<!--") ||
      l.startsWith("<details") ||
      l.startsWith("</details")
    )
      continue;
    if (l.startsWith("```")) {
      const code = [];
      while (++i < lines.length && !lines[i].startsWith("```"))
        code.push(lines[i]);
      blocks.push(
        <pre key={i}>
          <code>{code.join("\n")}</code>
        </pre>,
      );
      continue;
    }
    if (l.startsWith("|") && lines[i + 1]?.match(/^\|[\s:|-]+\|/)) {
      const cells = (x: string) =>
        x
          .trim()
          .replace(/^\||\|$/g, "")
          .split("|")
          .map((x) => x.trim());
      const heads = cells(l);
      i += 2;
      const rows = [];
      while (i < lines.length && lines[i].startsWith("|"))
        rows.push(cells(lines[i++]));
      i--;
      blocks.push(
        <Table key={i}>
          <TableHeader>
            <TableRow>
              {heads.map((h, j) => (
                <TableHead key={j}>{inline(h, path, onNavigate)}</TableHead>
              ))}
            </TableRow>
          </TableHeader>
          <TableBody>
            {rows.map((r, k) => (
              <TableRow key={k}>
                {r.map((c, j) => (
                  <TableCell key={j}>{inline(c, path, onNavigate)}</TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>,
      );
      continue;
    }
    const heading = l.match(/^(#{1,6}) (.*)/);
    if (heading) {
      const id = markdownHeadingId(heading[2], headings);
      blocks.push(
        React.createElement(
          `h${heading[1].length}`,
          { key: i, id },
          inline(heading[2], path, onNavigate),
        ),
      );
      continue;
    }
    if (l.startsWith("<summary>")) {
      blocks.push(<h3 key={i}>{l.replace(/<[^>]*>/g, "")}</h3>);
      continue;
    }
    if (l.match(/^[-*] /)) {
      blocks.push(
        <p className="report-bullet" key={i}>
          {inline(l.slice(2), path, onNavigate)}
        </p>,
      );
      continue;
    }
    blocks.push(<p key={i}>{inline(l, path, onNavigate)}</p>);
  }
  return <>{blocks}</>;
}
