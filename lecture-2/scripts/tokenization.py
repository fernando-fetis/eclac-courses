'''The vocabulary, and one sentence turned into ids by looking into it.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from _common import target
from diagram import box
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, INK, INK_SOFT, INK_SUBTLE, SURFACE, blank, figsize, save, use_style

# Invented ids, and words rather than the pieces a real tokenizer would produce: the point of the figure is the lookup, not the tokenizer.
VOCABULARY = [(9, '.'), (15, 'The'), (24, 'in'), None, (207, 'al'), (842, 'region'), (963, 'grew'), None, (1190, 'economy'), (3571, '2019')]

SPLIT = 'region', 'al'
SEQUENCE = [(15, 'The'), (842, 'region'), (207, 'al'), (1190, 'economy'), (963, 'grew'), (24, 'in'), (3571, '2019'), (9, '.')]

BOX_Y, BOX_HEIGHT = 0.46, 0.30


def vocabulary(ax: Axes) -> None:
    blank(ax)
    top, step = 0.94, 0.088

    ax.text(0.12, top + 0.07, 'id', ha='right', fontsize=11.5, color=INK_SUBTLE)
    ax.text(0.26, top + 0.07, 'token', ha='left', fontsize=11.5, color=INK_SUBTLE)
    ax.plot([0.0, 0.92], [top + 0.042, top + 0.042], color=BORDER, linewidth=1.0)

    for index, entry in enumerate(VOCABULARY):
        y = top - index * step
        if entry is None:
            ax.text(0.12, y, '…', ha='right', fontsize=12, color=INK_SUBTLE)
            ax.text(0.26, y, '…', ha='left', fontsize=12, color=INK_SUBTLE)
            continue
        token_id, piece = entry
        ax.text(0.12, y, str(token_id), ha='right', va='center', fontsize=12, family='monospace', color=ACCENT)
        ax.text(0.26, y, piece, ha='left', va='center', fontsize=12, family='monospace', color=INK)


def token_width(piece: str) -> float:
    return 0.028 * len(piece) + 0.042


def sequence(ax: Axes) -> None:
    blank(ax)
    span = sum(token_width(piece) + 0.010 for _, piece in SEQUENCE)
    ax.set_xlim(-0.006, span)

    x = 0.0
    for token_id, piece in SEQUENCE:
        width = token_width(piece)
        split = piece in SPLIT
        box(ax, x, BOX_Y, x + width, BOX_Y + BOX_HEIGHT, piece, ACCENT_SOFT if split else SURFACE, ACCENT if split else BORDER, ACCENT if split else INK, size=13, family='monospace', rounding=0.008)
        ax.text(x + width / 2, BOX_Y - 0.10, str(token_id), ha='center', va='center', fontsize=12, family='monospace', color=ACCENT)
        x += width + 0.010

    middle = sum(token_width(piece) + 0.010 for _, piece in SEQUENCE[:1]) + (token_width(SPLIT[0]) + token_width(SPLIT[1])) / 2
    ax.text(middle, BOX_Y + BOX_HEIGHT + 0.09, 'one word, two tokens', ha='center', fontsize=11.5, color=ACCENT)
    ax.text(0.0, 0.14, 'the sentence becomes the ids underneath', fontsize=11.5, color=INK_SOFT)


def tokenization() -> None:
    fig, axes = plt.subplots(1, 2, figsize=figsize(1.0, 0.26), gridspec_kw={'width_ratios': (1, 4.2)})
    vocabulary(axes[0])
    sequence(axes[1])
    save(fig, target('tokenization'), w_pad=1.4)


if __name__ == '__main__':
    use_style()
    tokenization()
