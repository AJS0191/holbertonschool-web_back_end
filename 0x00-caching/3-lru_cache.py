#!/usr/bin/python3
"""basic_cache"""

from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """inherits for BaseCaching has a limit"""
    def __init__(self) -> None:
        """initializes the cache"""
        super().__init__()
        self.queue = {}
        self.count = 0

    def put(self, key, item):
        """adds new item to cache if over max removes last in"""
        if(key and item):
            if(len(self.cache_data) == self.MAX_ITEMS):
                if(key not in self.cache_data):
                    rem = LRUlisting(self.queue, key, self.count)
                    del self.cache_data[rem]
                    print(f"DISCARD: {rem}")
            self.cache_data[key] = item
            LRUcountReplace(self.queue, key, self.count)
            self.count = self.count + 1

    def get(self, key):
        """returns the value of the key from cache"""
        if (key in self.cache_data):
            return self.cache_data[key]
        return None


def LRUlisting(queue, newValue, count):
    """takes a dict and removes the lowest count"""
    kholder = []
    for k in queue.keys():
        """keys in this dict are counts values are larger
        dict keys"""
        kholder.append(k)
    kholder.sort()
    rem = kholder[0]
    delKey = queue[rem]
    del queue[rem]
    queue[count] = newValue
    return delKey


def LRUcountReplace(queue, newValue, count):
    """replaces the count for a key being replaced in cache"""
    rem = None
    for k, v in queue.items():
        if v == newValue:
            rem = k
    if rem is None:
        queue[count] = newValue
    else:
        del queue[rem]
        queue[count] = newValue
