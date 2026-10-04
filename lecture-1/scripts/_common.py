'''Path setup shared by every figure script in this lecture.'''

import sys
from pathlib import Path

COMMON = Path(__file__).resolve().parents[2] / 'common' / 'scripts'
FIGURES = Path(__file__).resolve().parents[1] / 'figures'

sys.path.insert(0, str(COMMON))


def target(name: str) -> Path:
    return FIGURES / f'{name}.pdf'
