#!/usr/bin/python3
"""
Send request to URL passed & show value of X-Request-ID variable
in response header.
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
