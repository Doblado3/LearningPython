# first time working with regular expresions

import re #regular expresion library

bookend_regex = re.compile(r"\s0[7-9]:")
one_sided_regex = re.compile(r"0[7-9]:") #let's test out this regular expresion
#The difference between the two regex is that, the first one refers only to the hours
#while the second one could match the minutes too

seven_to_ten = re.compile(r"\s0[7-9]:|\s10:")

# this example should *fail*
sample1 = "2020-09-01 00:00:01.0430"

# this example should *match*
sample2 = "2020-09-01 09:04:23.7930"

# this example should *fail*
sample3 = "2020-09-01 10:07:02.0510"

# let's see what happens!
print("bookend_regex:")
#print(bookend_regex.search(sample1))
print(bookend_regex.search(sample2))
#print(bookend_regex.search(sample3))

print("one_sided_regex:")
#print(one_sided_regex.search(sample1))
print(one_sided_regex.search(sample2))
#print(one_sided_regex.search(sample3))

print("seven_to_ten:")
print(seven_to_ten.search(sample3))