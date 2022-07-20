#!/usr/bin/env python3

import uuid
import redis
from typing import Union, Optional, Callable
import sys


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

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """
        Get data from cache or call function
        """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, value: bytes) -> str:
        """
        Get data from cache as string
        """
        return value.decode("utf-8")

    def get_int(self, value: bytes) -> str:
        """
        Get data from cache as int
        """
        return int.from_bytes(value, sys.byteorder)
