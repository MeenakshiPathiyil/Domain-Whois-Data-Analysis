import whois
import pandas as pd


def keys_whois(domain):
    stripped_domain = domain.strip()
    whois_domain = whois.whois(stripped_domain)
    return list(whois_domain.keys())


# Read the domain.txt file into a DataFrame
domain = pd.read_csv('domain.txt', sep=" ", header=None)

# Apply the strip function to each element in the domain column
domain_stripped = domain[0].apply(lambda x: x.strip())

# Apply the col_whois function to each element in the domain_stripped series
contents_whois = domain_stripped.apply(keys_whois)

df = pd.DataFrame(columns=contents_whois[0], dtype=object)

# print (df)

# Define a function to retrieve values from WHOIS for a given domain
def values_whois(domain):
    stripped_domain = domain.strip()  # Remove leading and trailing whitespace from the domain
    whois_domain = whois.whois(stripped_domain)  # Perform WHOIS lookup for the domain
    return list(whois_domain.values())  # Return a list of WHOIS values

# Apply the 'values_whois' function to each domain in the 'domain_stripped' list
content_whois = domain_stripped.apply(values_whois)

# Get the length of the 'domain_stripped' list
length = len(domain_stripped)

i = 0

# Iterate through each index 'i' until the end of the list
while i < length:
    df.loc[i] = content_whois[i]  # Assign the WHOIS values to the corresponding row in the DataFrame 'df'
    i += 1  # Increment the counter variable

# Filter the DataFrame 'df' to create a new DataFrame 'country_df' containing only rows where the 'country' column is 'US'
country_df = df[df["country"] == 'US']

# Filter the DataFrame 'df' to create a new DataFrame 'registrar_df' containing only rows where the 'registrar' column is 'CSC CORPORATE DOMAINS, INC.'
registrar_df = df[df["registrar"] == 'CSC CORPORATE DOMAINS, INC.']
