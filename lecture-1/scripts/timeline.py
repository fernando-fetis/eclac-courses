'''Milestones of generative AI, 2012 to today.

Dates: AlexNet wins ILSVRC 30 Sep 2012; GANs arXiv Jun 2014; seq2seq arXiv Sep 2014; Transformer arXiv Jun 2017; GPT-1 Jun 2018; GPT-3 arXiv May 2020; Stable Diffusion public release Aug 2022; ChatGPT 30 Nov 2022; Sora announced Feb 2024; DeepSeek-R1 Jan 2025; coding agents spread through 2025.
'''

import matplotlib.pyplot as plt

from _common import target
from plotstyle import ACCENT, BORDER, GOLD, INK_SOFT, INK_SUBTLE, figsize, save, use_style

# (year, name, color, side, lane): lanes keep neighboring labels apart.
EVENTS = [
    (2012.75, 'AlexNet', INK_SOFT, +1, 1),
    (2014.44, 'GANs', GOLD, -1, 1),
    (2014.69, 'seq2seq', ACCENT, +1, 2),
    (2017.44, 'Transformer', ACCENT, +1, 1),
    (2018.44, 'GPT-1', ACCENT, -1, 1),
    (2020.41, 'GPT-3', ACCENT, +1, 1),
    (2022.64, 'Stable Diffusion', GOLD, +1, 2),
    (2022.91, 'ChatGPT', ACCENT, -1, 1),
    (2024.12, 'Sora', GOLD, -1, 2),
    (2025.05, 'DeepSeek-R1', ACCENT, +1, 1),
    (2025.60, 'Coding agents', ACCENT, -1, 1),
]
LANE_HEIGHT = {1: 0.30, 2: 0.62}


def timeline() -> None:
    fig, ax = plt.subplots(figsize=figsize(1.0, 0.36))
    ax.set_axis_off()
    ax.grid(False)
    ax.axhline(0, xmin=0.02, xmax=0.98, color=INK_SOFT, linewidth=1.2, zorder=1)

    for year in range(2012, 2027):
        ax.plot([year, year], [-0.045, 0.045], color=BORDER, linewidth=1.0, zorder=1)
        ax.text(year, -0.14, str(year), ha='center', va='top', fontsize=9.5, color=INK_SUBTLE)

    for x, name, color, side, lane in EVENTS:
        stem = LANE_HEIGHT[lane] * side
        alignment = 'bottom' if side > 0 else 'top'
        ax.plot([x, x], [0, stem], color=color, linewidth=1.1, alpha=0.5, zorder=2)
        ax.plot([x], [0], marker='o', markersize=5.5, color=color, zorder=3)
        ax.text(x, stem + 0.06 * side, name, ha='center', va=alignment, fontsize=13, color=color, fontweight=600, zorder=3)

    ax.set_xlim(2011.0, 2027.0)
    ax.set_ylim(-1.0, 1.0)
    save(fig, target('timeline'))


if __name__ == '__main__':
    use_style()
    timeline()
