# Data Management Plan (DMP)

**Research Title**

Bayesian Artificial Intelligence for Predictive Uncertainty Simulation of Citizen Insecurity Scenarios in Lima Metropolitana, Peru (2027)

**Researcher**

Ludmer Arcaya

**Institution**

Universidad Nacional Mayor de San Marcos (UNMSM)

---

# 1. Data Description

## Data Sources

This research exclusively uses secondary datasets obtained from official public institutions in Peru.

The primary data sources include:

- National Survey of Strategic Programs (ENAPRES – INEI)
- National Population and Housing Census (INEI)
- National Police Information System (SISPOL)
- Open Government Data Portal (datosabiertos.gob.pe)

These datasets provide information regarding:

- Crime incidents
- Citizen perception of insecurity
- Victimization
- Demographic indicators
- Socioeconomic indicators
- Geographic information
- Police statistics

## Data Types

The project will generate and manage the following research assets:

- Tabular datasets (CSV, XLSX, Parquet)
- Geospatial datasets (Shapefile, GeoJSON)
- Data dictionaries
- Python source code
- Jupyter notebooks
- Trained Bayesian AI models
- MLflow experiment logs
- Research documentation
- Figures and evaluation reports

## Estimated Volume

Approximately 2–10 GB of processed research data, depending on the integration of official datasets and experimental outputs.

---

# 2. FAIR Compliance

The research follows the FAIR Data Principles to maximize reproducibility and long-term usability.

## Findable

- Complete metadata will accompany every research artifact.
- Final research outputs will be deposited in Zenodo to obtain a DOI.
- GitHub will maintain version-controlled source code.

## Accessible

Source code, documentation, notebooks, and reproducible workflows will be publicly available through GitHub.

Official datasets will not be redistributed when institutional policies recommend referencing the original repository. Instead, links to the original governmental sources will be provided.

## Interoperable

Open and standardized formats will be used throughout the project.

Examples include:

- CSV
- JSON
- GeoJSON
- Parquet
- Markdown
- Python

Metadata and variable definitions will be documented using a comprehensive data dictionary.

## Reusable

The repository will include:

- README documentation
- Data Dictionary
- Methodological documentation
- Docker environment
- DVC pipeline
- MLflow experiment tracking

Source code will be released under an open-source license to facilitate reproducibility.

---

# 3. Anonymization Strategy

The study exclusively uses publicly available datasets that have already been anonymized by the corresponding governmental institutions.

No personally identifiable information (PII) is collected or processed.

No attempt will be made to re-identify individuals.

Because the research analyzes aggregated public statistics, additional anonymization techniques such as k-anonymity or differential privacy are not required for the primary datasets.

Only aggregated prediction results, district-level analyses, uncertainty estimates, and simulation outputs will be reported.

---

# 4. Storage & Backup

Research materials will be stored following the 3-2-1 backup strategy.

## Primary Storage

- Local encrypted workstation
- UNMSM research storage
- GitHub repository (source code only)

## Secondary Backup

- External encrypted hard drive

## Third Backup

- Secure institutional cloud storage

## Security Measures

- Version control using Git
- Docker containers for reproducibility
- DVC for dataset versioning
- MLflow for experiment tracking
- Restricted write permissions on research directories

Only the researcher will have write access during the doctoral project.

---

# 5. Legal Compliance

This research complies with the legal framework governing responsible data management in Peru.

Applicable regulations include:

- Peru Law No. 29733 – Personal Data Protection Law
- Supreme Decree No. 016-2024-JUS
- Peru Artificial Intelligence Law No. 31814
- FAIR Guiding Principles
- CARE Principles (where applicable)

Because the datasets are:

- Public,
- Aggregated,
- Anonymous,
- Government-published,

the study does not require informed consent from individual citizens.

GDPR is not applicable because no personal information from European Union residents is processed.

No international transfer of sensitive personal data will occur.

---

# 6. Sharing Plan

The project follows Open Science principles while respecting institutional data policies.

The following artifacts will be publicly shared:

- Source code
- Python scripts
- Jupyter notebooks
- Docker environment
- DVC pipeline
- MLflow experiment metadata
- Documentation
- Data dictionary
- Research reports

Repositories:

- GitHub
- Zenodo (DOI publication)

Public governmental datasets will be referenced through their official repositories rather than redistributed whenever institutional publication policies recommend direct citation of the original source.

Research outputs will be released after thesis publication.

---

# 7. Retention Period

Research materials will be retained for five years after successful thesis defense.

The following assets will be preserved:

- Source code
- Documentation
- Models
- Experiment logs
- Data dictionaries
- Reproducibility artifacts

Public datasets will remain available through their official governmental repositories.

After the retention period:

- Temporary intermediate files will be permanently deleted.
- Local backups will be securely removed.
- The GitHub repository and Zenodo archive will remain available to preserve scientific reproducibility.

---

# Research Software

The research software stack includes:

- Python
- Scikit-learn
- PyTorch
- TensorFlow
- PyMC
- MLflow
- Docker
- DVC
- Git
- JupyterLab
- PostgreSQL/PostGIS (if spatial database is required)

---

# Data Versioning Strategy

Version control will be implemented using:

- Git for source code
- DVC for datasets
- MLflow for experiments
- Semantic versioning for releases

Each experiment will record:

- Dataset version
- Model parameters
- Hyperparameters
- Evaluation metrics
- Random seed
- Model artifacts

---

# Data Quality Assurance

Data quality will be monitored through:

- Missing value analysis
- Duplicate detection
- Consistency validation
- Variable range validation
- Geographic consistency checks
- Feature engineering validation
- Reproducible preprocessing pipelines

---

# Reproducibility Statement

All computational experiments will be fully reproducible using:

- Docker
- Git
- DVC
- MLflow
- Jupyter Notebooks

The repository will contain sufficient documentation for independent researchers to reproduce the complete experimental workflow.

---

# Data Lifecycle Summary

| Phase | Description |
|---------|-------------|
| Collection | Download public datasets from official government repositories |
| Processing | Data cleaning, integration, transformation, and feature engineering |
| Analysis | Bayesian Deep Learning training and Generative AI simulations |
| Storage | Local encrypted storage, institutional repository, GitHub, DVC |
| Sharing | GitHub (code) and Zenodo (research outputs) |
| Preservation | Five-year retention period |
| Disposal | Secure deletion of temporary research files after retention period |

---

# FAIR Compliance Checklist

| Principle | Implementation |
|------------|----------------|
| Findable | Zenodo DOI, metadata, GitHub repository |
| Accessible | Public documentation and code |
| Interoperable | CSV, JSON, Parquet, GeoJSON, Markdown |
| Reusable | README, codebook, Docker, DVC, MLflow |

---

# Data Management Statement

This research follows international best practices for responsible data management by integrating FAIR principles, reproducible research workflows, open science practices, and secure data governance. Because the study exclusively analyzes publicly available and anonymized governmental datasets, ethical and privacy risks are minimal. The combination of Git, Docker, DVC, and MLflow ensures complete traceability and reproducibility throughout the doctoral research lifecycle.