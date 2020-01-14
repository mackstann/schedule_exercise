from flask import Flask, request, abort, url_for
from flask.json import jsonify

from . import data

app = Flask(__name__)

@app.route('/')
def index():
    # serve the template etc.
    pass

@app.route('/employer_schedules', methods=['GET'])
def employer_schedules():
    return jsonify(data.employer_schedules)
