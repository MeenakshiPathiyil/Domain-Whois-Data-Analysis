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


def values_whois(domain):
    stripped_domain = domain.strip()
    whois_domain = whois.whois(stripped_domain)
    return list(whois_domain.values())


content_whois = domain_stripped.apply(values_whois)

length = len(domain_stripped)
i = 0
while i < length:
    df.loc[i] = content_whois[i]
    i += 1

country_df = df[df["country"] == 'US']
registrar_df = df[df["registrar"] == 'CSC CORPORATE DOMAINS, INC.']
