"""Matplotlib styling helpers for consistent figures."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

DEFAULT_STYLE = {
    "figure.figsize": (6.5, 4.0),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 10,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "lines.linewidth": 1.5,
}


def apply_style(style: dict | None = None) -> None:
    """Apply default or custom matplotlib style settings."""
    plt.rcParams.update(DEFAULT_STYLE)
    if style:
        plt.rcParams.update(style)


def save_figure(fig: plt.Figure, path: str | Path, **kwargs) -> Path:
    """Save a figure, ensuring the output directory exists."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, **kwargs)
    return output_path
