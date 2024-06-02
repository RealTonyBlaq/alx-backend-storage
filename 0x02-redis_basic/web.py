#!/usr/bin/env python3
""" Get Page Module """

import requests
import redis
from datetime import timedelta


def get_page(url: str) -> str:
    """
    The core of the function is very simple.
    It uses the requests module to obtain the HTML content
    of a particular URL and returns it.
    """
    request = requests.get(url=url)
    content = request.text
    key = f'count:{url}'

    r = redis.Redis()
    r.setnx(key, 0)
    r.incr(key)
    r.setex(f'web_cache:{url}', timedelta(seconds=10), content)

    return content
