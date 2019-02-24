#!/bin/env python3

from flask import Flask
import requests

app = Flask(__name__)

char_request = lambda cid: requests.get("https://www.dndbeyond.com/character/{}/json".format(cid))

@app.route('/')
def index():
    return 'Hello, World'

@app.route('/sheets/<int:character>/')
def sheet(character):
    req = char_request(character)
    return str(req.json())
