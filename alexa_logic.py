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
	
	return "You seem pretty hungry. Should I buy you" + str(data.get("name")) + "for "+ str(data.get("basePrice"))+"."

@app.route("/")
def homepage():
	return "hello"

@ask.launch
def start_skill():
	lol = get_question()
	welcome_message = lol
	return question(welcome_message)

@ask.intent("YesIntent")
def order_food():
	 return statement("COOL")

@ask.intent("NoIntent")
def no_intent():
	bye = "Okay good bye!"
	return statement(bye)

if __name__ == "__main__":
	app.run(debug=True)