'''A token is looked up by its id, and a learned row comes back.'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.patches import Rectangle

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, BORDER, EMERALD, INK, INK_SOFT, INK_SUBTLE, SURFACE, WHITE, blank, cmap, figsize, save, use_style

WORD, TOKEN_ID = 'region', 842
ROW_LABELS = ['0', '1', '2', '…', str(TOKEN_ID), '…', '1022', '1023']
PICKED = 4
COLUMNS = 14

TOKEN_X, TOKEN_WIDTH = 0.02, 0.17
ID_X, ID_WIDTH = 0.25, 0.08
TABLE_X, TABLE_WIDTH = 0.42, 0.34

TABLE_TOP, ROW_HEIGHT = 0.86, 0.088
MIDDLE = TABLE_TOP - (PICKED + 0.5) * ROW_HEIGHT


def lookup(ax: Axes) -> None:
    box(ax, TOKEN_X, MIDDLE - 0.055, TOKEN_X + TOKEN_WIDTH, MIDDLE + 0.055, WORD, SURFACE, BORDER, INK, size=12, family='monospace', rounding=0.010)
    harrow(ax, TOKEN_X + TOKEN_WIDTH + 0.010, ID_X - 0.010, MIDDLE, INK_SUBTLE, scale=13, linewidth=1.2)
    ax.text(ID_X + ID_WIDTH / 2, MIDDLE, str(TOKEN_ID), ha='center', va='center', fontsize=13, family='monospace', color=ACCENT)
    harrow(ax, ID_X + ID_WIDTH + 0.010, TABLE_X - 0.060, MIDDLE, ACCENT, scale=13, linewidth=1.2)

    ax.text(TOKEN_X + TOKEN_WIDTH / 2, MIDDLE - 0.105, 'a token', ha='center', fontsize=11, color=INK_SUBTLE)
    ax.text(ID_X + ID_WIDTH / 2, MIDDLE - 0.105, 'its id', ha='center', fontsize=11, color=INK_SUBTLE)


def table(ax: Axes, values: np.ndarray) -> None:
    cell = TABLE_WIDTH / COLUMNS
    rows = len(ROW_LABELS)
    bottom = TABLE_TOP - rows * ROW_HEIGHT

    ax.imshow(values, cmap=cmap(), aspect='auto', vmin=-1, vmax=1, extent=(TABLE_X, TABLE_X + TABLE_WIDTH, bottom, TABLE_TOP))

    for index in range(rows + 1):
        y = TABLE_TOP - index * ROW_HEIGHT
        ax.plot([TABLE_X, TABLE_X + TABLE_WIDTH], [y, y], color=WHITE, linewidth=1.0)
    for index in range(COLUMNS + 1):
        x = TABLE_X + index * cell
        ax.plot([x, x], [bottom, TABLE_TOP], color=WHITE, linewidth=1.0)

    for index, name in enumerate(ROW_LABELS):
        y = TABLE_TOP - (index + 0.5) * ROW_HEIGHT
        chosen = index == PICKED
        ax.text(TABLE_X - 0.014, y, name, ha='right', va='center', fontsize=10.5, family='monospace', color=ACCENT if chosen else INK_SUBTLE)

    ax.add_patch(Rectangle((TABLE_X, TABLE_TOP - (PICKED + 1) * ROW_HEIGHT), TABLE_WIDTH, ROW_HEIGHT, facecolor='none', edgecolor=EMERALD, linewidth=2.2))
    harrow(ax, TABLE_X + TABLE_WIDTH + 0.010, TABLE_X + TABLE_WIDTH + 0.055, MIDDLE, EMERALD, scale=13, linewidth=1.2)
    ax.text(TABLE_X + TABLE_WIDTH + 0.070, MIDDLE, 'one learned vector,\nthe row of that id', ha='left', va='center', fontsize=11, color=EMERALD, linespacing=1.5)

    ax.text(TABLE_X, TABLE_TOP + 0.045, 'the embedding table: one row per token in the vocabulary', fontsize=11.5, color=INK_SOFT)
    ax.text(TABLE_X, bottom - 0.075, '1 024 rows, and every one of them is fitted during training', fontsize=11, color=INK_SUBTLE)


def embeddings() -> None:
    generator = np.random.default_rng(7)
    values = generator.normal(0, 0.5, (len(ROW_LABELS), COLUMNS)).clip(-1, 1)

    fig, ax = plt.subplots(figsize=figsize(1.0, 0.34))
    blank(ax)
    lookup(ax)
    table(ax, values)

    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(0.0, 0.96)
    save(fig, target('embeddings'))


if __name__ == '__main__':
    use_style()
    embeddings()
