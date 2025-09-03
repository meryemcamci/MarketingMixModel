# 📊 Marketing Mix Modeling (MMM) Project with Google Meridian (End-to-End Pipeline)

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

🔎 **Overview**

This project implements an end-to-end Marketing Mix Modeling (MMM) workflow using Python. The goal was to measure channel effectiveness, evaluate model performance, and optimize budget allocation across different media channels.

⚙️ **Steps**

**Synthetic Data Generation**

* Created a realistic marketing dataset including TV, search, social, and display spend.

* Added external control factors (e.g., price index, promotions, holidays).

**Data Preprocessing**

* Cleaned and structured the dataset.

* Ensured correct handling of time series and prepared data for modeling.

**Baseline & Regularized Models**

* Built a baseline linear regression model.

* Implemented a regularized MMM with Ridge regression, including adstock (lagged effects) and saturation (diminishing returns).

**Model Evaluation**

* Compared baseline vs. regularized models using R², MAPE, and RMSE.

* Analyzed residuals and contribution by channel.

* Found that TV spend contributed the most positively, while display spend showed weak/negative returns.

**Budget Optimization**

* Ran what-if scenarios: same budget, +10% increase, −20% decrease.

* Recommended reallocating spend toward search and social for efficiency.

* Demonstrated how MMM insights can guide strategic budget planning.

📌 **Key Insights**

* MMM captures carryover effects (adstock) and diminishing returns (saturation).

* Regularized MMM gives more robust and interpretable results compared to a simple linear baseline.

* Data-driven budget optimization shows how to maximize ROI under different spending constraints.

🚀 **Skills Demonstrated**

* Python (pandas, sklearn, scipy, matplotlib)

* Time-series feature engineering (adstock, saturation)

* Model evaluation (MAPE, RMSE, residual analysis)

* Optimization & scenario analysis for budget planning

* Clear storytelling through data visualization and interpretation

👉 This project shows how MMM can be applied in practice to support marketing strategy, ROI measurement, and budget optimization.
