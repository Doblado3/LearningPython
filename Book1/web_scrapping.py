# how to scrape a web page
# we need to find the tag of the data we want to extract
import requests
from bs4 import BeautifulSoup
import pandas as pd


current_page = 1

data = []

proceed = True

while(proceed):

    url = "https://books.toscrape.com/catalogue/page-"+str(current_page)+".html" #We get the url of the web page we want to scrap
    headers = {
                  'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13597.66.0) ' +
                  'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                  'Chrome/88.0.4324.109 Safari/537.36 Brave/88.1.19.86',
                  'From': 'Pablo Doblado Mendoza - pablodoza11@gmail.com'
             }  # This is data the website owner will be able to see in their server logs.

    page = requests.get(url,headers=headers)
    #print(page.text)
    soup = BeautifulSoup(page.text,"html.parser")

    if soup.title.text == "404 Not Found":

        proceed = False
    else:

        all_books = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3") #li class of the books items in the web

        for book in all_books: #Here you select your attributes

            item = {}

            item['Title'] = book.find("img").attrs["alt"]

            item['Link'] = book.find('a').attrs['href']

            item['Price'] = book.find('p',class_='price_color').text[2:] #You may need to print the items and see how they look to clean them a little

            data.append(item)
        
    current_page +=  1

df = pd.DataFrame(data)
df.to_csv("scrap_example.csv") #pandas csv's are a bit different to the csv library one's