"""Build every practice file into static/files/ (specs/practical-upgrade/spec.md §3).

Usage (from aict-guide/):  python3 tools/practice-files/build.py [lesson-folder ...]
"""

import importlib
import pkgutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from xlsxkit import new_workbook, fit_columns  # noqa: E402

STATIC = HERE.parent.parent / 'static' / 'files'


def load_defs():
    import defs
    for info in sorted(pkgutil.iter_modules(defs.__path__), key=lambda m: m.name):
        yield importlib.import_module(f'defs.{info.name}')


def output_dir(lesson) -> Path:
    return STATIC / lesson.APP / lesson.FOLDER


def build_lesson(lesson):
    out = output_dir(lesson)
    out.mkdir(parents=True, exist_ok=True)
    written = []
    for f in lesson.FILES:
        for finished in (False, True):
            wb = new_workbook()
            f.build(wb, finished)
            if f.fit == 'both' or (f.fit == 'finished' and finished):
                for ws in wb.worksheets:
                    fit_columns(ws)
            path = out / f"{f.name}-{'finished' if finished else 'starter'}.xlsx"
            wb.save(path)
            written.append(path)
    return written


def main(only):
    for lesson in load_defs():
        if only and lesson.FOLDER not in only:
            continue
        for path in build_lesson(lesson):
            print('built', path.relative_to(HERE.parent.parent))


if __name__ == '__main__':
    main(set(sys.argv[1:]))
