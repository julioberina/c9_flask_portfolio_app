from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone
import requests
import os
import random

# for Number Guess game
number = random.randrange(1, 101)
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	return render_template('index.html', name=name)

@app.route('/contact', methods=['GET'])
def contact_page():
	return render_template('contact.html')

@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 0
  	      try:
  	      	for str_num in request.form['text'].split():
  	      		total += int(str_num)
  	      	return render_template('add_numbers.html', result=str(total))
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"


@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())

          shop_list = []
          try:
            for item in request.form['text'].split():

              shop_list.append(item)



            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"


@app.route('/number_guess', methods=['GET','POST'])
def number_guess_post():
	global number

	if request.method == 'GET':
		return render_template('number_guess.html')
	elif request.method == 'POST':
		print("guess: {}".format(int(request.form['text'])))
		print("number: {}".format(number))
		consensus = ''

		try:
			guess = int(request.form['text'])
			if guess < number: consensus = 'Guess higher!'
			elif guess > number: consensus = 'Guess lower!'
			else:
				number = random.randrange(1, 101)
				consensus = 'You got it! I have a new number now...'

			return render_template('number_guess.html', result=consensus)
		except ValueError:
			return "Easy now! Let's keep it simple! Numbers only or don't leave blank!"

@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')


if __name__ == '__main__':
	app.run(debug=True)
