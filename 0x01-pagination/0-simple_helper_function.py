#!/usr/bin/env python3
"""Python pagination modules"""

import typing


def index_range(page: int, page_size: int):
    """finds the index range with the page and page size"""
    return (((page * page_size) - page_size), (page * page_size))
