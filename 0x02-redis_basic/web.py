#!/usr/bin/env python3
""" Get Page Module """

import requests
import redis


def get_page(url: str) -> str:
    """
    The core of the function is very simple.
    It uses the requests module to obtain the HTML content
    of a particular URL and returns it.
    """
    request = requests.get(url=url)
    content = request.content

    r = redis.Redis()
    r.setnx(f'count:{url}', 0)
    r.incr(f'count:{url}')
    r.expire()
