import json
import flask
from flask import Flask, render_template, request, session, redirect, jsonify, url_for, Response
from flask_cors import CORS
import requests
import string
from random import *

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"


@app.route('/api/password', methods=['GET'])
def generate_password():
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(8, 12)))
    return jsonify({"password": password})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)