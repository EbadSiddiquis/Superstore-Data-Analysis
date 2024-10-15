import pandas as pd

# Load Dataset
superstore = '/path/to/Superstore.csv'
df = pd.read_csv(superstore)

# 5. Top 10/Bottom 10 Analysis

# Top and Bottom 10 Products by Sales
top_10_sales_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
bottom_10_sales_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=True).head(10)

# Top and Bottom 10 products by Profit
top_10_profit_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
bottom_10_profit_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=True).head(10)

# Top and Bottom 10 customers by Sales
top_10_sales_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
bottom_10_sales_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=True).head(10)

# Top and Bottom 10 Customers by Profits
top_10_profit_customers = df.groupby('Customer Name')['Profit'].sum().sort_values(ascending=False).head(10)
bottom_10_profit_customers = df.groupby('Customer Name')['Profit'].sum().sort_values(ascending=True).head(10)

# Display the Top 10/Bottom 10 results
print("Top 10 Products by Sales:\n", top_10_sales_products)
print("Bottom 10 Products by Sales:\n", bottom_10_sales_products)
print("Top 10 Products by Profit:\n", top_10_profit_products)
print("Bottom 10 Products by Profit:\n", bottom_10_profit_products)
print("Top 10 Customers by Sales:\n", top_10_sales_customers)
print("Bottom 10 Customers by Sales:\n", bottom_10_sales_customers)
print("Top 10 Customers by Profit: \n", top_10_profit_customers)
print("Bottom 10 Customers by Profit: \n", bottom_10_profit_customers)
