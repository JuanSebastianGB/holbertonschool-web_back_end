#!/usr/bin/env python3

import uuid
import redis


class Cache():
    """
    Cache class
    """

    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis().flushdb()

    def store(self, data):
        """
        Store data in cache
        """
        key = self.redis.incr(key=uuid.uuid4().hex)
        self.redis.set(key, data)
        return key

    def retrieve(self, key):
        """
        Retrieve data from cache
        """
        return self.redis.get(key)
