#!/usr/bin/python3
"""
This script fetches the URL https://alx-intranet.hbtn.io/status
using the requests package.
It displays the body response in a specific format.
"""

import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
