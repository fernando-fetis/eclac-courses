'''One block, with its two parts, and the note that it is stacked.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import FancyBboxPatch

from _common import target
from diagram import box, varrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, GOLD, GOLD_SOFT, INK, INK_SUBTLE, SURFACE, blank, figsize, save, use_style

LEFT, RIGHT = 0.08, 0.74
CENTER = (LEFT + RIGHT) / 2
INNER_LEFT, INNER_RIGHT = LEFT + 0.07, RIGHT - 0.07

PART_HEIGHT, PART_GAP, BLOCK_PAD = 0.105, 0.055, 0.055
BLOCK_Y = 0.315
BLOCK_HEIGHT = 2 * PART_HEIGHT + PART_GAP + 2 * BLOCK_PAD
ENDS_HEIGHT = 0.105


def block(ax: Axes) -> None:
    ax.add_patch(FancyBboxPatch((LEFT, BLOCK_Y), RIGHT - LEFT, BLOCK_HEIGHT, boxstyle='round,pad=0,rounding_size=0.016', facecolor='none', edgecolor=INK_SUBTLE, linewidth=1.3))

    lower = BLOCK_Y + BLOCK_PAD
    upper = lower + PART_HEIGHT + PART_GAP
    box(ax, INNER_LEFT, lower, INNER_RIGHT, lower + PART_HEIGHT, 'self-attention', ACCENT_SOFT, ACCENT, ACCENT, size=12.5, rounding=0.012)
    box(ax, INNER_LEFT, upper, INNER_RIGHT, upper + PART_HEIGHT, 'feedforward network', GOLD_SOFT, GOLD, GOLD, size=12.5, rounding=0.012)
    varrow(ax, lower + PART_HEIGHT + 0.006, upper - 0.006, CENTER, INK_SUBTLE, scale=11, linewidth=1.1)

    ax.text(LEFT + 0.018, BLOCK_Y + BLOCK_HEIGHT - 0.030, 'Transformer block', fontsize=11, color=INK_SUBTLE)


def transformer_overview() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.44, 1.45))
    blank(ax)

    box(ax, LEFT, 0.06, RIGHT, 0.06 + ENDS_HEIGHT, 'sequence of tokens', SURFACE, BORDER, INK, size=12, rounding=0.014)
    box(ax, LEFT, 0.855, RIGHT, 0.855 + ENDS_HEIGHT, 'distribution of the next token', EMERALD_SOFT, EMERALD, EMERALD, size=12, rounding=0.014)

    block(ax)
    varrow(ax, 0.06 + ENDS_HEIGHT + 0.006, BLOCK_Y - 0.006, CENTER, INK_SUBTLE, scale=12, linewidth=1.2)
    varrow(ax, BLOCK_Y + BLOCK_HEIGHT + 0.006, 0.855 - 0.006, CENTER, INK_SUBTLE, scale=12, linewidth=1.2)

    brace = RIGHT + 0.055
    ax.plot([brace, brace], [BLOCK_Y, BLOCK_Y + BLOCK_HEIGHT], color=ACCENT, linewidth=1.3)
    for y in (BLOCK_Y, BLOCK_Y + BLOCK_HEIGHT):
        ax.plot([brace - 0.024, brace], [y, y], color=ACCENT, linewidth=1.3)
    ax.text(brace + 0.030, BLOCK_Y + BLOCK_HEIGHT / 2, 'repeated\n$L$ times', ha='left', va='center', fontsize=12.5, color=ACCENT, linespacing=1.6)

    ax.set_xlim(0.04, 1.04)
    ax.set_ylim(0.02, 1.0)
    save(fig, target('transformer-overview'))


if __name__ == '__main__':
    use_style()
    transformer_overview()
