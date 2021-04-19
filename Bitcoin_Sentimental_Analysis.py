# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:24:27 2021

@author: vaidik
"""

#ENVIRONMENT NAME: sentimental_analysis
import tweepy
import textblob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

keys = open('Twitter_Keys.txt', 'r').read().splitlines()

api_key = keys[0]
secret_key = keys[1]
access_tocken = keys[2]
secret_access_token = keys[3]
#print(api, secret_key)

authenticator = tweepy.OAuthHandler(api_key, secret_key)
authenticator.set_access_token(access_tocken, secret_access_token)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

crypto = input("Enter HashTag (without #): ")

start = "2021-01-01"
end = "2021-04-17"

search_string = f"#{crypto}-filter:retweets"

tweet_cursor = tweepy.Cursor(api.search, q=search_string, lang='en', unitl=end, since=start, tweet_mode='extended').items(500)

tweets = [tweet.full_text for tweet in tweet_cursor]

tweets_df = pd.DataFrame(tweets, columns=['Tweets'])

for _, row in tweets_df.iterrows():
    row['Tweets'] = re.sub('http\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('#\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('@\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('\\n', '', row['Tweets'])
    
tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
tweets_df['Result'] = tweets_df['Polarity'].map(lambda pol: '+' if pol>0 else '-')

positive = tweets_df[tweets_df.Result=='+'].count()['Tweets']
negative = tweets_df[tweets_df.Result=='-'].count()['Tweets']

fig, ax = plt.subplots()
plt.bar([0, 1], [positive, negative], label=['Positive', 'Negative'], color=['green', 'red'])
plt.title(f"{crypto} Sentimental Analysis")
plt.legend()
#ax.text(str(positive))

plt.show()