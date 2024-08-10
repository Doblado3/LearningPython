# quick script for determining whether there are typos &c. in any of the PPP
# loan data's bank names

import pandas as pd
import fingerprints

ppp_data = pd.read_csv("data/public_150k_plus_recent.csv")

unique_names = ppp_data['OriginatingLender'].unique() # This creates a list of unique bank names
print(len(unique_names))

fingerprint_list = []

for name in unique_names:

    fingerprint_list.append(fingerprints.generate(name))

fingerprints_set = set(fingerprint_list)
print(len(fingerprints_set)) 

# The length difference between the two lists certainly suggests 
# that there are some spelling discrepancies in our dataset