from flask import Flask
from flask_ask import Ask, statement, question, session
import json 
import requests
import time 
import unidecode
import requests
from pprint import pprint

app = Flask(__name__)
ask = Ask(app, "/working")

def get_question():
	data = requests.get('https://angelhacks17-nihaleg.c9users.io/cuisine')
	final_data = json.loads(data.text)

	shit = list(final_data.keys())
	print(shit)
	food_type = shit[0]
	rest_name = final_data[food_type]["Meals"]
	rest_name = rest_name[0]
	print(rest_name)
	# save = rest_name.index("name")


	# sess = requests.Session()
	# html = sess.get('https://angelhacks17-nihaleg.c9users.io/cuisine')
	# data = json.loads(html.content.decode("utf-8"))
	# print(data)

	# print(data)
# {'Thai': {'Meals': {'name': 'Mae Krua', 'latitude': 37.7394, 'longitude': -122.41799, 'rating': 'Rating: 4.5', 'image': 'https://www.yelp.com/biz/mae-krua-san-francisco?adjust_creative=vRSLRJhyDLQuyMD6K_4bBA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=vRSLRJhyDLQuyMD6K_4bBA', 'price': '$'}}}

	# json.format()
	# return "You seem pretty hungry. Should I buy you" + str(data.get("name")) + "for "+ str(data.get("basePrice"))+"."
	return "Great. I think you might be in the mood for some"+ food_type  +"food. I heard"+ rest_name.get("name") + "has pretty good food on yelp and it is not too expensive. It also has a "+str(rest_name.get("rating"))+" star rating. How does that sound?"

@app.route("/")
def homepage():
	return "hello"

@ask.launch
def start_skill():
	welcome_message = "Hey there. Isn't it a nice day? How are you?"
	return question(welcome_message)

@ask.intent("YesIntent")
def order_food():
	 return statement("Okay! I am moving the transaction to your phone! Please go confirm it!")

@ask.intent("GetFoodIntent")
def want_food():
	lol = get_question()
	return question(lol)

@ask.intent("NoIntent")
def no_intent():
	bye = "Okay, let me know then!"
	return statement(bye)

if __name__ == "__main__":
	app.run(debug=True)