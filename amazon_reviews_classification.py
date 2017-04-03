import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
from matplotlib import pyplot as plt
from sklearn.preprocessing import Imputer
import unicodedata
start_time = time.time()

data=pd.read_csv("../Amazon_Unlocked_Mobile.csv",encoding='utf-8')
data.columns = ['ProductName', 'BrandName', 'Price', 'Rating', 'Reviews', 'ReviewVotes']
reviews = data.iloc[:,4]
reviews_cleaned = reviews.dropna()
sid = SentimentIntensityAnalyzer()

data['sentiment_compound_polarity']=reviews_cleaned.apply(lambda x:sid.polarity_scores(x)['compound'])
data['sentiment_neutral']=reviews_cleaned.apply(lambda x:sid.polarity_scores(x)['neu'])
data['sentiment_negative']=reviews_cleaned.apply(lambda x:sid.polarity_scores(x)['neg'])
data['sentiment_pos']=reviews_cleaned.apply(lambda x:sid.polarity_scores(x)['pos'])
data['sentiment_type']=''
data.loc[data.sentiment_compound_polarity>0,'sentiment_type']='POSITIVE'
data.loc[data.sentiment_compound_polarity==0,'sentiment_type']='NEUTRAL'
data.loc[data.sentiment_compound_polarity<0,'sentiment_type']='NEGATIVE'
print("--- %s seconds ---" % (time.time() - start_time))
data.to_csv('amazon_data_pandas.csv', sep=',', encoding='utf-8')
data.sentiment_type.value_counts().plot(kind='bar',title="sentiment analysis")
plt.show()