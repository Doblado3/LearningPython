# How to import, when you stored it correctly, your API credentials with Python

import requests
from FRED_credentials import my_api_key

complete_data_url = "https://api.stlouisfed.org/fred/series/observations?&series_id=U6RATE&file_type=json&api_key="+my_api_key

FRED_output_file = open("FRED_API_data.json","w")
FRED_data = requests.get(complete_data_url)

FRED_output_file.write(FRED_data.text)
FRED_output_file.close()