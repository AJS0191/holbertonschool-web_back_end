#!/usr/bin/env python3
"""First stab at asyncio"""
import asyncio
import random
import typing


async def async_comprehension() -> typing.List[float]:
    """waits a random amount of time and returns it"""
    async_generator = __import__('0-async_generator').async_generator
    list = []
    async for i in async_generator():
        list.append(i)
    return list
