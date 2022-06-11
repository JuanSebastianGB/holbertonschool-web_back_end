#!/usr/bin/env python3
"""FIFO Cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Fifo cache class"""

    def __init__(self):
        """Init"""
        super().__init__()
        self.aux_list = []

    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item
            self.aux_list.append(key)
            if self.cache_data.__len__() > BaseCaching.MAX_ITEMS:
                del self.cache_data[self.aux_list[0]]
                self.aux_list.pop(0)

    def get(self, key):
        if key not in self.cache_data or not self.cache[key]:
            return None
        return self.cache_data[key]
