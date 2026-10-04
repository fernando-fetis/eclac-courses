'''The same sentence costs more tokens in Spanish than in English.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import FancyBboxPatch

from _common import target
from plotstyle import CRIMSON, INK_SOFT, SERIES, blank, figsize, save, use_style

ENGLISH = ['The', ' Comm', 'ission', ' published', ' its', ' annual', ' report']
SPANISH = ['La', ' Com', 'isión', ' public', 'ó', ' su', ' informe', ' anual']


def draw_row(ax: Axes, y: float, language: str, pieces: list[str], color: str) -> None:
    ax.text(-0.012, y + 0.035, language, ha='right', va='center', fontsize=12.5, fontweight=600, color=color)
    x = 0.0
    for index, piece in enumerate(pieces):
        width = 0.0132 * len(piece) + 0.021
        tone = SERIES[index % len(SERIES)]
        ax.add_patch(FancyBboxPatch((x, y), width, 0.07, boxstyle='round,pad=0,rounding_size=0.006', facecolor=tone, alpha=0.13, edgecolor=tone, linewidth=0.9))
        ax.text(x + width / 2, y + 0.035, piece.strip(), ha='center', va='center', fontsize=11, color=tone, family='monospace')
        x += width + 0.006
    ax.text(x + 0.016, y + 0.035, f'{len(pieces)} tokens', ha='left', va='center', fontsize=12, fontweight=600, color=color)


def tokenization() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.94, 0.26))
    blank(ax)
    ax.set_xlim(-0.10, 1.02)
    ax.set_ylim(0.0, 0.34)
    draw_row(ax, 0.20, 'English', ENGLISH, INK_SOFT)
    draw_row(ax, 0.06, 'Spanish', SPANISH, CRIMSON)
    save(fig, target('tokenization'))


if __name__ == '__main__':
    use_style()
    tokenization()
