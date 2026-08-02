# Calibration Review — Student Handout

**Research Methods & Scientific Integrity in AI · UNMSM Doctoral Program**  
**Individual Review **

---

# What to do

Read the methodology excerpt below once, at reviewing speed. Then, in the shared Google Sheet, score all five rubric criteria from 1 (unacceptable) to 5 (excellent) — one row for you — and write a one-line justification for each score. Do not discuss with anyone yet; the spread across the class is the whole point.
Every comment you make must quote or cite the exact line it refers to. Line numbers are provided for that purpose.


---

# The Five-Criterion Rubric

| Criterion | Weight | The question it asks |
|-----------|--------|---------------------|
| Scientific Rigor | 25% | Would this methodology adequately answer the research question? |
| Ethical Compliance | 20% | Who could be harmed, and is that addressed?? |
| Reproducibility Plan | 20% | Could a stranger repeat this? |
| Clarity of Writing | 20% | Can I evaluate it without guessing? |
| Feasibility | 15% | Can one person do this in the available time? |

---

# Methodology Excerpt (Anonymized)

# Methodology Excerpt (Anonymized)

**L1** This study proposes a Bayesian Artificial Intelligence framework integrating Bayesian Deep Learning and Generative Artificial Intelligence to predict citizen insecurity events and simulate future crime scenarios in Lima Metropolitana, Peru.

**L2** The research follows a Design Science Research (DSR) methodology consisting of six iterative phases: problem identification, objective definition, artifact design, model development, evaluation, and communication of results.

**L3** Secondary data were obtained from publicly available governmental sources, including the National Survey of Strategic Programs (ENAPRES), the National Police Information System (SISPOL), the National Population and Housing Census (INEI), and the Peruvian Open Government Data Portal.

**L4** The integrated dataset contains district-level information on crime incidents, victimization rates, citizen perception of insecurity, demographic characteristics, poverty indicators, educational attainment, police presence, population density, and geospatial variables. The datasets are anonymized and do not contain personally identifiable information.

**L5** Data preprocessing includes missing-value treatment, duplicate removal, feature engineering, categorical encoding, normalization, and integration of spatial variables. The final dataset is divided into training (70%), validation (15%), and testing (15%) subsets using stratified sampling.

**L6** Bayesian Deep Learning is employed to estimate both crime occurrence probabilities and predictive uncertainty. Generative Artificial Intelligence is used to simulate alternative crime scenarios under different public security intervention strategies.

**L7** Model performance will be evaluated using Accuracy, Precision, Recall, F1-score, ROC-AUC, Brier Score, calibration curves, and uncertainty calibration metrics. Fairness will be assessed using Disparate Impact, Statistical Parity Difference, and Equal Opportunity Difference across districts with different socioeconomic vulnerability levels.

**L8** The study exclusively uses publicly available datasets published by official governmental institutions. Since no personally identifiable information is processed and no human participants are recruited, informed consent is not required. The research complies with Peru's Personal Data Protection Law (Law No. 29733) and the Artificial Intelligence Promotion Law (Law No. 31814).

**L9** The complete computational workflow will be implemented in Python using PyTorch, PyMC, Scikit-learn, and MLflow. Source code, Docker containers, DVC pipelines, and experiment tracking metadata will be published through GitHub to ensure computational reproducibility. Official datasets will be referenced through their original repositories rather than redistributed.

**L10** The proposed framework is intended exclusively as a decision-support system for public institutions. Human experts will remain responsible for interpreting predictions and making operational decisions. The system is not intended to automate policing decisions or identify individuals.

**L11** The experimental evaluation will compare the proposed Bayesian framework with conventional Deep Learning and Random Forest models using identical datasets and evaluation protocols. Statistical significance will be assessed using paired hypothesis tests.

**L12** The research is expected to improve predictive performance, quantify uncertainty, reduce algorithmic bias through fairness-aware evaluation, and provide interpretable scenario simulations that support evidence-based public security planning in Lima Metropolitana.

---

# Your Scoring Sheet

| Criterion | Score (1–5) | One-line justification (quote the line) |
|-----------|-------------|------------------------------------------|
| Scientific Rigor |  |  |
| Ethical Compliance |  | |
| Reproducibility Plan |  |  |
| Clarity of Writing |  |  |
| Feasibility |  | |

---

Then, separately, list:
- Issues Considered Fatal (Cannot be fixed by simple rewriting; would require redesign.)*
- The issue you consider fixable (repairable by adding detail or rewriting)
- One genuine strength of the excerpt.

---
