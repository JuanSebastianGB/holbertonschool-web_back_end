#!/usr/bin/python3
''' LFUCache '''


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' LFU Cache '''

    def __init__(self):
        ''' Initialize LFUCache '''
        self.aux_list = []
        self.aux_dict = {}
        super().__init__()

    def _get_less_used(self):
        """
        It returns the key of the item in the dictionary with the lowest value
        :return: The key of the least used value in the aux_dict.
        """
        from functools import reduce
        return reduce(lambda x, y: x if x[1] < y[1] else y,
                      self.aux_dict.items())[0]

    def put(self, key, item):
        """
        If the key and item are not empty, and the cache is not full,
        add the key and item to the cache.
        If the cache is full, remove the least used item from the cache
        and the auxiliary dictionary

        :param key: the key to be added to the cache
        :param item: the item to be added to the cache
        """
        if key and item:
            if self.cache_data.__len__() >= BaseCaching.MAX_ITEMS:
                if self.aux_dict:
                    less_used_key = self._get_less_used()
                    if self.cache_data.get(less_used_key):
                        del self.cache_data[less_used_key]
                    if self.aux_dict.get(key):
                        del self.aux_dict[key]

            self.cache_data[key] = item
            """ self.aux_list.append(item) """

    def get(self, key):
        """
        If the key is in the cache, then return the value of the key

        :param key: The key to be searched in the cache
        :return: The value of the key in the cache_data dictionary.
        """
        if key in self.cache_data and key:
            """ self.aux_list.remove(key)
            self.aux_list.append(key) """
            if key in self.aux_list:
                self.aux_dict[key] += 1
            else:
                self.aux_dict[key] = 0
            return self.cache_data[key]
