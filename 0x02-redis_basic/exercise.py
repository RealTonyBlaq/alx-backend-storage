#!/usr/bin/env python3
""" Cache Class """

import redis
import uuid
from typing import Union


class Cache:
    """ Defining the cache class """

    def __init__(self) -> None:
        """ Initializing the attributes """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @coun
    def store(self, data: Union[int, str, float, bytes]) -> str:
        """ Stores data to Redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
