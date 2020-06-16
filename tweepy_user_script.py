import tweepy
import datetime
import time
import pandas as pd

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN =  '1225588001683771393-D8ScBf0UPOo2oGrIjt7aX9gONWLtf6'
ACCESS_SECRET = '8hBqgdJETOTRBIa7o0hlTz4ECYcNDSutXxYuGct5LloUb'
CONSUMER_KEY = 'GySvTYCGwyOOlOva33E6JU0IE'
CONSUMER_SECRET = 'roxhZ4gkUVlN0CPQWQsLbTYMJzbknZSKKDiJouN4ZQcvvCOq6c'

# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    return api


# Create API object
api = connect_to_twitter_OAuth()

twt_df = pd.read_csv("amazonfresh-apr-week-1.csv") #enter file and turns csv into dataframe

twt_df['location'] = '' # adds location column to the csv file

for i in range(len(twt_df)): # loops through every row

    user_handle = twt_df.iloc[i,1] 

    try:
        user = api.get_user(screen_name = user_handle) # tweepy call for user
        print(user.screen_name)
        location = user.location # assigns location attribute 
        print(location)
        twt_df.iloc[i,12] = location  # adds location to corresponding cell in location column
    except tweepy.TweepError as e: # error exception for user not found 
        print(e)
        pass
        
print(twt_df)
twt_df.to_csv('LOCATION-amazonfresh-apr-week-1.csv', index=False, encoding='utf-8')


