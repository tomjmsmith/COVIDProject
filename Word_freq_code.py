import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
import pandas as pd
import numpy as np
import openpyxl
import string
import chunk
#import reduce

tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()


def remove_stopwords(df_text):
    words = [w for w in df_text if w not in stopwords.words('english')]
    return words


def word_lemmatizer(df_text):
    lem_text = [lemmatizer.lemmatize(i) for i in df_text]
    return lem_text

def mapper(text):
    tokens_in_text = text.split()
    tokens_in_text = map(clean_word, tokens_in_text)
    tokens_in_text = filter(word_not_in_stopwords, tokens_in_text)
    return Counter(tokens_in_text)

def reducer(cnt1, cnt2):
    cnt1.update(cnt2)
    return cnt1

def chunk_mapper(chunk):
    mapped = map(mapper, chunk)
    reduced = reduce(reducer, mapped)
    return reduced


df =pd.read_csv('af_wf.csv')

data_count = df["text"].value_counts()
data_count.to_excel("amazonfresh-test.xlsx") # change this name

# works fine from here
# df = pd.read_csv('amazonfresh-test.csv', encoding='utf-8', converters={'text': str})

# df = pd.read_csv('af_wf.csv', header=[0], sep='\t')

# df = df[list(df.columns[~df.columns.duplicated()])]

# data_chunks = chunkify(data, number_of_chunks=36)

# step 1:
# mapped = pool.map(chunk_mapper, data_chunks)

# step 2:
# reduced = reduce(reducer, mapped)
# print(reduced.most_common(10))
# data_tok = df['text'].apply(lambda x: tokenizer.tokenize(x.lower()))
# data_stop = data_tok.apply(lambda x: remove_stopwords(x))
# data_lem = data_stop.apply(lambda x: word_lemmatizer(x))

# to here

# this is where I have issues

# data_tok = df['text'].apply('index').value_counts()
# data_c = df['text'].apply(lambda x: len(x))
# data_count = df['text'].str.split(expand=True).stack().value_counts()
# df['text'].str.split('  ').apply('text', 1).stack().value_counts()
# .apply(axis=1)

# data_count = data_tok.groupby('text').value_counts(df.values.flatten())


