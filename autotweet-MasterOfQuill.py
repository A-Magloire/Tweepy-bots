def send_tweet(request):

  # IMPORT lIBRARIES
  import tweepy
  import os
  import random
  from os import getenv
  import requests

  # Getting the key and secret codes from my environment variables
  consumer_key = getenv("CONSUMER_KEY")
  consumer_secret = getenv("CONSUMER_SECRET")
  access_token = getenv("ACCESS_TOKEN")
  access_secret = getenv("ACCESS_TOKEN_SECRET")

  # Tweepy's process for setting up authorisation
  client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_secret
  )

# request quote from quote API
  url = "https://quotel-quotes.p.rapidapi.com/quotes/random"

  payload = { "topicIds": [7, 8, 14, 19, 12, 100] }
  headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "e69db01245msh3fe399fbc24296ap1c09dcjsn0f432c2d9f6a",
    "X-RapidAPI-Host": "quotel-quotes.p.rapidapi.com"
  }

  response = requests.post(url, json=payload, headers=headers)

  quote = response.json()['quote']
  author = response.json()['name']

  tweet = f'"{quote}" - {author}'
  print(tweet)

  # Send a tweet
  client.create_tweet(text=tweet)
