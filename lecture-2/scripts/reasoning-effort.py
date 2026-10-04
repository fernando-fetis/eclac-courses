'''One model, one question, three budgets of thinking before the answer.'''

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, CRIMSON, CRIMSON_SOFT, EMERALD, EMERALD_SOFT, INK, INK_SOFT, INK_SUBTLE, SURFACE, blank, figsize, save, use_style

# Illustrative: the shape of the trade, not a measurement.
EFFORTS = [('low effort', 0.08, '120 tokens', False), ('medium effort', 0.20, '900 tokens', False), ('high effort', 0.34, '4 200 tokens', True)]

QUESTION_X, QUESTION_WIDTH = 0.02, 0.17
THINK_X = 0.30
ANSWER_WIDTH = 0.12

TOP, STEP, HEIGHT = 0.78, 0.24, 0.115


def reasoning_effort() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.94, 0.42))
    blank(ax)

    rows = [TOP - index * STEP for index in range(len(EFFORTS))]
    middle = (rows[0] + rows[-1]) / 2

    box(ax, QUESTION_X, middle - HEIGHT / 2, QUESTION_X + QUESTION_WIDTH, middle + HEIGHT / 2, 'the same\nquestion', SURFACE, BORDER, INK, size=12, rounding=0.012)
    ax.plot([QUESTION_X + QUESTION_WIDTH + 0.008, 0.25], [middle, middle], color=INK_SUBTLE, linewidth=1.1)
    ax.plot([0.25, 0.25], [rows[-1], rows[0]], color=INK_SUBTLE, linewidth=1.1)

    for (effort, length, spent, right), y in zip(EFFORTS, rows):
        harrow(ax, 0.25, THINK_X - 0.008, y, INK_SUBTLE, scale=11, linewidth=1.1)
        ax.add_patch(Rectangle((THINK_X, y - HEIGHT / 2), length, HEIGHT, facecolor=ACCENT_SOFT, edgecolor=ACCENT, linewidth=1.0))
        ax.text(THINK_X + 0.012, y, 'thinking', ha='left', va='center', fontsize=11, color=ACCENT)
        ax.text(THINK_X, y + HEIGHT / 2 + 0.028, effort, ha='left', fontsize=11, color=INK_SOFT)

        answer_x = THINK_X + length + 0.018
        box(ax, answer_x, y - HEIGHT / 2, answer_x + ANSWER_WIDTH, y + HEIGHT / 2, 'right' if right else 'wrong', EMERALD_SOFT if right else CRIMSON_SOFT, EMERALD if right else CRIMSON, EMERALD if right else CRIMSON, size=11.5, rounding=0.010)
        ax.text(0.99, y, spent, ha='right', va='center', fontsize=11, color=INK_SUBTLE)

    ax.text(THINK_X, TOP + HEIGHT / 2 + 0.10, 'the model writes its work before answering', fontsize=11.5, color=INK_SOFT)
    ax.text(0.99, TOP + HEIGHT / 2 + 0.10, 'generated, and billed', ha='right', fontsize=11.5, color=INK_SUBTLE)
    ax.text(THINK_X, rows[-1] - HEIGHT / 2 - 0.085, 'same weights, same prompt: only the budget changes', fontsize=11.5, color=ACCENT)

    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(0.10, 1.0)
    save(fig, target('reasoning-effort'))


if __name__ == '__main__':
    use_style()
    reasoning_effort()
