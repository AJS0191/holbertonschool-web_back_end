#!/usr/bin/env python3
"""Python pagination modules"""

import typing


def index_range(page: int, page_size: int):
    return (((page * page_size) - page_size), (page * page_size))
