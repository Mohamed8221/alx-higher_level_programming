#!/usr/bin/python3
"""
This script takes in a repository name and an owner name,
sends a request to the GitHub API and displays the 10 most
recent commits.
It uses the requests and sys packages.
"""

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    r = requests.get(url)
    json_obj = r.json()
    for i in range(10):
        print("{}: {}".format(json_obj[i].get('sha'), json_obj[i].get('commit')
                              .get('author').get('name')))
