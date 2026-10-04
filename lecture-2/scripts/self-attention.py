'''The output at one position is a weighted sum of the whole sequence.'''

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, INK, INK_SOFT, INK_SUBTLE, SURFACE, blank, figsize, save, use_style

WORDS = ['in', 'the', 'first', 'half']
WEIGHTS = [0.12, 0.46, 0.34, 0.08]
TARGET = 3

INPUT_X, INPUT_WIDTH = 0.02, 0.19
BAR_X, BAR_UNIT = 0.30, 0.43
MERGE_X = 0.68
OUTPUT_X, OUTPUT_WIDTH = 0.76, 0.19

ROW_TOP, ROW_STEP, ROW_HEIGHT = 0.74, 0.175, 0.115
BAR_HEIGHT = 0.056


def self_attention() -> None:
    fig, ax = plt.subplots(figsize=figsize(1.0, 0.36))
    blank(ax)

    rows = [ROW_TOP - index * ROW_STEP + ROW_HEIGHT / 2 for index in range(len(WORDS))]
    middle = (rows[0] + rows[-1]) / 2

    for index, (word, weight, center) in enumerate(zip(WORDS, WEIGHTS, rows)):
        chosen = index == TARGET
        box(ax, INPUT_X, center - ROW_HEIGHT / 2, INPUT_X + INPUT_WIDTH, center + ROW_HEIGHT / 2, word, SURFACE, ACCENT if chosen else BORDER, INK, size=11, family='monospace', rounding=0.010)

        harrow(ax, INPUT_X + INPUT_WIDTH + 0.008, BAR_X - 0.008, center, INK_SUBTLE, scale=11, linewidth=1.0)
        ax.add_patch(Rectangle((BAR_X, center - BAR_HEIGHT / 2), weight * BAR_UNIT, BAR_HEIGHT, facecolor=ACCENT_SOFT, edgecolor=ACCENT, linewidth=1.0))
        ax.text(BAR_X + weight * BAR_UNIT + 0.012, center, f'{weight:.2f}', ha='left', va='center', fontsize=10.5, color=ACCENT)
        ax.plot([BAR_X + 0.30, MERGE_X], [center, center], color=EMERALD, linewidth=1.0)

        if chosen:
            ax.text(INPUT_X, center - ROW_HEIGHT / 2 - 0.048, 'the position being computed', fontsize=10, color=ACCENT)

    ax.plot([MERGE_X, MERGE_X], [rows[-1], rows[0]], color=EMERALD, linewidth=1.0)
    harrow(ax, MERGE_X, OUTPUT_X - 0.008, middle, EMERALD, scale=11, linewidth=1.0)
    box(ax, OUTPUT_X, middle - ROW_HEIGHT / 2, OUTPUT_X + OUTPUT_WIDTH, middle + ROW_HEIGHT / 2, 'output', EMERALD_SOFT, EMERALD, EMERALD, size=11, family='monospace', rounding=0.010)

    ax.text(INPUT_X, 0.905, 'a sequence of embeddings', fontsize=11.5, color=INK_SOFT)
    ax.text(BAR_X, 0.905, 'how much each one counts', fontsize=11.5, color=ACCENT)
    ax.text(OUTPUT_X, 0.905, 'their weighted sum', fontsize=11.5, color=EMERALD)

    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(0.06, 0.95)
    save(fig, target('self-attention'))


if __name__ == '__main__':
    use_style()
    self_attention()
