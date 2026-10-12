// The front page at / (specs/site-design/spec.md, D-01 to D-06).
import fs from 'node:fs';
import path from 'node:path';
import {test, expect} from '@playwright/test';
import {MODULES} from './modules.js';
import {MODULE_LESSONS} from './lessons.js';

const BUILD_DIR = path.join(process.cwd(), 'build');

// Module folder names in course order, e.g. "module-04-ms-word".
const docsDir = path.join(process.cwd(), 'docs');
const MODULE_FOLDERS = fs
  .readdirSync(docsDir)
  .filter((name) => /^module-\d\d-/.test(name))
  .sort();

test.describe('Front page', () => {
  test.beforeEach(async ({page}) => {
    await page.goto('/');
  });

  test('front-hero: book title and coaching center', async ({page}) => {
    await expect(page.locator('main h1')).toHaveText('AICT Course Guide');
    await expect(page.locator('main')).toContainText('Global Coaching Center');
    // The front page is not a doc page: no docs sidebar.
    await expect(page.locator('.theme-doc-sidebar-container')).toHaveCount(0);
  });

  test('front-start-reading: Start Reading opens the book start page', async ({page}) => {
    await page.getByRole('link', {name: /Start Reading/}).first().click();
    await expect(page).toHaveURL(/\/start$/);
    await expect(page.locator('article h1')).toHaveText('Start Here');
  });

  test('front-module-cards: 16 cards in course order, each with the right status', async ({
    page,
  }) => {
    const cards = page.locator('[data-module-card]');
    await expect(cards).toHaveCount(16);
    for (let i = 0; i < 16; i++) {
      const card = cards.nth(i);
      const folder = MODULE_FOLDERS[i];
      const ready = (MODULE_LESSONS[folder] ?? []).length > 0;
      await expect(card).toContainText(MODULES[i].replace(/^Module \d+: /, ''));
      await expect(card).toContainText(ready ? 'Ready' : 'Coming soon');
      const href = await card.getAttribute('href');
      expect(href?.replace(/\/$/, '')).toBe(`/${folder}`);
    }
  });

  test('front-module-links: every module card opens its module page', async ({page}) => {
    const hrefs = await page
      .locator('[data-module-card]')
      .evaluateAll((els) => els.map((el) => el.getAttribute('href')));
    expect(hrefs).toHaveLength(16);
    for (let i = 0; i < hrefs.length; i++) {
      await page.goto(hrefs[i]);
      await expect(page.locator('article h1')).toHaveText(MODULES[i]);
    }
  });
});

test('no-sample-images: no Docusaurus sample images are built or used', async ({page}) => {
  const images = fs.readdirSync(path.join(BUILD_DIR, 'img'));
  expect(images.filter((name) => /docusaurus|undraw|^logo\.svg$/.test(name))).toEqual([]);
  await page.goto('/');
  const logo = await page.locator('.navbar__logo img').first().getAttribute('src');
  expect(logo).toMatch(/aict-logo\.svg$/);
});
