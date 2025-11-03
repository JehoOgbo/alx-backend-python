#!/usr/bin/env python3
""" element_length """
from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> list[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
