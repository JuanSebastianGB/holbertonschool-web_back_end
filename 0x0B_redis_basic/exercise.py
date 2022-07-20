#!/usr/bin/env python3

import uuid
import redis
from typing import Union


class Cache():
    """
    Cache class
    """

    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def retrieve(self, key):
        """
        Retrieve data from cache
        """
        return self.redis.get(key)
