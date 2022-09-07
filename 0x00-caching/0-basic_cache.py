#!/usr/bin/python3
"""basic_cache"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits for BaseCaching has no limit"""
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        if(key and item):
            self.cache_data[key] = item

    def get(self, key):
        if (key in self.cache_data):
            return self.cache_data[key]
        return None
