import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

# Load Iris dataset from sklearn and convert to DataFrame
iris = load_iris(as_frame=True)
df = iris.frame

print("First 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nCheck for missing values:")
print(df.isnull().sum())

# No missing values in this dataset, but code below shown as example
# df = df.fillna(method="ffill")  # or df.dropna()

# Task 2: Basic Data Analysis

print("\nBasic statistics on numerical columns:")
print(df.describe())

# Group by species and compute mean of all numeric columns
grouped = df.groupby("target").mean()
print("\nMean by species:")
print(grouped)

# Task 3: Data Visualization

sns.set(style="whitegrid")

# 1. Bar chart (mean sepal length per species)
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x=df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"}),
    y='sepal length (cm)',
    estimator=np.mean,
    ci=None
)
plt.title("Mean Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Mean Sepal Length (cm)")
plt.show()

# 2. Bar chart (mean petal width per species)
plt.figure(figsize=(8, 5))
grouped["petal width (cm)"].plot(kind='bar', color='skyblue')
plt.title("Average Petal Width by Species")
plt.xlabel("Species")
plt.ylabel("Petal Width (cm)")
plt.xticks(ticks=range(3), labels=iris.target_names, rotation=0)
plt.show()

# 3. Histogram (distribution of sepal length)
plt.figure(figsize=(8, 5))
sns.histplot(df["sepal length (cm)"], bins=20, color='coral')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length by species)
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="sepal length (cm)",
    y="petal length (cm)",
    hue=df["target"].map({0:"setosa", 1:"versicolor", 2:"virginica"})
)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
