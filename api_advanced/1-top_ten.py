#!/usr/bin/python3
""" Queries reddit API and first 10 titles post """
import requests


def top_ten(subreddit):
    headers = {"User-Agent": "ALU scriptting 1.0"}
    url = "https://www.reddit.com/r/{}.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=False)
    except requests.exceptions.Timeout:
        return "Request Timeout! "

    if response.status_code != 200:
        print(None)

    else:
        json_data = response.json()
        for i in range(10):
            print(json_data.get("data").get("children").get("title"))
