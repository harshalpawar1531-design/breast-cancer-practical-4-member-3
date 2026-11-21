# Breast Cancer Classification - MLOps

## Practical Details
- Practical Number: 4
- Member: 3
- Title: Data Lifecycle Management and Pipeline Automation

## Aim
To automate the breast cancer data lifecycle using DVC.

## Dataset
- Wisconsin Diagnostic Breast Cancer Dataset
- Total Samples: 569
- Original Input Features: 30
- Classes: Malignant and Benign
- Source: Scikit-learn

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- DVC
- Git

## Pipeline Stages
1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Data Validation

## Pipeline Flow
Collection -> Preprocessing -> Features -> Validation

## Execution Commands
python generate_breast_cancer.py
dvc repro
dvc dag
dvc status

## Results
- Data Collection: Successful
- Data Preprocessing: Successful
- Feature Engineering: Successful
- Data Validation: Successful
- Final Dataset Shape: (569, 34)
- New Engineered Features: 2
- No missing values in required columns

## Conclusion
The automated data pipeline was successfully implemented
using DVC for Breast Cancer Classification.

This project is for educational purposes only.
