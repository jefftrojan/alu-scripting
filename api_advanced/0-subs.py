#!/usr/bin/python3
""" 
Function that queries Reddit API and returns the number of subscribers
"""

import requests

URL = 'https://'

""" 

    Function to get the number of subscribers 

"""
def number_of_subscribers(subreddit):
    # Set custom user-agent header
    headers = {'User-Agent': 'ALU-scripting API 0.1'}
    url = f"https://www.reddit.com/r/{subreddit}.json"

    try:
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=False)
    except requests.exceptions.Timeout:
        return "The request Timed out"

    if response.status_code == 200:
        json_data = response.json()
        return json_data