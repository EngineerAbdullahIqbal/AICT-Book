// Reads a doc page as sections: each H2 in the article plus the blocks after it,
// up to the next H2. Used by the lesson (C3) and module overview (C4) tests.

// Heading anchors add a zero-width space to H2 text; strip it.
const clean = (text) => (text ?? '').replace(/​/g, '').trim();

export async function readSections(page) {
  const raw = await page.locator('article').first().evaluate((article) => {
    const markdown = article.querySelector('.theme-doc-markdown') ?? article;
    const sections = [];
    let current = null;
    for (const el of markdown.children) {
      if (el.tagName === 'H2') {
        current = {heading: el.textContent, blocks: []};
        sections.push(current);
      } else if (current) {
        current.blocks.push({
          tag: el.tagName,
          text: el.textContent,
          // Direct list items (for OL/UL blocks).
          items: ['OL', 'UL'].includes(el.tagName)
            ? [...el.children].map((li) => ({
                text: li.textContent,
                hasLink: !!li.querySelector('a[href]'),
              }))
            : [],
          // Table headers and rows (for TABLE blocks).
          headers: el.tagName === 'TABLE'
            ? [...el.querySelectorAll('thead th')].map((th) => th.textContent)
            : [],
          rows: el.tagName === 'TABLE'
            ? [...el.querySelectorAll('tbody tr')].map((tr) =>
                [...tr.children].map((td) => ({
                  text: td.textContent,
                  hasUrdu: !!td.querySelector('[lang="ur"]'),
                })),
              )
            : [],
          links: [...el.querySelectorAll('a[href]')].map((a) => a.getAttribute('href')),
        });
      }
    }
    return sections;
  });
  return raw.map((s) => ({...s, heading: clean(s.heading)}));
}

export function section(sections, heading) {
  return sections.find((s) => s.heading === heading);
}

export function firstBlock(sec, tags) {
  return sec?.blocks.find((b) => tags.includes(b.tag));
}

// Normalise doc URLs so "/a/b/" and "/a/b" compare equal.
export const normaliseUrl = (url) => (url ?? '').replace(/\/+$/, '');
