# Writer brief: Module 5 (MS PowerPoint 2021) lessons

Project root: /home/abdullahiqbal/Abdullah/global-coaching-center/book-guide
Lesson folder: aict-guide/docs/module-05-ms-powerpoint/

## Read first (required)
1. `specs/constitution.md` (v1.4): audience, student voice, tone, verification §3, the
   "If your screen looks different" box §4.
2. `specs/book-spec.md` (v1.4) §4 lesson template, §5 diagram rules.
3. `specs/module-05-ms-powerpoint/spec.md` (approved): scope per lesson, AC-P1…P4.
4. Model lessons (copy format, voice and depth):
   `aict-guide/docs/module-04-ms-word/formatting-text.mdx` and
   `aict-guide/docs/module-07-ms-excel/sum-and-average.mdx`.
5. Link back instead of re-teaching: ../module-04-ms-word/starting-word.mdx (ribbon, tabs),
   saving-closing-opening.mdx, formatting-text.mdx, formatting-paragraphs.mdx,
   bulleted-and-numbered-lists.mdx, tables.mdx, pictures-and-shapes.mdx,
   page-setup-and-printing.mdx, ../module-07-ms-excel/simple-chart.mdx,
   ../module-01-computer-basics/files-folders-saving-deleting.mdx.
   Lessons in this module (you may link by file name): starting-powerpoint.mdx,
   adding-slides-and-text.mdx, saving-and-slide-show.mdx, formatting-text-on-slides.mdx,
   design-themes.mdx, pictures-and-shapes.mdx, tables-and-charts.mdx, organizing-slides.mdx,
   slide-transitions.mdx, simple-animations.mdx, speaker-notes-and-printing.mdx,
   project-shop-presentation.mdx. Only link to a file in this module if it already exists or is
   in your own assignment (others may not be written yet — a missing link breaks the build).

## Voice and style
- Speak to the student as "you". NEVER mention the teacher, "class", "lab", "Say:". No "simply",
  "just", "obviously", "easy", "easily". Simple English: most sentences ≤ 15 words, none > 25.
  Every step or small group of steps says WHY. Everyday comparisons ("A slide is like one page
  of a flip chart."). Real-life Pakistani examples (mobile shop, school sports day, tuition
  centre, wedding plan, health talk); made-up names; neutral and respectful.

## Page format (automated tests check this)
Front matter exactly:
```
---
title: "Lesson 5.N: <Title>"
sidebar_label: "<label given in your task>"
sidebar_position: N
---
```
No H1. Exactly these H2s in order: `## Goal`, `## Why It Matters`, `## Key Terms`,
`## Step by Step`, `## Practice`, `## Check Questions`, `## Common Mistakes`, `## Sources`.
- Goal starts `By the end of this lesson, you can `.
- Key Terms: first table, headers exactly `| Term | Simple meaning |`, 3–8 rows.
- Step by Step: a worked example the student follows in PowerPoint; *You see …* in italics;
  bold UI names (**Home** tab, **New Slide**).
- Practice: a NEW real-life task. FIRST numbered list = steps; LAST item starts exactly
  `Check your work:` and says what a correct result looks like. No internet needed; pictures
  come from the student's own computer.
- Check Questions: FIRST numbered list, EXACTLY 3, at least one asks the student to DO or point
  to something. Each answer:
  ```
  1. Question?

     <details>
     <summary>Show answer</summary>

     **Answer:** …

     </details>
  ```
- Common Mistakes: first bullet list, 2–5 items `- **Mistake** → How to fix it.`
- Sources: first line exactly `*These official pages were checked when this lesson was written.*`
  then bullets, each with a Markdown link + a short exact quote of what it confirms + that it
  applies to PowerPoint 2021.
- At least one Mermaid diagram (flowchart, max 8 boxes, 1–4 words per box, no parentheses,
  quotes, colons or semicolons inside labels; accTitle + accDescr), then a blank line and a
  paragraph starting `**Diagram in words:**`.
- Optional hidden note for the owner: `{/* Screenshot to add: … */}` (never visible).
- MDX: no bare `<`, `{`, `}` in normal text.

## Verification (non-negotiable)
- Every PowerPoint tab, group, button, command, view, pane, dialog box, shortcut and behaviour
  must come from a Microsoft page whose "Applies to" list includes **PowerPoint 2021**
  (support.microsoft.com, learn.microsoft.com; e.g. "PowerPoint for Windows training" pages
  list PowerPoint 2021). Use WebSearch (allowed_domains support.microsoft.com,
  learn.microsoft.com) + WebFetch; if blocked, `curl -sL` via Bash (try en-gb copies).
  Context7 has no Office end-user coverage and is not needed.
- "Microsoft 365 only" pages do not count. Do not teach Designer, Copilot or other
  subscription-only features.
- Never invent names or locations. If a step can't be confirmed for 2021, give a confirmed
  backup way in a `:::tip[If your screen looks different]` box (student-friendly, no
  "test"/"teacher"/"unverified" words), or leave it out.
- Good-slide advice (few words, large text) only if a Microsoft page or recognised education
  source supports it.
- Any numbers in examples (prices, chart data): check with python3.

## Rules
- Write ONLY your assigned files. No npm test/build/git/servers. Work files in a folder of
  your own under /tmp/claude-1000/.
- Final reply (short): per file, sources used (URL + exact quote for each key step), every step
  in an "If your screen looks different" box (what the owner should check), anything left out.
