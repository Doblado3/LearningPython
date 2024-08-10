# a basic example of downloading data from the web with Python
# the source data we are downloading will come from the following URLs:
# http://feeds.bbci.co.uk/news/science_and_environment/rss.xml
# https://gbfs.citibikenyc.com/gbfs/en/station_status.json

import requests # a library which allow us to write Python code that act as a web browser

XMLfilename = "BBC_RSS.xml"
xml_output_file = open(XMLfilename,"w")
xml_data = requests.get("http://feeds.bbci.co.uk/news/science_and_environment/rss.xml") #Guardamos los datos en una variable

xml_output_file.write(xml_data.text) #Dentro de la variable anterior, la información se guarda como propiedad "text"
xml_output_file.close() #Muy sencillo

#Aplicamos exáctamente la misma lógica para el JSON

JSONfilename = "citibikenyc_station_status.json"
json_output_file = open(JSONfilename,"w")
json_data = requests.get("https://gbfs.citibikenyc.com/gbfs/en/station_status.json")

json_output_file.write(json_data.text)
json_output_file.close()

# We will overwrite the latest data executing this code each time.
