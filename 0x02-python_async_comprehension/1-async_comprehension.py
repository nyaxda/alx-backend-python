#!/usr/bin/env python3
"""Async Generators Module"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehensing"""
    result = [value async for value in async_generator()]
    return result
