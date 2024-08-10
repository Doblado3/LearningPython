#print("Hello World") #Checking all works well

#palabra = "Hello World".split() #Using the split() method and checking what it does
#print(palabra)


#question : How many Citi Bike rides each day are taken by "subscribers" versus "customers"?
#answer : Choose a single day of rides to examine

#program outline: 
    # 1.read in the data file
    # 2.create variables to count
    # 3.for each row in the file:
        #a. if the "usertype" is subscriber, +1 to subscriber_count
        #b. if the "usertype" is customer, +1 to costumer_count
        #c. if the "usertype" is other, +1 to other_count

import csv #Primera vez usando esta librería, es más usada pandas con dataframes directamente

source_file = open("data/JC-202009-citibike-tripdata.csv","r")
citibike_reader = csv.DictReader(source_file) 
print(citibike_reader.fieldnames)

#Let's build the for...in... loop to answer our question


subscriber_count = 0
customer_count = 0
other_count = 0

for r in citibike_reader: #We simply iterate through each row and check it's value at "usertype" column. Then, add 1 to the correct counter
    if r["usertype"] == "Subscriber":
        subscriber_count = subscriber_count + 1
    elif r["usertype"] == "Customer":
        customer_count = customer_count + 1
    else:
        other_count = other_count + 1
    

print("Number of Subscriber users :")
print(subscriber_count)
print("Number of Costumer users :")
print(customer_count)
print("Number of Other users :")
print(other_count)


