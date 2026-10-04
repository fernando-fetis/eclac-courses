'''The same scores under four temperatures, with everything the shortlist drops.'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

from _common import target
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, CRIMSON, EMERALD, EMERALD_SOFT, INK_SOFT, SURFACE, figsize, save, use_style

WORDS = ['economy', 'region', 'central', 'country']
# The four kept tokens, then the tail the shortlist throws away.
SCORES = np.array([3.1, 2.5, 2.1, 1.8, 1.4, 1.2, 1.0, 0.8, 0.6, 0.4, 0.2, 0.0])

TOP_K = 4
TEMPERATURES = [0.2, 0.6, 1.0, 1.8]


def probabilities(temperature: float) -> np.ndarray:
    weights = np.exp((SCORES - SCORES.max()) / temperature)
    return weights / weights.sum()


def panel(ax: Axes, temperature: float, first: bool) -> None:
    spread = probabilities(temperature)
    heights = list(spread[:TOP_K]) + [spread[TOP_K:].sum()]
    labels = WORDS + ['the rest']
    colors = [EMERALD_SOFT] + [ACCENT_SOFT] * (TOP_K - 1) + [SURFACE]
    edges = [EMERALD] + [ACCENT] * (TOP_K - 1) + [BORDER]

    ax.bar(labels, heights, color=colors, edgecolor=edges, width=0.62)
    for label, height in zip(labels, heights):
        ax.text(label, height + 0.03, f'{height:.2f}', ha='center', fontsize=9.5, color=INK_SOFT)

    ax.set_title(f'temperature {temperature}', fontsize=12.5, color=INK_SOFT, pad=10)
    ax.set_ylim(0, 1.16)
    ax.set_yticks([0, 0.5, 1.0])
    ax.tick_params(axis='x', labelrotation=90)
    ax.grid(axis='x', visible=False)
    if first:
        ax.set_ylabel('probability')


def decoding() -> None:
    fig, axes = plt.subplots(1, len(TEMPERATURES), figsize=figsize(1.0, 0.36), sharey=True)
    for index, (ax, temperature) in enumerate(zip(axes, TEMPERATURES)):
        panel(ax, temperature, index == 0)

    axes[0].text(0.8, 1.10, 'almost always the\nsame token', ha='left', fontsize=10.5, color=EMERALD, linespacing=1.5, va='top')
    axes[-1].text(TOP_K, 1.10, 'and most of the\nmass is thrown away', ha='right', fontsize=10.5, color=CRIMSON, linespacing=1.5, va='top')

    save(fig, target('decoding'))


if __name__ == '__main__':
    use_style()
    decoding()
