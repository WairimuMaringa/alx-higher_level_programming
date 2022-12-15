#!/bin bash
# Script showng content-length froma http request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
