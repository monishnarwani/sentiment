import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
tweets=pd.read_csv("iphone7plus.csv",encoding = "ISO-8859-1")
tweets.head()
from textblob import TextBlob
len_tweets = len(list(tweets))
list_tweets = list(tweets)
totalScore = 0
for i in range (0,len_tweets):
	str1 = str(list_tweets).encode('utf-8')
	blob = TextBlob(str1)
	totalSentScore = 0
	numSent = 0
	for sentence in blob.sentences:
		numSent = numSent + 1
		score = sentence.sentiment.polarity
		totalSentScore = totalSentScore + score
	
	totalScore = totalScore + (totalSentScore)

