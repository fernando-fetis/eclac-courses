'''A GAN: generator against classifier, with a real photo and an early fake.

Photos: Wikimedia Commons (Cat03, Felis catus on snow).
'''

import matplotlib.pyplot as plt

from _common import FIGURES, target
from diagram import box, harrow, photo, varrow
from plotstyle import ACCENT, BORDER, CRIMSON, EMERALD, GOLD, INK, INK_SUBTLE, SURFACE, WHITE, blank, figsize, save, use_style

FAKE_Y, REAL_Y = 0.64, 0.12
IMAGE_X = 0.36
GENERATOR_CENTER = 0.12


def gan() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.96, 0.42))
    blank(ax)

    box(ax, 0.02, 0.50, 0.22, 0.78, 'generator', ACCENT, 'none', WHITE, size=12.5, weight=600, rounding=0.016)
    harrow(ax, 0.225, 0.27, FAKE_Y, INK_SUBTLE, linewidth=1.4)

    photo(ax, FIGURES / 'photo-cat-2.jpg', (IMAGE_X, FAKE_Y), 1.9, edgecolor=CRIMSON, linewidth=1.6, interpolation='nearest', sample=12)
    ax.text(IMAGE_X, 0.83, 'generated image, early in training', ha='center', fontsize=10, color=CRIMSON, va='center')

    photo(ax, FIGURES / 'photo-cat-1.jpg', (IMAGE_X, REAL_Y), 0.16, edgecolor=EMERALD, linewidth=1.6)
    ax.text(IMAGE_X, 0.36, 'a real photo', ha='center', fontsize=10, color=EMERALD, va='center')

    box(ax, 0.52, -0.02, 0.70, 0.78, 'classifier', GOLD, 'none', WHITE, size=12.5, weight=600, rounding=0.016)
    harrow(ax, 0.445, 0.515, FAKE_Y, INK_SUBTLE, linewidth=1.4)
    harrow(ax, 0.445, 0.515, REAL_Y, INK_SUBTLE, linewidth=1.4)

    box(ax, 0.76, 0.29, 0.92, 0.47, 'real or fake?', SURFACE, BORDER, INK, size=10.5, rounding=0.016)
    harrow(ax, 0.705, 0.755, 0.38, INK_SUBTLE, linewidth=1.4)

    ax.plot([0.61, 0.61], [-0.025, -0.17], color=EMERALD, linewidth=1.3)
    ax.plot([0.61, GENERATOR_CENTER], [-0.17, -0.17], color=EMERALD, linewidth=1.3)
    varrow(ax, -0.17, 0.495, GENERATOR_CENTER, EMERALD, scale=13)
    ax.text(0.365, -0.235, 'every time a fake is caught, the generator improves, until the fakes pass', ha='center', fontsize=12, color=EMERALD, fontweight=600, va='top')

    ax.set_ylim(-0.31, 0.95)
    save(fig, target('gan'))


if __name__ == '__main__':
    use_style()
    gan()
