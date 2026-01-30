# geoscience-plots

A reproducible structure for geoscience plotting workflows.

## Repository layout

- `data/raw`: source data exactly as received.
- `data/processed`: cleaned, analysis-ready datasets.
- `data/metadata`: data dictionaries, provenance, and notes.
- `scripts/00_utils`: shared helpers for styling and I/O.
- `scripts/01_cleaning`: scripts that convert raw data to processed data.
- `scripts/02_plotting`: scripts that generate figures from processed data.
- `scripts/99_sandbox`: experimental or exploratory scripts.
- `figures/drafts`: working figures and checkpoints.
- `figures/final`: publication-ready figures.
- `figures/svg_pdf`: vector exports (SVG/PDF).
- `docs`: workflow documentation and figure specs.
- `outputs/logs`: runtime logs.
- `outputs/tables`: exported summary tables.

## Workflow

1. **Raw → Processed**: place incoming data in `data/raw`, then run cleaning scripts in
   `scripts/01_cleaning` to produce datasets in `data/processed`.
2. **Processed → Figures**: run plotting scripts in `scripts/02_plotting` to generate
   figures in `figures/drafts` or `figures/final`.
3. **Documentation**: capture data context in `docs/data_dictionary.md` and figure
   requirements in `docs/figure_specs.md`.

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running scripts

```bash
python scripts/01_cleaning/clean_example.py
python scripts/02_plotting/plot_example.py
```

Use the helpers in `scripts/00_utils` for consistent styling and data loading.
