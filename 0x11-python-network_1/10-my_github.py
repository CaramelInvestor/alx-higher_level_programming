#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""

from sys import argv
from requests import get, auth

if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    url = 'https://api.github.com/user'

    response = get(url, auth=auth.HTTPBasicAuth(username, passwd))
    print(response.json().get('id'))
