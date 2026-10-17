"""Lesson 7.22: Joining and Changing Text."""

from xlsxkit import XlsxFile, put_rows, formula

APP = 'excel'
MODULE = 'module-07-ms-excel'
LESSON_FILE = 'joining-and-changing-text.mdx'
FOLDER = 'joining-and-changing-text'


# Python versions of the Excel functions, following Microsoft's descriptions.
def trim(text):
    """TRIM: 'Removes all spaces from text except for single spaces between words.'"""
    return ' '.join(w for w in text.split(' ') if w)


def proper(text):
    """PROPER: capital after any non-letter (and at the start); all other letters small."""
    out, after_letter = [], False
    for ch in text:
        out.append(ch.lower() if after_letter else ch.upper())
        after_letter = ch.isalpha()
    return ''.join(out)


def dots(text):
    """The lesson page shows each space as a middle dot (·)."""
    return text.replace(' ', '·')


# Step by Step, part 1 (rows 1-6): an admission list. Join first and last names.
NAMES = [('Ayesha', 'Siddiqui'), ('Hamza', 'Qureshi'), ('Mehwish', 'Anwar'), ('Usman', 'Tariq'),
         ('Sadia', 'Malik')]
# Part 2 (rows 8-11): names typed in a hurry, with extra spaces and Caps Lock mistakes.
MESSY = ['  zainab   bibi', 'KAMRAN  AKHTAR  ', '  nOOR fATIMA']


def build_admission_list(wb, finished):
    ws = wb.active
    put_rows(ws, [('First name', 'Last name', 'Full name', 'Full name (CONCAT)',
                   'For certificate'), *NAMES])
    put_rows(ws, [('Name as typed', 'Spaces removed', 'Small letters', 'Clean name'),
                  *[(m,) for m in MESSY]], start_row=8)
    if finished:
        for r in range(2, 2 + len(NAMES)):
            formula(ws, f'C{r}', f'=A{r}&" "&B{r}')
            formula(ws, f'D{r}', f'=CONCAT(A{r}," ",B{r})')
            formula(ws, f'E{r}', f'=UPPER(C{r})')
        for r in range(9, 9 + len(MESSY)):
            formula(ws, f'B{r}', f'=TRIM(A{r})')
            formula(ws, f'C{r}', f'=LOWER(B{r})')
            formula(ws, f'D{r}', f'=PROPER(B{r})')


full = [f'{a} {b}' for a, b in NAMES]
admission_expected = {}
for r, name in zip(range(2, 7), full):
    admission_expected.update({f'C{r}': name, f'D{r}': name, f'E{r}': name.upper()})
trimmed = [trim(m) for m in MESSY]
for r, t in zip(range(9, 12), trimmed):
    admission_expected.update({f'B{r}': t, f'C{r}': t.lower(), f'D{r}': proper(t)})

# Practice: a shop's home-delivery customer list, typed in a hurry. The finished file shows the
# end of the task, after Rashid's city is changed to "rawalpindi" (Practice step 6).
CUSTOMERS = [('rashid  mehmood', 'lahore'), ('  SAIMA BATOOL', 'KARACHI  '),
             ('imran ali  ', '  multan'), ('fOZIA nAZ', 'Faisalabad'),
             ('Tahir   Abbas', 'peshawar')]
CUSTOMERS_AFTER_CHANGE = [('rashid  mehmood', 'rawalpindi')] + CUSTOMERS[1:]


def build_customer_list(wb, finished):
    ws = wb.active
    rows = CUSTOMERS_AFTER_CHANGE if finished else CUSTOMERS
    put_rows(ws, [('Name as typed', 'City as typed', 'Clean name', 'Clean city', 'Label'),
                  *rows])
    if finished:
        for r in range(2, 2 + len(rows)):
            formula(ws, f'C{r}', f'=PROPER(TRIM(A{r}))')
            formula(ws, f'D{r}', f'=PROPER(TRIM(B{r}))')
            formula(ws, f'E{r}', f'=CONCAT(C{r},", ",D{r})')


def clean_customers(rows):
    return [(proper(trim(n)), proper(trim(c))) for n, c in rows]


clean_before = clean_customers(CUSTOMERS)
clean_after = clean_customers(CUSTOMERS_AFTER_CHANGE)
customer_expected = {}
for r, (n, c) in zip(range(2, 7), clean_after):
    customer_expected.update({f'C{r}': n, f'D{r}': c, f'E{r}': f'{n}, {c}'})

FILES = [
    XlsxFile('admission-list', build_admission_list, admission_expected),
    XlsxFile('customer-list', build_customer_list, customer_expected),
]

# The lesson states these results; keep them in step with the page.
assert full == ['Ayesha Siddiqui', 'Hamza Qureshi', 'Mehwish Anwar', 'Usman Tariq', 'Sadia Malik']
assert [dots(m) for m in MESSY] == ['··zainab···bibi', 'KAMRAN··AKHTAR··', '··nOOR·fATIMA']
assert trimmed == ['zainab bibi', 'KAMRAN AKHTAR', 'nOOR fATIMA']
assert [t.lower() for t in trimmed] == ['zainab bibi', 'kamran akhtar', 'noor fatima']
assert [proper(t) for t in trimmed] == ['Zainab Bibi', 'Kamran Akhtar', 'Noor Fatima']
assert [dots(n) for n, _ in CUSTOMERS] == ['rashid··mehmood', '··SAIMA·BATOOL', 'imran·ali··',
                                         'fOZIA·nAZ', 'Tahir···Abbas']
assert [dots(c) for _, c in CUSTOMERS] == ['lahore', 'KARACHI··', '··multan', 'Faisalabad',
                                         'peshawar']
assert clean_before == [('Rashid Mehmood', 'Lahore'), ('Saima Batool', 'Karachi'),
                        ('Imran Ali', 'Multan'), ('Fozia Naz', 'Faisalabad'),
                        ('Tahir Abbas', 'Peshawar')]
assert clean_after[0] == ('Rashid Mehmood', 'Rawalpindi') and clean_after[1:] == clean_before[1:]
# Microsoft's own examples, to check the Python versions above.
assert proper('this is a TITLE') == 'This Is A Title' and proper('2-way street') == '2-Way Street'
assert proper('76BudGet') == '76Budget' and trim(' First Quarter Earnings ') == 'First Quarter Earnings'
