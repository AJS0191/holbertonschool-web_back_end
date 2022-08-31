#!/usr/bin/env python3
"""First stab at asyncio"""
import asyncio
import random
import time
import typing


def measure_time(n: int, max_delay: int) -> float:
    """returns time it takes to make the random list"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    curentT = time.perf_counter()
    result = loop.run_until_complete(wait_n(n, max_delay))
    totalTime = time.perf_counter() - curentT
    return totalTime / float(n)
