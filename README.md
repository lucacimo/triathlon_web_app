# Triathlon web application

Triathlon web app prototype

## Synopsis

This is the backend prototype for a triathlon sport application.

## Code Example

REST API to create, update and manage workouts and retrieve workout statistics. For the API usage and sample codes check the test script

## Installation

Install the following packages:

Install python 2.7

pip install cherrypy

pip install numpy

Run python triathlon_web_app.py, it will run on localhost:8080 by default

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
Check code samples in the test script

## License
CherryPy is distributed under a BSD license.
