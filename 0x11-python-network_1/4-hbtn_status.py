#!/usr/bin/python3

from urllib import request

if __name__ == "__main__":
    request = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {(body)}")
