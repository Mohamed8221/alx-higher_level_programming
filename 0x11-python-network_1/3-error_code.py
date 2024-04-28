#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response.
If the HTTP status code is greater than or equal to 400,
it prints: Error code: followed by the HTTP status code.
It uses the urllib and sys packages.
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
