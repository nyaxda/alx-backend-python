#!/usr/bin/env python3
"""
Annotation Module
"""
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """function to return the sum of the list of floats"""
    sum: Union[int, float] = 0
    for i in input_list:
        sum += i
    return sum
