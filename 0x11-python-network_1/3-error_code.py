#!/usr/bin/python3
"""Send request to URL passed & show response body decoded in utf-8."""

import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            risivd = response.read().decode("utf-8")
            print(risivd)
    except HTTPError as e:
        print(f"Error code: {e.code}")
    except URLError as e:
        print(f"URL Error: {e.reason}")
