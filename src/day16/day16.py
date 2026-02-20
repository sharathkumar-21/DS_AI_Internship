# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 09:55:36 2026

@author: Sharath Kumar
"""

# ==========================================================
# DAY 16 — STATISTICS: DISTRIBUTIONS COMPLETE SCRIPT
# ==========================================================

# ----------------------------------------------------------
# STEP 1 — Import Required Libraries
# ----------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# ----------------------------------------------------------
# STEP 2 — Create Dataset (Simulated Real-World Data)
# ----------------------------------------------------------
# We'll generate both normal and skewed data to compare

np.random.seed(42)

normal_data = np.random.normal(loc=50, scale=10, size=1000)   # Normal distribution
skewed_data = np.random.exponential(scale=20, size=1000)      # Right-skewed distribution

df = pd.DataFrame({
    "Normal_Data": normal_data,
    "Skewed_Data": skewed_data
})

# ==========================================================
# TOPIC 1 — UNDERSTANDING DISTRIBUTIONS
# ==========================================================

# Histogram for Normal Distribution
plt.figure()
sns.histplot(df["Normal_Data"], kde=True)
plt.title("Normal Distribution")
plt.show()

# Histogram for Skewed Distribution
plt.figure()
sns.histplot(df["Skewed_Data"], kde=True)
plt.title("Right-Skewed Distribution")
plt.show()

# Compare Mean and Median
print("\nNormal Data Mean:", df["Normal_Data"].mean())
print("Normal Data Median:", df["Normal_Data"].median())

print("\nSkewed Data Mean:", df["Skewed_Data"].mean())
print("Skewed Data Median:", df["Skewed_Data"].median())

# ==========================================================
# TOPIC 2 — Z-SCORES & OUTLIER DETECTION
# ==========================================================

# Calculate Z-scores for Normal Data
mean = df["Normal_Data"].mean()
std = df["Normal_Data"].std()

df["Z_Score"] = (df["Normal_Data"] - mean) / std

# Identify potential outliers (|Z| > 3)
outliers = df[np.abs(df["Z_Score"]) > 3]

print("\nNumber of Outliers Detected:", len(outliers))

# Visualize Outliers using Boxplot
plt.figure()
sns.boxplot(x=df["Normal_Data"])
plt.title("Outlier Detection (Boxplot)")
plt.show()

# ==========================================================
# TOPIC 3 — CENTRAL LIMIT THEOREM (CLT)
# ==========================================================

sample_means = []

# Take many random samples and compute their means
for i in range(1000):
    sample = np.random.choice(df["Skewed_Data"], size=30)
    sample_means.append(sample.mean())

# Plot distribution of sample means
plt.figure()
sns.histplot(sample_means, kde=True)
plt.title("Central Limit Theorem — Distribution of Sample Means")
plt.show()

# ==========================================================
# TOPIC 4 — SAMPLING TECHNIQUES
# ==========================================================

# Treat Normal_Data as population
population = df["Normal_Data"]

# Take random sample
sample = population.sample(n=50, random_state=42)

# Compare statistics
print("\nPopulation Mean:", population.mean())
print("Sample Mean:", sample.mean())

print("\nPopulation Std:", population.std())
print("Sample Std:", sample.std())

# Visualize population vs sample
plt.figure()
sns.histplot(population, color="blue", label="Population", kde=True)
sns.histplot(sample, color="red", label="Sample", kde=True)
plt.legend()
plt.title("Population vs Sample Distribution")
plt.show()

# ==========================================================
# FINAL INSIGHTS (Students should write their own)
# ==========================================================
print("\n===== SAMPLE INSIGHTS =====")
print("1. Normal data is symmetric, skewed data has long right tail.")
print("2. Z-scores help identify unusual values.")
print("3. Sample means become normally distributed (CLT).")
print("4. Sample statistics approximate population statistics.")
print("\nDay 16 Completed Successfully!")



















print("task-1,shape shifter")
import numpy as np                  
import pandas as pd                 
import matplotlib.pyplot as plt     
import seaborn as sns               

np.random.seed(0)

# Human Heights (Normal Distribution)
heights = np.random.normal(loc=170, scale=8, size=1000)

# Household Incomes (Right-Skewed Distribution)
incomes = np.random.exponential(scale=50000, size=1000)

# Easy Exam Scores (Left-Skewed Distribution)
scores = 100 - np.random.exponential(scale=10, size=1000)

df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

for column in df.columns:
    
    plt.figure()                                  
    sns.histplot(df[column], kde=True)            
    plt.title(f"{column} Distribution")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()
    
    mean_value = df[column].mean()                
    median_value = df[column].median()            
    
    
    print(f"{column} Mean: {mean_value}")
    print(f"{column} Median: {median_value}")
    
    # Identify Skewness
    if mean_value > median_value:
        print("Observation: Right-Skewed (Mean > Median)")
    elif mean_value < median_value:
        print("Observation: Left-Skewed (Mean < Median)")
    else:
        print("Observation: Approximately Normal (Mean ≈ Median)")
    
    print("-" * 50)
    
    
    
    
    
    
    
    
print("task-2,outlier detection")
    
import numpy as np                  
import pandas as pd                 

np.random.seed(0)

# Generate Sample Dataset 
data = np.random.normal(loc=1000, scale=200, size=1000)   

df = pd.DataFrame({"SAT_Score": data})                    

#Calculate Mean (μ) and Standard Deviation (σ)
mu = df["SAT_Score"].mean()                               
sigma = df["SAT_Score"].std()                             

print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)

# Step 2: Create Z-score column
# Formula: Z = (x - μ) / σ
df["z_score"] = (df["SAT_Score"] - mu) / sigma

# Identify Outliers where |Z| > 3

outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers (|Z| > 3):")
print(outliers)
print("\nNumber of Outliers:", len(outliers))




print("task-3,magic of averages")
# Import required libraries
import numpy as np                  
import pandas as pd                 
import matplotlib.pyplot as plt     
import seaborn as sns               

# Set seed for reproducibility
np.random.seed(0)

#Create a heavily skewed dataset
# (Using exponential distribution to simulate income)

population = np.random.exponential(scale=50000, size=100000)

#Visualize original skewed data
plt.figure()
sns.histplot(population, kde=True)
plt.title("Original Population Distribution (Right-Skewed)")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

#Take 1000 samples of size 30 and compute means
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)   
    sample_mean = np.mean(sample)                    
    sample_means.append(sample_mean)                 

# Convert to DataFrame
means_df = pd.DataFrame({"Sample_Means": sample_means})

#Plot distribution of sample means
plt.figure()
sns.histplot(means_df["Sample_Means"], kde=True)
plt.title("Distribution of Sample Means (n=30, 1000 samples)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()

# Print Mean and Standard Deviation of sample means
print("Mean of Sample Means:", means_df["Sample_Means"].mean())
print("Standard Deviation of Sample Means:", means_df["Sample_Means"].std())
    
    