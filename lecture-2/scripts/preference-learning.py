'''One question, two answers, a person choosing, and what training does.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import Rectangle

from _common import target
from diagram import box, harrow
from plotstyle import BORDER, CRIMSON, CRIMSON_SOFT, EMERALD, EMERALD_SOFT, INK, INK_SOFT, INK_SUBTLE, SURFACE, blank, figsize, save, use_style

QUESTION = 'How do I read this\npoverty table?'
ANSWERS = [
    ('answer A, the preferred one', 'more likely', EMERALD, EMERALD_SOFT, 0.74),
    ('answer B, the other one', 'less likely', CRIMSON, CRIMSON_SOFT, 0.28),
]
BEFORE = 0.50

QUESTION_X, QUESTION_WIDTH = 0.02, 0.19
SPLIT_X = 0.25
ANSWER_X, ANSWER_WIDTH = 0.31, 0.26
BAR_X, BAR_UNIT, BAR_HEIGHT = 0.68, 0.22, 0.052

UPPER, LOWER, CARD_HEIGHT = 0.72, 0.24, 0.15


def probabilities(ax: Axes, center: float, after: float, color: str) -> None:
    for index, (value, facecolor, name) in enumerate([(BEFORE, SURFACE, 'before'), (after, color, 'after')]):
        y = center + 0.012 - index * (BAR_HEIGHT + 0.012)
        ax.add_patch(Rectangle((BAR_X, y), value * BAR_UNIT, BAR_HEIGHT, facecolor=facecolor, edgecolor=color, linewidth=1.0))
        ax.text(BAR_X - 0.012, y + BAR_HEIGHT / 2, name, ha='right', va='center', fontsize=10, color=INK_SUBTLE)


def preference_learning() -> None:
    fig, ax = plt.subplots(figsize=figsize(1.0, 0.34))
    blank(ax)

    middle = (UPPER + LOWER) / 2 + CARD_HEIGHT / 2
    box(ax, QUESTION_X, middle - CARD_HEIGHT / 2, QUESTION_X + QUESTION_WIDTH, middle + CARD_HEIGHT / 2, QUESTION, SURFACE, BORDER, INK, size=11, rounding=0.012)

    ax.plot([QUESTION_X + QUESTION_WIDTH + 0.008, SPLIT_X], [middle, middle], color=INK_SUBTLE, linewidth=1.1)
    ax.plot([SPLIT_X, SPLIT_X], [LOWER + CARD_HEIGHT / 2, UPPER + CARD_HEIGHT / 2], color=INK_SUBTLE, linewidth=1.1)

    for (name, verdict, color, soft, after), bottom in zip(ANSWERS, (UPPER, LOWER)):
        center = bottom + CARD_HEIGHT / 2
        harrow(ax, SPLIT_X, ANSWER_X - 0.008, center, INK_SUBTLE, scale=12, linewidth=1.1)
        box(ax, ANSWER_X, bottom, ANSWER_X + ANSWER_WIDTH, bottom + CARD_HEIGHT, name, soft, color, color, size=11, rounding=0.012)
        harrow(ax, ANSWER_X + ANSWER_WIDTH + 0.008, BAR_X - 0.075, center, color, scale=12, linewidth=1.1)
        probabilities(ax, center, after, color)
        ax.text(BAR_X + BAR_UNIT + 0.030, center, verdict, ha='left', va='center', fontsize=10.5, color=color)

    ax.text(ANSWER_X, UPPER + CARD_HEIGHT + 0.060, 'a person points at one', fontsize=11.5, color=INK_SOFT)
    ax.text(BAR_X - 0.075, UPPER + CARD_HEIGHT + 0.060, 'and training moves both', fontsize=11.5, color=INK_SOFT)
    ax.text(QUESTION_X, 0.055, 'no one writes the ideal answer; someone only picks the better of two', fontsize=11, color=INK_SUBTLE)

    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(0.0, 1.0)
    save(fig, target('preference-learning'))


if __name__ == '__main__':
    use_style()
    preference_learning()
