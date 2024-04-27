#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    req_url = sys.argv[1]
    url_req = urllib.request.Request(req_url)
    with urllib.request.urlopen(url_req) as response:
        print(response.headers.get("X-Request-Id"))
