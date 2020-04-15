import datetime
import pytest
from app.shopping_cart import to_usd, find_product, timestamp 

def test_timestamp():
     time = datetime.datetime(2020,4,20,21,30,12)
     result = timestamp(time)
     assert result == "09:30 PM"
    
def test_to_usd():
     price = 34903.727
     result = to_usd(price)
     assert result == "$34,903.73"

#consulted https://github.com/s2t2/shopping-cart-screencast/blob/testing/shopping_cart_test.py
def test_find_product():
     products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99}
     ]

     matching_product = find_product("1", products)
     assert matching_product["aisle"] == "cookies cakes"     

     with pytest.raises(IndexError):
          find_product("2345", products)
