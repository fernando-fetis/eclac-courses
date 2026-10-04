'''Four ways to score a model, and what each of them cannot see.'''

import matplotlib.pyplot as plt

from _common import target
from diagram import box
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, CRIMSON, EMERALD, EMERALD_SOFT, GOLD, GOLD_SOFT, INK_SOFT, SURFACE, blank, figsize, save, use_style

METHODS = [
    ('held-out perplexity', 'cheap, runs\nduring training', 'says nothing\nabout usefulness', SURFACE, BORDER, INK_SOFT),
    ('public benchmarks', 'comparable\nacross models', 'the answers leak\ninto training data', ACCENT_SOFT, ACCENT, ACCENT),
    ('a model as judge', 'scales to\nthousands of answers', 'prefers long,\nconfident answers', GOLD_SOFT, GOLD, GOLD),
    ('people, on your task', 'the only measure\nthat decides', 'slow, and expensive\nto repeat', EMERALD_SOFT, EMERALD, EMERALD),
]

LEFT, WIDTH, GAP = 0.01, 0.235, 0.02
TOP, HEIGHT = 0.90, 0.20


def evaluation() -> None:
    fig, ax = plt.subplots(figsize=figsize(1.0, 0.32))
    blank(ax)

    for index, (name, strength, weakness, facecolor, edge, textcolor) in enumerate(METHODS):
        x = LEFT + index * (WIDTH + GAP)
        box(ax, x, TOP - HEIGHT, x + WIDTH, TOP, name, facecolor, edge, textcolor, size=12, weight=600, rounding=0.012)
        ax.text(x + WIDTH / 2, TOP - HEIGHT - 0.16, strength, ha='center', va='center', fontsize=11, color=INK_SOFT, linespacing=1.5)
        ax.text(x + WIDTH / 2, TOP - HEIGHT - 0.46, weakness, ha='center', va='center', fontsize=11, color=CRIMSON, linespacing=1.5)

    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(0.0, 0.96)
    save(fig, target('evaluation'))


if __name__ == '__main__':
    use_style()
    evaluation()
