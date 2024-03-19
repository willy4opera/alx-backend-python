#!/usr/bin/env python3
'''Run time for four parallel comprehensions.
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Run the async_comprehension 4 times and measures the
    total run time.
    '''
    begin = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - begin
