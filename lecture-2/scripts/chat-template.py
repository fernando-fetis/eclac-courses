'''A conversation is a single token stream, with special tokens as punctuation.'''

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from _common import target
from plotstyle import BORDER, CRIMSON, CRIMSON_SOFT, EMERALD, INK, SURFACE, blank, figsize, save, use_style

# The ChatML format, which is what the notebook prints out of a real tokenizer.
STREAM = [
    ('<|im_start|>system', 'special'),
    ('You answer questions about ECLAC statistics.', 'text'),
    ('<|im_end|>', 'special'),
    ('<|im_start|>user', 'special'),
    ('Which report publishes poverty by country?', 'text'),
    ('<|im_end|>', 'special'),
    ('<|im_start|>assistant', 'special'),
]

STYLES = {
    'special': (CRIMSON_SOFT, CRIMSON, CRIMSON),
    'text': (SURFACE, BORDER, INK),
}

LEFT, HEIGHT, GAP = 0.02, 0.115, 0.028


def chat_template() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.94, 0.44))
    blank(ax)

    top = 0.96
    for index, (text, kind) in enumerate(STREAM):
        y = top - index * (HEIGHT + GAP)
        facecolor, edgecolor, textcolor = STYLES[kind]
        width = 0.0128 * len(text) + 0.035
        ax.add_patch(FancyBboxPatch((LEFT, y - HEIGHT), width, HEIGHT, boxstyle='round,pad=0,rounding_size=0.008', facecolor=facecolor, edgecolor=edgecolor, linewidth=1.0))
        ax.text(LEFT + 0.016, y - HEIGHT / 2, text, ha='left', va='center', fontsize=11.5, family='monospace', color=textcolor)

    ax.plot([0.31, 0.74], [top - HEIGHT / 2, top - HEIGHT / 2], color=CRIMSON, linewidth=1.2)
    ax.text(0.75, top - HEIGHT / 2, 'special tokens\ndelimit the roles', ha='left', va='center', fontsize=11, color=CRIMSON, linespacing=1.5)

    assistant_y = top - 6 * (HEIGHT + GAP) - HEIGHT / 2
    ax.plot([0.30, 0.74], [assistant_y, assistant_y], color=EMERALD, linewidth=1.2)
    ax.text(0.75, assistant_y, 'the model writes from\nhere until <|im_end|>', ha='left', va='center', fontsize=11, color=EMERALD, linespacing=1.5)

    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(top - 7 * (HEIGHT + GAP) - 0.02, 1.0)
    save(fig, target('chat-template'))


if __name__ == '__main__':
    use_style()
    chat_template()
