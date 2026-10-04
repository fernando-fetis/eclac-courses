#!/usr/bin/env python3
'''Report slides whose content spills onto the following page.

The theme leaves two invisible markers on every slide (`slide-start` and `slide-end`). If they do not land on the same page, the slide overflowed.

    python3 common/scripts/check-overflow.py lecture-1/slides.typ
'''

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def query(source: Path, label: str) -> list[int]:
    result = subprocess.run(['typst', 'query', '--root', str(ROOT), str(source), f'<{label}>', '--field', 'value'], capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(result.stderr.strip() or f'typst query failed on <{label}>')
    return json.loads(result.stdout)


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    source = Path(sys.argv[1])
    starts = query(source, 'slide-start')
    ends = query(source, 'slide-end')
    overflowing = [(number, start, end) for number, (start, end) in enumerate(zip(starts, ends), start=1) if start != end]

    print(f'{source}: {len(starts)} slides')
    if not overflowing:
        print('None overflow.')
        return 0
    print(f'{len(overflowing)} overflow:')
    for number, start, end in overflowing:
        print(f'  slide {number}: starts on page {start}, ends on page {end}')
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
