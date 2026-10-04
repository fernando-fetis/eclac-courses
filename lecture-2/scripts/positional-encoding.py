'''Positions are looked up the same way, and the two vectors are added.'''

from collections.abc import Callable

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.colors import to_rgb
from matplotlib.patches import Rectangle

from _common import target
from diagram import box, harrow, varrow
from plotstyle import ACCENT, BORDER, EMERALD, GOLD, INK, INK_SOFT, INK_SUBTLE, SURFACE, WHITE, blank, figsize, save, use_style

WORD = 'region'
CELLS = 12
CELL_WIDTH, CELL_HEIGHT = 0.030, 0.085

ROW_X = 0.30
TOKEN_Y, POSITION_Y, SUM_Y = 0.76, 0.52, 0.17

Shade = Callable[[float], tuple[float, ...]]


def strip(ax: Axes, y: float, values: np.ndarray, color: Shade, edgecolor: str) -> None:
    for index, value in enumerate(values):
        ax.add_patch(Rectangle((ROW_X + index * CELL_WIDTH, y), CELL_WIDTH, CELL_HEIGHT, facecolor=color(value), edgecolor=WHITE, linewidth=1.0))
    ax.add_patch(Rectangle((ROW_X, y), CELLS * CELL_WIDTH, CELL_HEIGHT, facecolor='none', edgecolor=edgecolor, linewidth=1.2))


def shade(base: str) -> Shade:
    def color(value: float) -> tuple[float, ...]:
        return (*[channel + (1 - channel) * (1 - abs(value)) for channel in to_rgb(base)], 1.0)
    return color


def source(ax: Axes, y: float, badge: str, caption: str, color: str) -> None:
    box(ax, 0.02, y - 0.012, 0.22, y + CELL_HEIGHT + 0.012, badge, SURFACE, BORDER, INK, size=11.5, family='monospace', rounding=0.010)
    harrow(ax, 0.23, ROW_X - 0.012, y + CELL_HEIGHT / 2, color, scale=12, linewidth=1.2)
    ax.text(ROW_X + CELLS * CELL_WIDTH + 0.020, y + CELL_HEIGHT / 2, caption, ha='left', va='center', fontsize=10.5, color=color, linespacing=1.5)


def positional_encoding() -> None:
    generator = np.random.default_rng(11)
    token = generator.normal(0, 0.6, CELLS).clip(-1, 1)
    position = generator.normal(0, 0.6, CELLS).clip(-1, 1)
    total = ((token + position) / 2).clip(-1, 1)

    fig, ax = plt.subplots(figsize=figsize(1.0, 0.30))
    blank(ax)

    strip(ax, TOKEN_Y, token, shade(ACCENT), ACCENT)
    strip(ax, POSITION_Y, position, shade(GOLD), GOLD)
    strip(ax, SUM_Y, total, shade(EMERALD), EMERALD)

    source(ax, TOKEN_Y, WORD, 'which token it is', ACCENT)
    source(ax, POSITION_Y, 'position 9', 'where it sits', GOLD)

    middle = ROW_X + CELLS * CELL_WIDTH / 2
    ax.text(ROW_X - 0.035, (TOKEN_Y + POSITION_Y) / 2 + CELL_HEIGHT / 2, '+', ha='center', va='center', fontsize=17, color=INK_SUBTLE)
    ax.plot([ROW_X, ROW_X + CELLS * CELL_WIDTH], [POSITION_Y - 0.055, POSITION_Y - 0.055], color=INK_SUBTLE, linewidth=1.0)
    varrow(ax, POSITION_Y - 0.060, SUM_Y + CELL_HEIGHT + 0.012, middle, EMERALD, scale=12, linewidth=1.2)
    ax.text(ROW_X + CELLS * CELL_WIDTH + 0.020, SUM_Y + CELL_HEIGHT / 2, 'what the first block reads', ha='left', va='center', fontsize=10.5, color=EMERALD)

    ax.text(0.02, 0.955, 'a position is a row of a second learned table, exactly like a token', fontsize=11.5, color=INK_SOFT)
    ax.text(0.02, 0.045, 'every block then rewrites this sequence of vectors into a better one', fontsize=11.5, color=INK_SUBTLE)

    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(0.0, 1.0)
    save(fig, target('positional-encoding'))


if __name__ == '__main__':
    use_style()
    positional_encoding()
