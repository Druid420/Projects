import requests
from bs4 import BeautifulSoup
import re

#get user zipcode and request fuel type
zipcode = input("What zipcode? ")
#fuel_type = input("What fuel type? ")

#url
url = (f"https://www.gasbuddy.com/home?search={zipcode}&fuel=1&maxAge=0&method=all")
html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})

soup = BeautifulSoup(html.content, 'html.parser')

#find all a tags with gas station names
station_names = [name.text for name in soup.findAll('a', href=re.compile("/station/"))]

print(station_names)