#!/usr/bin/env python3
""" Cache Class """

import redis
import uuid


class Cache:
    """ Defiing the cache class """

    def __init__(self) -> None:
        """ Initializing the attributes """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """ Stores data to Redis """
        key = uuid.uuid4()
        