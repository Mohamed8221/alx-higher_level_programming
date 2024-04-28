#!/usr/bin/python3
"""json api"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""

    if len(sys.argv) > 1:
        q = sys.argv[1]

    payload = {'q': q}
    r = requests.post(url, data=payload)

    try:
        json_obj = r.json()
        if len(json_obj) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_obj.get('id'), json_obj.get('name')))
    except ValueError:
        print("Not a valid JSON")
