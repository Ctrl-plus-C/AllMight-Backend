import requests

def bore():
    data = requests.get("https://www.boredapi.com/api/activity/").json()
    return data["activity"]