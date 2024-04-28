#!/usr/bin/python3
"""
This script fetches the URL
https://alx-intranet.hbtn.io/status using the urllib package.
It displays the body response in a specific format.
"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
