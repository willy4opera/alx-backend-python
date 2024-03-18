#!/usr/bin/env python3
'''Task 4.
'''
import asyncio
from typing import List


rand_task_wait = __import__('3-tasks').rand_task_wait


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes rand_task_wait n times.
    '''
    time_wait = await asyncio.gather(
        *tuple(map(lambda _: rand_task_wait(max_delay), range(n)))
    )
    return sorted(time_wait)
