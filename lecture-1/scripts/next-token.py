'''Token-by-token generation: predict one piece, append it, ask again.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import FancyBboxPatch

from _common import target
from diagram import box, harrow, varrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, INK, INK_SUBTLE, SURFACE, WHITE, blank, figsize, save, use_style

PROMPT = ['ECLAC', 'was', 'founded', 'in']
GENERATED = ['1948', ',', 'based', 'in', 'Santiago']
ROWS = 3
ROW_TOP, ROW_STEP, TOKEN_HEIGHT = 0.86, 0.27, 0.115
MODEL_X, PREDICTION_X = 0.60, 0.76
STYLE = {
    'prompt': (SURFACE, BORDER, INK),
    'generated': (ACCENT_SOFT, ACCENT, ACCENT),
    'new': (EMERALD_SOFT, EMERALD, EMERALD),
}


def token_width(text: str) -> float:
    return 0.0125 * len(text) + 0.026


def token(ax: Axes, x: float, y: float, text: str, kind: str) -> float:
    facecolor, edgecolor, textcolor = STYLE[kind]
    width = token_width(text)
    ax.add_patch(FancyBboxPatch((x, y), width, TOKEN_HEIGHT, boxstyle='round,pad=0,rounding_size=0.008', facecolor=facecolor, edgecolor=edgecolor, linewidth=1.0))
    ax.text(x + width / 2, y + TOKEN_HEIGHT / 2, text, ha='center', va='center', fontsize=11.5, color=textcolor, family='monospace')
    return x + width + 0.007


def appended_center(index: int) -> float:
    x = sum(token_width(piece) + 0.007 for piece in PROMPT)
    for piece in GENERATED[:index]:
        x += token_width(piece) + 0.007
    return x + token_width(GENERATED[index]) / 2


def row(ax: Axes, index: int) -> None:
    y = ROW_TOP - index * ROW_STEP
    middle = y + TOKEN_HEIGHT / 2
    x = 0.0
    for piece in PROMPT:
        x = token(ax, x, y, piece, 'prompt')
    for piece in GENERATED[:index]:
        x = token(ax, x, y, piece, 'generated')

    harrow(ax, x + 0.004, MODEL_X - 0.008, middle, INK_SUBTLE, scale=12, linewidth=1.1)
    box(ax, MODEL_X, y - 0.008, MODEL_X + 0.10, y + TOKEN_HEIGHT + 0.008, 'model', ACCENT, 'none', WHITE, size=11.5, weight=600, rounding=0.012)
    harrow(ax, MODEL_X + 0.108, PREDICTION_X - 0.008, middle, EMERALD, scale=12, linewidth=1.2)
    token(ax, PREDICTION_X, y, GENERATED[index], 'new')

    if index < ROWS - 1:
        prediction_center = PREDICTION_X + token_width(GENERATED[index]) / 2
        target_center = appended_center(index)
        lane = y - 0.085
        next_top = y - ROW_STEP + TOKEN_HEIGHT + 0.010
        ax.plot([prediction_center, prediction_center], [y - 0.010, lane], color=EMERALD, linewidth=1.2)
        ax.plot([prediction_center, target_center], [lane, lane], color=EMERALD, linewidth=1.2)
        varrow(ax, lane, next_top, target_center, EMERALD, scale=12, linewidth=1.2)
        ax.text((prediction_center + target_center) / 2, lane + 0.018, 'appended, asked again', fontsize=9.5, color=EMERALD, ha='center', va='bottom')


def next_token() -> None:
    fig, ax = plt.subplots(figsize=figsize(1.0, 0.40))
    blank(ax)
    for index in range(ROWS):
        row(ax, index)
    ax.text(0.0, 0.055, '… five loops later:', fontsize=11, color=INK_SUBTLE, va='center')
    x = 0.22
    for piece in PROMPT:
        x = token(ax, x, 0.0, piece, 'prompt')
    for piece in GENERATED:
        x = token(ax, x, 0.0, piece, 'generated')

    ax.set_ylim(-0.04, 1.01)
    save(fig, target('next-token'))


if __name__ == '__main__':
    use_style()
    next_token()
