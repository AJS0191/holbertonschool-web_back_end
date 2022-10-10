#!/usr/bin/env python3

import uuid
import redis


class Cache():
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str, bytes, int, float) -> str:
        key = str(uuid.uuid3())
        self._redis.set(key, data)
