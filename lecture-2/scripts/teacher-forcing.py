'''Every prefix of one sentence is one training example.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, BORDER, EMERALD, EMERALD_SOFT, INK, INK_SOFT, SURFACE, blank, figsize, save, use_style

SENTENCE = ['The', 'region', 'grew', 'in', '2019']

ROW_TOP, ROW_STEP, HEIGHT = 0.84, 0.21, 0.135
LEFT, GAP = 0.02, 0.010
TARGET_X = 0.68


def width(word: str) -> float:
    return 0.026 * len(word) + 0.040


def row(ax: Axes, y: float, context: list[str], target_word: str, last: bool) -> None:
    x = LEFT
    for word in context:
        box(ax, x, y, x + width(word), y + HEIGHT, word, SURFACE, BORDER, INK, size=11.5, family='monospace', rounding=0.008)
        x += width(word) + GAP

    harrow(ax, x + 0.012, TARGET_X - 0.012, y + HEIGHT / 2, ACCENT, scale=12, linewidth=1.1)
    box(ax, TARGET_X, y, TARGET_X + width(target_word), y + HEIGHT, target_word, EMERALD_SOFT, EMERALD, EMERALD, size=11.5, family='monospace', rounding=0.008)

    if last:
        ax.text(LEFT + 0.02, y - 0.085, 'the whole sequence so far is the input', fontsize=11, color=ACCENT)


def teacher_forcing() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.88, 0.46))
    blank(ax)

    for index in range(1, len(SENTENCE)):
        y = ROW_TOP - (index - 1) * ROW_STEP
        row(ax, y, SENTENCE[:index], SENTENCE[index], index == len(SENTENCE) - 1)

    ax.text(LEFT, ROW_TOP + HEIGHT + 0.06, 'context', fontsize=12, color=INK_SOFT)
    ax.text(TARGET_X, ROW_TOP + HEIGHT + 0.06, 'next token', fontsize=12, color=EMERALD)

    ax.set_xlim(0.0, 0.90)
    ax.set_ylim(0.06, 1.02)
    save(fig, target('teacher-forcing'))


if __name__ == '__main__':
    use_style()
    teacher_forcing()
