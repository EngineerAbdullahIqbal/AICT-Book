// Contract C4: the Module 1 overview page.
// See specs/module-01-computer-basics/contracts/page-contracts.md
import {test, expect} from '@playwright/test';
import {MODULE_LESSONS} from './lessons.js';

const LESSONS = MODULE_LESSONS['module-01-computer-basics'];
import {readSections, section, firstBlock, normaliseUrl} from './page-sections.js';

const OVERVIEW_URL = '/module-01-computer-basics/';

test.describe('Module 1 overview', () => {
  test.beforeEach(async ({page}) => {
    await page.goto(OVERVIEW_URL);
  });

  test('overview-title', async ({page}) => {
    await expect(page.locator('article h1')).toHaveText('Module 1: Computer Basics');
  });

  test('overview-outcomes', async ({page}) => {
    const outcomes = section(await readSections(page), 'Learning Outcomes');
    const list = firstBlock(outcomes, ['UL', 'OL']);
    expect(list?.items.length).toBe(9);
  });

  test('overview-lesson-links', async ({page}) => {
    const lessons = section(await readSections(page), 'Lessons');
    expect(lessons, 'a "Lessons" section exists').toBeTruthy();
    const links = lessons.blocks.flatMap((b) => b.links).map(normaliseUrl);
    expect(links).toEqual(LESSONS.map((l) => normaliseUrl(l.url)));
    for (const lesson of LESSONS) {
      await page.goto(lesson.url);
      await expect(page.locator('article h1')).toHaveText(lesson.title);
    }
  });
});
