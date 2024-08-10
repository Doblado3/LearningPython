# an example of reading data from an .xml file with Python, using the "lxml" library. Writing it then as an csv file with "csv" library
#"Conversión de un archivo xml feed-based type a un archivo csv file.based type"
import csv
from lxml import etree

filename = "U6_FRED_data"
xml_source_file = open("data/"+filename+".xml","rb") # rb = read bytes, as lxml library expects bytes, not text

xml_doc = etree.parse(xml_source_file)
document_root = xml_doc.getroot() #Obtenemos la etiqueta raíz del archivo xml.
print(etree.tostring(document_root)) # Print the root tag means printing all the information stored in the xml file


#if etree.iselement(document_root):
#    output_file = open("xml_"+filename+".csv","w")
#    output_writer = csv.writer(output_file)
#    output_writer.writerow(document_root[0].attrib.keys()) #Nos quedamos con las claves de la etiqueta raíz como nombres de las columnas, attrib hace las de dict type
#
#    for child in document_root: #the xlml library converts xml elements to list
#        output_writer.writerow(child.attrib.values()) #Rellenamos las filas con los respectivos valores
#
#    output_file.close()