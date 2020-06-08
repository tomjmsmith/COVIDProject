from io import open
import os
import re
import math
import string
import requests
import json
from itertools import product
from inspect import getsourcefile
import pandas as pd
import vaderSentiment
import numpy as np
import openpyxl

def get_sentiment(rating_data): 
   
   #Load VADER
   from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
   analyser = SentimentIntensityAnalyzer()
    rating_data['sent_neg'] = -10
    rating_data['sent_neu'] = -10
    rating_data['sent_pos'] = -10
    rating_data['sent_compound'] = -10
  
    for i in range(len(rating_data)):
        #Date and Tweet Columns - add more if needed; just be sure to add to line 41 as well
        date = rating_data['Date'][i]
        tweet = rating_data['Tweets'][i]
         
        #Sentiment Scores - tweets are converted to strings
        ss = analyser.polarity_scores(str(tweet))
        rating_data.iloc[i, 2] = ss['neg']
        rating_data.iloc[i, 3] = ss['neu']
        rating_data.iloc[i, 4] = ss['pos']
        rating_data.iloc[i, 5] = ss['compound']
         
    return rating_data

#Input File
rating_data = pd.read_csv("walmartpickup-jan-week-1.csv")
#Set Columns - make sure input file has the corresponding columns
rating_data = rating_data.rename(columns={rating_data.columns[0]: "Date", rating_data.columns[1]: "Tweets"})

#Retrieving Sentiment Scores
sentiment_data = get_sentiment(rating_data)

#Output Scores to Spreadsheet - be sure to rename each time
sentiment_data.to_excel("SENTIMENT_walmartpickup-jan-week-1.xlsx", index = False)
print ("Finished! :)")
