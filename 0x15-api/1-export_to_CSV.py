#!/usr/bin/python3
"""This python script exports data in the CSV format."""
import csv
import requests
import sys
if __name__ == "__main__":
    rooturl = "https://jsonplaceholder.typicode.com/"
    req_user = requests.get(rooturl + "users/{}".format(sys.argv[1])).json()
    usertodo = requests.get(
        rooturl + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as mycsv:
        rowwriter = csv.writer(mycsv, quoting=csv.QUOTE_ALL)
        [rowwriter.writerow(
            [sys.argv[1], req_user.get("username"),
             onet.get("completed"), onet.get("title")]
        ) for onet in usertodo]
