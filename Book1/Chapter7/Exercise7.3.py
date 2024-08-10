# objectives: filter all January 2020 Citi Bike rides, and output a new
#             file containing only weekday rides

import csv
from datetime import datetime

source_file = open("data/202001-citibike-tripdata_1.csv","r")
output_file = open("data/weekly-citibike-tripdata.csv","w")

citibike_reader = csv.DictReader(source_file)
output_writer = csv.DictWriter(output_file, fieldnames=citibike_reader.fieldnames)
output_writer.writeheader()

for a_row in citibike_reader:

    date = datetime.strptime(a_row['starttime'], "%Y-%m-%d %H:%M:%S.%f") #Passing the format reduces computational time

    if date.weekday() <=4: #Monday is position 0

        output_writer.writerow(a_row)

output_file.close()