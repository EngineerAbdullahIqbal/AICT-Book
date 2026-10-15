# Writer brief: re-verify Word/Excel lessons for Office 2021

Project root: /home/abdullahiqbal/Abdullah/global-coaching-center/book-guide
The owner confirmed the lab computers have **Office 2021** (Word 2021, Excel 2021), not 2016/2019.
Read first: `specs/constitution.md` (v1.4, esp. §1–4) and `specs/book-spec.md` (v1.4) §4.

## Task, for each assigned lesson
1. Read the whole lesson. List EVERY software claim (tab, group, button, menu, dialog box,
   pane, shortcut, screen location, behaviour).
2. Check each against an official Microsoft page whose **"Applies to" list includes Word 2021 /
   Excel 2021** (support.microsoft.com, learn.microsoft.com, microsoft.com). Many current pages
   list "Microsoft 365, 2024, 2021, 2019, 2016": those count. A page that applies only to
   "Microsoft 365", or only to 2016/2019, does NOT confirm a 2021 step on its own.
   Office 2021 has the newer look in several places, for example (CHECK each, don't assume):
   the Editor pane for spelling; Insert > Pictures > This Device; table tabs "Table Design" and
   "Layout"; the Start screen with Blank document / Blank workbook; "Chart Design" tab.
3. Outcomes:
   - **Matches 2021** → keep; update the Sources note so it says the page applies to 2021.
   - **Differs in 2021** → correct the step to the 2021 name/route; update Check Questions,
     Common Mistakes, Key Terms and diagrams that depend on it.
   - **"If your screen looks different" box** (`:::tip[If your screen looks different]`):
     if a 2021 source now confirms the step, REMOVE the box and cite the source. If not, keep
     the box (student-friendly, with a confirmed backup way inside).
   - Cannot confirm for 2021 → keep the step only with a confirmed backup in an
     "If your screen looks different" box, or remove the claim.
4. Sources: replace sources that applied only to 2016/2019 with 2021-applicable ones where
   possible. Archived 2016/2019 pages may stay only as "supporting note only", never as the only
   proof for a 2021 step. Every Sources bullet keeps a Markdown link and says
   "(applies to Word 2021)" / "(applies to Excel 2021)" with a short exact quote.
5. Text that names the version ("Word 2016", "2016/2019", "Microsoft 365 only extra step",
   "older versions may show …") → rewrite for Word 2021 / Excel 2021.

Finished examples of the Sources style: `aict-guide/docs/module-04-ms-word/typing-and-correcting-text.mdx`,
`aict-guide/docs/module-07-ms-excel/sum-and-average.mdx`.

## Keep exactly (automated tests check these)
- Front matter; H2s exactly: Goal, Why It Matters, Key Terms, Step by Step, Practice,
  Check Questions, Common Mistakes, Sources; Goal starts "By the end of this lesson, you can ";
  Key Terms first table with headers `| Term | Simple meaning |`, 3–8 rows; Practice's first
  numbered list ends with an item starting `Check your work:`; exactly 3 Check Questions, each
  answer in `<details>` / `<summary>Show answer</summary>` / `**Answer:** …` / `</details>`;
  Common Mistakes 2–5 bullets; diagrams with accTitle/accDescr then `**Diagram in words:**`;
  hidden `{/* Screenshot to add: … */}` notes.
- Student voice: never "teacher", "class", "lab", "UNVERIFIED", "test it"; sentences ≤ 25 words;
  no "simply/just/obviously/easy". Every step says why.
- Excel numbers: recompute any changed result with python3.

## Tools / rules
- WebSearch (allowed_domains support.microsoft.com, learn.microsoft.com, microsoft.com) and
  WebFetch; if blocked (403), use `curl -sL` via Bash; try en-gb / en-in copies.
- Context7 has no Office end-user coverage; it is not needed for this task.
- Edit ONLY your assigned lesson files. No npm test/build/git/servers. Put work files in a
  folder of your own under /tmp/claude-1000/.
- Final reply: per lesson, a table — claim · result (OK 2021 / CORRECTED / BOX REMOVED /
  BOX KEPT / BOX ADDED) · source URL · exact quote. Then the list of boxes still left
  (lesson, step, what the owner should check on a 2021 computer).
