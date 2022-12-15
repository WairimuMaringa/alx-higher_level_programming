#!/bin/bash
# Script that takes a url and shows the allowed options
curl -sI "${1}" | grep "Allow" | cut -d " " -f2-
