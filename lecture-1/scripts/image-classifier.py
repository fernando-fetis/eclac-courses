'''One labeled photo through the network, and the correction loop that trains it.

Photos: Wikimedia Commons (Cat03, Felis catus on snow, yellow Labrador, Labrador portrait).
'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import FancyBboxPatch

from _common import FIGURES, target
from diagram import box, harrow, photo as draw_photo, varrow
from plotstyle import ACCENT, BORDER, EMERALD, GOLD, INK, INK_SOFT, INK_SUBTLE, WHITE, blank, figsize, save, use_style

TRAINING_SET = [
    ('photo-dog-1.jpg', 'dog'),
    ('photo-cat-2.jpg', 'cat'),
    ('photo-dog-2.jpg', 'dog'),
]
GUESSES = [('cat', 0.72, EMERALD), ('dog', 0.28, INK_SUBTLE)]
NETWORK_CENTER = 0.41
GUESS_CENTER = 0.7825


def photo(ax: Axes, name: str, x: float, y: float, zoom: float) -> None:
    draw_photo(ax, FIGURES / name, (x, y), zoom)


def image_classifier() -> None:
    fig, ax = plt.subplots(figsize=figsize(1.0, 0.40))
    blank(ax)

    photo(ax, 'photo-cat-1.jpg', 0.115, 0.565, 0.27)
    ax.text(0.115, 0.215, 'one training photo', ha='center', fontsize=11.5, color=INK_SOFT)
    ax.text(0.115, 0.125, 'true label: cat', ha='center', fontsize=11.5, color=EMERALD, fontweight=600)

    harrow(ax, 0.235, 0.30, 0.565, INK_SUBTLE)
    box(ax, 0.31, 0.405, 0.51, 0.725, None, ACCENT, 'none', None, rounding=0.016)
    ax.text(NETWORK_CENTER, 0.605, 'Neural network', ha='center', fontsize=13.5, color=WHITE, fontweight=600)
    ax.text(NETWORK_CENTER, 0.495, 'billions of\nadjustable parameters', ha='center', fontsize=10.5, color=WHITE, alpha=0.9, linespacing=1.4)

    harrow(ax, 0.52, 0.585, 0.565, INK_SUBTLE)
    box(ax, 0.595, 0.345, 0.97, 0.785, None, WHITE, BORDER, None)
    ax.text(GUESS_CENTER, 0.72, 'its guess: how likely each class is', ha='center', fontsize=11, color=INK_SOFT)
    for index, (label, value, color) in enumerate(GUESSES):
        y = 0.55 - index * 0.145
        ax.text(0.675, y + 0.03, label, ha='right', va='center', fontsize=12, color=INK)
        ax.add_patch(FancyBboxPatch((0.69, y), value * 0.20, 0.065, boxstyle='round,pad=0,rounding_size=0.005', facecolor=color, alpha=0.9 if index == 0 else 0.4, edgecolor='none'))
        ax.text(0.69 + value * 0.20 + 0.014, y + 0.03, f'{value:.0%}', ha='left', va='center', fontsize=11, color=INK_SUBTLE)

    ax.plot([GUESS_CENTER, GUESS_CENTER], [0.34, 0.26], color=GOLD, linewidth=1.4)
    ax.plot([GUESS_CENTER, NETWORK_CENTER], [0.26, 0.26], color=GOLD, linewidth=1.4)
    varrow(ax, 0.26, 0.39, NETWORK_CENTER, GOLD, linewidth=1.4)
    ax.text(0.6, 0.16, 'Still 28% incorrect. This is used to further improve the model.', ha='center', fontsize=11.5, color=GOLD, fontweight=600, linespacing=1.35)

    for index, (name, label) in enumerate(TRAINING_SET):
        photo(ax, name, 0.045 + index * 0.075, 0.935, 0.062)
        ax.text(0.045 + index * 0.075, 0.845, label, ha='center', fontsize=9, color=INK_SUBTLE)
    ax.text(0.27, 0.935, '… repeated millions of times', fontsize=11, color=INK_SUBTLE, va='center')

    ax.set_ylim(0.02, 1.02)
    save(fig, target('image-classifier'))


if __name__ == '__main__':
    use_style()
    image_classifier()
