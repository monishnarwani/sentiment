import json
from textblob import TextBlob
totalScore = 0
totalSentScore = 0
numSent = 0
with open('cell_temp.json') as data_file:#data extraction    
    data = json.load(data_file)
rang = 120
for i in range(0,120):
	str1 = (data["sentiments"][i]["reviewText"])
	blob = TextBlob(str1)
	totalSentScore = 0
	numSent = 0
	for sentence in blob.sentences:
		numSent = numSent + 1
		score = sentence.sentiment.polarity
		totalSentScore = totalSentScore + score
	totalScore = totalScore + (totalSentScore/numSent)
print (totalScore/rang*100)	
# print "hi"