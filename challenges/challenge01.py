import binascii
import re
import base64
from flask import Flask, url_for, Response, request, make_response
from flask import Blueprint

app = Blueprint('challenge01', __name__)


@app.route("/challenge01")
def challenge_01():
    try:
        with open('html/challenge01.html', 'r') as index:
            response = make_response(index.read())
            response.set_cookie('secretKeyPartEncoded', 'bmVlcuKdpO+4jw==')
            return response
    except Exception:
        return 'error during read html happened', 500


@app.route("/challenge01/task1")
def task1():
    value = request.args.get('value')
    if len(value) == 0:
        return {"response": False,
                'showHint': True}
    clear = ''
    try:
        clear = base64.b64decode(value).decode().strip()
    except binascii.Error:
        clear = base64.b64decode(value.strip() + '+').decode().strip()

    pattern = '^[a-zA-Z0-9!@#]{6,14}$'
    if len(clear) < 6:
        return {'response': False, 'hint': 'too short'}
    if len(clear) > 14:
        return {'response': False, 'hint': 'Too long'}
    if not re.search(pattern, clear):
        return {"response": False, 'hint': 'there are not allowed chars'}
    if sum(map(str.isupper, clear)) < 1:
        return {"response": False, 'hint': 'some capital letters expected'}
    if sum(map(lambda x: x in '!@#', clear)) > 2:
        return {"response": False, 'hint': 'too many special chars'}
    if sum(map(lambda x: x in '0123456789', clear)) < 2:
        return {"response": False, 'hint': 'need more digits'}
    if sum(map(lambda x: x in '0123456789', clear)) > 2:
        return {"response": False, 'hint': 'need less digits'}
    for index, i in enumerate(clear):
        if index < len(clear) - 2 and i.isnumeric() and clear[index + 1].isnumeric():
            return {"response": False, 'hint': 'digits too close'}
    return {"response": True}


@app.route("/challenge01/task2")
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


@app.route("/challenge01/task3")
def task3():
    return {"secretKeyPartEncoded": "YmVzdCBRQSBFbmdp"}
