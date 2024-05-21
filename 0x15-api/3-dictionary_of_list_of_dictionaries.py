#!/usr/bin/python3
"""This python script exports data in in the JSON format."""
import json
import requests

if __name__ == "__main__":
    rooturl = "https://jsonplaceholder.typicode.com/"
    allusers = requests.get(rooturl + "users").json()

    with open("todo_all_employees.json", "w") as myjson:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(rooturl + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in allusers}, myjson)
