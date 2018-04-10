# Import Required libraries
import pandas as pd 
import numpy as np 

# Read the Data
bldg_permits = pd.read_csv("D:\\work\\python\\DataClean\\Building_Permits.csv"
                , low_memory=False)

# set seed for reproducibility
np.random.seed(0)

# Find the count of missing values in each Column
missing_values_count = bldg_permits.isnull().sum()

# Print all the columns to know how many values are missing in each column
print(missing_values_count[0:43])

# Find the % of missing data by dividing # of missing cells/ Total Cells
total_cells = np.product(bldg_permits.shape)
total_missing = missing_values_count.sum()
print((total_missing/total_cells) * 100)

# Drop the columns which have atleast 1 missing value
columns_with_na_dropped = bldg_permits.dropna(axis=1)
columns_with_na_dropped.head()
print("Columns in original dataset: %d \n" % bldg_permits.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])

# backfill the columns missing values with the next column value and last column as 0
bldg_permits.fillna(method = 'bfill', axis=0).fillna("0")

print(bldg_permits.sample(5))
