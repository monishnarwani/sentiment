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

def displayDendo(product):
	global camera 
	global battery 
	global screen 
	global wifi
	global time 
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
	time = []
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
	pt = open('static/'+product1+'.csv', "w+")
	devices = ['screen','battery','price','camera','quality','software','wifi','memory','video','power','size']
	# one_company = 'Nokia Lumia 920 32GB Unlocked GSM 4G LTE Windows 8 Smartphone - Red'
	product1 = product.replace(","," ")
	myprod = product1.split(' ')
	one_company = product
	extractWords = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'terrible', 'awful','wow', 'hate','good','best', 'better','many', 'old','easy', 'nice', 'little','smart','bad','big', 'slow','excellent','powerful','worst','narrow','available' ,'failure', 'bad', 'performance' ,'poor', 'solid', 'problems' ,'perfect' ,'quality' ,'horrible', '16gb', '8gb', '32gb', '64gb', '128gb', 'extraordinary', 'great', 'loose', 'amazing', 'sharp', 'big' ]
	df_one_company = df.loc[df['ProductName'].isin([one_company])]
	df_one_company_sample = df_one_company.dropna()
	one_company = myprod[0]
	pt.write('id,value\n')
	pt.write(one_company + ",\n")

	
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

	
	setcamera = set(camera)
	if (len(setcamera)>0):
		pt.write(one_company + "." + 'camera' + ",\n")
	for rev in setcamera:
		pt.write(one_company + "." + 'camera' + "." + rev + ",1\n")
	setbattery = set(battery)
	if (len(setbattery)>0):
		pt.write(one_company + "." + 'battery' + ",\n")
	for rev in setbattery:
		pt.write(one_company + "." + 'battery' + "." + rev + ",1\n")
	setscreen = set(screen)
	if (len(setscreen)>0):
		pt.write(one_company + "." + 'screen' + ",\n")
	for rev in setscreen:
		pt.write(one_company + "." + 'screen' + "." + rev + ",1\n")
	setwifi = set(wifi)
	if (len(setwifi)>0):
		pt.write(one_company + "." + 'wifi' + ",\n")
	for rev in setwifi:
		pt.write(one_company + "." + 'wifi' + "." + rev + ",1\n")	
	setsize = set(size)
	if (len(setsize)>0):
		pt.write(one_company + "." + 'size' + ",\n")
	for rev in setsize:
		pt.write(one_company + "." + 'size' + "." + rev + ",1\n")
	setvideo = set(video)
	if (len(setvideo)>0):
			pt.write(one_company + "." + 'video' + ",\n")
	for rev in setvideo:
		pt.write(one_company + "." + 'video' + "." + rev + ",1\n")
	setsoftware = set(software)
	if (len(setsoftware)>0):
			pt.write(one_company + "." + 'software' + ",\n")
	for rev in setsoftware:
		pt.write(one_company + "." + 'software' + "." + rev + ",1\n")
	setmemory = set(memory)
	if (len(setmemory)>0):
			pt.write(one_company + "." + 'memory' + ",\n")
	for rev in setmemory:
		pt.write(one_company + "." + 'memory' + "." + rev + ",1\n")
	setquality = set(quality)
	if (len(setquality)>0):
			pt.write(one_company + "." + 'quality' + ",\n")
	for rev in setquality:
		pt.write(one_company + "." + 'quality' + "." + rev + ",1\n")
	setprice = set(price)
	if (len(setprice)>0):
			pt.write(one_company + "." + 'price' + ",\n")
	for rev in setprice:
		pt.write(one_company + "." + 'price' + "." + rev + ",1\n")
	settime = set(time)
	if (len(settime)>0):
			pt.write(one_company + "." + 'time' + ",\n")
	for rev in settime:
		pt.write(one_company + "." + 'time' + "." + rev + ",1\n")
	setpower = set(power)
	if (len(setpower)>0):
			pt.write(one_company + "." + 'power' + ",\n")
	for rev in setpower:
		pt.write(one_company + "." + 'power' + "." + rev + ",1\n")

	pt.close()




