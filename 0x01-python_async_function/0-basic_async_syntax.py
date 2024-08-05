#!/usr/bin/env python3
""" The module for python async operations"""

import asyncio
import random


async def wait_random(max_delay=10):
    """ Asynchronous function that waits for a random delay """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
