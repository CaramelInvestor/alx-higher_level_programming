#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)

    try:
        with request.urlopen(req) as response:
            body = response.read() 
            print(body.decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
