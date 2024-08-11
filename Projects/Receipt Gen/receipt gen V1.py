import random
import math
import datetime


# List of fake item names and prices
items = [
    ("Old El Paso Taco Shells", 10.99), ("Old El Paso Salsa", 6.99),
    ("Old El Paso Chili Powder", 3.99), ("Old El Paso Taco Seasoning", 5.99),
    ("Old El Paso Refried Beans", 8.99), ("Old El Paso Enchilada Sauce", 5.99),
    ("Gatorade Frost Thirst Quencher", 1.99),
    ("Gatorade Fierce Thirst Quencher", 1.99),
    ("Gatorade X-Factor Thirst Quencher", 1.99), ("Snickers Bar", 1.19),
    ("Skittles Original Fruit Candy", 1.79), ("Pepsi Cola", 1.99),
    ("Mountain Dew", 1.99), ("Lays Classic Potato Chips", 1.99),
    ("Doritos Nacho Cheese Chips", 1.99),
    ("Cheetos Crunchy Cheese Snacks", 1.99), ("Tostitos Scoops!", 1.99),
    ("Dove Men+Care Body and Face Bar", 1.99),
    ("Starbucks Mocha Frappuccino", 3.99),
    ("Ruffles Original Potato Chips", 1.99),
    ("Gatorade Zero Sugar Thirst Quencher", 1.99),
    ("Gatorade Zero Sugar Thirst Quencher with Protein", 5.29),
    ("Gatorade Zero Sugar Thirst Quencher with Protein and Electrolytes", 5.29),
    ("Gatorade Zero Sugar Thirst Quencher with Protein and Electrolytes and Vitamins",
     5.29), ("M&M's", 9.00), ("Snickers", 9.00), ("Skittles", 9.00), ("SheaMoisture Natural Infusions Moisture Shampoo", 10.00),
    ("Conditioner at Costco",
     10.00), ("Lahli Morning Protein Bites, Spinach Rustica (25.1 oz.)", 10.88),
    ("Rubbermaid Brilliance Food Storage Containers, 36 Piece Variety Set", 69.98)
]
# List of store names
store_names = ["Walmart Altoona", "Walgreens",
               "Sam's Club Altoona", "Target", "Costco"]


# Function to generate a random item
def get_random_item():
    return random.choice(items)


# Function to generate a receipt
def generate_receipt():
    # Choose a random store name
    store_name = random.choice(store_names)
    # Set the store name and the number of items on the receipt
    item_count = random.randint(1, 6)

    # Calculate the subtotal and tax rate
    subtotal = 0
    tax_rate = 0.06

    # Create an empty list to store the items on the receipt
    receipt_items = []

    # Generate the items for the receipt
    for i in range(item_count):
        item_name, item_price = get_random_item()
        item_price = round(item_price, 2)
        subtotal += item_price
        subtotal = round(subtotal, 2)
        receipt_items.append((item_name, item_price))

    # Calculate the tax and total
    tax = math.ceil(subtotal * tax_rate * 100) / 100
    total = math.ceil((subtotal + tax) * 100) / 100

    # Get the current date and time
    now = datetime.datetime.now()
    date_string = now.strftime("%m/%d/%Y %I:%M %p")

    # Print the receipt
    print("\033[1m" + store_name +
          " Receipt\033[0m")  # The \033[1m and \033[0m codes make the text bold
    print("----------------")
    print("Date: " + date_string)
    print("----------------")
    for item in receipt_items:
        print("Item: " + item[0])
        print("Price: $" + str(item[1]))
        print("----------------")
    print("Subtotal: $" + str(subtotal))
    print("Tax: $" + str(tax))
    print("Total: $" + str(total))
    print("----------------")
    print("Thank you for shopping at " + store_name + "!")


# Generate a receipt
generate_receipt()
