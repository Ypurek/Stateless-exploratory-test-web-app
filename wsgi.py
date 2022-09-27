import re
import base64
import string
from flask import Flask, url_for, Response, request, make_response

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static')


@app.route("/lite")
def lite():
    try:
        with open('lite.html', 'r') as index:
            response = make_response(index.read())
            response.set_cookie('secretKeyPartEncoded', 'PDw8PDw8PDw8PDwrKysrKysrKysrKw==')
            return response
    except Exception:
        return 'error during read html happened'


@app.route("/hard")
def hard():
    try:
        with open('hard.html', 'r') as index:
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
                'showHint': True,
                "secretKeyPartEncoded": "KysrKysrKysrKys+Pj4+Pj4+Pj4+Pj4+Pj4+"}

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


@app.route("/task1-help")
def task1_help():
    pattern = '^[a-zA-Z0-9!@#]{6,14}$'
    value = request.args.get('value')
    clear = base64.b64decode(value).decode().strip()
    if len(clear) < 6:
        return {'response': 'Too short'}
    if len(clear) > 14:
        return {'response': 'Too long'}

    check_includes = has_numeric(clear) + has_special(clear) + has_alpha()

    if check_includes == 1:
        return {'response': 'Something is missing'}
    elif check_includes == 2:
        return {'response': 'Close enough, but still not all'}

    if not any([i.isupper() for i in clear]):
        return {'response': 'Capitalize it!'}

    if count_numbers(clear) == 1:
        return {'response': 'We need more numbers'}

    for index, i in enumerate(clear):
        if index < len(clear) - 2 and i.isnumeric() and clear[index + 1].isnumeric():
            return {"response": 'It’s too close, separate them!'}

    if count_special(clear) > 2:
        return {'response': 'It’s too much!'}


def has_special(value: str):
    return 1 if any([i in '!@#' for i in value]) else 0


def has_numeric(value: str):
    return 1 if any([i.isnumeric() for i in value]) else 0


def count_numbers(value: str):
    return sum(map(str.isnumeric, value))


def count_special(value: str):
    return sum(map(lambda x: x in '!@#', value))


def has_alpha(value: str):
    return 1 if any([i.isalpha() for i in value]) else 0
