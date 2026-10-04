'''An agent: a model deciding, acting through tools, and reading the results.'''

import math

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import Arc, FancyArrowPatch

from _common import target
from diagram import box, harrow, varrow
from plotstyle import ACCENT, BORDER, EMERALD, EMERALD_SOFT, GOLD, GOLD_SOFT, INK, INK_SOFT, INK_SUBTLE, SURFACE, WHITE, blank, figsize, save, use_style

ROW_BOTTOM, ROW_TOP = 0.60, 0.84
ASPECT = 2.59  # x units per y unit, so the loop icon is drawn round
GOAL = (0.00, 0.12)
MODEL = (0.16, 0.40)
ACTION = (0.45, 0.63)
RESULT = (0.68, 0.88)
LOOP_Y = 0.46


def row_node(ax: Axes, span: tuple[float, float], label: str, facecolor: str, edgecolor: str, textcolor: str, weight: int = 400) -> None:
    box(ax, span[0], ROW_BOTTOM, span[1], ROW_TOP, label, facecolor, edgecolor, textcolor, weight=weight, rounding=0.016)


def loop_icon(ax: Axes, x: float, y: float, color: str, radius: float = 0.036, gap: float = 52) -> None:
    '''A small circular arrow, the symbol for the cycle repeating.'''
    x_radius, y_radius = radius / ASPECT, radius
    start, end = 90 + gap / 2, 90 - gap / 2 + 360

    def point(degrees: float) -> tuple[float, float]:
        angle = math.radians(degrees)
        return x + x_radius * math.cos(angle), y + y_radius * math.sin(angle)

    ax.add_patch(Arc((x, y), 2 * x_radius, 2 * y_radius, theta1=start, theta2=end - 9, color=color, linewidth=1.4))
    ax.add_patch(FancyArrowPatch(point(end - 12), point(end), arrowstyle='-|>', mutation_scale=10, color=color, linewidth=1.4))


def chip(ax: Axes, x0: float, x1: float, y0: float, label: str) -> None:
    box(ax, x0, y0, x1, y0 + 0.07, label, WHITE, BORDER, INK_SOFT, size=10, rounding=0.012)


def agent_loop() -> None:
    fig, ax = plt.subplots(figsize=figsize(0.96, 0.44))
    blank(ax)
    middle = (ROW_BOTTOM + ROW_TOP) / 2
    model_center = sum(MODEL) / 2
    result_center = sum(RESULT) / 2

    row_node(ax, GOAL, 'a goal,\nin words', SURFACE, BORDER, INK)
    harrow(ax, GOAL[1] + 0.005, MODEL[0] - 0.005, middle, INK_SUBTLE, linewidth=1.5)
    row_node(ax, MODEL, 'the model\ndecides the next step', ACCENT, 'none', WHITE, weight=600)
    harrow(ax, MODEL[1] + 0.005, ACTION[0] - 0.005, middle, ACCENT, linewidth=1.5)
    row_node(ax, ACTION, 'a tool runs\nthe action', GOLD_SOFT, GOLD, GOLD, weight=600)
    harrow(ax, ACTION[1] + 0.005, RESULT[0] - 0.005, middle, GOLD, linewidth=1.5)
    row_node(ax, RESULT, 'the result\ncomes back', EMERALD_SOFT, EMERALD, EMERALD)

    ax.plot([result_center, result_center], [ROW_BOTTOM - 0.005, LOOP_Y], color=EMERALD, linewidth=1.4)
    ax.plot([result_center, model_center], [LOOP_Y, LOOP_Y], color=EMERALD, linewidth=1.4)
    varrow(ax, LOOP_Y, ROW_BOTTOM - 0.005, model_center, EMERALD, linewidth=1.4)
    loop_center = (model_center + result_center) / 2
    loop_icon(ax, loop_center, 0.405, EMERALD)
    ax.text(loop_center, 0.345, 'the loop repeats until the goal is met', fontsize=10.5, color=EMERALD, ha='center', va='top')

    varrow(ax, ROW_TOP + 0.005, 0.935, model_center, INK_SUBTLE, linewidth=1.4)
    ax.text(model_center + 0.018, 0.89, 'when it judges the goal met', fontsize=10, color=INK_SUBTLE, ha='left', va='center')
    box(ax, MODEL[0], 0.94, MODEL[1], 1.11, 'the final answer,\nor the finished task', EMERALD_SOFT, EMERALD, EMERALD, size=11, rounding=0.016)

    box(ax, 0.30, 0.02, 0.79, 0.28, None, SURFACE, BORDER, None, rounding=0.016)
    ax.text(0.545, 0.235, 'tools it can call', fontsize=10, color=INK_SOFT, ha='center', va='center')
    chip(ax, 0.3475, 0.4925, 0.125, 'search the web')
    chip(ax, 0.5075, 0.6225, 0.125, 'read a file')
    chip(ax, 0.6375, 0.7425, 0.125, 'run code')
    chip(ax, 0.37, 0.53, 0.04, 'send an email')
    chip(ax, 0.545, 0.72, 0.04, 'launch sub-agents')

    ax.set_ylim(-0.02, 1.12)
    save(fig, target('agent-loop'))


if __name__ == '__main__':
    use_style()
    agent_loop()
