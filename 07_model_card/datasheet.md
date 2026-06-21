# Datasheet for Dataset

## Dataset Title

Citizen Insecurity Dataset for Lima Metropolitana

---

# 1. Motivation

## Why was this dataset created?

This dataset was created to support research on Bayesian Artificial Intelligence models for decision-making under uncertainty in citizen insecurity scenarios in Lima Metropolitana.

The primary objective is to identify spatial, temporal, and contextual patterns associated with crime incidents and citizen perceptions of insecurity, enabling the development of predictive and decision-support systems for public security management.

## Who created the dataset?

The dataset was assembled by Ludmer Arcaya as part of the Doctoral Program in Deep Technologies at Universidad Nacional Mayor de San Marcos (UNMSM).

## Intended users

- Researchers in Artificial Intelligence
- Public policy analysts
- Security agencies
- Data scientists
- Urban planning researchers

---

# 2. Composition

## What does the dataset contain?

The dataset contains records related to citizen insecurity events, including:

- Date and time of incident
- Geographic location
- District information
- Crime category
- Environmental context
- Socioeconomic indicators
- Historical crime statistics
- Public security indicators

## Number of instances


-  incident records

## Number of features



- n predictor variables
- 1 target variable

## Target Variable

Example:

- Crime occurrence probability
- Crime severity category
- Citizen insecurity level

---

# 3. Collection Process

## How was the data collected?

Data was obtained from publicly available sources including:

- National Police reports
- National Institute of Statistics (INEI)
- Open Government Data Portals
- Municipal public security reports

## Collection period


 2024 –  2026

## Sampling strategy

Historical records were collected and aggregated at district and temporal levels.

## Data acquisition limitations

- Missing records in some districts
- Reporting delays
- Potential underreporting of incidents

---

# 4. Preprocessing

## Cleaning Procedures

The following preprocessing steps were applied:

- Missing value treatment
- Duplicate removal
- Date standardization
- Geographical normalization
- Outlier analysis

## Feature Engineering

Examples:

- Crime frequency per district
- Rolling historical averages
- Population-adjusted crime rates
- Temporal seasonality indicators

## Data Quality Validation

Validation checks included:

- Consistency verification
- Range validation
- Missing data assessment

---

# 5. Uses

## Intended Uses

The dataset is intended for:

- Bayesian modeling
- Risk estimation
- Predictive analytics
- Decision-support systems
- Public security research

## Out-of-Scope Uses

The dataset should NOT be used for:

- Individual profiling
- Law enforcement actions against specific persons
- Automated judicial decisions
- Surveillance targeting

---

# 6. Distribution

## Access Method

The dataset is managed through DVC and version-controlled alongside the project repository.

## Storage

Data files are stored in:

```text
data/
```

Versioned through:

```bash
dvc add
dvc push
```

## License

Research and academic use only.

## Restrictions

Users must comply with applicable privacy regulations and ethical guidelines.

---

# 7. Maintenance

## Maintainer

Ludmer Arcaya

Doctoral Program in Deep Technologies – UNMSM

## Update Frequency

As new public security data becomes available.

## Versioning Strategy

Dataset versions are managed using:

- Git
- DVC

## Contact

[Add institutional email]