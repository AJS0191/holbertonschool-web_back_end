#!/usr/bin/env python3
"""First stab at asyncio"""
import asyncio
import random
import time
import typing


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """waits a random amount of time a num of times and returns list"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    waitList = []

    async def chain(max):
        x = await wait_random(max)
        waitList.append(x)

    await asyncio.gather(*(chain(max_delay) for l in range(n)))

    return waitList
