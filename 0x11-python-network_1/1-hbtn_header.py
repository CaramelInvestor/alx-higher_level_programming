#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response"""

import sys, urllib.request

url = sys.argv[1]
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    header = response.info()
    x_request_id = header.get("X-Request-Id")
    print(x_request_id)
