#!/usr/bin/env python3
"""
Annotation Module
"""
from typing import Sequence, List, Tuple


def element_length(lst: Sequence[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
