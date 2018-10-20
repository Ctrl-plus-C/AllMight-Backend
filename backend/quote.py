import requests

def quote_generator():
    data = requests.get("https://talaikis.com/api/quotes/random/").json()
    return data.get("quote") + "\n -- By " + data.get("author")
