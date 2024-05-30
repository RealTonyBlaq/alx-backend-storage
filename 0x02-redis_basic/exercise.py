#!/usr/bin/env python3
""" Cache Class """

import redis
from typing import Callable, Union, Optional
import uuid
import 


class Cache:
    """ Defining the cache class. """
    def __init__(self):
        """ Initializing the attributes """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        """ Stores data to Redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]=None) -> Union[None, int, str]:
        """ Retrieve data from Redis """
        data = self._redis.get(key)
        if data:
            return fn(data) if fn else data
        return None

    def get_str(self, key: str) -> str:
        """ Parameterizes Cache.get with the str function """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """ Parameterizes Cache.get with the int function """
        return self.get(key, fn=int)
