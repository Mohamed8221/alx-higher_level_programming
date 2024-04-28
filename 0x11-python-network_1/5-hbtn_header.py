#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in
the header of the response.
It uses the requests and sys packages.
"""

import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
