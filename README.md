# Triathlon web application

Triathlon web app prototype.

## Synopsis

This is the backend prototype for a triathlon sport application.

## Code Example

REST API to create, update and manage workouts and retrieve workout statistics. For the API usage and sample code check the test script

## Installation

Install the following packages:

1. install python 2.7
2. pip install -r requirements.txt

Run python triathlon_web_app.py, it will run on localhost:8080 by default.

## API Reference

User profile creation:

POST http://127.0.0.1:8080/profile?user=username

Retrieve user profile:

GET http://127.0.0.1:8080/profile?user=username

Update user profile:

PUT http://127.0.0.1:8080/profile?user=username

Delete user profile:

DELETE http://127.0.0.1:8080/profile?user=username

Workout creation:

Status "completed" or "planned"

POST http://127.0.0.1:8080/workouts?status=completed&date=YY-MM-DD&user=username

Retrieve workout:

Status "completed" or "planned"

GET http://127.0.0.1:8080/workouts?status=completed&date=YY-MM-DD&user=username

Update workout:

PUT http://127.0.0.1:8080/workouts?status=completed&date=YY-MM-DD&user=username

Delete workout:

DELETE http://127.0.0.1:8080/workouts?status=completed&date=YY-MM-DD&user=username

Retrieve overall statistics:

GET http://127.0.0.1:8080/statistics?user=username

Retrieve statistics by sport:

Sport "cycling" or "running" or "swimming"

GET http://127.0.0.1:8080/statistics?sport=cycling&user=username

## Tests
Check code samples in the test script.

## References
[1] http://www.ibm.com/developerworks/library/ws-restful/index.html

[2] http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api

[3] http://docs.cherrypy.org/en/latest/

[4] http://home.trainingpeaks.com/blog/article/joe-friel-s-quick-guide-to-setting-zones

## License
CherryPy is distributed under a BSD license.
