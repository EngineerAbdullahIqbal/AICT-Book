// @ts-check
// Playwright config for the AICT Course Guide.
// Tests always run against a fresh production build, so every run is also a
// broken-link check (see specs/module-01-computer-basics/research.md, R9).
import {defineConfig, devices} from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  reporter: 'list',
  use: {
    baseURL: 'http://localhost:3100',
  },
  projects: [
    {
      name: 'chromium',
      use: {...devices['Desktop Chrome']},
    },
  ],
  // Port 3100 so tests never collide with the dev server on port 3000.
  webServer: {
    command: 'npm run build && npm run serve -- --port 3100 --no-open',
    url: 'http://localhost:3100',
    reuseExistingServer: false,
    // A production build can take a while.
    timeout: 300 * 1000,
  },
});
