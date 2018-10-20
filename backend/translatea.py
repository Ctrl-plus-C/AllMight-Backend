import requests
import os

def translatefn(text):
	key = os.environ.get('translation_key')
	url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key="+key+"&text="+text+"&lang=en"
	print("++"+text)
	response = requests.get(url)
	val = response.json()['lang'].upper()+", Translation: "
	ans = ' '.join(response.json()['text'])
	return(val+ans)