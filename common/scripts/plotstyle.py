'''Shared matplotlib style for every figure in the ECLAC AI courses.'''

import logging
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.figure import Figure

INK = '#1F2A3A'
INK_SOFT = '#4D5E75'
INK_SUBTLE = '#7A8AA0'
GRID = '#CFDBE8'
SURFACE = '#EEF3F9'
BORDER = '#CFDBE8'
ACCENT = '#0072BC'
ACCENT_SOFT = '#D6EAF6'
EMERALD = '#0F766E'
EMERALD_SOFT = '#D6F0EA'
GOLD = '#A37430'
GOLD_SOFT = '#F6ECD8'
CRIMSON = '#B03A48'
CRIMSON_SOFT = '#FBE4E6'
WHITE = '#FFFFFF'
MIST = '#F5F7FA'

SERIES = [ACCENT, '#C1721F', EMERALD, '#0891B2', '#005B96', INK_SUBTLE]
SEQUENTIAL = ['#F2F8FC', '#D6EAF6', '#8CC3E4', '#0072BC', '#005B96', '#00437C']

TEXT_WIDTH_IN = 10.0


def use_style() -> None:
    logging.getLogger('matplotlib.font_manager').setLevel(logging.ERROR)
    logging.getLogger('fontTools').setLevel(logging.ERROR)
    mpl.rcParams.update(
        {
            'font.family': 'sans-serif',
            'font.sans-serif': ['Fira Sans', 'Helvetica Neue', 'DejaVu Sans'],
            'mathtext.fontset': 'custom',
            'mathtext.rm': 'Fira Sans',
            'mathtext.it': 'Fira Sans:italic',
            'mathtext.bf': 'Fira Sans:medium',
            'font.size': 13,
            'axes.titlesize': 14,
            'axes.labelsize': 13,
            'xtick.labelsize': 11,
            'ytick.labelsize': 11,
            'legend.fontsize': 11,
            'axes.prop_cycle': mpl.cycler(color=SERIES),
            'text.color': INK,
            'axes.labelcolor': INK,
            'axes.edgecolor': INK_SOFT,
            'xtick.color': INK_SOFT,
            'ytick.color': INK_SOFT,
            'grid.color': GRID,
            'figure.facecolor': 'none',
            'axes.facecolor': 'none',
            'savefig.facecolor': 'none',
            'savefig.transparent': True,
            'axes.spines.top': False,
            'axes.spines.right': False,
            'axes.grid': True,
            'axes.linewidth': 1.0,
            'grid.linewidth': 0.8,
            'grid.alpha': 0.7,
            'lines.linewidth': 2.0,
            'lines.markersize': 5,
            'patch.linewidth': 1.0,
            'legend.frameon': False,
            'figure.dpi': 120,
            'pdf.fonttype': 42,
        }
    )


def figsize(fraction: float = 0.82, aspect: float = 0.52) -> tuple[float, float]:
    width = TEXT_WIDTH_IN * fraction
    return (width, width * aspect)


def cmap() -> LinearSegmentedColormap:
    return LinearSegmentedColormap.from_list('course', SEQUENTIAL)


def blank(ax: Axes) -> None:
    '''Turn an axes into a bare drawing surface for box-and-arrow diagrams.'''
    ax.set_axis_off()
    ax.grid(False)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)


def save(fig: Figure, path: Path, **layout: float) -> None:
    '''Write the figure cropped to its content, so a slide can center it.'''
    fig.tight_layout(pad=0.3, **layout)
    fig.savefig(path, transparent=True, bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)
