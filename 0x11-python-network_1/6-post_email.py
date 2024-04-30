#!/usr/bin/python3
"""
Send POST request to URL passed w/ email as parameter
w/ requests & sys only and show response body.
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
