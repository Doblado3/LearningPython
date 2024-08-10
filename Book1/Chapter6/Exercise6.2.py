# reviewing all the column names in the ppp data to see
# what we can infer about them from the data itself

import pandas as pd

ppp_data = pd.read_csv("data/public_150k_plus_recent.csv") #convert all missing entries to NaN, not a number
converted_missing_data = ppp_data.convert_dtypes() #convert all missing data entries to <NA>
transpose_ppp_data = converted_missing_data.transpose()

print(transpose_ppp_data)
