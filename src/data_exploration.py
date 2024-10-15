import pandas as pd

# Load Dataset
superstore = '/Users/ebads/Documents/Superstore.csv'

# Load the dataset from the file path
df = pd.read_csv(superstore)

# Display basic information and structure of the dataset
df.info()  # To check the structure of the dataset

# Preview the first few rows of the dataset
print(df.head())  # To display the first five rows
