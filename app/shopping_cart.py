# shopping_cart.py

import datetime
import os
from dotenv import load_dotenv #https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/dotenv.md

load_dotenv()

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    
    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"


def timestamp(time):
    """
    this function takes in an argument variable of datetime type 
    
    returns a user-friendly string such as "09:30 PM"
    """
    return time.strftime("%I:%M %p")

def find_product(selected_id, products):
    """
    this function takes an id number as a string and a list of dictionaries in the format of "products" as arguments
    
    this function returns the id number if it matches the id value of an element of the list
    """ 
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product= matching_products[0]
    return matching_product


subtotal_price = 0
selected_ids = []
all_ids = [str(products["id"]) for products in products] #https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/lists.md

if __name__ == "__main__":

    # INPUT PRODUCTS
    while True:
        selected_id = input("Please input a product ID, type 'DONE' if you are finished inputting products: ")
        id_in = selected_id in all_ids
        if selected_id.upper() == "DONE":
            break
        elif id_in == False:
            print("Error: the ID you typed in is not in the list of products.")
        else:
            selected_ids.append(selected_id)

    # GENERATE RECEIPT
    print("---------------------------------")
    print("Francesco's Market")
    print("WWW.Cesco-Market.COM")
    print("---------------------------------")
    date = datetime.date.today()
    time = datetime.datetime.now()
    print(f"CHECKOUT AT: ", date, timestamp(time)) #https://stackabuse.com/how-to-format-dates-in-python/
    print("---------------------------------")
    print("Selected Products: ")

    #OUTPUT ALL PRODUCTS & CALCULATE COST

    #following for loop: https://www.youtube.com/watch?v=3BaGb-1cIr0&feature=youtu.be
    for selected_id in selected_ids:
        matching_product = find_product(selected_id, products)
        subtotal_price= subtotal_price + matching_product["price"]
        print(" ... " + matching_product["name"] + "(" + to_usd(matching_product["price"]) + ")")

    print("---------------------------------")
    print("SUBTOTAL: " + to_usd(subtotal_price))
    tax_rate = float(os.getenv("tax_rate", default = ".0875")) #https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/modules/os.md
    nominal_tax = tax_rate * subtotal_price
    total_price = subtotal_price + nominal_tax
    print("TAX: " + to_usd(nominal_tax))
    print("TOTAL: " + to_usd(total_price))
    print("---------------------------------")
    print("THANKS, SEE YOU AGAIN SOON!")
    print("---------------------------------")