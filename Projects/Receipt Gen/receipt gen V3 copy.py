import random
import math
import datetime
import tkinter as tk

#  List of item names and prices
items = [
   ("Totino's Pizza Rolls", 9.99)]

# Function to generate a random item


def get_random_item():
    return random.choice(items)


# Initialize the date_string with the current date and time
now = datetime.datetime.now()
date_string = now.strftime("%m/%d/%Y %I:%M %p")

# Function to generate a receipt


def generate_receipt():
    # Choose a random store name
    store_names = ["Sam's Club Altoona", "Walmart", "Wegmans", "Walgreens"]
    store_name = random.choice(store_names)
    item_count = random.randint(1, 6)

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

    # Calculate a random date and time within the last 12 days
    days_offset = random.randint(1, 12)
    random_date = now - datetime.timedelta(days=days_offset)
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
