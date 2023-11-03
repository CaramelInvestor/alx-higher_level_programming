#!/usr/bin/python3

from urllib import request

if __name__ == "__main__":
    req = request.get('https://alx-intranet.hbtn.io/status')
    t = req.text
    print("Body response:")
    print(f"\t- type: {type(t)}")
    print(f"\t- content: {t}")
