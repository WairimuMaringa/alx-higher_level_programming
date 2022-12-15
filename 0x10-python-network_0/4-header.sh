#!/bin/bash
# Script that takes a url and displays body of the response
curl -sX GET -H "X-School-User-Id: 98" "${1}"
