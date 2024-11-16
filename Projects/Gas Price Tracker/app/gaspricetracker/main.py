import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict

def getData():
  #get user zipcode and request fuel type
  zipcode = input("What zipcode? ")
  #fuel_type = input("What fuel type? ")

  #url
  url = (f"https://www.gasbuddy.com/home?search={zipcode}&fuel=1&maxAge=0&method=all")

  # Fetch raw HTML content and turn it into parsable HTML using beautifulsoup
  response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
  soup = BeautifulSoup(response.content, 'html.parser')

  #find gas-station, price, time stamp, & addresses using tag then puts in list
  gas_stations = [name.text for name in soup.findAll('a', href=re.compile("/station/"))]
  prices = [price.text for price in soup.findAll('span', class_='text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL')]
  time_updated = [time.text for time in soup.findAll('span', class_ = 'ReportedBy-module__postedTime___J5H9Z')]

  #gets addresses using findall then splits the div, removing the br/, and joins the two parts of the address
  addresses = [" ".join(address_div.stripped_strings) for address_div in soup.findAll('div', class_ ='StationDisplay-module__address___2_c7v')]

  #initalize a dictionary where the keys are the gas station names and key values are a list of dictionaries
  store_data = defaultdict(list)

  #populate dictionary
  for station, price, time, address in zip(gas_stations, prices, time_updated, addresses):
    store_data[station +" -- "+ address].append([price, time]) #keys are the gas station name PLUS the address for uniqueness

  #return data
  return store_data