#!/usr/bin/env python3
""" Using MongoDB """


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic """
    return [mongo_collection.find({"topic": {'$in': [topic]}})
