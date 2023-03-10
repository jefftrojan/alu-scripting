#!/usr/bin/python3
""" Queries reddit API and first 10 titles post """
import requests


def top_ten(subreddit):
    """ Set a custom header user-agent """
    headers = {"User-Agent": "ALU scriptting 1.0"}
    url = "https://reddit.com/r/{}.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers, timeout=30,
                                allow_redirects=False)
    except requests.exceptions.Timeout:
        return "Request Timeout! "

    if response.status_code == 200:
        json_data = response.json()
        for posts in range(10):
            print(json_data.get("data").get("children")[posts].get("data").get("title"))

    else:
        print(None)
