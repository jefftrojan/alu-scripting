#!/usr/bin/python3
""" Queries reddit API and first 10 titles post """
import requests


def top_ten(subreddit):
    headers = {"User-Agent": "ALU-scripting API 0.1" }
    url = "https://reddit.com/r/{}.json".format(subreddit)
    
    try:
	response = requests.get(url, headers=headers, timeout=30, allow_redirects=False)
    except requests.exceptions.Timeout:
	return " The Request Timed Out!"
    	
