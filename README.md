# schedule_exercise
Code exercise: An interview scheduling tool

# How to Build and Run

This project uses Python 3, so be careful not to accidentally use Python 2 if you have it installed.

    virtualenv env # or maybe virtualenv-3 etc.
    source env/bin/activate
    pip install -r requirements.txt # or maybe pip3 etc.
    FLASK_ENV=development FLASK_APP=schedule.py flask run

The UI will now be available at http://localhost:5000/
