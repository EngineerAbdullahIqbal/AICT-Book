// Contract C3: every lesson page follows the lesson template (data-model.md).
// See specs/module-01-computer-basics/contracts/page-contracts.md
import {test, expect} from '@playwright/test';
import {LESSONS} from './lessons.js';
import {readSections, section, firstBlock} from './page-sections.js';
import {
  expectAtLeastOneDiagram,
  expectDiagramsAccessible,
  expectDiagramsInWords,
} from './diagram-checks.js';

const SECTION_ORDER = [
  'Goal',
  'Why It Matters',
  'Key Terms',
  'Teacher Demo',
  'Student Task',
  'Check Questions',
  'Common Mistakes',
  'Sources',
];

for (const lesson of LESSONS) {
  test.describe(lesson.title, () => {
    test.beforeEach(async ({page}) => {
      await page.goto(lesson.url);
    });

    test('lesson-title', async ({page}) => {
      await expect(page.locator('article h1')).toHaveText(lesson.title);
    });

    test('sections-in-order', async ({page}) => {
      const headings = (await readSections(page)).map((s) => s.heading);
      expect(headings).toEqual(SECTION_ORDER);
    });

    test('goal-sentence', async ({page}) => {
      const goal = firstBlock(section(await readSections(page), 'Goal'), ['P']);
      expect(goal?.text.trim()).toMatch(/^By the end of this lesson, you can /);
    });

    test('has-diagram', async ({page}) => {
      await expectAtLeastOneDiagram(page);
      await expectDiagramsAccessible(page);
      await expectDiagramsInWords(page);
    });

    test('key-terms-table', async ({page}) => {
      const table = firstBlock(section(await readSections(page), 'Key Terms'), ['TABLE']);
      // The Urdu column is optional (book-spec v1.1). If present, every Urdu cell is marked.
      const headers = table?.headers.map((h) => h.trim());
      const hasUrdu = headers?.length === 3;
      expect(headers).toEqual(
        hasUrdu ? ['Term', 'Simple meaning', 'Urdu meaning'] : ['Term', 'Simple meaning'],
      );
      expect(table.rows.length).toBeGreaterThanOrEqual(3);
      expect(table.rows.length).toBeLessThanOrEqual(8);
      if (hasUrdu) {
        table.rows.forEach((row, i) => {
          expect(row[2]?.hasUrdu, `row ${i + 1} Urdu cell has lang="ur"`).toBe(true);
        });
      }
    });

    test('student-task-end', async ({page}) => {
      const list = firstBlock(section(await readSections(page), 'Student Task'), ['OL']);
      expect(list?.items.length).toBeGreaterThan(0);
      expect(list.items.at(-1).text).toContain('Show your teacher:');
    });

    test('three-questions', async ({page}) => {
      const list = firstBlock(section(await readSections(page), 'Check Questions'), ['OL']);
      expect(list?.items.length).toBe(3);
      list.items.forEach((item, i) => {
        expect(item.text, `question ${i + 1} has a model answer`).toContain('Answer:');
      });
    });

    test('common-mistakes', async ({page}) => {
      const list = firstBlock(section(await readSections(page), 'Common Mistakes'), ['UL', 'OL']);
      expect(list?.items.length).toBeGreaterThanOrEqual(2);
      expect(list.items.length).toBeLessThanOrEqual(5);
    });

    test('sources', async ({page}) => {
      const list = firstBlock(section(await readSections(page), 'Sources'), ['UL', 'OL']);
      expect(list?.items.length).toBeGreaterThanOrEqual(1);
      list.items.forEach((item, i) => {
        expect(item.hasLink, `source ${i + 1} has a link`).toBe(true);
      });
    });

    test('version-tabs', async ({page}) => {
      // Only lessons with Windows 10/11 differences have tab groups; each must offer
      // exactly these two versions.
      const tabLists = page.locator('article [role="tablist"]');
      const count = await tabLists.count();
      for (let i = 0; i < count; i++) {
        const labels = await tabLists.nth(i).getByRole('tab').allTextContents();
        expect(labels.map((l) => l.trim())).toEqual(['Windows 10', 'Windows 11']);
      }
    });
  });
}
