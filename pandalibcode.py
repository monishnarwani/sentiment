import pandas as pd
import numpy as np
from textblob import TextBlob
# from guage import gauge
from matplotlib import pyplot as plt
import sys 
reload(sys)  
sys.setdefaultencoding('utf8')


def findReviewsByBrand(brand, dataf):
	return dataf.loc[dataf['BrandName'].isin([brand])]

data = pd.read_csv('amazon_reviews.csv', encoding='utf-8')
df = data
df.columns = ['ProductName', 'BrandName', 'Price', 'Rating', 'Reviews', 'ReviewVotes']
df['Price'] = df['Price'].fillna(0)
df['ReviewVotes'] = df['ReviewVotes'].fillna(0)
df['Rating'] = df['Rating'].fillna(0)
# print data.describe()
# print num_review
list_reviews=list(df['Reviews'])
len_reviews = len(list_reviews)
# df_apple = df.loc[df['BrandName'].isin(['Samsung'])]
# df_apple = findReviewsByBrand('Samsung',df)
# df_apple_reviews = df_apple ['Reviews']
# list_apple_revies = list(df_apple_reviews)
# len_apple_reviews = len(list_apple_revies)

totalScore = 0
for i in range(0,len_reviews):
	str1 = str(list_reviews[i]).encode('utf-8')
	blob = TextBlob(str1)
	totalSentScore = 0
	numSent = 0
	for sentence in blob.sentences:
		numSent = numSent + 1
		score = sentence.sentiment.polarity
		totalSentScore = totalSentScore + score
	data['SentiScore'][i]=totalSentScore
	data['SentiType'][i]='Positive' if totalSentScore>0 else ('Negative' if totalSentScore <0 else 'Neutral') 
	print list_reviews[i]
	print data['SentiScore'][i]
	print data['SentiType'][i]
data.SentiType.value_counts().plot(kind='bar',title="sentiment analysis")
plt.show()




	# totalScore = totalScore + (totalSentScore)
# print (totalScore/200*100)
# pointVal = int((totalScore/200*100)/5)
# colm = ['5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100']
# gauge(labels=colm, \
#     colors=['#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00','#007A00']\
#     , arrow=pointVal, title='something here') 	

