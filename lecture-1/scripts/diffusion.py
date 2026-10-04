'''Diffusion: one sequence from picture to noise, walked in both directions.'''

import matplotlib.pyplot as plt
import numpy as np

from _common import target
from diagram import harrow
from plotstyle import ACCENT, BORDER, INK_SUBTLE, blank, figsize, save, use_style

FRAMES = 6
SIZE = 64
WIDTH, HEIGHT, BOTTOM = 0.125, 0.37, 0.31


def scene() -> np.ndarray:
    ys, xs = np.mgrid[0:SIZE, 0:SIZE]
    picture = np.zeros((SIZE, SIZE, 3))
    picture[ys < int(SIZE * 0.62)] = np.array([0.55, 0.78, 0.92])
    picture[ys >= int(SIZE * 0.62)] = np.array([0.24, 0.52, 0.38])
    disc = (xs - SIZE * 0.72) ** 2 + (ys - SIZE * 0.26) ** 2 < (SIZE * 0.11) ** 2
    picture[disc] = np.array([0.98, 0.82, 0.35])
    return picture


def frames() -> list[np.ndarray]:
    generator = np.random.default_rng(20260607)
    clean = scene()
    pictures = []
    for step in range(FRAMES):
        level = (step / (FRAMES - 1)) ** 0.8
        grain = generator.random((SIZE, SIZE, 1))
        noise = np.repeat(0.25 + 0.6 * grain, 3, axis=2)
        pictures.append(np.clip(level * noise + (1 - level) * clean, 0, 1))
    return pictures


def diffusion() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.96, 0.34))
    blank(ax)

    gap = (1.0 - FRAMES * WIDTH) / (FRAMES - 1)
    centers = []
    for index, picture in enumerate(frames()):
        x = index * (WIDTH + gap)
        ax.imshow(picture, extent=(x, x + WIDTH, BOTTOM, BOTTOM + HEIGHT), zorder=2, interpolation='bilinear', aspect='auto')
        ax.add_patch(plt.Rectangle((x, BOTTOM), WIDTH, HEIGHT, facecolor='none', edgecolor=BORDER, linewidth=1.0, zorder=3))
        centers.append(x + WIDTH / 2)

    ax.text(centers[0], BOTTOM - 0.10, 'a real picture', ha='center', fontsize=11, color=INK_SUBTLE)
    ax.text(centers[-1], BOTTOM - 0.10, 'pure noise', ha='center', fontsize=11, color=INK_SUBTLE)

    for left, right in zip(centers[:-1], centers[1:]):
        harrow(ax, left + 0.025, right - 0.025, 0.85, INK_SUBTLE, scale=13)
        harrow(ax, right - 0.025, left + 0.025, 0.11, ACCENT, scale=13, linewidth=1.5)

    ax.text(0.5, 0.97, 'forward: add a little noise (a fixed recipe, nothing is learned)', ha='center', fontsize=12, color=INK_SUBTLE)
    ax.text(0.5, -0.02, 'reverse: remove a little noise (this is what the network learns)', ha='center', fontsize=12.5, color=ACCENT, fontweight=600)

    ax.set_xlim(-0.01, 1.01)
    ax.set_ylim(-0.08, 1.04)
    save(fig, target('diffusion'))


if __name__ == '__main__':
    use_style()
    diffusion()
