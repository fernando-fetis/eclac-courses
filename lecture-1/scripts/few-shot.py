'''Few-shot prompting: solved examples in the prompt, and the model continues.'''

import matplotlib.pyplot as plt

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, BORDER, EMERALD, EMERALD_SOFT, INK, INK_SOFT, INK_SUBTLE, SURFACE, WHITE, blank, figsize, save, use_style

PROMPT = 'cat   → gato\ndog   → perro\nhorse →'


def few_shot() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.80, 0.28))
    blank(ax)

    box(ax, 0.03, 0.16, 0.37, 0.86, None, SURFACE, BORDER, None)
    ax.text(0.095, 0.51, PROMPT, ha='left', va='center', fontsize=13, color=INK, family='monospace', linespacing=1.8)
    ax.text(0.20, 0.97, 'the prompt: two solved examples, one unfinished', ha='center', fontsize=11, color=INK_SOFT)

    harrow(ax, 0.38, 0.455, 0.51, INK_SUBTLE, scale=13, linewidth=1.2)
    box(ax, 0.465, 0.40, 0.595, 0.62, 'model', ACCENT, 'none', WHITE, size=12.5, weight=600)
    harrow(ax, 0.605, 0.675, 0.51, EMERALD, scale=13)
    box(ax, 0.685, 0.40, 0.885, 0.62, 'caballo', EMERALD_SOFT, EMERALD, EMERALD, size=13, family='monospace')
    ax.text(0.785, 0.24, 'it simply continues the text', ha='center', fontsize=11, color=INK_SUBTLE)

    ax.set_ylim(0.10, 1.04)
    save(fig, target('few-shot'))


if __name__ == '__main__':
    use_style()
    few_shot()
