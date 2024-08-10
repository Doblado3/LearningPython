# quick script for adding a "fingerprint" column to our loan data, which will
# help us confirm/correct for any typos or inconsistencies in, e.g., bank names

import csv
import fingerprints

ppp_data = open("data/public_150k_plus_recent.csv","r")
ppp_data_reader = csv.DictReader(ppp_data)

augmented_ppp_data = open("data/public_150k_fingerprint.csv","w")
augmented_data_writer = csv.writer(augmented_ppp_data)

header_row = [] #Because we are adding a new column, we need to create a new header row too
# We create it with a for loop instead of writing it by hand, avoiding typos

for item in ppp_data_reader.fieldnames:

    header_row.append(item)

    if item == 'OriginatingLender':

        header_row.append('OriginatingLenderFingerprint')

augmented_data_writer.writerow(header_row) #column names

#we are going to create the agumented row's
for row in ppp_data_reader:

    new_row = []

    for column_name in ppp_data_reader.fieldnames:

        new_row.append(row[column_name]) #first we add the value for the column

        if column_name == 'OriginatingLender':

            fingerprint = fingerprints.generate(row[column_name]) + \
                              " " + row['OriginatingLenderLocationID'] 
            
            new_row.append(fingerprint) #we add the new fingerprint value

    augmented_data_writer.writerow(new_row)

augmented_ppp_data.close()
ppp_data.close()