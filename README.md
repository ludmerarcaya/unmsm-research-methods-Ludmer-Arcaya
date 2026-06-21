# UNMSM Research Methods – Ludmer Arcaya

## Overview

This repository contains the complete implementation of the capstone project developed for the course **Research Methods & Scientific Integrity in Artificial Intelligence** within the **UNMSM Doctoral Program in Deep Technologies**.

The objective of this project is to demonstrate the application of rigorous scientific research practices in Artificial Intelligence through a fully reproducible study. The repository integrates the complete research lifecycle, including paradigm selection, methodology design, protocol development, literature review, ethical assessment, data management, bias auditing, reproducible machine learning experimentation, and reflective analysis.

The project follows the principles of:

* Scientific rigor
* Reproducibility and replicability
* Research integrity
* Ethical AI development
* Transparent documentation

---

## Research Question


> How can Bayesian Artificial Intelligence models improve decision-making under uncertainty in citizen insecurity scenarios in Lima Metropolitana?

---

## Repository Structure

This repository is organized according to the course deliverables:

* **01_paradigm/** – Research paradigm justification
* **02_method/** – Method-fit matrix and methodology selection
* **03_protocol/** – Research protocol versions
* **04_literature/** – Systematic literature review and PRISMA analysis
* **05_pipeline/** – Reproducible machine learning pipeline
* **06_repro_audit/** – Reproducibility assessment
* **07_model_card/** – Model card and dataset documentation
* **09_ethics/** – Ethics protocol
* **10_data_mgmt/** – Data management plan
* **11_bias_audit/** – Bias assessment and mitigation
* **12_integrity/** – Research integrity documentation
* **14_peer_review/** – Peer review reports
* **reflections/** – Reflective research log

---

## Reproducibility Requirements

The project has been designed so that an independent researcher can reproduce all results using only this repository.

Required software:

* Docker
* Git
* DVC
* Python 3.11+

---

## Clone Repository

```bash
git clone https://github.com/ludmerarcaya/unmsm-research-methods-Ludmer-Arcaya.git
cd unmsm-research-methods-Ludmer-Arcaya
```

---

## Retrieve Dataset

Datasets are managed using DVC.

Pull the data from the configured remote storage:

```bash
dvc pull
```

Expected output:

```text
Data successfully downloaded from remote storage.
```

---

## Build the Environment

Build the Docker image:

```bash
docker compose build
```

or

```bash
docker build -t unmsm-research-methods .
```

---

## Start the Environment

```bash
docker compose up -d
```

Verify running containers:

```bash
docker ps
```

Enter the working container:

```bash
docker exec -it workbench bash
```

---

## Install Dependencies

If required:

```bash
pip install -r requirements.txt
```

All package versions are pinned to ensure reproducibility.

---

## Run the Reproducible Pipeline

Execute the complete experiment:

```bash
python 05_pipeline/src/train.py
```

or execute the notebook:

```bash
jupyter notebook
```

and open:

```text
05_pipeline/notebook.ipynb
```

---

## Experiment Tracking

Experiments are tracked using MLflow.

Tracking artifacts are stored in:

```text
mlruns/
```

To inspect experiments:

```bash
mlflow ui
```

Then open:

```text
http://localhost:5000
```

---

## Reproducibility Checklist

* [x] Version-controlled source code
* [x] Dockerized execution environment
* [x] Pinned software dependencies
* [x] Dataset versioning using DVC
* [x] Experiment tracking with MLflow
* [x] Documented methodology
* [x] Ethical assessment completed
* [x] Bias audit completed
* [x] Research protocol documented

---

## Scientific Integrity Statement

This project adheres to the principles of scientific integrity established in the course Research Methods & Scientific Integrity in Artificial Intelligence.

All methodological decisions, data transformations, experiments, and results have been documented to maximize transparency, traceability, and reproducibility.

Any use of AI-assisted tools complies with the project AI Use Policy documented in:

```text
12_integrity/ai_use_policy.md
```

---

## Author

Ludmer Arcaya 

Doctoral Program in Deep Technologies

Universidad Nacional Mayor de San Marcos (UNMSM)

---

## License

Academic and research use only.

