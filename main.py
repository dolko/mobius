#!/usr/bin/python3.6
from flask import Flask, request, send_from_directory, render_template, send_file
from flask_cors import CORS
from flask_restful import Resource, Api
from text import generate_text
from quickbks import find_amount

app = Flask(__name__)

CORS(app)

authorize_url = ""
request_token = ""
request_token_secret = ""


#generate the auth stuff
@app.route('/amount')
def amount():
    item = request.args['item']
    return find_amount(item)

@app.route('/prediction')
def prediction():
    item = request.args['item']

    return "based off how much you have in stock and recent demand you have around 10 days left"

@app.route('/newStock')
def newStock():
    item = request.args['item']

    return "You can order some new stock off ali baba, would you like to proceed?"

@app.route('/makeorder')
def makeOrder():
    item = request.args['item']

    return "the order is made, woudl you like me to send you a confirmation text"


# localhost:8000/text?number=0430853885&message=hello
@app.route('/text')
def text():
    #customize the website
    number = request.args['number']
    message = request.args['message']

    generate_text(number, message)
    return "sent texts"

if __name__ == '__main__':
    app.run(debug=False, port=8080)