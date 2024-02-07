#!/usr/bin/python3
""" Module: 101-stats """

import sys

file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for i, line in enumerate(sys.stdin, 1):
        data = line.split()
        if len(data) > 2:
            status_code = data[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
            file_size += int(data[-1])
        if i % 10 == 0:
            print("File size: {}".format(file_size))
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print("{}: {}".format(code, count))
finally:
    print("File size: {}".format(file_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))
