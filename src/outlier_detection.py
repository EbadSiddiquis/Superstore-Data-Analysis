import pandas as pd

# Load Dataset
superstore = '/path/to/Superstore.csv'
df = pd.read_csv(superstore)

# 3. Data Analysis

# Investigate extreme values in 'Sales' and 'Profit'
outliers_sales = df[df['Sales'] > df['Sales'].quantile(0.99)]  # Top 1% sales
outliers_profit = df[df['Profit'] < df['Profit'].quantile(0.01)]  # Bottom 1% profit (losses)

# Print Results
print("Top 1% sales outliers:\n", outliers_sales[['Order ID', 'Sales', 'Profit']])
print("Bottom 1% profit outliers:\n", outliers_profit[['Order ID', 'Sales', 'Profit']])
