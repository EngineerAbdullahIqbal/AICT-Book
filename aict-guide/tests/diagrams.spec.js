// Contract C2: diagrams on the book start page (moved from / to /start, site-design D-05).
// See specs/module-01-computer-basics/contracts/page-contracts.md
import {test} from '@playwright/test';
import {
  expectAtLeastOneDiagram,
  expectDiagramsAccessible,
  expectDiagramsInWords,
} from './diagram-checks.js';

test('home-diagram: the home page draws at least one diagram', async ({page}) => {
  await page.goto('/start');
  await expectAtLeastOneDiagram(page);
});

test('diagram-accessible: every home diagram has an accessible title and description', async ({
  page,
}) => {
  await page.goto('/start');
  await expectAtLeastOneDiagram(page);
  await expectDiagramsAccessible(page);
});

test('diagram-in-words: every home diagram is followed by "Diagram in words:"', async ({page}) => {
  await page.goto('/start');
  await expectAtLeastOneDiagram(page);
  await expectDiagramsInWords(page);
});
