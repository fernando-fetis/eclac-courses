'''Several heads read the same sequence and their outputs are joined.'''

import matplotlib.pyplot as plt

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, GOLD, GOLD_SOFT, INK, INK_SUBTLE, SURFACE, blank, figsize, save, use_style

HEADS = ['head 1', 'head 2', 'head 3', 'head 4']

INPUT_X, INPUT_WIDTH = 0.02, 0.15
SPLIT_X = 0.23
HEAD_X, HEAD_WIDTH = 0.30, 0.18
MERGE_X = 0.55
JOIN_X, JOIN_WIDTH = 0.62, 0.19
OUTPUT_X, OUTPUT_WIDTH = 0.86, 0.15

TOP, STEP, HEIGHT = 0.84, 0.20, 0.135


def multi_head() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.94, 0.44))
    blank(ax)

    rows = [TOP - index * STEP + HEIGHT / 2 for index in range(len(HEADS))]
    middle = (rows[0] + rows[-1]) / 2

    box(ax, INPUT_X, middle - HEIGHT / 2, INPUT_X + INPUT_WIDTH, middle + HEIGHT / 2, 'input\nsequence', SURFACE, BORDER, INK, size=12, rounding=0.012)
    ax.plot([INPUT_X + INPUT_WIDTH + 0.008, SPLIT_X], [middle, middle], color=INK_SUBTLE, linewidth=1.1)
    ax.plot([SPLIT_X, SPLIT_X], [rows[-1], rows[0]], color=INK_SUBTLE, linewidth=1.1)
    ax.plot([MERGE_X, MERGE_X], [rows[-1], rows[0]], color=ACCENT, linewidth=1.1)

    for name, center in zip(HEADS, rows):
        harrow(ax, SPLIT_X, HEAD_X - 0.008, center, INK_SUBTLE, scale=11, linewidth=1.1)
        box(ax, HEAD_X, center - HEIGHT / 2, HEAD_X + HEAD_WIDTH, center + HEIGHT / 2, name, ACCENT_SOFT, ACCENT, ACCENT, size=12, rounding=0.012)
        ax.plot([HEAD_X + HEAD_WIDTH + 0.008, MERGE_X], [center, center], color=ACCENT, linewidth=1.1)

    harrow(ax, MERGE_X, JOIN_X - 0.008, middle, ACCENT, scale=12, linewidth=1.1)
    box(ax, JOIN_X, middle - HEIGHT / 2, JOIN_X + JOIN_WIDTH, middle + HEIGHT / 2, 'concatenate\nand transform', EMERALD_SOFT, EMERALD, EMERALD, size=12, rounding=0.012)
    harrow(ax, JOIN_X + JOIN_WIDTH + 0.008, OUTPUT_X - 0.008, middle, GOLD, scale=12, linewidth=1.1)
    box(ax, OUTPUT_X, middle - HEIGHT / 2, OUTPUT_X + OUTPUT_WIDTH, middle + HEIGHT / 2, 'output\nsequence', GOLD_SOFT, GOLD, GOLD, size=12, rounding=0.012)

    ax.set_xlim(0.0, 1.03)
    ax.set_ylim(0.20, 1.0)
    save(fig, target('multi-head'))


if __name__ == '__main__':
    use_style()
    multi_head()
