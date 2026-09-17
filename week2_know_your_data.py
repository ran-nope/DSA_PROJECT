"""
WEEK 2 : "KNOW YOUR DATA"
Syllabus Mapping : Unit 1 (Practical)
----------------------------------------------------------------
Goals for this week:
    1. Load the dataset
    2. Check data types of every column
    3. Inspect the structure (shape, nulls, duplicates, uniques)
    4. Generate a "First Impression" report summarising the dataset
----------------------------------------------------------------
"""
import pandas as pd

DATA_PATH = "googleplaystore.csv"
df = pd.read_csv(DATA_PATH)

 
# 1. BASIC STRUCTURE
 
print("=" * 60)
print("BASIC STRUCTURE")
print("=" * 60)
print("Shape (rows, columns):", df.shape)
print("\nColumn names:", df.columns.tolist())
 
# 2. CHECKING DATA TYPES
 
print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)
print(df.dtypes)

# Note: Reviews, Size, Installs and Price look numeric but are
# stored as text (object) because of characters like "+", ",",
# "M", "$". This is exactly what we will fix in Week 3.

# 3. df.info() AND df.describe()
 
print("\n" + "=" * 60)
print("df.info()")
print("=" * 60)
df.info()

print("\n" + "=" * 60)
print("df.describe() - numeric columns")
print("=" * 60)
print(df.describe())

print("\n" + "=" * 60)
print("df.describe(include='object') - categorical columns")
print("=" * 60)
print(df.describe(include="object"))

 
# 4. MISSING VALUES
 
print("\n" + "=" * 60)
print("MISSING VALUES PER COLUMN")
print("=" * 60)
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_report = pd.DataFrame({"missing_count": missing, "missing_%": missing_pct.round(2)})
print(missing_report[missing_report["missing_count"] > 0])
 
# 5. DUPLICATES
 
print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)
print("Number of fully duplicate rows:", df.duplicated().sum())
print("Number of duplicate App names:", df.duplicated(subset="App").sum())
 
# 6. UNIQUE VALUES IN KEY CATEGORICAL COLUMNS
 
print("\n" + "=" * 60)
print("UNIQUE VALUES - KEY COLUMNS")
print("=" * 60)
for col in ["Category", "Type", "Content Rating", "Genres"]:
    print(f"\n{col}: {df[col].nunique()} unique values")
    print(df[col].value_counts().head(10))
 
# 7. "FIRST IMPRESSION" REPORT
 
print("\n" + "=" * 60)
print("FIRST IMPRESSION REPORT")
print("=" * 60)
report = f"""
Dataset          : Google Play Store Apps
Total records    : {df.shape[0]}
Total features   : {df.shape[1]}
Numeric columns  : {df.select_dtypes(include='number').columns.tolist()}
Text columns     : {df.select_dtypes(include='object').columns.tolist()}
Columns with missing data : {missing[missing > 0].index.tolist()}
Duplicate rows   : {df.duplicated().sum()}
Most common category : {df['Category'].mode()[0]}
Free vs Paid split : {df['Type'].value_counts().to_dict()}
Observations:
 - Reviews, Size, Installs, Price are stored as text and need cleaning.
 - Rating has missing values that will need imputation.
 - Category, Genres, Content Rating are categorical and can be
   used as grouping variables for later analysis.
"""
print(report)

with open("first_impression_report.txt", "w") as f:
    f.write(report)
print("Saved report to first_impression_report.txt")
