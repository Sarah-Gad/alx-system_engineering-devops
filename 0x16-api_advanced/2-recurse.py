#!/usr/bin/python3
"""This module contains a functiion that will query Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after="", number=0):
    """This fucntion will returns a list containing the titles
    of all hot articles using recursive function"""
    list_of_titles = []
    rd_endpoint = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    rd_headers = {
        "User-Agent": "windows, for 0x16-api_advanced project by Sarah-Gad "
    }
    rd_params = {
        "after": after,
        "number": number
    }
    respo = requests.get(
        rd_endpoint,
        params=rd_params,
        headers=rd_headers,
        allow_redirects=False)
    if respo.status_code == 404:
        return None
    parsed_repos = respo.json().get("data")
    after = parsed_repos.get("after")
    number += parsed_repos.get("dist")
    for one in parsed_repos.get("children"):
        list_of_titles.append(one.get("data").get("tilte"))
    if after is not None:
        recurse(subreddit, hot_list, after, number)
    return list_of_titles
