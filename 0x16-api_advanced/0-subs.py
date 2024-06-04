#!/usr/bin/python3
"""This module contains a functiion that will query Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """This fucntion will return the number of subscribers"""
    rd_endpoint = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    rd_headers = {
        "User-Agent": "windows, for 0x16-api_advanced project by Sarah-Gad "
    }
    respo = requests.get(
        rd_endpoint,
        headers=rd_headers,
        allow_redirects=False)
    if respo.status_code == 404:
        return 0
    return respo.json().get("data").get("subscribers")
