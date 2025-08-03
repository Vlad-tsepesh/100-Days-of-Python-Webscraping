import requests
from bs4 import BeautifulSoup

from db.rental_db import RentalDB

url = "https://appbrewery.github.io/Zillow-Clone/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

table_name = soup.select_one("div.result-list-container > div > h1").text.strip().replace(" ", "_")
# print(table_name)
db_name = "rental"
db = RentalDB(db_name, table_name)
results = soup.select("div.result-list-container > ul > li")
for i, result in enumerate(results):
    ID = i+1
    address = result.select_one("address").text.strip()
    price = result.select_one("div > span").text.strip().split("+")[0].split("/")[0]
    link = result.select_one("a").get("href")

    db.insert_data(id=ID, address=address, price=price, link=link)