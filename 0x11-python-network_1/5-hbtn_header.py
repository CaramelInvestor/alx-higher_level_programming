#!/usr/bin/python3

import sys
from urllib.request import urlopen

if __name__ == "__main__":
    url = sys.argv[1]

    # request = request.Request(url)
    with urlopen(url) as response:
        header = response.info()
        print(header)
        # print(header.get('X-Request-Id'))