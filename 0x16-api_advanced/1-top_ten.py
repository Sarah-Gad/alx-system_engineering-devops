#!/usr/bin/python3
"""This module contains a functiion that will query Reddit API"""

import requests


def top_ten(subreddit):
    """This fucntion will print the titles of the first hot posts"""
    rd_endpoint = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    rd_headers = {
        "User-Agent": "windows, for 0x16-api_advanced project by Sarah-Gad "
    }
    respo = requests.get(
        rd_endpoint,
        headers=rd_headers,
        allow_redirects=False)
    if respo.status_code == 404:
        print("None")
        return
    alldata = respo.json().get("data").get("children")
    for one in alldata:
        print(one.get("data").get("title"))
