#!/usr/bin/env python3
"""First stab at asyncio"""
import asyncio
import random
import time
import typing


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """waits a random amount of time a num of times and returns list"""
    task_wait_random = __import__('3-tasks').task_wait_random
    waitList = []

    async def chain(max):
        x = await task_wait_random(max)
        waitList.append(float(x))

    await asyncio.gather(*(chain(max_delay) for l in range(n)))

    return waitList
