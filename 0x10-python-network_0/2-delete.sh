#!/bin/bash
# sends DELETE request to URL it takes in & show response body
curl -X DELETE -s "$1" | grep -Ev '^$' && echo
