#!/bin/bash
# sends request to URL it takes in & show size of response body
curl -s $1 | wc -c
