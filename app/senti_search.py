import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
import nltk
import string
from nltk.corpus import stopwords
from wordcloud import WordCloud
from HTMLParser import HTMLParser
def load_data():
	data=pd.read_csv("../amazon_data_pandas.csv",encoding='utf-8')
	data.columns = ['index','ProductName','BrandName','Price','Rating','Reviews','ReviewVotes','sentiment_compound_polarity','sentiment_neutral','sentiment_negative','sentiment_pos','sentiment_type']	
	return data

def load_brands():
	data = load_data()
	unique_brand=list(set(data['BrandName']))
	ubrand=pd.DataFrame(unique_brand) 
	ubrand.columns = ['name']
	json_brand = ubrand.reset_index().to_json(orient='records')
	return json_brand


def search_brand(brandname):
	data = load_data()
	data_brand = data.loc[data['BrandName'].isin([brandname])]
	json_val = data_brand.sentiment_type.value_counts()
	val = range(3)
	val[0] = json_val.POSITIVE
	val[1] = json_val.NEGATIVE
	val[2] = json_val.NEUTRAL
	data_compound = data_brand['sentiment_compound_polarity']
	sum = data_compound.sum()
	num = len(data_compound.index)
	total = sum/num*5
	data_ratings = data_brand['Rating']
	rating_total = data_ratings.sum()
	rating_total = rating_total / (num*1.0)
	return val,total,rating_total
	

def load_products():
	data = load_data()
	unique_brand=list(set(data['ProductName']))
	ubrand=pd.DataFrame(unique_brand) 
	ubrand.columns = ['name']
	json_brand = ubrand.reset_index().to_json(orient='records')
	return json_brand


def search_products(product):
	data = load_data()
	data_prod = data.loc[data['ProductName'].isin([product])]
	json_val = data_prod.sentiment_type.value_counts()
	val = range(3)
	try:
		val[0] = json_val.POSITIVE
	except AttributeError:
		value_countsal[0] = 0
	try:
		val[1] = json_val.NEGATIVE
	except AttributeError:
		val[1] = 0
	try:
		val[2] = json_val.NEUTRAL
	except AttributeError:
		val[2] = 0
	data_compound = data_prod['sentiment_compound_polarity']
	sum = data_compound.sum()
	num = len(data_compound.index)
	total = sum/num*5
	data_ratings = data_prod['Rating']
	rating_total = data_ratings.sum()
	rating_total = rating_total / (num*1.0)
	return val,total,rating_total
# search_brand('Samsung')
