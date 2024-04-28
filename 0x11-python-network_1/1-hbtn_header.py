#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response.
It uses the urllib and sys packages.
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
