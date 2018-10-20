import requests

def random_joke():
    data = requests.get('https://api.yomomma.info/').json()["joke"]
    return data