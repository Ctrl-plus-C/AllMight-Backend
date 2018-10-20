import requests
import os
# cdcO

def forecast(city):
    url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric'+'&APPID='+os.environ.get('weather_key'))
    response = requests.get(url)
    obj = response.json()["main"]
    #icon = response.json()["weather"]["description"]
    return("\nCurrent: "+str(obj["temp"])
        +"\nMin: "+str(obj["temp_min"])
        +"\nMax: "+str(obj["temp_max"])
        +"\nHum: "+str(obj["humidity"]))