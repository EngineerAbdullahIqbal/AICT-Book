"""Lesson 7.24: Dates: TODAY, NOW, Days Between Dates and DATEDIF.

Every checked answer uses fixed dates. TODAY() and NOW() change every day, so their cells (H1
and H2 of fee-record) are NOT in `expected`; the asserts at the end check that the finished file
has the formulas there and that the starter file leaves them empty.

Dates are real Excel dates shown in Short Date (built-in format 14), like Lesson 7.5. Answer
cells are kept in the General format, so the days show as numbers, not as dates.
"""

from datetime import date, datetime

from xlsxkit import XlsxFile, put_rows, formula, bold, new_workbook

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'working-with-dates.mdx'
FOLDER = 'working-with-dates'

SHORT_DATE = 'mm-dd-yy'          # openpyxl's name for Excel's built-in format 14 (Short Date)
DATE_TIME = 'm/d/yy h:mm'        # Excel's built-in format 22 (date and time)


def dt(y, m, d):
    return datetime(y, m, d)


def date_cells(ws, *refs):
    for ref in refs:
        ws[ref].number_format = SHORT_DATE


# Step by Step, part 1 and 2: a tuition centre's March fee, due on 10 March 2026.
FEES = [('Ayesha Khan', dt(2026, 3, 10), dt(2026, 3, 8)),
        ('Bilal Ahmed', dt(2026, 3, 10), dt(2026, 3, 10)),
        ('Hira Shah', dt(2026, 3, 10), dt(2026, 3, 17)),
        ('Danish Ali', dt(2026, 3, 10), dt(2026, 4, 2)),
        ('Mariam Javed', dt(2026, 3, 10), dt(2026, 3, 12))]


def build_fee_record(wb, finished):
    ws = wb.active
    put_rows(ws, [('Student', 'Due date', 'Paid on', 'Days late', 'Using DAYS'), *FEES])
    ws['G1'], ws['G2'] = 'Today', 'Now'
    bold(ws, 'G1', 'G2')
    for r in range(2, 2 + len(FEES)):
        date_cells(ws, f'B{r}', f'C{r}')
    if finished:
        for r in range(2, 2 + len(FEES)):
            formula(ws, f'D{r}', f'=C{r}-B{r}')
            formula(ws, f'E{r}', f'=DAYS(C{r},B{r})')
        formula(ws, 'H1', '=TODAY()')
        formula(ws, 'H2', '=NOW()')
        ws['H1'].number_format = SHORT_DATE
        ws['H2'].number_format = DATE_TIME


days_late = [(paid - due).days for _, due, paid in FEES]
fee_expected = {}
for r, d in zip(range(2, 7), days_late):
    fee_expected[f'D{r}'] = d
    fee_expected[f'E{r}'] = d


# Step by Step, part 3: age in complete years on the admission date (DATEDIF with "Y").
def complete_years(start, end):
    """Complete years from start to end, like DATEDIF(start, end, "Y")."""
    return end.year - start.year - ((end.month, end.day) < (start.month, start.day))


ADMISSIONS = [('Zara Hussain', dt(2021, 1, 15), dt(2026, 4, 1)),
              ('Omar Farooq', dt(2019, 6, 20), dt(2026, 4, 1)),
              ('Laiba Noor', dt(2021, 4, 1), dt(2026, 4, 1)),
              ('Ahmed Saleem', dt(2021, 4, 2), dt(2026, 4, 1)),
              ('Fatima Iqbal', dt(2022, 9, 10), dt(2026, 4, 6))]


def build_admission_ages(wb, finished):
    ws = wb.active
    put_rows(ws, [('Student', 'Date of birth', 'Admission date', 'Age in years'), *ADMISSIONS])
    for r in range(2, 2 + len(ADMISSIONS)):
        date_cells(ws, f'B{r}', f'C{r}')
    if finished:
        for r in range(2, 2 + len(ADMISSIONS)):
            formula(ws, f'D{r}', f'=DATEDIF(B{r},C{r},"Y")')


ages = [complete_years(born, adm) for _, born, adm in ADMISSIONS]
age_expected = {f'D{r}': a for r, a in zip(range(2, 7), ages)}

# Practice: an office's long-service award on 30 June 2026 (review date in G1, used with $G$1).
REVIEW = dt(2026, 6, 30)
AWARD_YEARS = 5
STAFF = [('Kamran Akhtar', dt(2018, 3, 15)), ('Sadia Parveen', dt(2021, 8, 1)),
         ('Naveed Iqbal', dt(2021, 6, 30)), ('Rubina Kausar', dt(2024, 1, 10)),
         ('Tariq Mehmood', dt(2021, 7, 1))]


def build_staff_service(wb, finished):
    ws = wb.active
    put_rows(ws, [('Name', 'Joining date', 'Days worked', 'Years', 'Award'),
                  *[(n, j) for n, j in STAFF]])
    ws['F1'], ws['G1'] = 'Review date', REVIEW
    bold(ws, 'F1')
    date_cells(ws, 'G1')
    for r in range(2, 2 + len(STAFF)):
        date_cells(ws, f'B{r}')
    if finished:
        for r in range(2, 2 + len(STAFF)):
            formula(ws, f'C{r}', f'=$G$1-B{r}')
            formula(ws, f'D{r}', f'=DATEDIF(B{r},$G$1,"Y")')
            formula(ws, f'E{r}', f'=IF(D{r}>=5,"Yes","No")')


days_worked = [(REVIEW - j).days for _, j in STAFF]
service_years = [complete_years(j, REVIEW) for _, j in STAFF]
awards = ['Yes' if y >= AWARD_YEARS else 'No' for y in service_years]
staff_expected = {}
for r, d, y, a in zip(range(2, 7), days_worked, service_years, awards):
    staff_expected.update({f'C{r}': d, f'D{r}': y, f'E{r}': a})

FILES = [
    XlsxFile('fee-record', build_fee_record, fee_expected),
    XlsxFile('admission-ages', build_admission_ages, age_expected),
    XlsxFile('staff-service', build_staff_service, staff_expected),
]

# The lesson states these results; keep them in step with the page.
assert days_late == [-2, 0, 7, 23, 2]
assert ages == [5, 6, 5, 4, 3]
assert days_worked == [3029, 1794, 1826, 902, 1825]
assert service_years == [8, 4, 5, 2, 4]
assert awards == ['Yes', 'No', 'Yes', 'No', 'No']
# Cross-checks with Python's own date maths (independent of complete_years).
assert (date(2026, 4, 2) - date(2026, 3, 10)).days == 23
assert date(2026, 6, 30) >= date(2021 + 5, 6, 30) and date(2026, 6, 30) < date(2021 + 5, 7, 1)


# TODAY and NOW: only the formula text is checked, never the result (it changes every day).
def _sheet(build, finished):
    wb = new_workbook()
    build(wb, finished)
    return wb.active


_fin, _start = _sheet(build_fee_record, True), _sheet(build_fee_record, False)
assert _fin['H1'].value == '=TODAY()' and _fin['H2'].value == '=NOW()'
assert _start['H1'].value is None and _start['H2'].value is None
assert 'H1' not in fee_expected and 'H2' not in fee_expected
