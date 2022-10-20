#!/usr/bin/env python3

from pymongo import MongoClient


client = MongoClient()
db = client.my_db


def list_all(mongo_collection):
    """lists all documents in a collection"""
    collection = db[f'{mongo_collection}']
    return collection.find()
