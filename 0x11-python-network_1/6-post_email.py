#!/usr/bin/python3
"""
Send POST request to URL passed w/ email as parameter
w/ requests & sys only and show response body.
"""

import requests
import sys

if __name__ == "__main__":
    payload = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], params=payload)
    print(r.text)
