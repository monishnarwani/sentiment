import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np


def load_data():
	data=pd.read_csv("../amazon_data_pandas.csv",encoding='utf-8')
	data.columns = ['index','ProductName','BrandName','Price','Rating','Reviews','ReviewVotes','sentiment_compound_polarity','sentiment_neutral','sentiment_negative','sentiment_pos','sentiment_type']	
	return data

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
	return val,total
	
search_brand('Samsung')