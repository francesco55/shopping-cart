import datetime
import pytest
from app.shopping_cart import to_usd, find_product, timestamp 


def test_timestamp():
     # we cannot test datetime with the .now() functin so I test for a specified time
     # program should output in the format "09:30 PM", rounding seconds and in 12 hour format
     time = datetime.datetime(2020,4,20,21,30,12)
     result = timestamp(time)
     assert result == "09:30 PM"
    
def test_to_usd():
     #tests that to_usd() creates a string from a float that does the following:
     #         1) converts to two decimals
     #         2) includes commas for thousands place
     #         3) includes dollar sign
     price = 34903.727
     result = to_usd(price)
     assert result == "$34,903.73"

# consulted https://github.com/s2t2/shopping-cart-screencast/blob/testing/shopping_cart_test.py
def test_find_product():
     # tests the find_product()
     products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99}
     ]

     # this assertion tests if find_product() returns the correct dictionary for a given id in a list of dictionaries
     matching_product = find_product("1", products)
     assert matching_product["aisle"] == "cookies cakes"     

     # tests for error if invalid id number is passed as argument into find_product()
     with pytest.raises(IndexError):
          find_product("2345", products)
