import re
import base64
from flask import Flask, url_for, Response, request, make_response
from flask import Blueprint

app = Blueprint('challenge02', __name__)


@app.route("/challenge02")
def challenge_02():
    try:
        with open('html/challenge02.html', 'r') as index:
            return index.read()
    except Exception as e:
        print(e)
        return 'error during read html happened', 500


@app.route("/challenge02/check")
def task1():
    value = request.args.get('value')
    if value.lower() == 'hello':
        return {'result': 'you did it!'}
    return {'result': 'try harder'}
