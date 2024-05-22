#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


client = MongoClient()
logs = client.logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print('{} logs'.format(logs.estimated_document_count()))
print('Methods:')

for method in methods:
    print('    method {}: {}'.format(
        method,
        logs.count_documents(filter={'method': method})))

print('{} status check'.format(logs.count_documents(filter={
    'method': 'GET',
    'path': '/status'})))
