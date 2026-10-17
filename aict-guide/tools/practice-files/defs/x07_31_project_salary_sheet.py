"""Lesson 7.31: Project: Monthly Salary Sheet.

Two salary sheets with the same layout:
  A1:B4 the rates, each in one cell (B1 house rent %, B2 medical %, B3 deduction % (a made-up
  practice rate, not real tax law), B4 full-attendance bonus in rupees);
  row 6 headings: A Name, B Basic Pay (Rs), C Days Absent, D House Rent (Rs), E Medical (Rs),
  F Gross Pay (Rs), G Deduction (Rs), H Bonus (Rs), I Net Pay (Rs);
  staff from row 7; a Total row right below the staff.
House Rent = B*$B$1; Medical = B*$B$2; Gross = B+D+E; Deduction = F*$B$3;
Bonus = IF(C=0,$B$4,0); Net = F-G+H. The Total row adds columns B to I (C = days absent).

Starter: rates and staff (data only); the rates are typed as plain numbers (0.4 …), so the
student applies Percent Style. Finished: formulas, Percent Style on B1:B3. The Practice finished
file shows the end of the task, with the bonus changed to 1500.
"""

from xlsxkit import XlsxFile, put_rows, formula, bold

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'project-salary-sheet.mdx'
FOLDER = 'project-salary-sheet'

HEADINGS = ('Name', 'Basic Pay (Rs)', 'Days Absent', 'House Rent (Rs)', 'Medical (Rs)',
            'Gross Pay (Rs)', 'Deduction (Rs)', 'Bonus (Rs)', 'Net Pay (Rs)')
LABELS = ('House rent rate', 'Medical rate', 'Deduction rate (practice only)',
          'Full attendance bonus (Rs)')
FIRST = 7

# Step by Step: a small travel agency office in Multan.
OFFICE = dict(rates=(0.40, 0.10, 0.05, 2000), staff=[
    ('Asad Mehmood', 40000, 0), ('Rubina Kausar', 32000, 2), ('Faisal Iqbal', 28000, 0),
    ('Hina Shah', 36000, 1), ('Tahir Abbas', 25000, 0), ('Mehwish Ali', 30000, 3)])
# Practice: a bakery's workers. The bonus later goes up from 1000 to 1500 (one cell, B4).
BAKERY = dict(rates=(0.30, 0.05, 0.02, 1000), staff=[
    ('Naveed Akram', 25000, 0), ('Shazia Parveen', 20000, 1), ('Arif Hussain', 22000, 0),
    ('Kiran Javed', 18000, 2), ('Sajid Mehmood', 16000, 0)])
BAKERY_NEW_BONUS = 1500


def make_builder(sheet, final_rates):
    staff = sheet['staff']
    last = FIRST + len(staff) - 1
    total = last + 1

    def build(wb, finished):
        ws = wb.active
        rates = final_rates if finished else sheet['rates']
        put_rows(ws, list(zip(LABELS, rates)), bold_first=False)
        bold(ws, 'A1', 'A2', 'A3', 'A4')
        put_rows(ws, [HEADINGS, *staff], start_row=6)
        ws[f'A{total}'] = 'Total'
        bold(ws, f'A{total}')
        if not finished:
            return
        for ref in ('B1', 'B2', 'B3'):
            ws[ref].number_format = '0%'
        for r in range(FIRST, last + 1):
            formula(ws, f'D{r}', f'=B{r}*$B$1')
            formula(ws, f'E{r}', f'=B{r}*$B$2')
            formula(ws, f'F{r}', f'=B{r}+D{r}+E{r}')
            formula(ws, f'G{r}', f'=F{r}*$B$3')
            formula(ws, f'H{r}', f'=IF(C{r}=0,$B$4,0)')
            formula(ws, f'I{r}', f'=F{r}-G{r}+H{r}')
        for col in 'BCDEFGHI':
            formula(ws, f'{col}{total}', f'=SUM({col}{FIRST}:{col}{last})')
    return build


def expected_for(sheet, rates):
    hr, med, ded, bonus = rates
    exp = {}
    rows = []
    absences = 0
    for r, (_, basic, absent) in enumerate(sheet['staff'], start=FIRST):
        absences += absent
        d = basic * hr
        e = basic * med
        f = basic + d + e
        g = f * ded
        h = bonus if absent == 0 else 0
        i = f - g + h
        rows.append((basic, d, e, f, g, h, i))
        for col, v in zip('DEFGHI', (d, e, f, g, h, i)):
            exp[f'{col}{r}'] = v
    total = FIRST + len(rows)
    for k, col in enumerate('BDEFGHI'):
        exp[f'{col}{total}'] = sum(row[k] for row in rows)
    exp[f'C{total}'] = absences
    return exp


office = expected_for(OFFICE, OFFICE['rates'])
BAKERY_FINAL = BAKERY['rates'][:3] + (BAKERY_NEW_BONUS,)
bakery_before = expected_for(BAKERY, BAKERY['rates'])
bakery = expected_for(BAKERY, BAKERY_FINAL)

FILES = [
    XlsxFile('office-salary', make_builder(OFFICE, OFFICE['rates']), office),
    XlsxFile('bakery-salary', make_builder(BAKERY, BAKERY_FINAL), bakery),
]


# The lesson states these results; keep them in step with the page.
def column(exp, col, first, last):
    return [round(exp[f'{col}{r}'], 6) for r in range(first, last + 1)]


assert column(office, 'D', 7, 12) == [16000, 12800, 11200, 14400, 10000, 12000]
assert column(office, 'E', 7, 12) == [4000, 3200, 2800, 3600, 2500, 3000]
assert column(office, 'F', 7, 12) == [60000, 48000, 42000, 54000, 37500, 45000]
assert column(office, 'G', 7, 12) == [3000, 2400, 2100, 2700, 1875, 2250]
assert column(office, 'H', 7, 12) == [2000, 0, 2000, 0, 2000, 0]
assert column(office, 'I', 7, 12) == [59000, 45600, 41900, 51300, 37625, 42750]
assert column(office, 'B', 13, 13) + [round(office[f'{c}13'], 6) for c in 'DEFGHI'] == [
    191000, 76400, 19100, 286500, 14325, 6000, 278175]

assert column(bakery_before, 'F', 7, 11) == [33750, 27000, 29700, 24300, 21600]
assert column(bakery_before, 'G', 7, 11) == [675, 540, 594, 486, 432]
assert column(bakery_before, 'H', 7, 11) == [1000, 0, 1000, 0, 1000]
assert column(bakery_before, 'I', 7, 11) == [34075, 26460, 30106, 23814, 22168]
assert round(bakery_before['I12'], 6) == 136623
assert column(bakery, 'D', 7, 11) == [7500, 6000, 6600, 5400, 4800]
assert column(bakery, 'E', 7, 11) == [1250, 1000, 1100, 900, 800]
assert column(bakery, 'H', 7, 11) == [1500, 0, 1500, 0, 1500]
assert column(bakery, 'I', 7, 11) == [34575, 26460, 30606, 23814, 22668]
assert column(bakery, 'B', 12, 12) + [round(bakery[f'{c}12'], 6) for c in 'DEFGHI'] == [
    101000, 30300, 5050, 136350, 2727, 4500, 138123]
assert office['C13'] == 6 and bakery['C12'] == 3
