#!/usr/bin/python3
"""
Send request to URL passed & show response body
using requests & sys packages only.
"""

import requests
import sys
from requests.exceptions import HTTPError, ConnectionError

if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except HTTPError as e:
        print(f"Error code: {e.response.status.code}")
    except ConnectionError as e:
        print(f"URL Error: {e}")
