#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


client = MongoClient()
logs = client.logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print('{} logs'.format(logs.count_documents()))
print('Methods:')

for method in methods:
    print('\tmethod {method}: {logs.count_documents({'method': method})}'.for)

print(f'{logs.count_documents({'method': 'GET', 'path': '/status'})} status check')
