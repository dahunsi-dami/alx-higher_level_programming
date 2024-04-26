#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status w/ urllib."""

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print('Body response:')
    line_rec = response.read()
    print("\t- type:", type(line_rec))
    print("\t- content:", line_rec)
    print("\t- utf8 content:", line_rec.decode('utf-8'))
