#!/usr/bin/python3
"""
Send POST request to http://0.0.0.0:5000/search_user
w/ a letter stored in variable `q` as parameter
w/ requests & sys only and show response body.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        val = ""
    elif len(sys.argv) == 2:
        val = sys.argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': val})

    if r.status_code == 200:
        try:
            response = r.json()
            if isinstance(response, list):
                if response:
                    for i in response:
                        user_id = i.get('id')
                        user_name = i.get('name')
                        if user_id is not None and user_name is not None:
                            print(f"[{user_id}] {user_name}")
                        else:
                            print("No result")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
