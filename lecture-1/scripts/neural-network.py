'''A network is a chain of blocks; each block is the same simple unit repeated.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, INK_SOFT, INK_SUBTLE, SURFACE, WHITE, blank, figsize, save, use_style

BLOCKS = [(0.21, 'block 1'), (0.42, 'block 2'), (0.63, 'block 3')]
WIDTH, TOP, HEIGHT = 0.16, 0.74, 0.18


def chain_box(ax: Axes, x: float, width: float, label: str, facecolor: str, edgecolor: str, textcolor: str, weight: int = 400) -> None:
    box(ax, x, TOP, x + width, TOP + HEIGHT, label, facecolor, edgecolor, textcolor, size=12.5, weight=weight)


def neural_network() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.94, 0.44))
    blank(ax)
    middle = TOP + HEIGHT / 2

    chain_box(ax, 0.02, 0.13, 'input', SURFACE, BORDER, INK_SOFT)
    harrow(ax, 0.155, 0.203, middle, INK_SUBTLE, scale=13, linewidth=1.2)
    for x, name in BLOCKS:
        chain_box(ax, x, WIDTH, name, ACCENT_SOFT, ACCENT, ACCENT, weight=600)
        if x != BLOCKS[0][0]:
            harrow(ax, x - 0.048, x - 0.007, middle, INK_SUBTLE, scale=13, linewidth=1.2)
    harrow(ax, 0.795, 0.843, middle, INK_SUBTLE, scale=13, linewidth=1.2)
    chain_box(ax, 0.85, 0.13, 'output', EMERALD_SOFT, EMERALD, EMERALD)

    lens_left, lens_right = 0.31, 0.71
    box(ax, lens_left, 0.05, lens_right, 0.47, None, SURFACE, BORDER, None, rounding=0.016)
    for block_x, panel_x in ((0.42, lens_left), (0.58, lens_right)):
        ax.plot([block_x, panel_x], [TOP - 0.005, 0.47], color=BORDER, linewidth=1.0, linestyle=(0, (4, 3)), zorder=1)
    ax.text(0.51, 0.415, 'inside one block', ha='center', fontsize=11.5, color=INK_SUBTLE)

    left = [(0.40, 0.135 + index * 0.085) for index in range(3)]
    right = [(0.62, 0.115 + index * 0.058) for index in range(5)]
    for x0, y0 in left:
        for x1, y1 in right:
            ax.plot([x0, x1], [y0, y1], color=INK_SUBTLE, linewidth=0.6, alpha=0.55, zorder=2)
    for points, color in ((left, INK_SOFT), (right, ACCENT)):
        xs, ys = zip(*points)
        ax.scatter(xs, ys, s=120, color=color, zorder=3, linewidths=1.2, edgecolors=WHITE)

    ax.text(0.51, 0.98, 'Modern neural networks are made up of hundreds of simpler building blocks', ha='center', fontsize=12.5, color=ACCENT, fontweight=600)
    ax.text(0.51, -0.075, 'Each block contains a set of parameters that are adjusted during training', ha='center', fontsize=11, color=INK_SUBTLE, va='bottom')

    ax.set_ylim(-0.09, 1.03)
    save(fig, target('neural-network'))


if __name__ == '__main__':
    use_style()
    neural_network()
