# checking for the compliteness of the different columns

import pandas as pd

ppp_data = pd.read_csv("data/public_150k_plus_recent.csv")

print(ppp_data.value_counts('LoanStatus')) 
print(sum(ppp_data.value_counts('LoanStatus'))) 

print("----------------------------------")

print(ppp_data.value_counts('Gender')) 
print(sum(ppp_data.value_counts('Gender'))) 

print(ppp_data['BorrowerAddress'].isna().sum())

# Figuring out if the range of loan's money is correct
print(ppp_data['CurrentApprovalAmount'].min())
print(ppp_data['CurrentApprovalAmount'].max())