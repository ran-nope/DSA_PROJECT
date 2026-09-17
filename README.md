# The Perfect Product Launch — Google Play Store Analysis

**Category:** Business, Retail & E-Commerce | **SDG 9:** Industry, Innovation & Infrastructure

## Project Overview
This project performs an end-to-end exploratory data analysis (EDA) on the Google Play Store landscape. By cleaning, visualizing, and analyzing app metrics (ratings, size, installs, price, and categories), this analysis aims to uncover the patterns behind successful app launches in a freemium-dominated market.

## Project Structure
Ensure your directory looks like this before running the scripts:

```text
dsv-project/
├── data/
│   └── googleplaystore.csv       <- Download from Kaggle and place here
├── week1_data_hunting.py
├── week2_know_your_data.py
├── week3_cleaning_sprint.py
├── week4_eda_deep_dive.py
└── README.md
```

## Prerequisites & Installation

1. **Download the dataset** from Kaggle: [Google Play Store Apps](https://www.kaggle.com/datasets/lava18/google-play-store-apps)
2. **Move the CSV** into the same folder as the scripts (or a `data/` subfolder as shown above).
3. **Install the required Python libraries**:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy missingno
   ```

## How to Run

Execute the scripts sequentially. Each script prints its progress to the console and saves generated reports (.txt) and visualizations (.png) directly to the working directory.

```bash
python week1_data_hunting.py
python week2_know_your_data.py
python week3_cleaning_sprint.py   # Generates: googleplaystore_cleaned.csv
python week4_eda_deep_dive.py     # Requires the cleaned CSV from week 3
```
*Note: Re-run the scripts on your local machine to generate fresh copies of every plot and text report before submitting your final project document and slides.*

## Weekly Sprint Breakdown

| Week | Script File | Description | Syllabus Mapping |
| :--- | :--- | :--- | :--- |
| **Week 1** | `week1_data_hunting.py` | Loads data, documents GitHub setup, introduces Pandas/NumPy basics. | Unit 1 |
| **Week 2** | `week2_know_your_data.py` | Checks `dtypes`, `info()`, `describe()`, missing values, and generates the "First Impression" txt report. | Unit 1 (Practical) |
| **Week 3** | `week3_cleaning_sprint.py` | Cleans Installs/Price/Size/Reviews, imputes missing values, boxplot + Z-score outlier detection. Outputs cleaned CSV. | Unit 2 |
| **Week 4** | `week4_eda_deep_dive.py` | Univariate & bivariate analysis, distribution plots, correlation heatmap, and EDA insights generation. | Unit 2 (Practical) |

## Methodology Notes for Reviewers
During the **Week 3 Cleaning Sprint**, specific statistical choices were made to handle messy data:
*   **Median Imputation:** Applied to `Rating` and `Size` due to right-skewed distributions where the mean would be distorted.
*   **Mode Imputation:** Applied to the categorical `Type` column.
*   **Outlier Capping:** The `Reviews` column was capped at the 99th percentile to prevent a few hyper-viral apps from distorting downstream visualizations.
