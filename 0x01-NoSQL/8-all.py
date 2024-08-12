#!/usr/bin/env python3
"""
Module that lists all documents in a collection
"""
from typing import List


def list_all(mongo_collection) -> List:
    """
    Lists all documents in a collection
    """
    return list(mongo_collection.find())


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
