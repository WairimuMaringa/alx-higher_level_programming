#!/usr/bin/python3
"""
Python script that takes url and email address, sends a post
request and displays body of the response
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
