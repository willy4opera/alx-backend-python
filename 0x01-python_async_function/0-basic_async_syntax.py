#!/usr/bin/env python3
'''The basics of async 
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Random number of seconds waiting
    '''
    time_wait = random.random() * max_delay
    time_wait = random.random() * max_delay
    await asyncio.sleep(time_wait)
    return time_wait
