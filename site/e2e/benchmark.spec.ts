import { expect, test } from "@playwright/test";

test("deep links preserve the complete analysis through navigation", async ({ page }) => {
  await page.goto("/leaderboard?lang=ru&task=pii&compare=model%3Agliner2-fastino%2Cmodel%3Applx&difficulty=Hard&category=contacts&domainQuery=fast");
  await expect(page.getByLabel("Current analysis scope")).toContainText("Russian");
  await expect(page.getByLabel("Current analysis scope")).toContainText("PII datasets");
  await page.getByRole("link", { name: "Compare detectors" }).click();
  await expect(page).toHaveURL(/\/compare\?.*lang=ru/);
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
  await expect(page).toHaveURL(/\/methodology$/);

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
