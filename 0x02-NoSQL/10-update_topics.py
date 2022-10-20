#!/usr/bin/env python3
"""module contains a pymongo method"""


def update_topics(mongo_collection, name, topics):
    """update topics in doc"""
    mongo_collection.update_one(
        {name: name},
        {
            "$set": {
                topics: topics
            }
        }
    )
