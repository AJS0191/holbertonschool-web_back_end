#!/usr/bin/env python3
"""module contains a pymongo method list_all"""

from pymongo import MongoClient


client = MongoClient()
db = client.my_db


def list_all(mongo_collection):
    """lists all documents in a collection"""
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs
