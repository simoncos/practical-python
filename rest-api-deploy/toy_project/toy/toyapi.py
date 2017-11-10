#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import requests, json
from logic_a import cut

# business logic part

app = Flask(__name__) # create a Flask instance

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/cut/para/<string:content>') # syntax warning: must not have space beside ":"
def paraCut(content):
    word_str, word_num = cut(content)
    return "words: {}; number of words: {}".format(word_str, word_num)

@app.route('/cut/json/', methods=['POST'])
def jsonCut():
    if request.method == "POST":
        # get JSON in the request
        json_dict = request.get_json()
        content = json_dict['content']
        # run business logic
        word_str, word_num = cut(content)
        # format result to JSON
        data = {'word_str': word_str, 'word_num': word_num}
        return json.dumps(data) # serialize data to a JSON formatted str

# json post test
@app.route('/test/post/')
def postTest():
    # format a request
    url = 'http://localhost:5000/cut/json/'
    data = {'content': "我们中出了一个叛徒"}
    headers = {'Content-Type' : 'application/json'}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':
    app.run(debug=True)
