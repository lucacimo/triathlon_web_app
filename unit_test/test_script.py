import json
import requests
from test_data import users, workouts, dates

# create the session
s = requests.Session()


def print_request(r, request_type, body=""):
    print request_type, r.url
    for k, v in r.request.headers.iteritems():
        print k, ":", v
    print json.dumps(body, sort_keys=True, indent=4), "\n"


def print_response(r):
    print "Status", ":", r.status_code
    for k, v in r.headers.iteritems():
        print k, ":", v

    if "Content-Length" in r.headers and r.headers['Content-Type'] == "application/json":
        if r.headers["Content-Length"] != "0":
            print json.dumps(r.json(), sort_keys=True, indent=4), "\n"
        else:
            print r.text
    else:
        print r.text


def post_users():
    for user in users:
        parameters={'user': user['name']}
        r = s.post('http://127.0.0.1:8080/profile', params=parameters, json=user)
        print_request(r, "POST", user)
        print_response(r)


def get_users():
    for user in users:
        parameters = {'user': user['name']}
        r = s.get('http://127.0.0.1:8080/profile', params=parameters)
        print_request(r, "GET")
        print_response(r)


def put_users():
    for user in users:
        parameters = {'user': user['name']}
        user['body']["weight"] = 70
        r = s.put('http://127.0.0.1:8080/profile', params=parameters, json=user)
        print_request(r, "PUT", user)
        print_response(r)


def delete_users():
    for user in users:
        parameters = {'user': user['name']}
        r = s.delete('http://127.0.0.1:8080/profile', params=parameters, json=user)
        print_request(r, "DELETE")
        print_response(r)


def post_workouts():
    i = 0
    for workout in workouts:
        parameters={'user':users[0]['name'], 'status':"completed", 'date': dates[i]}
        r = s.post('http://127.0.0.1:8080/workouts', params=parameters, json=workouts[i])
        print_request(r, "POST", workouts[i])
        print_response(r)
        i +=1


def get_workouts():
    i = 0
    for workout in workouts:
        parameters = {'user': users[0]['name'], 'status': "completed", 'date': dates[i]}
        r = s.get('http://127.0.0.1:8080/workouts', params=parameters, json=workouts[i])
        print_request(r, "GET")
        print_response(r)
        i += 1


def put_workouts():
    workouts[0]['distance'] = 80
    workouts[1]['distance'] = 12
    workouts[2]['distance'] = 1.5
    i = 0
    for workout in workouts:
        parameters = {'user': users[0]['name'], 'status': "completed", 'date': dates[i]}
        r = s.put('http://127.0.0.1:8080/workouts', params=parameters, json=workouts[i])
        print_request(r, "PUT", workouts[i])
        print_response(r)
        i += 1


def delete_workouts():
    i = 0
    for workout in workouts:
        parameters = {'user': users[0]['name'], 'status': "completed", 'date': dates[i]}
        r = s.delete('http://127.0.0.1:8080/workouts', params=parameters, json=workouts[i])
        print_request(r, "DELETE", workouts[i])
        print_response(r)
        i += 1


def compute_over_all_statistics():
    parameters = {'user': users[0]['name']}
    r = s.get('http://127.0.0.1:8080/statistics', params=parameters)
    print_request(r, "GET")
    print_response(r)


def compute_statistics_by_sport():
    parameters = {'user': users[0]['name']}
    for workout in workouts:
        parameters = {'user': users[0]['name'], 'sport': workout['type']}
        r = s.get('http://127.0.0.1:8080/statistics', params=parameters)
        print_request(r, "GET")
        print_response(r)


if __name__ == '__main__':
    post_users()
    get_users()
    put_users()
    get_users()
    #delete_users()
    post_workouts()
    get_workouts()
    put_workouts()
    get_workouts()
    delete_workouts()
    post_workouts()
    compute_over_all_statistics()
    compute_statistics_by_sport()
