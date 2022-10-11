import binascii
import re
import base64
from flask import Flask, url_for, Response, request, make_response
from flask import Blueprint

app = Blueprint('challenge03', __name__)


@app.route("/challenge03")
def challenge_01():
    try:
        with open('html/challenge01.html', 'r') as index:
            response = make_response(index.read())
            response.set_cookie('secretKeyPartEncoded', 'bmVlcuKdpO+4jw==')
            return response
    except Exception:
        return 'error during read html happened', 500


# TODO how to verify result?
@app.route("/challenge03/task1")
def task2():
    value = request.args.get('value')
    if any(i not in '12345678' for i in value):
        return {"response": ''}

    if value.endswith('8'):
        value = value[0:-1]

    parity = ''
    if len(value) > 0 and len(value) % 2 == 0:
        parity = '8'

    if value == '':
        return {"response": '1' + parity}
    if value == '1':
        return {"response": '2' + parity}
    if value == '2':
        return {"response": '35' + parity}
    if value == '35':
        return {"response": '467' + parity}
    if value == '467':
        return {"response": '26' + parity}
    if value == '26':
        return {"response": '1' + parity}
    return {"response": '1' + parity}
