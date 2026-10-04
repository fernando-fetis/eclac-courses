'''Gradient descent on an everyday cost: when to leave home to avoid traffic.

The commute curve and the step positions are illustrative.
'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

from _common import target
from plotstyle import ACCENT, INK, INK_SUBTLE, figsize, save, use_style

STEPS = [8.52, 8.72, 8.90, 9.04, 9.14]


def commute(departure: np.ndarray | float) -> np.ndarray | float:
    return 45.0 + 18.0 * np.exp(-(((departure - 8.0) / 0.50) ** 2)) - 14.0 * np.exp(-(((departure - 6.75) / 0.38) ** 2)) - 8.0 * np.exp(-(((departure - 9.18) / 0.30) ** 2)) + 2.2 * (departure - 8.0) ** 2 / 4.0


def optimization() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.78, 0.46))

    grid = np.linspace(6.35, 9.75, 500)
    ax.plot(grid, commute(grid), color=INK_SUBTLE, linewidth=2.2, zorder=1)

    points = np.array(STEPS)
    ax.plot(points, commute(points), 'o', markersize=7, color=ACCENT, zorder=4)
    for start, end in zip(points[:-1], points[1:]):
        ax.add_patch(FancyArrowPatch((start, commute(start)), (end, commute(end)), arrowstyle='-|>', mutation_scale=14, color=ACCENT, linewidth=1.5, connectionstyle='arc3,rad=-0.35', shrinkA=6, shrinkB=6, zorder=3))

    ax.annotate('start', xy=(points[0], commute(points[0])), xytext=(4, 12), textcoords='offset points', ha='left', fontsize=12.5, color=ACCENT, fontweight=600)
    local = 9.16
    ax.annotate('a local minimum', xy=(local, commute(local)), xytext=(0, -26), textcoords='offset points', ha='center', fontsize=11, color=INK)
    best = 6.77
    ax.plot(best, commute(best), marker='*', markersize=15, color=INK_SUBTLE, zorder=4)
    ax.annotate('a better one,\nnever tried', xy=(best, commute(best)), xytext=(0, -34), textcoords='offset points', ha='center', fontsize=10.5, color=INK_SUBTLE, linespacing=1.3)

    ax.set_xlabel('departure time')
    ax.set_ylabel('minutes in traffic')
    ax.set_xticks([7.0, 8.0, 9.0])
    ax.set_xticklabels(['7:00', '8:00', '9:00'])
    ax.set_yticks([30, 45, 60])
    ax.grid(False)
    ax.set_xlim(6.25, 9.9)
    ax.set_ylim(22, 72)
    save(fig, target('optimization'))


if __name__ == '__main__':
    use_style()
    optimization()
