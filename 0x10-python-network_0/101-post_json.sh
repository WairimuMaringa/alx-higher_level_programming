#!/bin/bash
# Script that sends a json request to a url passed and displays response body
curl -sX POST -H "Content-Type: application/json" -d "@${2}" "${1}"
