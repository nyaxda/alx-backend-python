#!/usr/bin/env python3
""" The module for python async operations"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous function that waits for a random delay and returns it"""
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
