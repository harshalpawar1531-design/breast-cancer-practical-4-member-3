from pathlib import Path
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer(as_frame=True)
df = data.frame.copy()

df["diagnosis"] = df["target"].map({
    0: "malignant",
    1: "benign"
})

Path("data/raw").mkdir(parents=True, exist_ok=True)
df.to_csv("data/raw/breast_cancer.csv", index=False)

print("Dataset generated:", df.shape)
print("Saved to data/raw/breast_cancer.csv")
