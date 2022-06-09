#!/usr/bin/env python3

""" Async Generator """

from random import uniform
import asyncio


async def async_generator():
    """
    It's a generator that yields a random number every second
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
