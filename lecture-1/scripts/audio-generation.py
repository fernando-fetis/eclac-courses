'''Audio is a sequence too: discretize the wave, then predict the next piece.'''

import matplotlib.pyplot as plt
import numpy as np

from _common import target
from diagram import box, harrow
from plotstyle import ACCENT, BORDER, EMERALD, EMERALD_SOFT, GRID, INK, INK_SOFT, INK_SUBTLE, SURFACE, WHITE, blank, figsize, save, use_style

TOKENS = ['214', '87', '356', '12', '298', '45']
WAVE_LEFT, WAVE_RIGHT, WAVE_MID, AMPLITUDE = 0.03, 0.97, 0.76, 0.15
DONE, PREDICTED = 0.62, 0.74
TOKEN_WIDTH = 0.055


def waveform(x: np.ndarray) -> np.ndarray:
    t = x * 60
    envelope = 0.35 + 0.65 * np.exp(-((x - 0.35) ** 2) / 0.08)
    return envelope * (np.sin(t) + 0.45 * np.sin(2.7 * t + 1.2) + 0.22 * np.sin(6.3 * t + 0.4)) / 1.67


def audio_generation() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.94, 0.38))
    blank(ax)

    grid = np.linspace(0, 1, 900)
    x = WAVE_LEFT + grid * (WAVE_RIGHT - WAVE_LEFT)
    y = WAVE_MID + AMPLITUDE * waveform(grid)

    done = x <= WAVE_LEFT + DONE * (WAVE_RIGHT - WAVE_LEFT)
    predicted = (~done) & (x <= WAVE_LEFT + PREDICTED * (WAVE_RIGHT - WAVE_LEFT))
    ax.plot(x[done], y[done], color=ACCENT, linewidth=1.8)
    ax.plot(x[predicted], y[predicted], color=EMERALD, linewidth=2.6)
    ax.plot(x[~done & ~predicted], y[~done & ~predicted], color=GRID, linewidth=1.6, linestyle=(0, (2, 3)))

    ax.text(WAVE_LEFT + 0.28, 0.955, 'already generated', fontsize=11, color=ACCENT, ha='center')
    ax.text(WAVE_LEFT + 0.64, 0.955, 'the next slice', fontsize=11, color=EMERALD, fontweight=600, ha='center')
    ax.text(WAVE_LEFT + 0.87, 0.955, 'not yet', fontsize=11, color=INK_SUBTLE, ha='center')

    ax.text(0.0, 0.40, 'as pieces:', fontsize=11, color=INK_SOFT, va='center')
    x_box = 0.145
    for token in TOKENS:
        box(ax, x_box, 0.34, x_box + TOKEN_WIDTH, 0.46, token, SURFACE, BORDER, INK, size=10.5, family='monospace', rounding=0.008)
        x_box += TOKEN_WIDTH + 0.008

    harrow(ax, x_box + 0.004, x_box + 0.052, 0.40, INK_SUBTLE, scale=12, linewidth=1.1)
    x_box += 0.06
    box(ax, x_box, 0.335, x_box + 0.105, 0.465, 'model', ACCENT, 'none', WHITE, size=11.5, weight=600, rounding=0.012)
    harrow(ax, x_box + 0.11, x_box + 0.155, 0.40, EMERALD, scale=12, linewidth=1.2)
    box(ax, x_box + 0.16, 0.34, x_box + 0.215, 0.46, '171', EMERALD_SOFT, EMERALD, EMERALD, size=10.5, family='monospace', rounding=0.008)

    ax.text(0.0, 0.10, 'the same loop as text: a short slice of sound becomes a piece, and the model predicts the next one', fontsize=11.5, color=INK_SOFT, va='center')

    ax.set_ylim(0.02, 1.02)
    save(fig, target('audio-generation'))


if __name__ == '__main__':
    use_style()
    audio_generation()
