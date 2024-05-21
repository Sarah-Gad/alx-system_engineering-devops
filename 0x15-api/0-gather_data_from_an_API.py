#!/usr/bin/python3
"""This python script uses rest api to return
information about a user TODO list progress."""
import requests
import sys
if __name__ == "__main__":
    rooturl = "https://jsonplaceholder.typicode.com/"
    req_user = requests.get(rooturl + "users/{}".format(sys.argv[1])).json()
    usertodo = requests.get(
        rooturl + "todos", params={"userId": sys.argv[1]}).json()
    done = [onet.get(
        "title") for onet in usertodo if onet.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        req_user.get("name"), len(done), len(usertodo)))
    [print("\t {}".format(one)) for one in done]
