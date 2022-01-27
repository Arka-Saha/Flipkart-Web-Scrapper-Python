# Code for python (to be run in IDE)

from bs4 import BeautifulSoup
import re, requests
import pandas as pd

item_names = []
item_prices = []
item_images = []

print('Provide URL of only products like, Phones, Laptops etc, which have 24 products displayed in a page! Below are certain such URLs')

def get_name():
    for i in soup.find_all('div', class_='_4rR01T'):
        name = re.sub('^<div.*">|</div>', '', str(i))
        item_names.append(name)
    #print(len(item_names))

def get_price():
    for i in soup.find_all('div', class_='_30jeq3 _1_WHN1'):
        price = re.sub('^<div.*">|</div>', '', str(i))
        item_prices.append(price)
    #print(item_prices)

def get_image():
    for i in soup.find_all('img', class_='_396cs4 _3exPp9'):
        img = re.sub('^<img.*src="|"/>', '', str(i))
        item_images.append(img)
#     print(len(item_images))

# URL = "https://www.flipkart.com/search?q=mobile+phone+android&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobile+phone+android%7CMobiles&requestId=b5c365fc-51e9-40fb-b129-7758b44723cc&as-searchtext=mobile%20phone"
# URL = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
URL = input("Enter Url: ")
response = requests.get(URL)
#print(response.status_code)
soup = BeautifulSoup(response.content, 'lxml')
#print(soup)

get_name()
get_price()
get_image()

df = pd.DataFrame({"Product Name" : item_names,
                   "Product Price" : item_prices,
                   "Product Image" : item_images})

# display the result table in Jupyter notebook
# df.head()

# save result as excel file
df.to_excel('flipkart_products.xlsx')
