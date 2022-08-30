#!/usr/bin/env python3
"""takes list returns sum"""


def sum_list(input_list: "list[float]") -> float:
    """takes list returns sum"""
    n = 0
    for f in input_list:
        n = n + f
    return n
