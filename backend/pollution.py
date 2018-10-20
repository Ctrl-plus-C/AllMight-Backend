import requests
import os

def pollution11(city):
    data = requests.get("http://api.waqi.info/feed/"+city+"/?token="+os.environ.get('pollution_key')).json()
    pquality = data["data"]["aqi"]
    if(pquality <= 50 ):
        return "Air Pollution Level is Good"
    elif(pquality > 50 and pquality <= 100):
        return "Air Pollution Level is Moderate"
    elif(pquality > 100 and pquality <= 150):
        return "Air Pollution Level is Unhealthy for Sensitive Groups"
    elif(pquality > 150 and pquality <= 200):
        return "Air Pollution Level is Unhealthy"
    elif(pquality > 200 and pquality <= 300):
        return "Air Pollution Level is very Unhealthy"
    elif(pquality > 300):
        return "Air Pollution Level is Hazardous"
    
    return data

# print(bore("new delhi"))