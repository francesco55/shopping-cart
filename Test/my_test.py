import datetime
from app.shopping_cart import to_usd, find_product, timestamp 

def test_timestamp():
     time = datetime.datetime(2020,4,20,21,30,12)
     result = timestamp(time)
     assert result == "09:30 PM"
    
def test_to_usd():
     price = 34903.727
     result = to_usd(price)
     assert result == "$34,903.73"
