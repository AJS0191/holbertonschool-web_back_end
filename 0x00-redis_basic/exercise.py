#!/usr/bin/env python3
"""module containing cache class"""

import uuid
import redis
import typing
from functools import wraps


def replay(method: typing.Callable):
    """takes a method and returns info from the methods calling class"""
    zip(method.self._redis.get('store:input'),
        method.self._redis.lrange('store:input'))


def count_calls(method: typing.Callable) -> typing.Callable:
    """wraps methods and counts how many times they been used"""
    @wraps(method)
    def wrapper(self, data, *args, **kwargs):
        if self._redis.get(method.__qualname__):
            self._redis.incr(method.__qualname__)
        else:
            self._redis.set(method.__qualname__, 0)
        return method(self, data, *args, **kwargs)
    return wrapper


def call_history(method: typing.Callable) -> typing.Callable:
    """saves a call history """
    @wraps(method)
    def wrapper(*args):
        inkey = method.__qualname__ + ':inputs'
        outkey = method.__qualname__ + ':outputs'
        self = args[0]
        self._redis.rpush(inkey, str(args))
        out = method(*args)
        self._redis.rpush(outkey, out)
        return out
    return wrapper


class Cache():
    """cache class connected to a redis server"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
