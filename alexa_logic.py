from flask import Flask
from flask_ask import Ask, statement, question, session
import json 
import requests
import time 
import unidecode
import requests

app = Flask(__name__)
ask = Ask(app, "/working")

def get_question():
	sess = requests.Session()
	html = sess.get('https://angelhacks17-nihaleg.c9users.io/cuisine')
	data = json.loads(html.content.decode("utf-8"))
	print(data)
	meal = str((data.get("restaurants")[0]).get("name"))
	# return "You seem pretty hungry. Should I buy you" + str(data.get("name")) + "for "+ str(data.get("basePrice"))+"."
	return "Great. I think you might be in the mood for"+str(data.get("cuisine"))  +"food. I heard"+ str(data.get("name"))+ "has good ratings on yelp. I am going to order you"+ meal +"How does that sound?"

@app.route("/")
def homepage():
	return "hello"

@ask.launch
def start_skill():
	welcome_message = "Hey there. It's a nice day outside! How are you doing?"
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