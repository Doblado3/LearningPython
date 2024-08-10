# quick script finding the earliest and the latest dates in the PPP loan data

import pandas as pd

ppp_data = pd.read_csv("data/public_150k_plus_recent.csv") #Leemos el archivo csv y lo guaardamos en una variable

ppp_data['DateApproved'] = pd.to_datetime(ppp_data['DateApproved'], format = '%m/%d/%Y') #Necesitamos convertir las fechas en Date type
                                                                                         #Pasar format como parámetro reduce tiempo de ejecución
print(ppp_data['DateApproved'].min())
print(ppp_data['DateApproved'].max())


# Get the number of rows and columns

num_rows, num_columns = ppp_data.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")
