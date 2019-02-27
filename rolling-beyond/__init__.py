#!/bin/env python3

from flask import Flask, jsonify
import requests

app = Flask(__name__)

char_request = lambda cid: requests.get("https://www.dndbeyond.com/character/{}/json".format(cid))

@app.route('/')
def index():
    return 'Hello, World'

@app.route('/sheets/<int:character>/')
def sheet(character):
    req = char_request(character)
    return jsonify(req.json())

# Spell lists
# [(x['definition']['name'], x['prepared'] or x['alwaysPrepared']) for x in c['classSpells'][0]['spells']]

# slassSpells is a list of dict of spells granted to the character from a class

# Actions available from a class
# [x['name'] for x in c['actions']['class']]

