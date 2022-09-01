#!/usr/bin/env python3
"""First stab at asyncio"""
import asyncio
import time
import typing


async def measure_runtime() -> float:
    """measures runtime"""
    async_comprehension = __import__('1-async_comprehension').async_comprehension
    rt = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    rt = time.perf_counter() - rt
    return rt
