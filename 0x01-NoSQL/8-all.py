#!/usr/bin/env python3
""" Using MongoDB """

def list_all(mongo_collection):
    """ function that lists all documents in a collection """
    result = mongo_collection.find()
    if not result:
        return []
    
