#!/usr/bin/env python3
""" to_kv """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """
    to_kv - produce a tuple from the given arguments
    Args:
        k: string value to occupy first position in the tuple
        v: int or float value to occupy second position
    return a tuple
    """
    return (k, v)
