'''The whole model: embeddings, then the same block stacked L times.'''

import matplotlib.pyplot as plt

from _common import target
from diagram import box, varrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, GOLD, GOLD_SOFT, INK, INK_SUBTLE, SURFACE, blank, figsize, save, use_style

LEFT, RIGHT, HEIGHT = 0.20, 0.72, 0.090
CENTER = (LEFT + RIGHT) / 2

STAGES = [
    (0.06, 'token ids', SURFACE, BORDER, INK),
    (0.22, 'token and position embeddings', GOLD_SOFT, GOLD, GOLD),
    (0.40, 'Transformer block 1', ACCENT_SOFT, ACCENT, ACCENT),
    (0.55, 'Transformer block 2', ACCENT_SOFT, ACCENT, ACCENT),
    (0.85, 'Transformer block L', ACCENT_SOFT, ACCENT, ACCENT),
]

ELLIPSIS_Y = 0.70


def gpt_architecture() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.44, 1.24))
    blank(ax)

    for y, label, facecolor, edgecolor, textcolor in STAGES:
        box(ax, LEFT, y - HEIGHT / 2, RIGHT, y + HEIGHT / 2, label, facecolor, edgecolor, textcolor, size=13, rounding=0.012)

    for lower, upper in zip(STAGES, STAGES[1:]):
        if lower[0] < ELLIPSIS_Y < upper[0]:
            continue
        varrow(ax, lower[0] + HEIGHT / 2 + 0.006, upper[0] - HEIGHT / 2 - 0.006, CENTER, INK_SUBTLE, scale=11, linewidth=1.1)

    ax.text(CENTER, ELLIPSIS_Y, '$\\vdots$', ha='center', va='center', fontsize=26, color=INK_SUBTLE)

    ax.set_xlim(0.14, 0.78)
    ax.set_ylim(0.0, 0.94)
    save(fig, target('gpt-architecture'))


if __name__ == '__main__':
    use_style()
    gpt_architecture()
