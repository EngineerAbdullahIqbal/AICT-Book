// Shared checks for rendered Mermaid diagrams (contract C2, used again by lesson tests in C3).
import {expect} from '@playwright/test';

// Mermaid adds `aria-roledescription` to every diagram SVG it draws (research R4).
// A diagram that failed to render stays a code block and has no such SVG.
export function renderedDiagrams(page) {
  return page.locator('article svg[aria-roledescription]');
}

// Mermaid draws diagrams in the browser after the page loads. With several tests running at
// once this took over 5 s (the default) in one run, so allow more time.
const DIAGRAM_RENDER_TIMEOUT = 15_000;

export async function expectAtLeastOneDiagram(page) {
  await expect(renderedDiagrams(page).first()).toBeVisible({timeout: DIAGRAM_RENDER_TIMEOUT});
}

// Mermaid turns accTitle/accDescr into <title> and <desc> inside the SVG (research R4).
export async function expectDiagramsAccessible(page) {
  const diagrams = renderedDiagrams(page);
  const count = await diagrams.count();
  expect(count).toBeGreaterThan(0);
  for (let i = 0; i < count; i++) {
    const {title, desc} = await diagrams.nth(i).evaluate((svg) => ({
      title: svg.querySelector(':scope > title')?.textContent?.trim() ?? '',
      desc: svg.querySelector(':scope > desc')?.textContent?.trim() ?? '',
    }));
    expect(title, `diagram ${i + 1} accTitle`).not.toBe('');
    expect(desc, `diagram ${i + 1} accDescr`).not.toBe('');
  }
}

// The block right after each diagram must be a paragraph starting "Diagram in words:".
// We climb from the SVG to the first ancestor that has a next sibling, so the check
// does not depend on how the theme wraps the diagram.
export async function expectDiagramsInWords(page) {
  const diagrams = renderedDiagrams(page);
  const count = await diagrams.count();
  expect(count).toBeGreaterThan(0);
  for (let i = 0; i < count; i++) {
    const next = await diagrams.nth(i).evaluate((svg) => {
      let el = svg;
      while (el && !el.nextElementSibling && el.tagName !== 'ARTICLE') {
        el = el.parentElement;
      }
      const sibling = el?.nextElementSibling;
      return {tag: sibling?.tagName ?? '', text: sibling?.textContent?.trim() ?? ''};
    });
    expect(next.tag, `diagram ${i + 1}: block after diagram`).toBe('P');
    expect(next.text.startsWith('Diagram in words:'), `diagram ${i + 1}: "${next.text}"`).toBe(
      true,
    );
  }
}
