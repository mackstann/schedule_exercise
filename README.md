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

# Summary of things you learned

I haven't really touched JavaScript in years now, and it is really great to see how it has progressed. I thought using
vanilla JS would be too crude, but then I discovered `fetch()` and it changed my opinion. Most of the rest was familiar
to some degree; just rusty.

# How you would test it

I would test the API by exercising each of the possible validation problems that I handled in the POST endpoint:
essentially, submit various bad requests and expect to get the right errors.

If it was a real program, I would test the effects of a successful POST to see that the time slot was marked as booked.

I would test the GET endpoint by populating some expected data via a fixture, and then check that the endpoint returns
that same data.

I would test the UI with a browser testing tool like Selenium, which would "click" on the "book it" link and then check
to see that the alert contains a success message and refers to the same appointment that was clicked. It might also
check to see that there was a successful POST to the server in the background, though I'm not sure if that is typical.

I can't speak to writing unit tests for the frontend code, as I haven't done that before.

# Places you struggled

I missed the "propose a new time" feature until it was too late and I didn't have time to implement it. I debated
spending extra time to do it, but the instructions very clearly said to stop at 2 hours, so I kept to the spirit of the
exercise.

I struggled a bit deciding whether to leave the JS as one big block or further organizing it into functions. This
exercise is small enough that I questioned whether breaking it up into functions would be premature and just make it
more complicated than it needs to be. I'm kind of on the fence and either approach seems pretty reasonable, so I went
with the route of least disruption (i.e. leaving it how I wrote it).

# Things you’re proud of

I would like to think my solution is small, simple, and concise; lacking any unnecessary cruft, and conveying the
overall flow of the code clearly. Except the gif, which I threw in because it's fun. This reflects my approach to work
in general.
