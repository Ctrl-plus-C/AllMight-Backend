import requests

def hh(var11,zodiac):
    
    z_list = ["aries","leo","sagittarius","taurus","virgo","capricon","gemini","libra","aquarius","cancer","scorpio","pisces"]
    if zodiac.lower() not in z_list:
        return "Such Zodiac doesn't exist!!"
    
    var_list = ["today","week","month"]
    if var11.lower() not in var_list:
        return "I can find your horoscope for 'today', this 'week' or 'month'"

    url = "http://horoscope-api.herokuapp.com/horoscope/"+var11+"/"+zodiac
    data = requests.get(url).json()["horoscope"]

    # print(data)
    return data