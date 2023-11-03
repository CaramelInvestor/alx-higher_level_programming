#!/usr/bin/python3
"""Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a
parameter, and finally displays the body of the response"""
import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    # data = parse.urlencode(data)
    # data = data.encode('ascii')

    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read())