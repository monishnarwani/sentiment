import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
import nltk
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
data=pd.read_csv("../amazon_data_pandas.csv",encoding='utf-8')
data.columns = ['index','ProductName','BrandName','Price','Rating','Reviews','ReviewVotes','sentiment_compound_polarity','sentiment_neutral','sentiment_negative','sentiment_pos','sentiment_type']	
df = data
pt = open('parsetree.txt', "w")
devices = ['battery-life','screen','battery','time','price','app','camera','quality','card','life','service','button','network','software','wifi','music','keyboard','memory','sim','video','power','message','size','case']
one_company = 'Nokia Lumia 920 32GB Unlocked GSM 4G LTE Windows 8 Smartphone - Red'
df_one_company = df.loc[df['ProductName'].isin([one_company])]
df_one_company_sample = df_one_company.dropna()
pt.write('id,value\n')
pt.write(one_company + ",\n")

for dev in devices:
	pt.write(one_company + "." + dev + ",\n")

for val in df_one_company_sample.Reviews.str.lower():
	blob = TextBlob(val)
	for word in blob.noun_phrases:
		word_list = word.split(" ")
		if (word_list[0] in devices):
			to_write = word_list[1].replace("."," ")
			pt.write(one_company + "." + word_list[0] + "." + to_write + ",1\n")
		elif (word_list[1] in devices):
			to_write = word_list[0].replace("."," ")
			pt.write(one_company + "." + word_list[1] + "." + to_write + ",1\n")
pt.close()