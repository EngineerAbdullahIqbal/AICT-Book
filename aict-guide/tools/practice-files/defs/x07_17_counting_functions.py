"""Lesson 7.17: Counting: COUNTA, COUNTBLANK, COUNTIF and COUNTIFS."""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'counting-functions.mdx'
FOLDER = 'counting-functions'

# Step by Step: a tuition centre's fee register. An empty fee cell (None) means the fee is not
# paid yet. The answers go in F2:G7 (labels in F, formulas in G).
REGISTER = [
    ('Ayesha', 'Science', 2000, 72),
    ('Bilal', 'Arts', None, 35),
    ('Hira', 'Science', 2000, 58),
    ('Kamran', 'Arts', 2500, 81),
    ('Maryam', 'Science', None, 39),
    ('Noman', 'Arts', 2500, 44),
    ('Rabia', 'Science', 2000, 90),
    ('Saad', 'Arts', None, 28),
]
REGISTER_LABELS = ['Students', 'Fees paid', 'Fees not paid', 'Science students',
                   'Passed (40 or more)', 'Science passes']


def build_fee_register(wb, finished):
    ws = wb.active
    put_rows(ws, [('Student', 'Group', 'Fee Paid (Rs)', 'Test Marks'), *REGISTER])
    put_rows(ws, [('What we count', 'Answer'), *[(label,) for label in REGISTER_LABELS]],
             start_col=6)
    if finished:
        formula(ws, 'G2', '=COUNTA(A2:A9)')
        formula(ws, 'G3', '=COUNT(C2:C9)')
        formula(ws, 'G4', '=COUNTBLANK(C2:C9)')
        formula(ws, 'G5', '=COUNTIF(B2:B9,"Science")')
        formula(ws, 'G6', '=COUNTIF(D2:D9,">=40")')
        formula(ws, 'G7', '=COUNTIFS(B2:B9,"Science",D2:D9,">=40")')


reg_students = len([r for r in REGISTER if r[0] is not None])
reg_paid = len([r for r in REGISTER if isinstance(r[2], (int, float))])
reg_unpaid = len([r for r in REGISTER if r[2] is None])
reg_science = len([r for r in REGISTER if r[1] == 'Science'])
reg_passed = len([r for r in REGISTER if r[3] >= 40])
reg_science_passed = len([r for r in REGISTER if r[1] == 'Science' and r[3] >= 40])

# Practice: a computer centre's course list. An empty marks cell means the student missed the
# exam. The answers go in E2:F7.
COURSES = [
    ('Adeel', 'MS Office', 66),
    ('Bushra', 'Typing', None),
    ('Danish', 'MS Office', 48),
    ('Farah', 'Graphics', 75),
    ('Ghazala', 'Typing', 52),
    ('Haris', 'MS Office', None),
    ('Iqra', 'Graphics', 38),
    ('Junaid', 'MS Office', 81),
    ('Kiran', 'Typing', 45),
]
COURSE_LABELS = ['Students', 'Sat the exam', 'Missed the exam', 'MS Office students',
                 'Passed (50 or more)', 'MS Office passes']


def build_course_list(wb, finished):
    ws = wb.active
    put_rows(ws, [('Student', 'Course', 'Exam Marks'), *COURSES])
    put_rows(ws, [('What we count', 'Answer'), *[(label,) for label in COURSE_LABELS]],
             start_col=5)
    if finished:
        formula(ws, 'F2', '=COUNTA(A2:A10)')
        formula(ws, 'F3', '=COUNT(C2:C10)')
        formula(ws, 'F4', '=COUNTBLANK(C2:C10)')
        formula(ws, 'F5', '=COUNTIF(B2:B10,"MS Office")')
        formula(ws, 'F6', '=COUNTIF(C2:C10,">=50")')
        formula(ws, 'F7', '=COUNTIFS(B2:B10,"MS Office",C2:C10,">=50")')


def _has_marks(row):
    return isinstance(row[2], (int, float))


c_students = len(COURSES)
c_sat = len([r for r in COURSES if _has_marks(r)])
c_missed = len([r for r in COURSES if r[2] is None])
c_office = len([r for r in COURSES if r[1] == 'MS Office'])
c_passed = len([r for r in COURSES if _has_marks(r) and r[2] >= 50])
c_office_passed = len([r for r in COURSES if r[1] == 'MS Office' and _has_marks(r) and r[2] >= 50])

FILES = [
    XlsxFile('fee-register', build_fee_register, {
        'G2': reg_students, 'G3': reg_paid, 'G4': reg_unpaid,
        'G5': reg_science, 'G6': reg_passed, 'G7': reg_science_passed,
    }),
    XlsxFile('course-list', build_course_list, {
        'F2': c_students, 'F3': c_sat, 'F4': c_missed,
        'F5': c_office, 'F6': c_passed, 'F7': c_office_passed,
    }),
]

# The lesson states these results; keep them in step with the page.
assert (reg_students, reg_paid, reg_unpaid) == (8, 5, 3)
assert (reg_science, reg_passed, reg_science_passed) == (4, 5, 3)
assert (c_students, c_sat, c_missed) == (9, 7, 2)
assert (c_office, c_passed, c_office_passed) == (4, 4, 2)
