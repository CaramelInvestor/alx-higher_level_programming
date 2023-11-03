#!/usr/bin/python3

import requests

if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    t = req.text
    print("Body response:")
    print(f"\t- type: {type(t)}")
    print(f"\t- content: {t}")
