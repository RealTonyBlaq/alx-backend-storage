#!/usr/bin/env python3
""" Cache Class """

import redis
from typing import Callable, Union, Optional
import uuid
from functools import wraps


def replay(fn: Callable) -> None:
    """ Displays the history of calls of a particular function """
    r = redis.Redis()
    method = str(fn.__qualname__)
    if r.exists(method) > 0:
        call_count = int(r.get(method))
        input_history = r.lrange(f'{method}:inputs', 0, -1)
        output_history = r.lrange(f'{method}:outputs', 0, -1)
        print(f'{method} was called {call_count} times:')
        for input, output in zip(input_history, output_history):
            try:
                output = output.decode('utf-8')
                input = int(input)
            except ValueError:
                input = input.decode('utf-8')
            finally:
                print(f'{method}(*{input}) -> {output}')


def count_calls(f: Callable) -> Callable:
    """ Defines a wrapper function """
    key = f.__qualname__

    @wraps(f)
    def wrapper(self, *args, **kwargs):
        """ Returns the Callable f() """
        self._redis.setnx(key, 0)
        self._redis.incr(key)
        return f(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Defines the call_history wrapper function """
    dec_key = method.__qualname__

    @wraps(method)
    def call_wrapper(self, *args, **kwargs):
        """ Returns the callable method() """
        if args:
            self._redis.rpush(f'{dec_key}:inputs', str(args))
            value = method(self, *args, **kwargs)
            self._redis.rpush(f'{dec_key}:outputs', value)
            return value

    return call_wrapper


class Cache:
    """ Defining the cache class. """
    def __init__(self):
        """ Initializing the attributes """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[int, str, float, bytes]) -> str:
        """ Stores data to Redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[None,
                                                                    int, str]:
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
