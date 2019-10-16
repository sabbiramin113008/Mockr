
# -*- coding: utf-8 -*-
"""

author: S.M. Sabbir Amin
project_name: Test Server
date: 15 October, 2019

"""


import json
import codecs
from flask import Flask, request, jsonify

app = Flask(__name__)
app.secret_key = 'YourDummySecretKeyIsHere'
with codecs.open("db.json","r","utf-8") as f:
    db = json.load(f)

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Hello World</h1>'
    


@app.route('/api/books',methods=['POST'])
def find_book_details():
    if request.method=='POST':
        response = db["0"]["response"]
        return jsonify(response),200

@app.route('/api/authors',methods=['POST'])
def find_author_details():
    if request.method=='POST':
        response = db["1"]["response"]
        return jsonify(response),200


app.run(
    port=8000,
    host="localhost",
    debug=True
    )
