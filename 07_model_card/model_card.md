# Model Card

## Model Name

Bayesian Artificial Intelligence Model for Citizen Insecurity Prediction

---

# 1. Model Details

## Model Type

Bayesian Machine Learning Model

Examples:

- Bayesian Network
- Bayesian Logistic Regression
- Bayesian Hierarchical Model

## Version

v1.0

## Author

Ludmer Arcaya

Doctoral Program in Deep Technologies – UNMSM

## Date

2026

---

# 2. Intended Use

## Primary Intended Uses

The model is designed to:

- Estimate crime risk probabilities
- Support public security planning
- Assist decision-making under uncertainty
- Analyze citizen insecurity scenarios

## Intended Users

- Researchers
- Policymakers
- Public security analysts

## Out-of-Scope Uses

The model should NOT be used for:

- Individual-level risk assessments
- Automated legal decisions
- Predictive policing targeting individuals

---

# 3. Factors

The model performance may vary according to:

- Geographic region
- Crime category
- Data availability
- Temporal period
- Reporting quality

Relevant contextual variables include:

- Population density
- Historical crime rates
- Socioeconomic indicators
- Urban characteristics

---

# 4. Metrics

The following metrics are used:

## Classification Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

## Probabilistic Metrics

- Log Loss
- Brier Score
- Calibration Error

## Bayesian Metrics

- Posterior Probability Estimates
- Credible Intervals

---

# 5. Evaluation Data

## Evaluation Dataset

The evaluation dataset consists of holdout observations not used during training.

## Split Strategy

Example:

- Training: 70%
- Validation: 15%
- Test: 15%

## Evaluation Period

[Specify evaluation dates]

---

# 6. Training Data

## Training Dataset

Citizen Insecurity Dataset for Lima Metropolitana

## Data Sources

- National Police reports
- INEI datasets
- Public security reports

## Preprocessing

Training data underwent:

- Missing value treatment
- Feature engineering
- Standardization
- Data quality validation

---

# 7. Quantitative Analyses

## Overall Performance

| Metric | Value |
|----------|----------|
| Accuracy | TBD |
| Precision | TBD |
| Recall | TBD |
| F1 Score | TBD |
| ROC AUC | TBD |

## Calibration Analysis

Evaluate whether predicted probabilities correspond to observed frequencies.

## Uncertainty Analysis

Bayesian posterior distributions are analyzed to quantify uncertainty in predictions.

---

# 8. Ethical Considerations

## Potential Risks

- Reinforcement of historical biases
- Misinterpretation of risk estimates
- Unequal impact across districts

## Mitigation Strategies

- Bias auditing
- Fairness evaluation
- Transparency reporting
- Human oversight

## Privacy

The model uses aggregated and anonymized data whenever possible.

---

# 9. Caveats and Recommendations

## Limitations

- Data quality depends on reporting systems.
- Historical biases may be reflected in training data.
- Predictions are probabilistic, not deterministic.

## Recommendations

- Use predictions as decision-support information only.
- Combine model outputs with expert judgment.
- Periodically retrain and audit the model.
- Monitor performance and fairness over time.

## Future Improvements

- Incorporate citizen perception indicators.
- Improve uncertainty communication.
- Expand geographic coverage.
- Evaluate additional Bayesian approaches.