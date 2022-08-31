#!/usr/bin/env python3
"""First stab at asyncio"""
import asyncio
import random
import time
import typing


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns an async task"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
