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
        from functools import reduce
        return reduce(lambda x, y: x if x[1] < y[1] else y, self.aux_dict.items())[0]

    def put(self, key, item):
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
        if key in self.cache_data and key:
            """ self.aux_list.remove(key)
            self.aux_list.append(key) """
            if key in self.aux_list:
                self.aux_dict[key] += 1
            else:
                self.aux_dict[key] = 0
            return self.cache_data[key]
