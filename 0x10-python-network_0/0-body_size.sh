#!/bin/bash
# Script showing content length from a http request
curl -sI "${1}" | grep "Content-Length:" | cut -d " " -f2
