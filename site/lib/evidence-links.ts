export type EvidenceLink = {
  kind: "anchor" | "document" | "download" | "external";
  href: string;
  path?: string;
};

export function evidenceLink(href: string, currentPath: string): EvidenceLink {
  if (href.startsWith("#")) return { kind: "anchor", href };
  if (/^https?:\/\//i.test(href)) return { kind: "external", href };
  const resolved = new URL(href, `https://evidence.local/${currentPath}`);
  const path = resolved.pathname.replace(/^\//, "");
  const target = `/evidence/${path}${resolved.hash}`;
  return /(^|\/)LICENSE$|\.md$/i.test(path)
    ? { kind: "document", href: target, path: `${path}${resolved.hash}` }
    : { kind: "download", href: target, path };
}

export function markdownHeadingId(text: string, seen: Map<string, number>) {
  const base =
    text
      .toLowerCase()
      .normalize("NFKC")
      .replace(/[^\p{L}\p{N}\s-]/gu, "")
      .trim()
      .replace(/\s+/g, "-") || "section";
  const count = seen.get(base) ?? 0;
  seen.set(base, count + 1);
  return count ? `${base}-${count}` : base;
}
