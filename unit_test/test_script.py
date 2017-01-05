import json
import requests
from test_data import users

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


if __name__ == '__main__':
    post_users()
    get_users()
    put_users()
    get_users()
    delete_users()