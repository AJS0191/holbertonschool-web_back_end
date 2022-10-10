#!/usr/bin/env python3
"""module containing cache class"""

import uuid
import redis


class Cache():
    """cache class connected to a redis server"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str, bytes, int, float) -> str:
        """stores a uuid with data in redis cache"""
        key = str(uuid.uuid3())
        self._redis.set(key, data)
