# How many loans have been disbursed

import pandas as pd

ppp_data = pd.read_csv("data/public_150k_plus_recent.csv")

print(ppp_data['LoanStatus'].value_counts())
print(sum(ppp_data['LoanStatus'].value_counts())) #value_counts() will not include NA values

# finding a business within our dataset by (partial) name

ppp_data_named_borrowers = ppp_data[ppp_data['BorrowerName'].notna()] # we create a new dataset without missing 'BorrowerName' column values
                                                                      # pandas cannot search strings within a column with NA values

bankruptcy_example = ppp_data_named_borrowers[ \
                                ppp_data_named_borrowers['BorrowerName']
                                .str.contains('WATERFORD RECEPTIONS')] 

# transposing the result so it's easier to read
print(bankruptcy_example.transpose())

print(sum(ppp_data['LoanStatusDate'].isna())) #Match the number of LoanStatus = Exemption 4


