'''Training climbs: each step raises the probability the model gives the data.'''

import matplotlib.pyplot as plt
import numpy as np

from _common import target
from plotstyle import ACCENT, CRIMSON, EMERALD, INK_SOFT, INK_SUBTLE, figsize, save, use_style

LEARNING_RATE = 0.26
START = -0.30
STEPS = 7


def value(weight: float | np.ndarray) -> float | np.ndarray:
    return -0.34 * weight ** 4 - 0.2 * weight ** 3 + 1.6 * weight ** 2


def slope(weight: float) -> float:
    return -1.36 * weight ** 3 - 0.6 * weight ** 2 + 3.2 * weight


def ascent() -> np.ndarray:
    weight = START
    path = [weight]
    for _ in range(STEPS):
        weight += LEARNING_RATE * slope(weight)
        path.append(weight)
    return np.array(path)


def gradient_descent() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.80, 0.46))

    grid = np.linspace(-2.5, 2.1, 400)
    ax.plot(grid, value(grid), color=INK_SOFT, linewidth=1.6)

    path = ascent()
    ax.plot(path, value(path), color=ACCENT, marker='o', markersize=6, linewidth=1.2, linestyle=(0, (3, 3)))
    ax.scatter([path[0]], [value(path[0])], s=90, color=CRIMSON, zorder=4)
    ax.scatter([path[-1]], [value(path[-1])], s=90, color=EMERALD, zorder=4)

    ax.text(path[0] + 0.14, value(path[0]) - 0.30, 'random start', ha='left', fontsize=11.5, color=CRIMSON)
    ax.text(path[-1], value(path[-1]) + 0.26, 'after seven steps', ha='center', fontsize=11.5, color=EMERALD)
    ax.text(0.35, 2.55, 'small steps where the curve is flat,\nlong ones where it is steep', ha='left', fontsize=10.5, color=INK_SUBTLE, linespacing=1.5)

    ax.set_xlabel('value of one parameter')
    ax.set_ylabel('probability of the data')
    ax.set_xlim(-2.65, 2.25)
    ax.set_ylim(-1.2, 3.5)
    ax.set_yticks([])

    save(fig, target('gradient-descent'))


if __name__ == '__main__':
    use_style()
    gradient_descent()
