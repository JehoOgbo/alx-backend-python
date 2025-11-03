#!/usr/bin/env python3
""" sum_mixed_list """
from typing import Union


Vector = list[Union[float, int]]


def sum_mixed_list(mxd_lst: Vector) -> float:
    """
    sum_mixed_list - find the sum of a list of floats and integers
    Args:
        mxd_lst - a list of floats and integers
    return a float which is the sum of this list
    """
    summation: float = 0.0
    for number in mxd_lst:
        summation += number
    return summation
