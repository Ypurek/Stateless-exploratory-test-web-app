import re
import base64
import string
from flask import Flask, url_for, Response, request, make_response

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static')


@app.route("/")
def index():
    try:
        with open('index.html', 'r') as index:
            response = make_response(index.read())
            response.set_cookie('secretKeyPartEncoded', 'PDw8PDw8PDw8PDwrKysrKysrKysrKw==')
            return response
    except Exception:
        return 'error during read html happened'


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
def task1_new():
    pattern = '^[a-zA-Z0-9!@#]{6,14}$'
    value = request.args.get('value')
    clear = base64.b64decode(value).decode()
    if len(clear) == 0:
        return {'response': 'Not ok'}
    if clear == ' ':
        return {'response': 'Not ok!'}
    if len(clear) < 6:
        return {'response': 'Too short'}
    if len(clear) > 14:
        return {'response': 'Too long'}

    if not re.search(pattern, clear):
        return {"response": 'Too much'}

    check_includes = has_numeric(clear) + has_special(clear) + has_alpha(clear)

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

    return {'response': 'OK'}


@app.route("/task1-hard")
def task1_new_hard():
    pattern = '^[a-zA-Z0-9!@#]{6,14}$'
    value = request.args.get('value')
    clear = base64.b64decode(value).decode()
    if len(clear) == 0:
        return {'response': 'Not ok'}
    if clear == ' ':
        return {'response': 'Not ok!'}
    if len(clear) < 6:
        return {'response': 'Too short'}
    if len(clear) > 14:
        return {'response': 'Too long'}

    if not re.search(pattern, clear):
        return {"response": 'Too much'}

    check_includes = has_numeric(clear) + has_special(clear) + has_alpha(clear)

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

    if clear == 'a!yT1Q6dB#v':
        return {'response': 'secretKeyPartEncoded: KysrKysrKysrKys+Pj4+Pj4+Pj4+Pj4+Pj4+'}

    return {'response': 'OK'}


@app.route("/task-help")
def task1_help():
    value = request.args.get('value')
    if value.isnumeric():
        num = int(value)
        if 0 <= num <= 19:
            return {'response': 'Warmer! a!yT1Q6dB#v will help you!'}
        elif 19 < num <= 26:
            return {'response': 'Hot! %hint%'}
        elif num >= 27:
            return {'response': 'Warmer! a!yT1Q6dB#v will help you!'}

    return {'response': 'Cold! Try something else!'}


@app.route("/task-help-hard")
def task1_help_hard():
    value = request.args.get('value')
    if value.isnumeric():
        num = int(value)
        if 0 <= num <= 19:
            return {
                'response': 'Warmer! a!yT1Q6dB#v will help you! And to find a secret key remember that mature QA also looks inside the box!'}
        elif 19 < num <= 26:
            return {
                'response': 'Hot! To find a secret key check CSS, Cookies and Network!  Let the a!yT1Q6dB#v guide you!'}
        elif num >= 27:
            return {'response': 'Warmer! a!yT1Q6dB#v will help you!'}

    return {'response': 'Cold! Try something else!'}


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


if __name__ == "__main__":
    app.run(debug=True)
