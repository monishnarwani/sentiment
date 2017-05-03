import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
import nltk
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def storeword(devicename, word):
	to_write = word.replace("."," ")
	if devicename == 'camera':
		camera.extend([to_write])
	elif devicename == 'battery':
		battery.extend([to_write])
	elif devicename == 'screen':
		screen.extend([to_write])
	elif devicename == 'wifi':
		wifi.extend([to_write])
	elif devicename == 'time':
		time.extend([to_write])
	elif devicename == 'price':
		price.extend([to_write])
	elif devicename == 'quality':
		quality.extend([to_write])
	elif devicename == 'memory':
		memory.extend([to_write])
	elif devicename == 'software':
		software.extend([to_write])
	elif devicename == 'video':
		video.extend([to_write])
	elif devicename == 'size':
		size.extend([to_write])
	elif devicename == 'power':
		power.extend([to_write])
	else :
		other.extend([to_write])

def displayBar(product):
	global camera 
	global battery 
	global screen 
	global wifi
	global price 
	global quality 
	global memory
	global software
	global video 
	global size 
	global power 
	global other 
	camera = []
	battery = []
	screen = []
	wifi = []
	price = []
	quality = []
	memory = []
	software = []
	video = []
	size = []
	power = []
	other = []
	data=pd.read_csv("../amazon_data_pandas.csv",encoding='utf-8')
	data.columns = ['index','ProductName','BrandName','Price','Rating','Reviews','ReviewVotes','sentiment_compound_polarity','sentiment_neutral','sentiment_negative','sentiment_pos','sentiment_type']	
	df = data
	product1 = product.replace('/','').replace('\\','')
	devices = ['screen','battery','price','camera','quality','software','wifi','memory','video','power','size']
	# one_company = 'Nokia Lumia 920 32GB Unlocked GSM 4G LTE Windows 8 Smartphone - Red'
	product1 = product.replace(","," ")
	myprod = product1.split(' ')
	one_company = product
	extractWords = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'terrible', 'awful','wow', 'hate','good','best', 'better','many', 'old','easy', 'nice', 'little','smart','bad','big', 'slow','excellent','powerful','worst','narrow','available' ,'failure', 'bad' ,'poor', 'solid', 'problems' ,'perfect' ,'quality' ,'horrible', '16gb', '8gb', '32gb', '64gb', '128gb', 'extraordinary', 'great', 'loose', 'amazing', 'sharp', 'big' ]
	df_one_company = df.loc[df['ProductName'].isin([one_company])]
	df_one_company_sample = df_one_company.dropna()
	one_company = myprod[0]
	
	for val in df_one_company_sample.Reviews.str.lower():
		blob = TextBlob(val)
		for word in blob.noun_phrases:
			word_list = word.split(" ")
			if (word_list[0] in devices and word_list[1] in extractWords):
			# if (word_list[0] in devices ):
				# to_write = word_list[1].replace("."," ")
				# pt.write(one_company + "." + word_list[0] + "." + to_write + ",1\n")
				storeword(word_list[0], word_list[1])
			elif (word_list[1] in devices and word_list[0] in extractWords):
			# elif (word_list[1] in devices ):
				# to_write = word_list[0].replace("."," ")
				# pt.write(one_company + "." + word_list[1] + "." + to_write + ",1\n")
				storeword(word_list[1], word_list[0])

	positive_words = ['great', 'good', 'excellent', 'awesome', 'powerful', 'smart', 'amazing', 'nice', 'speed', 'fantastic', 'love', 'wow', 'good', 'best', 'better', 'many', 'smart', 'excellent', 'solid', 'perfect', 'quality']
	negative_words = ['bad', 'worst', 'horrendous', 'problems', 'fail', 'dead', 'ugly', 'broken', 'horrible', 'terrible', 'awful', 'slow', 'narrow', 'failure']

	pos_num = [0] * len(devices)
	neg_num = [0] * len(devices)

	for word in screen:
		if word in positive_words:
			pos_num[0] = pos_num[0] + 1
		else:
			neg_num[0] = neg_num[0] + 1
	for word in battery:
		if word in positive_words:
			pos_num[1] = pos_num[1] + 1
		else:
			neg_num[1] = neg_num[1] + 1
	for word in price:
		if word in positive_words:
			pos_num[2] = pos_num[2] + 1
		else:
			neg_num[2] = neg_num[2] + 1
	for word in camera:
		if word in positive_words:
			pos_num[3] = pos_num[3] + 1
		else:
			neg_num[3] = neg_num[3] + 1
	for word in quality:
		if word in positive_words:
			pos_num[4] = pos_num[4] + 1
		else:
			neg_num[4] = neg_num[4] + 1
	for word in software:
		if word in positive_words:
			pos_num[5] = pos_num[5] + 1
		else:
			neg_num[5] = neg_num[5] + 1
	for word in wifi:
		if word in positive_words:
			pos_num[6] = pos_num[6] + 1
		else:
			neg_num[6] = neg_num[6] + 1
	for word in memory:
		if word in positive_words:
			pos_num[7] = pos_num[7] + 1
		else:
			neg_num[7] = neg_num[7] + 1
	for word in video:
		if word in positive_words:
			pos_num[8] = pos_num[8] + 1
		else:
			neg_num[8] = neg_num[8] + 1
	for word in power:
		if word in positive_words:
			pos_num[9] = pos_num[9] + 1
		else:
			neg_num[9] = neg_num[9] + 1
	for word in size:
		if word in positive_words:
			pos_num[10] = pos_num[10] + 1
		else:
			neg_num[10] = neg_num[10] + 1

	print pos_num
	print neg_num

	return str(devices), str(pos_num), str(neg_num)



