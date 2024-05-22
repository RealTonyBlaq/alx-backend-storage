#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


client = MongoClient()
logs = client.logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print('{} logs'.format(logs.count_documents()))
print('Methods:')
for methos in methods:
    
