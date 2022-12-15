#!/bin/bash
# Script that makes a request and give a response
curl -sX PUT 0.0.0.0:5000/catch_me -d -H "You got me!" -L
