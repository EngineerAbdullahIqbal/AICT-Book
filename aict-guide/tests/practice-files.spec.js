// PU-01: every practical lesson offers at least one starter and one finished file, and every
// practice file downloads as a real Office file (.xlsx/.docx/.pptx are ZIPs: they start "PK").
import {test, expect} from '@playwright/test';
import {PRACTICE_LESSONS} from './practice-files.js';

for (const url of PRACTICE_LESSONS) {
  test(`practice-files: ${url}`, async ({page, request}) => {
    await page.goto(url);
    const hrefs = await page
      .locator('article a[download][href*="/files/"]')
      .evaluateAll((links) => links.map((a) => a.getAttribute('href')));
    expect(hrefs.some((h) => /-starter\.(xlsx|docx|pptx)$/.test(h)), 'a starter file').toBe(true);
    expect(hrefs.some((h) => /-finished\.(xlsx|docx|pptx)$/.test(h)), 'a finished file').toBe(true);
    for (const href of new Set(hrefs)) {
      const response = await request.get(href);
      expect(response.ok(), `${href} downloads`).toBe(true);
      const body = await response.body();
      expect(body.length, `${href} is not empty`).toBeGreaterThan(1000);
      expect(body.subarray(0, 2).toString(), `${href} is a real Office file`).toBe('PK');
    }
  });
}
