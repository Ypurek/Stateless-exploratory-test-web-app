import re
import base64
from flask import Flask, url_for, Response, request, make_response
from challenges import ch01, ch02

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static')
app.register_blueprint(ch01)
app.register_blueprint(ch02)

application = app


@app.route("/")
def root():
    try:
        with open('index.html', 'r') as index:
            return index.read()
    except Exception:
        return 'error during read html happened', 500


if __name__ == "__main__":
    app.run(debug=True)
