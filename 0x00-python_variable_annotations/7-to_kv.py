#!/usr/bin/env python3
"""
Annotation Module
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function to return a tuple"""
    return k, v*v
