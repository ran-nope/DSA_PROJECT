"""
WEEK 3 : THE CLEANING SPRINT
Syllabus Mapping : Unit 2
----------------------------------------------------------------
Goals for this week:
    1. Convert messy text columns (Reviews, Size, Installs, Price)
       into proper numeric columns
    2. Handle missing values (imputation strategies)
    3. Detect outliers using Boxplots and the Z-score method
    4. Save a cleaned dataset for next week's EDA
----------------------------------------------------------------
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_style("whitegrid")

DATA_PATH = "googleplaystore.csv"
df = pd.read_csv(DATA_PATH)

print("Shape before cleaning:", df.shape)

# ------------------------------------------------------------------
# 1. REMOVE DUPLICATES
# ------------------------------------------------------------------
before = df.shape[0]
df = df.drop_duplicates()
print(f"Removed {before - df.shape[0]} duplicate rows.")

# ------------------------------------------------------------------
# 2. CLEANING "Installs" -> numeric
#    e.g. "10,000+"  ->  10000
# ------------------------------------------------------------------
df["Installs"] = (
    df["Installs"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("+", "", regex=False)
    .str.replace("Free", "0", regex=False)   # safety net for stray bad values
)
df["Installs"] = pd.to_numeric(df["Installs"], errors="coerce")

# ------------------------------------------------------------------
# 3. CLEANING "Price" -> numeric
#    e.g. "$4.99" -> 4.99 , "0" -> 0.0
# ------------------------------------------------------------------
df["Price"] = df["Price"].astype(str).str.replace("$", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# ------------------------------------------------------------------
# 4. CLEANING "Size" -> numeric (in MB)
#    e.g. "19M" -> 19.0 , "Varies with device" -> NaN (imputed later)
# ------------------------------------------------------------------
def clean_size(value):
    value = str(value)
    if "Varies with device" in value:
        return np.nan
    if value.endswith("M"):
        return float(value.replace("M", ""))
    if value.endswith("k"):
        return float(value.replace("k", "")) / 1024   # convert KB to MB
    return np.nan

df["Size"] = df["Size"].apply(clean_size)

# ------------------------------------------------------------------
# 5. CLEANING "Reviews" -> numeric
# ------------------------------------------------------------------
df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")

print("\nData types after cleaning:")
print(df[["Installs", "Price", "Size", "Reviews", "Rating"]].dtypes)

# ------------------------------------------------------------------
# 6. HANDLING MISSING VALUES (Imputation)
# ------------------------------------------------------------------
print("\nMissing values BEFORE imputation:")
print(df[["Rating", "Size", "Type"]].isnull().sum())

# Rating -> numeric, right-skewed a bit -> use median (robust to outliers)
df["Rating"] = df["Rating"].fillna(df["Rating"].median())

# Size -> numeric -> use median as well ("Varies with device" left many NaNs)
df["Size"] = df["Size"].fillna(df["Size"].median())

# Type -> categorical -> use mode (most frequent category)
df["Type"] = df["Type"].fillna(df["Type"].mode()[0])

print("\nMissing values AFTER imputation:")
print(df[["Rating", "Size", "Type"]].isnull().sum())

# ------------------------------------------------------------------
# 7. OUTLIER DETECTION - BOXPLOTS
# ------------------------------------------------------------------
numeric_cols = ["Rating", "Reviews", "Size", "Installs", "Price"]

fig, axes = plt.subplots(1, len(numeric_cols), figsize=(20, 4))
for ax, col in zip(axes, numeric_cols):
    sns.boxplot(y=df[col], ax=ax, color="skyblue")
    ax.set_title(f"Boxplot: {col}")
plt.tight_layout()
plt.savefig("week3_boxplots.png", dpi=150)
plt.show()
plt.close()
print("\nSaved boxplots to week3_boxplots.png")

# ------------------------------------------------------------------
# 8. OUTLIER DETECTION - Z-SCORE METHOD
# ------------------------------------------------------------------
print("\nOutlier detection using Z-score (|z| > 3):")
outlier_summary = {}
for col in numeric_cols:
    z_scores = np.abs(stats.zscore(df[col].dropna()))
    n_outliers = (z_scores > 3).sum()
    outlier_summary[col] = n_outliers
    print(f"  {col}: {n_outliers} potential outliers")

# Example: capping Reviews outliers at the 99th percentile
# (a common strategy so that a few viral apps don't distort later analysis)
upper_cap = df["Reviews"].quantile(0.99)
df["Reviews"] = np.where(df["Reviews"] > upper_cap, upper_cap, df["Reviews"])
print(f"\nCapped 'Reviews' outliers above the 99th percentile ({upper_cap:.0f}).")

# ------------------------------------------------------------------
# 9. SAVE CLEANED DATASET
# ------------------------------------------------------------------
df.to_csv("googleplaystore_cleaned.csv", index=False)
print("\nCleaned dataset saved as googleplaystore_cleaned.csv")
print("Final shape:", df.shape)
