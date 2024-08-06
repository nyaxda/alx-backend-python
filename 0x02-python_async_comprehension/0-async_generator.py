#!/usr/bin/env python3
"""Async Generators Module"""

from typing import AsyncIterator
import asyncio
import random


async def async_generator() -> AsyncIterator[float]:
    """Async Generator that yields random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0.0, 10.0)
