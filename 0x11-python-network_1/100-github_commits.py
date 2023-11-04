#!/usr/bin/python3
"""The Holberton School staff evaluates candidates
applying for a back-end position with multiple
technical challenges, like this one"""

from requests import get
from sys import argv

if __name__ == '__main__':

    repo_name = argv[1]
    owner = argv[2]
    index = 0

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)

    response = get(url)
    format = response.json()

    for element in format:
        if index > 9:
            break
        req = element.get('sha')
        author = element.get('commit').get('author').get('name')
        print("{}: {}".format(req, author))
        index += 1
