#!/bin/bash
# sends DELETE request to URL it takes in & show response body
curl -X DELETE -is "$1" | awk '/^\r?$/{body=1;next}body'
