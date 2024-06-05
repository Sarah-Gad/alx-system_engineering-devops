#!/usr/bin/python3
"""This module contains a functiion that will query Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """This fucntion will returns a list containing the titles
    of all hot articles using recursive function"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "windows, for 0x16-api_advanced project by Sarah-Gad "
    }
    params = {'limit': 100}

    if after:
        params['after'] = after
    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                hot_list.append(post['data']['title'])

            if data['data']['after']:
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
    