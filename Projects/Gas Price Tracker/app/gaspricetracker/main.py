import requests
from bs4 import BeautifulSoup
import re
from tinydb import TinyDB, Query
from dotenv import load_dotenv
import os
from telegram import Bot
import asyncio

load_dotenv()

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
    #runs getData() function then adds any updated data to the database then sends telegram message
    for station, latest_price, address in getData():
      for store_info in db.search(data.id.exists()):
        if (store_info['id'] == station+address) and (latest_price != store_info['price']) and (latest_price != '- - -') :
                # Update data
                db.update({'price': latest_price}, data.id == station+address)
                print(f'Price updated for {station}: {store_info["price"]} --> {latest_price}')
                # Send message
                asyncio.run(send_telegram_message(f'Price updated for {station} at {address}: {store_info["price"]} --> {latest_price}')) 
        else:
            print(f'Price for {station} remained the same: {latest_price}')

# async function runs func while allowing flow on program to continue
async def send_telegram_message(message_content):
    try:
        bot_token = os.getenv("BOT_TOKEN")
        bot = Bot(token=bot_token)
        chat_id = os.getenv("chatId")

        # Send the message asynchronously
        await bot.send_message(chat_id=chat_id, text=message_content)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Failed to send message: {e}")

updateData()