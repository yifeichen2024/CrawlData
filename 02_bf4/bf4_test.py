from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com/"

content = requests.get(url).text

soup = BeautifulSoup(content, "html.parser")
# Extract price 
all_price = soup.find_all("p", attrs={"class" : "price_color"})
for price in all_price:
    print(price.string[2:])

all_title = soup.findAll("h3")
for titles in all_title:
    link = titles.find("a")
    print(link.string)