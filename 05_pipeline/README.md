# Reproducible ML Pipeline — Session 5

## What this is
A logistic-regression classifier on the citizen security lima dataset, built to be
fully reproducible: versioned code, data, experiments and environment.

## Data
data/citizen_security_lima_1000.csv is tracked with DVC. Pointer file: data/citizen_security_lima_1000.csv.dvc

## Reproduce the result
1. pip install -r requirements.txt
2. dvc pull            # retrieve the exact dataset version
3. python src/train.py --seed 42

## Expected output
seed=42  accuracy=0.21

## Environment
Python 3.11; exact packages in requirements.txt; see Dockerfile.
