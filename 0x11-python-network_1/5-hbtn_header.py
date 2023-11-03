#!/usr/bin/python3

import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]

    request = request.Request(url)
    with request.Request.urlopen(request) as response:
        header = response.info()
        print(header.get('X-Request-Id'))