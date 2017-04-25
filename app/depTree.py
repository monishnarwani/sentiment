import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
from nltk.parse.stanford import StanfordDependencyParser
import nltk

path_to_jar = '/home/monish/Documents/sentiment/stanford/stanford-parser/jars/stanford-parser.jar'
path_to_models_jar = '/home/monish/Documents/sentiment/stanford/stanford-parser/jars/stanford-parser-3.7.0-models.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar,path_to_models_jar=path_to_models_jar)

data=pd.read_csv("../amazon_data_pandas.csv",encoding='utf-8')
data.columns = ['index','ProductName','BrandName','Price','Rating','Reviews','ReviewVotes','sentiment_compound_polarity','sentiment_neutral','sentiment_negative','sentiment_pos','sentiment_type']	
df = data

one_company = 'Samsung Galaxy Note 3 N900A 32GB White - Unlocked'
df_one_company = df.loc[df['ProductName'].isin([one_company])]
df_one_company_sample = df_one_company.dropna()
collection = ''
for sent in df_one_company_sample.Reviews.str.lower():
    dpnlp = dependency_parser.raw_parse(sent)
    for line in dpnlp:
    	x = list(line.triples())
    	for arg1, pred1, arg2 in x:
    		w1, pos1 = arg1
    		w2, pos2 = arg2
    		if pos1.startswith('JJ') and pos2.startswith('RB'):
    			word = w2 + ' ' + w1
    			print word
    		elif pos1.startswith('VBG') and pos2.startswith('JJ'):
    			word = w2 + ' ' + w1
    			print word
    		elif pos1.startswith('VBN') and pos2.startswith('RB'):
    			word = w2 + ' ' + w1
    			print word
    		elif pos1.startswith('NNP') and pos2.startswith('NNP'):
    			word = w2 + ' ' + w1
    			print word