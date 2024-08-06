#!/usr/bin/env python3
"""Async Generators Module"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension"""
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    stop_time = time.time()
    total_runtime = stop_time - start_time

    return total_runtime
