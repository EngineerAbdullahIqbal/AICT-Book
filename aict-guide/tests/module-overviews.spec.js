// Contract C4 for every module that has lessons: the overview page lists its lessons in
// order, and each link opens the right lesson. Module 1's extra checks are in module-01.spec.js.
import {test, expect} from '@playwright/test';
import {MODULE_LESSONS} from './lessons.js';
import {readSections, section, firstBlock, normaliseUrl} from './page-sections.js';

const OVERVIEWS = [
  {module: 'module-04-ms-word', title: 'Module 4: MS Word', outcomes: 13},
  {module: 'module-07-ms-excel', title: 'Module 7: MS Excel', outcomes: 13},
];

for (const {module, title, outcomes} of OVERVIEWS) {
  const lessons = MODULE_LESSONS[module];
  test.describe(`${title} overview`, () => {
    test.beforeEach(async ({page}) => {
      await page.goto(`/${module}/`);
    });

    test('overview-outcomes', async ({page}) => {
      await expect(page.locator('article h1')).toHaveText(title);
      const list = firstBlock(section(await readSections(page), 'Learning Outcomes'), ['UL', 'OL']);
      expect(list?.items.length).toBe(outcomes);
    });

    test('overview-lesson-links', async ({page}) => {
      const sec = section(await readSections(page), 'Lessons');
      expect(sec, 'a "Lessons" section exists').toBeTruthy();
      const links = sec.blocks.flatMap((b) => b.links).map(normaliseUrl);
      expect(links).toEqual(lessons.map((l) => normaliseUrl(l.url)));
    });
  });
}
