#!/usr/bin/env python3
""" Using MongoDB """

def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    students = mongo_collection.find()
    for student in students:
        for topic in student['topics']:
            
