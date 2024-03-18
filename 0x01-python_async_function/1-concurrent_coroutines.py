#!/usr/bin/env python3
'''Let's execute multiple coroutines at
the same time with async
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes n times wait_random.
    '''
    time_waiting = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(time_waiting)
