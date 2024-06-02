#!/usr/bin/python3
""" Testing Replay() """

replay = __import__('exercise').replay
Cache = __import__('exercise').Cache

cache = Cache()
cache.store('foo')
cache.store('bar')
cache.store('alright')
cache.store('okay')
cache.store(23)

replay(cache.store)
