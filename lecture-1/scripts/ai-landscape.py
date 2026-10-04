'''Nested fields: each ring lists work seen at that level and nowhere deeper.'''

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from _common import target
from plotstyle import ACCENT, ACCENT_SOFT, GOLD, GOLD_SOFT, INK_SOFT, INK_SUBTLE, MIST, SURFACE, blank, figsize, save, use_style

LAYERS = [
    (0.000, 0.000, 0.720, 1.000, 'Artificial intelligence', 'any technique that automates a task needing intelligence', INK_SOFT, MIST, 'robotics · planning · expert systems'),
    (0.035, 0.055, 0.650, 0.790, 'Machine learning', 'the rules are learned from data', ACCENT, SURFACE, 'spam filters · credit scoring'),
    (0.070, 0.110, 0.580, 0.580, 'Deep learning', 'the rules are learned by deep neural networks', ACCENT, ACCENT_SOFT, 'face recognition · speech-to-text'),
    (0.105, 0.165, 0.510, 0.370, 'Generative AI', 'the network produces new content', GOLD, GOLD_SOFT, 'chat assistants · image synthesis'),
]


def ai_landscape() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.92, 0.46))
    blank(ax)

    for x, y, right, top, name, gloss, color, fill, examples in LAYERS:
        ax.add_patch(FancyBboxPatch((x, y), right - x, top - y, boxstyle='round,pad=0,rounding_size=0.012', facecolor=fill, edgecolor=color, linewidth=1.3, zorder=2))
        ax.text(x + 0.022, top - 0.060, name, fontsize=14, fontweight=600, color=color, va='center', zorder=3)
        ax.text(x + 0.022, top - 0.135, gloss, fontsize=10.5, color=INK_SUBTLE, va='center', zorder=3)
        ax.text(0.755, top - 0.060, 'examples:', fontsize=9, color=INK_SUBTLE, va='center', ha='left', zorder=3)
        ax.text(0.755, top - 0.125, examples, fontsize=10.5, color=color, va='center', ha='left', zorder=3)

    save(fig, target('ai-landscape'))


if __name__ == '__main__':
    use_style()
    ai_landscape()
