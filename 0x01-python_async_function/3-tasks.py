#!/usr/bin/env python3
""" The module for python async operations"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function that returns the max delay"""
    return asyncio.create_task(wait_random(max_delay))
