# HandleMissingValues.py
- Load Data & look for missing values, typically column values as NULL or NaN or None
- Find out which are the columns having at least one missing value & based on it find what % of the data is missing
- Data Intuition – figure out why data is missing and how it would affect analysis
- Imputation – Is the process of guessing missing data based on other values in the row and column
- Handle Missing Data
    - It can be a calculated value from the other values of the row. Example Total Score in a match based on individual scores
    - It can be a referenced value, such as State Name which is missing but can be filled using the State Code and Master data of States
    - Drop Missing values ( either rows or columns)
    - Fill missing values automatically - Copy the data from next available Row-Column into the missing column or fill with 0 or constant value


This Folder is to depict Data Cleaning activities that can be performed using Python