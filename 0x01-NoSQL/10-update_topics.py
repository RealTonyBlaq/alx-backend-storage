#!/usr/bin/env python3
""" Using MongoDB """

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name """
    mongo_collection.update_many({'name': name}, )
    client = MongoClient()
    coll = client.my_db.school
    coll.update_many()
