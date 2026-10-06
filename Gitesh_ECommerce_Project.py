import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("ecommerce_sales_data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# -----------------------------
# Data inspection
# -----------------------------
print("First 5 records:")
print(df.head())

print("\nDataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# -----------------------------
# Key Business KPIs
# -----------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_quantity = df["Quantity"].sum()
avg_order_value = total_sales / total_orders

print("\n========== KEY KPIs ==========")
print(f"Total Sales       : ₹{total_sales:,.2f}")
print(f"Total Profit      : ₹{total_profit:,.2f}")
print(f"Total Orders      : {total_orders}")
print(f"Total Quantity    : {total_quantity}")
print(f"Average Order Val.: ₹{avg_order_value:,.2f}")

# -----------------------------
# Product analysis
# -----------------------------
product_sales = (
    df.groupby("Product")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n========== SALES BY PRODUCT ==========")
print(product_sales)

# -----------------------------
# Category analysis
# -----------------------------
category_summary = (
    df.groupby("Category")[["Sales", "Profit"]]
      .sum()
      .sort_values("Sales", ascending=False)
)

print("\n========== CATEGORY PERFORMANCE ==========")
print(category_summary)

# -----------------------------
# Region analysis
# -----------------------------
region_summary = (
    df.groupby("Region")[["Sales", "Profit"]]
      .sum()
      .sort_values("Sales", ascending=False)
)

print("\n========== REGION PERFORMANCE ==========")
print(region_summary)

# -----------------------------
# Customer segment analysis
# -----------------------------
segment_summary = (
    df.groupby("Customer_Segment")[["Sales", "Profit"]]
      .sum()
      .sort_values("Sales", ascending=False)
)

print("\n========== CUSTOMER SEGMENTS ==========")
print(segment_summary)

# -----------------------------
# Monthly sales trend
# -----------------------------
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
      .sum()
)

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

# -----------------------------
# Top 10 customers
# -----------------------------
top_customers = (
    df.groupby("Customer_ID")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n========== TOP 10 CUSTOMERS ==========")
print(top_customers)

# -----------------------------
# Visualizations
# -----------------------------
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))
product_sales.head(10).plot(kind="bar")
plt.title("Top Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_products_sales.png", dpi=300)
plt.show()

plt.figure(figsize=(9, 5))
category_summary["Sales"].plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("category_sales.png", dpi=300)
plt.show()

plt.figure(figsize=(9, 5))
region_summary["Sales"].plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.savefig("region_sales.png", dpi=300)
plt.show()

plt.figure(figsize=(11, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=300)
plt.show()

plt.figure(figsize=(9, 5))
sns.scatterplot(data=df, x="Discount_Percent", y="Profit", hue="Category")
plt.title("Discount vs Profit")
plt.xlabel("Discount (%)")
plt.ylabel("Profit (₹)")
plt.tight_layout()
plt.savefig("discount_vs_profit.png", dpi=300)
plt.show()

print("\nAnalysis completed successfully.")
