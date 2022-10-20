#!/usr/bin/env python3
"""module contains a pymongo method"""


def insert_school(mongo_collection, **kwargs):
    """insert a school"""
    school = {}
    school.update(kwargs)

    return mongo_collection.insert_one(school).inserted_id
