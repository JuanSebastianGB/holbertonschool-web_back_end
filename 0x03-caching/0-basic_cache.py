#!/usr/bin/env python3
""" Basic cache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BasicCache.MAX_ITEMS:
                self.cache_data.popitem(last=False)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None
