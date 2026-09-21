import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  outputDir: "../.local/playwright",
  reporter: [["line"], ["html", { outputFolder: "../.local/playwright-report", open: "never" }]],
  use: {
    baseURL: "http://127.0.0.1:3101",
    launchOptions: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH
      ? { executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH }
      : {},
    screenshot: "only-on-failure",
    trace: "retain-on-failure",
  },
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }],
  webServer: {
    command: "./node_modules/.bin/next start -p 3101",
    url: "http://127.0.0.1:3101/leaderboard",
    reuseExistingServer: !process.env.CI,
    timeout: 120_000,
  },
});
