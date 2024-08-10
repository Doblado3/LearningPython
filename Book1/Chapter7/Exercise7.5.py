# an example of reading data from a fixed-width file with Python.

import csv

filename = "data/ghcnd-stations"
source_file = open(filename+".txt","r")

stations_list = source_file.readlines() #converts the txt file to a list of lines

output_file = open(filename+".csv","w")
output_writer = csv.writer(output_file)

headers = ["ID","LATITUDE","LONGITUDE","ELEVATION","STATE","NAME","GSN_FLAG",
           "HCNCRN_FLAG","WMO_ID"] #To know the names, we first need to read the metadata file
output_writer.writerow(headers)

for line in stations_list:

    new_row = []
    #we distinguish the values as position characters
    #strip() allow us to work with the withespace character

      # ID: positions 1-11
    new_row.append((line[0:11]).strip()) 

    # LATITUDE: positions 13-20
    new_row.append((line[12:20]).strip())

    # LONGITUDE: positions 22-30
    new_row.append((line[21:30]).strip())

    # ELEVATION: positions 32-37
    new_row.append((line[31:37]).strip())

    # STATE: positions 39-40
    new_row.append((line[38:40]).strip())

    # NAME: positions 42-71
    new_row.append((line[41:71]).strip())

    # GSN_FLAG: positions 73-75
    new_row.append((line[72:75]).strip())

    # HCNCRN_FLAG: positions 77-79
    new_row.append((line[76:79]).strip())

    # WMO_ID: positions 81-85
    new_row.append((line[80:85]).strip())

    output_writer.writerow(new_row)

output_file.close()

