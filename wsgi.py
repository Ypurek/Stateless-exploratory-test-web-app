import re
import base64
import json
from flask import Flask, url_for, Response, request, make_response

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static')


@app.route("/")
def root():
    try:
        with open('index.html', 'r') as index:
            response = make_response(index.read())
            response.set_cookie('secretKeyPartEncoded', 'PDw8PDw8PDw8PDwrKysrKysrKysrKw==')
            return response
    except Exception:
        return 'error during read html happened'


@app.route("/task1")
def task1():
    value = request.args.get('value')
    # rule: string 6-14 chars
    # only latin chars, at least 1 capital
    # 2 digits, but not next to each other
    # !@# chars allowed, but not more than 2
    # spaces stripped
    if len(value) == 0:
        return {"response": False,
                'showHint': True}

    clear = base64.b64decode(value).decode().strip()
    pattern = '^[a-zA-Z0-9!@#]{6,14}$'
    if not re.search(pattern, clear):
        return {"response": False}
    if sum(map(str.isupper, clear)) < 1:
        return {"response": False}
    if sum(map(lambda x: x in '!@#', clear)) > 2:
        return {"response": False}
    if sum(map(lambda x: x in '0123456789', clear)) != 2:
        return {"response": False}
    for index, i in enumerate(clear):
        if index < len(clear) - 2 and i.isnumeric() and clear[index + 1].isnumeric():
            return {"response": False}
    return {"response": True}


@app.route("/task2")
def task2():
    return {"secretKeyPartEncoded": "KysrKysrKysrKys+Pj4+Pj4+Pj4+Pj4+Pj4+"}


@app.route("/task3")
def task3():
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
