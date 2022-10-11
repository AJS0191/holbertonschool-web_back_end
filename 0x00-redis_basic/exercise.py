#!/usr/bin/env python3
"""module containing cache class"""

import uuid
import redis
import typing
from functools import wraps


def count_calls(method: typing.Callable) -> typing.Callable:
    """wraps methods and counts how many times they been used"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        if args[0]._redis.get(method.__qualname__):
            args[0]._redis.incr(method.__qualname__)
        else:
            args[0]._redis.set(method.__qualname__)
        return method(*args, **kwargs)
    return wrapper


class Cache():
    """cache class connected to a redis server"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """stores a uuid with data in redis cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None) -> None:
        """uses fn to change value of key to original datatype"""
        val = self._redis.get(key)
        if not val:
            return None
        if fn:
            return fn(val)
        return val

    def get_str(val: bytes) -> str:
        """changes val to str, its original data type"""
        return val.decode('utf-8')

    def get_int(val: bytes) -> int:
        """changes val to int, its original data type"""
        return int.from_bytes(val)
