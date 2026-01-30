"""Input/output helpers for data ingestion."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def read_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    """Read a CSV file with safe defaults."""
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")
    return pd.read_csv(csv_path, **kwargs)


def read_excel(path: str | Path, sheet_name: str | int | None = 0, **kwargs) -> pd.DataFrame:
    """Read an Excel file with safe defaults."""
    excel_path = Path(path)
    if not excel_path.exists():
        raise FileNotFoundError(f"Excel file not found: {excel_path}")
    return pd.read_excel(excel_path, sheet_name=sheet_name, **kwargs)
