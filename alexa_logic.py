from flask import Flask
from flask_ask import Ask, statement, question, session
import json 
import requests
import time 
import unidecode

app = Flask(__name__)
ask = Ask(app, "/working")

def get_question():
	return "aite dope"

@app.route("/")
def homepage():
	return "hello"

@ask.launch
def start_skill():
	welcome_message = "There is a Panda Express near you! Should I order it?"
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