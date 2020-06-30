from nltk import PorterStemmer
from nltk import WordNetLemmatizer
import csv
import gensim



def lemmatize_stemming(text):
    return PorterStemmer().stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess(text):
    result = []

    for token in gensim.utils.simple_preprocess(text):

        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))

    return result


def preprocessNoLem(text):
    result = []

    for token in gensim.utils.simple_preprocess(text):

        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 2:
            result.append(token)

    return result


myRootDir = "/Users/TomSmith/Desktop/MIS/Project/"  # change this to your directory
mydir = myRootDir #+ "data - tweets"

myFILENAME = mydir + "amazonfresh.csv" # name of input csv file
myFILE = open(myFILENAME, "r", encoding="utf8")
myReader = csv.reader(myFILE)

dataFILENAME = myRootDir + "af_wf.csv" # change this name to what name you want.
dataFILE = open(dataFILENAME, "a+")

tempLeaName = ""
tempLeaURL = ""

for line in myReader:

    print(line[6])

    linePerm = line[len(line) - 1]

    text = line[6]

    try:

        LemmaText = preprocessNoLem(text)

        datLine = linePerm + "," + ",".join(LemmaText) + "\n"

    except:

        print(line + "," + str(sys.exc_info()[0]) + "\n")

        datLine = linePerm + "," + str(sys.exc_info()[0]) + "\n"

    try:

        dataFILE.write(datLine)

    except UnicodeEncodeError:

        dataFILE.write(datLine.encode('cp1252', errors='replace').decode('cp1252'))


myFILE.close()

dataFILE.close()

