#!/usr/bin/env python3
"""fetches a bunch of HTTP resources using the popular Python requests library"""
import time

import requests


def main():
    """let's do this!"""
    start = time.time()
    urls = [
        f'https://httpbin.org/get?request={i}' for i in range(20)
    ]

    session = requests.Session()
    for url in urls:
        resp = session.get(url)
        #print(resp.json())
    end = time.time()

    print(f'{end - start} seconds')
if __name__ == "__main__":
    main()