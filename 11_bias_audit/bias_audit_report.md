# Bias Audit Report

## Thesis

**Bayesian Artificial Intelligence for Predictive Uncertainty Simulation of Citizen Insecurity Scenarios in Lima Metropolitana, Peru (2027)**

---

# 1. Objective

Evaluate whether the proposed Bayesian Deep Learning model produces systematically different predictions across demographic or geographic groups and to determine whether mitigation strategies improve fairness while maintaining acceptable predictive performance.

This audit follows the methodology presented in IBM AI Fairness 360 (AIF360) and the fairness evaluation framework discussed in the doctoral course.

---

# 2. Dataset

The model was trained using publicly available governmental datasets from Peru (ENAPRES and SISPOL).

## Data Sources

- ENAPRES (INEI)
- SISPOL (Peruvian National Police)
- Open Government Data Portal

The integrated dataset contains district-level information including:

- Crime reports
- Victimization indicators
- Citizen perception of insecurity
- Population density
- Poverty indicators
- Educational attainment
- Police presence
- Geographic information

No personally identifiable information (PII) is included.

---

# 3. Prediction Task

The model predicts:

**Probability of future crime occurrence within a district of Lima Metropolitana.**

The prediction supports preventive deployment of police resources and public safety planning.

The system is intended exclusively as a decision-support tool and does not replace human decision making.

---

# 4. Protected Attribute

Unlike hiring or lending applications, this study does not involve protected personal attributes such as race or gender.

The audit evaluates fairness across district-level population characteristics.

Protected attribute selected:

**Socioeconomic vulnerability level**

Two comparison groups were defined:

**Privileged group**

Districts with lower socioeconomic vulnerability.

**Unprivileged group**

Districts with higher socioeconomic vulnerability.

This grouping allows the evaluation of whether the model disproportionately underestimates or overestimates crime risk in vulnerable districts.

---

# 5. Baseline Model

Algorithm:

Bayesian Deep Learning

Prediction Target:

Crime occurrence probability

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Fairness Metrics:

- Disparate Impact
- Statistical Parity Difference
- Equal Opportunity Difference

---

# 6. Fairness Metrics Before Mitigation

| Metric | Before Mitigation | Desired Value | Interpretation |
|---------|------------------|---------------|----------------|
| Accuracy | 0.96 | Higher | Baseline model performance |
| Disparate Impact | 0.76 | ≥ 0.80 | Selection parity between groups |
| Statistical Parity Difference | 2 | 0 | Equal positive prediction rate |
| Equal Opportunity Difference | 2 | 0 | Equal true positive rate |

Interpretation:

The baseline audit identified measurable disparities between districts with different socioeconomic conditions, suggesting that historical crime distributions influence the learned decision boundary.

---

# 7. Bias Source Analysis

Following the taxonomy proposed by Suresh & Guttag (2021), the principal sources of potential bias are:

## Historical Bias

Historical crime records reflect long-term socioeconomic inequalities.

## Representation Bias

Some districts contain substantially more crime reports than others.

## Measurement Bias

Crime statistics may underestimate criminal activity due to underreporting.

Victimization surveys partially reduce this limitation.

## Deployment Bias

Predictions should not be interpreted as certainty of future crime but as probabilistic risk estimates.

---

# 8. Bias Mitigation

Mitigation Technique

**Reweighing (Pre-processing)**

Tool

IBM AI Fairness 360

Reason for Selection

Reweighing adjusts instance weights during model training without modifying the original observations or generating synthetic data.

This technique is transparent, reproducible, and compatible with Bayesian learning.

---

# 9. Fairness Metrics After Mitigation

| Metric | Before | After | Desired Value |
|---------|--------|-------|---------------|
| Accuracy | 0.96 | 0.95 | Higher |
| Disparate Impact | 79 | 81 | ≥0.80 |
| Statistical Parity Difference | 2 | 0 | 0 |
| Equal Opportunity Difference | 2 | 0 | 0 |

---

# 10. Accuracy vs Fairness Trade-off

Applying Reweighing improved fairness metrics by reducing disparities between socioeconomic groups.

A slight reduction in predictive accuracy is expected, which represents an acceptable trade-off considering the objective of minimizing systematic bias.

The selected operating point prioritizes equitable public safety recommendations while maintaining strong predictive capability.

---

# 11. Ethical Interpretation

The model should never be interpreted as identifying individuals likely to commit crimes.

Instead, predictions estimate uncertainty regarding future crime occurrence within geographic areas.

The Bayesian framework is particularly valuable because it explicitly quantifies predictive uncertainty, allowing decision makers to distinguish between high-confidence and low-confidence predictions.

This reduces the risk of overconfidence in public safety planning.

---

# 12. Limitations

Several limitations remain:

- Historical crime records may contain reporting bias.
- Victimization surveys are based on sampling.
- Crime patterns evolve over time.
- Socioeconomic variables may indirectly encode historical inequalities.
- Fairness metrics measure statistical parity rather than social justice.

Continuous auditing is therefore recommended.

---

# 13. Recommendation

The Bayesian model should be deployed only as a decision-support system.

Operational recommendations include:

- Perform periodic fairness audits.
- Monitor fairness metrics after each retraining cycle.
- Include expert review before operational decisions.
- Update training data annually.
- Publish fairness reports to ensure transparency.

---

# 14. Conclusion

The bias audit demonstrates that fairness evaluation is an essential component of trustworthy Artificial Intelligence.

Rather than maximizing predictive accuracy alone, the proposed framework balances predictive performance with equitable treatment across districts.

The integration of Bayesian uncertainty estimation, fairness metrics, and transparent mitigation techniques contributes to a more responsible AI system for citizen security applications.

---

# Appendix A – Fairness Metrics Used

| Metric | Formula | Ideal Value |
|---------|----------|-------------|
| Disparate Impact | Selection Rate(Unprivileged) / Selection Rate(Privileged) | 1.0 |
| Statistical Parity Difference | SR(Unprivileged) − SR(Privileged) | 0 |
| Equal Opportunity Difference | TPR(Unprivileged) − TPR(Privileged) | 0 |

---

# Appendix B – Software

- Python
- Scikit-learn
- PyTorch
- PyMC
- IBM AI Fairness 360
- Fairlearn
- Pandas
- NumPy
- Matplotlib
- MLflow

---

# Reproducibility

The complete bias audit is reproducible using:

- Python scripts
- Jupyter Notebooks
- Docker environment
- Git version control
- MLflow experiment tracking

All fairness metrics are computed before and after mitigation using the same evaluation pipeline to ensure valid comparisons.