#!/usr/bin/env python3
""" Using MongoDB """

def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    docs = mongo_collection.find()
