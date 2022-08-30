#!/usr/bin/env python3
"""takes str and num returns tuple"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns tuple of str and sq of num"""
    def x(float):
        return float * multiplier
    return x
