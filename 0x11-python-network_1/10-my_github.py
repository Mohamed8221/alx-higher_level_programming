#!/usr/bin/python3
"""
This script takes your GitHub credentials
(username and password) and uses the GitHub API to display your id.
It uses Basic Authentication with a personal access token as
password to access to your information.
It uses the requests and sys packages.
"""

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
