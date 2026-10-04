'''Path setup shared by every figure script in this lecture.'''

import pathlib
import sys

COMMON = pathlib.Path(__file__).resolve().parents[2] / 'common' / 'scripts'
FIGURES = pathlib.Path(__file__).resolve().parents[1] / 'figures'

sys.path.insert(0, str(COMMON))


def target(name: str) -> pathlib.Path:
    return FIGURES / f'{name}.pdf'
