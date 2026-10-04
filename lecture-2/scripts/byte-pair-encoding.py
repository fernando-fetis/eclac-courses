'''One word, at four stages of the merging that builds the vocabulary.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from _common import target
from diagram import box, varrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, INK, INK_SOFT, INK_SUBTLE, SURFACE, blank, figsize, save, use_style

# Illustrative: the stages a word passes through, not the merge log itself.
STAGES = [(['r', 'e', 'g', 'i', 'o', 'n'], 'every character is a token'), (['re', 'g', 'io', 'n'], 'after a few merges'), (['reg', 'ion'], 'after a few hundred'), (['region'], 'one token, in the end')]

ROW_TOP, ROW_STEP, HEIGHT = 0.84, 0.235, 0.15
UNIT, GAP = 0.050, 0.012
LEFT = 0.04


def stage(ax: Axes, y: float, pieces: list[str], caption: str, last: bool) -> None:
    facecolor, edgecolor, textcolor = (EMERALD_SOFT, EMERALD, EMERALD) if last else (SURFACE, BORDER, INK) if len(pieces) == 7 else (ACCENT_SOFT, ACCENT, ACCENT)

    x = LEFT
    for piece in pieces:
        width = UNIT * len(piece) + 0.026
        box(ax, x, y, x + width, y + HEIGHT, piece, facecolor, edgecolor, textcolor, size=13, family='monospace', rounding=0.010)
        x += width + GAP

    ax.text(0.70, y + HEIGHT / 2, caption, ha='left', va='center', fontsize=11.5, color=EMERALD if last else INK_SOFT)


def byte_pair_encoding() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.90, 0.44))
    blank(ax)

    for index, (pieces, caption) in enumerate(STAGES):
        y = ROW_TOP - index * ROW_STEP
        stage(ax, y, pieces, caption, index == len(STAGES) - 1)
        if index:
            varrow(ax, y + ROW_STEP - 0.010, y + HEIGHT + 0.010, LEFT + 0.05, INK_SUBTLE, scale=11, linewidth=1.1)

    ax.text(LEFT, 0.04, 'the pair that gets merged is always the most frequent one, never the most meaningful', fontsize=11.5, color=INK_SOFT)

    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(0.0, 1.0)
    save(fig, target('byte-pair-encoding'))


if __name__ == '__main__':
    use_style()
    byte_pair_encoding()
