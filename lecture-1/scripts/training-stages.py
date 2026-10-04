'''The three training stages, each with a sample of what its data looks like.'''

import matplotlib.pyplot as plt

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, EMERALD, INK, INK_SOFT, INK_SUBTLE, WHITE, blank, figsize, save, use_style

STAGES = [
    ('1 · Pre-training', INK_SOFT, 'The glaciers of Patagonia\nhave retreated steadily\nsince the 1970s, and the\nmeltwater feeds rivers\nthat …', 'any text at all: predict\nthe next piece', 'learns language and facts'),
    ('2 · Instruction tuning', ACCENT, 'User: Summarize this\nreport in one paragraph: …\n\nAssistant: The report\nfinds that regional …', 'written by people; same\nobjective, curated data', 'learns to answer'),
    ('3 · Preference tuning', EMERALD, 'Prompt: Explain inflation.\n\nA. Prices rise when …\nB. Well, it depends …\n\npreferred answer: A', 'people pick the better of\ntwo answers', 'learns tone and judgment'),
]
WIDTH = 0.30


def training_stages() -> None:
    fig, ax = plt.subplots(figsize=figsize(1.0, 0.40))
    blank(ax)

    for index, (title, color, sample, what, learns) in enumerate(STAGES):
        x = index * 0.35
        box(ax, x, 0.89, x + WIDTH, 1.005, title, color, 'none', WHITE, size=12.5, weight=600)
        box(ax, x, 0.34, x + WIDTH, 0.85, None, WHITE, color, None)
        ax.text(x + 0.016, 0.815, 'the training data:', fontsize=9, color=INK_SUBTLE, va='center')
        ax.text(x + 0.016, 0.575, sample, fontsize=9.5, color=INK, family='monospace', va='center', linespacing=1.55)

        ax.text(x + WIDTH / 2, 0.235, what, fontsize=10.5, color=INK_SOFT, ha='center', va='center', linespacing=1.4)
        ax.text(x + WIDTH / 2, 0.10, learns, fontsize=12, fontweight=600, color=color, ha='center', va='center')

        if index < len(STAGES) - 1:
            harrow(ax, x + WIDTH + 0.008, x + 0.345, 0.60, INK_SUBTLE, scale=13, linewidth=1.2)

    ax.set_ylim(0.03, 1.02)
    save(fig, target('training-stages'))


if __name__ == '__main__':
    use_style()
    training_stages()
