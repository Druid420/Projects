import random
import math
import datetime
import tkinter as tk

#  List of item names and prices
items = [
    ("Old El Paso Taco Shells", 6.00), ("Old El Paso Sause", 6.00),
    ("Old El Paso Chili Powder", 6.00), ("Old El Paso Taco Seasoning", 6.00),
    ("Old El Paso Refried Beans", 6.00), ("Old El Paso Enchilada Sauce", 6.00),
    ("Gatorade Frost Thirst Quencher", 1.99),
    ("Gatorade Fierce Thirst Quencher", 1.99),
    ("Gatorade X-Factor Thirst Quencher", 1.99), ("Snickers Bar", 3.99),
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
    ("Tyson Chicken Tenders", 7.99), ("Tyson Chicken Nuggets", 6.99),
    ("Jimmy Dean Breakfast Sausage", 3.99), ("Jimmy Dean Bacon", 4.99),
    ("State Fair Corn Dogs", 5.99), ("Tyson Any'tizers Chicken Wings", 8.99),
    ("Tyson Crispy Chicken Strips", 6.49), ("Jimmy Dean Pancakes & Sausage", 5.49),
    ("Jimmy Dean Delights Turkey Sausage",
     4.99), ("State Fair Mini Corn Dogs", 4.49),
    ("Tyson Grilled & Ready Chicken Breast Strips", 7.99), ("Jimmy Dean Delights Bacon", 5.99), ("Totino's Pizza Rolls", 9.99), ("Totino's Party Pizza Pack", 9.99),
    ("Tostitos Chips", 9.99), ("Tostitos Cheese Dip", 9.99), ("Tostitos Salsa Dip", 9.99), ("Axe Face Care", 9.99),     ("Dove Men+Care Face Care", 3.99),
    ("Dove Beauty Cream Bar", 2.49), ("Axe Body Spray", 4.99), ("Lipton Green Tea", 3.79), ("Lipton Black Tea", 2.99), ("Hellmann's Mayonnaise", 2.29),
    ("Vaseline Intensive Care Lotion", 4.49), ("Tresemme Shampoo", 5.99), ("Tresemme Conditioner", 5.99), ("Suave Essentials Shampoo", 1.99), 
    ("Suave Essentials Conditioner", 1.99), ("Knorr Chicken Bouillon Cubes", 3.49), ("Knorr Tomato Bouillon with Chicken Flavor", 3.49), ("Breyers Ice Cream", 4.79),
    ("Ben & Jerry's Ice Cream", 5.49), ("Q-tips Cotton Swabs", 2.99)]

# Function to generate a random item


def get_random_item():
    return random.choice(items)




# Function to generate a receipt


def generate_receipt():
    # Choose a random store name
    store_names = ["Walmart Altoona", "Walgreens",
                   "Sam's Club Altoona", "Costco"]
    store_name = random.choice(store_names)
    item_count = random.randint(1, 5)

    # Calculate the subtotal and tax rate
    subtotal = 0
    tax_rate = 0.07

    # Create an empty list to store the items on the receipt
    receipt_items = []

    # Generate the items for the receipt
    for i in range(item_count):
        item_name, item_price = get_random_item()
        subtotal += item_price
        receipt_items.append((item_name, item_price))

    # Calculate the tax and total
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)
    subtotal = round(subtotal, 2)  # Round the subtotal to two decimal places

    # Calculate a random date and time within the last 13 days
    now = datetime.datetime.now()
    days_offset = random.randint(1, 13)
    random_date = now - datetime.timedelta(days=days_offset)

    # Generate random hours, minutes, and seconds
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    random_seconds = random.randint(0, 59)

    random_date = random_date.replace(hour=random_hours, minute=random_minutes, second=random_seconds)

    date_string = random_date.strftime("%m/%d/%Y %I:%M %p")

    # Build the receipt content as a string
    receipt_content = []
    receipt_content.append(store_name + " Receipt")
    receipt_content.append("----------------")
    receipt_content.append("Date: " + date_string)
    receipt_content.append("----------------")
    for item in receipt_items:
        receipt_content.append(item[0])
        receipt_content.append("Price: " + "${:.2f}".format(item[1]))
        receipt_content.append("----------------")
    receipt_content.append("Subtotal: " + "${:.2f}".format(subtotal))
    receipt_content.append("Tax: " + "${:.2f}".format(tax))
    receipt_content.append("Total: " + "${:.2f}".format(total))
    receipt_content.append("----------------")
    receipt_content.append("Thank you for shopping at " + store_name + "!")

    # Update the Text widget with the new receipt content
    receipt_text.delete("1.0", tk.END)  # Clear the existing content
    receipt_text.insert(tk.END, "\n".join(receipt_content))


# Create a GUI window to display the receipt
receipt_window = tk.Tk()
receipt_window.title("Receipt")

# Create a Text widget to display the receipt content
receipt_text = tk.Text(receipt_window, wrap=tk.WORD, font=('Helvetica', 14))
receipt_text.pack()

# Create a button to generate another receipt
generate_another_button = tk.Button(
    receipt_window, text="Generate Another Receipt", command=generate_receipt)
generate_another_button.pack(side=tk.RIGHT, padx=10)

# Generate the initial receipt when the script is run
generate_receipt()

# Start the GUI main loop
receipt_window.mainloop()
