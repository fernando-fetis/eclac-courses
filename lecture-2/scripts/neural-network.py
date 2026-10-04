'''The feedforward sub-block: two hidden layers applied to one position.'''

import matplotlib.pyplot as plt

from _common import target
from plotstyle import ACCENT, EMERALD, INK, INK_SOFT, INK_SUBTLE, WHITE, blank, figsize, save, use_style

LAYERS = [(0.10, 4, INK_SOFT, '$x^{(t)}$'), (0.34, 6, ACCENT, 'hidden'), (0.58, 6, ACCENT, 'hidden'), (0.82, 4, EMERALD, '$y^{(t)}$')]

STEPS = [(0.22, '$h_1 = \\sigma(A_1 x^{(t)} + b_1)$'), (0.46, '$h_2 = \\sigma(A_2 h_1 + b_2)$'), (0.70, '$y^{(t)} = A_3 h_2 + b_3$')]


def column(size: int) -> list[float]:
    span = 0.075 * (size - 1)
    return [0.60 - span / 2 + 0.075 * index for index in range(size)]


def neural_network() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.92, 0.42))
    blank(ax)

    coordinates = [column(size) for _, size, _, _ in LAYERS]
    for index in range(len(LAYERS) - 1):
        left_x, right_x = LAYERS[index][0], LAYERS[index + 1][0]
        for left_y in coordinates[index]:
            for right_y in coordinates[index + 1]:
                ax.plot([left_x, right_x], [left_y, right_y], color=INK_SUBTLE, linewidth=0.5, alpha=0.45, zorder=1)

    for (x, _, color, name), ys in zip(LAYERS, coordinates):
        ax.scatter([x] * len(ys), ys, s=190, color=color, zorder=3, linewidths=1.4, edgecolors=WHITE)
        ax.text(x, 0.90, name, ha='center', fontsize=11.5, color=color)

    for x, equation in STEPS:
        ax.text(x, 0.20, equation, ha='center', fontsize=13, color=INK)

    ax.set_xlim(0.02, 0.94)
    ax.set_ylim(0.14, 0.97)
    save(fig, target('neural-network'))


if __name__ == '__main__':
    use_style()
    neural_network()
