#!/usr/bin/env python3
"""
Annotation Module
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function to return the sum of the list of floats"""
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
