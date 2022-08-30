#!/usr/bin/env python3
"""adding annotation for function"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """adding annotation for function"""
    return [(i, len(i)) for i in lst]
