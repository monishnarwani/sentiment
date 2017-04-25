import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
import nltk
import string
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def create_one_wordcloud(brand):
	data=pd.read_csv("../amazon_data_pandas.csv",encoding='utf-8')
	data.columns = ['index','ProductName','BrandName','Price','Rating','Reviews','ReviewVotes','sentiment_compound_polarity','sentiment_neutral','sentiment_negative','sentiment_pos','sentiment_type']	
	df = data

	one_company = brand
	df_one_company = df.loc[df['BrandName'].isin([one_company])]
	df_one_company_sample = df_one_company
	df_one_company_sample = df_one_company_sample.dropna()
	word_cloud_collection = ''
	for val in df_one_company_sample.Reviews.str.lower():
	    tokens = nltk.word_tokenize(val)

	    tokens = [word for word in tokens if word not in stopwords.words('english')]
	    for words in tokens:
	        word_cloud_collection = word_cloud_collection + words + ' '
	wordcloud = WordCloud(max_font_size=50, width=500, height=500).generate(word_cloud_collection)
	image = wordcloud.to_image()
	image.save('static/images/'+brand+'.png',format='png')
	# fwords = []
	# for val in df_one_company_sample.Reviews.str.lower():
	# 	blob = TextBlob(val)
	# 	fwords.extend(blob.noun_phrases)
def create_one_wordcloud_product(product):
	data=pd.read_csv("../amazon_data_pandas.csv",encoding='utf-8')
	data.columns = ['index','ProductName','BrandName','Price','Rating','Reviews','ReviewVotes','sentiment_compound_polarity','sentiment_neutral','sentiment_negative','sentiment_pos','sentiment_type']	
	df = data

	one_company = product
	df_one_company = df.loc[df['ProductName'].isin([one_company])]
	df_one_company_sample = df_one_company.dropna()
	word_cloud_collection = ''
	for val in df_one_company_sample.Reviews.str.lower():
	    tokens = nltk.word_tokenize(val)

	    tokens = [word for word in tokens if word not in stopwords.words('english')]
	    for words in tokens:
	        word_cloud_collection = word_cloud_collection + words + ' '
	wordcloud = WordCloud(max_font_size=50, width=500, height=500).generate(word_cloud_collection)
	image = wordcloud.to_image()
	image.save('static/images/'+product+'.png',format='png')