# converting data in an .xls file with Python to csv + metadata file
# also transforming the non-datetime values to actualy datetime format

import xlrd
import csv
from numbers import Number
from datetime import datetime

source_workbook = xlrd.open_workbook("data/U6RATE.xls")
source_workbook_metadata = open("data/metadata_U6RATE.txt","w")

for sheet_name in source_workbook.sheet_names(): # an .xls workbook can have multiple sheets

    current_sheet = source_workbook.sheet_by_name(sheet_name)

    output_file = open("xls"+sheet_name+".csv","w")

    output_writer = csv.writer(output_file)
    is_table = False #Boolen to detect when we reach the table-type data

    for row_num, row in enumerate(current_sheet.get_rows()):

        first_entry = current_sheet.row_values(row_num)[0]

        if first_entry == 'observation_date':

            is_table = True
        
        if is_table:

            # extract the table-type data values into separate variables(if we look at the data, there are two columns only)
            the_date_num = current_sheet.row_values(row_num)[0]
            U6_value = current_sheet.row_values(row_num)[1]

            new_row = [the_date_num,U6_value]

            # if the `the_date_num` is a number, then the current row is *not*
            # the header row. We need to transform the date.

            if isinstance(the_date_num,Number):

                the_date_num = xlrd.xldate.xldate_as_datetime(the_date_num,source_workbook.datemode)

                #overwrite the first value in the new row with the reformatted date
                new_row[0] = the_date_num.strftime('%m/%d/%Y')

            output_writer.writerow(new_row)

        else: #the row must be still metadata

            for item in current_sheet.row(row_num):
                #We want the metadata to be correctly formatted
                source_workbook_metadata.write(item.value)
                source_workbook_metadata.write('\t') #separate items with space

            source_workbook_metadata.write('\n') #at the end of each metadata line we write another line

output_file.close()
source_workbook_metadata.close()

