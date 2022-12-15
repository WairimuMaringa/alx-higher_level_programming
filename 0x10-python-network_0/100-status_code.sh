#!/bin/bash
# Script that sends a request to a url passed and displays response status code only
curl -so /dev/null -w "%{http_code}" "${1}"
