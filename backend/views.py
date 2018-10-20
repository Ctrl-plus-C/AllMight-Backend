from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from wit import Wit
import re
import os
from .translatea import translatefn
from .news import fetch
from .tweet import tweett
import tweepy
from .bored import bore
from .word import words
from .weather import forecast
from .currency import currency_convert
from .quote import quote_generator
from .jokes import random_joke
from .mail import send_mail
from .horoscope import hh
#from  quiz import Question
from .pollution import pollution11

class Command(APIView):
    def __init__(self):
        self.command_list = {
            "Help" : "Always ready to `help`!",
            # "Hey" : ""
            "Bored" : "Try asking me for `Something interesting` or let me know `I'm bored` ",
            "Quote": "Ask me to `Share a quote` or let me `Inspire` you",
            "Joke": "I can `Crack a joke` for you and `Say something funny` to lighten your mood!",
            "Weather" : "`Get the latest weather in New Delhi` or New York or anywhere!!",
            "News": "Let me `fetch the latest news from India` to England and everywhere in between",
            "Translate" : "I can even translate. Try `Translate 'わたし が いつも きた'` P.s. that means I ll always be!",
            "Dictionary":"Ask me the `meaning of life` ",
            "Currency Conversion" : "Convert currencies on the go. Try `Convert 10 USD to INR` or `Currency JPY 5000 - RUB`",        
            "Tweet": "Let me `Tweet a quote`, `Post a joke to Twitter` or simply anything on your mind. Try 'Tweet **AllMight is bestbot**' ;)",
            "Mail" : "Remind someone you love them. Try `Mail 'i love you dad' with subject 'hi dad!' to 'dad@family.com' from 'me@family.com'` Make sure the content comes before the subject and they both are enclosed in inverted commas", 
            "Horoscope": "I believe in science. But horoscopes are fun too! Try `Send my <weekly|monthly|today's> Libra horoscope`",
            "Pollution": "Know the pollution in your area. Try `Pollution in Allahabad` "
        }

    def post(self, request):
        print("AAAAAAAAAA")
        client = Wit(os.environ.get('wit_key'))
        response = ""
        
        resp = client.message(request.data.get('text'))

        command = []
        if "commands" not in resp["entities"]:
            response+="\nHmm... I dont think I quite understand.\nTry checking out help"
            return Response({"success":"hello"},status=status.HTTP_200_OK)
        length = len(resp["entities"]["commands"])
        
        for x in range(length):
            command.append(resp["entities"]["commands"][x]["value"])

        if "help" in command:
            response += self.help()
        elif "tweet" in command:
            if "quote" in command:
                response += self.tweet("quote", " ")
            elif "joke" in command:
                response += self.tweet("joke", " ")
            else:
                sentence = request.data.get('text').split('"')
                if len(sentence) == 3:
                    word = sentence[1]
                    response += self.tweet("this", word)
                else:
                    response += "Try putting the tweet in inverted quotes."                   
        elif "joke" in command:
            response += self.joke()
        elif "quote" in command:
            response += self.quotes()
        elif "bored" in command:
            response += self.bored()
        # elif "quiz" in command:
        #     response +="quiz "
        #     response += self.quiz()
        elif "meaning"in command:
            response += self.word(request.data.get('text'))
        elif "pollution" in command:
            location = resp["entities"]["location"][0]["value"]
            response += self.pollution(location)
        elif "weather" in command:
            location = resp["entities"]['location'][0]["value"]
            response += self.weather(location)
        elif "news" in command:
            location = resp["entities"]["location"][0]["value"]
            response += self.news(location)
        elif "translate" in command:
            sentence = request.data.get('text').split('"')
            if len(sentence) == 3:
                word = sentence[1]
                response += self.translate(word)
            else:
                response += "Try putting the request.data.get('text') to be translated in inverted quotes."
        elif "currency" in command:
            amt = resp["entities"]["amount_of_money"][0]["value"]
            from_curr = resp["entities"]["amount_of_money"][0]["unit"]
            to_curr = resp["entities"]["money_code"][0]["value"]
            response += self.currency(from_curr, to_curr, amt)
        elif "horoscope" in command:
            print(resp)
            timep = resp["entities"]["time"][0]["value"]
            zodiac = resp["entities"]["Zodiac"][0]["value"]
            response += self.horoscope(timep,zodiac)
        elif "mail" in command:
            response +=self.mail(resp,request.data.get('text'))
        # resp
        return Response({"data":response},status=status.HTTP_200_OK)

    def help(self):
        response = "Let me help you!\n\n"
        for c in self.command_list:
            response += c + ": "+ self.command_list[c]+"\n"
        return response

    def translate(self, word):
        return translatefn(word)

    def news(self, city):
        return fetch(city)

    def tweet(self, switch,text):
        return tweett(switch, text)

    def bored(self):
        return bore()

    def word(self, text):
        return words(text)

    def mail(self, resp,text):
        return send_mail(resp,text)

    def weather(self, location):
        return forecast(location)

    # def quiz(self):
    #     q = Question()
    #     q.gen_questions()
    #     return q.print_ques()

    def currency(self, from_c, to_c, amt):
        return currency_convert(from_c, to_c, amt)

    def quotes(self):
        return quote_generator()

    def joke(self):
        return random_joke()

    def horoscope(self, timep, zodiac):
        return hh(timep, zodiac)

    def pollution(self, location):
        return pollution11(location)
