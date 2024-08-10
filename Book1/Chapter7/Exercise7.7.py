# script to merge our PPP loan data with information from the SBA's NAICS size requirements

import pandas as pd

# Leer los datos
ppp_data = pd.read_csv("data/public_150k_fingerprint.csv", dtype='string')
sba_naics_data = pd.read_csv("data/Size_Standards_Effective.csv", dtype='string')

# Reemplazar valores nulos en 'NAICSCode'
ppp_data['NAICSCode'] = ppp_data['NAICSCode'].fillna('None')

# Realizar el merge
merged_data = pd.merge(ppp_data, sba_naics_data, how='left',
                       left_on=['NAICSCode'], right_on=['NAICS Codes'], indicator=True)

# Escribir el archivo combinado con codificación 'utf-8'
merged_data.to_csv("data/merged_fingerprint_naics.csv", index=False, encoding='utf-8')

# Imprimir los valores en la columna '_merge'
print(merged_data['_merge'].value_counts())

# Crear archivo con solo los valores no coincidentes
unmatched_values = merged_data[merged_data['_merge'] == 'left_only']
unmatched_values['NAICSCode'].value_counts().to_csv("data/unmatched_ppp_naics.csv", encoding='utf-8')

