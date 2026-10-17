"""Lesson 7.16: More Decisions: IFS, AND and OR."""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'ifs-and-or.mdx'
FOLDER = 'ifs-and-or'

# Step by Step: three subjects, each out of 100. Percentage = average of the three.
# Made-up grade bands: A 80+, B 70-79, C 60-69, D 40-59, F below 40. Pass mark: 40 in every subject.
MARKS = [('Ali', 85, 78, 92), ('Sana', 66, 74, 70), ('Hamza', 35, 70, 81),
         ('Fatima', 55, 48, 41), ('Usman', 30, 42, 36), ('Zainab', 90, 62, 79)]


def build_subject_marks(wb, finished):
    ws = wb.active
    put_rows(ws, [('Student', 'Maths', 'English', 'Urdu', 'Percentage', 'Grade', 'All subjects'),
                  *MARKS])
    if finished:
        for r in range(2, 2 + len(MARKS)):
            formula(ws, f'E{r}', f'=AVERAGE(B{r}:D{r})')
            formula(ws, f'F{r}', f'=IFS(E{r}>=80,"A",E{r}>=70,"B",E{r}>=60,"C",E{r}>=40,"D",TRUE,"F")')
            formula(ws, f'G{r}', f'=IF(AND(B{r}>=40,C{r}>=40,D{r}>=40),"Pass","Fail")')


def grade(p):
    if p >= 80:
        return 'A'
    if p >= 70:
        return 'B'
    if p >= 60:
        return 'C'
    if p >= 40:
        return 'D'
    return 'F'


percentages = [sum(m) / 3 for _, *m in MARKS]
grades = [grade(p) for p in percentages]
all_pass = ['Pass' if all(x >= 40 for x in m) else 'Fail' for _, *m in MARKS]
marks_expected = {}
for i, r in enumerate(range(2, 2 + len(MARKS))):
    marks_expected[f'E{r}'] = percentages[i]
    marks_expected[f'F{r}'] = grades[i]
    marks_expected[f'G{r}'] = all_pass[i]

# Practice: a tuition centre. Classes on Mon, Wed and Fri (P = present, A = absent).
# Test out of 50. A certificate needs no absence AND 40 or more in the test.
ATTENDANCE = [('Bilal', 'P', 'P', 'P', 45), ('Mahnoor', 'P', 'A', 'P', 48),
              ('Danish', 'P', 'P', 'P', 32), ('Iqra', 'A', 'P', 'A', 41),
              ('Faisal', 'P', 'P', 'P', 40), ('Hira', 'P', 'P', 'A', 47)]


def build_tuition_attendance(wb, finished):
    ws = wb.active
    put_rows(ws, [('Student', 'Mon', 'Wed', 'Fri', 'Any absence?', 'Test (out of 50)', 'Certificate')])
    for i, (name, mon, wed, fri, test) in enumerate(ATTENDANCE):
        r = 2 + i
        put_rows(ws, [(name, mon, wed, fri, None, test)], start_row=r, bold_first=False)
        if finished:
            formula(ws, f'E{r}', f'=IF(OR(B{r}="A",C{r}="A",D{r}="A"),"Yes","No")')
            formula(ws, f'G{r}', f'=IF(AND(E{r}="No",F{r}>=40),"Yes","No")')


absence = ['Yes' if 'A' in days else 'No' for _, *days, _ in ATTENDANCE]
certificate = ['Yes' if a == 'No' and t >= 40 else 'No' for a, (*_, t) in zip(absence, ATTENDANCE)]
attendance_expected = {}
for i, r in enumerate(range(2, 2 + len(ATTENDANCE))):
    attendance_expected[f'E{r}'] = absence[i]
    attendance_expected[f'G{r}'] = certificate[i]

FILES = [
    XlsxFile('subject-marks', build_subject_marks, marks_expected),
    XlsxFile('tuition-attendance', build_tuition_attendance, attendance_expected),
]

# The lesson states these results; keep them in step with the page.
assert percentages == [85, 70, 62, 48, 36, 77]
assert grades == ['A', 'B', 'C', 'D', 'F', 'B']
assert all_pass == ['Pass', 'Pass', 'Fail', 'Pass', 'Fail', 'Pass']
assert absence == ['No', 'Yes', 'No', 'Yes', 'No', 'Yes']
assert certificate == ['Yes', 'No', 'No', 'No', 'Yes', 'No']
