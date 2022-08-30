#!/usr/bin/env python3
"""takes str and num returns tuple"""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple of str and sq of num"""
    t = (k, float(v*v))
    return t
