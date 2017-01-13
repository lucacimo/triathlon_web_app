import cherrypy
import jsonschema
import os
import datetime
from tools import *


def look_up_user_profile(user):
    if user in cherrypy.session:
        profile = cherrypy.session[user]['profile']
        return profile
    else:
        return False


def look_up_workout(user, date, status):
    user_profile=look_up_user_profile(user)
    if not user_profile:
        return False

    if "workouts" in cherrypy.session[user]:
        if date in cherrypy.session[user]['workouts'][status]:
            workout = cherrypy.session[user]['workouts'][status][date]
            return workout
        else:
            return False


def validate_message(data, schema):
    try:
        jsonschema.validate(data, json.loads(schema))
    except jsonschema.ValidationError as e:
        raise cherrypy.HTTPError(400, e)
    except jsonschema.SchemaError as e:
        raise cherrypy.HTTPError(400, e)


def validate_params(status, date):
    if status not in ["planned", 'completed']:
        raise cherrypy.HTTPError(400, "status parameter not valid")
    try:
        validate_date(date)
    except ValueError:
        raise cherrypy.HTTPError(400, "wrong date format")


def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


@cherrypy.expose
class WorkoutStatisticsWebService(object):

    @cherrypy.tools.json_out()
    def GET(self, user, sport = None):

        if sport not in ["cycling", "running", "swimming", None]:
            raise cherrypy.HTTPError(400, "Invalid sport parameter")

        user_profile = look_up_user_profile(user)
        if not user_profile:
            raise cherrypy.HTTPError("404", "Profile not found")

        if "workouts" in cherrypy.session[user]:
            # compute overall statistics
            if sport is None:
                return compute_workouts_statistics(cherrypy.session[user]['workouts']['completed'])

            # compute statistics by sport
            workouts = filter_workouts_by_sport(cherrypy.session[user]['workouts']['completed'], sport)
            return compute_workouts_statistics(workouts, sport)

        else:
            return null_stats


@cherrypy.expose
class UserProfileWebService(object):

    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_out()
    def GET(self, user):
        user_profile = look_up_user_profile(user)
        if not user_profile:
            raise cherrypy.HTTPError("404", "Profile not found")
        return user_profile

    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_in()
    def POST(self, user):
        cherrypy.session[user] = {}
        cherrypy.session[user]['workouts'] = {}
        cherrypy.session[user]['workouts']['planned'] = {}
        cherrypy.session[user]['workouts']['completed'] = {}

        try:
            path = os.path.join(os.getcwd(), "json_schema/user_profile_schema.json")
            schema = open(path).read()
            data = cherrypy.request.json
            validate_message(data, schema)

            cherrypy.session[user]['profile'] = from_json_to_object(data)
            cherrypy.response.status = '201 Created'

        except RuntimeError:
            raise cherrypy.HTTPError(500, "Something went wrong when creating the user profile")

    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_in()
    def PUT(self, user):
        try:
            path = os.path.join(os.getcwd(), "json_schema/user_profile_schema.json")
            schema = open(path).read()
            data = cherrypy.request.json
            validate_message(data, schema)

            user_profile = look_up_user_profile(user)
            if not user_profile:
                raise cherrypy.HTTPError("404", "Profile not found")

            cherrypy.session[user]['profile'] = from_json_to_object(data)

        except RuntimeError:
            raise cherrypy.HTTPError(500, "Something went wrong when updating the profile")

    def DELETE(self, user):
        user_profile = look_up_user_profile(user)
        if not user_profile:
            raise cherrypy.HTTPError("404", "Profile not found")
        del cherrypy.session[user]
        cherrypy.response.status = '204 Deleted'


@cherrypy.expose
class WorkoutsWebService(object):

    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_out()
    def GET(self, user, date, status):
        validate_params(status, date)

        workout = look_up_workout(user, date, status)
        if not workout:
            raise cherrypy.HTTPError(404, "workout not found")
        return workout

    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_in()
    def POST(self, user, status, date):

        try:
            path = os.path.join(os.getcwd(), "json_schema/workout_schema.json")
            schema = open(path).read()
            data = cherrypy.request.json
            validate_message(data, schema)

            user_profile = look_up_user_profile(user)
            if not user_profile:
                raise cherrypy.HTTPError("404", "Profile not found")

            cherrypy.session[user]['workouts'][status][date] = from_json_to_object(data)
            cherrypy.response.status = '201 Created'

        except RuntimeError:
            raise cherrypy.HTTPError(500, "Something went wrong when creating a workout")

    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_in()
    def PUT(self, user, status, date):
        validate_params(status, date)

        try:
            path = os.path.join(os.getcwd(), "json_schema/workout_schema.json")
            schema = open(path).read()
            data = cherrypy.request.json
            validate_message(data, schema)

            workout = look_up_workout(user, date, status)
            if not workout:
                raise cherrypy.HTTPError(404, "workout not found")

            cherrypy.session[user]['workouts'][status][date] = from_json_to_object(data)

        except RuntimeError:
            raise cherrypy.HTTPError(500, "Something went wrong when updating a workout")

    def DELETE(self, user, status, date):
        validate_params(status, date)

        user_profile = look_up_user_profile(user)
        if not user_profile:
            raise cherrypy.HTTPError("404", "Profile not found")

        workout = look_up_workout(user, date, status)
        if not workout:
            raise cherrypy.HTTPError(404, "workout not found")

        del cherrypy.session[user]['workouts'][status][date]
        cherrypy.response.status = '204 Deleted'


if __name__ == '__main__':
    users = {"luca": "secretpassword",
             "otheruser": "otherpassword"}

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
            'tools.digest_auth.on': False,
            'tools.digest_auth.realm': 'Some site',
            'tools.digest_auth.users': users
        }


    }

    cherrypy.tree.mount(UserProfileWebService(), '/profile', conf)
    cherrypy.tree.mount(WorkoutsWebService(), '/workouts', conf)
    cherrypy.tree.mount(WorkoutStatisticsWebService(), '/statistics', conf)
    cherrypy.engine.start()
