# Data Cleaning & Visualization Project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load raw data
df = pd.read_csv("raw_data.csv")
print("Raw shape:", df.shape)
print(df.head())

# 2. Inspect missing values and duplicates
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# 3. Remove duplicate orders
df = df.drop_duplicates(subset=["Order_ID"]).copy()

# 4. Fill missing categorical values
df["Category"] = df["Category"].fillna(df["Category"].mode()[0])
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])

# 5. Fill missing numeric values with median
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Customer_Rating"] = df["Customer_Rating"].fillna(df["Customer_Rating"].median())

# 6. Handle outlier in Quantity using IQR
Q1 = df["Quantity"].quantile(0.25)
Q3 = df["Quantity"].quantile(0.75)
IQR = Q3 - Q1
upper = Q3 + 1.5 * IQR
df.loc[df["Quantity"] > upper, "Quantity"] = upper

# 7. Create useful columns
df["Date"] = pd.to_datetime(df["Date"])
df["Sales"] = df["Quantity"] * df["Unit_Price"]
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# 8. Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# 9. Summary
print("\nCleaned shape:", df.shape)
print("\nSales by category:\n", df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
print("\nSales by region:\n", df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

# 10. Visualization - sales by category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png", dpi=200)
plt.show()

# 11. Visualization - sales by region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png", dpi=200)
plt.show()

# 12. Visualization - monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()
plt.figure(figsize=(8,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png", dpi=200)
plt.show()
