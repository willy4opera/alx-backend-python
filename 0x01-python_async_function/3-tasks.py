#!/usr/bin/env python3
'''3. Tasks
'''
import asyncio


random_wait = __import__('0-basic_async_syntax').random_wait


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates an asynchronous task for random_wait.
    '''
    return asyncio.create_task(random_wait(max_delay))
