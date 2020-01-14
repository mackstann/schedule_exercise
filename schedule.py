from flask import Flask, request, abort, url_for
from flask.json import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # serve the template etc.
    pass
