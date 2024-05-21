#!/usr/bin/python3
"""This python script exports data in in the JSON format."""
import json
import requests
import sys
if __name__ == "__main__":
    rooturl = "https://jsonplaceholder.typicode.com/"
    req_user = requests.get(rooturl + "users/{}".format(sys.argv[1])).json()
    usertodo = requests.get(
        rooturl + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.json".format(sys.argv[1]), "w") as myjson:
        json.dump({sys.argv[1]: [{
            "task": onet.get("title"),
            "completed": onet.get("completed"),
            "username": req_user.get("name")
        } for onet in usertodo]}, myjson)
