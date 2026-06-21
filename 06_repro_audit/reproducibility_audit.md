# Reproducibility Audit — Scorecard

## Paper Information

**Paper Title:** Customer Churn Prediction Model using Explainable Machine Learning

**Authors / Year:**
Head - AI and Cognitive Experience, Tata Consultancy Services Ltd. (India)
DWH/BI Developer, Amdocs (India)
**Year:** 2023

**Venue:**
*International Journal of Computer Science Trends and Technology (IJCST)* – Volume 11, Issue 1, Jan–Feb 2023

**Dataset(s) Used:**
Dataset taken from the telecommunications industry to analyze customer churn rate.

---

## Reproducibility Checklist

| Checklist Item                           | What to Look For                                   | Score (Y / P / N) | Notes / Evidence                            |
| ---------------------------------------- | -------------------------------------------------- | ----------------- | ------------------------------------------- |
| Random seeds reported?                   | Stated and set for all libraries                   | **N**             | Not reported.                               |
| Data splits described?                   | Train/validation/test sizes and splitting strategy | **P**             | Only train and test split (70/30) reported. |
| Multiple runs?                           | Mean ± standard deviation, not a single number     | **N**             | Not reported.                               |
| Statistical test used?                   | Named test appropriate to the data                 | **N**             | Not reported.                               |
| Effect size / Confidence Interval shown? | Not just a p-value                                 | **N**             | Not reported.                               |
| Compute documented?                      | Hardware and runtime information                   | **N**             | Not reported.                               |
| Code & data available?                   | A stranger could re-run it                         | **N**             | Dataset and source code unavailable.        |

---

## Overall Reproducibility Score

**Scoring:** Yes = 1 · Partial = 0.5 · No = 0

**Score:** 0.5 / 7 (**7.1%**)

**Rating:** 🔴 Low

### Justification

This paper is not reproducible because neither the dataset nor the source code is publicly available. In addition, several critical elements required for reproducibility—such as random seeds, statistical testing, confidence intervals, and computational details—are not reported. The authors should improve transparency and reporting practices to increase confidence in the results.

---

## Top 3 Fixes That Would Most Improve Reproducibility

1. Public links to the dataset and source code should be provided.
2. Statistical tests and confidence intervals should be explicitly reported.
3. Computational environment details (CPU, GPU, runtime, and hardware specifications) should be documented.

---

# Reproducibility Audit — Scorecard

## Paper Information

**Paper Title:** Revisiting Deep Learning Models for Tabular Data

**Authors / Year:**
Yury Gorishniy, Ivan Rubachev, Valentin Khrulkov, Artem Babenko

**Year:** 2023

**Venue:**
*arXiv:2106.11959v5*

**Dataset(s) Used:**

* California Housing (CA) – Real estate data (Kelley & Pace, 1997)
* Adult (AD) – Income estimation (Kohavi, 1996)
* Helena (HE) – Anonymized dataset (Guyon et al., 2019)

---

## Reproducibility Checklist

| Checklist Item                           | What to Look For                                   | Score (Y / P / N) | Notes / Evidence                                                      |
| ---------------------------------------- | -------------------------------------------------- | ----------------- | --------------------------------------------------------------------- |
| Random seeds reported?                   | Stated and set for all libraries                   | **N**             | Not explicitly reported.                                              |
| Data splits described?                   | Train/validation/test sizes and splitting strategy | **Y**             | Dataset split sizes are documented.                                   |
| Multiple runs?                           | Mean ± standard deviation, not a single number     | **Y**             | Metrics are averaged over 15 random seeds.                            |
| Statistical test used?                   | Named test appropriate to the data                 | **Y**             | One-sided Wilcoxon test (p = 0.01) reported.                          |
| Effect size / Confidence Interval shown? | Not just a p-value                                 | **Y**             | Mean and standard deviation values reported (Table 8, page 15).       |
| Compute documented?                      | Hardware and runtime information                   | **P**             | NVIDIA Tesla V100 32GB reported, but runtime and CPU details omitted. |
| Code & data available?                   | A stranger could re-run it                         | **Y**             | Public source code available on GitHub.                               |

---

## Overall Reproducibility Score

**Scoring:** Yes = 1 · Partial = 0.5 · No = 0

**Score:** 5.5 / 7 (**78.6%**)

**Rating:** 🟢 High

### Justification

This paper is largely reproducible because the authors provide detailed experimental procedures, public source code, multiple-run evaluations, and statistical significance testing. However, exact replication may still be challenging because random seeds, runtime information, and direct dataset links are not fully documented.

---

## Top 3 Fixes That Would Most Improve Reproducibility

1. Public dataset links should be explicitly provided in the paper.
2. Confidence intervals should be reported using established statistical methods (e.g., t-distribution or z-distribution intervals).
3. Complete computational environment details, including CPU specifications, GPU configuration, and runtime measurements, should be documented.
