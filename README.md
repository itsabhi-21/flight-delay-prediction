# Flight Delay Prediction — EDA & Baseline Models

Binary classification project predicting whether a US domestic flight will 
arrive delayed (>15 minutes), using only information known before departure.

## Problem
Airlines and passengers both benefit from early delay prediction. This project 
frames delay prediction as a binary classification task: will a flight's 
arrival delay exceed 15 minutes — the US DOT's official on-time threshold?

## Data
[Airline Delay and Cancellation Data, 2009–2018](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018) 
(Kaggle) — 2018 subset, sampled to 20,000 flights for this project's scope.

Columns known only *after* a flight occurs (actual departure/arrival times, 
taxi times, delay-cause breakdowns) were excluded to avoid data leakage — 
only pre-departure information is used.

## Approach
1. **Data cleaning** — leakage-aware column selection, null handling
2. **EDA** — delay distribution, delay rate by hour/airline
3. **Feature engineering** — date-based features (day of week, month), 
   top-N categorical encoding for carrier/origin/destination
4. **Modeling** — Logistic Regression (interpretable baseline) vs 
   Random Forest (captures non-linear patterns)
5. **Explainability** — Random Forest feature importance

## Results

| Model | Precision (delayed) | Recall (delayed) | Accuracy |
|---|---|---|---|
| Logistic Regression | 0.25 | 0.59 | 0.59 |
| Random Forest | 0.26 | 0.57 | 0.62 |

Random Forest's marginal improvement over Logistic Regression suggests the 
relationship between features and delay is largely linear — favoring the 
simpler, more interpretable model for this use case.

**Top predictor:** Scheduled departure hour — evening flights show 
meaningfully higher delay rates than morning flights.

## Limitations & Future Work
- No weather data — typically the single biggest real-world delay driver
- Real-time features (upstream aircraft status, air traffic congestion) 
  would likely improve recall
- With more time: hyperparameter tuning (GridSearchCV), gradient boosting 
  models (XGBoost/LightGBM)

## Tech Stack
Python, pandas, scikit-learn, matplotlib, seaborn

## Notebook
See [`Flight_Delay_Prediction.ipynb`](./Flight_Delay_Prediction.ipynb) for 
full analysis with EDA visualizations and step-by-step reasoning.
