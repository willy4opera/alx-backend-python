#!/usr/bin/env python3
'''Measure the runtime
'''
import asyncio
import time


waiting_num = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Caluculates the average runtime of wait_n.
    '''
    start_t = time.time()
    asyncio.run(waiting_num(n, max_delay))
    return (time.time() - start_t) /n
