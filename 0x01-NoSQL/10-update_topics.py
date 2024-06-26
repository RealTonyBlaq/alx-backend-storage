#!/usr/bin/env python3
""" Using MongoDB """

def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name """
    mongo_collection.update_many(
        filter={'name': name},
        update={'$set': {'topics': topics}})
