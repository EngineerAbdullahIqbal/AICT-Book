# Writer brief: Module 6 (Presentation Skills) lessons

Project root: /home/abdullahiqbal/Abdullah/global-coaching-center/book-guide
Lesson folder: aict-guide/docs/module-06-presentation-skills/

## Read first (required)
1. `specs/constitution.md` (v1.4): audience, student voice, tone, verification §3, the
   "If your screen looks different" box §4.
2. `specs/book-spec.md` (v1.4) §4 lesson template, §5 diagram rules.
3. `specs/module-06-presentation-skills/spec.md` (approved): scope, AC-S1…S4, how the lesson
   format fits a speaking skill, owner decisions (language: either; project re-uses Lesson 5.12).
4. Model lessons (copy format, voice and depth):
   `aict-guide/docs/module-05-ms-powerpoint/design-themes.mdx` and
   `aict-guide/docs/module-01-computer-basics/caring-for-your-computer.mdx` (a non-software
   lesson with a checklist Practice).
5. Link back instead of re-teaching: Module 5 lessons in ../module-05-ms-powerpoint/
   (starting-powerpoint.mdx, adding-slides-and-text.mdx, saving-and-slide-show.mdx,
   formatting-text-on-slides.mdx, design-themes.mdx, pictures-and-shapes.mdx,
   tables-and-charts.mdx, organizing-slides.mdx, slide-transitions.mdx, simple-animations.mdx,
   speaker-notes-and-printing.mdx, project-shop-presentation.mdx).
   Module 6 files (you may link to a sibling only if it is in your own assignment or listed as
   already written in your task): what-makes-a-good-presentation.mdx, planning-your-talk.mdx,
   slides-that-help.mdx, your-voice.mdx, body-language-and-eye-contact.mdx,
   handling-nervousness.mdx, practising-with-powerpoint.mdx, answering-questions.mdx,
   project-three-minute-talk.mdx.

## Voice and style
- Speak to the student as "you". NEVER mention the teacher, "class", "lab", "Say:". No
  "simply", "just", "obviously", "easy", "easily". Simple English: most sentences ≤ 15 words,
  none > 25. Every step says WHY. Everyday comparisons. Real-life Pakistani examples (job
  interview, shop owner, health-awareness talk at a Basic Health Unit, college project, family
  event). Made-up names; neutral and respectful (no politics or religion).
- Say once per lesson where natural: these skills work the same when you speak in Urdu.
- Practice: a speaking task done alone, with a family member or friend, or by recording
  yourself on a phone (optional). "Check your work" = a short checklist the student can tick.

## Page format (automated tests check this)
Front matter exactly:
```
---
title: "Lesson 6.N: <Title>"
sidebar_label: "<label given in your task>"
sidebar_position: N
---
```
No H1. Exactly these H2s in order: `## Goal`, `## Why It Matters`, `## Key Terms`,
`## Step by Step`, `## Practice`, `## Check Questions`, `## Common Mistakes`, `## Sources`.
- Goal starts `By the end of this lesson, you can `.
- Key Terms: first table, headers exactly `| Term | Simple meaning |`, 3–8 rows.
- Step by Step: numbered steps the student does (plan on paper, read a short sample talk,
  say lines aloud, time yourself, use PowerPoint where relevant), with *You see/hear …* where
  useful.
- Practice: FIRST numbered list = steps; LAST item starts exactly `Check your work:` followed by
  a short checklist in the same item (e.g. "Check your work: tick each one — …").
- Check Questions: FIRST numbered list, EXACTLY 3, at least one asks the student to DO
  something. Each answer:
  ```
  1. Question?

     <details>
     <summary>Show answer</summary>

     **Answer:** …

     </details>
  ```
- Common Mistakes: first bullet list, 2–5 items `- **Mistake** → How to fix it.`
- Sources: first line exactly `*These official pages were checked when this lesson was written.*`
  then bullets, each with a Markdown link + a short exact quote of what it confirms.
- At least one Mermaid diagram (flowchart, max 8 boxes, 1–4 words per box, no parentheses,
  quotes, colons or semicolons inside labels; accTitle + accDescr), then a blank line and a
  paragraph starting `**Diagram in words:**`.
- Sample talks or scripts: put them in a `:::note[Sample talk]` box or a ```text block.
- MDX: no bare `<`, `{`, `}` in normal text.

## Verification (non-negotiable)
- Every speaking tip (voice, pace, pauses, eye contact, posture, hands, nerves, breathing,
  questions, talk structure, slide design) must come from a recognised source (constitution §3):
  a university page (e.g. a university communication / public speaking / writing centre),
  BBC Bitesize, GCFGlobal / learnfree.org (archived copies on web.archive.org are fine), or
  Microsoft's "Tips for creating and delivering an effective presentation" (applies to
  PowerPoint 2021). No blogs, commercial coaching sites, forums or Wikipedia. Quote the source.
- PowerPoint steps (Speaker Notes, Rehearse Timings, Presenter View, Slide Show): only from
  Microsoft pages whose "Applies to" list includes PowerPoint 2021 (Windows tab). No Speaker
  Coach or other subscription-only tools. Unconfirmed step → `:::tip[If your screen looks
  different]` with a confirmed backup way, or leave it out.
- Health claims (breathing to calm nerves) only if a recognised source says so.
- Use WebSearch + WebFetch; if blocked, `curl -sL` via Bash. Context7 is not needed.

## Rules
- Write ONLY your assigned files. No npm test/build/git/servers. Work files in a folder of your
  own under /tmp/claude-1000/.
- Final reply (short): per file, sources used (URL + exact quote per key tip/step), any
  "If your screen looks different" box (what the owner should check), anything left out.
