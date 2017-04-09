from flask import Flask, render_template,json,jsonify,redirect,request
from senti_search import search_brand, load_brands
from create_wordcloud import create_one_wordcloud
app = Flask(__name__)
brand_names = ''
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/welcome')
def welcome():
	name = 'Monish'
	author = 'Narwani'
	return render_template('new/welcome.html', author = author, name = name)

@app.route('/chart')
def display_chart():
	data = ['123','12','1']
	return render_template('new/chart.html',values=data )

@app.route('/lists')
def lists_display():
	return render_template('lists.html',mymsg='this is python')

@app.route('/api/user-data')
def user_data():
	data = {}
	data['head'] = 'My Heading'
	lists = ['first','second','third']
	data['lists'] = lists
	jdata = jsonify(data)
	return jdata

@app.route('/signup', methods = ['POST'])
def signup():
	print("hello")
	email = request.form['email']
	print("The email address is '" + email + "'")
	return redirect('/')

@app.route('/analysis')
def analysis_show():
	values=[0]*3
	total = 0
	rating_total=0
	brand = ''
	brand_names = load_brands()
	return render_template('ecomm/production/SMA_Charts.html',bar_values=values,total=total,total_rating=rating_total,brand=brand,brand_names=brand_names)

@app.route('/searchbrand', methods = ['GET'])
def product_search():
	brand = request.args.get('brand')
	values,total,rating_total = search_brand(brand)
	create_one_wordcloud(brand)
	return render_template('ecomm/production/SMA_Charts.html',bar_values=values,total=total,total_rating=rating_total,brand=brand,brand_name=brand_names)

if __name__ == '__main__':
    app.run()