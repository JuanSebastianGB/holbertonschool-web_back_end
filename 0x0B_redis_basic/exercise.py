#!/usr/bin/env python3
""" Exercise """


import uuid
import redis
from typing import Union, Optional, Callable
import sys
from functools import wraps


def count_calls(callback: Callable) -> Callable:
    """ Implementing counter """
    key_counter = callback.__qualname__

    @wraps(callback)
    def wrapper(self, *args, **kwargs):
        """ incr count """
        self._redis.incr(key_counter)
        return callback(self, *args, **kwargs)
    return wrapper


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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

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
