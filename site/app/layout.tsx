import type { Metadata } from "next";
import { ThemeProvider } from "next-themes";
import { DEFAULT_DESCRIPTION, GITHUB_URL, SITE_NAME, SITE_URL } from "@/lib/seo";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "PII & Secrets Detection Benchmark",
    template: `%s | ${SITE_NAME}`
  },
  description: DEFAULT_DESCRIPTION,
  applicationName: SITE_NAME,
  authors: [{ name: "Quakeer444", url: "https://github.com/Quakeer444" }],
  creator: "Quakeer444",
  publisher: "Quakeer444",
  keywords: ["PII detection benchmark", "secret detection benchmark", "PII detector comparison"],
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg"
  },
  alternates: { canonical: "/leaderboard" },
  openGraph: {
    type: "website",
    siteName: SITE_NAME,
    title: "PII & Secrets Detection Benchmark",
    description: DEFAULT_DESCRIPTION,
    url: "/leaderboard",
    images: [{ url: "/og.png", width: 1280, height: 640, alt: "PII & Secrets Benchmark leaderboard" }]
  },
  twitter: {
    card: "summary_large_image",
    title: "PII & Secrets Detection Benchmark",
    description: DEFAULT_DESCRIPTION,
    images: ["/og.png"]
  },
  other: {
    "source-code": GITHUB_URL
  }
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="antialiased">
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          enableSystem={false}
          storageKey="pii-bench-theme"
          disableTransitionOnChange
        >
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
