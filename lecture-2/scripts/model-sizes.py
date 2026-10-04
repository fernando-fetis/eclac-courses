'''Parameter counts, from the model in the notebook to the ones nobody discloses.'''

import matplotlib.pyplot as plt
import numpy as np

from _common import target
from plotstyle import ACCENT, ACCENT_SOFT, BORDER, EMERALD, EMERALD_SOFT, INK_SOFT, INK_SUBTLE, SURFACE, figsize, save, use_style

# Parameters in millions, as reported by each model card or paper. The ones the notebook actually runs are marked.
MODELS = [
    ('the notebook model', 2026, 11.5, True),
    ('GPT 1', 2018, 117, False),
    ('GPT 2', 2019, 124, False),
    ('GPT 2 XL', 2019, 1_558, True),
    ('Qwen2.5 7B', 2024, 7_600, True),
    ('Qwen3 8B', 2025, 8_200, True),
    ('GPT 3', 2020, 175_000, False),
    ('Llama 3.1', 2024, 405_000, False),
    ('DeepSeek V3', 2024, 671_000, False),
]


def label(parameters: float) -> str:
    if parameters < 1_000:
        return f'{parameters:g} M'
    return f'{parameters / 1_000:g} B'


def model_sizes() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.88, 0.44))

    names = [f'{name} ({year})' for name, year, _, _ in MODELS]
    values = [parameters for _, _, parameters, _ in MODELS]
    runs = [notebook for _, _, _, notebook in MODELS]
    y = np.arange(len(MODELS))[::-1]

    ax.barh(y, values, color=[EMERALD_SOFT if r else ACCENT_SOFT for r in runs], edgecolor=[EMERALD if r else ACCENT for r in runs], height=0.62)
    for position, value, runs_here in zip(y, values, runs):
        ax.text(value * 1.35, position, label(value), va='center', fontsize=11.5, color=EMERALD if runs_here else ACCENT)

    ax.barh([-1], [1_800_000], color=SURFACE, edgecolor=BORDER, height=0.62, hatch='///')
    ax.text(2.2, -1, 'GPT-6 Astra, Fable 5.1: not disclosed', va='center', ha='left', fontsize=11.5, color=INK_SUBTLE)

    ax.set_yticks(list(y) + [-1], names + ['frontier (2026)'], fontsize=11)
    ax.set_xscale('log')
    ax.set_xlim(0.75, 3_000_000)
    ax.set_ylim(-1.6, len(MODELS) - 0.35)
    ax.set_xlabel('parameters')
    ax.set_xticks([1, 10, 100, 1_000, 10_000, 100_000, 1_000_000], ['1 M', '10 M', '100 M', '1 B', '10 B', '100 B', '1 T'])
    ax.grid(axis='y', visible=False)
    ax.tick_params(axis='y', length=0)
    ax.set_axisbelow(True)
    ax.minorticks_off()
    ax.set_title('green: the models the notebook runs', fontsize=11, color=INK_SOFT, loc='left', pad=12)

    save(fig, target('model-sizes'))


if __name__ == '__main__':
    use_style()
    model_sizes()
