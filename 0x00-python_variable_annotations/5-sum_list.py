#!/usr/bin/env python3
""" Type Declarations """


Vector = list[float]

def sum_list(input_list: Vector) -> float:
    """
    sum_list - add all values of a list
    Args:
        input_list - a list of floats
    return the sum (a float)
    """
    summation: float = 0
    for item in input_list:
        summation += item
    return summation
