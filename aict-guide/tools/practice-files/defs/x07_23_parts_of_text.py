"""Lesson 7.23: Parts of Text: LEFT, RIGHT, MID and LEN.

All codes are made up. LEFT, RIGHT and MID give back text, so the expected values are strings
(the zero in front of "015" stays).
"""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'parts-of-text.mdx'
FOLDER = 'parts-of-text'

# Step by Step: roll codes at a computer institute: city - year - number. Row 4 is typed wrong
# at first (one digit missing). Step by Step fixes it, so the finished file has the right code.
ROLL_CODES = ['LHR-2026-015', 'KHI-2025-102', 'ISB-2026-07', 'MUL-2024-230', 'PEW-2026-041']
ROLL_FIXED = {'ISB-2026-07': 'ISB-2026-007'}


def roll_rows(finished):
    return [ROLL_FIXED.get(c, c) if finished else c for c in ROLL_CODES]


def build_roll_codes(wb, finished):
    ws = wb.active
    put_rows(ws, [('Roll code', 'City', 'Year', 'Number', 'Length'),
                  *[(c,) for c in roll_rows(finished)]])
    if finished:
        for r in range(2, 2 + len(ROLL_CODES)):
            formula(ws, f'B{r}', f'=LEFT(A{r},3)')
            formula(ws, f'C{r}', f'=MID(A{r},5,4)')
            formula(ws, f'D{r}', f'=RIGHT(A{r},3)')
            formula(ws, f'E{r}', f'=LEN(A{r})')


def roll_parts(code):
    # LEFT(text,3); MID(text,5,4) starts at character 5 (positions count from 1); RIGHT(text,3)
    return code[:3], code[4:8], code[-3:], len(code)


roll_before = [roll_parts(c) for c in roll_rows(False)]
roll_after = [roll_parts(c) for c in roll_rows(True)]
roll_expected = {}
for r, (city, year, number, length) in zip(range(2, 7), roll_after):
    roll_expected.update({f'B{r}': city, f'C{r}': year, f'D{r}': number, f'E{r}': length})

# Practice: a shoe shop's stock codes: type (4 letters) - size (2 digits) - colour (3 letters).
# A good code has 11 characters. Row 6 is typed wrong at first; Practice fixes it.
SHOE_CODES = ['SHOE-41-BLK', 'SNDL-38-BRN', 'SHOE-43-BRN', 'KHSA-39-RED', 'SNDL-4-BLK',
              'SHOE-36-BLK']
SHOE_FIXED = {'SNDL-4-BLK': 'SNDL-40-BLK'}
GOOD_LENGTH = 11


def shoe_rows(finished):
    return [SHOE_FIXED.get(c, c) if finished else c for c in SHOE_CODES]


def build_shoe_codes(wb, finished):
    ws = wb.active
    put_rows(ws, [('Code', 'Type', 'Size', 'Colour', 'Length', 'Check'),
                  *[(c,) for c in shoe_rows(finished)]])
    if finished:
        for r in range(2, 2 + len(SHOE_CODES)):
            formula(ws, f'B{r}', f'=LEFT(A{r},4)')
            formula(ws, f'C{r}', f'=MID(A{r},6,2)')
            formula(ws, f'D{r}', f'=RIGHT(A{r},3)')
            formula(ws, f'E{r}', f'=LEN(A{r})')
            formula(ws, f'F{r}', f'=IF(E{r}=11,"OK","Check code")')


def shoe_parts(code):
    n = len(code)
    return code[:4], code[5:7], code[-3:], n, 'OK' if n == GOOD_LENGTH else 'Check code'


shoe_before = [shoe_parts(c) for c in shoe_rows(False)]
shoe_after = [shoe_parts(c) for c in shoe_rows(True)]
shoe_expected = {}
for r, parts in zip(range(2, 8), shoe_after):
    shoe_expected.update({f'{col}{r}': v for col, v in zip('BCDEF', parts)})

FILES = [
    XlsxFile('roll-codes', build_roll_codes, roll_expected),
    XlsxFile('shoe-codes', build_shoe_codes, shoe_expected),
]

# The lesson states these results; keep them in step with the page.
assert roll_before[0] == ('LHR', '2026', '015', 12)
assert roll_before[2] == ('ISB', '2026', '-07', 11)
assert [p[3] for p in roll_before] == [12, 12, 11, 12, 12]
assert roll_after == [('LHR', '2026', '015', 12), ('KHI', '2025', '102', 12),
                      ('ISB', '2026', '007', 12), ('MUL', '2024', '230', 12),
                      ('PEW', '2026', '041', 12)]
assert shoe_before[0] == ('SHOE', '41', 'BLK', 11, 'OK')
assert shoe_before[4] == ('SNDL', '4-', 'BLK', 10, 'Check code')
assert [p[4] for p in shoe_before].count('Check code') == 1
assert [p[1] for p in shoe_after] == ['41', '38', '43', '39', '40', '36']
assert [p[0] for p in shoe_after] == ['SHOE', 'SNDL', 'SHOE', 'KHSA', 'SNDL', 'SHOE']
assert [p[2] for p in shoe_after] == ['BLK', 'BRN', 'BRN', 'RED', 'BLK', 'BLK']
assert all(p[3] == 11 and p[4] == 'OK' for p in shoe_after)
