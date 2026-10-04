'''From the last block to one probability for every token in the vocabulary.'''

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, INK_SOFT, INK_SUBTLE, SURFACE, blank, figsize, save, use_style

POSITIONS = ['The', 'region', 'grew', 'in']
CANDIDATES = [('2019', 0.42), ('the', 0.17), ('recent', 0.11), ('2020', 0.08)]

COLUMN_X, COLUMN_WIDTH = 0.02, 0.16
LINEAR_X, LINEAR_WIDTH = 0.32, 0.17
BAR_X, BAR_UNIT = 0.68, 0.62

TOP, STEP, HEIGHT = 0.86, 0.155, 0.105


def language_head() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.72, 0.56))
    blank(ax)

    rows = [TOP - index * STEP for index in range(len(POSITIONS))]
    last = rows[-1]

    for word, y in zip(POSITIONS, rows):
        final = y == last
        box(ax, COLUMN_X, y - HEIGHT / 2, COLUMN_X + COLUMN_WIDTH, y + HEIGHT / 2, word, ACCENT_SOFT if final else SURFACE, ACCENT if final else BORDER, ACCENT if final else INK_SUBTLE, size=11.5, family='monospace', rounding=0.010)

    ax.text(COLUMN_X, TOP + 0.10, 'out of the last block', fontsize=11.5, color=INK_SOFT)
    ax.text(COLUMN_X + COLUMN_WIDTH / 2, last - HEIGHT / 2 - 0.075, 'only the last one', ha='center', fontsize=11, color=ACCENT)

    harrow(ax, COLUMN_X + COLUMN_WIDTH + 0.010, LINEAR_X - 0.010, last, ACCENT, scale=12, linewidth=1.2)
    box(ax, LINEAR_X, last - HEIGHT / 2, LINEAR_X + LINEAR_WIDTH, last + HEIGHT / 2, 'one linear\nlayer', EMERALD_SOFT, EMERALD, EMERALD, size=11.5, rounding=0.012)
    harrow(ax, LINEAR_X + LINEAR_WIDTH + 0.010, BAR_X - 0.10, last, EMERALD, scale=12, linewidth=1.2)

    for index, (word, probability) in enumerate(CANDIDATES):
        y = TOP - index * STEP
        ax.add_patch(Rectangle((BAR_X, y - 0.030), probability * BAR_UNIT, 0.060, facecolor=EMERALD_SOFT if index == 0 else ACCENT_SOFT, edgecolor=EMERALD if index == 0 else ACCENT, linewidth=1.0))
        ax.text(BAR_X - 0.012, y, word, ha='right', va='center', fontsize=11, family='monospace', color=EMERALD if index == 0 else ACCENT)
        ax.text(BAR_X + probability * BAR_UNIT + 0.010, y, f'{probability:.2f}', ha='left', va='center', fontsize=10.5, color=INK_SOFT)

    ax.text(BAR_X - 0.012, TOP - len(CANDIDATES) * STEP + 0.02, '$\\vdots$', ha='right', fontsize=16, color=INK_SUBTLE)
    ax.text(BAR_X - 0.012, TOP + 0.10, 'one probability per token', fontsize=11.5, color=EMERALD)

    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(0.20, 1.02)
    save(fig, target('language-head'))


if __name__ == '__main__':
    use_style()
    language_head()
