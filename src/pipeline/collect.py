from pathlib import Path
import pandas as pd

df = pd.read_csv("data/raw/breast_cancer.csv")

df["collected_at"] = pd.Timestamp.now().isoformat()

Path("data/raw").mkdir(parents=True, exist_ok=True)

df.to_csv("data/raw/breast_cancer_raw.csv", index=False)

print("Collection completed. Rows:", len(df))
