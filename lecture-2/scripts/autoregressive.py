'''One pass of generation: score every token in the vocabulary, then sample.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import FancyBboxPatch

from _common import target
from diagram import box, harrow, varrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, INK, INK_SUBTLE, SURFACE, WHITE, blank, figsize, save, use_style

PROMPT = ['In', 'the', 'first', 'half', 'of', '2007', ',']

# Illustrative, and whole words: the shape of the distribution is the point.
CANDIDATES = [('economy', 0.31), ('region', 0.18), ('central', 0.12), ('country', 0.09), ('balance', 0.06)]

TOKEN_Y, TOKEN_HEIGHT = 0.86, 0.12
MODEL_LEFT, MODEL_RIGHT, MODEL_MIDDLE = 0.04, 0.24, 0.57
BAR_LEFT, BAR_UNIT = 0.66, 0.72
BAR_TOP, BAR_STEP, BAR_HEIGHT = 0.79, 0.115, 0.075


def token_width(text: str) -> float:
    return 0.0125 * len(text) + 0.024


def token(ax: Axes, x: float, y: float, text: str, facecolor: str, edgecolor: str, textcolor: str) -> float:
    width = token_width(text)
    ax.add_patch(FancyBboxPatch((x, y), width, TOKEN_HEIGHT, boxstyle='round,pad=0,rounding_size=0.008', facecolor=facecolor, edgecolor=edgecolor, linewidth=1.0))
    ax.text(x + width / 2, y + TOKEN_HEIGHT / 2, text, ha='center', va='center', fontsize=11, family='monospace', color=textcolor)
    return x + width + 0.007


def autoregressive() -> None:
    fig, ax = plt.subplots(figsize=figsize(1.0, 0.34))
    blank(ax)

    x = 0.0
    for word in PROMPT:
        x = token(ax, x, TOKEN_Y, word, SURFACE, BORDER, INK)

    stem = MODEL_LEFT + (MODEL_RIGHT - MODEL_LEFT) / 2
    varrow(ax, TOKEN_Y - 0.012, MODEL_MIDDLE + 0.075, stem, INK_SUBTLE, scale=12, linewidth=1.1)
    box(ax, MODEL_LEFT, MODEL_MIDDLE - 0.065, MODEL_RIGHT, MODEL_MIDDLE + 0.065, 'GPT', ACCENT, 'none', WHITE, size=13, weight=600, rounding=0.012)
    harrow(ax, MODEL_RIGHT + 0.008, 0.53, MODEL_MIDDLE, INK_SUBTLE, scale=12, linewidth=1.1)
    ax.text(stem, MODEL_MIDDLE - 0.10, 'Generative Pre-trained\nTransformer', ha='center', va='top', fontsize=11, color=ACCENT, linespacing=1.5)

    for index, (word, probability) in enumerate(CANDIDATES):
        y = BAR_TOP - index * BAR_STEP
        chosen = index == 0
        color = EMERALD if chosen else ACCENT
        ax.add_patch(FancyBboxPatch((BAR_LEFT, y), probability * BAR_UNIT, BAR_HEIGHT, boxstyle='round,pad=0,rounding_size=0.006', facecolor=EMERALD_SOFT if chosen else ACCENT_SOFT, edgecolor=color, linewidth=1.0))
        ax.text(BAR_LEFT - 0.012, y + BAR_HEIGHT / 2, word, ha='right', va='center', fontsize=11, family='monospace', color=color)
        ax.text(BAR_LEFT + probability * BAR_UNIT + 0.012, y + BAR_HEIGHT / 2, f'{probability:.2f}', ha='left', va='center', fontsize=10.5, color=color)

    ax.text(BAR_LEFT - 0.012, BAR_TOP + BAR_HEIGHT + 0.05, 'one probability for every token in the vocabulary', ha='left', fontsize=11.5, color=INK_SUBTLE)
    ax.text(BAR_LEFT - 0.012, 0.14, 'sample one, append it to the prompt, and ask again', ha='left', fontsize=11.5, color=EMERALD)

    ax.set_xlim(-0.01, 1.02)
    ax.set_ylim(0.08, 1.0)
    save(fig, target('autoregressive'))


if __name__ == '__main__':
    use_style()
    autoregressive()
