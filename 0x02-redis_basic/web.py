#!/usr/bin/env python3
""" Get Page Module """

from typing import Callable
import redis
import requests
from functools import wraps


def count(fn: Callable) -> Callable:
    """ Counts how many times a URL is accessed """

    @wraps(fn)
    def wrapper(url):
        """ Defining the wrapper function """
        key = f'count:{url}'
        r = redis.Redis()
        content = r.get(f'web_cache:{url}')
        if not content:
            content = fn(url)
            r.setnx(key, 0)
            r.incr(key)
            r.setex(f'web_cache:{url}', 10, content)

        return content

    return wrapper


@count
def get_page(url: str) -> str:
    """
    The core of the function is very simple.
    It uses the requests module to obtain the HTML content
    of a particular URL and returns it.
    """
    request = requests.get(url=url)
    content = request.text

    return content
