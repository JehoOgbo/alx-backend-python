#!/usr/bin/env python3
""" async_comprehension """
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension - async comprehension for async generator
    returns a list of floats
    """
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    return result
