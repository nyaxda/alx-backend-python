#!/usr/bin/env python3
"""
Annotation Module
"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function to return a list of tuples"""
    return [(i, len(i)) for i in lst]
