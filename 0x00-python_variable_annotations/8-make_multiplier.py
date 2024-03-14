#!/usr/bin/env python3

'''Complex types - functions.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Here, we create a multiplier function.
    '''
    return lambda x: x * multiplier
