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
        start = indexRan[0]
        size = indexRan[1]

        if size > len(dataSet):
            return []

        i = 1

        for i in range(start, size):
            showPages.append(dataSet[i])

        return showPages

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary of details about pages requested"""
        dataSet = self.dataset()

        data = self.get_page(page, page_size)
        pg_size = len(data)
        pg = index_range(page, page_size)[0]
        total_pages = int(len(dataSet) / index_range(page, page_size)[1])

        if pg_size == 0 or pg == total_pages:
            next_page = None
        else:
            next_page = pg + 1

        if pg == 1:
            prev_page = None
        else:
            prev_page = pg - 1

        details = {
            "page_size": pg_size,
            "page": pg,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int):
    """finds the index range with the page and page size"""
    return (((page * page_size) - page_size), (page * page_size))
