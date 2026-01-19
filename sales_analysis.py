# Sales Data Analysis
import pandas as pd

df = pd.read_csv("sales_data.csv")

# Display first few rows
print("FIRST 5 ROWS OF DATASET:")
print(df.head())

print("\nDATASET INFORMATION:")
print(df.info())

# Check for missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Handle missing values
df.fillna(0, inplace=True)

# Remove duplicate rows if any
df.drop_duplicates(inplace=True)

# Calculate metrics
total_sales = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
maximum_sales = df["Total_Sales"].max()
minimum_sales = df["Total_Sales"].min()

# Find best-selling product
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

# Display analysis results
print("\nSALES ANALYSIS REPORT")
print("----------------------------")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Average Sales: ₹{average_sales:,.2f}")
print(f"Highest Single Sale: ₹{maximum_sales:,.2f}")
print(f"Lowest Single Sale: ₹{minimum_sales:,.2f}")
print(f"Best Selling Product: {best_product}")

print("\nAnalysis completed successfully!")
