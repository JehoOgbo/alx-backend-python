#!/usr/bin/env python3
""" make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier - make a function that multiplies a float by
                      a multiplier
    Args:
        multiplier: float to be used as multiplier in new function
    return a function
    """
    def multiply_function(number: float) -> float:
        return number * multiplier
    return multiply_function
