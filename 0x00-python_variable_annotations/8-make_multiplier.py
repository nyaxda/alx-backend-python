#!/usr/bin/env python3
"""
Annotation Module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that returns a function"""
    def multiply(x: float) -> float:
        return x*multiplier
    return multiply
