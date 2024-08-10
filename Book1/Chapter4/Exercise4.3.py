# The same logic applied in "Exercise1.3.py", but now with a slightly more complex format in the xml file.

import csv
from lxml import etree

filename = "BBC News - Science & Environment XML Feed"
xml_source_file = open("data/"+filename+".xml","rb") 

xml_doc = etree.parse(xml_source_file)
document_root = xml_doc.getroot() 
print(etree.tostring(document_root)) #Now the content is less organized.


if etree.iselement(document_root):
    output_file = open("rss_"+filename+".csv","w")
    output_writer = csv.writer(output_file)

    main_channel = document_root[0] #We save here the channel elemnt
    article_example = main_channel.find("item") #The 'find' method return only the first instance of the element name. Because the element item repeats all along
                                                # we only need the first one to get the columns tags.
    
    tag_list = [] #Empty list where we will store our columns tags.
    for child in article_example.iterdescendants(): #Recorremos los elementos hijos de item
        tag_list.append(child.tag)

        if child.attrib: #if the current tag has any value

            for attrib_name in child.attrib.keys(): #loop through the attribute keys in the tag

                tag_list.append(attrib_name)
    output_writer.writerow(tag_list)
    
    
    #Now that we have the columns headers, we need to iterate through every item element in the file, using "findall()"
    for item in main_channel.findall('item'):

        new_row = []

        for tag in tag_list:

            if item.findtext(tag): #If the element associated with the tag has text value

                new_row.append(item.findtext(tag))
            
            elif tag == "isPermaLink": #otherwise, we check if is the permalink attribute, which tag is guid

                new_row.append(item.find('guid').get("isPermaLink"))

        output_writer.writerow(new_row)

    output_file.close()


