# Writer brief: Excel practical upgrade (practice files + new lessons)

Project root: /home/abdullahiqbal/Abdullah/global-coaching-center/book-guide
Website: aict-guide/. Lessons: aict-guide/docs/module-07-ms-excel/.

## Read first (required)
1. `specs/practical-upgrade/spec.md` (approved): goal, practice-file rules (§3), the new lessons
   and projects (§4), acceptance criteria.
2. `specs/constitution.md` (v1.4) and `specs/book-spec.md` (v1.5) §4–5: template, student voice,
   verification, diagrams.
3. The finished pilot — copy its pattern exactly:
   - lesson: `aict-guide/docs/module-07-ms-excel/sum-and-average.mdx` (see the `import
     PracticeFile …` line after the front matter and the two `:::info[Practice files]` boxes);
   - file definition: `aict-guide/tools/practice-files/defs/x07_08_sum_and_average.py`;
   - toolkit: `aict-guide/tools/practice-files/xlsxkit.py` (`XlsxFile`, `put_rows`, `formula`,
     `bold`; newer functions get Excel's prefixes automatically — always write formulas through
     `formula()` / `put_rows()`, never by assigning `ws[...] = '=…'` directly).

## Practice files: how to make them
1. Create `aict-guide/tools/practice-files/defs/x07_NN_<slug_with_underscores>.py` (NN = two-digit
   lesson number, e.g. `x07_14_absolute_references.py`) with `APP = 'excel'`,
   `MODULE = 'module-07-ms-excel'`, `LESSON_FILE = '<slug>.mdx'`, `FOLDER = '<slug>'`, and
   `FILES = [XlsxFile(...), ...]`.
2. One `XlsxFile` per table the student works on (usually one for Step by Step, one for
   Practice). Name it after the content (`shop-stock`, `fee-record`), lowercase with dashes.
3. **Same cells as the lesson**: every cell address in the lesson must point to the same thing in
   the file. Starter = data only (answer cells EMPTY). Finished = data + the real formulas.
4. `expected` = every answer cell → its correct value, **worked out in Python from the data**
   (not copied from Excel). Add `assert` lines that the numbers stated on the lesson page equal
   your Python results (like the pilot).
5. Build and check only your own lessons, from `aict-guide/`:
   `python3 tools/practice-files/build.py <folder> …` then
   `python3 tools/practice-files/verify.py <folder> …` — must print `OK` for each.
   Exception: files that use XLOOKUP, XMATCH, SORT, SORTBY, FILTER, UNIQUE or SEQUENCE cannot be
   recalculated yet (LibreOffice here is 24.2; these need 24.8+). verify.py will say so: that one
   message is expected — report it. Every other check must pass.
6. Link the files from the lesson with a `:::info[Practice files]` box at the start of the
   section that uses them, exactly like the pilot:
   `<PracticeFile href="/files/excel/<folder>/<name>-starter.xlsx">Download the starter file: …</PracticeFile>`
   plus one line saying what it has / when to open it. Add
   `import PracticeFile from '@site/src/components/PracticeFile';` once, right after the front
   matter. Never use a plain Markdown link for practice files.
7. Data: made up, realistic for Pakistan (rupees, Pakistani names, shops, schools, offices,
   homes); neutral and respectful; no real people, companies, phone numbers or CNICs. Use
   obviously fake numbers where a number like a phone is needed (e.g. 0300-0000000).

## New lessons (7.14–7.36): how to write them
- Same template, voice and rules as every lesson (constitution v1.4, book-spec v1.5): front
  matter (`title: "Lesson 7.N: <Title>"`, `sidebar_label`, `sidebar_position: N`), no H1, H2s
  exactly `Goal, Why It Matters, Key Terms, Step by Step, Practice, Check Questions,
  Common Mistakes, Sources`; Goal starts "By the end of this lesson, you can "; Key Terms first
  table `| Term | Simple meaning |` with 3–8 rows; Practice's first numbered list ends with an
  item starting `Check your work:` stating the exact correct results; exactly 3 Check Questions
  with `<details><summary>Show answer</summary> … **Answer:** … </details>`; Common Mistakes
  2–5 bullets; Sources first line `*These official pages were checked when this lesson was
  written.*` with linked bullets + exact quotes; ≥1 Mermaid diagram (accTitle, accDescr, ≤8
  boxes, no parentheses/quotes/colons/semicolons inside labels) followed by
  `**Diagram in words:**`. Student voice: never "teacher", "class", "lab", "UNVERIFIED";
  sentences ≤ 25 words; no "simply/just/obviously/easy"; every step says WHY; everyday
  comparisons; real-life Pakistani examples.
- **Every function**: its syntax, arguments and behaviour come from its Microsoft Support function
  page whose "Applies to" list includes **Excel 2021** (e.g.
  support.microsoft.com/en-us/office/if-function-…). Every ribbon step (Filter, Conditional
  Formatting, Freeze Panes, …) from a Microsoft page that applies to Excel 2021. Quote them in
  Sources. If a step can't be confirmed, use `:::tip[If your screen looks different]` with a
  confirmed backup, or leave it out.
- Link back to earlier lessons instead of re-teaching (e.g. formulas → first-formulas.mdx, fill
  handle → fill-handle.mdx, `$` → absolute-references.mdx). Only link to lessons that already exist
  on disk or are in your own assignment.
- **Projects (7.29–7.36)**: a real story (who needs the sheet and why), the finished sheet's
  purpose, Step by Step builds the main part, Practice extends it or builds a second version;
  state every correct result. Use only skills from earlier lessons (link them).
- **Dynamic array formulas (SORT, FILTER, UNIQUE, Lesson 7.25 and any project using them)**:
  in the finished file write them with openpyxl's `ArrayFormula(ref="<exact output range>",
  text=add_prefixes("=SORT(...)"))` so the results show in Excel 2021. Explain in the lesson,
  with a Microsoft source that applies to Excel 2021, how the formula spills when the student
  types it.

## Rules
- Edit ONLY your assigned lesson files and your own `defs/` modules (and the files they build
  under `aict-guide/static/files/excel/<your folders>/`). Do NOT edit tests, specs, index.md,
  xlsxkit.py, build.py, verify.py or other lessons. If the toolkit needs a change, report it.
- Do NOT run npm test/build, git or servers. Work files in your own folder under /tmp/claude-1000/.
- Use WebSearch/WebFetch for Microsoft pages; if blocked, `curl -sL` via Bash.
- Final reply (short): per lesson — files built (names), verify.py result, the Microsoft pages
  used (URL + exact quote per function/step), any "If your screen looks different" box (what to
  check on Excel 2021), anything left out.
