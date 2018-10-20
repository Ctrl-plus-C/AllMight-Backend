# import requests
# import json
# import os

# def words(word_s):
#     app_id = os.environ.get('word_id')
#     app_key = os.environ.get('word_key')

#     language = 'en'
#     word_id = word_s

#     url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '?q=' + word_id.lower() + '&prefix=false'

#     r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key}).json()
#     mylist = []
#     # print(r["results"])
#     for w in r["results"]:
#         # print(w)
#         mylist.append(w["word"])
    
#     a = ' '.join(mylist)
#     # print(a)
#     return a

# # def main():
# #     # words()
# #     print(words())

# # main()
# # print("code {}\n".format(r.status_code))
# # print("text \n" + r.text)
# # # print("json \n" + json.dumps(r.json()))

from PyDictionary import PyDictionary

def words(sentence):
    dictionary = PyDictionary()
    text = sentence.split('"')[1]
    res_m = dictionary.meaning(text)
    result = "\n"+text.upper()
    if res_m == None:
        return "Are you sure you entered the right word?"
    for x in res_m:
        y = ""
        y = y.join(res_m[x])
        result += "\n+ "+x+": "+y
    return result

# print(words('I want meaning of "pretty"'))