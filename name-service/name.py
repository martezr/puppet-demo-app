import json
import flask
from flask import Flask, render_template, request, session, redirect, jsonify, url_for, Response
from flask_cors import CORS
import requests
import string
import names

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"


@app.route('/api/name', methods=['GET'])
def generate_name():
    name = names.get_full_name()
    return jsonify({"name":name})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)