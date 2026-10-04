'''One block as a stream that runs through it, with two corrections added.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import Circle

from _common import target
from diagram import box, harrow, varrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, GOLD, GOLD_SOFT, INK, INK_SOFT, INK_SUBTLE, SURFACE, WHITE, blank, figsize, save, use_style

STREAM = 0.30
BRANCH = 0.62
PART_LEFT, PART_RIGHT, PART_HEIGHT = 0.44, 0.98, 0.125

PARTS = [
    (0.34, 'self-attention\nmixes the positions', ACCENT_SOFT, ACCENT),
    (0.68, 'feedforward network\ntransforms each one', GOLD_SOFT, GOLD),
]

ENDS_HEIGHT = 0.085


def stream_end(ax: Axes, y: float, label: str, facecolor: str, edgecolor: str, textcolor: str) -> None:
    box(ax, 0.06, y, 0.54, y + ENDS_HEIGHT, label, facecolor, edgecolor, textcolor, size=12.5, rounding=0.014)


def junction(ax: Axes, y: float) -> None:
    ax.add_patch(Circle((STREAM, y), 0.022, facecolor=WHITE, edgecolor=INK_SUBTLE, linewidth=1.2, zorder=3))
    ax.plot([STREAM - 0.011, STREAM + 0.011], [y, y], color=INK_SUBTLE, linewidth=1.1, zorder=4)
    ax.plot([STREAM, STREAM], [y - 0.011, y + 0.011], color=INK_SUBTLE, linewidth=1.1, zorder=4)


def part(ax: Axes, center: float, name: str, facecolor: str, edgecolor: str) -> None:
    leave, enter = center - 0.10, center + 0.10

    ax.plot([STREAM, BRANCH], [leave, leave], color=INK_SUBTLE, linewidth=1.1)
    ax.plot([BRANCH, BRANCH], [leave, center - PART_HEIGHT / 2], color=INK_SUBTLE, linewidth=1.1)
    box(ax, PART_LEFT, center - PART_HEIGHT / 2, PART_RIGHT, center + PART_HEIGHT / 2, name, facecolor, edgecolor, edgecolor, size=12, rounding=0.012)
    ax.plot([BRANCH, BRANCH], [center + PART_HEIGHT / 2, enter], color=INK_SUBTLE, linewidth=1.1)
    harrow(ax, BRANCH, STREAM + 0.024, enter, INK_SUBTLE, scale=12, linewidth=1.1)

    junction(ax, enter)
    ax.text(BRANCH + 0.014, (leave + center - PART_HEIGHT / 2) / 2, 'norm', ha='left', va='center', fontsize=10.5, color=INK_SUBTLE)


def transformer_block() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.58, 1.02))
    blank(ax)

    ax.plot([STREAM, STREAM], [0.145, 0.905], color=ACCENT_SOFT, linewidth=7.0, solid_capstyle='round', zorder=1)
    varrow(ax, 0.145, 0.905, STREAM, ACCENT, scale=13, linewidth=1.4)

    stream_end(ax, 0.055, 'input', SURFACE, BORDER, INK)
    stream_end(ax, 0.910, 'output', EMERALD_SOFT, EMERALD, EMERALD)

    for center, name, facecolor, edgecolor in PARTS:
        part(ax, center, name, facecolor, edgecolor)

    ax.text(STREAM - 0.055, 0.52, 'the residual stream', rotation=90, ha='center', va='center', fontsize=12, color=ACCENT)
    ax.text(0.06, 1.055, 'each part writes a correction onto the stream', fontsize=12, color=INK_SOFT)

    ax.set_xlim(0.0, 1.04)
    ax.set_ylim(0.0, 1.09)
    save(fig, target('transformer-block'))


if __name__ == '__main__':
    use_style()
    transformer_block()
