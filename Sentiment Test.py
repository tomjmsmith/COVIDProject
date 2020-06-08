import pandas as pd
import numpy as np
import nltk

nltk.download("vader_lexicon")
def get_sentiment(rating_data):
    """
    https: // github.com / cjhutto / vaderSentiment
    :return:
    """
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    rating_data['sent_neg'] = -10
    rating_data['sent_neu'] = -10
    rating_data['sent_pos'] = -10
    rating_data['sent_compound'] = -10
    for i in range(len(rating_data)):
        sentence = rating_data['Sentences'][i]
        print (sentence)
        ss = sid.polarity_scores(sentence.encode('ascii', 'ignore'))
        print (ss['neg'])
        rating_data.iloc[i, 1] = float(ss['neg'])
        print (rating_data.iloc[i, 1])
        rating_data.iloc[i, 2] = ss['neu']
        rating_data.iloc[i, 3] = ss['pos']
        rating_data.iloc[i, 4] = ss['compound']
    return rating_data



#Input file. Replace with the output file of the parserforsentiment script. Don't forget run this for each keyword
rating_data = pd.read_csv("realhomechef-jan-week-1.csv", encoding='utf-8', error_bad_lines=False)
print (rating_data)
rating_data = rating_data.rename(columns={ rating_data.columns[0]: "Sentences" })


sentiment_data = get_sentiment(rating_data)
#output for sentiment sheet. rename each time.
sentiment_data.to_excel(" realhomechef-jan-week-1.xlsx", index = False)
print ("Finally done! Don't forget to gather an output for each keyword :)")
