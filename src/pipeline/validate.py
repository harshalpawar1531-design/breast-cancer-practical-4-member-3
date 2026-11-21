import pandas as pd

df = pd.read_csv("data/processed/breast_cancer_features.csv")

required = [
    "mean radius", "mean texture", "mean perimeter", "mean area",
    "mean smoothness", "diagnosis", "target",
    "radius_texture_ratio", "perimeter_area_ratio"
]

missing = [column for column in required if column not in df.columns]

if missing:
    raise ValueError(f"Missing columns: {missing}")

if df.empty:
    raise ValueError("Dataset is empty")

if df[required].isnull().any().any():
    raise ValueError("Missing values found in required columns")

if not set(df["diagnosis"].unique()).issubset({"malignant", "benign"}):
    raise ValueError("Unexpected diagnosis label")

print("Data validation successful")
print("Dataset shape:", df.shape)
print("Required columns present; no missing values")
