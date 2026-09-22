import { expect, test } from "@playwright/test";

test("deep links preserve the complete analysis through navigation", async ({ page }) => {
  await page.goto("/leaderboard?lang=ru&task=pii&compare=model%3Agliner2-fastino%2Cmodel%3Applx&difficulty=Hard&category=contacts&domainQuery=fast");
  // Leaderboard filters scope only its table; the dashboard scope stays page-wide.
  await expect(page.getByRole("combobox", { name: "Language" })).toContainText("Russian");
  await expect(page.getByLabel("Current analysis scope")).toContainText("All languages");
  await expect(page.getByLabel("Current analysis scope")).toContainText("PII + secrets");
  await page.getByRole("link", { name: "Compare detectors" }).click();
  await expect(page).toHaveURL(/\/compare\?.*lang=ru/);
  await expect(page.getByLabel("Current analysis scope")).toContainText("Russian");
  await expect(page).toHaveURL(/difficulty=Hard/);
  await expect(page.getByText("shared datasets")).toBeVisible();
  await page.goBack();
  await expect(page).toHaveURL(/\/leaderboard\?.*lang=ru/);
  await page.getByRole("link", { name: "Methodology" }).click();
  await expect(page).toHaveURL(/\/methodology\?.*category=contacts/);
});

test("filtered export contains exact values and provenance", async ({ page }) => {
  await page.goto("/leaderboard?lang=en&task=pii");
  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Download current CSV" }).click();
  const file = await download;
  const stream = await file.createReadStream();
  let csv = "";
  for await (const chunk of stream!) csv += chunk.toString();
  expect(file.suggestedFilename()).toBe("pii-benchmark-filtered.csv");
  expect(csv).toContain('"snapshotHash"');
  expect(csv).toContain('"scopeDatasetIds"');
  expect(csv).toContain('"hit"');
  expect(csv).toContain('"detected"');
});

test("evidence documents navigate inside one viewer", async ({ page }) => {
  await page.goto("/methodology");
  await page.getByRole("button", { name: "Full methodology" }).click();
  await expect(page.getByRole("heading", { name: "methodology.md" })).toBeVisible();
  await page.getByRole("link", { name: "limitations", exact: true }).click();
  await expect(page.getByRole("heading", { name: "limitations.md" })).toBeVisible();
  await page.getByRole("button", { name: "Previous report" }).click();
  await expect(page.getByRole("heading", { name: "methodology.md" })).toBeVisible();
  await expect(page).toHaveURL(/\/methodology(?:\?|$)/);

  await page.goto("/downloads");
  await page.getByLabel("Search reports and files").fill("results/by-language.md");
  await page.getByRole("button", { name: /results\/by-language\.md/ }).click();
  await page.getByRole("link", { name: "scanner status table" }).click();
  await expect(page.getByRole("heading", { name: "reproduce.md" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Scanner adapter status" })).toBeInViewport();
});

test("compact layouts retain local scrolling and styled difficulty indicators", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/leaderboard");
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth)).toBe(true);
  const meters = page.locator(".difficulty-meter");
  await expect(meters.first()).toBeVisible();
  const styles = await meters.first().evaluate((element) => {
    const fill = element.firstElementChild as HTMLElement;
    return { track: getComputedStyle(element).backgroundColor, fill: getComputedStyle(fill).backgroundColor, width: fill.getBoundingClientRect().width };
  });
  expect(styles.track).not.toBe(styles.fill);
  expect(styles.width).toBeGreaterThan(0);
  await page.goto("/datasets");
  const badge = page.locator(".difficulty-badge").first();
  await expect(badge).toBeVisible();
  expect(await badge.evaluate((element) => getComputedStyle(element).backgroundColor)).not.toBe("rgba(0, 0, 0, 0)");
});

test("scanner status stays with the profile, comparison and export", async ({ page }) => {
  await page.goto("/detectors/gitleaks");
  await expect(page.getByText("corrected rerun · capture-v2 · 9 runs · 32 unresolved spans")).toBeVisible();
  await expect(page.getByText(/Full scanner inventory/)).toBeVisible();
  await expect(page.getByText(/10 runs · 38 unresolved spans/)).toBeVisible();

  await page.goto("/detectors/trufflehog");
  await expect(page.getByText("historical pre-fix · 3 runs · 0 unresolved spans")).toBeVisible();

  await page.goto("/compare?compare=model%3Agitleaks%2Cmodel%3Atrufflehog&task=secrets");
  await expect(page.getByRole("status")).toContainText("different scanner mapping policies");
  await expect(page.getByRole("status")).toContainText("trufflehog");
  await expect(page.getByRole("heading", { name: "gitleaks" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "trufflehog" })).toHaveCount(0);
  await page.getByRole("checkbox", { name: "Include historical pre-fix results" }).click();
  await expect(page.getByRole("heading", { name: "trufflehog" })).toBeVisible();
  await expect(page.getByText("historical pre-fix · 3 runs · 0 unresolved spans")).toBeVisible();

  await page.goto("/leaderboard?coverage=all&q=gitleaks&task=secrets");
  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Download current CSV" }).click();
  const file = await download;
  const stream = await file.createReadStream();
  let csv = "";
  for await (const chunk of stream!) csv += chunk.toString();
  const header = csv.split("\n")[0];
  const names = header.split(",").map((cell) => cell.slice(1, -1));
  expect(new Set(names).size).toBe(names.length);
  expect(names).toContain("filter_family");
  expect(names).toContain("system_family");
  expect(names).not.toContain("family");
  expect(csv).toContain("corrected-rerun");
  expect(csv).toContain("capture-v2");
});

test("all tasks survive reload and navigation on thematic pages", async ({ page, context }) => {
  await context.grantPermissions(["clipboard-read", "clipboard-write"]);
  const task = page.getByRole("combobox", { name: "Sensitive data type", exact: true });
  await page.goto("/benchmarks/pii-detection");
  await task.click();
  await page.getByRole("option", { name: "Personal data + secrets" }).click();
  await expect(page).toHaveURL(/\/benchmarks\/pii-detection\?.*task=all/);
  await page.getByRole("button", { name: "Copy link" }).first().click();
  await expect.poll(() => page.evaluate(() => navigator.clipboard.readText())).toContain("task=all");
  await page.reload();
  await expect(task).toContainText("Personal data + secrets");
  await page.getByRole("link", { name: "Leaderboard" }).click();
  await expect(page).toHaveURL(/\/leaderboard\?.*task=all/);
  await page.goBack();
  await expect(page).toHaveURL(/\/benchmarks\/pii-detection\?.*task=all/);
  await expect(task).toContainText("Personal data + secrets");

  await page.goto("/benchmarks/secrets-detection");
  await task.click();
  await page.getByRole("option", { name: "Personal data + secrets" }).click();
  await expect(page).toHaveURL(/\/benchmarks\/secrets-detection\?.*task=all/);
  await page.reload();
  await expect(task).toContainText("Personal data + secrets");
});

test("comparison CSV does not inherit unused leaderboard filters", async ({ page }) => {
  await page.goto("/compare?sort=fullyHidden&dir=asc&q=NO_MATCH_EXPECTED");
  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Download comparison CSV" }).click();
  const file = await download;
  const stream = await file.createReadStream();
  let csv = "";
  for await (const chunk of stream!) csv += chunk.toString();
  expect(csv).toContain('"compare"');
  expect(csv).toContain('"selection"');
  expect(csv).toContain('"model:gliner2-fastino"');
  expect(csv).not.toContain("NO_MATCH_EXPECTED");
  expect(csv).not.toContain('"ascending"');
  expect(csv).not.toContain('"fullyHidden","ascending"');
});

test("extra masking example and composition revisions match their contracts", async ({ page }) => {
  await page.goto("/methodology");
  await expect(page.getByText("5 masked characters / 11 characters")).toBeVisible();
  await expect(page.getByText("The email row above is not in this denominator.")).toBeVisible();
  await expect(page.getByText("Masked outside the labeled value")).toHaveCount(0);

  await page.goto("/ensembles");
  await page.getByRole("button", { name: "pplx+fastino+bardsai+mmbert", exact: true }).click();
  await expect(page.getByText("Member revisions")).toBeVisible();
  await expect(page.getByText("f1f90a53823f5df0a1344c1e137d9fffdaab54d6")).toBeVisible();
  await expect(page.getByText("c153999da5f4c509df4322b0c6a1baf3d2c284d7")).toBeVisible();
  await expect(page.getByText("0e72e19f030ed4e661b1673e549af8e0dd176386")).toBeVisible();
  await expect(page.getByText("d22c818cf9f2a8bfbbed8508cb417dc16a1ba3ea")).toBeVisible();
  await expect(page.getByText("Pinned revision / version")).toHaveCount(0);
  await expect(page.getByText(/identifies the published ensemble/)).toBeVisible();
});
