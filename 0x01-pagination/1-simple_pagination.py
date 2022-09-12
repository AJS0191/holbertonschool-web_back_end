#!/usr/bin/env python3
"""Python pagination modules"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves pages and puts them into list based on size"""
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0

        dataSet = self.dataset()
        indexRan = index_range(page, page_size)
        showPages = []
        size = indexRan[1]
        start = indexRan[0]

        for i in range((size * start), (size * start) + size + 1):
            showPages.append(dataSet[i])

        return showPages


def index_range(page: int, page_size: int):
    """finds the index range with the page and page size"""
    return (((page * page_size) - page_size), (page * page_size))
