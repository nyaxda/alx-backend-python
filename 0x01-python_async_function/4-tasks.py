#!/usr/bin/env python3
""" The module for python async operations"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function that returns a list of delays"""
    wait_delay = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]
    delay = []

    for task in asyncio.as_completed(wait_delay):
        result = await task
        delay.append(result)
    return sorted(delay)
