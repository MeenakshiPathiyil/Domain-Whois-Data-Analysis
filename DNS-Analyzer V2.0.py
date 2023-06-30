import pandas as pd

df = pd.read_csv('whois-db-download-info-sample.csv')

df_registrar = df[df["registrarName"] == 'GoDaddy.com, LLC']

df_createdate = df[df["createdDate"] > '2015-05-10']

unique_registrar = df.registrarName.unique()

duplicates = df['registrarName'].duplicated(keep=False)
df_unique = df[~duplicates]

num_rows = len(df)
num_cols = len(df.columns)