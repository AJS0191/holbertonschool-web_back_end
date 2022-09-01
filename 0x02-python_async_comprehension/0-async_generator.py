#!/usr/bin/env python3
"""First stab at asyncio"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, NoneType, NoneType]:
    """waits a random amount of time and returns it"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
