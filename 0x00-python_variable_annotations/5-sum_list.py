#!/usr/bin/env python3
"""takes list returns sum"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes list returns sum"""
    n = 0
    for f in input_list:
        n = n + f
    return n
