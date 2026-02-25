# Customer Analytics Project

## Overview
This project performs exploratory data analysis (EDA) on customer data to understand customer behavior, demographics, and spending patterns. The analysis includes data cleaning, visualization, and correlation analysis.

## Dataset
- **File**: `customer_analytics.csv`
- **Description**: Contains customer information including demographics and spending behavior

## Project Structure
```
├── customer_analytics.csv
├── miniproject.ipynb
├── README.md
└── Untitled.ipynb
```

## Data Columns (Expected)
The dataset includes the following features:
- **Age**: Customer age
- **Gender**: Customer gender
- **Education**: Educational background
- **AnnualIncome**: Yearly income of the customer
- **LastPurchaseAmount**: Amount spent in the last purchase
- **SpendingScore**: Score indicating spending behavior

## Analysis Workflow

### 1. Data Loading & Exploration
- Load the CSV file using pandas
- Display first few records (`head()`)
- Check data types and structure (`info()`)
- Generate summary statistics (`describe()`)

### 2. Data Cleaning
- **Missing Values**: 
  - Handle missing values in 'Education' column using mode
  - Impute 'AnnualIncome' missing values using median
- **Duplicates**: Remove duplicate records from the dataset

### 3. Exploratory Data Analysis (EDA)

#### Univariate Analysis
- **Age Distribution**: Histogram showing how customer ages are distributed
- **Gender Distribution**: Bar chart showing gender composition
- **Annual Income Distribution**: Histogram visualizing income spread
- **Income Box Plot**: Identifies outliers and shows median income

#### Bivariate Analysis
- **Purchase Amount by Education Level**: Box plot showing spending patterns across education levels
- **Spending Score by Gender**: Comparison of spending behavior between genders
- **Income vs Spending Score**: Scatter plot exploring the relationship between income and spending behavior

### 4. Correlation Analysis
- Generate correlation matrix for numeric columns
- Visualize correlations using a heatmap with annotations
- Identify strong relationships between variables

## Key Insights
- Income and spending behavior may not have a strong linear relationship
- Gender-based spending patterns show slight variations
- Correlation analysis helps identify which variables influence customer behavior

## Technologies Used
- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **Jupyter Notebook**: Interactive analysis environment

## How to Run
1. Ensure all dependencies are installed:
   ```bash
   pip install pandas matplotlib seaborn jupyter
   ```
2. Place `customer_analytics.csv` in the same directory as the notebook
3. Open the notebook in Jupyter:
   ```bash
   jupyter notebook miniproject.ipynb
   ```
4. Run all cells to execute the analysis

## Outputs
The notebook generates the following visualizations:
- Histograms for Age and Annual Income distributions
- Bar chart for Gender distribution
- Box plots for income and spending analysis
- Scatter plot for Income vs Spending Score relationship
- Correlation heatmap showing variable relationships

## Notes
- All missing values are handled appropriately before analysis
- Duplicate records are removed to ensure data quality
- Statistical summaries provide baseline understanding of the data
- Visualizations are created with clear titles and labels for easy interpretation

## Author
DS/AI Internship - Day 20 Project

## Date
February 2026
