import pathlib

from flask import Flask, request, send_from_directory
from flask.json import jsonify

from . import data

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    thisdir = pathlib.Path(__file__).parent.absolute()

    return send_from_directory(thisdir, 'index.html')

@app.route('/employer_schedules', methods=['GET'])
def employer_schedules():
    return jsonify(data.employer_schedules)

@app.route('/schedule_interview', methods=['POST'])
def schedule_interview():
    if not request.is_json:
        # HTTP 415 Unsupported Media Type: ... indicates that the server refuses to accept the request because the
        # payload format is in an unsupported format.
        return error_response(415, 'Only JSON request body is supported')

    try:
        slot_id = request.json['id']
    except KeyError:
        return error_response(400, '`id` field required')

    if not isinstance(slot_id, int):
        return error_response(400, '`id` must be an integer')

    if slot_id not in (slot['id'] for slot in data.employer_schedules):
        # HTTP 409 Conflict: The request could not be completed due to a conflict with the current state of the target
        # resource. This code is used in situations where the user might be able to resolve the conflict and resubmit
        # the request.
        #
        # 400 would also make some sense, but maybe the id submitted is not /wrong/ per se -- maybe it's just bad timing
        # and that slot did exist a minute ago, and was, say, deleted.
        return error_response(409, 'Unknown time slot')

    # Here we'd normally do something to actually book the time slot.

    return '', 204 # Success: HTTP 204 No Content

def error_response(code, message):
    return jsonify({'error': message}), code, {'Content-Type': 'application/json'}
