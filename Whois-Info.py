import whois
import pandas as pd

def col_whois(domain):
    stripped_domain = domain.strip()
    whois_domain = whois.whois(stripped_domain)
    return list(whois_domain)


# Read the domain.txt file into a DataFrame
domain = pd.read_csv('domain.txt', sep=" ", header=None)

# Apply the strip function to each element in the domain column
domain_stripped = domain[0].apply(lambda x: x.strip())

# Apply the col_whois function to each element in the domain_stripped series
contents_whois = domain_stripped.apply(col_whois)


# print (contents_whois)

user_domain = input("Enter the domain name: ")
user_parameter = input("Enter the parameter: ")
p = whois.whois(user_domain)
user_output = p[user_parameter]
print(user_output)
