import pandas as pd

# Load Dataset
superstore = '/path/to/Superstore.csv'
df = pd.read_csv(superstore)

# 2. Data Cleaning

# Convert 'Order Date' and 'Ship Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%y')

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

