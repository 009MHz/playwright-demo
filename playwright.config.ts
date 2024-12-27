import { defineConfig, devices } from '@playwright/test';

const browserName = process.env.BROWSER || 'chromium';
const isHeadless = process.env.HEADLESS === 'true';
const retries = process.env.CI ? 2 : 0;
const workers = process.env.CI ? 1 : undefined;

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: retries,
  workers: workers,
  reporter: [
    ['list'],
    ['allure-playwright',
      {
        resultsDir: "reports",
        detail: false,
        suiteTitle: true
      }
    ],
  ],
  use: {
    headless: isHeadless, // Dynamically set headless mode
    trace: 'on-first-retry',
  },
  projects: [
    // Dynamically select the browser based on the BROWSER environment variable
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'], headless: isHeadless },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'], headless: isHeadless },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'], headless: isHeadless },
    },
  ].filter((project) => project.name === browserName || browserName === 'all'), // Run the selected browser or all
  // Optional: Add a web server configuration if required
  // webServer: {
  //   command: 'npm run start',
  //   url: 'http://127.0.0.1:3000',
  //   reuseExistingServer: !process.env.CI,
  // },
});
