import json
import flask
from flask import Flask, render_template, request, session, redirect, jsonify, url_for, Response
from flask_cors import CORS
import requests
import string

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"

def getName():
    try:
        url = 'http://nameservice:8000/api/name'
        res = requests.get(url, timeout=3.0)
    except BaseException:
        res = None

    if res and res.status_code == 200:
        name = res.json()
        name = name['name']
        return 200, name
    else:
        status = res.status_code if res is not None and res.status_code else 500
        return status, 'Service unavailable'

def getPassword():
    try:
        url = 'http://passwordservice:8001/api/password'
        res = requests.get(url, timeout=3.0)
    except BaseException:
        res = None
    if res and res.status_code == 200:
        password = res.json()
        password = password['password']
        return 200, password
    else:
        status = res.status_code if res is not None and res.status_code else 500
        return status, 'Service unavailable'

@app.route('/', methods=['GET'])
def home():
    namestatus, name = getName()
    passwordstatus, password = getPassword()

    return render_template(
        'index.html',
        name=name,
        password=password)


@app.route('/api/output', methods=['GET'])
def apioutput():
    namestatus, name = getName()
    passwordstatus, password = getPassword()

    return jsonify({"name": name, "password": password})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)