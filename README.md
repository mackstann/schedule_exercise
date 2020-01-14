# schedule_exercise
Code exercise: An interview scheduling tool

# How to Build and Run

I'm using Flask, which is a small framework to make serving HTTP cleaner/easier/nicer.

This project uses Python 3, so be careful not to accidentally use Python 2 if you have it installed.

    virtualenv env # or maybe virtualenv-3 etc.
    source env/bin/activate
    pip install -r requirements.txt # or maybe pip3 etc.
    FLASK_ENV=development FLASK_APP=schedule.py flask run

The UI will now be available at http://localhost:5000/

## `POST /schedule_interview` curl examples

Success -> HTTP 204:

    curl -v -X POST http://localhost:5000/schedule_interview -d '{"id": 2}' -H "Content-Type: application/json"

Try to POST JSON without the `id` field -> HTTP 400:

    curl -v -X POST http://localhost:5000/schedule_interview -d '{"foo": 2}' -H "Content-Type: application/json"

Try to schedule a wrongly-typed time slot ID -> HTTP 400:

    curl -v -X POST -s http://localhost:5000/schedule_interview -d '{"id": "hello"}' -H "Content-Type: application/json"

Try to schedule a nonexistent slot ID -> HTTP 409:

    curl -v -X POST -s http://localhost:5000/schedule_interview -d '{"id": 1}' -H "Content-Type: application/json"

Try to POST a non-JSON body -> HTTP 415:

    curl -v -X POST -s http://localhost:5000/schedule_interview -d 'foo'
