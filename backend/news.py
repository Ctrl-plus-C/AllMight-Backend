import requests
import os

def fetch(country):
    countries = {
        'united arab emirates':'ae',
        'uae':'ae',
        "argentina":'ar',
        "austria":'at',
        "australia":'au',
        "belgium":'be',
        "bulgaria":'bg',
        "brazil":'br',
        "canada":'ca',
        "switzerland":'ch',
        "china":'cn',
        "colombia":'co',
        "cuba":'cu',
        "czechia":'cz',
        "germany":'de',
        "egypt":'eg',
        "france":'fr',
        "uk":'gb',
        "great britain":'gb'        ,
        "britain":'gb',
        "united kingdom":'gb',
        "greece":'gr',
        "hong kong":'hk',
        "hungry":'hu',
        "indonesia":'id',
        "ireland":'ie',
        "israel":'il',
        "india":'in',
        "italy":'it',
        "japan":'jp',
        "republic of korea":'kr',
        "korea":"kr",
        "south korea":"kr",
        "lithuania":'lt',
        "latvia":'lv',
        "morocco":'ma',
        "mexio":'mx',
        "malaysia":'my',
        "nigeria":'ng',
        "netherlands":'nl',
        "norway":'no',
        "new zealand":'nz',
        "philippines":'ph',
        "poland":'pl',
        "portugal":'pt',
        "romania":'ro',
        "serbia":'rs',
        "russia":'ru',
        "saudi arabia":"sa",
        "sweden":'se',
        "singapore":'sg',
        "slovenia":'si',
        "slovakia":'sk',
        "thailand":'th',
        "turkey":'tr',
        "taiwan":'tw',
        "ukraine":"ua",
        "usa":"us",
        "us":"us",
        "united states of america":"us",
        "america":"us",
        "venezuela":"ve",
        "south africa":"za",
        "africa":"za"
        }

    if country.lower() not in countries:
        return "Country not Supported..."
    url = ('https://newsapi.org/v2/top-headlines?'
        'country='+countries[country.lower()]+'&'
        'apiKey='+os.environ.get('news_key'))
    response = requests.get(url).json()
    i=0


    while(True):
        news_res = response["articles"][i]["title"]+"\n"
        des = response["articles"][i]['description']
        url = response["articles"][i]['urlToImage']
        if des is not None and url is not None:
            news_res+=des
            return news_res
        i=i+1