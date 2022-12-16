#!/usr/bin/python3
"""
Python script that takes a url, sends a request to the url
and displays the value of x-request-id
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
