"""
WEEK 4 : EDA DEEP DIVE
Syllabus Mapping : Unit 2 (Practical)
----------------------------------------------------------------
Goals for this week:
    1. Univariate analysis (single variable at a time)
    2. Bivariate analysis (relationship between two variables)
    3. Visualize distributions to understand app success patterns

Uses the cleaned dataset produced in Week 3
(googleplaystore_cleaned.csv). Run week3_cleaning_sprint.py first.
----------------------------------------------------------------
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("googleplaystore_cleaned.csv")
print("Loaded cleaned dataset. Shape:", df.shape)

# ==================================================================
# PART A : UNIVARIATE ANALYSIS
# ==================================================================

# A1. Distribution of Rating
plt.figure(figsize=(8, 5))
sns.histplot(df["Rating"], bins=20, kde=True, color="steelblue")
plt.title("Distribution of App Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Apps")
plt.tight_layout()
plt.savefig("week4_univariate_rating.png", dpi=150)
plt.show()
plt.close()
print("Saved: week4_univariate_rating.png")

# A2. Number of apps per Category
plt.figure(figsize=(10, 5))
order = df["Category"].value_counts().index
sns.countplot(y="Category", data=df, order=order, palette="viridis")
plt.title("Number of Apps per Category")
plt.xlabel("Count")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("week4_univariate_category.png", dpi=150)
plt.show()
plt.close()
print("Saved: week4_univariate_category.png")

# A3. Free vs Paid split
plt.figure(figsize=(5, 5))
df["Type"].value_counts().plot.pie(autopct="%1.1f%%", colors=["#66b3ff", "#ff9999"])
plt.title("Free vs Paid Apps")
plt.ylabel("")
plt.tight_layout()
plt.savefig("week4_univariate_type.png", dpi=150)
plt.show()
plt.close()
print("Saved: week4_univariate_type.png")

# A4. Distribution of Installs (log scale, since installs vary hugely)
plt.figure(figsize=(8, 5))
sns.histplot(np.log10(df["Installs"].replace(0, 1)), bins=20, color="seagreen")
plt.title("Distribution of Installs (log10 scale)")
plt.xlabel("log10(Installs)")
plt.ylabel("Number of Apps")
plt.tight_layout()
plt.savefig("week4_univariate_installs.png", dpi=150)
plt.show()
plt.close()
print("Saved: week4_univariate_installs.png")

# ==================================================================
# PART B : BIVARIATE ANALYSIS
# ==================================================================

# B1. Rating vs Category (Boxplot)
plt.figure(figsize=(12, 6))
sns.boxplot(x="Category", y="Rating", data=df, palette="Set2")
plt.title("Rating Distribution across Categories")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("week4_bivariate_rating_category.png", dpi=150)
plt.show()
plt.close()
print("Saved: week4_bivariate_rating_category.png")

# B2. Reviews vs Installs (scatter, log-log since both are skewed)
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x=np.log10(df["Installs"].replace(0, 1)),
    y=np.log10(df["Reviews"].replace(0, 1)),
    hue=df["Type"],
    alpha=0.6,
)
plt.title("Reviews vs Installs (log-log scale)")
plt.xlabel("log10(Installs)")
plt.ylabel("log10(Reviews)")
plt.tight_layout()
plt.savefig("week4_bivariate_reviews_installs.png", dpi=150)
plt.show()
plt.close()
print("Saved: week4_bivariate_reviews_installs.png")

# B3. Rating vs Type (Free vs Paid)
plt.figure(figsize=(6, 5))
sns.violinplot(x="Type", y="Rating", data=df, palette="pastel")
plt.title("Rating Distribution: Free vs Paid Apps")
plt.tight_layout()
plt.savefig("week4_bivariate_rating_type.png", dpi=150)
plt.show()
plt.close()
print("Saved: week4_bivariate_rating_type.png")

# B4. Correlation heatmap of numeric features
plt.figure(figsize=(7, 6))
numeric_df = df[["Rating", "Reviews", "Size", "Installs", "Price"]]
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Numeric Features")
plt.tight_layout()
plt.savefig("week4_correlation_heatmap.png", dpi=150)
plt.show()
plt.close()
print("Saved: week4_correlation_heatmap.png")

# ==================================================================
# PART C : KEY INSIGHTS SUMMARY (for the report)
# ==================================================================
insights = f"""
WEEK 4 - KEY EDA INSIGHTS
--------------------------------------------------
1. Average app rating is {df['Rating'].mean():.2f}, and most ratings
   cluster between 4.0 and 4.5 - users tend to rate apps generously.
2. {df['Category'].value_counts().idxmax()} is the most common category
   in this sample ({df['Category'].value_counts().max()} apps).
3. {(df['Type'].value_counts(normalize=True)['Free']*100):.1f}% of apps
   are Free, confirming a freemium-dominated market.
4. Installs and Reviews show a positive relationship on the log scale -
   apps with more installs tend to accumulate more reviews.
5. Correlation between Rating and other numeric features
   (Reviews, Size, Price, Installs) is generally weak, suggesting
   rating alone is not driven by any single numeric factor - this is
   part of the motivation for the PCA step planned in later weeks.
"""
print(insights)
with open("week4_insights.txt", "w") as f:
    f.write(insights)
print("Saved: week4_insights.txt")
