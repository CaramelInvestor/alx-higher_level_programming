#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id in the response header"""
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    url = sys.argv[1]

    # request = request.Request(url)
    with urlopen(url) as response:
        header = response.info()
        print(header.get('X-Request-Id'))