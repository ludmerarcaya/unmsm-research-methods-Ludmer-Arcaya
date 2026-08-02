# AI Research Ethics Protocol

**Research Title**

Bayesian Artificial Intelligence for Predictive Uncertainty Simulation of Citizen Insecurity Scenarios in Lima Metropolitana, Peru (2027)

**Researcher**

Ludmer Arcaya

**Institution**

Universidad Nacional Mayor de San Marcos (UNMSM)

---

# 1. Purpose & Participants

## Research Purpose

The purpose of this research is to design, develop, and evaluate a Bayesian Artificial Intelligence framework capable of predicting crime events and simulating citizen insecurity scenarios under uncertainty in Lima Metropolitana. The proposed framework aims to support evidence-based decision-making by integrating Bayesian Deep Learning and Generative Artificial Intelligence while promoting transparency, interpretability, and responsible AI practices.

## Participants

This study does not involve direct participation of human subjects.

The research exclusively analyzes secondary datasets published by official Peruvian governmental institutions. Consequently, no interviews, questionnaires, observations, or experiments involving identifiable individuals will be conducted.

---

# 2. Data Collection

The research uses publicly available secondary datasets obtained from official governmental institutions.

Primary data sources include:

- National Survey of Strategic Programs (ENAPRES – INEI)
- National Police Information System (SISPOL)
- Open Government Data Portal (datosabiertos.gob.pe)

The datasets contain aggregated demographic, socioeconomic, geographic, victimization, perception of insecurity, and police incident information.

No personally identifiable information (PII), biometric information, names, identification numbers, addresses, telephone numbers, or other sensitive personal data are processed during this research.

---

# 3. Informed Consent

Because this study exclusively uses secondary public datasets released by authorized governmental institutions, direct informed consent from individual citizens is not required.

The datasets were collected under the legal and institutional procedures established by the Peruvian Government and are publicly available for research purposes.

Although informed consent is not applicable, the study follows the Belmont Principle of Respect for Persons by ensuring that no attempt will be made to identify or re-identify individuals.

---

# 4. Risks

Although individual privacy risks are minimal due to the absence of identifiable personal information, several ethical risks have been identified.

| Risk | Affected Entity | Probability | Impact | Mitigation Strategy |
|-------|----------------|-------------|---------|---------------------|
| Algorithmic bias | Citizens | Medium | High | Fairness evaluation, bias auditing, Bayesian uncertainty estimation |
| Geographic stigmatization | Districts | Medium | Medium | Report aggregated results and uncertainty intervals; avoid deterministic labeling |
| Misinterpretation of predictions | Decision makers | Medium | High | Clearly communicate model limitations and confidence estimates |
| Dual-use of AI | Society | Low | High | Restrict intended use to decision support; require human oversight |

The proposed system is intended exclusively as a decision-support tool and must not replace professional judgment or public policy decisions.

---

# 5. Benefits

## Scientific Benefits

- Development of a novel Bayesian AI framework integrating Bayesian Deep Learning and Generative AI.
- Advancement of uncertainty-aware prediction methods for public security.
- Contribution to reproducible AI research through Git, Docker, DVC, and MLflow.

## Societal Benefits

- Support evidence-based public security planning.
- Improve allocation of police and municipal security resources.
- Enable proactive rather than reactive crime prevention strategies.
- Increase transparency by explicitly communicating predictive uncertainty.

The anticipated scientific and societal benefits outweigh the minimal ethical risks associated with the use of aggregated public datasets.

---

# 6. Confidentiality

The datasets used in this research are publicly available and do not contain personally identifiable information.

Nevertheless, responsible data management practices will be applied by:

- Preserving the original anonymization provided by the data publishers.
- Avoiding any attempt to re-identify individuals.
- Reporting only aggregated statistical results.
- Ensuring that no publication includes information that could indirectly reveal individual identities.

---

# 7. Data Storage & Retention

The research exclusively uses publicly available datasets published by official Peruvian governmental institutions, including INEI, SISPOL, the National Census, and Open Government repositories.

Research datasets, source code, documentation, and trained models will be stored in secure institutional and local repositories to ensure integrity, reproducibility, and version control.

Only source code, documentation, methodological artifacts, and reproducible experiments will be published through GitHub. Public datasets will be referenced using their official repositories rather than redistributed whenever institutional publication policies recommend direct citation of the original source.

Research materials will be retained for five years following thesis completion in accordance with institutional research practices.

---

# 8. Conflict of Interest

The researcher declares no financial, political, or commercial conflict of interest.

This work is conducted exclusively for academic purposes as part of the Doctoral Program at Universidad Nacional Mayor de San Marcos.

No external institution has influenced:

- the research objectives,
- dataset selection,
- methodology,
- experimental results,
- or publication decisions.

---

# AI-Specific Ethical Considerations

## Training Data Provenance

All datasets originate from official governmental institutions:

- National Institute of Statistics and Informatics (INEI)
- National Police Information System (SISPOL)
- National Population Census
- Open Government Data Portal

The provenance of every dataset will be fully documented to ensure transparency and reproducibility.

---

## Fairness and Bias

Historical crime datasets may reflect reporting bias, geographic disparities, socioeconomic inequalities, or institutional policing patterns.

To mitigate these risks, the research incorporates:

- Bayesian uncertainty estimation
- Bias auditing
- Distribution analysis
- Fairness evaluation
- Human interpretation of predictive outputs

---

## Explainability and Transparency

Unlike deterministic AI models, Bayesian Deep Learning provides probability distributions and confidence estimates.

Decision-makers will receive:

- predicted probabilities,
- uncertainty intervals,
- confidence estimates,
- model limitations,

rather than binary predictions.

---

## Human Oversight

The proposed framework is intended solely as a Decision Support System.

Final operational decisions regarding citizen security will always remain under the responsibility of authorized public officials.

No fully automated decisions affecting individuals will be performed.

---

## Dual-Use Risk

The research recognizes that predictive AI systems could potentially be misused for excessive surveillance or discriminatory policing.

To minimize this risk:

- predictions are generated only at aggregated geographic levels,
- no individual profiling is performed,
- uncertainty information accompanies every prediction,
- the framework is intended exclusively for strategic planning and public policy support.

---

# Ethical Principles

This research follows:

- Belmont Report (Respect for Persons, Beneficence, Justice)
- Menlo Report (This report proposes a framework for ethical guidelines for computer and information se- curity research)
- CARE Principles for Responsible Data Governance
- Peru Law No. 29733 (Personal Data Protection)
- Peru Law No. 31814 (Artificial Intelligence Law)
- National Code of Scientific Integrity (CONCYTEC)

---

# Ethical Statement

This research recognizes that Artificial Intelligence applied to citizen security has significant social implications. Accordingly, the proposed Bayesian AI framework has been designed under the principles of transparency, fairness, accountability, privacy protection, uncertainty quantification, and human oversight. The study seeks to maximize public benefit while minimizing potential risks through responsible data governance and ethical AI practices.