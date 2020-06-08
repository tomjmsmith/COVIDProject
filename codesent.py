from io import open
#------------------
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

def get_sentiment(rating_data): ###this is the vader medium article###
   
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyser = SentimentIntensityAnalyzer()
    rating_data['sent_neg'] = -10
    rating_data['sent_neu'] = -10
    rating_data['sent_pos'] = -10
    rating_data['sent_compound'] = -10
    for i in range(len(rating_data)):
        date = rating_data['Date'][i]
        sentence = rating_data['Sentences'][i]
        ss = analyser.polarity_scores(str(sentence))
        rating_data.iloc[i, 2] = ss['neg']
        rating_data.iloc[i, 3] = ss['neu']
        rating_data.iloc[i, 4] = ss['pos']
        rating_data.iloc[i, 5] = ss['compound']
    return rating_data

###need to add in date column

#Input file. Replace with the output file of the parserforsentiment script. Don't forget run this for each keyword
rating_data = pd.read_csv("walmartpickup-jan-week-1.csv")
#print (rating_data)
rating_data = rating_data.rename(columns={rating_data.columns[0]: "Date", rating_data.columns[1]: "Sentences"})


sentiment_data = get_sentiment(rating_data)
#output for sentiment sheet. rename each time.
sentiment_data.to_excel("SENTIMENT_walmartpickup-jan-week-1.xlsx", index = False)
print ("Finally done! Don't forget to gather an output for each keyword :)")
