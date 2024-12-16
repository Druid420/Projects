import requests
from bs4 import BeautifulSoup
import re
import json
from collections import defaultdict
from tinydb import TinyDB, Query

db = TinyDB("db.json")
zipcode = input("What zipcode? ")

# Function to fetch and parse gas station data from the website
def getData():

    # Construct the URL for fuel type 1 (regular) 
    # TO DO: Update for ALL fuel types
    url = (f"https://www.gasbuddy.com/home?search={zipcode}&fuel=1&maxAge=0&method=all")

    # Fetch raw HTML content and turn it into parsable HTML using BeautifulSoup
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract gas station names, prices, timestamps, and addresses
    gas_stations = [name.text for name in soup.findAll('a', href=re.compile("/station/"))]

    prices = [price.text for price in soup.findAll('span', class_='text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL')]
    
    time_updated = [time.text for time in soup.findAll('span', class_='ReportedBy-module__postedTime___J5H9Z')]
    
    addresses = [" ".join(address_div.stripped_strings) for address_div in soup.findAll('div', class_='StationDisplay-module__address___2_c7v')]
    
    # for station, price, time, address in zip(gas_stations, prices, time_updated, addresses):
    #     db.insert({"store": station, "price": price, "time_updated": time, "address": address})
    return zip(gas_stations, prices, time_updated, addresses)

def insertData():
    #if the data base is empty then insert data
    if not db.all():
        for station, price, time, address in getData():
            db.insert({"store": station, "price": price, "time_updated": time, "address": address})
    else:
        print("Can't do that! Something's in there!")
def updateData():
    pass


insertData()
print(db.all())
#db.drop_tables()