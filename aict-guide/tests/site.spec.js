// Contract C1: the site as a whole.
// See specs/module-01-computer-basics/contracts/page-contracts.md
import fs from 'node:fs';
import path from 'node:path';
import {test, expect} from '@playwright/test';
import {MODULES} from './modules.js';

const BOOK_TITLE = 'AICT Course Guide';
// `npm test` runs from aict-guide/, and the webServer command builds into build/.
const BUILD_DIR = path.join(process.cwd(), 'build');

// Every folder path inside build/ (relative), for checking what was generated.
function buildFolders(dir = BUILD_DIR, prefix = '') {
  return fs
    .readdirSync(dir, {withFileTypes: true})
    .filter((entry) => entry.isDirectory())
    .flatMap((entry) => {
      const rel = path.join(prefix, entry.name);
      return [rel, ...buildFolders(path.join(dir, entry.name), rel)];
    });
}

test('site-title: the site is named AICT Course Guide', async ({page}) => {
  await page.goto('/');
  await expect(page).toHaveTitle(new RegExp(BOOK_TITLE));
  // `.navbar__title` is the classic theme's navbar title element (Infima class).
  await expect(page.locator('.navbar__title')).toHaveText(BOOK_TITLE);
});

// The book's first doc page moved from / to /start when the front page was added
// (specs/site-design/spec.md, D-02).
const START_URL = '/start';
const START_TITLE = 'Start Here';

test('book-start: /start is the first book page (a doc page)', async ({page}) => {
  await page.goto(START_URL);
  // Doc pages render inside <article> next to the docs sidebar
  // (`theme-doc-sidebar-container` is a stable theme class name).
  await expect(page.locator('article h1')).toHaveText(START_TITLE);
  await expect(page.locator('.theme-doc-sidebar-container')).toBeVisible();
});

test('no-blog: the blog is not built and not linked', async ({page}) => {
  expect(fs.existsSync(path.join(BUILD_DIR, 'blog'))).toBe(false);
  await page.goto(START_URL);
  await expect(page.locator('.navbar').getByRole('link', {name: 'Blog'})).toHaveCount(0);
});

test('no-tutorial: the sample tutorial is not built and not in the sidebar', async ({page}) => {
  const tutorialFolders = buildFolders().filter((folder) =>
    /tutorial-(basics|extras)/.test(folder),
  );
  expect(tutorialFolders).toEqual([]);
  await page.goto(START_URL);
  const sidebar = page.locator('.theme-doc-sidebar-container');
  await expect(sidebar).toBeVisible();
  await expect(sidebar).not.toContainText('Tutorial');
});

// Top-level sidebar entries: label + link of the first link in each top-level item.
// Works whether a module is a plain link or an expandable category.
async function topLevelSidebarItems(page) {
  await page.goto(START_URL);
  const menu = page.locator('.theme-doc-sidebar-container ul.theme-doc-sidebar-menu');
  await expect(menu).toBeVisible();
  return menu.evaluate((ul) =>
    [...ul.children].map((li) => {
      const link = li.querySelector('a');
      return {label: link?.textContent?.trim() ?? '', href: link?.getAttribute('href') ?? ''};
    }),
  );
}

test('sixteen-modules: the sidebar shows Start Here then the 16 modules in order', async ({
  page,
}) => {
  const labels = (await topLevelSidebarItems(page)).map((item) => item.label);
  expect(labels).toEqual([START_TITLE, ...MODULES]);
});

test('module-placeholders: each module link opens a page titled with its module name', async ({
  page,
}) => {
  const modules = (await topLevelSidebarItems(page)).filter((item) =>
    item.label.startsWith('Module '),
  );
  expect(modules.map((m) => m.label)).toEqual(MODULES);
  for (const {label, href} of modules) {
    await page.goto(href);
    await expect(page.locator('article h1'), `page for "${label}"`).toHaveText(label);
  }
});
