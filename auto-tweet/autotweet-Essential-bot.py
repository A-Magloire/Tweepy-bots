# The requeset parameter passed into the below function is used for google cloud functions
def send_tweet(request):

  # IMPORT lIBRARIES
  import tweepy
  import os
  import random
  from os import getenv
  import requests
  from currentsapi import CurrentsAPI


  # Getting the key and secret codes from my environment variables
  consumer_key = getenv("CONSUMER_KEY")
  consumer_secret = getenv("CONSUMER_SECRET")
  access_token = getenv("ACCESS_TOKEN")
  access_secret = getenv("ACCESS_TOKEN_SECRET")

  # Tweepy's process for setting up authorisation
  # client = tweepy.Client(
  #   consumer_key=consumer_key,
  #   consumer_secret=consumer_secret,
  #   access_token=access_token,
  #   access_token_secret=access_secret
  # )

# request data from currentsAPI
  api = CurrentsAPI(api_key='vvlaKymy-rdpwfl-jjVOuWKEvlfP6oLawTjKij4CLAfR2Csh')
  api.latest_news()
  response = api.search(category='technology', limit=5)
  
  news = ""
  count = 0
  for item in response['news']:
    if 'title' in item and 'url' in item:
      news += f"{item['title']} Read more: {item['url']}\n" 
      count += 1
      if count == 5:
        break
  
  print(news)

  # Send a tweet
  # client.create_tweet(text=tweet)

