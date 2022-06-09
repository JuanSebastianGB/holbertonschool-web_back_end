#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions  """
from asyncio import gather, run
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    It measures the time it takes to run four async comprehensions
    :return: The time it takes to run the async_comprehension function 4 times.
    """
    start = time.time()
    for i in range(4):
        await gather(async_comprehension())
    end = time.time()
    return end - start
