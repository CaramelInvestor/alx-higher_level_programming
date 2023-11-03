#!/usr/bin/python3

from urllib.request import Request, urlopen

if __name__ == "__main__":
    request = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: (body)")
