'''Stochastic gradient descent fitting a cubic: four snapshots of the training.'''

import matplotlib.pyplot as plt
import numpy as np

from _common import target
from plotstyle import ACCENT, INK_SUBTLE, figsize, save, use_style

TRUE = np.array([0.9, -1.8, 0.15, 0.11])
SNAPSHOTS = [0, 200, 1500, 8000]
BATCH = 8


def model(coefficients: np.ndarray, x: np.ndarray) -> np.ndarray:
    powers = np.vstack([x**k for k in range(len(coefficients))])
    return coefficients @ powers


def sgd(x: np.ndarray, y: np.ndarray, initial: np.ndarray, steps: int = 8001, rate: float = 1.25e-4) -> dict[int, np.ndarray]:
    generator = np.random.default_rng(7)
    coefficients = initial.copy()
    powers = np.vstack([x**k for k in range(4)])
    snapshots = {}
    for step in range(steps):
        if step in SNAPSHOTS:
            snapshots[step] = coefficients.copy()
        batch = generator.choice(x.size, BATCH, replace=False)
        residual = coefficients @ powers[:, batch] - y[batch]
        coefficients = coefficients - rate * (powers[:, batch] @ residual)
    return snapshots


def polynomial_fit() -> None:
    generator = np.random.default_rng(11)
    x = np.linspace(-3.4, 3.4, 40)
    y = model(TRUE, x) + generator.normal(0, 0.55, x.size)
    initial = generator.normal(0.0, 1.0, 4) * np.array([2.0, 1.0, 0.35, 0.12])
    snapshots = sgd(x, y, initial)

    fig, axes = plt.subplots(1, 4, figsize=figsize(1.0, 0.26))
    smooth = np.linspace(-3.55, 3.55, 250)

    for ax, step in zip(axes, SNAPSHOTS):
        ax.scatter(x, y, s=11, color=INK_SUBTLE, zorder=2, linewidths=0)
        ax.plot(smooth, model(snapshots[step], smooth), color=ACCENT, linewidth=2.2, zorder=3)
        ax.set_title(f'step {step:,}'.replace(',', ' '), fontsize=12)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(False)
        ax.set_ylim(y.min() - 2.2, y.max() + 2.2)

    save(fig, target('polynomial-fit'))


if __name__ == '__main__':
    use_style()
    polynomial_fit()
