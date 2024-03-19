#!/usr/bin/env python3

'''Async Generator
'''
import asyncio
import random


async def async_generator():
    '''Here, we generated a sequence of 10 numbers.ls
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
