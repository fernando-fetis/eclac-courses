'''A tool call in sequence: the model writes, pauses, the program acts, it resumes.'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import FancyBboxPatch

from _common import target
from diagram import box, varrow
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, GOLD, GOLD_SOFT, INK, INK_SOFT, SURFACE, blank, figsize, save, use_style

STYLE = {
    'plain': (SURFACE, BORDER, INK),
    'marker': (GOLD_SOFT, GOLD, GOLD),
    'call': (ACCENT_SOFT, ACCENT, ACCENT),
    'result': (EMERALD_SOFT, EMERALD, EMERALD),
}

HEIGHT = 0.105
LEFT = 0.17
GAP = 0.007

ASK = [('What is the population of Chile?', 'plain')]
WRITE = [
    ('Let me check the latest census.', 'plain'),
    ('<tool>', 'marker'),
    ('search("Chile population")', 'call'),
    ('</tool>', 'marker'),
]
CONTINUE = [
    ('<result>', 'marker'),
    ('19.6 million (2024)', 'result'),
    ('</result>', 'marker'),
    ('Chile has about 19.6 million people.', 'plain'),
]


def piece_width(text: str) -> float:
    return 0.0102 * len(text) + 0.022


def row_width(pieces: list[tuple[str, str]]) -> float:
    return sum(piece_width(text) for text, _ in pieces) + GAP * (len(pieces) - 1)


def pieces_row(ax: Axes, y: float, pieces: list[tuple[str, str]]) -> list[float]:
    x = LEFT
    centers = []
    for text, kind in pieces:
        facecolor, edgecolor, textcolor = STYLE[kind]
        width = piece_width(text)
        ax.add_patch(FancyBboxPatch((x, y), width, HEIGHT, boxstyle='round,pad=0,rounding_size=0.008', facecolor=facecolor, edgecolor=edgecolor, linewidth=1.0))
        ax.text(x + width / 2, y + HEIGHT / 2, text, ha='center', va='center', fontsize=10.5, color=textcolor, family='monospace')
        centers.append(x + width / 2)
        x += width + GAP
    return centers


def actor(ax: Axes, y: float, label: str, color: str) -> None:
    ax.text(0.0, y + HEIGHT / 2, label, ha='left', va='center', fontsize=11, color=color, fontweight=600)


def tool_calls() -> None:
    fig, ax = plt.subplots(figsize=figsize(1.0, 0.36))
    blank(ax)

    actor(ax, 0.87, 'the user asks', INK_SOFT)
    pieces_row(ax, 0.87, ASK)

    actor(ax, 0.64, 'the model writes', ACCENT)
    centers = pieces_row(ax, 0.64, WRITE)
    pause = centers[-1]
    varrow(ax, 0.555, 0.630, pause, GOLD, scale=12, linewidth=1.2)
    ax.text(pause, 0.535, 'generation\npauses here', fontsize=10, color=GOLD, ha='center', va='top', linespacing=1.3)

    result_centers = pieces_row(ax, 0.09, CONTINUE)
    output_center = result_centers[1]

    actor(ax, 0.35, 'the program runs it', GOLD)
    box(ax, output_center - 0.23, 0.325, output_center + 0.23, 0.48, 'runs the search and pastes the output back into the text', GOLD_SOFT, GOLD, GOLD, size=10.5, rounding=0.012)
    varrow(ax, 0.315, 0.215, output_center, GOLD, scale=12, linewidth=1.2)

    actor(ax, 0.09, 'the model continues', ACCENT)

    ax.set_xlim(0.0, LEFT + max(row_width(pieces) for pieces in (ASK, WRITE, CONTINUE)) + 0.012)
    ax.set_ylim(0.0, 1.02)
    save(fig, target('tool-calls'))


if __name__ == '__main__':
    use_style()
    tool_calls()
