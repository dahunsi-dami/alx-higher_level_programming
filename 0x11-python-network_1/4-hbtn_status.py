#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status w/ requests pkg only."""

import requests
r = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print("\t- type:", type(r.text))
print("\t- content:", r.text)
