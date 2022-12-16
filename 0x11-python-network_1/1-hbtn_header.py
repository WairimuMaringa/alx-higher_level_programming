#!/usr/bin/python3
"""
Python script that takes a url, sends a request and displays
the value of x-request id variable found in the header
"""
import urllib.request
import sys


if __name__ "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
