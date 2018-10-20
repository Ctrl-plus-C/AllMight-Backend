import requests
import datetime

def currency_convert(from_c, to_c, amt):
    base = from_c.upper()
    symbols = to_c.upper()
    value = int(amt)
    url = ('https://api.exchangeratesapi.io/latest?base='+base+'&symbols='+symbols)
    response = requests.get(url)
    rate = response.json()["rates"][symbols]
    return("\nConversion Rate: "+str(rate)
        +"\nConverted Amount: "+str(value*rate))