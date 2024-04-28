#!/usr/bin/python3
"""my github"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]

    r = requests.get(url, auth=HTTPBasicAuth(username, token))
    json_obj = r.json()
    print(json_obj.get('id'))
