import requests
from bs4 import BeautifulSoup
import re
from tinydb import TinyDB, Query

db = TinyDB("db.json")
zipcode = 21502
data = Query()

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
    
    #time_updated = [time.text for time in soup.findAll('span', class_='ReportedBy-module__postedTime___J5H9Z')]
    
    addresses = [" ".join(address_div.stripped_strings) for address_div in soup.findAll('div', class_='StationDisplay-module__address___2_c7v')]
    

    print("Successfully retreived Data!")
    return zip(gas_stations, prices, addresses)

def insertData():
    #if the data base is empty then insert data
    if not db.all():
        db.drop_tables()
        for station, price, address in getData():
            db.insert({"id": station+address, "name": station, "price": price, "address": address})
    else:
        print("Can't do that! Something's in there!")
        
def updateData():
    for station, latest_price, address in getData():
      for store_info in db.search(data.id.exists()):
          if store_info['id'] == station+address:
              if latest_price != store_info['price']:
                  db.update({'price': latest_price}, data.id == station+address)
                  print(f'Price updated for {station}: {store_info["price"]} --> {latest_price}')
              else:
                  print(f'Price for {station} remained the same: {latest_price}')

def sendMessage():
    msg = EmailMessage()
    msg.set_content('lets get a bag.')

    msg['From'] = senderEmail # 'email@address.com'
    msg['To'] = gatewayAddress  # '1112223333@vmobl.com'
    msg['Subject'] = 'Finance Family'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail, appKey)

    server.send_message(msg)
    server.quit()
updateData()