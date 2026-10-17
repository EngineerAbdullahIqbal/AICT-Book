"""Lesson 7.9: Functions: MIN, MAX and COUNT."""

from xlsxkit import XlsxFile, put_rows, formula, bold

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'min-max-count.mdx'
FOLDER = 'min-max-count'

# Step by Step: test marks. Hamza was absent, so B4 holds the word Absent (as in the lesson's
# table; step 5 later changes it to 50 to show the formulas update).
MARKS = [('Ali', 78), ('Sana', 85), ('Hamza', 'Absent'), ('Fatima', 91), ('Usman', 62),
         ('Zainab', 70)]


def build_test_marks(wb, finished):
    ws = wb.active
    put_rows(ws, [('Student', 'Marks'), *MARKS])
    put_rows(ws, [('Lowest',), ('Highest',), ('Students with marks',)], start_row=8,
             bold_first=False)
    bold(ws, 'A8', 'A9', 'A10')
    if finished:
        formula(ws, 'B8', '=MIN(B2:B7)')
        formula(ws, 'B9', '=MAX(B2:B7)')
        formula(ws, 'B10', '=COUNT(B2:B7)')


marks = [m for _, m in MARKS if isinstance(m, (int, float))]

# Practice: street cricket runs. Rehan did not bat (text); Danish scored 0 (a number).
RUNS = [('Bilal', 45), ('Kashif', 12), ('Danish', 0), ('Imran', 67), ('Rehan', 'Did not bat'),
        ('Asad', 23), ('Faisal', 38)]


def build_cricket_runs(wb, finished):
    ws = wb.active
    put_rows(ws, [('Player', 'Runs'), *RUNS])
    put_rows(ws, [('Lowest',), ('Highest',), ('Players who batted',)], start_row=9,
             bold_first=False)
    bold(ws, 'A9', 'A10', 'A11')
    if finished:
        formula(ws, 'B9', '=MIN(B2:B8)')
        formula(ws, 'B10', '=MAX(B2:B8)')
        formula(ws, 'B11', '=COUNT(B2:B8)')


runs = [r for _, r in RUNS if isinstance(r, (int, float))]

FILES = [
    XlsxFile('test-marks', build_test_marks, {
        'B8': min(marks), 'B9': max(marks), 'B10': len(marks),
    }),
    XlsxFile('cricket-runs', build_cricket_runs, {
        'B9': min(runs), 'B10': max(runs), 'B11': len(runs),
    }),
]

# The lesson states these results; keep them in step with the page.
assert (min(marks), max(marks), len(marks)) == (62, 91, 5)
with_50 = marks + [50]  # step 5: Hamza gets 50
assert (min(with_50), len(with_50)) == (50, 6)
assert (min(runs), max(runs), len(runs)) == (0, 67, 6)
