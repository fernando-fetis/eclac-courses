'''Two ways to build a system: write the rules, or learn them from examples.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from _common import target
from diagram import box, varrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, INK, INK_SOFT, INK_SUBTLE, SURFACE, WHITE, blank, figsize, save, use_style

WIDTH = 0.40


def step(ax: Axes, center_x: float, y0: float, y1: float, label: str, facecolor: str, edgecolor: str, textcolor: str, size: float = 11.5, **options: str | int) -> None:
    box(ax, center_x - WIDTH / 2, y0, center_x + WIDTH / 2, y1, label, facecolor, edgecolor, textcolor, size=size, linespacing=1.5, rounding=0.015, **options)


def shift() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.94, 0.42))
    blank(ax)

    left, right = 0.26, 0.76

    ax.text(left, 0.95, 'Write the rules', ha='center', fontsize=15, fontweight=600, color=INK_SOFT)
    ax.text(right, 0.95, 'Learn the rules', ha='center', fontsize=15, fontweight=600, color=ACCENT)

    step(ax, left, 0.64, 0.82, 'an expert states\nwhat they know', SURFACE, BORDER, INK)
    varrow(ax, 0.62, 0.54, left, INK_SUBTLE, scale=13, linewidth=1.2)
    step(ax, left, 0.32, 0.52, 'IF fever AND cough\n THEN suspect flu', WHITE, BORDER, INK_SOFT, size=10.5, family='monospace')
    varrow(ax, 0.30, 0.22, left, INK_SUBTLE, scale=13, linewidth=1.2)
    step(ax, left, 0.02, 0.20, 'a program applies\nthe defined rules', SURFACE, BORDER, INK)

    step(ax, right, 0.64, 0.82, 'millions of examples\nshow the right answer', SURFACE, BORDER, INK)
    varrow(ax, 0.62, 0.54, right, ACCENT, scale=13, linewidth=1.2)
    step(ax, right, 0.32, 0.52, 'a neural network adjusts\nits own rules', ACCENT, 'none', WHITE, weight=600)
    varrow(ax, 0.30, 0.22, right, ACCENT, scale=13, linewidth=1.2)
    step(ax, right, 0.02, 0.20, 'the rules exist, but\nnobody wrote them down', ACCENT_SOFT, ACCENT, ACCENT)

    ax.plot([0.51, 0.51], [0.02, 0.86], color=BORDER, linewidth=1.0, linestyle=(0, (4, 4)))

    ax.set_ylim(-0.02, 1.06)
    save(fig, target('shift'))


if __name__ == '__main__':
    use_style()
    shift()
