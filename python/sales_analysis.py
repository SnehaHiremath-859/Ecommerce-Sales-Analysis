import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../dataset/SampleSuperstore.csv")

# Dataset Information
print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nSummary Statistics:")
print(df.describe())

# ----------------------------
# Sales by Category
# ----------------------------
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# ----------------------------
# Sales by Region
# ----------------------------
region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

plt.figure(figsize=(6,4))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# ----------------------------
# Sales by Segment
# ----------------------------
segment_sales = df.groupby("Segment")["Sales"].sum()

print("\nSales by Segment:")
print(segment_sales)

plt.figure(figsize=(6,4))
segment_sales.plot(kind="bar")
plt.title("Sales by Segment")
plt.xlabel("Segment")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# ----------------------------
# Top 10 Sub-Categories by Sales
# ----------------------------
top_products = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Sub-Categories by Sales:")
print(top_products)

plt.figure(figsize=(8,5))
top_products.plot(kind="bar")
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# Profit by Region
# ----------------------------
region_profit = df.groupby("Region")["Profit"].sum()

print("\nProfit by Region:")
print(region_profit)

plt.figure(figsize=(6,4))
region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.show()