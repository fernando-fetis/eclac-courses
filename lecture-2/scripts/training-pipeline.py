'''Three trainings: what each one reads, and what each one learns to do.'''

import matplotlib.pyplot as plt

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, ACCENT_SOFT, EMERALD, EMERALD_SOFT, GOLD, GOLD_SOFT, INK_SOFT, INK_SUBTLE, blank, figsize, save, use_style

STAGES = [
    ('pre-training', 'raw text', 'predict the next token', ACCENT_SOFT, ACCENT),
    ('instruction tuning', 'written answers', 'answer the question asked', GOLD_SOFT, GOLD),
    ('preference learning', 'ranked pairs', 'answer the way people prefer', EMERALD_SOFT, EMERALD),
]

LEFT, WIDTH, GAP = 0.01, 0.30, 0.045
TOP, HEIGHT = 0.86, 0.20


def training_pipeline() -> None:
    fig, ax = plt.subplots(figsize=figsize(1.0, 0.34))
    blank(ax)

    for index, (name, data, task, facecolor, color) in enumerate(STAGES):
        x = LEFT + index * (WIDTH + GAP)
        box(ax, x, TOP - HEIGHT, x + WIDTH, TOP, name, facecolor, color, color, size=13, weight=600, rounding=0.012)
        if index:
            harrow(ax, x - GAP + 0.006, x - 0.006, TOP - HEIGHT / 2, INK_SUBTLE, scale=12, linewidth=1.2)

        ax.text(x + WIDTH / 2, TOP - HEIGHT - 0.12, f'data: {data}', ha='center', va='center', fontsize=12, color=INK_SOFT)
        ax.text(x + WIDTH / 2, TOP - HEIGHT - 0.28, f'task: {task}', ha='center', va='center', fontsize=12, color=color)

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.34, 0.94)
    save(fig, target('training-pipeline'))


if __name__ == '__main__':
    use_style()
    training_pipeline()
