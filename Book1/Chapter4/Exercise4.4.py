# a example of reading data from a .json file using python

import csv
import json # "json" is a built-in library

filename = "U6_FRED_data"
json_source_file = open("data/"+filename+".json","r")

json_data = json.load(json_source_file)

output_file = open("json_"+filename+".csv","w")
output_writer = csv.writer(output_file)

output_writer.writerow(list(json_data["observations"][0].keys())) # grab the first observation and use its keys as the column headers
                                                                  # we need to convert it to a list because json library interpret it as a dictionary 

for obj in json_data["observations"]: #our target data is a list whose key is "observations"

    #Every object in json_data is a dictionary, but to write it we need to convert each one to a list
    obj_values = []

    for key,value in obj.items():

        obj_values.append(value)
    
    output_writer.writerow(obj_values)

output_file.close()