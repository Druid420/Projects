import requests
from bs4 import BeautifulSoup
import re
import json
import time
from collections import defaultdict

# Function to load previous data from a JSON file
def load_previous_data():
    try:
        with open("previous_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return empty if no previous data exists

# Function to save current data to a JSON file
def save_current_data(store_data):
    with open("previous_data.json", "w") as file:
        json.dump(store_data, file, indent=4)

# Function to compare and detect price changes
def compare_prices(old_data, new_data):
    changes = {}
    for station, new_price_info in new_data.items():
        if station in old_data:
            old_price_info = old_data[station]
            if new_price_info[0] != old_price_info[0]:  # Compare prices
                changes[station] = {"old_price": old_price_info[0], "new_price": new_price_info[0]}
    return changes

# Function to fetch and parse gas station data from the website
def getData():
    zipcode = input("What zipcode? ")

    # Construct the URL
    url = (f"https://www.gasbuddy.com/home?search={zipcode}&fuel=1&maxAge=0&method=all")

    # Fetch raw HTML content and turn it into parsable HTML using BeautifulSoup
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract gas station names, prices, timestamps, and addresses
    gas_stations = [name.text for name in soup.findAll('a', href=re.compile("/station/"))]
    prices = [price.text for price in soup.findAll('span', class_='text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL')]
    time_updated = [time.text for time in soup.findAll('span', class_='ReportedBy-module__postedTime___J5H9Z')]
    addresses = [" ".join(address_div.stripped_strings) for address_div in soup.findAll('div', class_='StationDisplay-module__address___2_c7v')]

    # Initialize a dictionary where the keys are gas station names and addresses, and the values are price and timestamp
    store_data = defaultdict(list)

    # Populate the dictionary
    for station, price, time, address in zip(gas_stations, prices, time_updated, addresses):
        store_data[station + " -- " + address].append([price, time])

    return store_data

# Main loop to run the script every minute and detect price changes
def run_script():

    while True:
        previous_data = load_previous_data()  # Load previous data
        current_data = getData()  # Get the current data

        # Compare the old and new data to detect price changes
        price_changes = compare_prices(previous_data, current_data)
        if price_changes:
            print("Price changes detected:")
            for station, change in price_changes.items():
                print(f"{station}: {change['old_price']} -> {change['new_price']}")

        # Save the current data for the next iteration
        save_current_data(current_data)

        # Wait for 60 seconds before running again
        time.sleep(60)

# Start the script
if __name__ == "__main__":
    run_script()