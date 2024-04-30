#!/usr/bin/python3
"""
Takes your GitHub credentials (username & password) and uses GitHub API
to display your id w/ requests & sys only.
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=basic)
    response = r.json()
    print(response.get("id"))
