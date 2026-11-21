import pandas as pd

df = pd.read_csv("data/processed/breast_cancer_preprocessed.csv")

df["radius_texture_ratio"] = (
    df["mean radius"] / df["mean texture"].replace(0, 1)
)

df["perimeter_area_ratio"] = (
    df["mean perimeter"] / df["mean area"].replace(0, 1)
)

df.to_csv("data/processed/breast_cancer_features.csv", index=False)

print("Feature engineering completed")
print("Added radius_texture_ratio and perimeter_area_ratio")
