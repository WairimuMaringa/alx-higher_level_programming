#!/bin/bash
# Script that sends a post request and displays response body
curl -sX POST "${1}" -d "email=test@gmail.com&subject=I will always be here for PLD"
