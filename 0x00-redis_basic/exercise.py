#!/usr/bin/env python3
"""module containing cache class"""

import uuid
import redis
import typing


class Cache():
    """cache class connected to a redis server"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """stores a uuid with data in redis cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, b(data))
        return key
