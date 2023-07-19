import pandas as pd

# Read the CSV file 'whois-db-download-info-sample.csv' into a DataFrame called 'df'
df = pd.read_csv('domain.csv')

print(df)

# Filter the DataFrame 'df' to create a new DataFrame 'df_registrar' containing only rows where the 'registrarName' column is 'GoDaddy.com, LLC'
df_registrar = df[df["registrarName"] == 'GoDaddy.com, LLC']

# Filter the DataFrame 'df' to create a new DataFrame 'df_createdate' containing only rows where the 'createdDate' column is greater than '2015-05-10'
df_createdate = df[df["createdDate"] > '2015-05-10']

# Get the unique values in the 'registrarName' column of the DataFrame 'df' and store them in the 'unique_registrar' variable
unique_registrar = df.registrarName.unique()

# Find duplicate values in the 'registrarName' column of the DataFrame 'df'
duplicates = df['registrarName'].duplicated(keep=False)

# Create a new DataFrame 'df_unique' containing only the rows from 'df' that are not duplicated in the 'registrarName' column
df_unique = df[~duplicates]

# Get the number of rows in the DataFrame 'df' and store it in the 'num_rows' variable
num_rows = len(df)

# Get the number of columns in the DataFrame 'df' and store it in the 'num_cols' variable
num_cols = len(df.columns)
