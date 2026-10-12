# Module 1 Specification: Computer Basics

**Status**: APPROVED v1.0 (owner approved 2026-10-11)
**Created**: 2026-10-10
**Module folder (planned)**: `module-01-computer-basics`
**Governed by**: `specs/constitution.md`, `specs/book-spec.md`

---

## 1. Module Summary

This is the student's first contact with a computer. By the end of the module, a student who has
never touched a computer can name its main parts, turn it on and off safely, use the mouse and
keyboard, find their way around the desktop, and save a file in a folder.

**Prerequisites**: none.

**Target system**: the lab has a **mix of Windows 10 and Windows 11** computers.
- Every software step (Lessons 1.4, 1.7, 1.8) must be verified for **both** versions.
- Where the two versions are the same, show one set of steps and say it works on both.
- Where they differ, show the steps for each version separately, clearly labelled
  "Windows 10" and "Windows 11". How this looks on the page is decided in the plan, after
  checking the documentation.
- An UNVERIFIED step is only cleared after the owner has tested it on **each** version it
  applies to: **Windows 11 on the owner's laptop**, and **Windows 10 on a lab computer**.

**Lab hardware**: **desktop computers** (monitor, system unit, separate keyboard and mouse).
Laptops and touchpads are out of scope for this module.

**Internet**: the lab has **reliable internet** during class. A Student Task may use a website,
but only if the website is checked and listed in Sources. Every task must still have a step the
student can do without the website, in case the connection fails that day.

## 2. Learning Outcomes

By the end of Module 1, the student can:

- **LO-1**: Explain the four jobs of a computer (input, processing, output, storage) and give one
  everyday example of each.
- **LO-2**: Sort a list of items into hardware and software.
- **LO-3**: Point to the main parts of the lab computer and say what each one does.
- **LO-4**: Start the computer and shut it down the correct way.
- **LO-5**: Use the mouse to point, click, double-click, right-click and drag.
- **LO-6**: Find the main key groups on the keyboard and use the most common keys. (Real typing
  practice is in Module 2.)
- **LO-7**: Say what an operating system is, and name and use the main parts of the desktop.
- **LO-8**: Create a folder, save a file into it, find the file again, delete it, and get it
  back from the Recycle Bin.
- **LO-9**: Follow basic rules for keeping themselves and the computer safe.

## 3. Lesson List

### Changes from the starting point (for owner review)

| Change | Reason |
|--------|--------|
| Mouse and keyboard moved from last to **before** the desktop and files lessons | Students need the mouse to use the desktop and to save files. Without it, they can't do the Student Tasks in Lessons 1.7–1.8. |
| "Mouse and keyboard basics" **split into two lessons** | For a first-time user, mouse skills alone are a full session. Keyboard basics here are only the key groups and a few keys; typing is Module 2. |
| "Starting up, shutting down, and caring for a computer" **split into two lessons** | Turning on and off is needed on day one, so it comes early. Caring for the computer makes more sense once students know the parts, so it ends the module. |

**Owner decision (2026-10-10)**: all three changes accepted, giving 9 lessons.

### Lessons (proposed teaching order)

| # | Lesson | Main outcome |
|---|--------|--------------|
| 1.1 | What Is a Computer? Input, Processing, Output and Storage | LO-1 |
| 1.2 | Hardware and Software | LO-2 |
| 1.3 | Parts of a Computer and Their Jobs | LO-3 |
| 1.4 | Starting Up and Shutting Down Safely | LO-4 |
| 1.5 | Using the Mouse | LO-5 |
| 1.6 | Keyboard Basics | LO-6 |
| 1.7 | The Operating System and the Desktop | LO-7 |
| 1.8 | Files, Folders, Saving and Deleting | LO-8 |
| 1.9 | Caring for Your Computer | LO-9 |

## 4. Acceptance Criteria — All Lessons

Every lesson in this module must meet **all** of these. The "Checked by" column is a draft; the
plan will turn each automated check into a test that is written first (Test-First).

| ID | Criterion | Checked by |
|----|-----------|------------|
| AC-C1 | All 8 template sections are present, in order, with the exact headings from `book-spec.md` Section 4. | Automated (browser test) |
| AC-C2 | At least one Mermaid diagram, which the browser draws as a picture (not code). | Automated (browser test) |
| AC-C3 | Every diagram has `accTitle` and `accDescr`, and a "diagram in words" sentence below it. | Automated (source check) + owner review |
| AC-C4 | Every technical claim is verified and listed in Sources. Every software step that could not be verified is in an UNVERIFIED box. | Owner review + automated check that Sources is not empty |
| AC-C5 | `npm run build` passes with zero broken-link, broken-anchor and broken-Markdown-link messages. | Automated (build) |
| AC-C6 | Exactly 3 Check Questions, each with a model answer. At least one asks the student to *do* or *point to* something. | Automated (count) + owner review |
| AC-C7 | Key Terms has 3–8 terms, each with an English meaning (Urdu meaning optional, constitution v1.3). Every new word used in the lesson appears there. Writing follows the plain-language rules. | Automated (table has 2 or 3 columns, 3–8 rows) + owner review (any Urdu text, plain language) |
| AC-C10 | The lesson fits one 60-minute session using the time plan in `book-spec.md` Section 4. | Owner review |
| AC-C8 | Student Task ends with "Show your teacher: …". | Automated (text check) |
| AC-C9 | The owner has reviewed and approved the lesson. | Owner |

## 5. Lessons in Detail

For each lesson: the goal (draft wording), what is in and out of scope, likely key terms, a
diagram idea, and its own acceptance criteria. All of these are *topics*; the facts are verified
when the lesson is written (constitution, Section 3).

### Lesson 1.1 — What Is a Computer? Input, Processing, Output and Storage

- **Goal (draft)**: By the end of this lesson, you can explain the four jobs of a computer and
  give an example of each.
- **In scope**: a computer as a machine that takes in information, works on it, shows a result,
  and keeps it; an everyday comparison students already know.
- **Out of scope**: names of parts in detail (Lesson 1.3), binary, history of computers.
- **Likely key terms**: computer, input, processing, output, storage, data.
- **Diagram idea**: flowchart Input → Processing → Output, with Storage connected to Processing.
- **Lesson acceptance criteria**:
  - AC-1.1-a: All four jobs are named, explained in one sentence each, and shown in the diagram.
  - AC-1.1-b: Each job has one everyday example.
  - AC-1.1-c: One Check Question asks the student to sort examples into the four jobs.

### Lesson 1.2 — Hardware and Software

- **Goal (draft)**: By the end of this lesson, you can tell whether something is hardware or
  software.
- **In scope**: hardware = parts you can touch; software = instructions/programs; how they need
  each other.
- **Out of scope**: types of software in depth, installing software.
- **Likely key terms**: hardware, software, program, app.
- **Diagram idea**: two groups (Hardware, Software) with examples, joined by "work together".
- **Lesson acceptance criteria**:
  - AC-1.2-a: Hardware and software are defined in plain words, with at least 3 examples each.
  - AC-1.2-b: The Student Task has the student sort at least 6 items into hardware or software.
  - AC-1.2-c: Examples of software are named only if verified (constitution, Section 3).

### Lesson 1.3 — Parts of a Computer and Their Jobs

- **Goal (draft)**: By the end of this lesson, you can point to the main parts of a computer
  and say what each one does.
- **In scope**: the parts students can see on the lab computer, each linked back to the four
  jobs from Lesson 1.1.
- **Out of scope**: opening the computer case, building or upgrading a computer.
- **Likely key terms**: monitor, keyboard, mouse, system unit / CPU, speakers, printer.
  (Desktop parts only. The final list is the parts actually present in the lab.)
- **Diagram idea**: each part connected to its job (input / processing / output / storage).
- **Lesson acceptance criteria**:
  - AC-1.3-a: Every part shown is one the students can see in the lab.
  - AC-1.3-b: Every part is linked to one of the four jobs from Lesson 1.1.
  - AC-1.3-c: The Student Task has the student point to each part on a real computer.

### Lesson 1.4 — Starting Up and Shutting Down Safely

- **Goal (draft)**: By the end of this lesson, you can turn the computer on and shut it down
  the correct way.
- **In scope**: turning on, waiting for it to start, signing in (if the lab uses it), shutting
  down from the operating system, and why not to just pull the plug.
- **Out of scope**: restarting after a crash, sleep and hibernate in detail, passwords and
  accounts in depth.
- **Likely key terms**: power button, start up, sign in, shut down.
- **Diagram idea**: flowchart of the steps from power button to desktop, and from desktop to
  shut down.
- **Software-step risk**: the shut-down steps depend on the Windows version. Each one must come
  from Microsoft's official documentation, or be marked UNVERIFIED.
- **Lesson acceptance criteria**:
  - AC-1.4-a: The shut-down steps are given for Windows 10 and Windows 11 (or shown once if
    identical), each citing a Microsoft source, or marked UNVERIFIED.
  - AC-1.4-b: The lesson explains why the correct shut-down matters, in plain words.
  - AC-1.4-c: Common Mistakes includes turning off at the wall/plug without shutting down.

### Lesson 1.5 — Using the Mouse

- **Goal (draft)**: By the end of this lesson, you can point, click, double-click, right-click
  and drag with the mouse.
- **In scope**: holding the mouse, the pointer, left and right buttons, the scroll wheel, the
  five actions above.
- **Out of scope**: touchpads (the lab uses desktops), changing mouse settings.
- **Likely key terms**: mouse, pointer, click, double-click, right-click, drag, scroll.
- **Diagram idea**: mouse action → what happens on screen.
- **Lesson acceptance criteria**:
  - AC-1.5-a: Each of the five actions has its own demo step and its own practice step.
  - AC-1.5-b: Common Mistakes includes moving the mouse while clicking, and double-clicking too
    slowly.
  - AC-1.5-c: The Student Task can be done on the lab computer without installing anything.
    An online mouse practice page may be added only if it is checked and listed in Sources, and
    the task still works without it.

### Lesson 1.6 — Keyboard Basics

- **Goal (draft)**: By the end of this lesson, you can find the main key groups and use the most
  common keys.
- **In scope**: key groups (letters, numbers, function keys, arrow keys, number pad if present);
  a small set of common keys.
- **Out of scope**: touch typing and typing speed (Module 2); keyboard shortcuts (later modules,
  each verified).
- **Likely key terms**: key, keyboard, Enter, Space bar, Backspace, Shift, Caps Lock.
  (Every key name must be verified.)
- **Diagram idea**: keyboard divided into key groups.
- **Lesson acceptance criteria**:
  - AC-1.6-a: Every key name and what it does is verified (constitution, Section 3).
  - AC-1.6-b: No keyboard shortcut appears in this lesson.
  - AC-1.6-c: The lesson says clearly that typing practice comes in Module 2.

### Lesson 1.7 — The Operating System and the Desktop

- **Goal (draft)**: By the end of this lesson, you can say what an operating system does and
  use the main parts of the desktop.
- **In scope**: what an operating system is; the desktop, icons, Start menu, taskbar; opening
  and closing a program; a window and its buttons.
- **Out of scope**: settings, installing apps, the full list of operating systems.
- **Likely key terms**: operating system, desktop, icon, taskbar, Start menu, window.
- **Diagram idea**: layers: you → operating system → hardware; or the desktop's main parts.
- **Software-step risk**: names and places of desktop parts depend on the Windows version. Each
  must come from Microsoft's official documentation, or be marked UNVERIFIED.
- **Lesson acceptance criteria**:
  - AC-1.7-a: Every desktop part named is checked for both Windows 10 and Windows 11. Any
    difference in name or place is shown for each version. Each cites a Microsoft source, or is
    marked UNVERIFIED.
  - AC-1.7-b: The Student Task has the student open and close a program.
  - AC-1.7-c: The operating system is explained without technical words that have not been
    taught yet.

### Lesson 1.8 — Files, Folders, Saving and Deleting

- **Goal (draft)**: By the end of this lesson, you can make a folder, save a file into it, find
  it again, delete it, and get it back.
- **In scope**: what a file is; what a folder is; making a folder; making a simple drawing in
  **Paint** and saving it with a name; finding and opening it again; deleting it; getting it
  back from the Recycle Bin.
- **Out of scope**: file types and extensions in depth, USB drives, cloud storage, emptying the
  Recycle Bin, Paint's drawing tools beyond what is needed to make a first file.
- **Likely key terms**: file, folder, save, file name, File Explorer, Paint, delete,
  Recycle Bin.
- **Time risk**: this lesson has the most steps in the module. If the draft does not fit one
  60-minute session (AC-C10), it is split into "1.8 Files, Folders and Saving" and
  "1.9 Deleting and the Recycle Bin", and Caring becomes 1.10. The owner approves any split.
- **Diagram idea**: tree: folder → sub-folder → files; or save → name → choose folder → find.
- **Software-step risk**: File Explorer, Paint, delete and Recycle Bin steps depend on the
  Windows version. Each must come from Microsoft's official documentation, or be marked
  UNVERIFIED.
- **Lesson acceptance criteria**:
  - AC-1.8-a: The Student Task has the student open the file they saved from the folder they
    made, delete it, and then get it back from the Recycle Bin.
  - AC-1.8-b: Paint is confirmed from official Microsoft sources to be available on both
    Windows 10 and Windows 11. Its open and save steps are verified for both. If either
    cannot be confirmed, the owner is told before the lesson is written.
  - AC-1.8-c: Common Mistakes includes saving without choosing a folder, then not finding the
    file.
  - AC-1.8-d: The lesson explains, in plain words, that a deleted file goes to the Recycle Bin
    first and can be brought back from there. This is verified for both versions.

### Lesson 1.9 — Caring for Your Computer

- **Goal (draft)**: By the end of this lesson, you can follow basic rules to keep yourself and
  the computer safe.
- **In scope**: food and drink away from the computer, clean hands, handling cables, power
  safety, sitting correctly, and resting your eyes.
- **Out of scope**: viruses and online safety (Module 3), repairs.
- **Likely key terms**: care, power cable, surge, posture.
- **Diagram idea**: do / don't sorting diagram.
- **Lesson acceptance criteria**:
  - AC-1.9-a: Every safety or health statement cites an official or recognised source.
  - AC-1.9-b: The rules suit the lab setting (owner confirms).
  - AC-1.9-c: The Student Task is a short checklist the student uses on their own computer.

## 6. Module-Level Acceptance Criteria

- **M1-01**: The module overview page lists all lessons in the order in Section 3, and each one
  links to its lesson page.
- **M1-02**: Every learning outcome LO-1 to LO-9 is covered by at least one lesson's Goal and
  Student Task.
- **M1-03**: Every lesson meets AC-C1 to AC-C10 and its own lesson criteria.
- **M1-04**: The module has no UNVERIFIED markers left that the owner has not tested.

## 7. Open Questions (to resolve before this spec is final)

All open questions were answered by the owner on 2026-10-10 and are recorded above. None are
left. Approved by the owner on 2026-10-11.
