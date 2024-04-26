#!/usr/bin/python3
"""Take URL passed, show value of X-Request-ID variable in response header."""

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    hedaz = response.headers
    valpick = hedaz.get('X-Request-ID')
    print(valpick)
