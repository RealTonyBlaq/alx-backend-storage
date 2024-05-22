#!/usr/bin/env python3
""" Using MongoDB """


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic """
    return [top for top in mongo_collection.find({"topics": topic})]
