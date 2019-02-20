#!/usr/bin/env python3
"""a simple Flask HTTP service"""
from flask import Flask, jsonify
import requests


app = Flask(__name__)

session = requests.Session()

@app.route('/')
def index():
    resp = session.get('https://httpbin.org/get?request=1').json()
    return jsonify(resp)

if __name__ == "__main__":
    app.run(threaded=False)