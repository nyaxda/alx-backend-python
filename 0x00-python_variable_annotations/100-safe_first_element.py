#!/usr/bin/env python3
"""
Annotation Module
"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function to return the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
