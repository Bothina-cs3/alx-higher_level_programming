#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve this challenge.
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    params = {'per_page': 10}
    res = requests.get(url, params=params)
    commits = res.json()
    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))
