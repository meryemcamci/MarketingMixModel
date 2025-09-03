# Marketing Mix Model with Google Meridian

This repo is a structured starter for running a Bayesian MMM using **Google Meridian**,
with a baseline regression for comparison and simple budget optimization experiments.

## Structure
```
MarketingMixModel_Meridian/
├── data/
│   └── marketing_data.csv        # put your dataset here
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_baseline_regression.ipynb
│   ├── 03_meridian_model.ipynb
│   ├── 04_model_evaluation.ipynb
│   └── 05_budget_optimization.ipynb
├── reports/
│   └── (generated outputs: html/pdf/images)
├── src/
│   └── utils.py
├── environment.yml
└── requirements.txt
```

## Quickstart (conda)
```bash
# 1) Create & activate env (Apple Silicon friendly)
conda env create -f environment.yml
conda activate mmm-meridian

# 2) Register Jupyter kernel
python -m ipykernel install --user --name mmm-meridian --display-name "Python (mmm-meridian)"

# 3) Launch Jupyter
jupyter lab
```

## Quickstart (venv + pip)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name mmm-meridian --display-name "Python (mmm-meridian)"
jupyter lab
```

## Data Columns (minimal example)
- date (YYYY-MM-DD weekly or daily, no gaps)
- revenue (KPI; or replace with your KPI and set revenue_per_kpi accordingly in notebook)
- tv_spend, search_spend, social_spend, display_spend
- price_index (numeric), promo (0/1), holiday (0/1)

> Put your CSV at `data/marketing_data.csv` before running the notebooks.
