import datetime
from app.shopping_cart import timestamp

def test_timestamp():
     time = datetime.datetime(2020,4,20,21,30,12)
     result = timestamp(time)
     assert result == "09:30 PM"
    

    ## test