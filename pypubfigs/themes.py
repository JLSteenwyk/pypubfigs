import seaborn as sns
import matplotlib.pyplot as plt


def _set_theme(style='white', params=None):
    """Set the base theme using seaborn and matplotlib."""
    sns.set_theme(style=style)
    if params:
        plt.rcParams.update(params)

def _move_legend_bottom(ax, y_offset=-0.1, text_color=None, base_size=12):
    """Helper function to place legend below the plot."""
    legend = ax.legend(
        loc='upper center',
        bbox_to_anchor=(0.5, y_offset),
        frameon=False,
        ncol=3,
        fontsize=base_size,
        title_fontsize=base_size + 2
    )
    if text_color:
        plt.setp(legend.get_texts(), color=text_color)
        plt.setp(legend.get_title(), color=text_color)

# === Themes ===

def theme_simple(base_size=12):
    params = {
        'font.size': base_size,
        'axes.titlesize': base_size + 4,
        'axes.labelsize': base_size + 2,
        'xtick.labelsize': base_size,
        'ytick.labelsize': base_size,
        'legend.title_fontsize': base_size + 2,
        'legend.fontsize': base_size,
        'figure.facecolor': 'none',
        'axes.facecolor': 'none',
        'axes.edgecolor': 'black',
        'axes.grid': False,
        'axes.spines.top': False,
        'axes.spines.right': False,
    }
    _set_theme('white', params)
    return lambda ax: _move_legend_bottom(ax, base_size=base_size)

def theme_red(base_size=12):
    params = {
        'font.size': base_size,
        'axes.titlesize': base_size + 4,
        'axes.labelsize': base_size + 2,
        'xtick.labelsize': base_size,
        'ytick.labelsize': base_size,
        'figure.facecolor': '#8B1A1A',
        'axes.facecolor': '#8B1A1A',
        'axes.edgecolor': 'white',
        'axes.labelcolor': 'white',
        'xtick.color': 'white',
        'ytick.color': 'white',
        'grid.color': 'white',
        'axes.grid': True,
        'text.color': 'white',
        'axes.spines.top': False,
        'axes.spines.right': False,
    }
    _set_theme('dark', params)
    return lambda ax: _move_legend_bottom(ax, text_color='white', base_size=base_size)

def theme_grid(base_size=12):
    params = {
        'font.size': base_size,
        'axes.titlesize': base_size + 4,
        'axes.labelsize': base_size + 2,
        'figure.facecolor': 'none',
        'axes.facecolor': 'none',
        'axes.edgecolor': 'black',
        'axes.grid': True,
        'grid.color': 'lightgrey',
        'axes.spines.top': False,
        'axes.spines.right': False,
    }
    _set_theme('whitegrid', params)
    return lambda ax: _move_legend_bottom(ax, base_size=base_size)

def theme_grey(base_size=12):
    params = {
        'font.size': base_size,
        'axes.titlesize': base_size + 4,
        'axes.labelsize': base_size + 2,
        'figure.facecolor': 'none',
        'axes.facecolor': '#E5E5E5',
        'grid.color': 'white',
        'axes.grid': True,
        'axes.edgecolor': 'black',
        'axes.spines.top': False,
        'axes.spines.right': False,
    }
    _set_theme('white', params)
    return lambda ax: _move_legend_bottom(ax, base_size=base_size)

def theme_blue(base_size=12):
    params = {
        'font.size': base_size,
        'axes.titlesize': base_size + 4,
        'axes.labelsize': base_size + 2,
        'figure.facecolor': '#104E8B',
        'axes.facecolor': '#104E8B',
        'axes.edgecolor': 'white',
        'axes.labelcolor': 'white',
        'xtick.color': 'white',
        'ytick.color': 'white',
        'grid.color': 'white',
        'axes.grid': True,
        'text.color': 'white',
        'axes.spines.top': False,
        'axes.spines.right': False,
    }
    _set_theme('dark', params)
    return lambda ax: _move_legend_bottom(ax, text_color='white', base_size=base_size)

def theme_black(base_size=12):
    params = {
        'font.size': base_size,
        'axes.titlesize': base_size + 4,
        'axes.labelsize': base_size + 2,
        'figure.facecolor': 'black',
        'axes.facecolor': 'black',
        'axes.edgecolor': 'white',
        'axes.labelcolor': 'white',
        'xtick.color': 'white',
        'ytick.color': 'white',
        'grid.color': 'white',
        'axes.grid': True,
        'text.color': 'white',
        'axes.spines.top': False,
        'axes.spines.right': False,
    }
    _set_theme('dark', params)
    return lambda ax: _move_legend_bottom(ax, text_color='white', base_size=base_size)

def theme_big_simple(base_size=16):
    params = {
        'font.size': base_size,
        'axes.titlesize': base_size + 8,
        'axes.labelsize': base_size + 8,
        'xtick.labelsize': base_size + 4,
        'ytick.labelsize': base_size + 4,
        'figure.facecolor': 'none',
        'axes.facecolor': 'none',
        'axes.edgecolor': 'black',
        'axes.linewidth': 1.0,
        'xtick.major.size': 5,
        'ytick.major.size': 5,
        'axes.grid': False,
        'axes.spines.top': False,
        'axes.spines.right': False,
    }
    _set_theme('white', params)
    return lambda ax: _move_legend_bottom(ax, y_offset=-0.15, base_size=base_size)

def theme_big_grid(base_size=12):
    params = {
        'font.size': base_size,
        'axes.titlesize': 16,
        'axes.labelsize': 24,
        'xtick.labelsize': 20,
        'ytick.labelsize': 20,
        'figure.facecolor': 'none',
        'axes.facecolor': 'none',
        'axes.edgecolor': 'black',
        'axes.grid': True,
        'grid.color': 'lightgrey',
        'axes.spines.top': False,
        'axes.spines.right': False,
    }
    _set_theme('whitegrid', params)
    return lambda ax: _move_legend_bottom(ax, y_offset=-0.15, base_size=base_size)
