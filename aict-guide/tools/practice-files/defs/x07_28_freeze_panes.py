"""Lesson 7.28: Freeze Panes for Long Lists.

Freezing has no formulas, so there are no answer cells to recalculate (`expected` is empty).
The finished files are frozen the way the lesson ends; the asserts below check the freeze
settings and every value the lesson states.
"""

from xlsxkit import XlsxFile, new_workbook, put_rows

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'freeze-panes.mdx'
FOLDER = 'freeze-panes'

# Step by Step: a school's list of 50 students (made-up names).
NAMES = [
    'Ahmed', 'Aiman', 'Ali', 'Alina', 'Amna', 'Anas', 'Areeba', 'Arham', 'Asad', 'Ayesha',
    'Bilal', 'Dua', 'Eman', 'Faisal', 'Fatima', 'Hamza', 'Haris', 'Hiba', 'Hira', 'Huda',
    'Ibrahim', 'Iqra', 'Junaid', 'Kamran', 'Khadija', 'Laiba', 'Maham', 'Maryam', 'Moiz', 'Musa',
    'Nida', 'Noman', 'Omar', 'Rabia', 'Rafay', 'Saad', 'Sadia', 'Sana', 'Shahzaib', 'Sidra',
    'Talha', 'Tooba', 'Umair', 'Usman', 'Wajiha', 'Yasir', 'Zain', 'Zainab', 'Zara', 'Zoya',
]
FATHERS = ['Abdul Rauf', 'Khalid Mehmood', 'Tariq Aziz', 'Nadeem Akhtar', 'Shahid Iqbal',
           'Imran Saeed', 'Javed Anwar', 'Arshad Ali', 'Naveed Ahmed', 'Zafar Hussain', 'Rashid Khan']
FEE = {6: 2000, 7: 2200, 8: 2400, 9: 2600, 10: 2800}
STUDENTS = [(i + 1, name, FATHERS[(i * 7) % len(FATHERS)], 6 + i % 5, FEE[6 + i % 5])
            for i, name in enumerate(NAMES)]


def build_student_list(wb, finished):
    """Finished: the end of Step by Step, top row frozen."""
    ws = wb.active
    put_rows(ws, [('Roll No', 'Student Name', "Father's Name", 'Grade', 'Fee (Rs)'), *STUDENTS])
    if finished:
        ws.freeze_panes = 'A2'


# Practice: a general store's daily sales register for October: units of 40 items sold on each
# day. The 31 day columns (B to AF) are too wide for one screen, so freezing column A matters.
ITEMS = [
    'Atta (10 kg bag)', 'Basmati rice (kg)', 'Sella rice (kg)', 'Sugar (kg)', 'Salt (pack)',
    'Tea (pack)', 'Cooking oil (litre)', 'Ghee (kg)', 'Daal chana (kg)', 'Daal masoor (kg)',
    'Daal moong (kg)', 'White chana (kg)', 'Red chilli (pack)', 'Turmeric (pack)',
    'Coriander powder (pack)', 'Garam masala (pack)', 'Milk pack (litre)', 'Yogurt (500 g)',
    'Eggs (dozen)', 'Bread', 'Rusk (pack)', 'Biscuits (pack)', 'Jam (jar)', 'Ketchup (bottle)',
    'Vermicelli (pack)', 'Custard (pack)', 'Jelly (pack)', 'Soap', 'Shampoo (bottle)',
    'Toothpaste', 'Toothbrush', 'Washing powder (1 kg)', 'Dishwash bar', 'Matchbox',
    'Candles (pack)', 'Tissue box', 'Mineral water (1.5 l)', 'Juice (1 l)', 'Notebook',
    'Ballpoint pen',
]
DAYS = [f'{d} Oct' for d in range(1, 32)]
SALES = [[2 + (i * i * 7 + d * d * 3 + i * d * 5 + i + 2 * d) % 17 for d in range(31)]
         for i in range(len(ITEMS))]


def build_sales_log(wb, finished):
    """Finished: the end of Practice, row 1 and column A frozen (cell B2)."""
    ws = wb.active
    put_rows(ws, [('Item', *DAYS), *([item, *units] for item, units in zip(ITEMS, SALES))])
    if finished:
        ws.freeze_panes = 'B2'


FILES = [
    XlsxFile('student-list', build_student_list),
    XlsxFile('sales-log', build_sales_log),
]

# The lesson states these values; keep them in step with the page.
assert len(NAMES) == len(set(NAMES)) == 50 and len(STUDENTS) == 50
assert STUDENTS[-1] == (50, 'Zoya', 'Tariq Aziz', 10, 2800)             # row 51
assert STUDENTS[29] == (30, 'Musa', 'Imran Saeed', 10, 2800)            # row 31
assert STUDENTS[0] == (1, 'Ahmed', 'Abdul Rauf', 6, 2000)               # row 2
assert len(ITEMS) == len(set(ITEMS)) == 40                              # rows 2 to 41
assert len(DAYS) == 31 and DAYS[-1] == '31 Oct'                         # columns B to AF
assert ITEMS[-1] == 'Ballpoint pen' and SALES[-1][-1] == 3              # cell AF41
assert ITEMS[0] == 'Atta (10 kg bag)' and SALES[0][-1] == 8             # cell AF2
assert SALES[-1][0] == 12                                               # cell B41

for _build, _cell in ((build_student_list, 'A2'), (build_sales_log, 'B2')):
    _wb = new_workbook()
    _build(_wb, True)
    assert _wb.active.freeze_panes == _cell
    _wb = new_workbook()
    _build(_wb, False)
    assert _wb.active.freeze_panes is None
_wb = new_workbook()
build_sales_log(_wb, True)
assert _wb.active['AF41'].value == 3 and _wb.active['A41'].value == 'Ballpoint pen'
assert _wb.active['AF1'].value == '31 Oct' and _wb.active['AF2'].value == 8
assert _wb.active['B41'].value == 12 and _wb.active['B1'].value == '1 Oct'
_wb = new_workbook()
build_student_list(_wb, True)
assert _wb.active['B51'].value == 'Zoya' and _wb.active['A51'].value == 50
