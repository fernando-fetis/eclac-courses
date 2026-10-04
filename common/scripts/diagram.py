'''Shared drawing helpers for box-and-arrow figures.

Arrows are horizontal or vertical only; a connection that changes direction is an elbow of axis-aligned segments with the arrowhead on the last one.
'''

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def box(ax: Axes, x0: float, y0: float, x1: float, y1: float, label: str | None, facecolor: str, edgecolor: str, textcolor: str | None, size: float = 12, weight: int = 400, family: str | None = None, linespacing: float = 1.15, rounding: float = 0.014) -> None:
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle=f'round,pad=0,rounding_size={rounding}', facecolor=facecolor, edgecolor=edgecolor, linewidth=1.2))
    if label:
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, label, ha='center', va='center', fontsize=size, color=textcolor, fontweight=weight, family=family, linespacing=linespacing)


def harrow(ax: Axes, x0: float, x1: float, y: float, color: str, linewidth: float = 1.3, scale: float = 14) -> None:
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle='-|>', mutation_scale=scale, color=color, linewidth=linewidth))


def varrow(ax: Axes, y0: float, y1: float, x: float, color: str, linewidth: float = 1.3, scale: float = 14) -> None:
    ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle='-|>', mutation_scale=scale, color=color, linewidth=linewidth))


def photo(ax: Axes, path: Path, xy: tuple[float, float], zoom: float, edgecolor: str = 'white', linewidth: float = 2.0, sample: int = 1, **image_args: object) -> None:
    image = plt.imread(path)[::sample, ::sample]
    ax.add_artist(AnnotationBbox(OffsetImage(image, zoom=zoom, **image_args), xy, frameon=True, pad=0.14, bboxprops={'edgecolor': edgecolor, 'linewidth': linewidth}))
