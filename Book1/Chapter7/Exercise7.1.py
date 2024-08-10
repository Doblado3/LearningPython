# objectives: filter all September 2020 Citi Bike rides, and output a new
#             file containing only the rides from 2020-09-01

import csv

with open("data/202001-citibike-tripdata_1.csv", "r") as source_file:
    with open("data/202001-citibike-tripdata_filtered.csv", "w", newline='') as output_file:
        citibike_reader = csv.DictReader(source_file)
        output_writer = csv.DictWriter(output_file, fieldnames=citibike_reader.fieldnames)
        output_writer.writeheader()

        for a_row in citibike_reader:
            start_timestamp = a_row['starttime']
            date, time = start_timestamp.split(" ")
            
            if date == "2020-01-01":
                output_writer.writerow(a_row)

