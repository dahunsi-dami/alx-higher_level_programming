#!/usr/bin/python3
"""
Send POST request to URL passed w/ email as parameter
and show response body decoded in utf-8.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    param = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(param).encode('ascii')
    full_url = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(full_url) as response:
        risivd = response.read().decode("utf-8")
        print(risivd)
