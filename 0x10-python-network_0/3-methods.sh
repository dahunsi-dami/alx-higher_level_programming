#!/bin/bash
# Takes in URL & show all HTTP methods server accepts
curl -sI $1 | grep -i "Allow" | cut -d " " -f 2-
