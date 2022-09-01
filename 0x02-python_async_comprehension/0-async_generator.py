#!/usr/bin/env python3
"""First stab at asyncio"""
import asyncio
import random


async def async_generator() -> float:
    """waits a random amount of time and returns it"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
