import pandas as pd

# Load Dataset
superstore = './data/Superstore.csv'
df = pd.read_csv(superstore)

# 4. Aggregation for Insights

# Aggregate Sales, Profit, and Discount by Region
agg_by_region = df.groupby('Region').agg({'Sales': 'sum', 'Profit': 'sum'})
print("Sales, and Profit, by Region:\n", agg_by_region)

# Aggregate Sales, Profit, and Discount by Category
agg_by_category = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum', 'Discount': 'sum'})
print("Sales, Profit, and Discount by Category:\n", agg_by_category)

# Aggregate Sales, Profit, and Discount by Ship Mode
agg_by_ship_mode = df.groupby('Ship Mode').agg({'Sales': 'sum', 'Profit': 'sum', 'Discount': 'sum'})
print("Sales, Profit, and Discount by Ship Mode:\n", agg_by_ship_mode)
