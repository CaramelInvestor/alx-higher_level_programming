#!/usr/bin/python3

from urllib import request

if __name__ == "__main__":
    request = request.Request('https://alx-intranet.hbtn.io/status')
    with request.Request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {(content)}")
