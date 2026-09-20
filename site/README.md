# Benchmark website

This directory contains the public Next.js website for the PII & Secrets Detection Benchmark. It renders real routes for every main view, detector and dataset, plus canonical metadata, `robots.txt`, `sitemap.xml` and Dataset JSON-LD.

## Local development

Run commands from this directory. The pre-scripts copy the current benchmark publication from the repository root and regenerate the browser-ready data.

```sh
pnpm install --frozen-lockfile
pnpm dev
```

Validation:

```sh
pnpm typecheck
pnpm build
```

`public/data/` and `public/evidence/` are generated and ignored. Edit benchmark results and documentation in the repository root, then rebuild the site.

## Vercel setup

1. Import `Quakeer444/pii-secrets-benchmark` as a Vercel project.
2. Set **Root Directory** to `site` and keep the detected **Next.js** framework preset.
3. Keep **Include source files outside of the Root Directory in the Build Step** enabled. The site copies the authoritative benchmark publication from the repository root before every build.
4. Keep **Skip deployment** disabled so changes to benchmark results also trigger a website deployment.
5. Enable Vercel system environment variables. `VERCEL_PROJECT_PRODUCTION_URL` supplies the canonical origin until a custom domain is attached.
6. After adding the final domain, set `SITE_URL=https://your-domain.example` for Production and Preview, then redeploy.

Every push to the production branch creates a production deployment; other branches and pull requests receive preview deployments.

## Search launch checklist

After the production domain is final:

1. Verify `/robots.txt` and `/sitemap.xml` use the production origin.
2. Add the domain property in Google Search Console.
3. Submit `/sitemap.xml` in the Sitemaps report.
4. Inspect `/leaderboard`, `/datasets` and one `/datasets/<id>` page.
5. Validate Dataset JSON-LD with Google's Rich Results Test.

Do not submit preview deployment URLs. Vercel marks preview deployments as non-indexable by default.
