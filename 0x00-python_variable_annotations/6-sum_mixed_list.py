#!/usr/bin/env python3
"""takes mixed list returns sum"""


from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """takes mixed list returns sum"""
    n = 0
    for f in input_list:
        n = n + float(f)
    return float(n)
