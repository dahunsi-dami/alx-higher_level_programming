#!/bin/bash
# sends DELETE request to URL it takes in & show response body
curl -X DELETE -is "$1" | grep -Ev '^$' && echo
