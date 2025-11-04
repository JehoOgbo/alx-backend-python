#!/usr/bin/env python3
""" async_generator - coroutine """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async_generator - loop 10 times and each time yield a number
                      between 0 and 10
    yield: random number
    return: None
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
