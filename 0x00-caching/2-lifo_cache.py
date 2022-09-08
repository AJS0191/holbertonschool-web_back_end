#!/usr/bin/python3
"""basic_cache"""

from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """inherits for BaseCaching has a limit"""
    def __init__(self) -> None:
        """initializes the cache"""
        super().__init__()
        self.queue = deque([])

    def put(self, key, item):
        """adds new item to cache if over max removes last in"""
        if(key and item):
            if(len(self.cache_data) == self.MAX_ITEMS):
                if(key not in self.queue):
                    rem = self.queue.pop()
                    del self.cache_data[rem]
                    print(f"DISCARD: {rem}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """returns the value of the key from cache"""
        if (key in self.cache_data):
            return self.cache_data[key]
        return None
