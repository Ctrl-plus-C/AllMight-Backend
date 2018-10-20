import tweepy
from .jokes import random_joke
from .quote import quote_generator
import os


def tweett(key, text):
    consumer_key = os.environ.get('consumer_key')
    consumer_secret = os.environ.get('consumer_secret')
    access_token = os.environ.get('access_token')
    access_token_secret = os.environ.get('access_token_secret')
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    # import pdb; pdb.set_trace()
    api = tweepy.API(auth)
    # print(api.status_code)

    status = 0

    if key == 'joke':
        while True:
            joke_gen = random_joke()
            if len(joke_gen)<=139:
                break
        api.update_status(status=joke_gen)
        status = 1
    elif key == 'quote':
        while True:
            quote_gen = quote_generator()
            if len(quote_gen)<=139:
                break
        api.update_status(status=quote_gen)
        status = 2
    elif key == 'this':
        if len(text)>139:
            status = -1
        else:
            api.update_status(status=text)
            status = 3
    
    if status == -1:
        return "Character limit exceeded."
    elif status == 1:
        return "Tweeted joke"
    elif status == 2:
        return "Tweeted quote"
    elif status == 3:
        return "Tweeted"

