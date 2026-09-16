"""
WEEK 1 : TEAM FORMATION & DATA HUNTING
Syllabus Mapping : Unit 1
----------------------------------------------------------------
Goals for this week:
    1. Select the dataset (Google Play Store Apps - Kaggle)
    2. Set up the GitHub repository for the project
    3. Get comfortable with the two core libraries we will use
       throughout the project: Pandas and NumPy

Dataset source:
    https://www.kaggle.com/datasets/lava18/google-play-store-apps
    File used: googleplaystore.csv
    (Download it from Kaggle and place it in the same folder as
    this script before running.)
----------------------------------------------------------------
"""

import pandas as pd
import numpy as np

# ------------------------------------------------------------------
# 1. GITHUB SETUP (documented here for the report - not executable code)
# ------------------------------------------------------------------
# git init
# git add .
# git commit -m "Week 1: project setup + dataset added"
# git remote add origin <your-repo-url>
# git push -u origin main
#
# Repo structure used for this project:
#   dsv-project/
#   ├── data/googleplaystore.csv
#   ├── week1_data_hunting.py
#   ├── week2_know_your_data.py
#   ├── week3_cleaning_sprint.py
#   ├── week4_eda_deep_dive.py
#   └── README.md

# ------------------------------------------------------------------
# 2. LOADING THE DATASET FOR THE FIRST TIME
# ------------------------------------------------------------------
DATA_PATH = "googleplaystore.csv"
df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Shape of the dataset (rows, columns):", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows of the dataset:")
print(df.head())

# ------------------------------------------------------------------
# 3. GETTING COMFORTABLE WITH PANDAS
# ------------------------------------------------------------------
print("\n--- Pandas basics ---")
print("Selecting a single column (App):")
print(df["App"].head())

print("\nSelecting multiple columns:")
print(df[["App", "Category", "Rating"]].head())

print("\nFiltering rows: apps with a Rating above 4.5")
high_rated = df[df["Rating"] > 4.5]
print(f"Number of apps rated above 4.5: {len(high_rated)}")

print("\nSorting apps by Rating (descending):")
print(df.sort_values(by="Rating", ascending=False)[["App", "Rating"]].head())

# ------------------------------------------------------------------
# 4. GETTING COMFORTABLE WITH NUMPY
# ------------------------------------------------------------------
print("\n--- NumPy basics ---")
ratings_array = df["Rating"].dropna().to_numpy()
print("Ratings converted to a NumPy array, sample:", ratings_array[:5])
print("Mean rating (NumPy):", np.mean(ratings_array))
print("Standard deviation of ratings (NumPy):", np.std(ratings_array))
print("Max rating:", np.max(ratings_array), "| Min rating:", np.min(ratings_array))

# A quick NumPy array operation demo
sample = np.array([1, 2, 3, 4, 5])
print("\nSample array:", sample)
print("Array squared:", sample ** 2)
print("Array mean:", sample.mean())

print("\nWeek 1 complete: dataset selected, repo initialised, "
      "and team is comfortable with Pandas/NumPy basics.")
