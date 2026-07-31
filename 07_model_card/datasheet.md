# Datasheet for Dataset

# Citizen Insecurity Dataset for Metropolitan Lima
### Version 1.0

---

## Dataset Summary

| Item | Description |
|------|-------------|
| Dataset Name | Citizen Insecurity Dataset for Metropolitan Lima |
| Version | 1.0 |
| Author | Ludmer Arcaya |
| Institution | Universidad Nacional Mayor de San Marcos (UNMSM) |
| Doctoral Program | Doctoral Program in Deep Technologies |
| Research Area | Artificial Intelligence, Bayesian Deep Learning, Generative AI |
| License | Academic Research Only |
| Repository | Version controlled with Git + DVC |

---

# 1. Motivation

## Why was this dataset created?

This dataset was developed to support doctoral research focused on designing an Artificial Intelligence framework capable of predicting citizen insecurity events and generating crime scenarios under uncertainty using Bayesian Deep Learning and Generative Artificial Intelligence.

The dataset integrates official public information describing victimization, crime perception, demographic conditions, geographic characteristics, and socioeconomic indicators associated with urban insecurity in Metropolitan Lima.

The research seeks to answer the following research questions:

- How can Bayesian Artificial Intelligence improve crime prediction under uncertainty?
- How can Generative AI simulate future crime scenarios for strategic decision making?
- How can uncertainty estimation improve public security management?

---

## Who created the dataset?

**Researcher**

Ludmer Arcaya

Doctoral Program in Deep Technologies

Universidad Nacional Mayor de San Marcos (UNMSM)

---

## Funding

Academic research.

No commercial funding.

---

## Intended Users

The dataset is intended for:

- Artificial Intelligence researchers
- Bayesian Machine Learning researchers
- Public security researchers
- Urban planning researchers
- Government agencies
- Policy makers
- Data scientists
- Smart city researchers

---

# 2. Dataset Composition

## Primary Data Sources

The dataset integrates publicly available governmental information, including:

- National Institute of Statistics and Informatics (INEI)
- ENAPRES (National Budget Programs Survey)  (https://proyectos.inei.gob.pe/microdatos/)
- National Open Data Portal (https://observatorio.mininter.gob.pe/)


The ENAPRES survey provides nationally representative information regarding victimization, perception of insecurity, confidence in public institutions, crime reporting, prevention measures, demographic characteristics, and household conditions, making it one of the principal sources for the proposed research. :contentReference[oaicite:1]{index=1}



---

## Geographic Coverage

Primary study area:

- Metropolitan Lima

Reference data:

- National ENAPRES survey
- 24 departments
- Constitutional Province of Callao
- Urban and rural coverage

The original ENAPRES survey is nationally representative, while this research extracts and processes observations corresponding to Metropolitan Lima for model development. :contentReference[oaicite:2]{index=2}

---

## Temporal Coverage

Historical observations:

2020–2026

Reference survey:

ENAPRES 2025

Crime historical statistics:

Multiple years (depending on source availability)

---

## Population

Residents of private households located in Metropolitan Lima.

The original ENAPRES survey covers residents of private dwellings and excludes collective residences such as hospitals, prisons, military facilities, hotels, and nursing homes. :contentReference[oaicite:3]{index=3}

---

## Unit of Analysis

Each record represents either:

- an individual,
- a household,
- or an aggregated spatial-temporal observation,

depending on the modeling stage.

---

## Dataset Size

Current version

- n observations
- p predictor variables
- 1 target variable

---

## Target Variable

Example target variables include:

- Crime occurrence probability
- Citizen insecurity level
- Crime category
- Victimization risk
- Simulated future crime scenario

---

# 3. Variables

The dataset combines variables from several domains.

## Demographic Variables

- Age
- Gender
- Education
- Household composition
- Marital status

---

## Geographic Variables

- District
- Geographic coordinates
- Administrative region
- Urban characteristics

---

## Crime Variables

Examples include

- Victimization
- Type of crime
- Crime reporting
- Crime frequency
- Crime location
- Time of occurrence
- Weapon involved
- Number of victimizations

These variables are derived from the ENAPRES Security module. :contentReference[oaicite:4]{index=4}

---

## Citizen Perception Variables

Examples include

- Fear of crime
- Perceived insecurity
- Confidence in police
- Confidence in local authorities
- Community participation
- Security measures adopted
- Activities avoided because of fear

These variables are obtained from the Security Citizen chapter of ENAPRES. :contentReference[oaicite:5]{index=5}

---

## Environmental Variables

Examples

- Public lighting
- Neighborhood infrastructure
- Public services
- Waste management
- Disaster exposure

---

## Socioeconomic Variables

Examples

- Household conditions
- Housing characteristics
- Access to services
- Telecommunications
- Population density

---

# 4. Data Collection Process

## Collection Method

Data were collected from official public institutions through publicly available statistical datasets.

The principal source is the National Budget Programs Survey (ENAPRES), which is conducted annually by the National Institute of Statistics and Informatics (INEI). The survey uses direct household interviews performed by trained personnel following standardized statistical procedures. :contentReference[oaicite:6]{index=6}

---

## Survey Design

According to the ENAPRES technical documentation:

- Probabilistic sampling
- Stratified sampling
- Two-stage sampling
- Independent departmental samples
- Systematic selection
- 95% confidence level

The annual sample consists of approximately 44,000 households distributed nationwide. :contentReference[oaicite:7]{index=7}

---

## Data Quality

Official governmental statistics include

- Quality control
- Enumerator training
- Field supervision
- Consistency validation
- Statistical inference

---

# 5. Preprocessing

The following preprocessing pipeline was applied.

## Data Cleaning

- Missing value treatment
- Duplicate removal
- Invalid record removal
- Date normalization
- Variable harmonization

---

## Feature Engineering

Examples include

- Crime rate per district
- Historical moving averages
- Time-of-day encoding
- Weekday encoding
- Population-adjusted crime rates
- Spatial neighborhood statistics
- Bayesian prior variables
- Lag features
- Seasonal indicators

---

## Encoding

Categorical variables were encoded using:

- One-hot encoding
- Label encoding

depending on model requirements.

---

## Data Validation

Validation procedures include

- Range validation
- Logical consistency
- Missingness analysis
- Outlier detection

---

# 6. Biases and Limitations

Potential limitations include:

- Underreporting of crimes
- Survey response bias
- Delayed crime reporting
- Missing observations
- Geographic aggregation effects
- Changes in crime reporting policies over time

The dataset should therefore be interpreted as an approximation of citizen insecurity rather than an exhaustive representation of all criminal events.

---

# 7. Ethical Considerations

This dataset does not include personally identifiable information.

The research complies with:

- Responsible AI principles
- Research ethics
- Data minimization
- Privacy preservation
- FAIR principles
- Reproducible science practices

---

# 8. Intended Uses

The dataset is intended for

- Bayesian Deep Learning
- Crime prediction
- Risk estimation
- Spatial analysis
- Crime hotspot detection
- Uncertainty estimation
- Scenario simulation
- Public policy analysis
- Decision-support systems

---

# 9. Out-of-Scope Uses

The dataset must **NOT** be used for

- Individual profiling
- Predictive policing targeting specific citizens
- Automated legal decisions
- Social scoring
- Discriminatory decision making
- Surveillance of identifiable individuals

---

# 10. Storage and Distribution

Repository structure

```
data/
raw/
processed/
external/
interim/
```

Version control

- Git
- DVC

Model artifacts

- MLflow

---

# 11. Reproducibility

The complete pipeline is reproducible using

- Python
- Docker
- Git
- DVC
- MLflow

Every dataset version is traceable through Git commits and DVC hashes.

---

# 12. Maintenance

Maintainer

Ludmer Arcaya

Universidad Nacional Mayor de San Marcos

---

## Update Frequency

Annual

or whenever new official crime statistics become available.

---
